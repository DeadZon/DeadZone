from __future__ import annotations

import argparse
import os
import shutil
import zipfile
from pathlib import Path
from typing import Any

from .fastboot_template import REQUIRED_BIN_FILES, prepare_fastboot_template
from .flash_scripts import (
    FLASH_ORDER,
    MTK_VAB_REQUIRED_IMAGES,
    SCRIPT_NAMES,
    generate_windows_flash_scripts,
    validate_mtk_required_images,
)
from .report import write_final_fastboot_zip_report


REQUIRED_PUBLIC_FILES = [
    "bin/windows/fastboot.exe",
    "bin/windows/AdbWinApi.dll",
    "bin/windows/AdbWinUsbApi.dll",
    *SCRIPT_NAMES,
]

# Images packed inside super.img — excluded from the public ZIP when super.img is present.
DYNAMIC_PARTITION_IMAGES: frozenset[str] = frozenset({
    "system.img",
    "system_ext.img",
    "system_dlkm.img",
    "product.img",
    "vendor.img",
    "vendor_dlkm.img",
    "odm.img",
    "odm_dlkm.img",
    "mi_ext.img",
    "my_product.img",
    "my_engineering.img",
    "my_stock.img",
    "my_heytap.img",
    "my_region.img",
})

REQUIRED_FINAL_IMAGES = [
    "super.img",
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "vbmeta.img",
]

SIDECARE_FILES_EXCLUDED = [
    "sha256sums.txt",
    "build_info.txt",
    "logs.zip",
    "upload_links.txt",
    "final_zip_name.zip.sha256",
]

FORBIDDEN_NAMES = {
    "sha256sums.txt",
    "build_info.txt",
    "upload_links.txt",
    "README",
    "README.txt",
    "README.md",
    "Flash_2.bat",
    "Flash MTK.bat",
}

FORBIDDEN_SUBSTRINGS = [
    "runner",
    "/home/",
    "logs",
    "output/reports",
    ".git",
    "__pycache__",
    "HyperUR",
    "work/",
]

# Image filenames that must never appear in the final ZIP regardless of location.
FORBIDDEN_IMAGE_NAMES: frozenset[str] = frozenset({
    "super.unsparse.img",
    "super_metadata.img",
    "lpdump.img",
    "lpdump_validation.img",
})

KNOWN_IMAGE_ORDER = [image for _, image in FLASH_ORDER]


def _normalize_entry(path: str) -> str:
    return path.replace("\\", "/").lstrip("/")


def _is_allowed_entry(name: str) -> bool:
    normalized = _normalize_entry(name)
    if normalized in REQUIRED_PUBLIC_FILES:
        return True
    return normalized.startswith("images/") and normalized.endswith(".img") and normalized.count("/") == 1


def _forbidden_reason(name: str) -> str | None:
    normalized = _normalize_entry(name)
    lowered = normalized.lower()
    leaf = normalized.rsplit("/", 1)[-1]
    if name.startswith("/") or ":\\" in name or ":/" in name:
        return "absolute path"
    if leaf in FORBIDDEN_NAMES:
        return "forbidden file"
    if leaf.lower().endswith(".zip.sha256"):
        return "sidecar checksum"
    if leaf.lower().endswith(".unsparse.img"):
        return "unsparse image must not be in final ZIP"
    if leaf in FORBIDDEN_IMAGE_NAMES:
        return f"forbidden image: {leaf}"
    for pattern in FORBIDDEN_SUBSTRINGS:
        if pattern.lower() in lowered:
            return f"forbidden pattern: {pattern}"
    if not _is_allowed_entry(normalized):
        return "not in public ZIP allowlist"
    return None


def _validate_entries(entries: list[str]) -> tuple[str, list[str]]:
    forbidden = []
    for entry in entries:
        reason = _forbidden_reason(entry)
        if reason:
            forbidden.append(f"{entry} ({reason})")
    required_missing = [entry for entry in REQUIRED_PUBLIC_FILES if entry not in entries]
    forbidden.extend(f"{entry} (missing required public file)" for entry in required_missing)
    return ("PASSED" if not forbidden else "FAILED", forbidden)


def _iter_staging_files(staging_dir: Path) -> list[Path]:
    return sorted(path for path in staging_dir.rglob("*") if path.is_file())


def _is_dynamic_partition(name: str) -> bool:
    return name in DYNAMIC_PARTITION_IMAGES or name.endswith("_dlkm.img")


