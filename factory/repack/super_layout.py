"""Super partition layout capture, reporting, and validation.

Responsibilities
----------------
1. Extract per-partition LP allocation sizes from super_info partition_table.
2. Write output/reports/original_super_layout.json at unpack time.
3. Read original_super_layout.json at build time to supply correct sizes to lpmake.
4. Write output/reports/final_super_layout.json after super.img is built.
5. Compare original vs final per-partition allocation sizes; fail on any mismatch.

Critical rules
--------------
- Only the 9 listed dynamic partitions are allowed inside super.img.
- The LP allocation size for each partition must equal the original exactly.
- Image file size on disk may be smaller (sparse/erofs) but allocation must not change.
- If image file size > original allocation: error (cannot fit).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ALLOWED_DYNAMIC_PARTITIONS: list[str] = [
    "system",
    "product",
    "system_ext",
    "vendor",
    "odm",
    "vendor_dlkm",
    "system_dlkm",
    "odm_dlkm",
    "mi_ext",
]

_ALLOWED_SET: frozenset[str] = frozenset(ALLOWED_DYNAMIC_PARTITIONS)

ORIGINAL_LAYOUT_REPORT = "original_super_layout.json"
FINAL_LAYOUT_REPORT = "final_super_layout.json"


def _base_name(name: str) -> str:
    if name.endswith("_a") or name.endswith("_b"):
        return name[:-2]
    return name


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=4, ensure_ascii=False) + "\n", encoding="utf-8")


def _read_json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def extract_original_partition_sizes(super_info: dict[str, Any]) -> dict[str, int]:
    """Return {base_partition_name: lp_allocation_bytes} for allowed _a-slot entries.

    Returns an empty dict if partition_table has no size fields (e.g., payload
    manifest source) — callers must handle this gracefully.
    """
    partition_table = super_info.get("partition_table") or []
    sizes: dict[str, int] = {}
    for item in partition_table:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name", ""))
        base = _base_name(name)
        if base not in _ALLOWED_SET:
            continue
        if name.endswith("_b"):
            continue
        raw = item.get("size")
        if raw is None:
            continue
        try:
            sz = int(raw)
        except (TypeError, ValueError):
            continue
        if sz > 0:
            sizes[base] = sz
    return sizes


def build_original_layout_record(super_info: dict[str, Any]) -> dict[str, Any]:
    """Build the data structure written to original_super_layout.json."""
    partition_table = super_info.get("partition_table") or []
    block_devices = super_info.get("block_devices") or []
    super_size = 0
    if block_devices:
        super_size = int(block_devices[0].get("size", 0) or 0)

    partitions: list[dict[str, Any]] = []
    for item in partition_table:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name", ""))
        if not name:
            continue
        base = _base_name(name)
        if base not in _ALLOWED_SET:
            continue
        slot = "_a" if name.endswith("_a") else ("_b" if name.endswith("_b") else "")
        raw = item.get("size")
        size_bytes = int(raw) if raw is not None else 0
        group = str(item.get("group_name", ""))
        attrs = item.get("attributes")
        if isinstance(attrs, int):
            readonly = bool(attrs & 1)
        else:
            readonly = "readonly" in str(attrs).lower() if attrs else True
        partitions.append({
            "name": name,
            "base_name": base,
            "size_bytes": size_bytes,
            "group": group,
            "readonly": readonly,
            "slot_suffix": slot,
        })

    return {
        "source": super_info.get("_super_info_source", "unknown"),
        "super_size": super_size,
        "partitions": partitions,
    }


def write_original_layout_report(super_info: dict[str, Any], reports_dir: Path) -> Path:
    """Write original_super_layout.json; return the output path."""
    reports_dir = Path(reports_dir)
    record = build_original_layout_record(super_info)
    out_path = reports_dir / ORIGINAL_LAYOUT_REPORT
    _write_json(out_path, record)
    print(f"[super_layout] original_super_layout.json → {out_path}")
    return out_path


def read_original_partition_sizes(reports_dir: Path) -> dict[str, int]:
    """Read original_super_layout.json; return {base_name: size_bytes}.

    Returns empty dict if the file is absent or has no size data.
    """
    path = Path(reports_dir) / ORIGINAL_LAYOUT_REPORT
    data = _read_json(path)
    if not data:
        return {}
    sizes: dict[str, int] = {}
    for p in data.get("partitions", []):
        if p.get("slot_suffix") == "_b":
            continue
        base = p.get("base_name", "")
        sz = p.get("size_bytes", 0)
        if base in _ALLOWED_SET and sz > 0:
            sizes[base] = sz
    return sizes


def compare_layouts(
    original_sizes: dict[str, int],
    final_partition_table: list[dict[str, Any]],
) -> tuple[bool, list[str]]:
    """Compare original and final LP allocation sizes; return (ok, error_messages).

    Every allowed partition in original_sizes must exist in the final metadata
    with the exact same size_bytes.  A 1-byte discrepancy is a build error.
    """
    errors: list[str] = []

    final_sizes: dict[str, int] = {}
    for item in final_partition_table:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name", ""))
        base = _base_name(name)
        if name.endswith("_b") or base not in _ALLOWED_SET:
            continue
        raw = item.get("size")
        if raw is not None:
            try:
                final_sizes[base] = int(raw)
            except (TypeError, ValueError):
                pass

    for base, orig_size in original_sizes.items():
        final_size = final_sizes.get(base)
        if final_size is None:
            errors.append(
                f"ERROR: {base} missing from final super metadata "
                f"(expected size {orig_size} bytes)"
            )
        elif final_size != orig_size:
            errors.append(
                f"ERROR: {base} size changed from {orig_size} to {final_size} bytes"
            )

    return (not errors, errors)


def write_final_layout_report(
    final_super_info: dict[str, Any],
    original_sizes: dict[str, int],
    reports_dir: Path,
) -> tuple[Path, bool, list[str]]:
    """Write final_super_layout.json; return (path, validation_ok, errors)."""
    reports_dir = Path(reports_dir)
    partition_table = final_super_info.get("partition_table") or []
    block_devices = final_super_info.get("block_devices") or []
    super_size = int(block_devices[0].get("size", 0)) if block_devices else 0

    partitions: list[dict[str, Any]] = []
    for item in partition_table:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name", ""))
        base = _base_name(name)
        if base not in _ALLOWED_SET:
            continue
        slot = "_a" if name.endswith("_a") else ("_b" if name.endswith("_b") else "")
        sz = int(item.get("size", 0) or 0)
        partitions.append({
            "name": name,
            "base_name": base,
            "size_bytes": sz,
            "slot_suffix": slot,
        })

    ok, errors = compare_layouts(original_sizes, partition_table)

    record: dict[str, Any] = {
        "super_size": super_size,
        "partitions": partitions,
        "comparison": {
            "original_sizes": original_sizes,
            "passed": ok,
            "errors": errors,
        },
    }
    out_path = reports_dir / FINAL_LAYOUT_REPORT
    _write_json(out_path, record)
    print(f"[super_layout] final_super_layout.json → {out_path}")
    return out_path, ok, errors
