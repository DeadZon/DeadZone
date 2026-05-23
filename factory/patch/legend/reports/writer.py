"""
Legend unified patch report writer.

All Legend pipeline steps append to one report:
    output/reports/deadzone_patch_report.txt

Call append_section() from each patcher/step to record results.
Call write_final_summary() at the end of the Legend runner.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[4]
_REPORTS_DIR = _REPO_ROOT / "output" / "reports"
REPORT_TXT = _REPORTS_DIR / "deadzone_patch_report.txt"
REPORT_JSON = _REPORTS_DIR / "deadzone_patch_report.json"


def _ensure_dir() -> None:
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def start_report(flavor: str, execute: bool, project_dir: Path) -> None:
    """Write the report header (overwrites any previous run)."""
    _ensure_dir()
    mode = "EXECUTE" if execute else "DRY-RUN"
    header = (
        f"DeadZone Legend Patch Report  [{mode}]\n"
        f"{'=' * 72}\n"
        f"Started   : {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Flavor    : {flavor}\n"
        f"Project   : {project_dir}\n"
        f"\n"
    )
    REPORT_TXT.write_text(header, encoding="utf-8")


def append_section(title: str, lines: list[str]) -> None:
    """Append a named section to the running report."""
    _ensure_dir()
    block = f"\n── {title} ──\n" + "\n".join(lines) + "\n"
    with REPORT_TXT.open("a", encoding="utf-8") as f:
        f.write(block)


def write_final_summary(report: dict[str, Any]) -> None:
    """Write JSON report and append text summary footer."""
    _ensure_dir()

    REPORT_JSON.write_text(
        json.dumps(report, indent=2, default=str, ensure_ascii=True),
        encoding="utf-8",
    )

    status = report.get("final_status", "UNKNOWN")
    errors = report.get("errors", [])
    warnings = report.get("warnings", [])

    footer_lines = [
        f"\n{'=' * 72}",
        f"FINAL STATUS : {status}",
        f"Errors  : {len(errors)}",
        f"Warnings: {len(warnings)}",
    ]
    if errors:
        footer_lines.append("\nErrors:")
        footer_lines.extend(f"  ! {e}" for e in errors)
    if warnings:
        footer_lines.append("\nWarnings:")
        footer_lines.extend(f"  ~ {w}" for w in warnings)
    footer_lines.append(f"\nReport JSON : {REPORT_JSON}")
    footer_lines.append(f"Report TXT  : {REPORT_TXT}")

    with REPORT_TXT.open("a", encoding="utf-8") as f:
        f.write("\n".join(footer_lines) + "\n")

    print(f"[legend_report] TXT : {REPORT_TXT}")
    print(f"[legend_report] JSON: {REPORT_JSON}")
