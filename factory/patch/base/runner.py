"""Base patch runner — applies common patches shared by all mods.

Runs before the selected mod runner. Contains:
- common ROM cleanup
- common props
- OTA rules
- minimal debloat
- shared permissions

Mod-specific logic must not live here.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[3]


def run_base(
    root: Path | str,
    output_dir: Path | str | None = None,
    context: dict[str, Any] | None = None,
) -> dict:
    """Apply base common patches to an unpacked ROM.

    Parameters
    ----------
    root       ROM project root directory.
    output_dir Output directory (default: <repo_root>/output).
    context    Optional dict with keys: execute (bool), flavor (str).
    """
    ctx = context or {}
    execute = bool(ctx.get("execute", False))
    flavor = str(ctx.get("flavor", "deadzone"))
    root = Path(root).resolve()

    from factory.patch.common_rom.project_legacy import (
        _write_reports,
        apply_common_project_legacy_patches,
    )

    report = apply_common_project_legacy_patches(
        project_dir=root,
        root_dir=_REPO_ROOT,
        mi_incremental=None,
        flavor=flavor,
        execute=execute,
    )
    _write_reports(report)

    status = str(report.get("final_status") or report.get("status") or "APPLIED").upper()
    return {
        "stage": "base",
        "final_status": status,
        "warnings": report.get("warnings", []),
        "errors": report.get("errors", []),
        "steps": {"common_rom": report},
    }
