from __future__ import annotations

import argparse
from pathlib import Path

from factory.core.cleanup import cleanup
from factory.core.detector import detect_rom
from factory.core.device_registry import list_devices, resolve_device
from factory.core.downloader import download_rom
from factory.core.final_zip import build_final_zip
from factory.core.inspector import inspect_workspace
from factory.core.repacker import build_repacked_super, repack_partitions
from factory.core.style_runner import apply_style, normalize_style
from factory.core.unpacker import unpack_rom
from factory.core.workspace import create_workspace


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="DeadZone universal ROM builder")
    parser.add_argument("--rom-url")
    parser.add_argument("--style", choices=["Stable", "Legend", "Gaming", "EPiC", "stable", "legend", "gaming", "epic"])
    parser.add_argument("--soc", choices=["mtk", "snapdragon"])
    parser.add_argument("--custom-codename", default="")
    parser.add_argument("--mode", default="build")
    parser.add_argument("--list-devices", action="store_true")
    parser.add_argument("--show-device", default="")
    parser.add_argument("--upload-pixeldrain", action="store_true")
    parser.add_argument("--notify-telegram", action="store_true")
    return parser.parse_args()


def _print_device(device: dict) -> None:
    print(f"[DEVICE] Codename: {device.get('resolved_codename') or device.get('codename')}")
    print(f"[DEVICE] Name: {device.get('name')}")
    print(f"[SOC] {device.get('soc')}")
    print(f"[PROFILE] Source: {device.get('profile_source')}")
    super_cfg = device.get("super") if isinstance(device.get("super"), dict) else {}
    print(f"[SUPER PROFILE] Source: {super_cfg.get('metadata_source') or device.get('device_source')}")


def _print_device_list() -> None:
    grouped = list_devices()
    total = sum(len(values) for values in grouped.values())
    print(f"[DEVICES] total: {total}")
    for soc, devices in grouped.items():
        print(f"[{soc}] {len(devices)}")
        for device in devices:
            print(f"  {device.get('codename')} | {device.get('name')}")


def main() -> int:
    args = parse_args()
    if args.list_devices:
        _print_device_list()
        return 0
    if args.show_device:
        ws = create_workspace(Path("output/workspace"), clean=False)
        device = resolve_device(args.show_device, ws=ws)
        _print_device(device)
        return 0
    if not args.rom_url or not args.style or not args.soc:
        raise SystemExit("--rom-url, --style, and --soc are required for build mode")

    style_key, _ = normalize_style(args.style)
    ws = create_workspace(Path("output/workspace"), clean=True)
    source = download_rom(args.rom_url, ws)
    info = detect_rom(source, ws, soc=args.soc, custom_codename=args.custom_codename)
    device = resolve_device(rom_metadata=info, custom_codename=args.custom_codename, ws=ws)
    _print_device(device)
    unpack_result = unpack_rom(source, info, ws)
    inspection = inspect_workspace(ws, info, unpack_result)
    apply_style(style_key, ws, info)
    repack_partitions(ws)
    inspection = inspect_workspace(ws, info, unpack_result)
    build_repacked_super(ws, info, inspection)
    final_zip = build_final_zip(ws, info, style_key)
    cleanup(ws, keep_workspace=True)
    print(f"[DONE] {final_zip}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
