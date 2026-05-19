"""Report writer for the legacy build pipeline orchestrator."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPORT_JSON = "16_legacy_build_pipeline_report.json"
REPORT_TXT = "16_legacy_build_pipeline_report.txt"


def _ascii(value: object) -> str:
    return str(value).encode("ascii", errors="replace").decode("ascii")


def _append_list(lines: list[str], values: object) -> None:
    if not values:
        lines.append("  (none)")
        return
    if not isinstance(values, list):
        values = [values]
    for value in values:
        lines.append(f"  - {_ascii(value)}")


def format_legacy_build_pipeline_report(report: dict[str, Any]) -> str:
    lines = [
        "DeadZone Legacy Build Pipeline Report",
        "====================================",
        f"Stage:               {report.get('stage')}",
        f"Final status:        {report.get('final_status')}",
        f"Dry run:             {report.get('dry_run')}",
        f"Execute:             {report.get('execute')}",
        f"Build name:          {report.get('build_name')}",
        f"Device:              {report.get('device')}",
        f"SoC:                 {report.get('soc')}",
        f"Platform:            {report.get('platform')}",
        f"Flavor:              {report.get('flavor')}",
        f"Android version:     {report.get('android_version')}",
        f"MI incremental:      {report.get('mi_incremental')}",
        f"Project dir:         {report.get('project_dir')}",
        f"ROM path:            {report.get('rom_path')}",
        f"Images dir:          {report.get('images_dir')}",
        f"Output dir:          {report.get('output_dir')}",
        f"Final ZIP:           {report.get('final_zip')}",
        f"Telegram enabled:    {report.get('telegram_enabled')}",
        f"Telegram message id: {report.get('telegram_message_id')}",
        "",
        "Stages:",
    ]
    for stage in report.get("stages") or []:
        lines.append(
            "  [{status}] {name} ({duration:.2f}s)".format(
                status=_ascii(stage.get("status")),
                name=_ascii(stage.get("name")),
                duration=float(stage.get("duration_seconds") or 0.0),
            )
        )
        if stage.get("reason"):
            lines.append(f"    Reason: {_ascii(stage.get('reason'))}")
        if stage.get("report_path"):
            lines.append(f"    Report: {_ascii(stage.get('report_path'))}")
    lines.append("")
    lines.append("Warnings:")
    _append_list(lines, report.get("warnings"))
    lines.append("")
    lines.append("Errors:")
    _append_list(lines, report.get("errors"))
    lines.append("")
    return "\n".join(lines)


def write_legacy_build_pipeline_report(report: dict[str, Any], output_dir: Path) -> dict[str, str]:
    reports_dir = Path(output_dir) / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = reports_dir / REPORT_JSON
    txt_path = reports_dir / REPORT_TXT
    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=True, default=str),
        encoding="utf-8",
        newline="\n",
    )
    txt_path.write_text(
        format_legacy_build_pipeline_report(report),
        encoding="utf-8",
        newline="\n",
    )
    return {"json": str(json_path), "txt": str(txt_path)}

