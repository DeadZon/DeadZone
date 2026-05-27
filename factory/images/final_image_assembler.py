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

from factory.images.source_image_manifest import build_source_image_manifest


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
    skipped_images: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    work_root = source_images_dir.parent
    manifest = build_source_image_manifest(
        source_roots=[source_images_dir],
        work_root=work_root,
        final_super_path=super_img if super_img.is_file() else None,
    )

    split_super_parts: list[Path] = []
    for entry in manifest.get("images", []):
        name = str(entry.get("name", ""))
        name_lower = name.lower()
        role = entry.get("role")
        if entry.get("include_in_final") and role != "super":
            standalone_to_copy[name_lower] = Path(entry["path"])
        elif role == "dynamic_partition":
            excluded_dynamic.append(name)
        elif role == "split_super":
            split_super_parts.append(Path(entry["path"]))
            skipped_images.append(name)
        elif role in {"validation", "temp"}:
            skipped_images.append(name)

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

    can_merge_split_super = bool(split_super_parts)
    if not super_img.is_file() and not can_merge_split_super:
        errors.append(f"super.img not found at {super_img} - final assembly cannot proceed")

    result = {
        "status": "DRY_RUN" if not execute else "FAILED",
        "final_dir": str(final_dir),
        "super_img_source": str(super_img),
        "standalone_to_copy": {k: str(v) for k, v in standalone_to_copy.items()},
        "excluded_dynamic": excluded_dynamic,
        "skipped_images": skipped_images,
        "source_image_manifest": manifest,
        "warnings": warnings,
        "errors": errors,
        "final_images": [],
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
        if super_img.is_file() and super_img.resolve() == target_super.resolve():
            # Already in final dir (preserve_original_super strategy placed it here)
            copied.append("super.img")
            warnings.append(
                "super.img already present; keeping final super (same-file skip)"
            )
            print(
                f"[final_assembler] super.img already in final dir (same-file); skipping copy"
            )
        elif super_img.is_file():
            shutil.copy2(super_img, target_super)
            copied.append("super.img")
            print(f"[final_assembler] super.img → {target_super}")
        elif can_merge_split_super:
            _merge_split_super_chunks(split_super_parts, target_super)
            copied.append("super.img")
            warnings.append("split super chunks merged into final super.img")
    except Exception as exc:
        errors.append(f"copy super.img: {exc}")

    # Copy standalone images
    for _key, src in standalone_to_copy.items():
        target = final_dir / src.name
        try:
            if src.resolve() == target.resolve():
                copied.append(src.name)
                warnings.append(f"{src.name} already in final dir; skipping same-file copy")
            else:
                shutil.copy2(src, target)
                copied.append(src.name)
        except Exception as exc:
            errors.append(f"copy {src.name}: {exc}")

    result["copied"] = copied
    result["final_manifest"] = sorted(
        p.name for p in final_dir.glob("*.img") if p.is_file()
    )
    result["final_images"] = result["final_manifest"]
    result["exactly_one_super_img"] = _exactly_one_super(final_dir)
    result["status"] = "FAILED" if errors else "APPLIED"
    result["errors"] = errors
    result["warnings"] = warnings
    _write_final_image_manifest(final_dir, result, manifest)
    return result


def _natural_key(path: Path) -> list:
    import re

    return [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)", path.name)]


def _merge_split_super_chunks(parts: list[Path], target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as dst:
        for part in sorted(parts, key=_natural_key):
            with part.open("rb") as src:
                shutil.copyfileobj(src, dst, length=1024 * 1024)


def _is_super_variant(path: Path) -> bool:
    name = path.name.lower()
    return (
        name == "super.img"
        or name.startswith("super.img.")
        or name.endswith(".unsparse.img")
        or (name.startswith("super_") and name.endswith(".chunk"))
    )


def _exactly_one_super(final_dir: Path) -> bool:
    variants = sorted(p.name for p in final_dir.iterdir() if p.is_file() and _is_super_variant(p))
    return variants == ["super.img"]


def _write_final_image_manifest(final_dir: Path, result: dict, source_manifest: dict) -> None:
    import json

    reports_dir = final_dir.parents[1] / "reports" if len(final_dir.parents) > 1 else final_dir.parent / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    images = [
        {"name": path.name, "path": str(path), "size_bytes": path.stat().st_size}
        for path in sorted(final_dir.glob("*.img"))
        if path.is_file()
    ]
    payload = {
        "final_dir": str(final_dir),
        "final_image_count": len(images),
        "included_images": [image["name"] for image in images],
        "images": images,
        "skipped_duplicate_super_images": [
            e["name"] for e in source_manifest.get("images", [])
            if e.get("role") in {"super", "split_super"} and not e.get("include_in_final")
        ],
        "skipped_dynamic_temp_images": [
            e["name"] for e in source_manifest.get("images", [])
            if e.get("role") in {"dynamic_partition", "validation", "temp"}
        ],
        "exactly_one_super_img": result.get("exactly_one_super_img", False),
    }
    (reports_dir / "final_image_manifest.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


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
