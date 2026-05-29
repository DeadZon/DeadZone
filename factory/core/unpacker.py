from __future__ import annotations

from pathlib import Path

from factory.adapters.common import extract_archive
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


def unpack_rom(source: Path, info: RomInfo, ws: Workspace) -> dict:
    print("[UNPACK] normalizing source into output/workspace")
    extract_archive(source, ws.extracted)
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
