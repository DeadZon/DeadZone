"""
Thin GitHub Actions / CI entrypoint for the Legend patch runner.

Usage (from a workflow or shell):
    python -m factory.patch.mods.legend.actions.run_legend \\
        --project /path/to/unpacked_rom \\
        --flavor legend \\
        [--output-dir /path/to/output] \\
        [--execute]

This file must contain NO Legend patch logic.  All work is delegated to:
    factory.patch.mods.legend.runner.run_legend
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="DeadZone Legend patch action entrypoint")
    p.add_argument("--project", required=True, type=Path, help="Unpacked ROM project directory")
    p.add_argument("--flavor", default="legend", help="ROM flavor (legend | deadzone_legend)")
    p.add_argument("--output-dir", dest="output_dir", type=Path, default=None)
    p.add_argument("--android-major", dest="android_major", type=int, default=None)
    p.add_argument("--execute", action="store_true", help="Apply patches (default: dry-run)")
    args = p.parse_args(argv)

    project_dir = args.project.resolve()
    if not project_dir.is_dir():
        print(f"[run_legend] ERROR: project directory not found: {project_dir}", file=sys.stderr)
        return 2

    from factory.patch.mods.legend.runner import run_legend

    report = run_legend(
        root=project_dir,
        output_dir=args.output_dir,
        report_path=None,
        context={
            "flavor": args.flavor,
            "android_major": args.android_major,
            "execute": args.execute,
        },
    )

    for w in report.get("warnings", []):
        print(f"[run_legend] WARNING: {w}")
    for e in report.get("errors", []):
        print(f"[run_legend] ERROR: {e}", file=sys.stderr)

    return 1 if report.get("errors") else 0


if __name__ == "__main__":
    sys.exit(main())
