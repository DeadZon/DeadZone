from __future__ import annotations

from pathlib import Path

from factory.adapters.common import copy_images, merge_split_images
from factory.core.workspace import Workspace


def adapt(extracted: Path, ws: Workspace) -> dict:
    merged = merge_split_images(extracted, ws.images / "super.img")
    images = copy_images(extracted, ws.images)
    converted: list[str] = []
    if any(extracted.rglob("*.new.dat.br")):
        from factory.adapters import new_dat

        result = new_dat.adapt(extracted, ws)
        converted = result.get("images") or []
        images.extend(converted)
    if merged:
        images.append("super.img")
    if not images:
        raise RuntimeError("Xiaomi EU archive contained no supported images")
    return {
        "adapter": "eu",
        "images": sorted(set(images)),
        "converted_new_dat": sorted(set(converted)),
        "merged_super": bool(merged),
    }
