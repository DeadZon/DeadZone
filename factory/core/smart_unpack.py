"""
DeadZone Phase 4 – Smart Unpack Orchestrator.

Single canonical entry point that accepts any supported ROM input type
and produces a unified unpack result with images/partitions metadata
and reports.  Replaces all competing unpack entry points with one
well-defined pipeline.

Supported input routes:
  payload      – OTA ZIP or folder containing payload.bin
  fastboot     – Fastboot TGZ/TAR/ZIP with images/ directory
  super        – Raw super.img (staged for later lpunpack phase)
  image_folder – Folder or archive already containing partition .img files
  new_dat      – new.dat.br / transfer.list style ROM
  unsupported  – Reports cleanly; never crashes randomly

All public functions use mezo_* or deadzone_* prefix.
Private helpers use _ prefix.
Original ROM input is never deleted or modified.
All extraction happens inside the provided Workspace.
No patch operations, UI changes, or HyperUR runtime are invoked here.
"""
from __future__ import annotations

import shutil
import tarfile
import time
import zipfile
from pathlib import Path
from typing import Any

from factory.core.payload_extract import (
    DEFAULT_PARTITIONS,
    OPTIONAL_PARTITIONS,
    REQUIRED_PARTITIONS,
    deadzone_payload_extract_stage,
)
from factory.core.rom_intake import (
    ARCHIVE_RAW,
    ARCHIVE_TAR,
    ARCHIVE_TGZ,
    ARCHIVE_ZIP,
    deadzone_rom_intake,
    mezo_detect_archive_type,
    mezo_extract_rom_archive,
    mezo_find_payload_bin,
)
from factory.core.workspace import Workspace, write_json


# ── Canonical partition lists ──────────────────────────────────────────────────

_IMAGE_PARTITIONS: list[str] = [
    "system",
    "product",
    "vendor",
    "system_ext",
    "odm",
    "mi_ext",
    "system_dlkm",
    "vendor_dlkm",
]

_REQUIRED_IMAGES: frozenset[str] = frozenset({"system", "vendor", "product"})
_OPTIONAL_IMAGES: frozenset[str] = frozenset({
    "system_ext", "odm", "mi_ext", "system_dlkm", "vendor_dlkm",
})

# Input type constants
INPUT_ZIP = "zip"
INPUT_TGZ = "tgz"
INPUT_IMG = "img"
INPUT_FOLDER = "folder"
INPUT_UNKNOWN = "unknown"

# Route constants
ROUTE_PAYLOAD = "payload"
ROUTE_FASTBOOT = "fastboot_images"
ROUTE_SUPER = "super"
ROUTE_IMAGE_FOLDER = "image_folder"
ROUTE_NEW_DAT = "new_dat"
ROUTE_UNSUPPORTED = "unsupported"


# ── Archive inspection helpers ─────────────────────────────────────────────────

def _peek_archive_members(input_path: Path) -> list[str]:
    """Return member names from a ZIP or TAR archive without extracting."""
    try:
        if zipfile.is_zipfile(input_path):
            with zipfile.ZipFile(input_path, "r") as zf:
                return zf.namelist()
    except Exception:
        pass
    try:
        with tarfile.open(input_path, "r:*") as tf:
            return tf.getnames()
    except Exception:
        pass
    return []


def _is_super_img_file(path: Path) -> bool:
    """Return True if *path* is a raw super.img by name or Android LP magic."""
    if path.name.lower() == "super.img":
        return True
    try:
        with path.open("rb") as fh:
            fh.seek(4096)
            magic = fh.read(4)
        # Android LP metadata magic: little-endian 0x534C4F57
        return magic == b"\x57\x4C\x4F\x53"
    except Exception:
        return False


def _dir_has_payload_bin(root: Path) -> Path | None:
    """Return first payload.bin found under *root*, or None."""
    hits = mezo_find_payload_bin(root)
    return hits[0] if hits else None


def _dir_has_super_img(root: Path) -> Path | None:
    """Return first super.img found under *root*, or None."""
    if not root.is_dir():
        return None
    candidates = sorted(p for p in root.rglob("super.img") if p.is_file())
    return candidates[0] if candidates else None


