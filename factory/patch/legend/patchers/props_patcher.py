"""Legend props patcher — patches build.prop / system.prop values if present."""
from __future__ import annotations

from pathlib import Path
from typing import Optional


def patch_props(
    root: Path,
    *,
    execute: bool = False,
    report_lines: Optional[list[str]] = None,
) -> dict:
    """
    Stub — extend with Legend-specific prop changes as needed.

    Returns a result dict compatible with the unified runner report.
    """
    result: dict = {
        "props_patched": 0,
        "files_touched": [],
        "errors": [],
        "dry_run": not execute,
        "status": "SKIPPED_NO_RULES",
    }
    _log(report_lines, "[props_patcher] no active prop rules — skipped")
    return result


def _log(report_lines: Optional[list[str]], msg: str) -> None:
    print(msg)
    if report_lines is not None:
        report_lines.append(msg)
