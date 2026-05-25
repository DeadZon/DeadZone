"""
Unpack-stage report generation.

Writes two files per session:
  output/reports/01_unpack_report.json  — machine-readable structured data
  output/reports/01_unpack_report.txt   — human-readable summary

Both files are derived entirely from the BuildContext object; nothing is read
from disk here.
"""
from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from factory.core.reports import write_json_report, write_text_report

if TYPE_CHECKING:
    from factory.core.context import BuildContext

_REPORT_JSON = "01_unpack_report.json"
_REPORT_TXT = "01_unpack_report.txt"


def build_unpack_report(ctx: "BuildContext") -> dict:
    """Serialise BuildContext into a plain dict suitable for JSON output."""
    return {
        "input_rom": str(ctx.input_rom),
        "archive_type": ctx.archive_type,
        "payload_found": ctx.payload_found,
        "super_found": ctx.super_found,
        "partitions_extracted": ctx.partitions,
        "boot_images_found": ctx.images,
        "build_prop_device": ctx.detected_device,
        "factory_device": ctx.factory_device,
        "effective_device": ctx.effective_device,
        "android_version": ctx.android_version,
        "mi_version": ctx.mi_version,
        "warnings": ctx.warnings,
        "errors": ctx.errors,
        # Original partition sizes from payload manifest (for super rebuild).
        # Empty when no payload was processed or manifest parsing failed.
        # Do NOT use extracted image file sizes — use these values instead.
        "partition_sizes_from_manifest": dict(ctx.partition_sizes_from_manifest),
        # Path references for downstream stages
        "paths": {
            "root_dir": str(ctx.root_dir),
            "work_dir": str(ctx.work_dir),
            "project_dir": str(ctx.project_dir),
            "output_dir": str(ctx.output_dir),
            "reports_dir": str(ctx.reports_dir),
        },
    }


def format_text_report(report: dict) -> str:
    """Render the report dict as the canonical human-readable text format."""
    lines: list[str] = [
        "DeadZone Unpack Report",
        "======================",
        f"Input ROM:           {report['input_rom']}",
        f"Archive type:        {report['archive_type'] or '(unknown)'}",
        f"Payload found:       {'yes' if report['payload_found'] else 'no'}",
        f"Super found:         {'yes' if report['super_found'] else 'no'}",
        "",
        "Partitions extracted:",
    ]

    partitions = report.get("partitions_extracted") or []
    if partitions:
        for p in partitions:
            lines.append(f"  - {p}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Boot images found:")
    boot_images = report.get("boot_images_found") or []
    if boot_images:
        for img in boot_images:
            lines.append(f"  - {img}")
    else:
        lines.append("  (none)")

    lines += [
        "",
        f"Build.prop device:   {report['build_prop_device'] or '(not found)'}",
        f"Factory device:      {report['factory_device'] or '(not set)'}",
        f"Effective device:    {report['effective_device'] or '(undetermined)'}",
        f"Android:             {report['android_version'] or '(not found)'}",
        f"MI version:          {report['mi_version'] or '(not found)'}",
        "",
        "Warnings:",
    ]

    warnings = report.get("warnings") or []
    if warnings:
        for w in warnings:
            lines.append(f"  ! {w}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Errors:")

    errors = report.get("errors") or []
    if errors:
        for e in errors:
            lines.append(f"  X {e}")
    else:
        lines.append("  (none)")

    lines.append("")
    return "\n".join(lines)


def write_reports(ctx: "BuildContext") -> tuple[Path, Path]:
    """
    Build and write both JSON and TXT reports.
    Returns (json_path, txt_path).
    """
    report = build_unpack_report(ctx)

    json_path = ctx.reports_dir / _REPORT_JSON
    txt_path = ctx.reports_dir / _REPORT_TXT

    write_json_report(json_path, report)
    write_text_report(txt_path, format_text_report(report))

    print(f"[report] JSON: {json_path}")
    print(f"[report] TXT : {txt_path}")
    return json_path, txt_path
