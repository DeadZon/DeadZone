"""CLI pipeline for the legacy images, vbmeta, and firmware-info stage."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from factory.images.firmware_info_legacy import (
    generate_deadzone_firmware_info,
    resolve_effective_device,
)
from factory.images.image_collector_legacy import collect_required_images_legacy
from factory.images.report import write_images_vbmeta_legacy_reports
from factory.images.vbmeta_legacy import apply_vbmeta_legacy_patch
from factory.unpack.build_prop import read_build_props

_REPO_ROOT = Path(__file__).resolve().parents[2]


def _clean(value: str | None) -> str | None:
    if value is None:
        return None
    value = str(value).strip()
    return value or None


def _default_output_dir(project_dir: Path, output_dir: Path | None) -> Path:
    if output_dir is not None:
        return Path(output_dir)
    return project_dir / "output"


def _default_images_dir(
    project_dir: Path,
    output_dir: Path,
    images_dir: Path | None,
    device: str | None,
    android_version: str | None,
    mi_incremental: str | None,
) -> Path:
    if images_dir is not None:
        return Path(images_dir)

    props = read_build_props(project_dir)
    detected_device = _clean(props.get("ro.product.odm.device"))
    build_android = _clean(props.get("ro.system.build.version.release"))
    build_mi = _clean(props.get("ro.mi.os.version.incremental"))

    factory_device = _clean(device) or _clean(os.environ.get("DEADZONE_DEVICE_CODENAME"))
    final_device, _ = resolve_effective_device(detected_device, factory_device)
    final_android = _clean(android_version) or build_android
    final_mi = _clean(mi_incremental) or build_mi

    if final_device and final_android:
        return project_dir / f"DeadZone_{final_device}_{final_mi or ''}_{final_android}" / "images"
    return output_dir / "images"


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


def apply_images_vbmeta_legacy_stage(
    project_dir: Path,
    output_dir: Path | None = None,
    images_dir: Path | None = None,
    partition_staging_dir: Path | None = None,
    flavor: str = "legend",
    device: str | None = None,
    soc: str | None = None,
    platform: str | None = None,
    android_version: str | None = None,
    mi_incremental: str | None = None,
    vbmeta_mode: str | int | None = None,
    execute: bool = False,
) -> dict:
    """Run the legacy image/vbmeta/firmware-info stage."""
    project_dir = Path(project_dir).resolve()
    output_dir = _default_output_dir(project_dir, output_dir).resolve()
    images_dir = _default_images_dir(
        project_dir,
        output_dir,
        images_dir,
        device,
        android_version,
        mi_incremental,
    ).resolve()
    reports_dir = output_dir / "reports"

    mode = "EXECUTE" if execute else "DRY-RUN"
    print(f"[images] mode={mode} flavor={flavor} project={project_dir}")
    print(f"[images] images_dir={images_dir}")

    firmware = generate_deadzone_firmware_info(
        project_dir=project_dir,
        images_dir=images_dir,
        flavor=flavor,
        device=device,
        soc=soc,
        platform=platform,
        android_version=android_version,
        mi_incremental=mi_incremental,
        execute=execute,
    )
    collection = collect_required_images_legacy(
        project_dir=project_dir,
        images_dir=images_dir,
        partition_staging_dir=partition_staging_dir,
        execute=execute,
    )
    vbmeta = apply_vbmeta_legacy_patch(
        images_dir=images_dir,
        vbmeta_mode=vbmeta_mode,
        execute=execute,
    )

    errors = _merge_lists(
        firmware.get("errors"),
        collection.get("errors"),
        vbmeta.get("errors"),
    )
    warnings = _merge_lists(
        firmware.get("warnings"),
        collection.get("warnings"),
        vbmeta.get("warnings"),
    )
    skipped = _merge_lists(
        collection.get("skipped_items"),
        vbmeta.get("skipped_items"),
    )

    if not execute:
        final_status = "DRY_RUN"
    elif errors:
        final_status = "FAILED"
    else:
        final_status = "APPLIED"

    report = {
        "stage": "images_vbmeta_legacy",
        "dry_run": not execute,
        "project_dir": str(project_dir),
        "output_dir": str(output_dir),
        "images_dir": str(images_dir),
        "partition_staging_dir": str(partition_staging_dir) if partition_staging_dir else None,
        "flavor": flavor,
        "device": device,
        "soc": soc,
        "platform": platform,
        "android_version": firmware.get("android_version"),
        "mi_incremental": firmware.get("mi_incremental"),
        "vbmeta_mode": str(vbmeta_mode) if vbmeta_mode is not None else None,
        "detected_device_from_build_prop": firmware.get("detected_device_from_build_prop"),
        "factory_device": firmware.get("factory_device"),
        "effective_device": firmware.get("effective_device"),
        "device_decision": firmware.get("device_decision"),
        "firmware_info_status": firmware.get("status"),
        "image_collection_status": collection.get("status"),
        "vbmeta_status": vbmeta.get("status"),
        "required_images": collection.get("required_images", []),
        "optional_images": collection.get("optional_images", []),
        "found_images": collection.get("found_images", []),
        "missing_required_images": collection.get("missing_required_images", []),
        "copied_images": collection.get("copied_images", []),
        "moved_images": collection.get("moved_images", []),
        "dynamic_images_moved_to_staging": collection.get("dynamic_images_moved_to_staging", []),
        "standalone_images_moved_to_images": collection.get("standalone_images_moved_to_images", []),
        "generated_files": firmware.get("generated_files", []),
        "patched_vbmeta_files": vbmeta.get("patched_vbmeta_files", []),
        "vbmeta_files_found": vbmeta.get("vbmeta_files_found", []),
        "skipped_items": skipped,
        "warnings": warnings,
        "errors": errors,
        "final_status": final_status,
        "subreports": {
            "firmware_info": firmware,
            "image_collection": collection,
            "vbmeta": vbmeta,
        },
    }

    write_images_vbmeta_legacy_reports(report, reports_dir)
    print(f"[images] status={final_status}")
    return report


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="DeadZone legacy images, vbmeta, and firmware-info stage",
    )
    parser.add_argument("--project", required=True, help="Path to unpacked project")
    parser.add_argument("--output-dir", default=None, help="Output directory")
    parser.add_argument("--images-dir", default=None, help="Images directory")
    parser.add_argument("--flavor", default="legend", help="ROM flavor")
    parser.add_argument("--device", default=None, help="Factory device codename")
    parser.add_argument("--soc", default=None, help="SoC key")
    parser.add_argument("--platform", default=None, help="Platform key")
    parser.add_argument("--android-version", default=None, help="Android release")
    parser.add_argument("--mi-version", dest="mi_version", default=None, help="MI or HyperOS version")
    parser.add_argument("--vbmeta-mode", default=None, help="Legacy vbmeta mode value")
    parser.add_argument("--execute", action="store_true", help="Apply changes")
    return parser


def _main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(f"[images] ERROR: project directory not found: {project_dir}", file=sys.stderr)
        return 2

    report = apply_images_vbmeta_legacy_stage(
        project_dir=project_dir,
        output_dir=Path(args.output_dir).resolve() if args.output_dir else None,
        images_dir=Path(args.images_dir).resolve() if args.images_dir else None,
        flavor=args.flavor,
        device=args.device,
        soc=args.soc,
        platform=args.platform,
        android_version=args.android_version,
        mi_incremental=args.mi_version,
        vbmeta_mode=args.vbmeta_mode,
        execute=args.execute,
    )

    if report.get("errors"):
        for error in report["errors"]:
            print(f"[images] ERROR: {error}", file=sys.stderr)
        return 1
    if report.get("warnings"):
        for warning in report["warnings"]:
            print(f"[images] WARNING: {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(_main())
