"""
Post-extraction partition and boot-image scanning.

After super.img (or payload.bin) has been unpacked, this module inspects the
project_dir to discover:
  - extracted partition directories  (system/, vendor/, product/, …)
  - standalone boot-class images     (boot.img, init_boot.img, dtbo.img, …)

None of the functions here modify any files.
"""
from __future__ import annotations

from pathlib import Path

# Dynamic partitions that live inside super.img (slot _a suffix stripped).
# Order matches what MEZOBuildRom.py recognises.
_DYNAMIC_PARTITION_NAMES = frozenset({
    "system",
    "system_ext",
    "system_dlkm",
    "vendor",
    "vendor_dlkm",
    "product",
    "odm",
    "mi_ext",
})

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

    Searches one level deep plus the top level — mirrors where fastboot-
    flashable images typically live inside a ROM ZIP.
    """
    found: set[str] = set()
    _scan_dir_for_boot_images(rom_extract_dir, found)
    # Also check one level of sub-directories (e.g. images/ sub-folder in some ROMs)
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
