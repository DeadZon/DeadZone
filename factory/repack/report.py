"""Report writer for the legacy EROFS repack stage."""
from __future__ import annotations

from pathlib import Path

from factory.core.reports import write_json_report, write_text_report

REPORT_JSON = "13_erofs_repack_legacy_report.json"
REPORT_TXT = "13_erofs_repack_legacy_report.txt"


def _append_list(lines: list[str], values: object) -> None:
    if not values:
        lines.append("  (none)")
        return
    if not isinstance(values, list):
        values = [values]
    for value in values:
        lines.append(f"  - {value}")


def format_erofs_repack_legacy_report(report: dict) -> str:
    """Render the report as plain ASCII text."""
    lines = [
        "DeadZone EROFS Repack Legacy Report",
        "===================================",
        f"Stage:                {report.get('stage')}",
        f"Mode:                 {'dry-run' if report.get('dry_run') else 'execute'}",
        f"Project:              {report.get('project_dir')}",
        f"Images:               {report.get('images_dir')}",
        f"Flavor:               {report.get('flavor')}",
        f"mkfs.erofs:           {report.get('mkfs_erofs_path') or '(not found)'}",
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
    lines.append("Commands planned:")
    for command in report.get("commands_planned") or []:
        if isinstance(command, list):
            lines.append(f"  - {' '.join(str(item) for item in command)}")
        else:
            lines.append(f"  - {command}")
    if not report.get("commands_planned"):
        lines.append("  (none)")
    lines.append("")
    lines.append("Commands executed:")
    for command in report.get("commands_executed") or []:
        if isinstance(command, list):
            lines.append(f"  - {' '.join(str(item) for item in command)}")
        else:
            lines.append(f"  - {command}")
    if not report.get("commands_executed"):
        lines.append("  (none)")
    lines.append("")
    lines.append("Images created:")
    _append_list(lines, report.get("images_created"))
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


def write_erofs_repack_legacy_reports(report: dict, reports_dir: Path) -> tuple[Path, Path]:
    """Write JSON and text reports for the stage."""
    reports_dir = Path(reports_dir)
    json_path = reports_dir / REPORT_JSON
    txt_path = reports_dir / REPORT_TXT
    write_json_report(json_path, report)
    write_text_report(txt_path, format_erofs_repack_legacy_report(report))
    print(f"[erofs_repack] Report JSON: {json_path}")
    print(f"[erofs_repack] Report TXT : {txt_path}")
    return json_path, txt_path

