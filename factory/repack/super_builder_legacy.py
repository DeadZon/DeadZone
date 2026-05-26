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
    "odm",
    "vendor_dlkm",
    "system_dlkm",
    "odm_dlkm",
    "mi_ext",
]

# LP metadata reserved space: geometry blocks ×2 + metadata slots ×3 ×2 + alignment.
# 4 MiB is a conservative safe margin so group_size never exceeds device capacity.
_LP_METADATA_OVERHEAD: int = 4 * 1024 * 1024


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
    """Collect partition image names from a directory, ordered like legacy metadata.

    Pass partition_staging_dir here when EROFS images live in a separate staging
    directory (MEZOBuildRom-style separation).  The default images_dir path is
    kept for backward-compatibility with callers that haven't been updated yet.
    """
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
    original_partition_sizes: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Derive the legacy lpmake layout from super_info and images_dir.

    original_partition_sizes — {base_name: lp_allocation_bytes} from the original
    super.img metadata.  When provided these values are used for the lpmake
    --partition allocation size instead of the current image file size.
    """
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

    # partition_image_sizes records actual on-disk file sizes for reporting.
    # These are NOT used for lpmake --partition allocation; original_partition_sizes
    # (from original super metadata) are used there instead.
    partition_image_sizes = {
        part: _image_for_partition(images_dir, part, "a").stat().st_size
        for part in selected_parts
        if _image_for_partition(images_dir, part, "a").is_file()
    }

    # group_size must be < super_size to leave room for LP metadata headers.
    # Using super_size directly causes lpmake to reject the image because the
    # group capacity would exceed the available data space on the block device.
    group_size = max(0, super_size - _LP_METADATA_OVERHEAD) if super_size > 0 else 0

    return {
        "block_device_name": block_device_name,
        "super_size": super_size,
        "super_type": super_type,
        "metadata_slot_count": metadata_slot_count,
        "group_name": group_name,
        "group_a_name": group_a_name,
        "group_b_name": group_b_name,
        "group_size": group_size,
        "slot_mode": "vab" if super_type == 2 else "single",
        "virtual_ab": super_type == 2,
        "output_format": super_info.get("output_format") or "sparse",
        "selected_parts": selected_parts,
        "partition_image_sizes": partition_image_sizes,
        "original_partition_sizes": original_partition_sizes or {},
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
    partition_images_dir: Path,
    output_super: Path,
    super_info: dict[str, Any],
    lpmake_path: Path | None,
    original_partition_sizes: dict[str, int] | None = None,
) -> tuple[list[str], dict[str, Any], list[str], list[str]]:
    """Build the lpmake argument list.

    partition_images_dir    — directory containing the EROFS-repacked *.img files
                              (may be a separate staging dir, never the final images dir).
    output_super            — path where lpmake must write super.img.
    original_partition_sizes — {base_name: lp_allocation_bytes} from the original
                              super.img metadata.  Each partition's --partition
                              allocation is set to this value, NOT the image file size.
                              If absent, falls back to image file size with a warning.
    """
    layout = derive_super_layout_legacy(partition_images_dir, super_info, original_partition_sizes)
    warnings: list[str] = []
    errors: list[str] = []
    super_size = int(layout["super_size"] or 0)
    if super_size <= 0:
        errors.append("super_info has no valid block device size")

    lpmake_sparse_enabled = (layout.get("output_format") or "sparse") == "sparse"
    layout["lpmake_sparse_enabled"] = lpmake_sparse_enabled

    orig_sizes: dict[str, int] = original_partition_sizes or {}
    if not orig_sizes:
        errors.append(
            "ERROR: original super metadata missing; cannot preserve partition byte sizes. "
            "original_partition_sizes is empty — refusing to fall back to image file sizes."
        )

    command = [
        str(lpmake_path) if lpmake_path else "lpmake",
        "--metadata-size", "65536",
        "-super-name", str(layout["block_device_name"]),
        "-metadata-slots", "3" if layout["super_type"] == 2 else "2",
    ]
    if lpmake_sparse_enabled:
        command.append("--sparse")

    group_size = int(layout.get("group_size") or 0)
    if group_size <= 0 and super_size > 0:
        group_size = max(0, super_size - _LP_METADATA_OVERHEAD)

    def _alloc_size(part_name: str, img_path: Path) -> int | None:
        """Return LP allocation size for a partition; None signals a hard error."""
        img_size = img_path.stat().st_size
        if part_name in orig_sizes:
            alloc = orig_sizes[part_name]
            if img_size > alloc:
                errors.append(
                    f"ERROR: {part_name}.img size {img_size} exceeds original "
                    f"{part_name} allocation {alloc} bytes"
                )
                return None
            return alloc
        errors.append(
            f"ERROR: original super metadata missing for {part_name}; "
            f"cannot preserve partition byte sizes. "
            f"Refusing to fall back to image file size."
        )
        return None

    selected_parts = list(layout["selected_parts"])
    if layout["super_type"] == 1:
        command += [
            "-device", f"{layout['block_device_name']}:{super_size}",
            "--group", f"{layout['group_a_name']}:{group_size}",
        ]
        for part_name in selected_parts:
            img_path = _image_for_partition(partition_images_dir, part_name, "a")
            if not img_path.exists():
                errors.append(f"Required image not found for super pack: {img_path}")
                continue
            alloc = _alloc_size(part_name, img_path)
            if alloc is None:
                continue
            command += [
                "--partition", f"{part_name}:readonly:{alloc}:{layout['group_a_name']}",
                "--image", f"{part_name}={img_path}",
            ]
    else:
        command += [
            "-device", f"{layout['block_device_name']}:{super_size}",
            "--group", f"{layout['group_a_name']}:{group_size}",
        ]
        for part_name in selected_parts:
            img_path = _image_for_partition(partition_images_dir, part_name, "a")
            if not img_path.exists():
                errors.append(f"Required _a image not found for super pack: {img_path}")
                continue
            alloc = _alloc_size(part_name, img_path)
            if alloc is None:
                continue
            command += [
                "--partition", f"{part_name}_a:readonly:{alloc}:{layout['group_a_name']}",
                "--image", f"{part_name}_a={img_path}",
            ]
        command += ["--group", f"{layout['group_b_name']}:{group_size}"]
        for part_name in selected_parts:
            img_path = partition_images_dir / f"{part_name}_b.img"
            if can_use_slot_image_legacy(part_name, img_path, layout["slot_mode"]):
                alloc = _alloc_size(part_name, img_path)
                if alloc is None:
                    command += ["--partition", f"{part_name}_b:readonly:0:{layout['group_b_name']}"]
                    continue
                command += [
                    "--partition", f"{part_name}_b:readonly:{alloc}:{layout['group_b_name']}",
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
    partition_images_dir: Path | None = None,
    device: str | None = None,
    execute: bool = False,
    original_partition_sizes: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Plan or execute the legacy lpmake super.img build.

    partition_images_dir    — directory that holds the EROFS-repacked dynamic
                              partition images (system.img, vendor.img, …).
    images_dir              — the final fastboot images directory (output/images/).
    original_partition_sizes — {base_name: lp_allocation_bytes} from the original
                              super.img metadata.  These are used for the lpmake
                              --partition size argument so the final LP metadata
                              preserves the exact original allocation sizes.
    """
    partition_images_dir = Path(partition_images_dir).resolve() if partition_images_dir else Path(images_dir).resolve()
    images_dir = Path(images_dir).resolve()
    output_super = Path(output_super).resolve()
    device = device

    # Pre-flight validation: original metadata must be present before lpmake runs.
    # partition_table may be empty when super_info comes from a hardcoded device profile
    # or the payload manifest path; what matters is that original_partition_sizes is
    # populated (either from LP super metadata or from the payload manifest per-partition
    # new_partition_info.size values threaded in by the pipeline stage).
    preflight_errors: list[str] = []
    if not original_partition_sizes:
        preflight_errors.append(
            "ERROR: original super metadata missing; cannot preserve partition byte sizes. "
            "original_partition_sizes is empty — refusing to fall back to image file sizes."
        )
    block_devices = super_info.get("block_devices") or []
    raw_super_size = int(block_devices[0].get("size", 0) or 0) if block_devices else 0
    if raw_super_size <= 0:
        preflight_errors.append(
            "ERROR: super_info has no valid block device size (super_size=0). "
            "Cannot determine group allocation."
        )
    if preflight_errors:
        return {
            "dry_run": not execute,
            "status": "FAILED",
            "partition_images_dir": str(partition_images_dir),
            "images_dir": str(images_dir),
            "output_super": str(output_super),
            "layout": {},
            "lpmake_path": None,
            "lpmake_command": [],
            "lpmake_executed": False,
            "lpmake_sparse_enabled": False,
            "super_img_created": False,
            "super_img_size": None,
            "return_code": None,
            "command_output": None,
            "skipped_items": [{"item": "lpmake", "reason": "pre-flight validation failed"}],
            "warnings": [],
            "errors": preflight_errors,
        }

    lpmake_path = resolve_lpmake_binary_legacy()
    command, layout, warnings, errors = _build_lpmake_command(
        partition_images_dir, output_super, super_info, lpmake_path,
        original_partition_sizes=original_partition_sizes,
    )
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
            "partition_images_dir": str(partition_images_dir),
            "images_dir": str(images_dir),
            "output_super": str(output_super),
            "layout": layout,
            "lpmake_path": str(lpmake_path) if lpmake_path else None,
            "lpmake_command": command,
            "lpmake_executed": lpmake_executed,
            "lpmake_sparse_enabled": layout.get("lpmake_sparse_enabled", False),
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
            "partition_images_dir": str(partition_images_dir),
            "images_dir": str(images_dir),
            "output_super": str(output_super),
            "layout": layout,
            "lpmake_path": str(lpmake_path) if lpmake_path else None,
            "lpmake_command": command,
            "lpmake_executed": lpmake_executed,
            "lpmake_sparse_enabled": layout.get("lpmake_sparse_enabled", False),
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
        "partition_images_dir": str(partition_images_dir),
        "images_dir": str(images_dir),
        "output_super": str(output_super),
        "layout": layout,
        "lpmake_path": str(lpmake_path) if lpmake_path else None,
        "lpmake_command": command,
        "lpmake_executed": lpmake_executed,
        "lpmake_sparse_enabled": layout.get("lpmake_sparse_enabled", False),
        "super_img_created": super_img_created,
        "super_img_size": super_img_size,
        "return_code": return_code,
        "command_output": command_output,
        "skipped_items": skipped_items,
        "warnings": warnings,
        "errors": errors,
    }