def _dir_img_files(root: Path) -> list[Path]:
    """Return .img files directly in *root* or inside an images/ subdirectory."""
    found: list[Path] = list(sorted(root.glob("*.img")))
    images_sub = root / "images"
    if images_sub.is_dir():
        found.extend(sorted(images_sub.glob("*.img")))
    return found


def _dir_has_new_dat_br(root: Path) -> bool:
    """Return True if any *.new.dat.br exists under *root*."""
    return any(True for _ in root.rglob("*.new.dat.br"))


# ── Input type detection ───────────────────────────────────────────────────────

def mezo_detect_rom_input_type(input_path: Path) -> str:
    """Detect the broad input category of *input_path*.

    Returns one of: "zip", "tgz", "img", "folder", "unknown".
    Does not extract or modify anything.
    """
    if input_path.is_dir():
        return INPUT_FOLDER
    if not input_path.is_file():
        return INPUT_UNKNOWN
    archive_type = mezo_detect_archive_type(input_path)
    if archive_type == ARCHIVE_ZIP:
        return INPUT_ZIP
    if archive_type in (ARCHIVE_TGZ, ARCHIVE_TAR):
        return INPUT_TGZ
    # Covers .img, .raw, .bin, .simg, .sparse and anything else
    return INPUT_IMG


# ── Route planning ─────────────────────────────────────────────────────────────

def mezo_plan_unpack_route(
    input_path: Path,
    input_type: str,
    extracted_root: Path | None = None,
) -> tuple[str, str]:
    """Determine the best unpack route for *input_path*.

    *extracted_root* is an already-extracted directory to inspect instead of
    peeking into the archive.  Pass None to let this function peek.

    Returns (route, reason) where route is one of the ROUTE_* constants and
    reason is a human-readable explanation logged in the report.
    """
    if input_type == INPUT_UNKNOWN:
        return ROUTE_UNSUPPORTED, "input path does not exist or is not a recognised type"

    if input_type == INPUT_IMG:
        if _is_super_img_file(input_path):
            return ROUTE_SUPER, "input is a super.img (detected by name or LP magic)"
        return ROUTE_UNSUPPORTED, "raw .img that is not super.img — no supported extraction path"

    if input_type == INPUT_FOLDER:
        if _dir_has_payload_bin(input_path):
            return ROUTE_PAYLOAD, "folder contains payload.bin"
        imgs = _dir_img_files(input_path)
        if imgs:
            if any(p.name.lower() == "super.img" for p in imgs):
                return ROUTE_SUPER, "folder contains super.img"
            return ROUTE_IMAGE_FOLDER, "folder contains .img files"
        if _dir_has_new_dat_br(input_path):
            return ROUTE_NEW_DAT, "folder contains *.new.dat.br files"
        return ROUTE_UNSUPPORTED, "folder has no recognised ROM artifacts"

    # ZIP or TGZ — inspect extracted root if available, otherwise peek
    if input_type in (INPUT_ZIP, INPUT_TGZ):
        if extracted_root and extracted_root.is_dir():
            if _dir_has_payload_bin(extracted_root):
                return ROUTE_PAYLOAD, "archive contains payload.bin"
            imgs = _dir_img_files(extracted_root)
            if imgs:
                if any(p.name.lower() == "super.img" for p in imgs):
                    return ROUTE_SUPER, "archive contains super.img"
                return ROUTE_FASTBOOT, "archive contains .img files (fastboot layout)"
            if _dir_has_new_dat_br(extracted_root):
                return ROUTE_NEW_DAT, "archive contains *.new.dat.br files"
            return ROUTE_UNSUPPORTED, "archive contains no recognised ROM artifacts"

        # Peek without extracting
        members = _peek_archive_members(input_path)
        lower = [m.lower() for m in members]
        if any(m.endswith("payload.bin") for m in lower):
            return ROUTE_PAYLOAD, "archive contains payload.bin"
        has_imgs = any(m.endswith(".img") for m in lower)
        if has_imgs:
            if any(m.endswith("super.img") for m in lower):
                return ROUTE_SUPER, "archive contains super.img"
            return ROUTE_FASTBOOT, "archive contains .img files (fastboot layout)"
        if any(m.endswith(".new.dat.br") for m in lower):
            return ROUTE_NEW_DAT, "archive contains *.new.dat.br files"
        return ROUTE_UNSUPPORTED, "archive contains no recognised ROM artifacts"

    return ROUTE_UNSUPPORTED, f"unrecognised input type: {input_type!r}"


