"""Report writer for the legacy images and vbmeta stage."""
from __future__ import annotations

from pathlib import Path

from factory.core.reports import write_json_report, write_text_report

REPORT_JSON = "12_images_vbmeta_legacy_report.json"
REPORT_TXT = "12_images_vbmeta_legacy_report.txt"


def format_images_vbmeta_report(report: dict) -> str:
    """Render the stage report as plain ASCII text."""
    lines = [
        "DeadZone Images and VBMeta Legacy Report",
        "========================================",
        f"Stage:              {report.get('stage')}",
        f"Mode:               {'dry-run' if report.get('dry_run') else 'execute'}",
        f"Project:            {report.get('project_dir')}",
        f"Images:             {report.get('images_dir')}",
        f"Flavor:             {report.get('flavor')}",
        f"Device:             {report.get('device') or '(not set)'}",
        f"SoC:                {report.get('soc') or '(not set)'}",
        f"Platform:           {report.get('platform') or '(not set)'}",
        f"Android:            {report.get('android_version') or '(not found)'}",
        f"MI version:         {report.get('mi_incremental') or '(not found)'}",
        "",
        f"Build.prop device:  {report.get('detected_device_from_build_prop') or '(not found)'}",
        f"Factory device:     {report.get('factory_device') or '(not set)'}",
        f"Effective device:   {report.get('effective_device') or '(undetermined)'}",
        "",
        f"Firmware status:    {report.get('firmware_info_status')}",
        f"Collection status:  {report.get('image_collection_status')}",
        f"VBMeta status:      {report.get('vbmeta_status')}",
        f"Final status:       {report.get('final_status')}",
        "",
        "Copied images:",
    ]
    _append_list(lines, report.get("copied_images"))
    lines.append("")
    lines.append("Moved images:")
    _append_list(lines, report.get("moved_images"))
    lines.append("")
    lines.append("Generated files:")
    _append_list(lines, report.get("generated_files"))
    lines.append("")
    lines.append("Patched vbmeta files:")
    _append_list(lines, report.get("patched_vbmeta_files"))
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


def _append_list(lines: list[str], values: object) -> None:
    if not values:
        lines.append("  (none)")
        return
    if not isinstance(values, list):
        values = [values]
    for value in values:
        lines.append(f"  - {value}")


def write_images_vbmeta_legacy_reports(report: dict, reports_dir: Path) -> tuple[Path, Path]:
    """Write JSON and text reports for the stage."""
    reports_dir = Path(reports_dir)
    json_path = reports_dir / REPORT_JSON
    txt_path = reports_dir / REPORT_TXT
    write_json_report(json_path, report)
    write_text_report(txt_path, format_images_vbmeta_report(report))
    print(f"[images] Report JSON: {json_path}")
    print(f"[images] Report TXT : {txt_path}")
    return json_path, txt_path

