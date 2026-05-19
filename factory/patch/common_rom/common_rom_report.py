"""
Report writer for common ROM project-level legacy patches.

Writes:
  output/reports/03_common_rom_legacy_report.json
  output/reports/03_common_rom_legacy_report.txt
"""
from __future__ import annotations

import json
from pathlib import Path

_REPORT_JSON = "03_common_rom_legacy_report.json"
_REPORT_TXT  = "03_common_rom_legacy_report.txt"


def _format_text_report(report: dict) -> str:
    mode = "DRY RUN" if report.get("dry_run") else "EXECUTE"
    lines: list[str] = [
        f"DeadZone Common ROM Legacy Patch Report  [{mode}]",
        "=" * 60,
        f"Status:         {report.get('status', '?')}",
        f"Flavor:         {report.get('flavor', '?')}",
        f"Project:        {report.get('project_dir', '?')}",
        f"mi_incremental: {report.get('mi_incremental') or '(none)'}",
        f"Dry run:        {report.get('dry_run', True)}",
        "",
        "Functions planned:",
    ]
    for fn in report.get("functions_planned", []):
        lines.append(f"  - {fn}")

    lines.append("")
    lines.append("Functions executed:")
    executed = report.get("functions_executed", [])
    if executed:
        for fn in executed:
            lines.append(f"  OK  {fn}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Skipped functions:")
    skipped = report.get("skipped_functions", [])
    if skipped:
        for item in skipped:
            lines.append(f"  --  {item.get('function')}  ({item.get('reason')})")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Warnings:")
    warnings = report.get("warnings", [])
    if warnings:
        for w in warnings:
            lines.append(f"  ! {w}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Errors:")
    errors = report.get("errors", [])
    if errors:
        for e in errors:
            lines.append(f"  X {e}")
    else:
        lines.append("  (none)")

    lines.append("")
    return "\n".join(lines)


def write_common_rom_reports(report: dict, reports_dir: Path) -> tuple[Path, Path]:
    reports_dir.mkdir(parents=True, exist_ok=True)

    json_path = reports_dir / _REPORT_JSON
    txt_path  = reports_dir / _REPORT_TXT

    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )
    txt_path.write_text(_format_text_report(report), encoding="utf-8")

    print(f"[common_rom_report] JSON: {json_path}")
    print(f"[common_rom_report] TXT : {txt_path}")
    return json_path, txt_path
