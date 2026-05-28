"""
generate_device_readiness_report.py

Reads registry/devices/factory_devices.json, builds the device readiness
matrix, and writes:

  output/reports/device_readiness_matrix.json
  output/reports/device_readiness_report.txt

Usage:
  python scripts/generate_device_readiness_report.py
  python scripts/generate_device_readiness_report.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

FACTORY_JSON = REPO_ROOT / "registry" / "devices" / "factory_devices.json"
REPORTS_DIR  = REPO_ROOT / "output" / "reports"


def _build_txt_report(matrix: dict) -> str:
    summary = matrix["summary"]
    devices = matrix["devices"]

    lines = [
        "=" * 62,
        "  DeadZone Factory — Device Readiness Report",
        "=" * 62,
        "",
        "  Summary",
        "  -------",
        f"  Total devices        : {summary['total']}",
        f"  Enabled              : {summary['enabled']}",
        f"  Disabled             : {summary['disabled']}",
        f"  MTK                  : {summary['mtk_count']}",
        f"  Snapdragon           : {summary['snapdragon_count']}",
        f"  Auto (unknown SoC)   : {summary['auto_count']}",
        f"  Official support     : {summary['official_count']}",
        f"  Metadata support     : {summary['metadata_count']}",
        f"  Ready for Free       : {summary['ready_for_free']}",
        f"  Not ready            : {summary['not_ready']}",
        "",
    ]

    if summary["duplicate_codenames"]:
        lines.append("  [FAIL] Duplicate codenames:")
        for cn in summary["duplicate_codenames"]:
            lines.append(f"    - {cn}")
        lines.append("")

    if summary["not_ready_devices"]:
        lines.append("  [FAIL] Not-ready devices:")
        for entry in summary["not_ready_devices"]:
            reasons = "; ".join(entry["reasons"]) or "unknown"
            lines.append(f"    - {entry['codename']}: {reasons}")
        lines.append("")

    # Devices missing from workflow dropdown (soc not mtk/snapdragon and not auto-handled)
    missing_dropdown = [
        r for r in devices
        if r["enabled"] and not r["dropdown_ready"]
    ]
    if missing_dropdown:
        lines.append("  Devices missing from workflow dropdown:")
        for r in missing_dropdown:
            lines.append(f"    - {r['codename']} (soc={r['soc']})")
        lines.append("")

    disabled = [r for r in devices if not r["enabled"]]
    if disabled:
        lines.append(f"  Disabled devices ({len(disabled)}):")
        for r in disabled:
            lines.append(f"    - {r['codename']} ({r['display_name']})")
        lines.append("")

    # Per-device table (enabled only)
    lines += [
        "  Device readiness (enabled only):",
        f"  {'Codename':<20} {'SoC':<12} {'Source':<12} {'Level':<12} {'Ready'}",
        "  " + "-" * 58,
    ]
    for r in sorted(devices, key=lambda x: x["codename"]):
        if not r["enabled"]:
            continue
        ready = "YES" if r["universal_engine_ready"] else "NO "
        notes = " | " + "; ".join(r["notes"]) if r["notes"] else ""
        lines.append(
            f"  {r['codename']:<20} {r['soc']:<12} {r['source']:<12} "
            f"{r['support_level']:<12} {ready}{notes}"
        )

    lines += ["", "=" * 62]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate device readiness report")
    parser.add_argument("--dry-run", action="store_true", help="Print report, don't write files")
    parser.add_argument(
        "--devices-json",
        default=str(FACTORY_JSON),
        help="Path to factory_devices.json",
    )
    args = parser.parse_args(argv)

    devices_path = pathlib.Path(args.devices_json)
    if not devices_path.exists():
        print(f"[FAIL] factory_devices.json not found: {devices_path}", file=sys.stderr)
        return 1

    # Import here so the script works standalone without installing the package
    sys.path.insert(0, str(REPO_ROOT))
    from factory.registry.device_readiness import build_device_readiness_matrix

    matrix = build_device_readiness_matrix(devices_path)
    summary = matrix["summary"]

    txt_report = _build_txt_report(matrix)
    print(txt_report)

    if args.dry_run:
        print("[dry-run] Not writing files.")
        return 0 if summary["not_ready"] == 0 and not summary["duplicate_codenames"] else 1

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    json_path = REPORTS_DIR / "device_readiness_matrix.json"
    txt_path  = REPORTS_DIR / "device_readiness_report.txt"

    json_path.write_text(json.dumps(matrix, indent=2, ensure_ascii=False), encoding="utf-8")
    txt_path.write_text(txt_report, encoding="utf-8")

    print(f"[OK] Written: {json_path}")
    print(f"[OK] Written: {txt_path}")

    if summary["not_ready"] > 0 or summary["duplicate_codenames"]:
        print(
            f"\n[RESULT] FAILED — {summary['not_ready']} not-ready device(s), "
            f"{len(summary['duplicate_codenames'])} duplicate(s).",
            file=sys.stderr,
        )
        return 1

    print(f"\n[RESULT] All {summary['enabled']} enabled devices are ready.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
