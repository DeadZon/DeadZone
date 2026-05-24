"""Gaming edition runner — common patches + gaming build package overlay."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

_ALLOWED_PARTITIONS = frozenset({"system", "product", "system_ext", "vendor", "odm", "mi_ext"})


def _apply_build_package(root: Path, execute: bool) -> dict:
    """Apply gaming build package from local build/ or GAMING_BUILD_URL."""
    build_dir = Path(__file__).parent / "build"
    build_url = os.environ.get("GAMING_BUILD_URL", "").strip()

    if not build_dir.is_dir() and not build_url:
        return {"status": "SKIPPED_TEMPORARY", "reason": "build/ missing and GAMING_BUILD_URL not set"}

    from factory.patch.editions._build_patcher import apply_build_package
    return apply_build_package(
        root=root,
        build_dir=build_dir if build_dir.is_dir() else None,
        build_url=build_url or None,
        edition="gaming",
        allowed_partitions=_ALLOWED_PARTITIONS,
        execute=execute,
    )


def run_edition(
    root: Path | str,
    output_dir: Path | str | None = None,
    context: dict[str, Any] | None = None,
) -> dict:
    ctx = context or {}
    execute = bool(ctx.get("execute", False))
    root = Path(root).resolve()

    steps: dict = {}
    errors: list[str] = []
    warnings: list[str] = []

    from factory.patch.common_rom.project_legacy import (
        _write_reports,
        apply_common_project_legacy_patches,
    )

    common = apply_common_project_legacy_patches(
        project_dir=root,
        root_dir=Path(__file__).resolve().parents[4],
        flavor="deadzone_gaming",
        execute=execute,
    )
    _write_reports(common)
    steps["common_rom"] = common
    warnings.extend(common.get("warnings", []))
    errors.extend(common.get("errors", []))

    build = _apply_build_package(root, execute)
    steps["build_package"] = build
    if build.get("status") == "FAILED":
        errors.extend(build.get("errors", [f"gaming build_package FAILED"]))
    warnings.extend(build.get("warnings", []))

    failed = bool(errors and execute)
    return {
        "edition": "gaming",
        "final_status": "FAILED" if failed else ("APPLIED" if execute else "DRY_RUN"),
        "warnings": warnings,
        "errors": errors,
        "steps": steps,
    }
