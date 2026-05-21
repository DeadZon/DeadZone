"""Compatibility entrypoint for Provision.apk patching.

Legend flavors are handled by the clean static rule system in
``factory.patch.legend.provision``. This module remains only so older factory
call sites and CLI invocations keep working.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from factory.patch.legend.provision.runner import apply_legend_provision_patch

_REPO_ROOT = Path(__file__).resolve().parents[3]
_REPORTS_DIR = _REPO_ROOT / "output" / "reports"
_LEGEND_FLAVORS = frozenset({"legend", "deadzone_legend"})


def apply_provision_legacy_patch(
    project_dir: Path,
    flavor: str,
    execute: bool = False,
    work_dir: Path | None = None,
) -> dict:
    if flavor.strip().lower() in _LEGEND_FLAVORS:
        return apply_legend_provision_patch(project_dir, flavor, execute=execute, work_dir=work_dir)
    return {
        "stage": "provision_compatibility_entrypoint",
        "flavor": flavor,
        "dry_run": not execute,
        "project_dir": str(project_dir),
        "work_dir": str(work_dir) if work_dir else "",
        "final_status": "SKIPPED_OPTIONAL",
        "reason": "Provision legacy patch logic has been retired; only Legend flavors use the static rule system.",
    }


def _format_text_report(report: dict) -> str:
    lines = [
        "Provision APK Legacy Patch Report",
        "=" * 60,
        f"Stage         : {report.get('stage')}",
        f"Flavor        : {report.get('flavor')}",
        f"Final status  : {report.get('final_status')}",
        f"Dry run       : {report.get('dry_run')}",
        "",
        "Warnings:",
    ]
    warnings = report.get("warnings") or []
    lines.extend([f"  ~ {w}" for w in warnings] or ["  (none)"])
    lines.append("Errors:")
    errors = report.get("errors") or []
    lines.extend([f"  ! {e}" for e in errors] or ["  (none)"])
    return "\n".join(lines) + "\n"


def _write_reports(report: dict) -> None:
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = _REPORTS_DIR / "09_provision_apk_legacy_report.json"
    txt_path  = _REPORTS_DIR / "09_provision_apk_legacy_report.txt"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    txt_path.write_text(_format_text_report(report), encoding="utf-8")
    report["report_files"] = {"json": str(json_path), "txt": str(txt_path)}


def _write_report(report: dict) -> None:
    _write_reports(report)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Provision.apk compatibility patch entrypoint")
    parser.add_argument("--project", required=True)
    parser.add_argument("--flavor", required=True)
    parser.add_argument("--work-dir", dest="work_dir", default=None)
    parser.add_argument("--execute", action="store_true")
    return parser


def _main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(f"[provision_legacy] ERROR: project directory not found: {project_dir}", file=sys.stderr)
        return 2
    report = apply_provision_legacy_patch(
        project_dir=project_dir,
        flavor=args.flavor,
        execute=args.execute,
        work_dir=Path(args.work_dir).resolve() if args.work_dir else None,
    )
    _write_report(report)
    print(f"[provision_legacy] final_status={report.get('final_status')}")
    return 0 if not str(report.get("final_status", "")).startswith("FAILED") else 1


if __name__ == "__main__":
    sys.exit(_main())

