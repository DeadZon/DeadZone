from __future__ import annotations

import re
import shutil
import tarfile
import zipfile
from pathlib import Path


def extract_archive(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)
    elif zipfile.is_zipfile(src):
        with zipfile.ZipFile(src) as zf:
            zf.extractall(dst)
    elif tarfile.is_tarfile(src):
        with tarfile.open(src, "r:*") as tf:
            tf.extractall(dst)
    else:
        shutil.copy2(src, dst / src.name)


def copy_images(src: Path, images_dir: Path) -> list[str]:
    images_dir.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    for img in sorted(src.rglob("*.img")):
        if img.is_file():
            target = images_dir / img.name
            if img.resolve() != target.resolve():
                shutil.copy2(img, target)
            copied.append(target.name)
    return sorted(set(copied))


def merge_split_images(root: Path, output: Path, prefix: str = "super.img") -> Path | None:
    parts = sorted(root.rglob(f"{prefix}.*"), key=lambda p: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", p.name)])
    parts = [p for p in parts if re.search(r"\.\d+$", p.name)]
    if len(parts) < 2:
        return None
    nums = [int(p.name.rsplit(".", 1)[1]) for p in parts]
    if nums != list(range(len(parts))):
        raise RuntimeError(f"{prefix} parts are not contiguous: {nums}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as dst:
        for part in parts:
            with part.open("rb") as src:
                shutil.copyfileobj(src, dst, length=8 * 1024 * 1024)
    return output
