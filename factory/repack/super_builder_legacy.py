"""Legacy-compatible lpmake super image builder."""
from __future__ import annotations

import os
import platform
import shutil
import stat
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
    from core.utils import gettype  # type: ignore
except Exception:  # pragma: no cover - fallback keeps dry-runs usable
    gettype = None  # type: ignore

KNOWN_PARTITIONS = [
    "system",
    "product",
    "system_ext",
    "vendor",
    "vendor_dlkm",
    "system_dlkm",
    "odm",
    "mi_ext",
]


def _default_root_dir(root_dir: Path | None = None) -> Path:
    return Path(root_dir).resolve() if root_dir is not None else _LEGACY_ROOT.resolve()


def _try_existing(path: Path) -> Path | None:
    if not path.exists():
        return None
    if os.name == "posix" and not os.access(str(path), os.X_OK):
        try:
            path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        except Exception:
            pass
    return path


def resolve_lpmake_binary_legacy(root_dir: Path | None = None) -> Path | None:
    """Resolve lpmake with the legacy tool search order."""
    root_dir = _default_root_dir(root_dir)
    tool_name = "lpmake.exe" if os.name == "nt" else "lpmake"
    candidates = [
        Path("lpmake"),
        root_dir / "bin" / platform.system() / platform.machine() / "lpmake",
        root_dir / "bin" / platform.system() / platform.machine() / tool_name,
        root_dir / "bin" / "lpmake",
        root_dir / "bin" / tool_name,
    ]
    for candidate in candidates:
        if candidate.is_absolute() or str(candidate) != "lpmake":
            if found := _try_existing(candidate):
                return found
        elif candidate.exists():
            return candidate
    which_result = shutil.which("lpmake") or shutil.which(tool_name)
    return Path(which_result) if which_result else None


def _base_partition_name(name: str) -> str:
    return name[:-2] if name.endswith("_a") or name.endswith("_b") else name


def _image_for_partition(images_dir: Path, partition_name: str, slot: str | None = "a") -> Path:
    candidates = []
    if slot:
        candidates.append(images_dir / f"{partition_name}_{slot}.img")
    candidates.append(images_dir / f"{partition_name}.img")
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return candidates[0]


def collect_part_names_legacy(
    images_dir: Path,
    super_info: dict[str, Any] | None = None,
) -> list[str]:
    """Collect partition image names from images_dir, ordered like legacy metadata."""
    images_dir = Path(images_dir).resolve()
    found = {
        _base_partition_name(path.stem)
        for path in images_dir.glob("*.img")
        if path.name.lower() != "super.img" and not path.stem.startswith("vbmeta")
    }

    ordered: list[str] = []
    if super_info:
        for item in super_info.get("partition_table", []) or []:
            if not isinstance(item, dict):
                continue
            base = _base_partition_name(str(item.get("name", "")))
            if base in found and base not in ordered:
                ordered.append(base)

    for name in KNOWN_PARTITIONS:
        if name in found and name not in ordered:
            ordered.append(name)
    return ordered


