"""
DeadZone Phase 2 – ROM Intake Stage.

Orchestrates safe archive extraction, payload.bin discovery,
build.prop metadata collection, and intake report generation.

All public functions use mezo_* or deadzone_* prefix.
Private helpers use _ prefix.
This module never deletes or modifies the original ROM input.
All extraction happens exclusively inside ws.extracted.
"""
from __future__ import annotations

import shutil
import tarfile
import zipfile
from pathlib import Path
from typing import Any

from factory.core.unpacker import _safe_destination
from factory.core.workspace import Workspace, write_json

# Archive type identifiers
ARCHIVE_ZIP = "zip"
ARCHIVE_TGZ = "tgz"
ARCHIVE_TAR = "tar"
ARCHIVE_RAW = "raw"

# Build.prop keys to collect — mirrors HyperUR BUILD_PROP_KEYS + slot/model extras
_INTAKE_PROP_KEYS = frozenset({
    "ro.product.odm.brand",
    "ro.product.odm.device",
    "ro.product.odm.model",
    "ro.product.odm.marketname",
    "ro.product.vendor.brand",
    "ro.product.vendor.device",
    "ro.product.vendor.model",
    "ro.product.vendor.marketname",
    "ro.product.product.device",
    "ro.product.system.device",
    "ro.product.device",
    "ro.mi.os.version.incremental",
    "ro.system.build.version.release",
    "ro.build.version.release",
    "ro.vendor.build.version.release",
    "ro.build.version.incremental",
})

# Partition directories to search for build.prop, in priority order
_PROP_PARTITION_PRIORITY = ("system", "product", "vendor", "odm")


# ── Archive type detection ────────────────────────────────────────────────────

_RAW_EXTENSIONS = frozenset({".img", ".raw", ".bin", ".simg", ".sparse"})


def mezo_detect_archive_type(path: Path) -> str:
    """Detect archive type from *path* by name suffix then file sniffing.

    Known archive extensions (.zip, .tgz, .tar.gz, .tar) are returned
    immediately without sniffing.  Known raw image extensions (.img, .raw,
    .bin, .simg, .sparse) are also returned immediately as "raw" so that
    null-padded disk images are never mis-identified as TAR archives.

    For any other extension, content is sniffed (zip magic, tar header).

    Returns one of: "zip", "tgz", "tar", "raw".
    """
    name = path.name.lower()
    if name.endswith(".zip"):
        return ARCHIVE_ZIP
    if name.endswith((".tgz", ".tar.gz")):
        return ARCHIVE_TGZ
    if name.endswith(".tar"):
        return ARCHIVE_TAR
    # Short-circuit raw disk-image extensions before sniffing
    suffix = Path(name).suffix
    if suffix in _RAW_EXTENSIONS:
        return ARCHIVE_RAW
    # Sniff for ambiguous or unknown extensions
    if path.is_file():
        if zipfile.is_zipfile(path):
            return ARCHIVE_ZIP
        try:
            if tarfile.is_tarfile(path):
                suffixes = [s.lower() for s in path.suffixes]
                return ARCHIVE_TGZ if ".gz" in suffixes else ARCHIVE_TAR
        except Exception:
            pass
    return ARCHIVE_RAW


# ── Safe archive extraction ───────────────────────────────────────────────────

def _extract_zip_intake(src: Path, dst: Path) -> None:
    """Extract zip *src* into *dst* with traversal protection."""
    with zipfile.ZipFile(src, "r") as zf:
        for info in zf.infolist():
            _safe_destination(dst, info.filename)
        zf.extractall(dst)


def _extract_tar_intake(src: Path, dst: Path, mode: str = "r:*") -> None:
    """Extract tar *src* into *dst* with traversal protection."""
    with tarfile.open(src, mode) as tf:
        for member in tf.getmembers():
            _safe_destination(dst, member.name)
        tf.extractall(dst)


