from __future__ import annotations

import os
import shutil
import tarfile
import zipfile
from pathlib import Path

from factory.core.detector import (
    ROM_EU,
    ROM_FASTBOOT_TGZ,
    ROM_FASTBOOT_ZIP,
    ROM_IMAGES,
    ROM_NEW_DAT,
    ROM_PAYLOAD,
    ROM_RAW_SUPER,
    ROM_SPLIT_SUPER,
    RomInfo,
)
from factory.core.workspace import Workspace, write_json


def _safe_destination(root: Path, member_name: str) -> Path:
    root_abs = root.resolve()
    target = (root / member_name).resolve()
    if os.path.commonpath([str(root_abs), str(target)]) != str(root_abs):
        raise RuntimeError(f"archive member escapes workspace: {member_name}")
    return target


def _extract_zip_safe(src: Path, dst: Path) -> None:
    with zipfile.ZipFile(src) as zf:
        for info in zf.infolist():
            _safe_destination(dst, info.filename)
        zf.extractall(dst)


def _extract_tar_safe(src: Path, dst: Path) -> None:
    with tarfile.open(src, "r:*") as tf:
        for member in tf.getmembers():
            _safe_destination(dst, member.name)
        tf.extractall(dst)


def _extract_archive(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)
    elif zipfile.is_zipfile(src):
        _extract_zip_safe(src, dst)
    elif tarfile.is_tarfile(src):
        _extract_tar_safe(src, dst)
    else:
        shutil.copy2(src, dst / src.name)


def unpack_rom(source: Path, info: RomInfo, ws: Workspace) -> dict:
    print("[UNPACK] normalizing source into output/workspace")
    _extract_archive(source, ws.extracted)
    if info.rom_type == ROM_PAYLOAD:
        from factory.adapters import payload as adapter
    elif info.rom_type in {ROM_FASTBOOT_TGZ, ROM_FASTBOOT_ZIP}:
        from factory.adapters import fastboot as adapter
    elif info.rom_type == ROM_EU:
        from factory.adapters import eu as adapter
    elif info.rom_type in {ROM_RAW_SUPER, ROM_SPLIT_SUPER}:
        from factory.adapters import super as adapter
    elif info.rom_type == ROM_NEW_DAT:
        from factory.adapters import new_dat as adapter
    elif info.rom_type == ROM_IMAGES:
        from factory.adapters import images as adapter
    else:
        raise RuntimeError(f"unsupported ROM type: {info.rom_type}")
    result = adapter.adapt(ws.extracted, ws)
    write_json(ws.meta / "unpack_result.json", result)
    print(f"[UNPACK] Adapter: {result.get('adapter')}")
    print(f"[UNPACK] Images: {len(result.get('images') or [])}")
    return result