# ── Image and partition collection ─────────────────────────────────────────────

def mezo_collect_unpacked_images(images_dir: Path) -> dict[str, str | None]:
    """Scan *images_dir* for extracted partition .img files.

    Returns {partition_name: absolute_path_str | None} for each canonical
    partition.  Accepts both slot-free (system.img) and _a-slot names.
    """
    result: dict[str, str | None] = {}
    for name in _IMAGE_PARTITIONS:
        candidate = images_dir / f"{name}.img"
        if not (candidate.is_file() and candidate.stat().st_size > 0):
            candidate = images_dir / f"{name}_a.img"
        if candidate.is_file() and candidate.stat().st_size > 0:
            result[name] = str(candidate)
        else:
            result[name] = None
    return result


def mezo_collect_unpacked_partitions(partitions_dir: Path) -> dict[str, str | None]:
    """Scan *partitions_dir* for extracted partition directories.

    Returns {partition_name: absolute_path_str | None} for system, product,
    vendor — the three required partitions.
    """
    result: dict[str, str | None] = {}
    for name in ("system", "product", "vendor"):
        part_dir = partitions_dir / name
        populated = part_dir.is_dir() and any(part_dir.iterdir())
        result[name] = str(part_dir) if populated else None
    return result


# ── Route executors ────────────────────────────────────────────────────────────

def _execute_route_payload_archive(input_path: Path, ws: Workspace) -> dict[str, Any]:
    """Payload route for archive inputs (zip/tgz).

    Calls deadzone_rom_intake (which handles extraction) then
    deadzone_payload_extract_stage.
    """
    try:
        intake = deadzone_rom_intake(input_path, ws)
        payload_locations = intake.get("payload_locations") or []
        payload_bin: Path | None = None
        if payload_locations:
            payload_bin = ws.extracted / payload_locations[0]
    except Exception as exc:
        return {
            "status": "FAILED",
            "payload_path": None,
            "images": {k: None for k in _IMAGE_PARTITIONS},
            "sub_reports": [],
            "error": f"rom intake failed: {exc}",
        }

    try:
        extract = deadzone_payload_extract_stage(ws, payload_bin=payload_bin)
        return {
            "status": extract.get("status", "FAILED"),
            "payload_path": extract.get("payload_path"),
            "images": mezo_collect_unpacked_images(ws.images),
            "sub_reports": [
                str(ws.reports / "deadzone_rom_intake_report.txt"),
                str(ws.reports / "deadzone_payload_extract_report.txt"),
            ],
            "error": "",
        }
    except RuntimeError as exc:
        return {
            "status": "FAILED",
            "payload_path": str(payload_bin) if payload_bin else None,
            "images": mezo_collect_unpacked_images(ws.images),
            "sub_reports": [str(ws.reports / "deadzone_rom_intake_report.txt")],
            "error": str(exc),
        }


def _execute_route_payload_folder(input_path: Path, ws: Workspace) -> dict[str, Any]:
    """Payload route for folder inputs.

    Finds payload.bin in the folder and calls deadzone_payload_extract_stage
    directly (avoids calling rom_intake which does not support folder inputs).
    """
    payload_bin_path = _dir_has_payload_bin(input_path)
    if payload_bin_path is None:
        return {
            "status": "FAILED",
            "payload_path": None,
            "images": {k: None for k in _IMAGE_PARTITIONS},
            "sub_reports": [],
            "error": "payload.bin not found in folder",
        }

    try:
        extract = deadzone_payload_extract_stage(ws, payload_bin=payload_bin_path)
        return {
            "status": extract.get("status", "FAILED"),
            "payload_path": extract.get("payload_path"),
            "images": mezo_collect_unpacked_images(ws.images),
            "sub_reports": [str(ws.reports / "deadzone_payload_extract_report.txt")],
            "error": "",
        }
    except RuntimeError as exc:
        return {
            "status": "FAILED",
            "payload_path": str(payload_bin_path),
            "images": mezo_collect_unpacked_images(ws.images),
            "sub_reports": [],
            "error": str(exc),
        }


