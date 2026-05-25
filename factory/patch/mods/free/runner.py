"""Free mod runner — base build package overlay only."""
from __future__ import annotations

from pathlib import Path
from typing import Any

_MOD_ROOT = Path(__file__).resolve().parent


def run_mod(
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

    from factory.patch.mods._common.build_package_patcher import apply_mod_build_package
    build_dir = _MOD_ROOT / "build"
    build = apply_mod_build_package(
        rom_root=root,
        mod_id="free",
        build_dir=build_dir if build_dir.is_dir() and any(build_dir.iterdir()) else None,
        build_url_env="FREE_BUILD_URL",
        execute=execute,
    )
    steps["build_package"] = build
    if build.get("status") == "FAILED":
        errors.extend(build.get("errors", ["free build_package FAILED"]))
    warnings.extend(build.get("warnings", []))

    failed = bool(errors and execute)
    return {
        "mod": "free",
        "final_status": "FAILED" if failed else ("APPLIED" if execute else "DRY_RUN"),
        "applied_steps": list(steps.keys()),
        "skipped_steps": [],
        "warnings": warnings,
        "errors": errors,
        "steps": steps,
        "modified_files": [],
        "vendor_modified_files": [],
    }
