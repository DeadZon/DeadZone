"""
super.img detection, unpacking, and partition extraction.

find_super_img() is copied inline from MEZOBuildRom.py (lines 266-283) because
it has zero external dependencies — only stdlib pathlib.

unpack_super_img() and extract_partitions() delegate to the legacy
implementations in MEZOBuildRom.py:
  - unpack_super()                → lines 6457-6468
  - extract_partitions_from_super() → lines 6661-6677

Those functions depend on:
  src.core.lpunpack   (SparseImage, lpunpack_unpack, lpunpack_get_info)
  src.core.imgextractor
  src.core.contextpatch, fspatch
  src.core.utils (gettype, simg2img, JsonEdit)

We import them lazily through payload._legacy() which handles sys.path setup
and CWD save/restore on the first import of MEZOBuildRom.
"""
from __future__ import annotations

from pathlib import Path

from factory.unpack.payload import _legacy  # reuse the lazy-import helper


# ── legacy-extracted from MEZOBuildRom.py:find_super_img (lines 266-283) ────
def find_super_img(search_dir: Path) -> Path | None:
    """
    Search *search_dir* recursively for super.img.

    Prefers exact name match (super.img) over prefix match (super*.img).
    Returns the first match found, or None.
    """
    exact: list[Path] = []
    partial: list[Path] = []

    for path in search_dir.rglob("*"):
        if not path.is_file():
            continue
        lower = path.name.lower()
        if lower == "super.img":
            exact.append(path)
        elif lower.startswith("super") and lower.endswith(".img"):
            partial.append(path)

    if exact:
        return exact[0]
    if partial:
        return partial[0]
    return None


def unpack_super_img(super_img: Path, output_dir: Path) -> Path:
    """
    Delegate to MEZOBuildRom.unpack_super (lines 6457-6468).

    Converts a sparse super.img to raw if needed, then unpacks it with
    lpunpack into output_dir/super/.  Returns the super/ directory path.
    """
    m = _legacy()
    return m.unpack_super(super_img, output_dir)


def extract_partitions(
    super_out_dir: Path,
    output_dir: Path,
    super_img: Path,
) -> None:
    """
    Delegate to MEZOBuildRom.extract_partitions_from_super (lines 6661-6677).

    Normalises _a slot images, writes config/super, and extracts each
    partition directory (ext4 via imgextractor, erofs via extract.erofs).
    No patching of any kind is performed.
    """
    m = _legacy()
    m.extract_partitions_from_super(super_out_dir, output_dir, super_img)
