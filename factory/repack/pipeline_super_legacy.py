"""CLI pipeline for the legacy super.img lpmake build stage."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from factory.repack.super_builder_legacy import (
    build_super_image_legacy,
    collect_part_names_legacy,
    derive_super_layout_legacy,
    resolve_lpmake_binary_legacy,
)
from factory.repack.super_config_legacy import sync_super_config_for_device_legacy
from factory.repack.super_info_legacy import load_super_info_legacy
from factory.repack.super_report import write_super_build_legacy_reports

_REPO_ROOT = Path(__file__).resolve().parents[2]
_OUTPUT_ROOT = _REPO_ROOT / "output"


def _merge_lists(*values: object) -> list:
    result: list = []
    for value in values:
        if not value:
            continue
        if isinstance(value, list):
            result.extend(value)
        else:
            result.append(value)
    return result


def apply_super_build_legacy_stage(
    project_dir: Path,
    images_dir: Path,
    output_super: Path | None = None,
    flavor: str = "legend",
    device: str | None = None,
    soc: str | None = None,
    platform: str | None = None,
    execute: bool = False,
) -> dict:
    """Run the legacy lpmake super.img build stage."""
    project_dir = Path(project_dir).resolve()
    images_dir = Path(images_dir).resolve()
    output_super = Path(output_super).resolve() if output_super is not None else (images_dir / "super.img").resolve()
    reports_dir = _OUTPUT_ROOT / "reports"

    print(f"[super_build] mode={'EXECUTE' if execute else 'DRY-RUN'} flavor={flavor} project={project_dir}")
    print(f"[super_build] images_dir={images_dir}")
    print(f"[super_build] output_super={output_super}")

    sync_report = sync_super_config_for_device_legacy(
        project_dir=project_dir,
        images_dir=images_dir,
        device=device,
        soc=soc,
        platform=platform,
        execute=execute,
    )
    super_info = load_super_info_legacy(
        project_dir=project_dir,
        images_dir=images_dir,
        device=device,
        soc=soc,
        platform=platform,
        execute=execute,
    )
    super_info_source = super_info.get("_super_info_source", "missing")
    part_names = collect_part_names_legacy(images_dir, super_info)

    lpmake_path = resolve_lpmake_binary_legacy()
    if super_info_source != "missing":
        layout = derive_super_layout_legacy(images_dir, super_info)
        build_report = build_super_image_legacy(
            images_dir=images_dir,
            output_super=output_super,
            super_info=super_info,
            device=device,
            execute=execute,
        )
    else:
        layout = {
            "super_size": None,
            "group_name": None,
            "group_size": None,
            "slot_mode": None,
            "virtual_ab": None,
            "output_format": None,
            "selected_parts": part_names,
            "partition_image_sizes": {},
        }
        build_report = {
            "status": "FAILED",
            "lpmake_path": str(lpmake_path) if lpmake_path else None,
            "lpmake_command": [],
            "lpmake_executed": False,
            "super_img_created": False,
            "super_img_size": None,
            "skipped_items": [{"item": "super.img", "reason": "super_info missing"}],
            "warnings": [],
            "errors": ["Cannot build super.img because dynamic partition metadata is missing"],
        }

    requested = list(layout.get("selected_parts") or part_names)
    found = [
        part
        for part in requested
        if (images_dir / f"{part}.img").is_file() or (images_dir / f"{part}_a.img").is_file()
    ]
    missing = [part for part in requested if part not in found]

    warnings = _merge_lists(super_info.get("warnings"), sync_report.get("warnings"), build_report.get("warnings"))
    errors = _merge_lists(super_info.get("errors"), sync_report.get("errors"), build_report.get("errors"))
    skipped = _merge_lists(sync_report.get("skipped_items"), build_report.get("skipped_items"))

    if not execute:
        final_status = "DRY_RUN" if not errors else "FAILED"
    elif errors:
        final_status = "FAILED"
    else:
        final_status = "APPLIED"

    report = {
        "stage": "super_build_legacy",
        "dry_run": not execute,
        "project_dir": str(project_dir),
        "images_dir": str(images_dir),
        "output_super": str(output_super),
        "device": device,
        "soc": soc,
        "platform": platform,
        "flavor": flavor,
        "super_info_source": super_info_source,
        "super_size": layout.get("super_size"),
        "group_name": layout.get("group_name"),
        "group_size": layout.get("group_size"),
        "slot_mode": layout.get("slot_mode"),
        "virtual_ab": layout.get("virtual_ab"),
        "output_format": layout.get("output_format"),
        "partitions_requested": requested,
        "partitions_found": found,
        "partitions_missing": missing,
        "partition_image_sizes": layout.get("partition_image_sizes", {}),
        "lpmake_path": build_report.get("lpmake_path") or (str(lpmake_path) if lpmake_path else None),
        "lpmake_command": build_report.get("lpmake_command", []),
        "lpmake_output": build_report.get("command_output"),
        "lpmake_executed": build_report.get("lpmake_executed", False),
        "super_img_created": build_report.get("super_img_created", False),
        "super_img_size": build_report.get("super_img_size"),
        "validation_status": None,
        "skipped_items": skipped,
        "warnings": warnings,
        "errors": errors,
        "final_status": final_status,
        "subreports": {
            "sync_super_config": sync_report,
            "build_super": build_report,
        },
    }

    write_super_build_legacy_reports(report, reports_dir)
    print(f"[super_build] status={final_status}")
    return report


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="DeadZone legacy super.img lpmake build stage")
    parser.add_argument("--project", required=True, help="Path to unpacked project")
    parser.add_argument("--images-dir", required=True, help="Images directory with rebuilt partition images")
    parser.add_argument("--output-super", default=None, help="Output super.img path")
    parser.add_argument("--flavor", default="legend", help="ROM flavor")
    parser.add_argument("--device", default=None, help="Factory device codename")
    parser.add_argument("--soc", default=None, help="SoC key")
    parser.add_argument("--platform", default=None, help="Platform key")
    parser.add_argument("--execute", action="store_true", help="Apply changes")
    return parser


def _main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    project_dir = Path(args.project).resolve()
    images_dir = Path(args.images_dir).resolve()
    if not project_dir.is_dir():
        print(f"[super_build] ERROR: project directory not found: {project_dir}", file=sys.stderr)
        return 2
    if not images_dir.is_dir():
        print(f"[super_build] ERROR: images directory not found: {images_dir}", file=sys.stderr)
        return 2

    report = apply_super_build_legacy_stage(
        project_dir=project_dir,
        images_dir=images_dir,
        output_super=Path(args.output_super).resolve() if args.output_super else None,
        flavor=args.flavor,
        device=args.device,
        soc=args.soc,
        platform=args.platform,
        execute=args.execute,
    )

    if report.get("errors"):
        for error in report["errors"]:
            print(f"[super_build] ERROR: {error}", file=sys.stderr)
        return 1
    if report.get("warnings"):
        for warning in report["warnings"]:
            print(f"[super_build] WARNING: {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(_main())
