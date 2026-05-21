"""MTK firmware image collection before final fastboot packaging."""
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path
from typing import Any


REQUIRED_MTK_FIRMWARE_IMAGES: tuple[str, ...] = (
    "apusys.img",
    "audio_dsp.img",
    "ccu.img",
    "connsys_bt.img",
    "connsys_gnss.img",
    "connsys_wifi.img",
    "dpm.img",
    "gpueb.img",
    "gz.img",
    "mcf_ota.img",
    "mcupm.img",
    "md1img.img",
    "mvpu_algo.img",
    "pi_img.img",
    "scp.img",
    "spmfw.img",
    "sspm.img",
    "vcp.img",
)

_DYNAMIC_PARTITION_IMAGES: frozenset[str] = frozenset({
    "system.img",
    "product.img",
    "vendor.img",
    "odm.img",
    "system_ext.img",
    "mi_ext.img",
})


def _is_dynamic_partition(name: str) -> bool:
    lowered = name.lower()
    return lowered in _DYNAMIC_PARTITION_IMAGES or lowered.endswith("_dlkm.img")


def _dedupe_existing(paths: list[Path]) -> list[Path]:
    seen: set[str] = set()
    result: list[Path] = []
    for path in paths:
        try:
            key = str(path.resolve())
        except OSError:
            key = str(path)
        if key in seen or not path.is_dir():
            continue
        seen.add(key)
        result.append(path)
    return result


def _search_dirs(project_dir: Path, output_dir: Path, images_dir: Path) -> list[Path]:
    work_dir = output_dir / "work"
    candidates = [
        project_dir,
        project_dir / "rom",
        project_dir / "rom" / "payload_extracted",
        project_dir / "rom" / "images",
        project_dir / "rom" / "firmware-update",
        project_dir / "payload_extracted",
        project_dir / "images",
        project_dir.parent,
        project_dir.parent / "rom",
        project_dir.parent / "rom" / "payload_extracted",
        project_dir.parent / "rom" / "images",
        project_dir.parent / "rom" / "firmware-update",
        work_dir,
        images_dir,
    ]
    return _dedupe_existing(candidates)


def _find_required_images(search_dirs: list[Path]) -> dict[str, Path]:
    wanted = {name.lower() for name in REQUIRED_MTK_FIRMWARE_IMAGES}
    found: dict[str, Path] = {}
    for root in search_dirs:
        for dirpath, dirnames, filenames in os.walk(root, topdown=True, onerror=lambda _exc: None):
            dirnames[:] = [
                name for name in dirnames
                if name not in {".git", "__pycache__"} and not name.endswith(".zip")
            ]
            for filename in sorted(filenames, key=str.lower):
                lowered = filename.lower()
                if lowered in wanted and lowered not in found and not _is_dynamic_partition(lowered):
                    found[lowered] = Path(dirpath) / filename
    return found


def _write_report(report: dict[str, Any], reports_dir: Path) -> dict[str, str]:
    reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = reports_dir / "mtk_firmware_image_collection_report.json"
    txt_path = reports_dir / "mtk_firmware_image_collection_report.txt"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=True, default=str) + "\n", encoding="utf-8")

    lines = [
        "MTK Firmware Image Collection Report",
        "====================================",
        f"device: {report.get('device')}",
        f"soc: {report.get('soc')}",
        f"status: {report.get('status')}",
        "",
        "Searched directories:",
    ]
    lines.extend(f"- {path}" for path in report.get("searched_dirs", []))
    lines.append("")
    lines.append("Found firmware images:")
    found_images = report.get("found_images", {})
    if found_images:
        lines.extend(f"- {name}: {path}" for name, path in found_images.items())
    else:
        lines.append("- (none)")
    lines.append("")
    lines.append("Copied images:")
    copied_images = report.get("copied_images", [])
    if copied_images:
        for item in copied_images:
            lines.append(f"- {item.get('image')}: {item.get('source')} -> {item.get('destination')}")
    else:
        lines.append("- (none)")
    lines.append("")
    lines.append("Missing firmware images:")
    missing_images = report.get("missing_images", [])
    if missing_images:
        lines.extend(f"- {name}" for name in missing_images)
        lines.append("")
        lines.append("MTK firmware images not present in source ROM. Provide matching fastboot TGZ or firmware pack.")
    else:
        lines.append("- (none)")
    lines.append("")

    txt_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return {"json": str(json_path), "txt": str(txt_path)}


def collect_mtk_firmware_images_legacy(
    *,
    project_dir: Path,
    output_dir: Path,
    images_dir: Path,
    device: str | None,
    soc: str | None,
    execute: bool = False,
) -> dict[str, Any]:
    """Copy required MTK firmware images into output/images and write diagnostics."""
    project_dir = Path(project_dir).resolve()
    output_dir = Path(output_dir).resolve()
    images_dir = Path(images_dir).resolve()
    reports_dir = output_dir / "reports"
    searched_dirs = _search_dirs(project_dir, output_dir, images_dir)
    found_sources = _find_required_images(searched_dirs)

    print("[mtk_firmware] searched_dirs:")
    for directory in searched_dirs:
        print(f"[mtk_firmware]   {directory}")

    copied_images: list[dict[str, str]] = []
    found_images: dict[str, str] = {}
    errors: list[str] = []

    if execute:
        try:
            images_dir.mkdir(parents=True, exist_ok=True)
        except Exception as exc:
            errors.append(f"create images directory: {exc}")

    for name in REQUIRED_MTK_FIRMWARE_IMAGES:
        source = found_sources.get(name.lower())
        existing = images_dir / name
        if source is None and existing.is_file():
            source = existing
        if source is None:
            continue
        found_images[name] = str(source)
        print(f"[mtk_firmware] found {name}: {source}")
        destination = images_dir / name
        if execute and not errors and not destination.is_file():
            try:
                shutil.copy2(source, destination)
                copied_images.append({
                    "image": name,
                    "source": str(source),
                    "destination": str(destination),
                })
                print(f"[mtk_firmware] copied {name}: {source} -> {destination}")
            except Exception as exc:
                errors.append(f"copy {name} from {source}: {exc}")

    missing_images = [
        name for name in REQUIRED_MTK_FIRMWARE_IMAGES
        if not (images_dir / name).is_file() and name not in found_images
    ]
    for name in missing_images:
        print(f"[mtk_firmware] missing {name}")

    status = "FAILED_MISSING_FIRMWARE" if missing_images or errors else "APPLIED"
    if missing_images:
        errors.append(
            "MTK firmware images not present in source ROM. "
            "Provide matching fastboot TGZ or firmware pack."
        )

    report: dict[str, Any] = {
        "device": device,
        "soc": soc,
        "dry_run": not execute,
        "required_images": list(REQUIRED_MTK_FIRMWARE_IMAGES),
        "found_images": found_images,
        "missing_images": missing_images,
        "searched_dirs": [str(path) for path in searched_dirs],
        "copied_images": copied_images,
        "status": status,
        "errors": errors,
    }
    if missing_images or errors:
        report["failure_message"] = (
            "MTK firmware images not present in source ROM. "
            "Provide matching fastboot TGZ or firmware pack."
        )
    report["report_files"] = _write_report(report, reports_dir)
    return report
