"""Report writer for the legacy super build stage."""
from __future__ import annotations

from pathlib import Path

from factory.core.reports import write_json_report, write_text_report

REPORT_JSON = "14_super_build_legacy_report.json"
REPORT_TXT = "14_super_build_legacy_report.txt"


def _append_list(lines: list[str], values: object) -> None:
    if not values:
        lines.append("  (none)")
        return
    if not isinstance(values, list):
        values = [values]
    for value in values:
        lines.append(f"  - {value}")


def format_super_build_legacy_report(report: dict) -> str:
    """Render the report as plain ASCII text."""
    command = report.get("lpmake_command") or []
    lines = [
        "DeadZone Super Build Legacy Report",
        "==================================",
        f"Stage:                {report.get('stage')}",
        f"Mode:                 {'dry-run' if report.get('dry_run') else 'execute'}",
        f"Project:              {report.get('project_dir')}",
        f"Images:               {report.get('images_dir')}",
        f"Output super:         {report.get('output_super')}",
        f"Device:               {report.get('device')}",
        f"SoC:                  {report.get('soc')}",
        f"Platform:             {report.get('platform')}",
        f"Flavor:               {report.get('flavor')}",
        f"Super info source:    {report.get('super_info_source')}",
        f"Super size:           {report.get('super_size')}",
        f"Group name:           {report.get('group_name')}",
        f"Group size:           {report.get('group_size')}",
        f"Slot mode:            {report.get('slot_mode')}",
        f"Virtual A/B:          {report.get('virtual_ab')}",
        f"Output format:        {report.get('output_format')}",
        f"lpmake:               {report.get('lpmake_path') or '(not found)'}",
        f"lpmake executed:      {report.get('lpmake_executed')}",
        f"super.img created:    {report.get('super_img_created')}",
        f"super.img size:       {report.get('super_img_size')}",
        f"Validation status:    {report.get('validation_status')}",
        f"Final status:         {report.get('final_status')}",
        "",
        "Partitions requested:",
    ]
    _append_list(lines, report.get("partitions_requested"))
    lines.append("")
    lines.append("Partitions found:")
    _append_list(lines, report.get("partitions_found"))
    lines.append("")
    lines.append("Partitions missing:")
    _append_list(lines, report.get("partitions_missing"))
    lines.append("")
    lines.append("Partition image sizes:")
    sizes = report.get("partition_image_sizes") or {}
    if isinstance(sizes, dict) and sizes:
        for name in sorted(sizes):
            lines.append(f"  - {name}: {sizes[name]}")
    else:
        lines.append("  (none)")
    lines.append("")
    lines.append("lpmake command:")
    lines.append(f"  {' '.join(str(item) for item in command)}" if command else "  (none)")
    lines.append("")
    lines.append("Skipped items:")
    _append_list(lines, report.get("skipped_items"))
    lines.append("")
    lines.append("Warnings:")
    _append_list(lines, report.get("warnings"))
    lines.append("")
    lines.append("Errors:")
    _append_list(lines, report.get("errors"))
    lines.append("")
    return "\n".join(lines)


def write_super_build_legacy_reports(report: dict, reports_dir: Path) -> tuple[Path, Path]:
    """Write JSON and text reports for the stage."""
    reports_dir = Path(reports_dir)
    json_path = reports_dir / REPORT_JSON
    txt_path = reports_dir / REPORT_TXT
    write_json_report(json_path, report)
    write_text_report(txt_path, format_super_build_legacy_report(report))
    print(f"[super_build] Report JSON: {json_path}")
    print(f"[super_build] Report TXT : {txt_path}")
    return json_path, txt_path
