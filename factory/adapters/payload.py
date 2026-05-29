from __future__ import annotations

import os
import platform
import shutil
import subprocess
import stat
import struct
from pathlib import Path
from typing import Any

from factory.adapters.common import copy_images
from factory.core.detector import DYNAMIC_PARTITIONS
from factory.core.workspace import Workspace, read_json, write_json


MISSING_TOOL_MESSAGE = "payload-dumper-go is missing. Add it to tools/helper or install it in Docker/GitHub runner."


def _base_partition(name: str) -> str:
    return Path(str(name)).stem.removesuffix("_a").removesuffix("_b")


def _slot_suffix(name: str) -> str:
    stem = Path(str(name)).stem
    if stem.endswith("_a"):
        return "_a"
    if stem.endswith("_b"):
        return "_b"
    return ""


def _read_varint(data: bytes, pos: int) -> tuple[int, int]:
    value = 0
    shift = 0
    while pos < len(data):
        byte = data[pos]
        pos += 1
        value |= (byte & 0x7F) << shift
        if not byte & 0x80:
            return value, pos
        shift += 7
        if shift > 70:
            break
    raise ValueError("invalid protobuf varint")


def _skip_field(data: bytes, pos: int, wire_type: int) -> int:
    if wire_type == 0:
        _, pos = _read_varint(data, pos)
        return pos
    if wire_type == 1:
        return pos + 8
    if wire_type == 2:
        length, pos = _read_varint(data, pos)
        return pos + length
    if wire_type == 5:
        return pos + 4
    raise ValueError(f"unsupported protobuf wire type {wire_type}")


def _iter_fields(data: bytes):
    pos = 0
    while pos < len(data):
        key, pos = _read_varint(data, pos)
        field = key >> 3
        wire_type = key & 0x7
        value_pos = pos
        pos = _skip_field(data, pos, wire_type)
        yield field, wire_type, data[value_pos:pos]


def _field_bytes(value: bytes) -> bytes:
    length, pos = _read_varint(value, 0)
    return value[pos:pos + length]


def _field_string(value: bytes) -> str:
    return _field_bytes(value).decode("utf-8", errors="replace")


def _field_varint(value: bytes) -> int:
    parsed, _ = _read_varint(value, 0)
    return parsed


def _payload_manifest_bytes(payload_bin: Path) -> bytes:
    header_fmt = ">4sQQI"
    header_size = struct.calcsize(header_fmt)
    with payload_bin.open("rb") as fh:
        magic, _version, manifest_len, _sig_len = struct.unpack(header_fmt, fh.read(header_size))
        if magic != b"CrAU":
            raise ValueError("payload.bin has invalid magic")
        if manifest_len <= 0:
            raise ValueError("payload.bin manifest length is zero")
        return fh.read(manifest_len)


def _parse_partition_info(data: bytes) -> dict[str, int]:
    info: dict[str, int] = {}
    for field, wire_type, value in _iter_fields(data):
        if field == 1 and wire_type == 0:
            info["size"] = _field_varint(value)
    return info


def _parse_partition_update(data: bytes) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for field, wire_type, value in _iter_fields(data):
        if field == 1 and wire_type == 2:
            result["partition_name"] = _field_string(value)
        elif field == 7 and wire_type == 2:
            result["new_partition_info"] = _parse_partition_info(_field_bytes(value))
    return result


def _parse_dynamic_group(data: bytes) -> dict[str, Any]:
    group: dict[str, Any] = {"partition_names": []}
    for field, wire_type, value in _iter_fields(data):
        if field == 1 and wire_type == 2:
            group["name"] = _field_string(value)
        elif field == 2 and wire_type == 0:
            group["size"] = _field_varint(value)
        elif field == 3 and wire_type == 2:
            group["partition_names"].append(_field_string(value))
    return group


def _parse_manifest(data: bytes) -> dict[str, Any]:
    manifest: dict[str, Any] = {"partitions": [], "dynamic_groups": [], "block_size": 4096}
    for field, wire_type, value in _iter_fields(data):
        if field == 3 and wire_type == 0:
            manifest["block_size"] = _field_varint(value)
        elif field == 13 and wire_type == 2:
            manifest["partitions"].append(_parse_partition_update(_field_bytes(value)))
        elif field == 15 and wire_type == 2:
            dpm = _field_bytes(value)
            for group_field, group_wire, group_value in _iter_fields(dpm):
                if group_field == 1 and group_wire == 2:
                    manifest["dynamic_groups"].append(_parse_dynamic_group(_field_bytes(group_value)))
    return manifest


