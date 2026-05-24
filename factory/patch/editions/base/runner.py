"""Base edition runner — applies common patches only."""
from __future__ import annotations

from pathlib import Path
from typing import Any


def run_edition(
    root: Path | str,
    output_dir: Path | str | None = None,
    context: dict[str, Any] | None = None,
) -> dict:
    ctx = context or {}
    execute = bool(ctx.get("execute", False))
    root = Path(root).resolve()

    from factory.patch.common_rom.project_legacy import (
        _write_reports,
        apply_common_project_legacy_patches,
    )

    report = apply_common_project_legacy_patches(
        project_dir=root,
        root_dir=Path(__file__).resolve().parents[4],
        flavor="deadzone",
        execute=execute,
    )
    _write_reports(report)

    status = report.get("final_status") or report.get("status", "APPLIED")
    return {
        "edition": "base",
        "final_status": status,
        "warnings": report.get("warnings", []),
        "errors": report.get("errors", []),
        "steps": {"common_rom": report},
    }
