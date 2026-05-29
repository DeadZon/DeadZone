from __future__ import annotations

import shutil
from typing import Any

from factory.core.detector import RomInfo
from factory.core.super_builder import DYNAMIC_IMAGES, build_super_image
from factory.core.workspace import Workspace, write_json


def repack_partitions(ws: Workspace) -> dict:
    # Placeholder for filesystem-aware repack after styles mutate mounted partitions.
    # Existing .img files are already normalized in workspace/images.
    staged = []
    for img in ws.images.glob("*.img"):
        if img.name in DYNAMIC_IMAGES:
            target = ws.partitions / img.name
            if img.resolve() != target.resolve():
                shutil.copy2(img, target)
            staged.append(img.name)
    result = {"status": "OK", "dynamic_images_staged": sorted(staged)}
    write_json(ws.meta / "repack_result.json", result)
    print(f"[REPACK] Dynamic images staged: {len(staged)}")
    return result


def build_repacked_super(ws: Workspace, info: RomInfo, inspection: dict[str, Any]) -> dict[str, Any]:
    return build_super_image(ws, info, inspection)