def _is_excluded_super_artifact(name: str) -> bool:
    """Return True for super build artifacts that must never enter the final ZIP."""
    lower = name.lower()
    return (
        lower.endswith(".unsparse.img")
        or name in FORBIDDEN_IMAGE_NAMES
    )


def _collect_image_files(
    images_dir: Path,
    exclude: frozenset[str] | None = None,
) -> tuple[list[Path], list[str]]:
    images = {path.name: path for path in Path(images_dir).glob("*.img") if path.is_file()}
    excluded_names: list[str] = []
    for name in list(images.keys()):
        if _is_excluded_super_artifact(name):
            excluded_names.append(name)
            del images[name]
        elif exclude and _is_dynamic_partition(name):
            excluded_names.append(name)
            del images[name]
    ordered = [images.pop(name) for name in KNOWN_IMAGE_ORDER if name in images]
    ordered.extend(images[name] for name in sorted(images))
    return ordered, sorted(excluded_names)


def _report_base(
    images_dir: Path,
    output_dir: Path,
    build_name: str,
    device: str,
    flavor: str,
    soc: str | None,
    staging_dir: Path,
    final_zip: Path,
    execute: bool,
) -> dict[str, Any]:
    return {
        "stage": "final_fastboot_zip",
        "dry_run": not execute,
        "build_name": build_name,
        "device": device,
        "flavor": flavor,
        "soc": soc,
        "images_dir": str(images_dir),
        "output_dir": str(output_dir),
        "staging_dir": str(staging_dir),
        "final_zip": str(final_zip),
        "template_source": None,
        "files_copied": [],
        "images_included": [],
        "images_missing": [],
        "images_missing_required": [],
        "scripts_generated": [],
        "zip_entries": [],
        "forbidden_entries": [],
        "sidecar_files_excluded": SIDECARE_FILES_EXCLUDED,
        "validation_status": "NOT_RUN",
        "warnings": [],
        "errors": [],
        "compression_mode": "ZIP_DEFLATED compresslevel=9",
        "super_img_detected": False,
        "images_excluded_dynamic": [],
        "dynamic_images_excluded_from_final_zip": [],
        "forbidden_dynamic_images_in_output_images": [],
        "missing_final_required_images": [],
        "final_zip_image_list": [],
        "zip_size_mib": None,
        "final_zip_size_mib": None,
        "final_status": "DRY_RUN" if not execute else "FAILED",
    }


