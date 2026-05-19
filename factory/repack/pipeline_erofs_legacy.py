"""CLI pipeline for the legacy EROFS partition repack stage."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from factory.repack.erofs_legacy import resolve_mkfs_erofs_binary_legacy
from factory.repack.partition_legacy import KNOWN_PARTITIONS, repack_single_partition_legacy, resolve_partition_root_legacy
from factory.repack.report import write_erofs_repack_legacy_reports

_REPO_ROOT = Path(__file__).resolve().parents[2]
_OUTPUT_ROOT = _REPO_ROOT / "output"


def _default_images_dir(images_dir: Path | None) -> Path:
    if images_dir is not None:
        return Path(images_dir)
    return _OUTPUT_ROOT / "images"


def _parse_partitions(value: str | None) -> list[str] | None:
    if value is None:
        return None
    return [item.strip() for item in value.split(",") if item.strip()]


def _detect_partitions(project_dir: Path) -> list[str]:
    return [
        partition
        for partition in KNOWN_PARTITIONS
        if resolve_partition_root_legacy(project_dir, partition) is not None
    ]


def apply_erofs_repack_legacy_stage(
    project_dir: Path,
    images_dir: Path | None = None,
    flavor: str = "legend",
    partitions: list[str] | None = None,
    execute: bool = False,
) -> dict:
    """Run the legacy EROFS partition repack stage."""
    project_dir = Path(project_dir).resolve()
    images_dir = _default_images_dir(images_dir).resolve()
    reports_dir = _OUTPUT_ROOT / "reports"
    requested = partitions or _detect_partitions(project_dir)
    mkfs_path = resolve_mkfs_erofs_binary_legacy()

    print(f"[erofs_repack] mode={'EXECUTE' if execute else 'DRY-RUN'} flavor={flavor} project={project_dir}")
    print(f"[erofs_repack] images_dir={images_dir}")

    warnings: list[str] = []
    errors: list[str] = []
    skipped_items: list[dict] = []
    partitions_found: list[str] = []
    partitions_missing: list[str] = []
    commands_planned: list[list[str]] = []
    commands_executed: list[list[str]] = []
    images_created: list[str] = []
    partition_reports: list[dict] = []

    if execute:
        images_dir.mkdir(parents=True, exist_ok=True)

    for partition in requested:
        if resolve_partition_root_legacy(project_dir, partition) is None:
            partitions_missing.append(partition)
        else:
            partitions_found.append(partition)

        result = repack_single_partition_legacy(
            project_dir=project_dir,
            images_dir=images_dir,
            partition_name=partition,
            root_dir=None,
            execute=execute,
        )
        partition_reports.append(result)
        commands_planned.extend(result.get("commands_planned", []))
        commands_executed.extend(result.get("commands_executed", []))
        images_created.extend(result.get("images_created", []))
        skipped_items.extend(result.get("skipped_items", []))
        warnings.extend(result.get("warnings", []))
        errors.extend(result.get("errors", []))

        if execute and result.get("repack") is not None and result.get("status") == "FAILED":
            warnings.append(f"Stopped after failed EROFS repack for partition: {partition}")
            break

    if not requested:
        warnings.append("No partition folders were detected or requested")

    if not execute:
        final_status = "DRY_RUN" if not errors else "FAILED"
    elif errors:
        final_status = "FAILED"
    else:
        final_status = "APPLIED"

    report = {
        "stage": "erofs_repack_legacy",
        "dry_run": not execute,
        "project_dir": str(project_dir),
        "images_dir": str(images_dir),
        "flavor": flavor,
        "partitions_requested": requested,
        "partitions_found": partitions_found,
        "partitions_missing": partitions_missing,
        "mkfs_erofs_path": str(mkfs_path) if mkfs_path else None,
        "commands_planned": commands_planned,
        "commands_executed": commands_executed,
        "images_created": images_created,
        "skipped_items": skipped_items,
        "warnings": warnings,
        "errors": errors,
        "final_status": final_status,
        "partition_reports": partition_reports,
    }

    write_erofs_repack_legacy_reports(report, reports_dir)
    print(f"[erofs_repack] status={final_status}")
    return report


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="DeadZone legacy EROFS partition repack stage",
    )
    parser.add_argument("--project", required=True, help="Path to unpacked project")
    parser.add_argument("--images-dir", default=None, help="Images directory")
    parser.add_argument("--flavor", default="legend", help="ROM flavor")
    parser.add_argument("--partitions", default=None, help="Comma-separated partition names")
    parser.add_argument("--execute", action="store_true", help="Apply changes")
    return parser


def _main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(f"[erofs_repack] ERROR: project directory not found: {project_dir}", file=sys.stderr)
        return 2

    report = apply_erofs_repack_legacy_stage(
        project_dir=project_dir,
        images_dir=Path(args.images_dir).resolve() if args.images_dir else None,
        flavor=args.flavor,
        partitions=_parse_partitions(args.partitions),
        execute=args.execute,
    )

    if report.get("errors"):
        for error in report["errors"]:
            print(f"[erofs_repack] ERROR: {error}", file=sys.stderr)
        return 1
    if report.get("warnings"):
        for warning in report["warnings"]:
            print(f"[erofs_repack] WARNING: {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(_main())
