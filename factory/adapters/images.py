from __future__ import annotations

from pathlib import Path

from factory.adapters.common import copy_images
from factory.core.workspace import Workspace


def adapt(extracted: Path, ws: Workspace) -> dict:
    images = copy_images(extracted, ws.images)
    if not images:
        raise RuntimeError("images-folder ROM contained no .img files")
    return {"adapter": "images", "images": images}
