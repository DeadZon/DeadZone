"""CLI entry point: python -m factory.registry.device_readiness

Writes:
  output/reports/device_readiness_matrix.json
  output/reports/device_readiness_report.txt
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
_FACTORY_DEVICES = _REPO_ROOT / "registry" / "devices" / "factory_devices.json"
_OUT_JSON = _REPO_ROOT / "output" / "reports" / "device_readiness_matrix.json"
_OUT_TXT  = _REPO_ROOT / "output" / "reports" / "device_readiness_report.txt"


def _report_lines(matrix: dict) -> list[str]:
    s = matrix["summary"]
    devices = matrix["devices"]

    lines: list[str] = [
        "=" * 60,
        "DeadZone Factory — Device Readiness Report",
        "=" * 60,
        "",
        f"Total devices         : {s['total']}",
        f"Enabled               : {s['enabled']}",
        f"Disabled              : {s['disabled']}",
        f"MTK (enabled)         : {s['mtk_count']}",
        f"Snapdragon (enabled)  : {s['snapdragon_count']}",
        f"Auto SoC (enabled)    : {s['auto_count']}",
        f"Official support      : {s['official_count']}",
        f"Metadata support      : {s['metadata_count']}",
        f"Ready for free edition: {s['ready_for_free']}",
        f"Not ready             : {s['not_ready']}",
        f"Duplicate codenames   : {s['duplicate_codenames'] or 'none'}",
        "",
        "Direct GitHub workflow: all workflow_ready devices are supported",
        "Fly workflow          : all workflow_ready devices are supported",
        "Codename input        : free text (same for both workflows)",
        "",
    ]

    if s["not_ready_devices"]:
        lines.append("NOT READY DEVICES:")
        for entry in s["not_ready_devices"]:
            lines.append(f"  {entry['codename']}: {', '.join(entry['reasons'])}")
        lines.append("")

    lines.append("DEVICE MATRIX:")
    lines.append(
        f"  {'Codename':<20} {'SoC':<12} {'Direct':>6} {'Fly':>6} {'Edition':>8} {'Notes'}"
    )
    lines.append("  " + "-" * 70)
    for r in sorted(devices, key=lambda x: x["codename"]):
        direct = "YES" if r["direct_supported"] else "NO "
        fly    = "YES" if r["fly_supported"]    else "NO "
        edition = "free+paid" if r["ready_for_paid_editions"] else ("free" if r["ready_for_free"] else "NONE")
        notes = "; ".join(r["notes"]) if r["notes"] else ""
        lines.append(
            f"  {r['codename']:<20} {r['soc']:<12} {direct:>6} {fly:>6} {edition:>8}  {notes}"
        )

    lines += ["", "=" * 60]
    return lines


def main(argv: list[str] | None = None) -> int:
    import argparse
    p = argparse.ArgumentParser(description="Generate device readiness report")
    p.add_argument(
        "--factory-devices",
        type=Path,
        default=_FACTORY_DEVICES,
        help="Path to factory_devices.json",
    )
    p.add_argument("--out-json", type=Path, default=_OUT_JSON)
    p.add_argument("--out-txt",  type=Path, default=_OUT_TXT)
    args = p.parse_args(argv)

    if not args.factory_devices.exists():
        print(f"[ERROR] factory_devices.json not found: {args.factory_devices}", file=sys.stderr)
        return 1

    from factory.registry.device_readiness import build_device_readiness_matrix
    matrix = build_device_readiness_matrix(args.factory_devices)

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(matrix, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[readiness] JSON → {args.out_json}")

    report_lines = _report_lines(matrix)
    report_text = "\n".join(report_lines) + "\n"
    args.out_txt.parent.mkdir(parents=True, exist_ok=True)
    args.out_txt.write_text(report_text, encoding="utf-8")
    print(f"[readiness] TXT  → {args.out_txt}")

    s = matrix["summary"]
    print(f"[readiness] total={s['total']}  mtk={s['mtk_count']}  snapdragon={s['snapdragon_count']}  not_ready={s['not_ready']}")

    # Print the text report to stdout as well
    print(report_text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
