"""
Compatibility wrapper for the Legend MiuiSystemUI patch stage.

The runtime implementation lives in factory.patch.legend.mods.apk.systemui.runner.
This module preserves the old public entry point for pipeline callers.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from factory.patch.legend.mods.apk.systemui import runner as systemui_runner


def apply_legend_systemui_patch(
    project_dir: Path,
    flavor: str,
    execute: bool = False,
    work_dir: Path | None = None,
    reference_dir: Path | None = None,
) -> dict:
    """Apply or dry-run the Legend MiuiSystemUI patch."""
    report = systemui_runner.apply_systemui_patch(
        project_dir,
        flavor,
        execute=execute,
        work_dir=work_dir,
    )
    if reference_dir is not None:
        report.setdefault("warnings", []).append(
            "reference_dir is deprecated and ignored by systemui_legend"
        )
    return report


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Legend MiuiSystemUI APK patch wrapper",
    )
    parser.add_argument("--project", required=True)
    parser.add_argument("--flavor", required=True)
    parser.add_argument("--work-dir", dest="work_dir", default=None)
    parser.add_argument("--reference-dir", dest="reference_dir", default=None)
    parser.add_argument("--execute", action="store_true")
    return parser


def _main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(
            f"[systemui_legend] ERROR: project directory not found: {project_dir}",
            file=sys.stderr,
        )
        return 2

    work_dir = Path(args.work_dir).resolve() if args.work_dir else None
    reference_dir = Path(args.reference_dir).resolve() if args.reference_dir else None

    report = apply_legend_systemui_patch(
        project_dir,
        args.flavor,
        execute=args.execute,
        work_dir=work_dir,
        reference_dir=reference_dir,
    )

    print(f"[systemui_legend] final_status={report.get('final_status')}")
    for warning in report.get("warnings", []):
        print(f"[systemui_legend] WARNING: {warning}")
    for error in report.get("errors", []):
        print(f"[systemui_legend] ERROR: {error}", file=sys.stderr)

    return 1 if report.get("errors") else 0


if __name__ == "__main__":
    sys.exit(_main())
