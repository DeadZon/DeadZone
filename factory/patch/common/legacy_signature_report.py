"""
Report data structures and writers for the Legend legacy signature bypass stage.

Writes:
  output/reports/04_legend_signature_bypass_report.json
  output/reports/04_legend_signature_bypass_report.txt
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

_REPORT_JSON = "04_legend_signature_bypass_report.json"
_REPORT_TXT  = "04_legend_signature_bypass_report.txt"


@dataclass
class SigBypassReport:
    flavor: str
    android_major: int
    project_path: str
    work_dir: str
    selected_function: str        # name of the legacy function that would / did run
    status: str                   # DRY_RUN | APPLIED | SKIPPED_NON_LEGEND | SKIPPED_UNSUPPORTED_ANDROID | FAILED
    folders_checked: list[str] = field(default_factory=list)
    folders_present: list[str] = field(default_factory=list)
    folders_missing: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


def _to_dict(r: SigBypassReport) -> dict:
    return {
        "flavor":            r.flavor,
        "android_major":     r.android_major,
        "project_path":      r.project_path,
        "work_dir":          r.work_dir,
        "selected_function": r.selected_function,
        "status":            r.status,
        "folders_checked":   r.folders_checked,
        "folders_present":   r.folders_present,
        "folders_missing":   r.folders_missing,
        "warnings":          r.warnings,
        "errors":            r.errors,
    }


def _to_txt(r: SigBypassReport) -> str:
    lines = [
        "DeadZone Legend Signature Bypass (Legacy) Report",
        "=" * 56,
        f"Status:            {r.status}",
        f"Flavor:            {r.flavor}",
        f"Android major:     {r.android_major}",
        f"Project path:      {r.project_path}",
        f"Work directory:    {r.work_dir}",
        f"Selected function: {r.selected_function}",
        "",
        "Workspace folders checked:",
    ]
    for f_path in r.folders_checked:
        present = f_path in r.folders_present
        mark = "OK " if present else "!  "
        lines.append(f"  [{mark}] {f_path}")
    lines.append("")

    lines.append("Warnings:")
    if r.warnings:
        for w in r.warnings:
            lines.append(f"  ! {w}")
    else:
        lines.append("  (none)")
    lines.append("")

    lines.append("Errors:")
    if r.errors:
        for e in r.errors:
            lines.append(f"  X {e}")
    else:
        lines.append("  (none)")
    lines.append("")
    return "\n".join(lines)


def write_sig_bypass_reports(report: SigBypassReport, reports_dir: Path) -> tuple[Path, Path]:
    reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = reports_dir / _REPORT_JSON
    txt_path  = reports_dir / _REPORT_TXT
    json_path.write_text(
        json.dumps(_to_dict(report), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    txt_path.write_text(_to_txt(report), encoding="utf-8")
    print(f"[sig_bypass] Report JSON: {json_path}")
    print(f"[sig_bypass] Report TXT : {txt_path}")
    return json_path, txt_path
