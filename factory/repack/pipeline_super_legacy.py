"""CLI pipeline for the legacy super.img lpmake build stage."""
from __future__ import annotations

import argparse
import shutil
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

# LP geometry header magic at byte offset 4096 in a raw LP super image ("gDla" LE).
_LP_GEOMETRY_MAGIC = b"\x67\x44\x6c\x61"
# Android sparse image magic (simg_header_t.magic = 0xED26FF3A LE).
_SPARSE_MAGIC = b"\x3a\xff\x26\xed"
# Absolute minimum size for any real super.img (100 MiB).
_SUPER_MIN_SIZE_BYTES = 100 * 1024 * 1024


def _validate_super_img(super_path: Path) -> tuple[str, list[str]]:
    """Return ("PASSED", []) or ("FAILED", [reasons]) for the built super.img.

    Checks:
      1. File exists at expected path.
      2. Size >= 100 MiB (guards against an empty or truncated output).
      3. Magic bytes: accepts a sparse image header (offset 0) or a raw LP
         geometry header (offset 4096).  Either format is a valid lpmake output.
    """
    errors: list[str] = []
    if not super_path.exists():
        errors.append(f"super.img not found at: {super_path}")
        return "FAILED", errors

    size = super_path.stat().st_size
    if size < _SUPER_MIN_SIZE_BYTES:
        errors.append(
            f"super.img size {size} bytes is below the 100 MiB sanity threshold "
            f"— image is likely corrupt or lpmake produced an empty file"
        )
        return "FAILED", errors

    try:
        with super_path.open("rb") as fh:
            first4 = fh.read(4)
        if first4 == _SPARSE_MAGIC:
            # Valid Android sparse image (lpmake --sparse output).
            pass
        else:
            # Expect a raw LP image: geometry header at offset 4096.
            with super_path.open("rb") as fh:
                fh.seek(4096)
                geo4 = fh.read(4)
            if geo4 != _LP_GEOMETRY_MAGIC:
                errors.append(
                    f"super.img header mismatch — "
                    f"offset-0 bytes: {first4.hex()!r}, "
                    f"offset-4096 bytes: {geo4.hex()!r}; "
                    f"expected sparse magic {_SPARSE_MAGIC.hex()!r} "
                    f"or LP geometry magic {_LP_GEOMETRY_MAGIC.hex()!r}"
                )
                return "FAILED", errors
    except OSError as exc:
        errors.append(f"Could not read super.img for validation: {exc}")
        return "FAILED", errors

    return "PASSED", []


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


def _delete_partition_staging_dir(staging_dir: Path, warnings: list[str]) -> bool:
    """Delete the temporary partition staging directory.

    This mirrors MEZOBuildRom's cleanup_after_repack() — it is called only
    after super.img has been validated so that the workspace is clean before
    the final ZIP is assembled.  Returns True if deletion succeeded.
    """
    if not staging_dir.is_dir():
        return True
    try:
        shutil.rmtree(staging_dir)
        print(f"[super_build] partition_staging_dir_deleted={staging_dir}")
        return True
    except Exception as exc:
        warnings.append(f"Could not delete partition staging dir {staging_dir}: {exc}")
        return False


