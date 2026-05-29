from __future__ import annotations

from pathlib import Path
from typing import Any

from factory.core.device_registry import resolve_device
from factory.core.detector import DYNAMIC_PARTITIONS, RomInfo
from factory.core.workspace import Workspace, read_json, write_json

DEFAULT_SUPER_SIZE = 8_500_000_000
LP_METADATA_OVERHEAD = 4 * 1024 * 1024
METADATA_SIZE = 65_536


def _base_partition(name: str) -> str:
    stem = Path(name).stem
    return stem.removesuffix("_a").removesuffix("_b")


def _int_value(*values: Any) -> int:
    for value in values:
        try:
            parsed = int(value)
        except (TypeError, ValueError):
            continue
        if parsed > 0:
            return parsed
    return 0


def _slot_mode(*values: Any) -> str:
    for value in values:
        normalized = str(value or "").strip().upper().replace("-", "_")
        if normalized in {"VAB", "VIRTUAL_AB", "VIRTUAL_A/B"}:
            return "VAB"
        if normalized in {"A/B", "AB"}:
            return "A/B"
        if normalized in {"A_ONLY", "A-ONLY"}:
            return "A-only"
    return "A-only"


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


def dynamic_images(ws: Workspace, partition_map: dict[str, Any]) -> dict[str, Path]:
    ordered: dict[str, Path] = {}
    by_partition = partition_map.get("by_partition") if isinstance(partition_map.get("by_partition"), dict) else {}
    for name in sorted(DYNAMIC_PARTITIONS):
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


def _first_source_value(named_sources: list[tuple[str, dict[str, Any]]], *keys: str) -> tuple[Any, str]:
    for source_name, source in named_sources:
        for key in keys:
            value = source.get(key)
            if value not in (None, "", []):
                return value, source_name
    return None, "unresolved"


