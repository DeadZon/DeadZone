"""
Post-extraction partition and boot-image scanning, plus dynamic-partition
extraction from a payload_extracted directory.

After super.img (or payload.bin) has been unpacked, this module:
  - inspects project_dir for extracted partition directories
  - scans rom_extract_dir for standalone boot-class images
  - extracts dynamic partition .img files produced by payload extraction
    into project_dir using MEZOBuildRom.extract_single_partition
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

# Dynamic partitions that live inside super.img (slot _a suffix stripped).
_DYNAMIC_PARTITION_NAMES = frozenset({
    "system",
    "system_ext",
    "system_dlkm",
    "vendor",
    "vendor_dlkm",
    "product",
    "odm",
    "odm_dlkm",
    "mi_ext",
})

# Ordered list of dynamic partition images expected from payload extraction.
# odm_dlkm is included; the Usagi reference missed it but DeadZone requires it.
_DYNAMIC_PARTITION_IMGS = [
    "mi_ext.img",
    "odm.img",
    "odm_dlkm.img",
    "product.img",
    "system.img",
    "system_dlkm.img",
    "system_ext.img",
    "vendor.img",
    "vendor_dlkm.img",
]

# Standalone flash images that sit alongside the ROM ZIP (never inside super).
_BOOT_IMAGE_NAMES = frozenset({
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "recovery.img",
    "dtbo.img",
    "vbmeta.img",
    "vbmeta_system.img",
    "vbmeta_vendor.img",
    "super_empty.img",
    "cust.img",
    "preloader.img",
    "lk.img",
    "logo.img",
    "persist.img",
    "tee.img",
})


def collect_extracted_partitions(project_dir: Path) -> list[str]:
    """
    Return names of dynamic partitions that were successfully extracted into
    project_dir.  A partition is considered extracted when a sub-directory
    with its name exists (e.g., project_dir/system/).
    """
    found: list[str] = []
    for name in sorted(_DYNAMIC_PARTITION_NAMES):
        if (project_dir / name).is_dir():
            found.append(name)
    return found


def collect_boot_images(rom_extract_dir: Path) -> list[str]:
    """
    Return filenames of standalone boot-class images found under
    rom_extract_dir (the directory where the ROM archive was unpacked).

    Searches one level deep plus the top level.
    """
    found: set[str] = set()
    _scan_dir_for_boot_images(rom_extract_dir, found)
    try:
        for child in rom_extract_dir.iterdir():
            if child.is_dir():
                _scan_dir_for_boot_images(child, found)
    except Exception:
        pass
    return sorted(found)


def _scan_dir_for_boot_images(directory: Path, result: set[str]) -> None:
    try:
        for entry in directory.iterdir():
            if entry.is_file() and entry.name.lower() in _BOOT_IMAGE_NAMES:
                result.add(entry.name)
    except Exception:
        pass


def _remove_force(path: Path) -> None:
    try:
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
        else:
            path.unlink(missing_ok=True)
    except Exception:
        pass


def _write_parts_info(config_dir: Path, parts_info: dict[str, str]) -> None:
    """Merge parts_info into config_dir/parts_info (JSON)."""
    parts_info_path = config_dir / "parts_info"
    existing: dict = {}
    try:
        if parts_info_path.exists():
            existing = json.loads(parts_info_path.read_text(encoding="utf-8"))
    except Exception:
        existing = {}
    if isinstance(existing, dict):
        existing.update(parts_info)
    else:
        existing = dict(parts_info)
    parts_info_path.write_text(
        json.dumps(existing, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def extract_dynamic_partitions_from_payload_dir(
    payload_out_dir: Path,
    project_dir: Path,
) -> dict[str, str]:
    """
    For each expected dynamic partition image found in *payload_out_dir*,
    move it to *project_dir* and extract it via MEZOBuildRom.extract_single_partition.

    That function handles:
      - filesystem type detection (ext / erofs / sparse)
      - sparse-to-raw conversion (simg2img)
      - directory extraction (Extractor / extract.erofs / fsck.erofs)
      - fs_config and file_contexts generation (fspatch / contextpatch)

    After extraction the .img file is removed from project_dir (consistent with
    the legacy MEZOBuildRom behaviour).

    Returns parts_info: {partition_name: fs_type} for every successfully
    extracted partition.  Also persists parts_info to project_dir/config/parts_info.
    """
    from factory.unpack.payload import _legacy  # lazy-import helper

    legacy = _legacy()
    config_dir = project_dir / "config"
    config_dir.mkdir(parents=True, exist_ok=True)

    parts_info: dict[str, str] = {}

    for img_name in _DYNAMIC_PARTITION_IMGS:
        src_img = payload_out_dir / img_name
        if not src_img.is_file():
            continue

        dst_img = project_dir / img_name
        try:
            if dst_img.exists():
                _remove_force(dst_img)
            shutil.move(str(src_img), str(dst_img))
            print(f"[partitions] Extracting {img_name} …")
            legacy.extract_single_partition(dst_img, project_dir, parts_info)
        except Exception as exc:
            print(f"[partitions] ERROR extracting {img_name}: {exc}")
        finally:
            if dst_img.exists():
                _remove_force(dst_img)

    if parts_info:
        _write_parts_info(config_dir, parts_info)

    return parts_info