def derive_super_layout_legacy(
    images_dir: Path,
    super_info: dict[str, Any],
) -> dict[str, Any]:
    """Derive the legacy lpmake layout from super_info and images_dir."""
    images_dir = Path(images_dir).resolve()
    block_devices = super_info.get("block_devices", []) or []
    group_table = super_info.get("group_table", []) or []
    partition_table = super_info.get("partition_table", []) or []

    block_device_name = "super"
    super_size = 0
    if block_devices:
        block_device_name = str(block_devices[0].get("name", "super"))
        super_size = int(block_devices[0].get("size", 0) or 0)

    metadata_slot_count = int(super_info.get("metadata_slot_count", 3) or 3)
    partition_names = [str(item.get("name", "")) for item in partition_table if isinstance(item, dict)]
    group_names = [
        str(item.get("name", ""))
        for item in group_table
        if isinstance(item, dict) and item.get("name") != "default"
    ]

    super_type = 2 if any(name.endswith("_a") or name.endswith("_b") for name in partition_names) else 1
    if metadata_slot_count == 3:
        super_type = 2

    group_name = "qti_dynamic_partitions"
    group_a_name = ""
    group_b_name = ""
    for name in group_names:
        if name.endswith("_a"):
            group_a_name = name
            group_name = name[:-2]
        elif name.endswith("_b"):
            group_b_name = name

    if super_type == 1 and group_names:
        group_name = group_names[0]
        group_a_name = group_name
        group_b_name = group_name
    else:
        if not group_a_name:
            group_a_name = f"{group_name}_a"
        if not group_b_name:
            group_b_name = f"{group_name}_b"

    part_names = collect_part_names_legacy(images_dir, super_info)
    selected_parts: list[str] = []
    for name in partition_names:
        base_name = _base_partition_name(name)
        if base_name in part_names and base_name not in selected_parts:
            selected_parts.append(base_name)
    if not selected_parts:
        selected_parts = part_names

    partition_image_sizes = {
        part: _image_for_partition(images_dir, part, "a").stat().st_size
        for part in selected_parts
        if _image_for_partition(images_dir, part, "a").is_file()
    }

    return {
        "block_device_name": block_device_name,
        "super_size": super_size,
        "super_type": super_type,
        "metadata_slot_count": metadata_slot_count,
        "group_name": group_name,
        "group_a_name": group_a_name,
        "group_b_name": group_b_name,
        "group_size": super_size,
        "slot_mode": "vab" if super_type == 2 else "single",
        "virtual_ab": super_type == 2,
        "output_format": super_info.get("output_format") or "sparse",
        "selected_parts": selected_parts,
        "partition_image_sizes": partition_image_sizes,
    }


def can_use_slot_image_legacy(
    partition_name: str,
    image_path: Path,
    slot_mode: str | None = None,
) -> bool:
    """Return whether a slot image can be passed to lpmake."""
    partition_name = partition_name
    slot_mode = slot_mode
    image_path = Path(image_path)
    if not image_path.exists() or not image_path.is_file():
        return False
    if image_path.stat().st_size <= 0:
        return False
    if gettype is None:
        return True
    img_type = gettype(str(image_path))
    return img_type in {"erofs", "ext", "f2fs", "sparse"}


def _build_lpmake_command(
    images_dir: Path,
    output_super: Path,
    super_info: dict[str, Any],
    lpmake_path: Path | None,
) -> tuple[list[str], dict[str, Any], list[str], list[str]]:
    layout = derive_super_layout_legacy(images_dir, super_info)
    warnings: list[str] = []
    errors: list[str] = []
    super_size = int(layout["super_size"] or 0)
    if super_size <= 0:
        errors.append("super_info has no valid block device size")

    command = [
        str(lpmake_path) if lpmake_path else "lpmake",
        "--metadata-size", "65536",
        "-super-name", str(layout["block_device_name"]),
        "-metadata-slots", "3" if layout["super_type"] == 2 else "2",
    ]

    selected_parts = list(layout["selected_parts"])
    if layout["super_type"] == 1:
        command += [
            "-device", f"{layout['block_device_name']}:{super_size}",
            "--group", f"{layout['group_a_name']}:{super_size}",
        ]
        for part_name in selected_parts:
            img_path = _image_for_partition(images_dir, part_name, "a")
            if not img_path.exists():
                errors.append(f"Required image not found for super pack: {img_path}")
                continue
            command += [
                "--partition", f"{part_name}:readonly:{img_path.stat().st_size}:{layout['group_a_name']}",
                "--image", f"{part_name}={img_path}",
            ]
    else:
        command += [
            "-device", f"{layout['block_device_name']}:{super_size}",
            "--group", f"{layout['group_a_name']}:{super_size}",
        ]
        for part_name in selected_parts:
            img_path = _image_for_partition(images_dir, part_name, "a")
            if not img_path.exists():
                errors.append(f"Required _a image not found for super pack: {img_path}")
                continue
            command += [
                "--partition", f"{part_name}_a:readonly:{img_path.stat().st_size}:{layout['group_a_name']}",
                "--image", f"{part_name}_a={img_path}",
            ]
        command += ["--group", f"{layout['group_b_name']}:{super_size}"]
        for part_name in selected_parts:
            img_path = images_dir / f"{part_name}_b.img"
            if can_use_slot_image_legacy(part_name, img_path, layout["slot_mode"]):
                command += [
                    "--partition", f"{part_name}_b:readonly:{img_path.stat().st_size}:{layout['group_b_name']}",
                    "--image", f"{part_name}_b={img_path}",
                ]
            else:
                if img_path.exists():
                    warnings.append(f"Skipping invalid _b image and adding empty metadata partition: {img_path.name}")
                command += ["--partition", f"{part_name}_b:readonly:0:{layout['group_b_name']}"]
        command += ["--virtual-ab"]

    command += ["--out", str(output_super)]
    return command, layout, warnings, errors


