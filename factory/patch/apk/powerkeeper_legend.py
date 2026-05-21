"""Compatibility wrapper for the Legend PowerKeeper patch stage."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from factory.patch.legend.powerkeeper import runner as powerkeeper_runner

_LEGEND_FLAVORS = frozenset({"legend", "deadzone_legend"})


def _is_legend(flavor: str) -> bool:
    return flavor.strip().lower().replace("-", "_") in _LEGEND_FLAVORS


def apply_legend_powerkeeper_patch(
    project_dir: Path,
    flavor: str,
    execute: bool = False,
    work_dir: Path | None = None,
) -> dict:
    """Apply or dry-run the Legend PowerKeeper patch."""
    if not _is_legend(flavor):
        return {
            "stage": "legend_powerkeeper",
            "flavor": flavor,
            "dry_run": not execute,
            "final_status": "SKIPPED_OPTIONAL",
            "warnings": ["non-Legend flavor"],
            "errors": [],
        }
    return powerkeeper_runner.apply_legend_powerkeeper_patch(
        project_dir,
        flavor,
        execute=execute,
        work_dir=work_dir,
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Legend PowerKeeper APK patch wrapper")
    parser.add_argument("--project", required=True)
    parser.add_argument("--flavor", required=True)
    parser.add_argument("--work-dir", dest="work_dir", default=None)
    parser.add_argument("--execute", action="store_true")
    return parser


def _main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(f"[powerkeeper_legend] ERROR: project directory not found: {project_dir}", file=sys.stderr)
        return 2
    report = apply_legend_powerkeeper_patch(
        project_dir,
        args.flavor,
        execute=args.execute,
        work_dir=Path(args.work_dir).resolve() if args.work_dir else None,
    )
    print(f"[powerkeeper_legend] final_status={report.get('final_status')}")
    for warning in report.get("warnings", []):
        print(f"[powerkeeper_legend] WARNING: {warning}")
    for error in report.get("errors", []):
        print(f"[powerkeeper_legend] ERROR: {error}", file=sys.stderr)
    return 1 if report.get("errors") else 0


if __name__ == "__main__":
    sys.exit(_main())
