"""
Legend debloat patcher — thin runner wrapper for the OS3 debloat executor.

Called by runner.py between props_patcher and apk_patcher.
The executor guards itself; non-OS3 builds receive SKIPPED status.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any


def patch_debloat(
    root: Path,
    flavor: str = "legend",
    os_family: str = "OS3",
    execute: bool = False,
    report_lines: list[str] | None = None,
    context: dict[str, Any] | None = None,
) -> dict:
    """
    Run the OS3 debloat profile against *root*.

    Parameters
    ----------
    root         : ROM project root.
    flavor       : Build flavor string (e.g. "legend").
    os_family    : OS family string (e.g. "OS3").
    execute      : True → apply; False → dry-run.
    report_lines : Optional list to receive human-readable summary lines.
    context      : Optional extra keys (currently unused).

    Returns
    -------
    dict  Result with ``final_status`` in
          ``{"APPLIED", "DRY_RUN", "SKIPPED", "FAILED"}``.
    """
    lines = report_lines if report_lines is not None else []

    from factory.patch.legend.mods.debloat.os3.debloat_executor import (
        apply_legend_os3_debloat,
    )

    result = apply_legend_os3_debloat(
        project_dir=Path(root),
        flavor=flavor,
        os_family=os_family,
        execute=execute,
    )

    status = result.get("final_status", "FAILED")
    lines.append(f"status={status}")
    lines.append(f"removed={result.get('removed_count', 0)}")
    lines.append(f"moved={result.get('moved_count', 0)}")
    lines.append(f"renamed={result.get('renamed_count', 0)}")
    for w in result.get("warnings", []):
        lines.append(f"  WARN: {w}")
    for e in result.get("errors", []):
        lines.append(f"  ERROR: {e}")

    return result
