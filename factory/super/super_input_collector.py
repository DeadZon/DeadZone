"""Super partition input collector for DeadZone Factory.

Gathers dynamic partition images from extracted ROM source directories
and prepares them for super.img rebuilding.

Handles VAB layouts:
    _a images → real partition data (copied to super_parts_dir as base-name.img)
    _b images with size 0 → valid VAB metadata placeholder (accepted, not copied)
    _b images with size > 0 → unexpected but treated as placeholder (warning issued)

Output
------
    output/work/super_parts/*.img     — base-named dynamic partition images
    output/reports/super_input_report.txt
"""
from __future__ import annotations

import shutil
from pathlib import Path


DYNAMIC_PARTITION_NAMES: list[str] = [
    "system",
    "system_ext",
    "product",
    "vendor",
    "odm",
    "mi_ext",
    "vendor_dlkm",
    "odm_dlkm",
    "system_dlkm",
]

_DYNAMIC_SET: frozenset[str] = frozenset(DYNAMIC_PARTITION_NAMES)


def _base(name: str) -> str:
    if name.endswith("_a") or name.endswith("_b"):
        return name[:-2]
    return name


def _detect_group_name(source_dirs: list[Path]) -> str | None:
    """Read dynamic_partitions_op_list from source directories to find group name."""
    for src_dir in source_dirs:
        for candidate in [src_dir, src_dir.parent, src_dir.parent.parent]:
            op_list = candidate / "dynamic_partitions_op_list"
            if not op_list.is_file():
                continue
            try:
                for line in op_list.read_text(encoding="utf-8", errors="replace").splitlines():
                    tokens = line.strip().split()
                    if tokens and tokens[0] == "add_group" and len(tokens) >= 2:
                        name = tokens[1]
                        if name == "default":
                            continue
                        return name[:-2] if (name.endswith("_a") or name.endswith("_b")) else name
            except Exception:
                pass
    return None


def collect_super_inputs(
    source_dirs: list[Path],
    super_parts_dir: Path,
    reports_dir: Path,
    execute: bool = False,
) -> dict:
    """Collect dynamic partition images from source directories.

    Parameters
    ----------
    source_dirs:
        Directories to scan for dynamic partition images (searched in order).
    super_parts_dir:
        Destination: output/work/super_parts/
    reports_dir:
        Where super_input_report.txt is written.
    execute:
        False → dry-run. True → copy images to super_parts_dir.

    Returns
    -------
    dict with collected partition info and build status.
    """
    source_dirs = [Path(d) for d in source_dirs]
    super_parts_dir = Path(super_parts_dir)
    reports_dir = Path(reports_dir)

    found_dynamic: dict[str, Path] = {}     # base_name → source path
    vab_b_placeholders: dict[str, Path] = {}
    warnings: list[str] = []
    errors: list[str] = []

    for src_dir in source_dirs:
        if not src_dir.is_dir():
            continue
        for img in sorted(src_dir.rglob("*.img")):
            if not img.is_file():
                continue
            stem = img.stem.lower()
            base = _base(stem)
            if base not in _DYNAMIC_SET:
                continue

            is_b = stem.endswith("_b")
            is_a = stem.endswith("_a")

            if is_b:
                sz = img.stat().st_size
                if sz > 0:
                    warnings.append(
                        f"{img.name}: _b slot has {sz} bytes (expected 0 for VAB); "
                        f"treating as placeholder"
                    )
                vab_b_placeholders.setdefault(base, img)
            elif is_a:
                found_dynamic.setdefault(base, img)
            else:
                found_dynamic.setdefault(base, img)

    missing = [p for p in DYNAMIC_PARTITION_NAMES if p not in found_dynamic]
    if missing:
        warnings.append(f"Dynamic partitions not found in source: {', '.join(missing)}")

    group_name = _detect_group_name(source_dirs)

    result = {
        "status": "DRY_RUN" if not execute else "FAILED",
        "source_dirs": [str(d) for d in source_dirs],
        "super_parts_dir": str(super_parts_dir),
        "found_dynamic_partitions": {k: str(v) for k, v in found_dynamic.items()},
        "vab_b_placeholders": {k: str(v) for k, v in vab_b_placeholders.items()},
        "missing_dynamic_partitions": missing,
        "detected_group_name": group_name,
        "warnings": warnings,
        "errors": errors,
    }

    if not execute:
        _write_report(result, reports_dir)
        return result

    super_parts_dir.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []

    for base_key, src in found_dynamic.items():
        out_name = f"{base_key}.img"
        target = super_parts_dir / out_name
        try:
            shutil.copy2(src, target)
            copied.append(out_name)
        except Exception as exc:
            errors.append(f"copy {src.name} → {out_name}: {exc}")

    result["copied"] = copied
    result["status"] = "FAILED" if errors else "APPLIED"
    result["errors"] = errors
    _write_report(result, reports_dir)
    return result


def _write_report(result: dict, reports_dir: Path) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "super_input_report.txt"

    found = result.get("found_dynamic_partitions") or {}
    placeholders = result.get("vab_b_placeholders") or {}
    missing = result.get("missing_dynamic_partitions") or []
    warnings = result.get("warnings") or []
    errors = result.get("errors") or []

    lines = [
        "═══════════════════════════════════════════════════════",
        "  DeadZone Factory — Super Input Collector Report",
        "═══════════════════════════════════════════════════════",
        f"  Status                 : {result.get('status')}",
        f"  Detected group name    : {result.get('detected_group_name') or '(unknown)'}",
        f"  super_parts_dir        : {result.get('super_parts_dir')}",
        "",
        f"  Found dynamic partitions ({len(found)}):",
    ]
    for name, pth in sorted(found.items()):
        lines.append(f"    {name:20s}: {pth}")
    if not found:
        lines.append("    (none)")

    lines += [f"", f"  VAB _b placeholders ({len(placeholders)}):"]
    for name, pth in sorted(placeholders.items()):
        lines.append(f"    {name:20s}: {pth}")
    if not placeholders:
        lines.append("    (none)")

    lines += [f"", f"  Missing partitions ({len(missing)}):"]
    for m in missing:
        lines.append(f"    {m}")
    if not missing:
        lines.append("    (none)")

    lines += [f"", f"  Warnings ({len(warnings)}):"]
    for w in warnings:
        lines.append(f"    {w}")

    lines += [f"", f"  Errors ({len(errors)}):"]
    for e in errors:
        lines.append(f"    {e}")

    lines.append("═══════════════════════════════════════════════════════")
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[super_input_collector] Report: {path}")
