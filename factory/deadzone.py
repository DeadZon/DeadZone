from __future__ import annotations

import argparse
from pathlib import Path

from factory.core.cleanup import cleanup
from factory.core.detector import detect_rom
from factory.core.downloader import download_rom
from factory.core.final_zip import build_final_zip
from factory.core.inspector import inspect_workspace
from factory.core.repacker import repack_partitions
from factory.core.style_runner import apply_style, normalize_style
from factory.core.super_builder import build_super
from factory.core.unpacker import unpack_rom
from factory.core.workspace import create_workspace


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="DeadZone universal ROM builder")
    parser.add_argument("--rom-url", required=True)
    parser.add_argument("--style", required=True, choices=["Stable", "Legend", "Gaming", "EPiC", "stable", "legend", "gaming", "epic"])
    parser.add_argument("--soc", required=True, choices=["mtk", "snapdragon"])
    parser.add_argument("--custom-codename", default="")
    parser.add_argument("--mode", default="build")
    parser.add_argument("--upload-pixeldrain", action="store_true")
    parser.add_argument("--notify-telegram", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    style_key, _ = normalize_style(args.style)
    ws = create_workspace(Path("output/workspace"), clean=True)
    source = download_rom(args.rom_url, ws)
    info = detect_rom(source, ws, soc=args.soc, custom_codename=args.custom_codename)
    unpack_result = unpack_rom(source, info, ws)
    inspection = inspect_workspace(ws, info, unpack_result)
    apply_style(style_key, ws, info)
    repack_partitions(ws)
    inspection = inspect_workspace(ws, info, unpack_result)
    build_super(ws, info, inspection)
    final_zip = build_final_zip(ws, info, style_key)
    cleanup(ws, keep_workspace=True)
    print(f"[DONE] {final_zip}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
