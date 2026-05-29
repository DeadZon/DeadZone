from __future__ import annotations

import os
import platform
import shutil
import stat
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from factory.core.detector import RomInfo
from factory.core.workspace import Workspace, read_json, write_json

DEFAULT_SUPER_SIZE = 8_500_000_000
LP_METADATA_OVERHEAD = 4 * 1024 * 1024
METADATA_SIZE = 65_536

DYNAMIC_PARTITIONS = [
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
DYNAMIC_IMAGES = {f"{name}.img" for name in DYNAMIC_PARTITIONS}


@dataclass(frozen=True)
class Toolset:
    lpmake: Path | None
    lpdump: Path | None
    lpunpack: Path | None
    simg2img: Path | None
    img2simg: Path | None


def _metadata_path(ws: Workspace, name: str) -> Path:
    return ws.meta / name


def _load_required_metadata(ws: Workspace) -> dict[str, dict[str, Any]]:
    names = ["rom_info.json", "device_info.json", "super_layout.json", "partition_map.json"]
    missing = [name for name in names if not _metadata_path(ws, name).is_file()]
    if missing:
        raise RuntimeError(f"required super metadata is missing: {', '.join(missing)}")
    return {name: read_json(_metadata_path(ws, name), {}) for name in names}


def _helper_candidates(tool: str) -> list[Path]:
    exe = f"{tool}.exe" if os.name == "nt" else tool
    system_name = platform.system().lower()
    machine = platform.machine()
    roots = [
        Path("tools/helper"),
        Path("tools/helper/bin"),
        Path("tools/helper/bin") / system_name,
        Path("tools/helper/bin") / system_name / machine,
        Path("tools/helper/bin/linux"),
        Path("tools/helper/bin/windows"),
    ]
    return [root / exe for root in roots] + [root / tool for root in roots if exe != tool]


def resolve_tool(tool: str) -> Path | None:
    for candidate in _helper_candidates(tool):
        if candidate.is_file():
            if os.name == "posix":
                try:
                    candidate.chmod(candidate.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                except OSError:
                    pass
            return candidate.resolve()
    found = shutil.which(tool) or shutil.which(f"{tool}.exe")
    return Path(found).resolve() if found else None


def resolve_tools() -> Toolset:
    return Toolset(
        lpmake=resolve_tool("lpmake"),
        lpdump=resolve_tool("lpdump"),
        lpunpack=resolve_tool("lpunpack"),
        simg2img=resolve_tool("simg2img"),
        img2simg=resolve_tool("img2simg"),
    )


def _profile_path(soc: str) -> Path:
    key = (soc or "").strip().lower()
    return Path("profiles") / f"{key}.yml"


def _load_profile(soc: str) -> dict[str, Any]:
    path = _profile_path(soc)
    if not path.is_file():
        return {}
    try:
        import yaml  # type: ignore
    except Exception:
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, dict) else {}


def _base_partition(name: str) -> str:
    stem = Path(name).stem
    return stem.removesuffix("_a").removesuffix("_b")


def _image_for_partition(ws: Workspace, part: str) -> Path | None:
    candidates = [
        ws.partitions / f"{part}.img",
        ws.partitions / f"{part}_a.img",
        ws.images / f"{part}.img",
        ws.images / f"{part}_a.img",
    ]
    for candidate in candidates:
        if candidate.is_file() and candidate.stat().st_size > 0:
            return candidate
    return None


def _dynamic_images(ws: Workspace, partition_map: dict[str, Any]) -> dict[str, Path]:
    ordered: dict[str, Path] = {}
    by_partition = partition_map.get("by_partition") if isinstance(partition_map.get("by_partition"), dict) else {}
    for name in DYNAMIC_PARTITIONS:
        mapped = by_partition.get(name)
        if isinstance(mapped, str):
            mapped_path = ws.partitions / Path(mapped).name
            if mapped_path.is_file() and mapped_path.stat().st_size > 0:
                ordered[name] = mapped_path
                continue
        found = _image_for_partition(ws, name)
        if found:
            ordered[name] = found
    for directory in [ws.partitions, ws.images]:
        for img in sorted(directory.glob("*.img")):
            part = _base_partition(img.name)
            if part in DYNAMIC_PARTITIONS and part not in ordered and img.stat().st_size > 0:
                ordered[part] = img
    return ordered


def _int_value(*values: Any) -> int:
    for value in values:
        try:
            parsed = int(value)
        except (TypeError, ValueError):
            continue
        if parsed > 0:
            return parsed
    return 0


def _group_from_metadata(super_layout: dict[str, Any], profile_super: dict[str, Any]) -> str:
    for key in ("dynamic_group_name", "group_name", "group_basename"):
        value = super_layout.get(key) or profile_super.get(key)
        if isinstance(value, str) and value.strip():
            return value.removesuffix("_a").removesuffix("_b")
    return "qti_dynamic_partitions"


def _slot_mode(device_info: dict[str, Any], super_layout: dict[str, Any]) -> str:
    value = str(super_layout.get("slot_mode") or device_info.get("slot_mode") or "").upper()
    if value in {"VAB", "VIRTUAL_AB", "VIRTUAL-A/B"}:
        return "VAB"
    if value in {"A/B", "AB"}:
        return "A/B"
    return "A-only"


def _partition_sizes(super_layout: dict[str, Any], partition_map: dict[str, Any]) -> dict[str, int]:
    result: dict[str, int] = {}
    for source in [super_layout.get("partition_sizes"), partition_map.get("partition_sizes")]:
        if not isinstance(source, dict):
            continue
        for key, value in source.items():
            size = _int_value(value)
            if size:
                result[_base_partition(str(key))] = size
    return result


def _metadata_source(super_layout: dict[str, Any], partition_map: dict[str, Any], profile_path: Path) -> str:
    for key in ("metadata_source", "input_metadata_source", "super_metadata_source"):
        value = super_layout.get(key) or partition_map.get(key)
        if isinstance(value, str) and value:
            return value
    if _partition_sizes(super_layout, partition_map):
        return "dynamic_partition_metadata"
    if profile_path.is_file():
        return str(profile_path)
    return "profile_defaults"


def _derive_layout(
    ws: Workspace,
    metadata: dict[str, dict[str, Any]],
    dynamic_images: dict[str, Path],
) -> dict[str, Any]:
    device_info = metadata["device_info.json"]
    super_layout = metadata["super_layout.json"]
    partition_map = metadata["partition_map.json"]
    soc = str(device_info.get("soc") or "").lower()
    profile = _load_profile(soc)
    profile_super = profile.get("super") if isinstance(profile.get("super"), dict) else {}
    profile_path = _profile_path(soc)

    slot_mode = _slot_mode(device_info, super_layout)
    is_vab = slot_mode == "VAB"
    group_name = _group_from_metadata(super_layout, profile_super)
    metadata_source = _metadata_source(super_layout, partition_map, profile_path)
    target_size = _int_value(
        super_layout.get("super_size"),
        super_layout.get("target_super_size"),
        super_layout.get("default_target_super_size"),
        profile_super.get("default_super_size"),
        DEFAULT_SUPER_SIZE,
    )
    if target_size < DEFAULT_SUPER_SIZE and metadata_source in {"profile_defaults", str(profile_path)}:
        target_size = DEFAULT_SUPER_SIZE

    group_size = _int_value(super_layout.get("group_size"), profile_super.get("group_size"))
    if group_size <= 0:
        group_size = max(0, target_size - LP_METADATA_OVERHEAD)

    selected = [name for name in DYNAMIC_PARTITIONS if name in dynamic_images]
    sizes = _partition_sizes(super_layout, partition_map)
    return {
        "metadata_source": metadata_source,
        "target_super_size": target_size,
        "block_device_name": str(super_layout.get("block_device_name") or "super"),
        "metadata_size": _int_value(super_layout.get("metadata_size"), METADATA_SIZE),
        "metadata_slots": _int_value(super_layout.get("metadata_slots"), 3 if is_vab else 2),
        "dynamic_group_name": group_name,
        "group_name": group_name,
        "group_a_name": f"{group_name}_a" if is_vab else group_name,
        "group_b_name": f"{group_name}_b" if is_vab else "",
        "group_size": group_size,
        "slot_mode": slot_mode,
        "virtual_ab": is_vab,
        "vab_zero_b": bool(profile_super.get("vab_zero_b", True)),
        "output_format": str(super_layout.get("output_format") or "sparse"),
        "partition_sizes": sizes,
        "selected_partitions": selected,
        "dynamic_images": {name: str(path) for name, path in dynamic_images.items()},
    }


def _allocation(part: str, image: Path, layout: dict[str, Any], warnings: list[str]) -> int:
    sizes = layout.get("partition_sizes") if isinstance(layout.get("partition_sizes"), dict) else {}
    original_size = _int_value(sizes.get(part))
    image_size = image.stat().st_size
    if original_size:
        if image_size > original_size:
            raise RuntimeError(
                f"{image.name} size {image_size} exceeds metadata allocation {original_size} bytes"
            )
        return original_size
    warnings.append(f"{part}.img has no metadata allocation; using current image size {image_size}")
    return image_size


def _build_lpmake_command(
    output_super: Path,
    layout: dict[str, Any],
    dynamic_images: dict[str, Path],
    lpmake: Path,
    warnings: list[str],
) -> list[str]:
    target_size = int(layout["target_super_size"])
    if target_size <= 0:
        raise RuntimeError("target super size is missing or invalid")
    group_size = int(layout["group_size"])
    if group_size <= 0 or group_size >= target_size:
        raise RuntimeError("dynamic group size is missing or exceeds target super size")

    command = [
        str(lpmake),
        "--metadata-size", str(layout["metadata_size"]),
        "--super-name", str(layout["block_device_name"]),
        "--metadata-slots", str(layout["metadata_slots"]),
        "--device", f"{layout['block_device_name']}:{target_size}",
    ]
    if layout.get("output_format") == "sparse":
        command.append("--sparse")

    selected = list(layout["selected_partitions"])
    if not selected:
        raise RuntimeError("no dynamic partition images are available to build super.img")

    if layout["virtual_ab"]:
        command += ["--group", f"{layout['group_a_name']}:{group_size}"]
        for part in selected:
            image = dynamic_images[part]
            alloc = _allocation(part, image, layout, warnings)
            command += ["--partition", f"{part}_a:readonly:{alloc}:{layout['group_a_name']}"]
            command += ["--image", f"{part}_a={image}"]
        command += ["--group", f"{layout['group_b_name']}:{group_size}"]
        for part in selected:
            command += ["--partition", f"{part}_b:readonly:0:{layout['group_b_name']}"]
        command.append("--virtual-ab")
    else:
        command += ["--group", f"{layout['group_a_name']}:{group_size}"]
        for part in selected:
            image = dynamic_images[part]
            alloc = _allocation(part, image, layout, warnings)
            command += ["--partition", f"{part}:readonly:{alloc}:{layout['group_a_name']}"]
            command += ["--image", f"{part}={image}"]

    command += ["--out", str(output_super)]
    return command


def _validate_with_lpdump(super_img: Path, lpdump: Path | None) -> dict[str, Any]:
    if lpdump is None:
        return {"status": "SKIPPED", "reason": "lpdump not available from tools/helper or PATH", "output": ""}
    if not super_img.is_file():
        return {"status": "FAILED", "reason": f"super.img not found: {super_img}", "output": ""}
    proc = subprocess.run(
        [str(lpdump), str(super_img)],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return {
        "status": "PASSED" if proc.returncode == 0 else "FAILED",
        "reason": "lpdump completed" if proc.returncode == 0 else f"lpdump exited with code {proc.returncode}",
        "output": proc.stdout,
    }


def _write_report(
    ws: Workspace,
    result: dict[str, Any],
    layout: dict[str, Any],
    validation: dict[str, Any],
) -> None:
    command = result.get("lpmake_command") or []
    lines = [
        "DeadZone Super Build Report",
        "===========================",
        f"action: {result.get('action')}",
        f"reason: {result.get('reason')}",
        f"input metadata source: {layout.get('metadata_source')}",
        f"target super size: {layout.get('target_super_size')}",
        f"group name: {layout.get('dynamic_group_name')}",
        f"group size: {layout.get('group_size')}",
        f"slot mode: {layout.get('slot_mode')}",
        "",
        "partition list:",
    ]
    for part in layout.get("selected_partitions", []):
        image = layout.get("dynamic_images", {}).get(part, "")
        size = layout.get("partition_sizes", {}).get(part, "image-size")
        lines.append(f"  - {part}: image={image} allocation={size}")
    lines += ["", "_b zero-size entries for VAB:"]
    if layout.get("virtual_ab"):
        for part in layout.get("selected_partitions", []):
            lines.append(f"  - {part}_b: 0")
    else:
        lines.append("  (not VAB)")
    lines += [
        "",
        "lpmake command:",
        f"  {' '.join(str(token) for token in command)}" if command else "  (none)",
        "",
        f"validation status: {validation.get('status')}",
        f"validation reason: {validation.get('reason')}",
    ]
    if validation.get("output"):
        lines += ["", "lpdump output:"]
        lines.extend(f"  {line}" for line in str(validation["output"]).splitlines())
    warnings = result.get("warnings") or []
    errors = result.get("errors") or []
    lines += ["", "warnings:"]
    lines.extend([f"  - {warning}" for warning in warnings] or ["  (none)"])
    lines += ["", "errors:"]
    lines.extend([f"  - {error}" for error in errors] or ["  (none)"])
    lines.append("")
    (ws.reports / "super_build_report.txt").write_text("\n".join(lines), encoding="utf-8")


def build_super_image(ws: Workspace, info: RomInfo | None = None, inspection: dict[str, Any] | None = None) -> dict[str, Any]:
    metadata = _load_required_metadata(ws)
    rom_info = metadata["rom_info.json"]
    device_info = metadata["device_info.json"]
    super_layout = metadata["super_layout.json"]
    partition_map = metadata["partition_map.json"]
    dynamic_images = _dynamic_images(ws, partition_map)
    layout = _derive_layout(ws, metadata, dynamic_images)
    tools = resolve_tools()
    final_super = ws.images / "super.img"
    needs_rebuild = bool(
        super_layout.get("rebuild_required")
        or super_layout.get("needs_super_rebuild")
        or rom_info.get("super_rebuild_required")
        or rom_info.get("needs_super_rebuild")
        or (inspection or {}).get("needs_super_rebuild")
    )
    reason = ""
    warnings: list[str] = []
    errors: list[str] = []
    command: list[str] = []

    if final_super.is_file() and not needs_rebuild:
        action = "preserved"
        reason = "original super.img is present and no dynamic partition rebuild was requested"
        validation = _validate_with_lpdump(final_super, tools.lpdump)
    elif final_super.is_file() and not dynamic_images:
        action = "preserved"
        reason = "super.img is present and no replacement dynamic partition images are available"
        validation = _validate_with_lpdump(final_super, tools.lpdump)
    else:
        action = "rebuilt"
        if not dynamic_images:
            raise RuntimeError("cannot rebuild super.img because no dynamic partition images are available")
        if tools.lpmake is None:
            raise RuntimeError("lpmake not available from tools/helper or PATH")
        reason = "dynamic partition content requires a new super.img"
        if not final_super.is_file():
            reason = "no original super.img is available and dynamic partition images exist"
        command = _build_lpmake_command(final_super, layout, dynamic_images, tools.lpmake, warnings)
        final_super.parent.mkdir(parents=True, exist_ok=True)
        if final_super.exists():
            final_super.unlink()
        log = ws.logs / "lpmake.log"
        with log.open("w", encoding="utf-8") as fh:
            proc = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=fh, stderr=subprocess.STDOUT, text=True)
        if proc.returncode != 0 or not final_super.is_file():
            errors.append(f"lpmake failed with code {proc.returncode}; see {log}")
            validation = {"status": "FAILED", "reason": "lpmake did not produce a valid super.img", "output": ""}
        else:
            validation = _validate_with_lpdump(final_super, tools.lpdump)

    result = {
        "status": "FAILED" if errors or validation.get("status") == "FAILED" else "OK",
        "action": action,
        "reason": reason,
        "super_img": str(final_super),
        "super_size": final_super.stat().st_size if final_super.is_file() else None,
        "input_metadata_source": layout.get("metadata_source"),
        "target_super_size": layout.get("target_super_size"),
        "group_name": layout.get("dynamic_group_name"),
        "group_size": layout.get("group_size"),
        "slot_mode": layout.get("slot_mode") or device_info.get("slot_mode"),
        "partition_list": layout.get("selected_partitions"),
        "vab_zero_size_b_partitions": [f"{p}_b" for p in layout.get("selected_partitions", [])] if layout.get("virtual_ab") else [],
        "lpmake_command": command,
        "tools": {name: str(path) if path else None for name, path in tools.__dict__.items()},
        "validation": validation,
        "warnings": warnings,
        "errors": errors,
    }
    write_json(ws.meta / "super_layout.json", {**super_layout, **layout, "lpmake_command": command, "validation": validation})
    write_json(ws.meta / "super_build_result.json", result)
    _write_report(ws, result, layout, validation)
    if errors:
        raise RuntimeError("; ".join(errors))
    print(f"[SUPER] {action}")
    return result


def build_super(ws: Workspace, info: RomInfo | None = None, inspection: dict[str, Any] | None = None) -> dict[str, Any]:
    return build_super_image(ws, info, inspection)
