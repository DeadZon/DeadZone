"""
ROM archive detection and extraction.

Logic extracted from MEZOBuildRom.py:
  - extract_tar_safe()  → lines 133-139  (path-traversal-safe tar extraction)
  - extract_rom()       → lines 142-166  (ZIP / TGZ / TAR / bare-img dispatch)

These functions use only stdlib (zipfile, tarfile, shutil, pathlib) so they are
copied inline rather than imported from the legacy module to avoid the
os.chdir() side-effect that MEZOBuildRom triggers at import time.
"""
from __future__ import annotations

import os
import shutil
import tarfile
import zipfile
from pathlib import Path

# ── Archive-type constants ────────────────────────────────────────────────────
ARCHIVE_ZIP = "zip"
ARCHIVE_TAR_GZ = "tar.gz"
ARCHIVE_TGZ = "tgz"
ARCHIVE_TAR = "tar"
ARCHIVE_IMG = "img"
ARCHIVE_DIR = "dir"
ARCHIVE_UNKNOWN = "unknown"


def detect_archive_type(rom_path: Path) -> str:
    """Return a short label for the input type (used in reports)."""
    if rom_path.is_dir():
        return ARCHIVE_DIR
    name = rom_path.name.lower()
    if name.endswith(".zip"):
        return ARCHIVE_ZIP
    if name.endswith(".tar.gz"):
        return ARCHIVE_TAR_GZ
    if name.endswith(".tgz"):
        return ARCHIVE_TGZ
    if name.endswith(".tar"):
        return ARCHIVE_TAR
    if name.endswith(".img"):
        return ARCHIVE_IMG
    return ARCHIVE_UNKNOWN


# ── legacy-extracted from MEZOBuildRom.py:extract_tar_safe (lines 133-139) ──
def extract_tar_safe(archive: tarfile.TarFile, dest: Path) -> None:
    """Extract a tar archive while rejecting path-traversal entries."""
    dest_abs = dest.resolve()
    for member in archive.getmembers():
        member_path = (dest / member.name).resolve()
        if os.path.commonpath([str(dest_abs), str(member_path)]) != str(dest_abs):
            raise RuntimeError(f"Invalid tar entry (path traversal): {member.name}")
    archive.extractall(dest)


# ── legacy-extracted from MEZOBuildRom.py:extract_rom (lines 142-166) ────────
def extract_rom(rom_path: Path, output_dir: Path) -> Path:
    """
    Extract a ROM archive into output_dir/rom/ and return that sub-directory.

    Supported input types:
      .zip            → ZipFile extraction
      .tgz / .tar.gz  → gzip-compressed tar extraction (path-traversal safe)
      .tar            → uncompressed tar extraction   (path-traversal safe)
      anything else   → copied as-is (handles bare .img inputs)
    """
    rom_extract_dir = output_dir / "rom"
    rom_extract_dir.mkdir(parents=True, exist_ok=True)

    name_lower = rom_path.name.lower()
    print(f"[archive] Extracting ROM: {rom_path.name}")

    if name_lower.endswith(".zip"):
        with zipfile.ZipFile(rom_path, "r") as zf:
            zf.extractall(rom_extract_dir)
        return rom_extract_dir

    if name_lower.endswith((".tgz", ".tar.gz")):
        with tarfile.open(rom_path, "r:gz") as tf:
            extract_tar_safe(tf, rom_extract_dir)
        return rom_extract_dir

    if name_lower.endswith(".tar"):
        with tarfile.open(rom_path, "r") as tf:
            extract_tar_safe(tf, rom_extract_dir)
        return rom_extract_dir

    # Bare .img or unknown — copy it into the work dir so the rest of the
    # pipeline can treat it like any other extracted directory.
    copied = rom_extract_dir / rom_path.name
    shutil.copy2(rom_path, copied)
    return rom_extract_dir