def mezo_extract_rom_archive(src: Path, dst: Path) -> str:
    """Extract ROM archive *src* safely into *dst*.

    Handles .zip, .tgz, .tar.gz, .tar, and raw .img passthrough.
    Traversal attacks (../ paths, absolute paths) raise RuntimeError.
    Never modifies or deletes *src*.

    Returns the detected archive type string.
    """
    dst.mkdir(parents=True, exist_ok=True)
    archive_type = mezo_detect_archive_type(src)

    if archive_type == ARCHIVE_ZIP:
        _extract_zip_intake(src, dst)
    elif archive_type == ARCHIVE_TGZ:
        _extract_tar_intake(src, dst, mode="r:gz")
    elif archive_type == ARCHIVE_TAR:
        _extract_tar_intake(src, dst, mode="r:*")
    else:
        # Raw passthrough — copy file as-is, preserve name
        shutil.copy2(src, dst / src.name)

    return archive_type


# ── Payload.bin discovery ─────────────────────────────────────────────────────

def mezo_find_payload_bin(extracted_root: Path) -> list[Path]:
    """Recursively search *extracted_root* for payload.bin files.

    Returns a sorted list of absolute paths found.
    Returns an empty list (no exception) if nothing is found.
    """
    if not extracted_root.is_dir():
        return []
    return sorted(p for p in extracted_root.rglob("payload.bin") if p.is_file())


# ── Build.prop metadata ───────────────────────────────────────────────────────

def mezo_parse_single_build_prop(path: Path) -> dict[str, str]:
    """Parse *path* as a build.prop file, returning only known intake keys.

    Skips comment lines and malformed entries.
    Keys not in _INTAKE_PROP_KEYS are silently discarded.
    """
    props: dict[str, str] = {}
    if not path.is_file():
        return props
    try:
        for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip()
            if key in _INTAKE_PROP_KEYS and key not in props:
                props[key] = value
    except Exception:
        pass
    return props


def _prop_priority(path: Path) -> tuple[int, int]:
    """Sort key: prefer system > product > vendor > odm > others, shallow first."""
    parts = [p.lower() for p in path.parts]
    for i, name in enumerate(_PROP_PARTITION_PRIORITY):
        if name in parts:
            return i, len(path.parts)
    return 99, len(path.parts)


def mezo_read_build_prop_metadata(extracted_root: Path) -> dict[str, Any]:
    """Aggregate build.prop metadata from all partitions in *extracted_root*.

    Mirrors the HyperUR reference BUILD_PROP_KEYS aggregation logic.
    Searches system, product, vendor, odm first, then any remaining partitions.

    Returns a dict with normalised fields:
        codename, model, marketname, brand,
        mi_version, android_release,
        prop_files_found (int)
    """
    prop_files: list[Path] = []
    if extracted_root.is_dir():
        prop_files = sorted(
            (p for p in extracted_root.rglob("build.prop") if p.is_file()),
            key=_prop_priority,
        )

    aggregated: dict[str, str] = {}
    for prop_path in prop_files:
        parsed = mezo_parse_single_build_prop(prop_path)
        for key, value in parsed.items():
            aggregated.setdefault(key, value)

    codename = (
        aggregated.get("ro.product.odm.device")
        or aggregated.get("ro.product.vendor.device")
        or aggregated.get("ro.product.product.device")
        or aggregated.get("ro.product.system.device")
        or aggregated.get("ro.product.device")
        or ""
    )
    model = (
        aggregated.get("ro.product.odm.model")
        or aggregated.get("ro.product.vendor.model")
        or ""
    )
    marketname = (
        aggregated.get("ro.product.odm.marketname")
        or aggregated.get("ro.product.vendor.marketname")
        or ""
    )
    brand = (
        aggregated.get("ro.product.odm.brand")
        or aggregated.get("ro.product.vendor.brand")
        or ""
    )
    mi_version = aggregated.get("ro.mi.os.version.incremental") or ""
    android_release = (
        aggregated.get("ro.system.build.version.release")
        or aggregated.get("ro.build.version.release")
        or aggregated.get("ro.vendor.build.version.release")
        or ""
    )

    return {
        "codename": codename.lower() if codename else "",
        "model": model,
        "marketname": marketname,
        "brand": brand,
        "mi_version": mi_version,
        "android_release": android_release,
        "prop_files_found": len(prop_files),
    }


# ── Report ────────────────────────────────────────────────────────────────────