def apply_super_build_legacy_stage(
    project_dir: Path,
    images_dir: Path,
    output_super: Path | None = None,
    partition_staging_dir: Path | None = None,
    flavor: str = "legend",
    device: str | None = None,
    soc: str | None = None,
    platform: str | None = None,
    execute: bool = False,
) -> dict:
    """Run the legacy lpmake super.img build stage.

    partition_staging_dir — temporary directory holding the EROFS-repacked
                            dynamic partition images (MEZOBuildRom-style staging).
                            When provided, lpmake reads partition images from here
                            and writes super.img to output_super (output/images/).
                            On successful super.img validation the staging dir is
                            deleted so that output/images/ never contains individual
                            dynamic partition images.
                            When omitted, images_dir is used as the source (old
                            behavior, kept for backward-compatibility).
    """
    project_dir = Path(project_dir).resolve()
    images_dir = Path(images_dir).resolve()
    output_super = Path(output_super).resolve() if output_super is not None else (images_dir / "super.img").resolve()
    partition_staging_dir = Path(partition_staging_dir).resolve() if partition_staging_dir is not None else None
    reports_dir = _OUTPUT_ROOT / "reports"

    # Partition images live in staging dir (new) or fall back to images_dir (old).
    partition_source = partition_staging_dir if partition_staging_dir is not None else images_dir

    print(f"[super_build] mode={'EXECUTE' if execute else 'DRY-RUN'} flavor={flavor} project={project_dir}")
    print(f"[super_build] images_dir={images_dir}")
    print(f"[super_build] partition_staging_dir={partition_staging_dir}")
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
    part_names = collect_part_names_legacy(partition_source, super_info)

    lpmake_path = resolve_lpmake_binary_legacy()
    if super_info_source != "missing":
        layout = derive_super_layout_legacy(partition_source, super_info)
        build_report = build_super_image_legacy(
            images_dir=images_dir,
            output_super=output_super,
            super_info=super_info,
            partition_images_dir=partition_staging_dir,
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

    # ── Validate super.img after successful build ────────────────────────────
    validation_errors: list[str] = []
    staging_deleted = False
    if execute and build_report.get("super_img_created"):
        validation_status, validation_errors = _validate_super_img(output_super)
        print(f"[super_build] super_img_validated={validation_status}")
        if validation_status == "FAILED":
            print(f"[super_build] validation errors: {validation_errors}")
        elif validation_status == "PASSED" and partition_staging_dir is not None:
            # Mirroring MEZOBuildRom cleanup_after_repack(): once super.img is
            # validated, the temporary partition images are no longer needed.
            # Deleting them ensures output/images/ holds only super.img and
            # standalone boot/vbmeta/dtbo images — so the final ZIP is correct.
            _warnings_for_staging: list[str] = []
            staging_deleted = _delete_partition_staging_dir(partition_staging_dir, _warnings_for_staging)
            if _warnings_for_staging:
                validation_errors.extend(_warnings_for_staging)
    elif not execute:
        validation_status = "DRY_RUN"
    else:
        # Build did not produce the file — validation cannot proceed.
        validation_status = "NOT_BUILT"

    # Check partition presence in partition_source (staging or images_dir).
    requested = list(layout.get("selected_parts") or part_names)
    found = [
        part
        for part in requested
        if (partition_source / f"{part}.img").is_file() or (partition_source / f"{part}_a.img").is_file()
    ]
    missing = [part for part in requested if part not in found]

    warnings = _merge_lists(super_info.get("warnings"), sync_report.get("warnings"), build_report.get("warnings"))
    errors = _merge_lists(super_info.get("errors"), sync_report.get("errors"), build_report.get("errors"), validation_errors)
    skipped = _merge_lists(sync_report.get("skipped_items"), build_report.get("skipped_items"))

    if not execute:
        final_status = "DRY_RUN" if not errors else "FAILED"
    elif errors or validation_status not in {"PASSED", "DRY_RUN"}:
        final_status = "FAILED"
    else:
        final_status = "APPLIED"

    report = {
        "stage": "super_build_legacy",
        "dry_run": not execute,
        "project_dir": str(project_dir),
        "images_dir": str(images_dir),
        "partition_staging_dir": str(partition_staging_dir) if partition_staging_dir else None,
        "partition_staging_dir_deleted": staging_deleted,
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
        "lpmake_sparse_enabled": build_report.get("lpmake_sparse_enabled", False),
        "super_img_created": build_report.get("super_img_created", False),
        "super_img_size": build_report.get("super_img_size"),
        "validation_status": validation_status,
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
    parser.add_argument("--images-dir", required=True, help="Final fastboot images directory (output/images/)")
    parser.add_argument("--partition-staging-dir", default=None,
                        help="Temporary directory containing EROFS partition images for lpmake input")
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
        partition_staging_dir=Path(args.partition_staging_dir).resolve() if args.partition_staging_dir else None,
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
