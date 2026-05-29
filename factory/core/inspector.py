from __future__ import annotations

from pathlib import Path

from factory.core.detector import DYNAMIC_PARTITIONS, RomInfo
from factory.core.workspace import Workspace, write_json


def inspect_workspace(ws: Workspace, info: RomInfo, unpack_result: dict) -> dict:
    images = sorted(p.name for p in ws.images.rglob("*.img"))
    dynamic = sorted(n for n in images if Path(n).stem.removesuffix("_a").removesuffix("_b") in DYNAMIC_PARTITIONS)
    firmware = sorted(n for n in images if n not in dynamic and n != "super.img")
    partition_map = {
        Path(n).stem.removesuffix("_a").removesuffix("_b"): n
        for n in images
        if Path(n).stem.removesuffix("_a").removesuffix("_b") in DYNAMIC_PARTITIONS
    }
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
        "unpack": unpack_result,
    }
    write_json(ws.meta / "inspection.json", report)
    write_json(ws.meta / "partition_map.json", {
        "dynamic_partitions": sorted(DYNAMIC_PARTITIONS),
        "by_partition": partition_map,
        "source_images_seen": images,
    })
    return report