def build_super_profile(
    ws: Workspace,
    info: RomInfo | None = None,
    inspection: dict[str, Any] | None = None,
    device_config: dict[str, Any] | None = None,
) -> dict[str, Any]:
    rom_info = read_json(ws.meta / "rom_info.json", {})
    device_info = read_json(ws.meta / "device_info.json", {})
    super_layout = read_json(ws.meta / "super_layout.json", {})
    partition_map = read_json(ws.meta / "partition_map.json", {})
    if info is not None:
        rom_info.update({k: v for k, v in info.__dict__.items() if v is not None})

    if device_config is None:
        device_config = read_json(ws.meta / "device_registry.json", {})
    if not device_config:
        device_config = resolve_device(rom_metadata=rom_info or device_info, ws=ws)
    profile_super = device_config.get("super") if isinstance(device_config.get("super"), dict) else {}
    soc_super = device_config.get("_soc_super") if isinstance(device_config.get("_soc_super"), dict) else profile_super
    device_super = device_config.get("_device_super") if isinstance(device_config.get("_device_super"), dict) else profile_super

    detected_sizes = _partition_sizes(super_layout, partition_map)
    original_metadata = super_layout if super_layout.get("metadata_source") in {
        "original_super_metadata",
        "super_metadata",
        "lpdump",
    } else {}
    payload_metadata = super_layout if detected_sizes else {}
    named_sources = [
        ("original_super_metadata", original_metadata),
        ("payload_dynamic_partition_metadata", payload_metadata),
        ("device_profile", device_super),
        ("soc_profile", soc_super),
    ]

    size_value, size_source = _first_source_value(
        named_sources,
        "super_size",
        "target_super_size",
        "default_target_super_size",
        "default_size",
        "default_super_size",
    )
    group_value, group_source = _first_source_value(named_sources, "group_size")
    group_name_value, group_name_source = _first_source_value(
        named_sources,
        "dynamic_group_name",
        "dynamic_group",
        "group_name",
        "group_basename",
    )
    slot_value, slot_source = _first_source_value(named_sources, "slot_mode")
    output_value, output_source = _first_source_value(named_sources, "output_format", "super_output_format")
    metadata_slots_value, metadata_slots_source = _first_source_value(named_sources, "metadata_slots")

    target_size = _int_value(size_value, DEFAULT_SUPER_SIZE)
    group_size = _int_value(group_value)
    if group_size <= 0:
        group_size = max(0, target_size - LP_METADATA_OVERHEAD)
        group_source = f"{size_source}_minus_metadata_overhead"

    slot_mode = _slot_mode(slot_value, device_info.get("slot_mode"), rom_info.get("slot_mode"))
    is_vab = slot_mode == "VAB"
    group_name = str(group_name_value or "qti_dynamic_partitions").removesuffix("_a").removesuffix("_b")
    images = dynamic_images(ws, partition_map)
    selected = [name for name in sorted(DYNAMIC_PARTITIONS) if name in images]
    metadata_source = size_source
    if detected_sizes and metadata_source == "unresolved":
        metadata_source = "payload_dynamic_partition_metadata"

    profile = {
        "metadata_source": metadata_source,
        "metadata_priority": [
            "original_super_metadata",
            "payload_dynamic_partition_metadata",
            "device_profile",
            "soc_profile",
        ],
        "target_super_size": target_size,
        "block_device_name": str(super_layout.get("block_device_name") or "super"),
        "metadata_size": _int_value(super_layout.get("metadata_size"), METADATA_SIZE),
        "metadata_slots": _int_value(metadata_slots_value, super_layout.get("metadata_slots"), 3 if is_vab else 2),
        "metadata_slots_source": metadata_slots_source,
        "dynamic_group_name": group_name,
        "group_name": group_name,
        "group_name_source": group_name_source,
        "group_a_name": f"{group_name}_a" if is_vab else group_name,
        "group_b_name": f"{group_name}_b" if is_vab else "",
        "group_size": group_size,
        "group_size_source": group_source,
        "slot_mode": slot_mode,
        "slot_mode_source": slot_source,
        "virtual_ab": is_vab,
        "vab_zero_b": bool(profile_super.get("vab_zero_b", True)),
        "output_format": str(output_value or "sparse"),
        "output_format_source": output_source,
        "partition_sizes": detected_sizes,
        "partition_sizes_source": "detected_metadata" if detected_sizes else "unavailable",
        "selected_partitions": selected,
        "dynamic_images": {name: str(path) for name, path in images.items()},
        "allow_image_size_allocations": False,
        "device": {
            "codename": device_config.get("resolved_codename") or device_config.get("codename"),
            "name": device_config.get("name"),
            "soc": device_config.get("soc"),
            "profile_source": device_config.get("profile_source"),
            "device_source": device_config.get("device_source"),
        },
        "inspection_needs_rebuild": bool((inspection or {}).get("needs_super_rebuild")),
    }
    write_json(ws.meta / "super_profile.json", profile)
    write_super_profile_report(ws, profile)
    return profile


def write_super_profile_report(ws: Workspace, profile: dict[str, Any]) -> None:
    lines = [
        "DeadZone Super Profile Report",
        "=============================",
        f"device: {profile.get('device', {}).get('codename')} ({profile.get('device', {}).get('name')})",
        f"soc: {profile.get('device', {}).get('soc')}",
        f"source: {profile.get('metadata_source')}",
        f"target super size: {profile.get('target_super_size')}",
        f"group name: {profile.get('dynamic_group_name')} ({profile.get('group_name_source')})",
        f"group size: {profile.get('group_size')} ({profile.get('group_size_source')})",
        f"slot mode: {profile.get('slot_mode')} ({profile.get('slot_mode_source')})",
        f"VAB zero-size _b entries: {profile.get('vab_zero_b')}",
        f"partition size source: {profile.get('partition_sizes_source')}",
        "",
        "selected partitions:",
    ]
    lines.extend([f"  - {part}" for part in profile.get("selected_partitions", [])] or ["  (none)"])
    lines.append("")
    (ws.reports / "super_profile_report.txt").write_text("\n".join(lines), encoding="utf-8")