def _copy_imgs_to_workspace(source_dir: Path, ws: Workspace) -> None:
    """Copy .img files from *source_dir* (and its images/ subdir) into ws.images."""
    ws.images.mkdir(parents=True, exist_ok=True)
    img_files: list[Path] = list(source_dir.glob("*.img"))
    images_sub = source_dir / "images"
    if images_sub.is_dir():
        img_files.extend(images_sub.glob("*.img"))
    for img in img_files:
        dest = ws.images / img.name
        if not dest.exists():
            shutil.copy2(img, dest)


def _execute_route_fastboot(
    input_path: Path,
    ws: Workspace,
    input_type: str,
) -> dict[str, Any]:
    """Fastboot route: extract archive and collect .img files."""
    if input_type in (INPUT_ZIP, INPUT_TGZ):
        try:
            mezo_extract_rom_archive(input_path, ws.extracted)
        except RuntimeError as exc:
            return {
                "status": "FAILED",
                "payload_path": None,
                "images": {k: None for k in _IMAGE_PARTITIONS},
                "sub_reports": [],
                "error": f"archive traversal blocked: {exc}",
            }
        _copy_imgs_to_workspace(ws.extracted, ws)
    elif input_type == INPUT_FOLDER:
        _copy_imgs_to_workspace(input_path, ws)

    return {
        "status": "OK",
        "payload_path": None,
        "images": mezo_collect_unpacked_images(ws.images),
        "sub_reports": [],
        "error": "",
    }


def _execute_route_super(
    input_path: Path,
    ws: Workspace,
    input_type: str,
) -> dict[str, Any]:
    """Super route: locate super.img and stage it; report ready for later lpunpack."""
    super_path: Path | None = None

    if input_type == INPUT_IMG and _is_super_img_file(input_path):
        super_path = input_path
    elif input_type == INPUT_FOLDER:
        super_path = _dir_has_super_img(input_path)
    elif input_type in (INPUT_ZIP, INPUT_TGZ):
        try:
            mezo_extract_rom_archive(input_path, ws.extracted)
        except RuntimeError as exc:
            return {
                "status": "FAILED",
                "payload_path": None,
                "super_img": None,
                "images": {k: None for k in _IMAGE_PARTITIONS},
                "sub_reports": [],
                "error": f"archive traversal blocked: {exc}",
            }
        super_path = _dir_has_super_img(ws.extracted)

    if super_path is None:
        return {
            "status": "FAILED",
            "payload_path": None,
            "super_img": None,
            "images": {k: None for k in _IMAGE_PARTITIONS},
            "sub_reports": [],
            "error": "super.img could not be located",
        }

    # Attempt to copy super.img into ws.images for canonical access
    dest_super = ws.images / "super.img"
    if super_path.resolve() != dest_super.resolve() and not dest_super.exists():
        try:
            shutil.copy2(super_path, dest_super)
            super_img_str = str(dest_super)
        except Exception:
            super_img_str = str(super_path)
    else:
        super_img_str = str(dest_super) if dest_super.is_file() else str(super_path)

    return {
        "status": "OK",
        "payload_path": None,
        "super_img": super_img_str,
        "images": mezo_collect_unpacked_images(ws.images),
        "sub_reports": [],
        "error": "",
    }


def _execute_route_image_folder(input_path: Path, ws: Workspace) -> dict[str, Any]:
    """Image folder route: collect .img files from a folder without copying them.

    Files are referenced in place unless the folder is outside ws.images, in
    which case images are collected from the source folder directly so that
    large partition images are not duplicated unnecessarily.
    """
    # Prefer in-place collection to avoid duplicating huge files
    images = mezo_collect_unpacked_images(input_path)
    # Fall back to ws.images in case something was already copied there
    if not any(images.values()):
        images = mezo_collect_unpacked_images(ws.images)
    return {
        "status": "OK",
        "payload_path": None,
        "images": images,
        "sub_reports": [],
        "error": "",
    }


