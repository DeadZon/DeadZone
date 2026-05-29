from __future__ import annotations

from pathlib import Path

from factory.core.detector import DYNAMIC_PARTITIONS, RomInfo
from factory.core.workspace import Workspace, read_json, write_json


def _positive_int(value: object) -> int:
    try:
        parsed = int(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0
    return parsed if parsed > 0 else 0


def inspect_workspace(ws: Workspace, info: RomInfo, unpack_result: dict) -> dict:
    images = sorted(p.name for p in ws.images.rglob("*.img"))
    dynamic = sorted(n for n in images if Path(n).stem.removesuffix("_a").removesuffix("_b") in DYNAMIC_PARTITIONS)
    firmware = sorted(n for n in images if n not in dynamic and n != "super.img")
    partition_map = {
        Path(n).stem.removesuffix("_a").removesuffix("_b"): n
        for n in images
        if Path(n).stem.removesuffix("_a").removesuffix("_b") in DYNAMIC_PARTITIONS
    }
    partition_sizes = {}
    for name, size in (unpack_result.get("partition_sizes") or {}).items():
        partition = Path(str(name)).stem.removesuffix("_a").removesuffix("_b")
        parsed_size = _positive_int(size)
        if partition in DYNAMIC_PARTITIONS and parsed_size:
            partition_sizes[partition] = parsed_size
    metadata_source = "payload_metadata" if partition_sizes else "workspace_scan"
    report = {
        "image_count": len(images),
        "images": images,
        "dynamic_partition_images": dynamic,
        "firmware_images": firmware,
        "has_super": "super.img" in images,
        "has_payload": info.has_payload,
        "source_has_super": info.has_super,
        "needs_super_rebuild": info.needs_super_rebuild or "super.img" not in images,
        "partition_map": partition_map,
        "partition_sizes": partition_sizes,
        "metadata_source": metadata_source,
        "unpack": unpack_result,
    }
    write_json(ws.meta / "inspection.json", report)
    write_json(ws.meta / "partition_map.json", {
        "dynamic_partitions": sorted(DYNAMIC_PARTITIONS),
        "by_partition": partition_map,
        "partition_sizes": partition_sizes,
        "metadata_source": metadata_source,
        "source_images_seen": images,
    })
    super_layout = read_existing_super_layout(ws)
    super_layout.update({
        "metadata_source": metadata_source,
        "partition_sizes": partition_sizes,
        "dynamic_group_name": super_layout.get("dynamic_group_name") or "qti_dynamic_partitions",
        "default_target_super_size": int(super_layout.get("default_target_super_size") or 8_500_000_000),
        "needs_super_rebuild": report["needs_super_rebuild"],
        "rebuild_required": report["needs_super_rebuild"],
    })
    write_json(ws.meta / "super_layout.json", super_layout)
    return report


def read_existing_super_layout(ws: Workspace) -> dict:
    path = ws.meta / "super_layout.json"
    if not path.is_file():
        return {}
    return read_json(path, {})