def _write_github_summary_missing(missing: list[str], device: str) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    lines = [
        "## MTK Fastboot Image Validation — FAILED",
        f"Device: `{device}`",
        "",
        f"**{len(missing)} required firmware image(s) missing from images directory:**",
        "",
    ]
    lines.extend(f"- `{name}`" for name in missing)
    lines += [
        "",
        "Build aborted. Fix the ROM extraction or SoC firmware pack before re-running.",
    ]
    with open(summary_path, "a", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def build_final_fastboot_zip(
    images_dir: Path,
    output_dir: Path,
    build_name: str,
    device: str,
    flavor: str = "legend",
    soc: str | None = None,
    template_zip: Path | None = None,
    execute: bool = False,
    # Optional ROM metadata forwarded to the BAT header generator
    device_model: str | None = None,
    android_version: str | None = None,
    build_incremental: str | None = None,
    platform: str | None = None,
) -> dict:
    images_dir = Path(images_dir)
    output_dir = Path(output_dir)
    template_zip = Path(template_zip) if template_zip else None
    staging_dir = output_dir / f"{build_name}_{device}_fastboot"
    final_zip = output_dir / f"{build_name}_{device}_fastboot.zip"
    report = _report_base(images_dir, output_dir, build_name, device, flavor, soc, staging_dir, final_zip, execute)
    reports_dir = output_dir.parent / "reports"

    if not images_dir.is_dir():
        report["errors"].append(f"Images directory not found: {images_dir}")
        report["validation_status"] = "FAILED"
        report["final_status"] = "FAILED"
        report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
        return report

    # Strict MTK firmware completeness check — must pass before any ZIP is built.
    if soc == "mtk":
        missing_required = validate_mtk_required_images(images_dir)
        report["images_missing_required"] = missing_required
        if missing_required:
            report["errors"].append(
                f"MTK fastboot validation failed: {len(missing_required)} required firmware "
                f"image(s) missing: {', '.join(missing_required)}"
            )
            report["errors"].append(
                "MTK firmware images not present in source ROM. "
                "Provide matching fastboot TGZ or firmware pack."
            )
            report["validation_status"] = "FAILED"
            report["final_status"] = "FAILED"
            _write_github_summary_missing(missing_required, device)
            report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
            return report

    # Hard-fail guard: dynamic partition images must never reach output/images.
    # They belong in partition_staging_dir and are packed into super.img by lpmake.
    _FORBIDDEN_DYNAMIC: frozenset[str] = frozenset({
        "system.img", "product.img", "vendor.img", "system_ext.img",
        "odm.img", "odm_dlkm.img", "mi_ext.img",
        "vendor_dlkm.img", "system_dlkm.img",
    })
    forbidden_found = sorted(name for name in _FORBIDDEN_DYNAMIC if (images_dir / name).is_file())
    report["forbidden_dynamic_images_in_output_images"] = forbidden_found
    if forbidden_found:
        msg = (
            f"output/images contains forbidden dynamic partition images that must be "
            f"in partition_staging_dir, not in the final fastboot directory: "
            f"{', '.join(forbidden_found)}"
        )
        report["errors"].append(msg)
        report["validation_status"] = "FAILED"
        report["final_status"] = "FAILED"
        print(f"[final_zip] ERROR: {msg}")
        report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
        return report

    has_super = (images_dir / "super.img").is_file()
    report["super_img_detected"] = has_super
    exclude = DYNAMIC_PARTITION_IMAGES if has_super else frozenset()

    image_files, excluded_dynamic = _collect_image_files(images_dir, exclude=exclude)
    report["images_included"] = [path.name for path in image_files]
    report["final_zip_image_list"] = report["images_included"]
    report["images_excluded_dynamic"] = excluded_dynamic
    report["dynamic_images_excluded_from_final_zip"] = excluded_dynamic
    report["images_missing"] = [name for name in KNOWN_IMAGE_ORDER if not (images_dir / name).is_file()]

    # Hard-fail: required final images must all be present before packaging.
    missing_final_required = [name for name in REQUIRED_FINAL_IMAGES if not (images_dir / name).is_file()]
    report["missing_final_required_images"] = missing_final_required
    if missing_final_required:
        msg = (
            f"missing_final_required_images: {', '.join(missing_final_required)} — "
            f"final_zip_image_list={[p.name for p in image_files]}"
        )
        report["errors"].append(msg)
        report["validation_status"] = "FAILED"
        report["final_status"] = "FAILED"
        print(f"[final_zip] ERROR: {msg}")
        report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
        return report

    print(f"[final_zip] super_img_detected={has_super}")
    print(f"[final_zip] compression_mode=ZIP_DEFLATED compresslevel=9")
    print(f"[final_zip] final_zip_image_list={[p.name for p in image_files]}")
    print(f"[final_zip] images_included ({len(image_files)}): {', '.join(p.name for p in image_files)}")
    if excluded_dynamic:
        print(
            f"[final_zip] dynamic_images_excluded_from_final_zip "
            f"({len(excluded_dynamic)}): {', '.join(excluded_dynamic)}"
        )
    else:
        print("[final_zip] dynamic_images_excluded_from_final_zip=(none)")

    template_result = prepare_fastboot_template(staging_dir, template_zip=template_zip, execute=False)
    report["template_source"] = template_result.get("template_source")
    report["files_copied"].extend(template_result.get("files_copied", []))
    report["warnings"].extend(template_result.get("warnings", []))
    report["errors"].extend(template_result.get("errors", []))
    if template_result.get("status") in {"FAILED", "SKIPPED_MISSING_TEMPLATE"}:
        report["validation_status"] = "FAILED"
        report["final_status"] = "FAILED"
        report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
        return report

    if not execute:
        planned_entries = [
            *(f"bin/windows/{name}" for name in REQUIRED_BIN_FILES),
            *(f"images/{path.name}" for path in image_files),
            *SCRIPT_NAMES,
        ]
        validation_status, forbidden = _validate_entries(planned_entries)
        script_result = generate_windows_flash_scripts(
            staging_dir, images_dir,
            device=device, soc=soc, platform=platform, flavor=flavor,
            device_model=device_model, android_version=android_version,
            build_incremental=build_incremental,
            execute=False,
        )
        report["scripts_generated"] = script_result["scripts_generated"]
        report["zip_entries"] = planned_entries
        report["forbidden_entries"] = forbidden
        report["validation_status"] = validation_status
        report["final_status"] = "DRY_RUN" if validation_status == "PASSED" else "FAILED"
        report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
        return report

    # ── execute path continues below ────────────────────────────────────────────

    if staging_dir.exists():
        shutil.rmtree(staging_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    template_result = prepare_fastboot_template(staging_dir, template_zip=template_zip, execute=True)
    report["files_copied"] = template_result.get("files_copied", [])
    report["template_source"] = template_result.get("template_source")
    report["warnings"].extend(template_result.get("warnings", []))
    report["errors"].extend(template_result.get("errors", []))
    if template_result.get("status") != "APPLIED":
        report["validation_status"] = "FAILED"
        report["final_status"] = "FAILED"
        report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
        return report

    staged_images = staging_dir / "images"
    staged_images.mkdir(parents=True, exist_ok=True)
    for image in image_files:
        shutil.copy2(image, staged_images / image.name)
        report["files_copied"].append(f"images/{image.name}")

    script_result = generate_windows_flash_scripts(
        staging_dir, staged_images,
        device=device, soc=soc, platform=platform, flavor=flavor,
        device_model=device_model, android_version=android_version,
        build_incremental=build_incremental,
        execute=True,
    )
    report["scripts_generated"] = script_result["scripts_generated"]

    staging_entries = [_normalize_entry(str(path.relative_to(staging_dir))) for path in _iter_staging_files(staging_dir)]
    validation_status, forbidden = _validate_entries(staging_entries)
    report["forbidden_entries"] = forbidden
    report["validation_status"] = validation_status
    if validation_status != "PASSED":
        report["errors"].append("Staging validation failed; final ZIP was not created.")
        report["final_status"] = "FAILED"
        report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
        return report

    if final_zip.exists():
        final_zip.unlink()
    with zipfile.ZipFile(final_zip, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in _iter_staging_files(staging_dir):
            arcname = _normalize_entry(str(path.relative_to(staging_dir)))
            zf.write(path, arcname)

    zip_size_bytes = final_zip.stat().st_size
    zip_size_mib = zip_size_bytes / (1024 * 1024)
    report["zip_size_mib"] = round(zip_size_mib, 1)
    report["final_zip_size_mib"] = report["zip_size_mib"]
    print(f"[final_zip] zip_size_mib={zip_size_mib:.1f}")
    print(f"[final_zip] final_zip_size_mib={zip_size_mib:.1f}")
    if zip_size_mib > 6000:
        msg = f"Final ZIP size {zip_size_mib:.1f} MiB exceeds 6000 MiB — verify no duplicate images were included"
        report["warnings"].append(msg)
        print(f"[final_zip] WARNING: {msg}")

    with zipfile.ZipFile(final_zip, "r") as zf:
        zip_entries = [_normalize_entry(name) for name in zf.namelist()]
    zip_validation_status, zip_forbidden = _validate_entries(zip_entries)
    report["zip_entries"] = zip_entries
    report["forbidden_entries"] = zip_forbidden
    report["validation_status"] = zip_validation_status
    report["final_status"] = "APPLIED" if zip_validation_status == "PASSED" else "FAILED"
    if zip_validation_status != "PASSED":
        report["errors"].append("ZIP validation failed after creation.")
    else:
        try:
            shutil.rmtree(staging_dir)
            report["warnings"].append(f"Staging dir removed after successful ZIP: {staging_dir.name}")
        except Exception as exc:
            report["warnings"].append(f"Staging dir cleanup failed (non-fatal): {exc}")

    report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
    return report


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build the DeadZone final fastboot ZIP.")
    parser.add_argument("--images-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--build-name", required=True)
    parser.add_argument("--device", required=True)
    parser.add_argument("--flavor", default="legend")
    parser.add_argument("--soc", default=None)
    parser.add_argument("--template-zip", type=Path)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--device-model", default=None)
    parser.add_argument("--android-version", default=None)
    parser.add_argument("--build-incremental", default=None)
    parser.add_argument("--platform", default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    report = build_final_fastboot_zip(
        images_dir=args.images_dir,
        output_dir=args.output_dir,
        build_name=args.build_name,
        device=args.device,
        flavor=args.flavor,
        soc=args.soc,
        template_zip=args.template_zip,
        execute=args.execute,
        device_model=args.device_model,
        android_version=args.android_version,
        build_incremental=args.build_incremental,
        platform=args.platform,
    )
    print(f"final_status={report['final_status']}")
    print(f"validation_status={report['validation_status']}")
    print(f"final_zip={report['final_zip']}")
    print(f"template_source={report['template_source']}")
    return 0 if report["final_status"] in {"DRY_RUN", "APPLIED"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
