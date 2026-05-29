from __future__ import annotations

import shutil
from pathlib import Path

from factory.adapters.common import merge_split_images
from factory.core.workspace import Workspace


def adapt(extracted: Path, ws: Workspace) -> dict:
    merged = merge_split_images(extracted, ws.images / "super.img")
    if merged:
        return {"adapter": "super", "images": ["super.img"], "merged_super": True}
    supers = list(extracted.rglob("super.img"))
    if not supers and extracted.name == "super.img":
        supers = [extracted]
    if not supers:
        raise RuntimeError("super.img not found")
    shutil.copy2(supers[0], ws.images / "super.img")
    return {"adapter": "super", "images": ["super.img"], "merged_super": False}
