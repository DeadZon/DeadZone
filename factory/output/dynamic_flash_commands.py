"""Generate fastboot flash command lines from actual images in a directory.

Used by deadzone_template_patcher to produce platform-specific command blocks.
Images are collected via the shared _collect_flash_commands logic which applies
all skip/ordering rules (super last, forbidden list, dynamic partition exclusion).
"""
from __future__ import annotations

from pathlib import Path

from .flash_scripts import (
    _DYNAMIC_PARTITION_IMAGES,
    _NEVER_FLASH_IMAGES,
    _collect_flash_commands,
    _should_skip_flash_image,
)


def collect_commands(images_dir: Path) -> list[tuple[str, str]]:
    """Return (partition, image_filename) pairs from actual .img files in images_dir."""
    return _collect_flash_commands(Path(images_dir))


def bat_flash_lines(commands: list[tuple[str, str]]) -> list[str]:
    """Windows BAT flash command block (includes set_active a at start).

    Produces lines like:
        %fastboot% set_active a
        %fastboot% flash boot_ab images\\boot.img
        %fastboot% flash super images\\super.img
    """
    lines = ["%fastboot% set_active a"]
    for partition, image in commands:
        lines.append(f"%fastboot% flash {partition} images\\{image}")
    return lines


def sh_flash_lines(
    commands: list[tuple[str, str]],
    fastboot_var: str = "$fastboot",
) -> list[str]:
    """POSIX SH flash command block (includes set_active a at start).

    Produces lines like:
        $fastboot set_active a
        $fastboot flash boot_ab images/boot.img
        $fastboot flash super images/super.img
    """
    lines = [f"{fastboot_var} set_active a"]
    for partition, image in commands:
        lines.append(f"{fastboot_var} flash {partition} images/{image}")
    return lines


def skipped_images_report(images_dir: Path) -> list[dict]:
    """Return per-image dicts for .img files in images_dir that are NOT flashed.

    Each dict has keys: image (str), reason (str).
    """
    images_dir = Path(images_dir)
    if not images_dir.is_dir():
        return []
    present = {f.name for f in images_dir.iterdir() if f.is_file() and f.suffix == ".img"}
    has_super = "super.img" in present
    included = {img for _, img in _collect_flash_commands(images_dir)}
    result: list[dict] = []
    for name in sorted(present):
        if name in included:
            continue
        lower = name.lower()
        if lower in _NEVER_FLASH_IMAGES:
            reason = "in never-flash list"
        elif lower.startswith("super.img.") or lower.endswith(".chunk"):
            reason = "split super chunk"
        elif "unsparse" in lower:
            reason = "unsparse artifact"
        elif "validation" in lower or "lpdump" in lower:
            reason = "validation/lpdump artifact"
        elif has_super and lower in {n.lower() for n in _DYNAMIC_PARTITION_IMAGES}:
            reason = "dynamic partition (packed into super.img)"
        else:
            reason = "skipped by flash rules"
        result.append({"image": name, "reason": reason})
    return result
