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
from factory.repack.super_collector import (
    DYNAMIC_SUPER_PARTITIONS,
    validate_super_with_lpunpack,
    write_super_build_reports as _write_collector_reports,
)
from factory.repack.super_config_legacy import sync_super_config_for_device_legacy
from factory.repack.super_info_legacy import load_super_info_legacy
from factory.repack.super_layout import (
    ALLOWED_DYNAMIC_PARTITIONS,
    extract_original_partition_sizes,
    read_original_partition_sizes,
    write_final_layout_report,
    write_original_layout_report,
)
from factory.repack.super_report import write_super_build_legacy_reports

_FORBIDDEN_DYNAMIC_IN_FINAL: frozenset[str] = frozenset(
    f"{p}.img" for p in DYNAMIC_SUPER_PARTITIONS
)

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


def _write_deadzone_patch_report(
    reports_dir: Path,
    found_dynamic: list[str],
    final_images_manifest: list[str],
    original_partition_sizes: dict[str, int],
    layout: dict,
    build_report: dict,
    validation_status: str,
    final_status: str,
    lpmake_command: list,
) -> None:
    """Write output/reports/deadzone_patch_report.txt."""
    reports_dir = Path(reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    out_path = reports_dir / "deadzone_patch_report.txt"

    non_super = [
        name for name in final_images_manifest
        if name != "super.img" and name not in {f"{p}.img" for p in ALLOWED_DYNAMIC_PARTITIONS}
    ]

    partition_sizes_header = "Original partition allocation sizes:"
    final_sizes_header = "Final partition allocation sizes:"

    lpmake_args: list[str] = []
    cmd = lpmake_command or []
    i = 0
    while i < len(cmd):
        token = str(cmd[i])
        if token == "--partition" and i + 1 < len(cmd):
            lpmake_args.append(f"  --partition {cmd[i + 1]}")
            i += 2
        else:
            i += 1

    lines = [
        "DeadZone Patch Report — Super Build",
        "====================================",
        "",
        "Dynamic images used to build super.img:",
    ]
    for part in found_dynamic:
        lines.append(f"  {part}.img")
    if not found_dynamic:
        lines.append("  (none)")

    lines += ["", "Non-super images kept for flashing:"]
    for name in sorted(non_super):
        lines.append(f"  {name}")
    if not non_super:
        lines.append("  (none)")

    lines += ["", partition_sizes_header]
    for part in ALLOWED_DYNAMIC_PARTITIONS:
        orig = original_partition_sizes.get(part)
        if orig:
            lines.append(f"  {part}: {orig} bytes")
    if not any(original_partition_sizes.get(p) for p in ALLOWED_DYNAMIC_PARTITIONS):
        lines.append("  (not available — source was payload manifest or registry)")

    lines += ["", final_sizes_header]
    final_part_sizes = layout.get("partition_image_sizes") or {}
    for part in ALLOWED_DYNAMIC_PARTITIONS:
        sz = final_part_sizes.get(part)
        if sz is not None:
            lines.append(f"  {part}: {sz} bytes (image file)")
    if not final_part_sizes:
        lines.append("  (not available)")

    lines += ["", "lpmake --partition arguments:"]
    lines.extend(lpmake_args if lpmake_args else ["  (none)"])

    lines += [
        "",
        f"Validation result:  {validation_status}",
        f"Final status:       {final_status}",
        "",
        "Excluded from final ZIP (packed inside super.img):",
    ]
    for part in ALLOWED_DYNAMIC_PARTITIONS:
        lines.append(f"  {part}.img")

    lines.append("")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[super_build] deadzone_patch_report.txt → {out_path}")


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

    # Write original_super_layout.json — captures LP allocation sizes from the
    # source ROM metadata before any repacking changes the on-disk image sizes.
    original_layout_path: Path | None = None
    if super_info_source != "missing":
        try:
            original_layout_path = write_original_layout_report(super_info, reports_dir)
        except Exception as exc:
            print(f"[super_build] WARNING: could not write original_super_layout.json: {exc}")

    # Extract per-partition original LP allocation sizes from the source metadata.
    # These are passed to lpmake so the final super uses the exact original sizes.
    original_partition_sizes: dict[str, int] = {}
    if super_info_source != "missing":
        original_partition_sizes = extract_original_partition_sizes(super_info)
        if original_partition_sizes:
            print(
                f"[super_build] original_partition_sizes ({len(original_partition_sizes)}): "
                + ", ".join(f"{k}={v}" for k, v in original_partition_sizes.items())
            )
        else:
            print(
                "[super_build] WARNING: no per-partition sizes in source metadata "
                "(source may be payload manifest only) — image file sizes will be used"
            )

    part_names = collect_part_names_legacy(partition_source, super_info)

    lpmake_path = resolve_lpmake_binary_legacy()
    if super_info_source != "missing":
        layout = derive_super_layout_legacy(partition_source, super_info, original_partition_sizes)
        build_report = build_super_image_legacy(
            images_dir=images_dir,
            output_super=output_super,
            super_info=super_info,
            partition_images_dir=partition_staging_dir,
            device=device,
            execute=execute,
            original_partition_sizes=original_partition_sizes,
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
    lpunpack_validation: dict = {}
    staging_deleted = False
    if execute and build_report.get("super_img_created"):
        validation_status, validation_errors = _validate_super_img(output_super)
        print(f"[super_build] super_img_magic_validated={validation_status}")
        if validation_status == "FAILED":
            print(f"[super_build] validation errors: {validation_errors}")

        if validation_status == "PASSED":
            # Deep LP metadata validation via lpunpack.
            selected = list(layout.get("selected_parts") or part_names)
            expected_super_size = int(layout.get("super_size") or 0) or None
            lpunpack_validation = validate_super_with_lpunpack(
                super_path=output_super,
                expected_partitions=selected,
                expected_super_size=expected_super_size,
            )
            print(f"[super_build] lpunpack_validation={lpunpack_validation.get('status')}")
            if lpunpack_validation.get("errors"):
                validation_errors.extend(lpunpack_validation["errors"])
                validation_status = "FAILED"

            # Check that final images_dir does NOT contain standalone dynamic
            # partition images — they belong in partition_staging_dir / super.img.
            forbidden_found = sorted(
                name for name in _FORBIDDEN_DYNAMIC_IN_FINAL
                if (images_dir / name).is_file()
            )
            if forbidden_found:
                msg = (
                    f"Dynamic partition images found as standalone files in "
                    f"images_dir (must be inside super.img): "
                    f"{', '.join(forbidden_found)}"
                )
                validation_errors.append(msg)
                validation_status = "FAILED"
                print(f"[super_build] ERROR: {msg}")

        if validation_status == "PASSED" and original_partition_sizes:
            # Post-build LP metadata size comparison:
            # read the final super.img LP metadata and verify every allowed
            # partition has the exact same allocation size as the original.
            try:
                from factory.repack.super_collector import _lpunpack_get_info as _lp  # type: ignore
                final_si: dict = {}
                if _lp is not None:
                    final_si = _lp(str(output_super)) or {}
                if not final_si:
                    validation_errors.append(
                        "WARNING: lpunpack_get_info returned empty result for final super.img "
                        "— skipping per-partition size comparison"
                    )
                else:
                    _fl_path, _fl_ok, _fl_errors = write_final_layout_report(
                        final_si, original_partition_sizes, reports_dir
                    )
                    if not _fl_ok:
                        for e in _fl_errors:
                            print(f"[super_build] {e}")
                        validation_errors.extend(_fl_errors)
                        validation_status = "FAILED"
                    else:
                        print("[super_build] final_super_layout comparison: PASSED")
            except Exception as exc:
                validation_errors.append(
                    f"WARNING: could not write final_super_layout.json: {exc}"
                )

        if validation_status == "PASSED" and partition_staging_dir is not None:
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

    # Build final images manifest for the report
    final_images_manifest = sorted(
        p.name for p in images_dir.glob("*.img") if p.is_file()
    ) if images_dir.is_dir() else []

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
        "lpdump_summary": lpunpack_validation.get("lpdump_summary"),
        "lpunpack_device_size": lpunpack_validation.get("device_size_in_super"),
        "lpunpack_partitions_in_super": lpunpack_validation.get("partitions_in_super", []),
        "missing_dynamic_partitions": lpunpack_validation.get("missing_partitions", missing),
        "forbidden_standalone_dynamic_images": sorted(
            name for name in _FORBIDDEN_DYNAMIC_IN_FINAL
            if (images_dir / name).is_file()
        ) if execute and images_dir.is_dir() else [],
        "final_images_manifest": final_images_manifest,
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

    # Write deadzone_patch_report.txt — human-readable super build summary.
    _write_deadzone_patch_report(
        reports_dir=reports_dir,
        found_dynamic=found,
        final_images_manifest=final_images_manifest,
        original_partition_sizes=original_partition_sizes,
        layout=layout,
        build_report=build_report,
        validation_status=validation_status,
        final_status=final_status,
        lpmake_command=build_report.get("lpmake_command", []),
    )

    # Also write the canonical super_build_report.{json,txt} consumed by CI / other tools.
    _collector_report = {
        "status": final_status,
        "payload_images_dir": str(partition_staging_dir) if partition_staging_dir else str(images_dir),
        "output_super": str(output_super),
        "final_images_dir": str(images_dir),
        "dynamic_super_partitions": {p: "" for p in found},
        "standalone_fastboot_images": {},
        "super_size": layout.get("super_size"),
        "group_name": layout.get("group_name"),
        "slot_mode": layout.get("slot_mode"),
        "output_format": layout.get("output_format"),
        "lpmake_command": build_report.get("lpmake_command", []),
        "lpmake_executed": build_report.get("lpmake_executed", False),
        "lpmake_return_code": build_report.get("return_code"),
        "lpmake_output": build_report.get("command_output"),
        "super_img_created": build_report.get("super_img_created", False),
        "super_img_size": build_report.get("super_img_size"),
        "lpdump_summary": lpunpack_validation.get("lpdump_summary"),
        "validation_status": validation_status,
        "missing_dynamic_partitions": lpunpack_validation.get("missing_partitions", missing),
        "forbidden_standalone_dynamic_images": report["forbidden_standalone_dynamic_images"],
        "final_images_manifest": final_images_manifest,
        "warnings": warnings,
        "errors": errors,
    }
    _write_collector_reports(_collector_report, reports_dir)

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