def _payload_metadata(payload_bin: Path) -> dict[str, Any]:
    try:
        manifest = _parse_manifest(_payload_manifest_bytes(payload_bin))
    except Exception as exc:
        return {
            "metadata_source": "unavailable",
            "extraction_method": "minimal_payload_manifest_parser",
            "error": str(exc),
            "partition_sizes": {},
            "partitions": [],
        }

    partition_sizes: dict[str, int] = {}
    partitions: list[dict[str, Any]] = []
    group_by_part: dict[str, str] = {}
    groups = [g for g in manifest.get("dynamic_groups", []) if g.get("name") and g.get("name") != "default"]
    for group in groups:
        group_name = str(group.get("name") or "").removesuffix("_a").removesuffix("_b")
        for raw in group.get("partition_names") or []:
            group_by_part[_base_partition(str(raw))] = group_name

    for part in manifest.get("partitions", []) or []:
        raw_name = str(part.get("partition_name") or "")
        base = _base_partition(raw_name)
        info = part.get("new_partition_info") if isinstance(part.get("new_partition_info"), dict) else {}
        size = int(info.get("size") or 0)
        dynamic = base in group_by_part or base in DYNAMIC_PARTITIONS
        item = {
            "name": base,
            "partition_name": raw_name,
            "slot_suffix": _slot_suffix(raw_name),
            "allocation_size": size if size > 0 else None,
            "new_partition_size": size if size > 0 else None,
            "dynamic": dynamic,
            "group": group_by_part.get(base, ""),
            "source": "payload_manifest",
        }
        partitions.append(item)
        if not dynamic:
            continue
        if size > 0:
            partition_sizes[base] = size

    group_name = ""
    group_size = 0
    group_partitions: list[str] = []
    if groups:
        group = max(groups, key=lambda item: int(item.get("size") or 0))
        group_name = str(group.get("name") or "").removesuffix("_a").removesuffix("_b")
        group_size = int(group.get("size") or 0)
        seen: set[str] = set()
        for raw in group.get("partition_names") or []:
            base = _base_partition(str(raw))
            if base and base not in seen:
                seen.add(base)
                group_partitions.append(base)

    return {
        "metadata_source": "payload_manifest",
        "extraction_method": "minimal_payload_manifest_parser",
        "manifest_path": str(payload_bin),
        "block_size": int(manifest.get("block_size") or 4096),
        "dynamic_group_name": group_name,
        "group_size": group_size,
        "group_partitions": group_partitions,
        "partitions": partitions,
        "partition_sizes": dict(sorted(partition_sizes.items())),
    }


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