def _execute_route_new_dat(
    input_path: Path,
    ws: Workspace,
    input_type: str,
) -> dict[str, Any]:
    """New dat route: try the new_dat adapter; report UNSUPPORTED cleanly on failure."""
    source = input_path

    if input_type in (INPUT_ZIP, INPUT_TGZ):
        try:
            mezo_extract_rom_archive(input_path, ws.extracted)
        except RuntimeError as exc:
            return {
                "status": "FAILED",
                "payload_path": None,
                "images": {k: None for k in _IMAGE_PARTITIONS},
                "sub_reports": [],
                "error": f"archive traversal blocked: {exc}",
            }
        source = ws.extracted

    try:
        from factory.adapters import new_dat as _new_dat_adapter
        adapter_result = _new_dat_adapter.adapt(source, ws)
        sub_reports: list[str] = []
        if adapter_result.get("report_path"):
            sub_reports.append(adapter_result["report_path"])
        if adapter_result.get("meta_path"):
            sub_reports.append(adapter_result["meta_path"])
        return {
            "status": "OK",
            "payload_path": None,
            "images": mezo_collect_unpacked_images(ws.images),
            "sub_reports": sub_reports,
            "error": "",
        }
    except Exception as exc:
        sub_reports = []
        report_path = ws.reports / "new_dat_adapter_report.txt"
        if report_path.is_file():
            sub_reports.append(str(report_path))
        return {
            "status": "UNSUPPORTED",
            "payload_path": None,
            "images": {k: None for k in _IMAGE_PARTITIONS},
            "sub_reports": sub_reports,
            "error": f"new_dat adapter unavailable or failed: {exc}",
        }


# ── Report ─────────────────────────────────────────────────────────────────────

def deadzone_write_smart_unpack_report(
    ws: Workspace,
    result: dict[str, Any],
) -> Path:
    """Write the smart unpack report and JSON metadata.

    Writes:
    - ws.reports/deadzone_smart_unpack_report.txt
    - ws.meta/smart_unpack.json

    Returns the report path.
    """
    report_path = ws.reports / "deadzone_smart_unpack_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    images: dict[str, Any] = result.get("images") or {}
    partitions: dict[str, Any] = result.get("partitions") or {}
    missing_required: list[str] = result.get("missing_required") or []
    missing_optional: list[str] = result.get("missing_optional") or []
    sub_reports: list[str] = result.get("reports") or []

    image_lines = [
        f"  {name}: {images.get(name) or '(missing)'}"
        for name in _IMAGE_PARTITIONS
    ]
    partition_lines = [
        f"  {name}: {partitions.get(name) or '(missing)'}"
        for name in ("system", "product", "vendor")
    ]

    lines = [
        "DeadZone Smart Unpack Report",
        "============================",
        f"input_path        : {result.get('input_path', '(unknown)')}",
        f"input_type        : {result.get('input_type', '(unknown)')}",
        f"route             : {result.get('route', '(unknown)')}",
        f"route_reason      : {result.get('route_reason', '(unknown)')}",
        f"status            : {result.get('status', '(unknown)')}",
        f"payload_path      : {result.get('payload_path') or '(none)'}",
        f"super_img         : {result.get('super_img') or '(none)'}",
        f"error             : {result.get('error') or '(none)'}",
        "",
        "images:",
        *image_lines,
        "",
        "partition directories:",
        *partition_lines,
        "",
        f"missing required ({len(missing_required)}):",
        *([f"  {p}" for p in missing_required] or ["  (none)"]),
        "",
        f"missing optional ({len(missing_optional)}):",
        *([f"  {p}" for p in missing_optional] or ["  (none)"]),
        "",
        "sub-reports generated:",
        *([f"  {r}" for r in sub_reports] or ["  (none)"]),
        "",
        "compatibility note:",
        "  factory/core/unpacker.py retains the unpack_rom path for callers",
        "  that supply a RomInfo object from detect_rom.  deadzone_smart_unpack",
        "  is the canonical Phase 4+ entry point for all new pipeline code.",
        "",
        "no mods executed  : True",
        "",
    ]

    report_path.write_text("\n".join(lines), encoding="utf-8")
    write_json(ws.meta / "smart_unpack.json", result)
    return report_path