def build_super_image_legacy(
    images_dir: Path,
    output_super: Path,
    super_info: dict[str, Any],
    device: str | None = None,
    execute: bool = False,
) -> dict[str, Any]:
    """Plan or execute the legacy lpmake super.img build."""
    images_dir = Path(images_dir).resolve()
    output_super = Path(output_super).resolve()
    device = device
    lpmake_path = resolve_lpmake_binary_legacy()
    command, layout, warnings, errors = _build_lpmake_command(images_dir, output_super, super_info, lpmake_path)
    skipped_items: list[dict[str, str]] = []
    lpmake_executed = False
    super_img_created = False
    super_img_size: int | None = None
    return_code: int | None = None
    command_output: str | None = None

    if lpmake_path is None:
        errors.append("lpmake was not found by the legacy resolver")
    if output_super.exists():
        warnings.append(f"Existing super.img will be overwritten by legacy lpmake build: {output_super}")

    if not execute:
        status = "DRY_RUN" if not errors else "FAILED"
        return {
            "dry_run": True,
            "status": status,
            "images_dir": str(images_dir),
            "output_super": str(output_super),
            "layout": layout,
            "lpmake_path": str(lpmake_path) if lpmake_path else None,
            "lpmake_command": command,
            "lpmake_executed": lpmake_executed,
            "super_img_created": super_img_created,
            "super_img_size": super_img_size,
            "return_code": return_code,
            "command_output": command_output,
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    if errors:
        skipped_items.append({"item": "lpmake", "reason": "preflight failed"})
        return {
            "dry_run": False,
            "status": "FAILED",
            "images_dir": str(images_dir),
            "output_super": str(output_super),
            "layout": layout,
            "lpmake_path": str(lpmake_path) if lpmake_path else None,
            "lpmake_command": command,
            "lpmake_executed": lpmake_executed,
            "super_img_created": super_img_created,
            "super_img_size": super_img_size,
            "return_code": return_code,
            "command_output": command_output,
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    output_super.parent.mkdir(parents=True, exist_ok=True)
    if output_super.exists():
        output_super.unlink()

    try:
        result = subprocess.run(
            command,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name != "posix" else 0,
        )
        lpmake_executed = True
        return_code = result.returncode
        command_output = result.stdout.decode("utf-8", errors="replace")
    except FileNotFoundError as exc:
        lpmake_executed = True
        return_code = 2
        command_output = f"[FileNotFoundError] {exc}"

    super_img_created = output_super.exists()
    super_img_size = output_super.stat().st_size if super_img_created else None
    if return_code != 0 or not super_img_created:
        errors.append(f"lpmake failed building super.img with return code {return_code}")

    return {
        "dry_run": False,
        "status": "APPLIED" if not errors else "FAILED",
        "images_dir": str(images_dir),
        "output_super": str(output_super),
        "layout": layout,
        "lpmake_path": str(lpmake_path) if lpmake_path else None,
        "lpmake_command": command,
        "lpmake_executed": lpmake_executed,
        "super_img_created": super_img_created,
        "super_img_size": super_img_size,
        "return_code": return_code,
        "command_output": command_output,
        "skipped_items": skipped_items,
        "warnings": warnings,
        "errors": errors,
    }
