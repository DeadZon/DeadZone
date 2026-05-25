"""Legend JAR patcher — thin wrapper around the MTCR runner."""
from __future__ import annotations

import importlib
from pathlib import Path
from typing import Optional


def patch_jars(
    root: Path,
    flavor: str,
    *,
    execute: bool = False,
    android_major: Optional[int] = None,
    legend_jar_mods: Optional[dict] = None,
    report_lines: Optional[list[str]] = None,
) -> dict:
    """
    Apply all Legend JAR patches via the MTCR runner.

    Delegates entirely to factory.patch.mods.legend.mtcr.runner so there is one
    code path for JAR patching.
    """
    _log(report_lines, "[jar_patcher] Delegating to factory.patch.mods.legend.mtcr.runner")

    try:
        mtcr = importlib.import_module("factory.patch.mods.legend.mtcr.runner")
    except ImportError as exc:
        msg = f"[jar_patcher] MTCR runner not available: {exc}"
        _log(report_lines, msg)
        return {"status": "FAILED", "errors": [msg], "dry_run": not execute}

    report = mtcr.apply_legend_mtcr_patches(
        project_dir=root,
        flavor=flavor,
        execute=execute,
        android_major=android_major,
        legend_jar_mods=legend_jar_mods,
    )
    _log(report_lines, f"[jar_patcher] MTCR result: {report.get('final_status')}")
    return report


def _log(report_lines: Optional[list[str]], msg: str) -> None:
    print(msg)
    if report_lines is not None:
        report_lines.append(msg)
