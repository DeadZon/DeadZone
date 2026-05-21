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
        return apply_legend_provision_patch(
            project_dir,
            flavor,
            execute=execute,
            work_dir=work_dir,
        )

    return {
        "stage": "provision_compatibility_entrypoint",
        "flavor": flavor,
        "dry_run": not execute,
        "project_dir": str(project_dir),
        "work_dir": str(work_dir) if work_dir else "",
        "final_status": "SKIPPED_OPTIONAL",
        "reason": "Provision legacy patch logic has been retired; only Legend flavors use the static rule system.",
        "warnings": [],
        "errors": [],
    }


def _format_text_report(report: dict) -> str:
    mode = "DRY RUN" if report.get("dry_run") else "EXECUTE"

    lines = [
        f"DeadZone Provision APK Legacy Report  [{mode}]",
        "=" * 60,
        f"Stage         : {report.get('stage', '?')}",
        f"Final status  : {report.get('final_status', '?')}",
        f"Flavor        : {report.get('flavor', '?')}",
        f"Project dir   : {report.get('project_dir', '?')}",
        f"Work dir      : {report.get('work_dir', '?')}",
        "",
    ]

    reason = report.get("reason")
    if reason:
        lines.extend(
            [
                "Reason:",
                f"  {reason}",
                "",
            ]
        )

    warnings = report.get("warnings") or []
    lines.append("Warnings:")
    if warnings:
        lines.extend(f"  ~ {warning}" for warning in warnings)
    else:
        lines.append("  (none)")

    errors = report.get("errors") or []
    lines.append("Errors:")
    if errors:
        lines.extend(f"  ! {error}" for error in errors)
    else:
        lines.append("  (none)")

    actions = report.get("actions") or report.get("operations") or report.get("patched_files") or []
    if actions:
        lines.append("")
        lines.append("Actions:")
        if isinstance(actions, dict):
            for key, value in actions.items():
                lines.append(f"  - {key}: {value}")
        elif isinstance(actions, list):
            for item in actions:
                lines.append(f"  - {item}")
        else:
            lines.append(f"  - {actions}")

    report_files = report.get("report_files") or {}
    if report_files:
        lines.append("")
        lines.append("Report files:")
        if isinstance(report_files, dict):
            for key, value in report_files.items():
                lines.append(f"  - {key}: {value}")
        else:
            lines.append(f"  - {report_files}")

    lines.append("")
    return "\n".join(lines)


def _write_report(report: dict) -> None:
    """Backward-compatible single JSON writer used by older CLI flows."""
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    path = _REPORTS_DIR / "09_provision_apk_legacy_report.json"
    path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )

    report["report_files"] = {
        "json": str(path),
    }


def _write_reports(report: dict, output_dir: Path | None = None) -> None:
    """Write JSON and TXT reports for pipeline callers expecting _write_reports.

    Some newer/older factory stages import this symbol directly. Keeping it here
    prevents the Provision APK stage from failing before the real patch runner
    gets a chance to execute.
    """
    reports_dir = (Path(output_dir) / "reports") if output_dir else _REPORTS_DIR
    reports_dir.mkdir(parents=True, exist_ok=True)

    json_path = reports_dir / "09_provision_apk_legacy_report.json"
    txt_path = reports_dir / "09_provision_apk_legacy_report.txt"

    report["report_files"] = {
        "json": str(json_path),
        "txt": str(txt_path),
    }

    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )
    txt_path.write_text(
        _format_text_report(report),
        encoding="utf-8",
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Provision.apk compatibility patch entrypoint"
    )
    parser.add_argument("--project", required=True)
    parser.add_argument("--flavor", required=True)
    parser.add_argument("--work-dir", dest="work_dir", default=None)
    parser.add_argument("--execute", action="store_true")
    return parser


def _main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(
            f"[provision_legacy] ERROR: project directory not found: {project_dir}",
            file=sys.stderr,
        )
        return 2

    work_dir = Path(args.work_dir).resolve() if args.work_dir else None

    report = apply_provision_legacy_patch(
        project_dir=project_dir,
        flavor=args.flavor,
        execute=args.execute,
        work_dir=work_dir,
    )

    # Keep the old CLI behavior, but write both JSON and TXT now.
    _write_reports(report)

    print(f"[provision_legacy] final_status={report.get('final_status')}")

    return 0 if not str(report.get("final_status", "")).startswith("FAILED") else 1


if __name__ == "__main__":
    sys.exit(_main())
