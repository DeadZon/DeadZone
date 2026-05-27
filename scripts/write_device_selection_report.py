"""
write_device_selection_report.py

Writes output/reports/device_selection_report.txt with device metadata and
ROM resolution details for the current build run.

Called by workflow step after the pipeline completes (if: always()).

Usage:
    python scripts/write_device_selection_report.py \
        --codename zircon \
        --display-name "Redmi Note 13 Pro+ 5G" \
        --select-device "zircon | Redmi Note 13 Pro+ 5G" \
        --rom-source manual_url \
        --rom-url https://example.com/rom.zip \
        --mode execute
"""

import argparse
import datetime
import json
import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEVICES_JSON = REPO_ROOT / "registry" / "devices" / "factory_devices.json"
DEFAULT_OUTPUT = REPO_ROOT / "output" / "reports" / "device_selection_report.txt"

_SEP = "─" * 44


def lookup_device_meta(codename: str, json_path: pathlib.Path) -> dict:
    try:
        devices = json.loads(json_path.read_text(encoding="utf-8"))
        return next((d for d in devices if d.get("codename") == codename), {})
    except Exception:
        return {}


def build_report(
    codename: str,
    display_name: str,
    select_device: str,
    rom_source: str,
    rom_url: str,
    mode: str,
    meta: dict,
) -> str:
    soc = meta.get("soc", "unknown")
    source_reg = meta.get("source", "unknown")
    support_level = meta.get("support_level", "unknown")
    generated = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = [
        "DeadZone Device Selection Report",
        f"Generated : {generated}",
        _SEP,
        f"Selected dropdown : {select_device}",
        f"Final codename    : {codename}",
        f"Device name       : {display_name}",
        f"Source registry   : {source_reg}",
        f"SoC               : {soc}",
        f"Support level     : {support_level}",
        _SEP,
        f"ROM source        : {rom_source}",
        f"ROM URL           : {rom_url or '(none)'}",
        f"Build mode        : {mode}",
        "",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Write device selection report.")
    parser.add_argument("--codename", required=True)
    parser.add_argument("--display-name", default="")
    parser.add_argument("--select-device", default="")
    parser.add_argument("--rom-source", default="")
    parser.add_argument("--rom-url", default="")
    parser.add_argument("--mode", default="")
    parser.add_argument("--devices-json", type=pathlib.Path, default=DEVICES_JSON)
    parser.add_argument("--output", type=pathlib.Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)

    meta = lookup_device_meta(args.codename, args.devices_json)

    report = build_report(
        codename=args.codename,
        display_name=args.display_name,
        select_device=args.select_device,
        rom_source=args.rom_source,
        rom_url=args.rom_url,
        mode=args.mode,
        meta=meta,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    print(f"[REPORT] Written: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