# ── Main orchestrator ──────────────────────────────────────────────────────────

def deadzone_smart_unpack(
    input_path: Path,
    ws: Workspace,
) -> dict[str, Any]:
    """Smart unpack orchestrator — canonical Phase 4 entry point.

    Accepts any supported ROM input type and returns a unified result dict
    with images/partitions metadata, status, and reports.

    Safety guarantees:
    - *input_path* is never deleted or modified.
    - All extraction happens inside *ws* directories.
    - No random temp folders are created outside the workspace.
    - No patch operations, UI changes, or HyperUR runtime are invoked.
    - Unsupported input types and missing partitions are reported cleanly;
      this function does not raise unless *input_path* does not exist.

    Writes:
    - ws.meta/smart_unpack.json
    - ws.reports/deadzone_smart_unpack_report.txt

    Returns the canonical result dict.
    """
    started = time.monotonic()
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"ROM input not found: {input_path}")

    print(f"[SMART UNPACK] Input: {input_path}")

    # ── Step 1: detect input type ────────────────────────────────────────────
    input_type = mezo_detect_rom_input_type(input_path)
    print(f"[SMART UNPACK] Input type: {input_type}")

    # ── Step 2: plan route ───────────────────────────────────────────────────
    route, route_reason = mezo_plan_unpack_route(input_path, input_type)
    print(f"[SMART UNPACK] Route: {route} — {route_reason}")

    # ── Step 3: execute route ────────────────────────────────────────────────
    if route == ROUTE_PAYLOAD:
        if input_type == INPUT_FOLDER:
            route_result = _execute_route_payload_folder(input_path, ws)
        else:
            route_result = _execute_route_payload_archive(input_path, ws)

    elif route == ROUTE_FASTBOOT:
        route_result = _execute_route_fastboot(input_path, ws, input_type)

    elif route == ROUTE_SUPER:
        route_result = _execute_route_super(input_path, ws, input_type)

    elif route == ROUTE_IMAGE_FOLDER:
        route_result = _execute_route_image_folder(input_path, ws)

    elif route == ROUTE_NEW_DAT:
        route_result = _execute_route_new_dat(input_path, ws, input_type)

    else:
        route_result = {
            "status": "UNSUPPORTED",
            "payload_path": None,
            "images": {k: None for k in _IMAGE_PARTITIONS},
            "sub_reports": [],
            "error": route_reason,
        }

    # ── Step 4: build canonical result ───────────────────────────────────────
    images: dict[str, Any] = route_result.get("images") or {}
    for part in _IMAGE_PARTITIONS:
        images.setdefault(part, None)

    partitions = mezo_collect_unpacked_partitions(ws.partitions)

    missing_required = [p for p in sorted(_REQUIRED_IMAGES) if not images.get(p)]
    missing_optional = [p for p in sorted(_OPTIONAL_IMAGES) if not images.get(p)]

    raw_status = route_result.get("status", "FAILED")
    # Downgrade OK to FAILED if required images are absent
    status = "FAILED" if (raw_status == "OK" and missing_required) else raw_status

    elapsed = time.monotonic() - started

    result: dict[str, Any] = {
        "input_path": str(input_path),
        "input_type": input_type,
        "route": route,
        "route_reason": route_reason,
        "status": status,
        "payload_path": route_result.get("payload_path"),
        "super_img": route_result.get("super_img"),
        "images": images,
        "partitions": partitions,
        "missing_required": missing_required,
        "missing_optional": missing_optional,
        "reports": list(route_result.get("sub_reports") or []),
        "error": route_result.get("error") or "",
        "elapsed_seconds": elapsed,
    }

    # ── Step 5: write report and JSON ─────────────────────────────────────────
    report_path = deadzone_write_smart_unpack_report(ws, result)
    result["reports"].append(str(report_path))

    # Update JSON with final report list
    write_json(ws.meta / "smart_unpack.json", result)

    print(f"[SMART UNPACK] Status: {status}")
    print(f"[SMART UNPACK] Report: {report_path}")

    return result
