from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPORT_JSON_NAME = "15_final_fastboot_zip_report.json"
REPORT_TXT_NAME = "15_final_fastboot_zip_report.txt"


def write_final_fastboot_zip_report(report: dict[str, Any], reports_dir: Path) -> dict[str, str]:
    reports_dir = Path(reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = reports_dir / REPORT_JSON_NAME
    txt_path = reports_dir / REPORT_TXT_NAME

    json_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    zip_size_mib = report.get("zip_size_mib")
    zip_size_str = f"{zip_size_mib} MiB" if zip_size_mib is not None else "N/A (dry-run)"
    size_warn = zip_size_mib is not None and zip_size_mib > 6000

    lines = [
        "DeadZone Final Fastboot ZIP Report",
        "==================================",
        f"stage: {report.get('stage')}",
        f"final_status: {report.get('final_status')}",
        f"dry_run: {report.get('dry_run')}",
        f"build_name: {report.get('build_name')}",
        f"device: {report.get('device')}",
        f"flavor: {report.get('flavor')}",
        f"template_source: {report.get('template_source')}",
        f"staging_dir: {report.get('staging_dir')}",
        f"final_zip: {report.get('final_zip')}",
        f"validation_status: {report.get('validation_status')}",
        f"compression_mode: {report.get('compression_mode', 'ZIP_DEFLATED compresslevel=9')}",
        f"super_img_detected: {report.get('super_img_detected', False)}",
        f"zip_size_mib: {zip_size_str}",
        *([f"WARNING: ZIP size {zip_size_mib} MiB exceeds 6000 MiB — check for duplicate images"] if size_warn else []),
        "",
        "Images included:",
    ]
    lines.extend(f"- {name}" for name in report.get("images_included", []))
    lines.append("")
    lines.append("Images excluded (dynamic, packed in super.img):")
    excluded = report.get("images_excluded_dynamic", [])
    if excluded:
        lines.extend(f"- {name}" for name in excluded)
    else:
        lines.append("  (none — super.img not detected or no dynamic images present)")
    lines.append("")
    missing_required = report.get("images_missing_required", [])
    if missing_required:
        lines.append("MISSING REQUIRED IMAGES (build aborted):")
        lines.extend(f"- MISSING: {name}" for name in missing_required)
    else:
        lines.append("Missing required images: none")
    lines.append("")
    lines.append("Images missing from flash order (optional):")
    lines.extend(f"- {name}" for name in report.get("images_missing", []))
    lines.append("")
    lines.append("Scripts generated:")
    lines.extend(f"- {name}" for name in report.get("scripts_generated", []))
    lines.append("")
    lines.append("Forbidden entries:")
    lines.extend(f"- {name}" for name in report.get("forbidden_entries", []))
    lines.append("")
    lines.append("Warnings:")
    lines.extend(f"- {item}" for item in report.get("warnings", []))
    lines.append("")
    lines.append("Errors:")
    lines.extend(f"- {item}" for item in report.get("errors", []))
    lines.append("")

    txt_path.write_text("\n".join(lines), encoding="utf-8")
    return {"json": str(json_path), "txt": str(txt_path)}
