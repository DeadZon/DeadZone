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
        "",
        "Images included:",
    ]
    lines.extend(f"- {name}" for name in report.get("images_included", []))
    lines.append("")
    lines.append("Images missing:")
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

