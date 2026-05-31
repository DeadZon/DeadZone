from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from factory.core.device_registry import resolve_device
from factory.core.detector import DYNAMIC_PARTITIONS, RomInfo
from factory.core.super_config import resolve_super_config_for_device, STATUS_READY
from factory.core.workspace import Workspace, read_json, write_json

DEFAULT_SUPER_SIZE = 8_500_000_000
LP_METADATA_OVERHEAD = 4 * 1024 * 1024
METADATA_SIZE = 65_536
SAFE_ALLOCATION_SOURCES = [
    "hyperur_superconfig",
    "original_super_metadata",
    "payload_manifest",
    "payload_partitions",
    "dynamic_partitions_op_list",
    "device_profile",
    "soc_profile",
]


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
            mapped_raw = Path(mapped)
            candidates = [
                mapped_raw if mapped_raw.is_absolute() else ws.root / mapped_raw,
                ws.partitions / mapped_raw.name,
                ws.images / mapped_raw.name,
            ]
            for mapped_path in candidates:
                if mapped_path.is_file() and mapped_path.stat().st_size > 0:
                    ordered[name] = mapped_path
                    break
            if name in ordered:
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


def _partition_entries(source: dict[str, Any], source_name: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for key in ("partitions", "partition_table"):
        entries = source.get(key)
        if not isinstance(entries, list):
            continue
        for item in entries:
            if not isinstance(item, dict):
                continue
            raw_name = str(item.get("name") or item.get("partition_name") or "")
            base = _base_partition(raw_name)
            if base not in DYNAMIC_PARTITIONS or raw_name.endswith("_b"):
                continue
            size = _int_value(
                item.get("allocation_size"),
                item.get("size_bytes"),
                item.get("size"),
                item.get("partition_size"),
            )
            if not size:
                continue
            result[base] = {
                "allocation_size": size,
                "group_name": str(item.get("group_name") or item.get("group") or ""),
                "readonly": bool(item.get("readonly", True)),
                "source": source_name,
            }
    return result


def _size_entries(sizes: dict[str, Any], source_name: str, group_name: str = "") -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for key, value in sizes.items():
        base = _base_partition(str(key))
        size = _int_value(value)
        if base in DYNAMIC_PARTITIONS and size:
            result[base] = {
                "allocation_size": size,
                "group_name": group_name,
                "readonly": True,
                "source": source_name,
            }
    return result


def _read_payload_metadata(ws: Workspace) -> dict[str, Any]:
    merged: dict[str, Any] = {}
    for name in ["payload_metadata.json", "payload_manifest.json", "payload_partitions.json"]:
        data = read_json(ws.meta / name, {})
        if not data:
            continue
        if not merged:
            merged = dict(data)
            continue
        for key, value in data.items():
            if key in {"partitions", "partition_table"} and isinstance(value, list):
                existing = merged.get(key) if isinstance(merged.get(key), list) else []
                by_name = {
                    _base_partition(str(item.get("name") or item.get("partition_name") or "")): item
                    for item in existing
                    if isinstance(item, dict)
                }
                for item in value:
                    if isinstance(item, dict):
                        by_name[_base_partition(str(item.get("name") or item.get("partition_name") or ""))] = item
                merged[key] = list(by_name.values())
            elif key == "partition_sizes" and isinstance(value, dict):
                sizes = merged.get("partition_sizes") if isinstance(merged.get("partition_sizes"), dict) else {}
                sizes.update(value)
                merged["partition_sizes"] = sizes
            elif value not in (None, "", [], {}):
                merged[key] = value
    return merged


def _read_payload_json(ws: Workspace, filename: str) -> dict[str, Any]:
    data = read_json(ws.meta / filename, {})
    return data if isinstance(data, dict) else {}


def _parse_dynamic_partitions_op_list(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    sizes: dict[str, int] = {}
    part_groups: dict[str, str] = {}
    group_sizes: dict[str, int] = {}
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        tokens = re.split(r"\s+", line)
        op = tokens[0].lower()
        if op in {"resize", "resize_partition"} and len(tokens) >= 3:
            base = _base_partition(tokens[1])
            size = _int_value(tokens[2])
            if base in DYNAMIC_PARTITIONS and size:
                sizes[base] = size
        elif op in {"add", "add_partition"} and len(tokens) >= 3:
            base = _base_partition(tokens[1])
            if base in DYNAMIC_PARTITIONS:
                part_groups[base] = str(tokens[2]).removesuffix("_a").removesuffix("_b")
        elif op in {"add_group", "resize_group"} and len(tokens) >= 3:
            group = str(tokens[1]).removesuffix("_a").removesuffix("_b")
            size = _int_value(tokens[2])
            if group and size:
                group_sizes[group] = size
    if not sizes and not group_sizes:
        return {}
    group_name = ""
    group_size = 0
    if group_sizes:
        group_name, group_size = max(group_sizes.items(), key=lambda item: item[1])
    return {
        "metadata_source": "dynamic_partitions_op_list",
        "path": str(path),
        "partition_sizes": sizes,
        "partition_groups": part_groups,
        "dynamic_group_name": group_name,
        "group_size": group_size,
    }


def _find_op_list(ws: Workspace) -> dict[str, Any]:
    for root in [ws.extracted / "payload", ws.extracted, ws.meta, ws.images]:
        if not root.exists():
            continue
        for path in sorted(root.rglob("dynamic_partitions_op_list") if root.is_dir() else []):
            parsed = _parse_dynamic_partitions_op_list(path)
            if parsed:
                return parsed
    return {}


def _first_source_value(named_sources: list[tuple[str, dict[str, Any]]], *keys: str) -> tuple[Any, str]:
    for source_name, source in named_sources:
        for key in keys:
            value = source.get(key)
            if value not in (None, "", []):
                return value, source_name
    return None, "unresolved"


def _build_superconfig_source(device_config: dict[str, Any], rom_info: dict[str, Any]) -> dict[str, Any]:
    """Build a named-source dict from imported HyperUR SuperConfig for this device."""
    codename = str(
        device_config.get("resolved_codename")
        or device_config.get("codename")
        or rom_info.get("codename")
        or ""
    ).strip().lower()
    soc = str(device_config.get("soc") or rom_info.get("soc") or "").strip().lower()
    if not codename:
        return {}
    sc = resolve_super_config_for_device(codename, soc=soc)
    if sc.get("status") != STATUS_READY:
        return {}

    # Build a source dict compatible with the named_sources format
    # SuperConfig provides reliable metadata — expose all needed keys
    result: dict[str, Any] = {
        "super_size": sc.get("super_size"),
        "slot_mode": sc.get("slot_mode"),
        "metadata_slots": sc.get("metadata_slots"),
        "dynamic_group_name": sc.get("group_name"),
        "group_name": sc.get("group_name"),
        "group_size": sc.get("group_size"),
        # partition_sizes derived from SuperConfig partition table
        "partition_sizes": {
            name: entry.get("size", 0)
            for name, entry in (sc.get("partitions") or {}).items()
            if entry.get("size")
        },
    }

    # Build partition table in the format _partition_entries expects
    partition_list = []
    for name, entry in (sc.get("partitions") or {}).items():
        size = entry.get("size", 0)
        if size:
            partition_list.append({
                "name": f"{name}_a",
                "group_name": f"{entry.get('group_name', sc.get('group_name', 'qti_dynamic_partitions'))}_a",
                "size": size,
                "allocation_size": size,
            })
    if partition_list:
        result["partitions"] = partition_list
        result["partition_table"] = partition_list

    result["_super_config_status"] = sc.get("status")
    result["_super_config_codename"] = codename
    result["_super_config_source_label"] = sc.get("source_label", "HyperUR_Build_CN_V21 imported reference")
    return result


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
    payload_metadata = _read_payload_metadata(ws)
    payload_manifest = _read_payload_json(ws, "payload_manifest.json")
    payload_partitions = _read_payload_json(ws, "payload_partitions.json")
    op_list_metadata = _find_op_list(ws)
    if info is not None:
        rom_info.update({k: v for k, v in info.__dict__.items() if v is not None})

    if device_config is None:
        device_config = read_json(ws.meta / "device_registry.json", {})
    if not device_config:
        device_config = resolve_device(rom_metadata=rom_info or device_info, ws=ws)
    profile_super = device_config.get("super") if isinstance(device_config.get("super"), dict) else {}
    soc_super = device_config.get("_soc_super") if isinstance(device_config.get("_soc_super"), dict) else profile_super
    device_super = device_config.get("_device_super") if isinstance(device_config.get("_device_super"), dict) else profile_super

    # Load HyperUR SuperConfig — highest-priority source (overrides payload inspection)
    superconfig_source = _build_superconfig_source(device_config, rom_info)

    detected_sizes = _partition_sizes(super_layout, partition_map)
    for payload_data in [payload_metadata, payload_manifest, payload_partitions]:
        if isinstance(payload_data.get("partition_sizes"), dict):
            detected_sizes.update(_partition_sizes(payload_data, {}))
    if isinstance(op_list_metadata.get("partition_sizes"), dict):
        detected_sizes.update(_partition_sizes(op_list_metadata, {}))
    original_metadata = super_layout if super_layout.get("metadata_source") in {
        "original_super_metadata",
        "super_metadata",
        "lpdump",
    } else {}
    payload_source = dict(super_layout) if detected_sizes else {}
    payload_source.update(payload_metadata)

    # SuperConfig is highest priority — only payload detection can be blocked by it,
    # not the other way around (no override unless forced by debug flag)
    named_sources_base = [
        ("original_super_metadata", original_metadata),
        ("payload_manifest", payload_manifest or payload_source),
        ("payload_partitions", payload_partitions),
        ("dynamic_partitions_op_list", op_list_metadata),
        ("device_profile", device_super),
        ("soc_profile", soc_super),
    ]
    named_sources = (
        [("hyperur_superconfig", superconfig_source)] + named_sources_base
        if superconfig_source
        else named_sources_base
    )

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
        metadata_source = "payload_manifest"

    allocation_sources: dict[str, dict[str, dict[str, Any]]] = {}

    # SuperConfig allocation entries — use partition sizes from imported reference
    if superconfig_source:
        sc_entries = _partition_entries(superconfig_source, "hyperur_superconfig")
        sc_sizes = superconfig_source.get("partition_sizes") if isinstance(superconfig_source.get("partition_sizes"), dict) else {}
        if sc_sizes:
            sc_group = str(superconfig_source.get("group_name") or group_name)
            sc_entries.update(_size_entries(sc_sizes, "hyperur_superconfig", sc_group))
        if sc_entries:
            allocation_sources["hyperur_superconfig"] = sc_entries

    original_entries = _partition_entries(original_metadata, "original_super_metadata")
    if original_entries:
        allocation_sources["original_super_metadata"] = original_entries
    manifest_entries = _partition_entries(payload_manifest or payload_source, "payload_manifest")
    manifest_sizes = _partition_sizes(payload_manifest or payload_source, {})
    if manifest_sizes:
        manifest_entries.update(_size_entries(manifest_sizes, "payload_manifest", group_name))
    if manifest_entries:
        allocation_sources["payload_manifest"] = manifest_entries
    partition_entries = _partition_entries(payload_partitions, "payload_partitions")
    partition_sizes = _partition_sizes(payload_partitions, {})
    if partition_sizes:
        partition_entries.update(_size_entries(partition_sizes, "payload_partitions", group_name))
    if partition_entries:
        allocation_sources["payload_partitions"] = partition_entries
    op_entries = _size_entries(
        op_list_metadata.get("partition_sizes") if isinstance(op_list_metadata.get("partition_sizes"), dict) else {},
        "dynamic_partitions_op_list",
        str(op_list_metadata.get("dynamic_group_name") or group_name),
    )
    for part, entry in op_entries.items():
        groups = op_list_metadata.get("partition_groups") if isinstance(op_list_metadata.get("partition_groups"), dict) else {}
        entry["group_name"] = str(groups.get(part) or entry.get("group_name") or group_name)
    if op_entries:
        allocation_sources["dynamic_partitions_op_list"] = op_entries
    device_sizes = device_super.get("partition_sizes") if isinstance(device_super.get("partition_sizes"), dict) else {}
    device_entries = _size_entries(device_sizes, "device_profile", group_name)
    if device_entries:
        allocation_sources["device_profile"] = device_entries
    soc_sizes = soc_super.get("partition_sizes") if isinstance(soc_super.get("partition_sizes"), dict) else {}
    soc_entries = _size_entries(soc_sizes, "soc_profile", group_name)
    if soc_entries:
        allocation_sources["soc_profile"] = soc_entries

    partitions: dict[str, dict[str, Any]] = {}
    missing_metadata: list[str] = []
    for part in selected:
        image = images[part]
        chosen: dict[str, Any] | None = None
        checked: list[str] = []
        for source_name in SAFE_ALLOCATION_SOURCES:
            checked.append(source_name)
            entry = allocation_sources.get(source_name, {}).get(part)
            if entry and _int_value(entry.get("allocation_size")):
                chosen = dict(entry)
                break
        if chosen is None:
            missing_metadata.append(part)
            partitions[part] = {
                "name": part,
                "slot_suffix": "_a" if is_vab else "",
                "image_path": str(image),
                "image_size": image.stat().st_size,
                "allocation_size": None,
                "group_name": group_name,
                "readonly": True,
                "source": "unresolved",
                "safe_sources_checked": checked,
            }
            continue
        partitions[part] = {
            "name": part,
            "slot_suffix": "_a" if is_vab else "",
            "image_path": str(image),
            "image_size": image.stat().st_size,
            "allocation_size": _int_value(chosen.get("allocation_size")),
            "group_name": str(chosen.get("group_name") or group_name),
            "readonly": bool(chosen.get("readonly", True)),
            "source": str(chosen.get("source") or "unresolved"),
            "safe_sources_checked": checked,
        }
    vab_zero_b = [
        {
            "name": f"{part}_b",
            "base_name": part,
            "allocation_size": 0,
            "group_name": f"{group_name}_b",
            "readonly": True,
            "source": "VAB zero_b",
        }
        for part in selected
    ] if is_vab else []
    resolved_sources = [
        str(entry.get("source"))
        for entry in partitions.values()
        if entry.get("allocation_size") and entry.get("source")
    ]
    allocation_metadata_source = resolved_sources[0] if resolved_sources else "unresolved"

    profile = {
        "metadata_source": allocation_metadata_source if allocation_metadata_source != "unresolved" else metadata_source,
        "geometry_metadata_source": metadata_source,
        "allocation_metadata_source": allocation_metadata_source,
        "metadata_priority": SAFE_ALLOCATION_SOURCES,
        "super_size": target_size,
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
        "allow_super_compaction": bool(profile_super.get("allow_super_compaction") or profile_super.get("allow_compact_super")),
        "partition_sizes": detected_sizes,
        "partition_sizes_source": "detected_metadata" if detected_sizes else "unavailable",
        "partitions": partitions,
        "missing_metadata": missing_metadata,
        "vab_zero_b_partitions": vab_zero_b,
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
        "superconfig_source": superconfig_source.get("_super_config_source_label") if superconfig_source else None,
        "superconfig_codename": superconfig_source.get("_super_config_codename") if superconfig_source else None,
        "superconfig_active": bool(superconfig_source),
    }
    if missing_metadata:
        profile["metadata_source"] = metadata_source or "partial"
    write_json(ws.meta / "super_profile.json", profile)
    write_super_profile_report(ws, profile)
    print(f"[SUPER PROFILE] Source: {profile.get('metadata_source')}")
    if profile.get("superconfig_active"):
        print(f"[SUPER PROFILE] SuperConfig: {profile.get('superconfig_source')} codename={profile.get('superconfig_codename')}")
    print(f"[SUPER PROFILE] Group: {profile.get('dynamic_group_name')} size={profile.get('group_size')}")
    for part, entry in partitions.items():
        print(
            f"[SUPER PROFILE] Partition: {part} allocation={entry.get('allocation_size')} "
            f"source={entry.get('source')}"
        )
        print(f"[SUPER PROFILE] Allocation source: {part}={entry.get('source')}")
    return profile


def write_super_profile_report(ws: Workspace, profile: dict[str, Any]) -> None:
    lines = [
        "DeadZone Super Profile Report",
        "=============================",
        f"device: {profile.get('device', {}).get('codename')} ({profile.get('device', {}).get('name')})",
        f"soc: {profile.get('device', {}).get('soc')}",
        f"source: {profile.get('metadata_source')}",
        f"allocation source: {profile.get('allocation_metadata_source')}",
        f"target super size: {profile.get('target_super_size')}",
        f"group name: {profile.get('dynamic_group_name')} ({profile.get('group_name_source')})",
        f"group size: {profile.get('group_size')} ({profile.get('group_size_source')})",
        f"slot mode: {profile.get('slot_mode')} ({profile.get('slot_mode_source')})",
        f"superconfig active: {profile.get('superconfig_active')} source={profile.get('superconfig_source') or 'none'}",
        f"VAB zero-size _b entries: {profile.get('vab_zero_b')}",
        f"partition size source: {profile.get('partition_sizes_source')}",
        f"payload_manifest.json present: {(ws.meta / 'payload_manifest.json').is_file()}",
        f"payload_partitions.json present: {(ws.meta / 'payload_partitions.json').is_file()}",
        f"missing metadata: {', '.join(profile.get('missing_metadata') or []) or '(none)'}",
        "",
        "dynamic partition allocations:",
    ]
    partitions = profile.get("partitions") if isinstance(profile.get("partitions"), dict) else {}
    for part in profile.get("selected_partitions", []):
        entry = partitions.get(part, {})
        lines.append(
            f"  - {part}: allocation={entry.get('allocation_size')} "
            f"image_size={entry.get('image_size')} source={entry.get('source')} "
            f"group={entry.get('group_name')} checked={', '.join(entry.get('safe_sources_checked') or [])}"
        )
    if not profile.get("selected_partitions"):
        lines.append("  (none)")
    lines += ["", "mi_ext allocation status:"]
    mi_ext = partitions.get("mi_ext")
    if mi_ext:
        lines.append(
            f"  allocation={mi_ext.get('allocation_size')} source={mi_ext.get('source')} "
            f"image={mi_ext.get('image_path')}"
        )
    else:
        lines.append("  (no mi_ext image selected)")
    lines += ["", "VAB zero-size _b entries:"]
    zero_entries = profile.get("vab_zero_b_partitions") or []
    lines.extend(
        [f"  - {entry.get('name')}: allocation={entry.get('allocation_size')} group={entry.get('group_name')}" for entry in zero_entries]
        or ["  (not VAB)"]
    )
    lines.append("")
    (ws.reports / "super_profile_report.txt").write_text("\n".join(lines), encoding="utf-8")
