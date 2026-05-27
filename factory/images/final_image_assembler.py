"""Final image assembler for DeadZone Factory.

Assembles the complete fastboot image folder: output/images/final/

Rules
-----
- Copies final super.img (rebuilt by super_rebuilder).
- Copies all standalone firmware images from source.
- Excludes dynamic partition images (system.img, vendor.img, etc.)
  — those are packed inside super.img and must not appear as separate files.
- Applies patched image overrides (vbmeta, boot, etc.) if supplied.
- No temporary work files, no split super chunks, no runner paths.

Also writes output/reports/rom_intake_report.txt as the comprehensive
end-to-end summary of the full ROM intake and build pipeline.
"""
from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional


DYNAMIC_PARTITION_IMAGES: frozenset[str] = frozenset({
    "system.img",
    "system_ext.img",
    "product.img",
    "vendor.img",
    "odm.img",
    "mi_ext.img",
    "vendor_dlkm.img",
    "odm_dlkm.img",
    "system_dlkm.img",
})


def assemble_final_images(
    super_img: Path,
    source_images_dir: Path,
    final_dir: Path,
    patched_images: Optional[dict[str, Path]] = None,
    execute: bool = False,
) -> dict:
    """Assemble the final fastboot image folder.

    Parameters
    ----------
    super_img:
        Path to the rebuilt super.img.
    source_images_dir:
        Directory containing collected standalone images from source ROM.
    final_dir:
        Destination: output/images/final/
    patched_images:
        {filename: path} — patched images that override source equivalents.
    execute:
        False → dry-run. True → copy files.

    Returns
    -------
    dict with assembled image list and status.
    """
    super_img = Path(super_img)
    source_images_dir = Path(source_images_dir)
    final_dir = Path(final_dir)
    patched_images = patched_images or {}

    standalone_to_copy: dict[str, Path] = {}
    excluded_dynamic: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    # Collect standalone images, excluding dynamic partitions and bare super.img
    if source_images_dir.is_dir():
        for img in sorted(source_images_dir.rglob("*.img")):
            if not img.is_file():
                continue
            name_lower = img.name.lower()
            if name_lower in DYNAMIC_PARTITION_IMAGES:
                excluded_dynamic.append(img.name)
                continue
            if name_lower == "super.img":
                continue  # will be placed from rebuilt super_img path
            standalone_to_copy[name_lower] = img

    # Apply patched overrides
    for fname, ppath in patched_images.items():
        key = fname.lower()
        if key in DYNAMIC_PARTITION_IMAGES:
            warnings.append(f"Patched image {fname} is a dynamic partition — excluded from final")
            continue
        ppath = Path(ppath)
        if ppath.is_file():
            standalone_to_copy[key] = ppath
        else:
            warnings.append(f"Patched image not found: {ppath}")

    if not super_img.is_file():
        errors.append(f"super.img not found at {super_img} — final assembly cannot proceed")

    result = {
        "status": "DRY_RUN" if not execute else "FAILED",
        "final_dir": str(final_dir),
        "super_img_source": str(super_img),
        "standalone_to_copy": {k: str(v) for k, v in standalone_to_copy.items()},
        "excluded_dynamic": excluded_dynamic,
        "warnings": warnings,
        "errors": errors,
    }

    if not execute:
        return result

    if errors:
        result["status"] = "FAILED"
        return result

    final_dir.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []

    # Place super.img
    target_super = final_dir / "super.img"
    try:
        shutil.copy2(super_img, target_super)
        copied.append("super.img")
        print(f"[final_assembler] super.img → {target_super}")
    except Exception as exc:
        errors.append(f"copy super.img: {exc}")

    # Copy standalone images
    for _key, src in standalone_to_copy.items():
        target = final_dir / src.name
        try:
            shutil.copy2(src, target)
            copied.append(src.name)
        except Exception as exc:
            errors.append(f"copy {src.name}: {exc}")

    result["copied"] = copied
    result["final_manifest"] = sorted(
        p.name for p in final_dir.glob("*.img") if p.is_file()
    )
    result["status"] = "FAILED" if errors else "APPLIED"
    result["errors"] = errors
    return result


def write_intake_report(
    reports_dir: Path,
    rom_url_or_path: str,
    detected_format: str,
    detected_codename: Optional[str],
    selected_codename: str,
    codename_match: bool,
    detected_android_version: Optional[str],
    detected_miui_hyper_version: Optional[str],
    detected_region: Optional[str],
    found_images_count: int,
    found_dynamic_count: int,
    original_super_exists: bool,
    split_super_merged: bool,
    super_rebuilt: bool,
    final_image_list: list[str],
    cleanup_status: str,
    extra_notes: Optional[list[str]] = None,
) -> Path:
    """Write output/reports/rom_intake_report.txt.

    Comprehensive summary of the full ROM intake and build pipeline.
    Returns the path to the written report.
    """
    reports_dir = Path(reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "rom_intake_report.txt"

    match_label = "MATCH" if codename_match else "MISMATCH — build may be unsafe"

    lines = [
        "═══════════════════════════════════════════════════════",
        "  DeadZone Factory — ROM Intake Report",
        f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "═══════════════════════════════════════════════════════",
        "",
        "  Input",
        "  ─────",
        f"  ROM source             : {rom_url_or_path}",
        f"  Detected ROM format    : {detected_format}",
        "",
        "  Device",
        "  ──────",
        f"  Detected codename      : {detected_codename or '(unknown)'}",
        f"  Selected codename      : {selected_codename}",
        f"  Device match status    : {match_label}",
        "",
        "  Version",
        "  ───────",
        f"  Detected Android ver   : {detected_android_version or '(unknown)'}",
        f"  Detected HyperOS/MIUI  : {detected_miui_hyper_version or '(unknown)'}",
        f"  Detected region        : {detected_region or '(unknown)'}",
        "",
        "  Images",
        "  ──────",
        f"  Found images count     : {found_images_count}",
        f"  Found dynamic parts    : {found_dynamic_count}",
        f"  Original super.img     : {'yes' if original_super_exists else 'no'}",
        f"  Split super merged     : {'yes' if split_super_merged else 'no'}",
        f"  Final super rebuilt    : {'yes' if super_rebuilt else 'no'}",
        "",
        f"  Final image list ({len(final_image_list)}):",
    ]
    for img in sorted(final_image_list):
        lines.append(f"    {img}")
    if not final_image_list:
        lines.append("    (none)")

    lines += [
        "",
        "  Cleanup",
        "  ───────",
        f"  Cleanup status         : {cleanup_status}",
    ]

    if extra_notes:
        lines += ["", "  Notes:", "  ──────"]
        for note in extra_notes:
            lines.append(f"    {note}")

    lines.append("═══════════════════════════════════════════════════════")
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[final_assembler] ROM intake report: {path}")
    return path