def _resolve_payload_tool() -> Path | None:
    for candidate in _helper_candidates("payload-dumper-go"):
        if candidate.is_file():
            if os.name == "posix":
                try:
                    candidate.chmod(candidate.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                except OSError:
                    pass
            return candidate.resolve()
    found = shutil.which("payload-dumper-go") or shutil.which("payload-dumper-go.exe")
    return Path(found).resolve() if found else None


def _stage_payload_files(extracted: Path, ws: Workspace) -> Path:
    payloads = sorted(extracted.rglob("payload.bin"))
    if not payloads:
        raise RuntimeError("payload.bin not found")

    payload_dir = ws.extracted / "payload"
    payload_dir.mkdir(parents=True, exist_ok=True)
    staged_payload = payload_dir / "payload.bin"
    if payloads[0].resolve() != staged_payload.resolve():
        shutil.copy2(payloads[0], staged_payload)

    for props in sorted(extracted.rglob("payload_properties.txt")):
        staged_props = payload_dir / "payload_properties.txt"
        if props.resolve() != staged_props.resolve():
            shutil.copy2(props, staged_props)
        break
    return staged_payload


def _dumped_images(ws: Workspace) -> list[Path]:
    return sorted(p for p in ws.images.glob("*.img") if p.is_file() and p.stat().st_size > 0)


def _first_lines(path: Path, count: int = 50) -> list[str]:
    if not path.is_file():
        return []
    return path.read_text(encoding="utf-8", errors="replace").splitlines()[:count]


def _write_payload_report(
    ws: Workspace,
    *,
    tool: Path | None,
    command: list[str],
    exit_code: int | None,
    images: list[Path],
    payload_metadata: dict[str, Any],
    error: str = "",
) -> Path:
    stderr_path = ws.logs / "payload_dump_stderr.log"
    report_path = ws.reports / "payload_unpack_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    stderr_lines = _first_lines(stderr_path, 50)
    manifest_path = ws.meta / "payload_manifest.json"
    partitions_path = ws.meta / "payload_partitions.json"
    parts = payload_metadata.get("partitions") if isinstance(payload_metadata.get("partitions"), list) else []
    mi_ext = next((item for item in parts if isinstance(item, dict) and item.get("name") == "mi_ext"), {})
    allocation_lines = [
        "  - {name}: allocation={allocation} dynamic={dynamic} group={group} source={source}".format(
            name=item.get("name"),
            allocation=item.get("allocation_size"),
            dynamic=item.get("dynamic"),
            group=item.get("group") or "(none)",
            source=item.get("source"),
        )
        for item in parts
        if isinstance(item, dict)
    ] or ["  (none)"]
    lines = [
        "MEZO / DeadZone Payload Unpack Report",
        "=====================================",
        f"tool path: {tool or '(missing)'}",
        f"command: {' '.join(command) if command else '(not run)'}",
        f"exit code: {exit_code if exit_code is not None else '(not run)'}",
        f"payload metadata extraction method: {payload_metadata.get('extraction_method') or '(none)'}",
        f"payload_manifest.json created: {manifest_path.is_file()}",
        f"payload_partitions.json created: {partitions_path.is_file()}",
        f"dynamic group: {payload_metadata.get('dynamic_group_name') or '(none)'}",
        f"group size: {payload_metadata.get('group_size') or '(none)'}",
        f"mi_ext allocation status: {mi_ext.get('allocation_size') or '(missing)'} source={mi_ext.get('source') or '(none)'}",
        f"output directory: {ws.images}",
        f"found image count: {len(images)}",
        f"images: {', '.join(p.name for p in images) if images else '(none)'}",
        f"error: {error or '(none)'}",
        "",
        "partition allocations:",
        *allocation_lines,
        "",
        "first 50 lines of stderr:",
        *(stderr_lines or ["(none)"]),
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def _update_payload_metadata(ws: Workspace, images: list[Path], dumped: bool, payload_metadata: dict[str, Any]) -> None:
    image_names = [p.name for p in images]
    partition_map = read_json(ws.meta / "partition_map.json", {})
    by_partition = partition_map.get("by_partition") if isinstance(partition_map.get("by_partition"), dict) else {}
    by_partition.update({p.stem.removesuffix("_a").removesuffix("_b"): str(p.relative_to(ws.root)) for p in images})
    partition_map["by_partition"] = dict(sorted(by_partition.items()))
    if payload_metadata.get("partition_sizes"):
        partition_map["partition_sizes"] = payload_metadata["partition_sizes"]
        partition_map["partition_size_source"] = "payload_manifest"
    if payload_metadata.get("dynamic_group_name"):
        partition_map["dynamic_group_name"] = payload_metadata["dynamic_group_name"]
    if payload_metadata.get("group_size"):
        partition_map["group_size"] = payload_metadata["group_size"]
    seen = set(partition_map.get("source_images_seen") or [])
    seen.update(image_names)
    partition_map["source_images_seen"] = sorted(seen)
    write_json(ws.meta / "partition_map.json", partition_map)

    rom_info = read_json(ws.meta / "rom_info.json", {})
    rom_info.update({
        "has_payload": True,
        "payload_dumped": dumped,
        "payload_image_count": len(images),
    })
    write_json(ws.meta / "rom_info.json", rom_info)

    write_json(ws.meta / "payload_metadata.json", payload_metadata)
    manifest_data = dict(payload_metadata)
    manifest_data["manifest_json"] = str(ws.meta / "payload_manifest.json")
    write_json(ws.meta / "payload_manifest.json", manifest_data)
    write_json(
        ws.meta / "payload_partitions.json",
        {
            "metadata_source": payload_metadata.get("metadata_source") or "payload_manifest",
            "extraction_method": payload_metadata.get("extraction_method") or "",
            "dynamic_group_name": payload_metadata.get("dynamic_group_name") or "",
            "group_size": payload_metadata.get("group_size") or 0,
            "partitions": payload_metadata.get("partitions") if isinstance(payload_metadata.get("partitions"), list) else [],
            "partition_sizes": payload_metadata.get("partition_sizes") if isinstance(payload_metadata.get("partition_sizes"), dict) else {},
        },
    )
    super_layout = read_json(ws.meta / "super_layout.json", {})
    if payload_metadata.get("partition_sizes"):
        super_layout["partition_sizes"] = payload_metadata["partition_sizes"]
        super_layout["partition_size_source"] = "payload_manifest"
        super_layout["metadata_source"] = "payload_dynamic_partition_metadata"
    if payload_metadata.get("dynamic_group_name"):
        super_layout["dynamic_group_name"] = payload_metadata["dynamic_group_name"]
    if payload_metadata.get("group_size"):
        super_layout["group_size"] = payload_metadata["group_size"]
    if payload_metadata.get("group_partitions"):
        super_layout["dynamic_group_partitions"] = payload_metadata["group_partitions"]
    write_json(ws.meta / "super_layout.json", super_layout)


def adapt(extracted: Path, ws: Workspace) -> dict:
    payload_bin = _stage_payload_files(extracted, ws)
    payload_metadata = _payload_metadata(payload_bin)
    sizes = payload_metadata.get("partition_sizes") if isinstance(payload_metadata.get("partition_sizes"), dict) else {}
    stdout_path = ws.logs / "payload_dump_stdout.log"
    stderr_path = ws.logs / "payload_dump_stderr.log"
    stdout_path.write_text("", encoding="utf-8")
    stderr_path.write_text("", encoding="utf-8")

    tool = _resolve_payload_tool()
    command: list[str] = []
    exit_code: int | None = None
    if tool is None:
        images = _dumped_images(ws)
        _update_payload_metadata(ws, images, dumped=False, payload_metadata=payload_metadata)
        _write_payload_report(ws, tool=tool, command=command, exit_code=exit_code, images=images, payload_metadata=payload_metadata, error=MISSING_TOOL_MESSAGE)
        print("[PAYLOAD] Tool: (missing)")
        print("[PAYLOAD] Command: (not run)")
        print(f"[PAYLOAD] Output: {ws.images}")
        print(f"[PAYLOAD] Manifest metadata: method={payload_metadata.get('extraction_method')} partitions={len(payload_metadata.get('partitions') or [])}")
        for name, size in sorted(sizes.items()):
            print(f"[PAYLOAD] Partition allocation: {name}={size} source=payload_manifest")
        print(f"[PAYLOAD] Images dumped: {len(images)}")
        raise RuntimeError(MISSING_TOOL_MESSAGE)

    command = [str(tool), "-o", str(ws.images), str(payload_bin)]
    print(f"[PAYLOAD] Tool: {tool}")
    print(f"[PAYLOAD] Command: {' '.join(command)}")
    print(f"[PAYLOAD] Output: {ws.images}")
    with stdout_path.open("w", encoding="utf-8") as stdout, stderr_path.open("w", encoding="utf-8") as stderr:
        result = subprocess.run(command, stdout=stdout, stderr=stderr)
    exit_code = result.returncode
    ok = exit_code == 0 and bool(_dumped_images(ws))

    images = _dumped_images(ws)
    _update_payload_metadata(ws, images, dumped=ok, payload_metadata=payload_metadata)
    _write_payload_report(ws, tool=tool, command=command, exit_code=exit_code, images=images, payload_metadata=payload_metadata)
    print(f"[PAYLOAD] Manifest metadata: method={payload_metadata.get('extraction_method')} partitions={len(payload_metadata.get('partitions') or [])}")
    for name, size in sorted(sizes.items()):
        print(f"[PAYLOAD] Partition allocation: {name}={size} source=payload_manifest")
    print(f"[PAYLOAD] Images dumped: {len(images)}")
    if not ok:
        _write_payload_report(
            ws,
            tool=tool,
            command=command,
            exit_code=exit_code,
            images=images,
            payload_metadata=payload_metadata,
            error="payload-dumper-go ran but produced no images",
        )
        raise RuntimeError(
            f"payload-dumper-go ran but produced no images. See {ws.reports / 'payload_unpack_report.txt'}"
        )
    return {"adapter": "payload", "images": copy_images(ws.images, ws.images), "partition_sizes": sizes}
