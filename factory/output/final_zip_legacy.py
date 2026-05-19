from __future__ import annotations

import argparse
import shutil
import zipfile
from pathlib import Path
from typing import Any

from .fastboot_template import REQUIRED_BIN_FILES, prepare_fastboot_template
from .flash_scripts import FLASH_ORDER, SCRIPT_NAMES, generate_windows_flash_scripts
from .report import write_final_fastboot_zip_report


REQUIRED_PUBLIC_FILES = [
    "bin/windows/fastboot.exe",
    "bin/windows/AdbWinApi.dll",
    "bin/windows/AdbWinUsbApi.dll",
    *SCRIPT_NAMES,
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
]

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


def _collect_image_files(images_dir: Path) -> list[Path]:
    images = {path.name: path for path in Path(images_dir).glob("*.img") if path.is_file()}
    ordered = [images.pop(name) for name in KNOWN_IMAGE_ORDER if name in images]
    ordered.extend(images[name] for name in sorted(images))
    return ordered


def _report_base(
    images_dir: Path,
    output_dir: Path,
    build_name: str,
    device: str,
    flavor: str,
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
        "images_dir": str(images_dir),
        "output_dir": str(output_dir),
        "staging_dir": str(staging_dir),
        "final_zip": str(final_zip),
        "template_source": None,
        "files_copied": [],
        "images_included": [],
        "images_missing": [],
        "scripts_generated": [],
        "zip_entries": [],
        "forbidden_entries": [],
        "sidecar_files_excluded": SIDECARE_FILES_EXCLUDED,
        "validation_status": "NOT_RUN",
        "warnings": [],
        "errors": [],
        "compression_mode": "ZIP_DEFLATED compresslevel=9",
        "final_status": "DRY_RUN" if not execute else "FAILED",
    }


def build_final_fastboot_zip(
    images_dir: Path,
    output_dir: Path,
    build_name: str,
    device: str,
    flavor: str = "legend",
    template_zip: Path | None = None,
    execute: bool = False,
) -> dict:
    images_dir = Path(images_dir)
    output_dir = Path(output_dir)
    template_zip = Path(template_zip) if template_zip else None
    staging_dir = output_dir / f"{build_name}_{device}_fastboot"
    final_zip = output_dir / f"{build_name}_{device}_fastboot.zip"
    report = _report_base(images_dir, output_dir, build_name, device, flavor, staging_dir, final_zip, execute)
    reports_dir = output_dir.parent / "reports"

    if not images_dir.is_dir():
        report["errors"].append(f"Images directory not found: {images_dir}")
        report["validation_status"] = "FAILED"
        report["final_status"] = "FAILED"
        report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
        return report

    image_files = _collect_image_files(images_dir)
    report["images_included"] = [path.name for path in image_files]
    report["images_missing"] = [name for name in KNOWN_IMAGE_ORDER if not (images_dir / name).is_file()]

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
        script_result = generate_windows_flash_scripts(staging_dir, images_dir, device=device, execute=False)
        report["scripts_generated"] = script_result["scripts_generated"]
        report["zip_entries"] = planned_entries
        report["forbidden_entries"] = forbidden
        report["validation_status"] = validation_status
        report["final_status"] = "DRY_RUN" if validation_status == "PASSED" else "FAILED"
        report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
        return report

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

    script_result = generate_windows_flash_scripts(staging_dir, staged_images, device=device, execute=True)
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

    with zipfile.ZipFile(final_zip, "r") as zf:
        zip_entries = [_normalize_entry(name) for name in zf.namelist()]
    zip_validation_status, zip_forbidden = _validate_entries(zip_entries)
    report["zip_entries"] = zip_entries
    report["forbidden_entries"] = zip_forbidden
    report["validation_status"] = zip_validation_status
    report["final_status"] = "APPLIED" if zip_validation_status == "PASSED" else "FAILED"
    if zip_validation_status != "PASSED":
        report["errors"].append("ZIP validation failed after creation.")

    report["report_files"] = write_final_fastboot_zip_report(report, reports_dir)
    return report


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build the DeadZone final fastboot ZIP.")
    parser.add_argument("--images-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--build-name", required=True)
    parser.add_argument("--device", required=True)
    parser.add_argument("--flavor", default="legend")
    parser.add_argument("--template-zip", type=Path)
    parser.add_argument("--execute", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    report = build_final_fastboot_zip(
        images_dir=args.images_dir,
        output_dir=args.output_dir,
        build_name=args.build_name,
        device=args.device,
        flavor=args.flavor,
        template_zip=args.template_zip,
        execute=args.execute,
    )
    print(f"final_status={report['final_status']}")
    print(f"validation_status={report['validation_status']}")
    print(f"final_zip={report['final_zip']}")
    print(f"template_source={report['template_source']}")
    return 0 if report["final_status"] in {"DRY_RUN", "APPLIED"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