def deadzone_write_rom_intake_report(ws: Workspace, intake_result: dict[str, Any]) -> Path:
    """Write the ROM intake report to ws.reports/deadzone_rom_intake_report.txt.

    Includes: input ROM path, archive type, payload status, extracted roots,
    and all detected metadata fields.
    Returns the report path.
    """
    report_path = ws.reports / "deadzone_rom_intake_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    metadata: dict[str, Any] = intake_result.get("metadata") or {}
    payload_locations: list[str] = intake_result.get("payload_locations") or []
    extracted_roots: list[str] = intake_result.get("extracted_roots") or []
    payload_status = "FOUND" if intake_result.get("payload_found") else "MISSING"

    lines = [
        "DeadZone ROM Intake Report",
        "==========================",
        f"input_rom         : {intake_result.get('input_rom', '(unknown)')}",
        f"archive_type      : {intake_result.get('archive_type', '(unknown)')}",
        f"payload_status    : {payload_status}",
        "",
        "payload locations:",
    ]
    lines += [f"  {loc}" for loc in payload_locations] or ["  (none)"]
    lines += [
        "",
        "extracted roots:",
    ]
    lines += [f"  {r}" for r in extracted_roots] or ["  (none)"]
    lines += [
        "",
        "detected metadata:",
        f"  codename        : {metadata.get('codename') or '(unknown)'}",
        f"  model           : {metadata.get('model') or '(unknown)'}",
        f"  marketname      : {metadata.get('marketname') or '(unknown)'}",
        f"  brand           : {metadata.get('brand') or '(unknown)'}",
        f"  mi_version      : {metadata.get('mi_version') or '(unknown)'}",
        f"  android_release : {metadata.get('android_release') or '(unknown)'}",
        f"  prop_files_found: {metadata.get('prop_files_found', 0)}",
        "",
    ]

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


# ── Main intake orchestrator ──────────────────────────────────────────────────

def deadzone_rom_intake(rom_path: Path, ws: Workspace) -> dict[str, Any]:
    """Intake a ROM: extract safely, discover payload.bin, collect build.prop metadata.

    Safety guarantees:
    - *rom_path* is never modified or deleted.
    - Extraction writes only inside ws.extracted.
    - Traversal attacks in archive members raise RuntimeError before extraction.

    Returns the intake result dict and writes:
    - ws.meta/rom_intake.json
    - ws.reports/deadzone_rom_intake_report.txt
    """
    if not rom_path.exists():
        raise FileNotFoundError(f"ROM input not found: {rom_path}")

    print(f"[INTAKE] Input: {rom_path}")
    archive_type = mezo_extract_rom_archive(rom_path, ws.extracted)
    print(f"[INTAKE] Archive type: {archive_type}")

    extracted_roots = sorted(
        str(p.relative_to(ws.extracted))
        for p in ws.extracted.iterdir()
    ) if ws.extracted.is_dir() else []

    payload_paths = mezo_find_payload_bin(ws.extracted)
    payload_found = bool(payload_paths)
    payload_locations = [str(p.relative_to(ws.extracted)) for p in payload_paths]
    print(f"[INTAKE] Payload status: {'FOUND' if payload_found else 'MISSING'}")
    for loc in payload_locations:
        print(f"[INTAKE] Payload at: {loc}")

    metadata = mezo_read_build_prop_metadata(ws.extracted)
    print(f"[INTAKE] Codename: {metadata.get('codename') or '(unknown)'}")
    print(f"[INTAKE] Marketname: {metadata.get('marketname') or '(unknown)'}")
    print(f"[INTAKE] MI version: {metadata.get('mi_version') or '(unknown)'}")
    print(f"[INTAKE] Android: {metadata.get('android_release') or '(unknown)'}")

    result: dict[str, Any] = {
        "input_rom": str(rom_path),
        "archive_type": archive_type,
        "extracted_roots": extracted_roots,
        "payload_found": payload_found,
        "payload_locations": payload_locations,
        "metadata": metadata,
    }

    write_json(ws.meta / "rom_intake.json", result)
    deadzone_write_rom_intake_report(ws, result)
    print(f"[INTAKE] Report: {ws.reports / 'deadzone_rom_intake_report.txt'}")

    return result
