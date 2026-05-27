"""Super image rebuilder for DeadZone Factory.

Rebuilds final super.img from collected dynamic partition images.

Metadata priority
-----------------
1. Original super.img present → read metadata via lpunpack (group name,
   super size, partition allocation sizes, VAB slot layout).
2. No original super.img → use original_partition_sizes from op_list /
   payload manifest (supplied by the pipeline caller).
3. Neither available → fail immediately with a clear error.

Output
------
    output/images/final/super.img
    output/reports/super_rebuild_report.txt

Validation
----------
After lpmake completes:
- Confirm all expected _a-slot partitions exist in LP metadata.
- Confirm every _b slot has size == 0 (VAB invariant).
- Write result to super_rebuild_report.txt.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[2]
_LEGACY_ROOT = _REPO_ROOT / "third_party" / "mezo_core"
_LEGACY_SRC = _LEGACY_ROOT / "src"

if str(_LEGACY_SRC) not in sys.path:
    sys.path.insert(0, str(_LEGACY_SRC))

try:
    from core.lpunpack import get_info as _lpunpack_get_info  # type: ignore
except Exception:
    _lpunpack_get_info = None  # type: ignore

from factory.repack.super_builder_legacy import resolve_lpmake_binary_legacy
from factory.super.super_input_collector import DYNAMIC_PARTITION_NAMES, _DYNAMIC_SET

_LP_METADATA_OVERHEAD: int = 4 * 1024 * 1024


# ── Metadata helpers ──────────────────────────────────────────────────────────

def _base(name: str) -> str:
    if name.endswith("_a") or name.endswith("_b"):
        return name[:-2]
    return name


def read_super_metadata(super_img: Path) -> dict | None:
    """Read LP metadata from super.img using the Python lpunpack library."""
    if _lpunpack_get_info is None:
        return None
    try:
        info = _lpunpack_get_info(str(super_img))
        return info if info else None
    except Exception:
        return None


def extract_partition_sizes_from_metadata(super_info: dict) -> dict[str, int]:
    """Return {base_name: lp_allocation_bytes} from super_info partition_table.

    Skips _b slots (VAB placeholders) and zero-size entries.
    """
    sizes: dict[str, int] = {}
    for item in (super_info.get("partition_table") or []):
        if not isinstance(item, dict):
            continue
        name = str(item.get("name", ""))
        base = _base(name)
        if base not in _DYNAMIC_SET or name.endswith("_b"):
            continue
        try:
            sz = int(item.get("size", 0) or 0)
        except (TypeError, ValueError):
            sz = 0
        if sz > 0:
            sizes[base] = sz
    return sizes


# ── lpmake command construction ───────────────────────────────────────────────

def _build_lpmake_command(
    super_parts_dir: Path,
    output_super: Path,
    super_info: dict,
    original_partition_sizes: dict[str, int],
    lpmake_path: Path | None,
) -> tuple[list[str], list[str], list[str]]:
    """Build the lpmake argument list from LP metadata.

    Returns (command, warnings, errors).
    """
    warnings: list[str] = []
    errors: list[str] = []

    if lpmake_path is None:
        errors.append("lpmake binary not found — cannot build super.img")
        return [], warnings, errors

    if not original_partition_sizes:
        errors.append(
            "original_partition_sizes is empty — cannot preserve partition allocations. "
            "Refusing to fall back to image file sizes."
        )
        return [], warnings, errors

    block_devices = super_info.get("block_devices") or []
    super_size = int(block_devices[0].get("size", 0) or 0) if block_devices else 0
    if super_size <= 0:
        errors.append("super_info has no valid block device size (super_size=0)")
        return [], warnings, errors

    group_table = super_info.get("group_table") or []
    partition_table = super_info.get("partition_table") or []
    metadata_slots = int(super_info.get("metadata_slot_count", 3) or 3)

    part_names_in_meta = [str(p.get("name", "")) for p in partition_table if isinstance(p, dict)]
    is_vab = (
        any(n.endswith("_a") or n.endswith("_b") for n in part_names_in_meta)
        or metadata_slots == 3
    )

    # Determine group names from metadata
    group_base = "qti_dynamic_partitions"
    group_a = ""
    group_b = ""
    for g in group_table:
        if not isinstance(g, dict):
            continue
        gn = str(g.get("name", ""))
        if gn.endswith("_a"):
            group_a = gn
            group_base = gn[:-2]
        elif gn.endswith("_b"):
            group_b = gn
    if not group_a:
        group_a = f"{group_base}_a"
    if not group_b:
        group_b = f"{group_base}_b"

    group_size = max(0, super_size - _LP_METADATA_OVERHEAD)

    # Partitions present in super_parts_dir
    selected = [p for p in DYNAMIC_PARTITION_NAMES if (super_parts_dir / f"{p}.img").is_file()]
    if not selected:
        errors.append(f"No dynamic partition images found in {super_parts_dir}")
        return [], warnings, errors

    cmd = [
        str(lpmake_path),
        "--metadata-size", "65536",
        "--super-name", "super",
        "--metadata-slots", str(3 if is_vab else 2),
        "--device", f"super:{super_size}",
        "--sparse",
        "--group", f"{group_a}:{group_size}",
    ]

    included: list[str] = []
    for part in selected:
        img = super_parts_dir / f"{part}.img"
        img_size = img.stat().st_size
        if part not in original_partition_sizes:
            errors.append(
                f"original_partition_sizes missing for '{part}' — cannot determine "
                f"LP allocation. Refusing to use image file size as fallback."
            )
            continue
        alloc = original_partition_sizes[part]
        if img_size > alloc:
            errors.append(
                f"{part}.img ({img_size} bytes) exceeds original LP allocation ({alloc} bytes)"
            )
            continue
        cmd += [
            "--partition", f"{part}_a:readonly:{alloc}:{group_a}",
            "--image", f"{part}_a={img}",
        ]
        included.append(part)

    if is_vab:
        cmd += ["--group", f"{group_b}:{group_size}"]
        for part in included:
            cmd += ["--partition", f"{part}_b:readonly:0:{group_b}"]
        cmd += ["--virtual-ab"]

    cmd += ["--out", str(output_super)]
    return cmd, warnings, errors


# ── LP validation ─────────────────────────────────────────────────────────────

def _validate_super(
    super_img: Path,
    expected_sizes: dict[str, int],
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "status": "SKIPPED",
        "partitions_found": [],
        "missing_partitions": [],
        "vab_b_slots_are_zero_size": False,
        "warnings": [],
        "errors": [],
    }

    if _lpunpack_get_info is None:
        result["warnings"].append("lpunpack not available — skipping LP metadata validation")
        return result

    try:
        info = _lpunpack_get_info(str(super_img))
        if not info:
            result["errors"].append("lpunpack returned empty result — super.img may be corrupt")
            result["status"] = "FAILED"
            return result

        partition_table = info.get("partition_table") or []
        all_parts: dict[str, int] = {
            str(p.get("name", "")): int(p.get("size", 0) or 0)
            for p in partition_table if isinstance(p, dict)
        }
        result["partitions_found"] = sorted(all_parts.keys())

        val_errors: list[str] = []
        for base, expected_alloc in expected_sizes.items():
            a_name = f"{base}_a"
            if a_name not in all_parts:
                val_errors.append(f"Missing _a slot in final super: {a_name}")
            elif all_parts[a_name] != expected_alloc:
                val_errors.append(
                    f"{a_name} allocation {all_parts[a_name]} != expected {expected_alloc}"
                )

        b_invalid = [
            f"{base}_b"
            for base in expected_sizes
            if f"{base}_b" in all_parts and all_parts[f"{base}_b"] != 0
        ]
        b_missing = [
            f"{base}_b"
            for base in expected_sizes
            if f"{base}_b" not in all_parts
        ]
        result["vab_b_slots_are_zero_size"] = not b_invalid and not b_missing
        if b_invalid:
            val_errors.append(f"_b slots with non-zero size (must be 0 for VAB): {b_invalid}")
        if b_missing:
            val_errors.append(f"Missing _b slot entries: {b_missing}")

        result["missing_partitions"] = [e for e in val_errors if "Missing _a" in e]
        result["errors"] = val_errors
        result["status"] = "PASSED" if not val_errors else "FAILED"

    except Exception as exc:
        result["errors"].append(f"lpunpack validation exception: {exc}")
        result["status"] = "FAILED"

    return result


# ── Public API ─────────────────────────────────────────────────────────────────

def rebuild_super(
    super_parts_dir: Path,
    output_super: Path,
    reports_dir: Path,
    original_super_img: Path | None = None,
    original_partition_sizes: dict[str, int] | None = None,
    execute: bool = False,
) -> dict[str, Any]:
    """Rebuild final super.img from collected dynamic partition images.

    Parameters
    ----------
    super_parts_dir:
        Directory containing base-named partition images (e.g. system.img).
    output_super:
        Destination path for the rebuilt super.img.
    reports_dir:
        Where super_rebuild_report.txt is written.
    original_super_img:
        Original super.img to read LP metadata from (preferred).
    original_partition_sizes:
        {base_name: lp_allocation_bytes} — used when no original super.img.
    execute:
        False → dry-run (command built but not executed).
    """
    super_parts_dir = Path(super_parts_dir)
    output_super = Path(output_super)
    reports_dir = Path(reports_dir)

    result: dict[str, Any] = {
        "status": "DRY_RUN" if not execute else "FAILED",
        "super_parts_dir": str(super_parts_dir),
        "output_super": str(output_super),
        "original_super_img": str(original_super_img) if original_super_img else None,
        "super_metadata_source": None,
        "lpmake_command": [],
        "lpmake_executed": False,
        "lpmake_return_code": None,
        "super_img_created": False,
        "super_img_size": None,
        "validation_status": "NOT_RUN",
        "vab_b_slots_valid": False,
        "partitions_in_final": [],
        "missing_partitions": [],
        "warnings": [],
        "errors": [],
    }

    # ── Load super metadata ───────────────────────────────────────────────────
    super_info: dict[str, Any] = {}

    if original_super_img and original_super_img.is_file():
        meta = read_super_metadata(original_super_img)
        if meta:
            super_info = meta
            result["super_metadata_source"] = "original_super_img"
            if not original_partition_sizes:
                original_partition_sizes = extract_partition_sizes_from_metadata(super_info)
                if original_partition_sizes:
                    result["warnings"].append(
                        f"Extracted partition sizes from original super.img metadata: "
                        f"{list(original_partition_sizes.keys())}"
                    )
        else:
            result["warnings"].append(
                f"Could not read LP metadata from original super.img: {original_super_img}. "
                f"Falling back to original_partition_sizes if provided."
            )

    if not super_info and original_partition_sizes:
        total = sum(original_partition_sizes.values())
        super_size = max(total * 2, 9 * 1024 * 1024 * 1024)
        result["warnings"].append(
            f"No original super.img — estimating super size: {super_size} bytes"
        )
        super_info = {
            "block_devices": [{"name": "super", "size": super_size}],
            "group_table": [
                {"name": "qti_dynamic_partitions_a"},
                {"name": "qti_dynamic_partitions_b"},
            ],
            "partition_table": (
                [
                    {"name": f"{p}_a", "size": s, "group_name": "qti_dynamic_partitions_a", "attributes": 1}
                    for p, s in original_partition_sizes.items()
                ] + [
                    {"name": f"{p}_b", "size": 0, "group_name": "qti_dynamic_partitions_b", "attributes": 1}
                    for p in original_partition_sizes
                ]
            ),
            "metadata_slot_count": 3,
        }
        result["super_metadata_source"] = "derived_from_partition_sizes"

    if not super_info:
        result["errors"].append(
            "Cannot rebuild super.img: no original super.img and no "
            "original_partition_sizes provided."
        )
        _write_report(result, reports_dir)
        return result

    if not original_partition_sizes:
        result["errors"].append(
            "original_partition_sizes is empty — cannot build super.img safely."
        )
        _write_report(result, reports_dir)
        return result

    lpmake_path = resolve_lpmake_binary_legacy()
    cmd, cmd_warnings, cmd_errors = _build_lpmake_command(
        super_parts_dir, output_super, super_info,
        original_partition_sizes, lpmake_path,
    )
    result["warnings"].extend(cmd_warnings)
    result["errors"].extend(cmd_errors)
    result["lpmake_command"] = cmd

    if not execute:
        result["status"] = "DRY_RUN" if not cmd_errors else "FAILED"
        _write_report(result, reports_dir)
        return result

    if cmd_errors or not cmd:
        result["status"] = "FAILED"
        _write_report(result, reports_dir)
        return result

    # ── Run lpmake ────────────────────────────────────────────────────────────
    output_super.parent.mkdir(parents=True, exist_ok=True)
    if output_super.exists():
        output_super.unlink()

    print(f"[super_rebuilder] running lpmake → {output_super}")
    try:
        proc = subprocess.run(
            cmd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0,
        )
        result["lpmake_executed"] = True
        result["lpmake_return_code"] = proc.returncode
        output_txt = proc.stdout.decode("utf-8", errors="replace")
        if proc.returncode != 0:
            result["errors"].append(f"lpmake exited with code {proc.returncode}: {output_txt}")
    except FileNotFoundError as exc:
        result["lpmake_executed"] = True
        result["lpmake_return_code"] = 2
        result["errors"].append(f"lpmake not found: {exc}")

    result["super_img_created"] = output_super.is_file()
    if result["super_img_created"]:
        result["super_img_size"] = output_super.stat().st_size
        print(f"[super_rebuilder] super.img: {result['super_img_size']} bytes")
    else:
        result["errors"].append("lpmake did not produce super.img")
        _write_report(result, reports_dir)
        return result

    # ── Validate ──────────────────────────────────────────────────────────────
    validation = _validate_super(output_super, original_partition_sizes)
    result["validation_status"] = validation["status"]
    result["vab_b_slots_valid"] = validation.get("vab_b_slots_are_zero_size", False)
    result["partitions_in_final"] = validation.get("partitions_found", [])
    result["missing_partitions"] = validation.get("missing_partitions", [])
    result["warnings"].extend(validation.get("warnings", []))
    result["errors"].extend(validation.get("errors", []))

    result["status"] = "FAILED" if result["errors"] else "APPLIED"
    _write_report(result, reports_dir)
    return result


def _write_report(result: dict, reports_dir: Path) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "super_rebuild_report.txt"

    cmd = result.get("lpmake_command") or []
    warnings = result.get("warnings") or []
    errors = result.get("errors") or []

    lines = [
        "═══════════════════════════════════════════════════════",
        "  DeadZone Factory — Super Rebuild Report",
        "═══════════════════════════════════════════════════════",
        f"  Status                 : {result.get('status')}",
        f"  Metadata source        : {result.get('super_metadata_source') or '(none)'}",
        f"  super.img created      : {result.get('super_img_created')}",
        f"  super.img size         : {result.get('super_img_size')}",
        f"  lpmake executed        : {result.get('lpmake_executed')}",
        f"  lpmake return code     : {result.get('lpmake_return_code')}",
        f"  Validation status      : {result.get('validation_status')}",
        f"  VAB _b slots valid     : {result.get('vab_b_slots_valid')}",
        "",
        "  Partitions in final super:",
    ]
    for p in sorted(result.get("partitions_in_final") or []):
        lines.append(f"    {p}")
    if not result.get("partitions_in_final"):
        lines.append("    (none)")

    missing = result.get("missing_partitions") or []
    lines += [f"", f"  Missing partitions ({len(missing)}):"]
    for m in missing:
        lines.append(f"    {m}")
    if not missing:
        lines.append("    (none)")

    lines += ["", "  lpmake command:"]
    lines.append("    " + " ".join(str(t) for t in cmd) if cmd else "    (none)")

    lines += [f"", f"  Warnings ({len(warnings)}):"]
    for w in warnings:
        lines.append(f"    {w}")

    lines += [f"", f"  Errors ({len(errors)}):"]
    for e in errors:
        lines.append(f"    {e}")
    if not errors:
        lines.append("    (none)")

    lines.append("═══════════════════════════════════════════════════════")
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[super_rebuilder] Report: {path}")
