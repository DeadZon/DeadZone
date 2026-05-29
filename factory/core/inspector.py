from __future__ import annotations

from pathlib import Path

from factory.core.detector import DYNAMIC_PARTITIONS, RomInfo
from factory.core.workspace import Workspace, write_json


def inspect_workspace(ws: Workspace, info: RomInfo, unpack_result: dict) -> dict:
    images = sorted(p.name for p in ws.images.glob("*.img"))
    dynamic = sorted(n for n in images if Path(n).stem.replace("_a", "").replace("_b", "") in DYNAMIC_PARTITIONS)
    firmware = sorted(n for n in images if n not in dynamic and n != "super.img")
    report = {
        "image_count": len(images),
        "images": images,
        "dynamic_partition_images": dynamic,
        "firmware_images": firmware,
        "has_super": "super.img" in images,
        "needs_super_rebuild": info.super_rebuild_required or "super.img" not in images,
        "unpack": unpack_result,
    }
    write_json(ws.meta / "inspection.json", report)
    return report
