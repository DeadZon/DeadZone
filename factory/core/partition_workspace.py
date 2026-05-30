"""
DeadZone Phase 7/8 – Partition Workspace Stage.

Converts the unified smart_unpack result into a normalized partition workspace.
Reads smart_unpack images/super output and produces:
  - Extracted partition directories under ws.partitions/
  - fs_config / file_contexts metadata per partition
  - output/meta/partition_workspace.json
  - output/reports/deadzone_partition_workspace_report.txt

Supported input routes (via smart_unpack result):
  payload      – images extracted by deadzone_payload_extract_stage
  fastboot     – images collected from fastboot layout
  image_folder – images collected from a source folder
  super        – lpunpack attempted via mezo_extract_super_to_images
  new_dat      – images collected via new_dat adapter

Extraction supports:
  android_sparse – simg2img conversion into ws.root/raw_images/
  raw_ext4       – debugfs rdump or pure-Python ext4 extractor
  raw_erofs      – fsck.erofs/erofsfuse/dump.erofs; EXTRACTOR_TOOL_MISSING if absent
  super_lp       – lpunpack into ws.root/super_images/; not_wired if lpunpack absent
  unknown        – 7z fallback; fails cleanly if unavailable

All public functions use mezo_* or deadzone_* prefix.
Private helpers use _ prefix.
Original ROM input is never deleted or modified.
All extraction happens inside the provided Workspace.
No patch operations, UI changes, or HyperUR runtime are invoked here.
"""
from __future__ import annotations

import time
from pathlib import Path
from typing import Any

from factory.core.fs_config import mezo_regenerate_fs_metadata
from factory.core.image_extractor import (  # noqa: PLC2701
    _detect_format,
    _entry,
    _extract_7z,
    _extract_erofs,
    _extract_ext4,
    _run,
)
from factory.core.toolchain import resolve_toolchain
from factory.core.workspace import Workspace, read_json, write_json


# ── Canonical partition lists ─────────────────────────────────────────────────

_REQUIRED_PARTITIONS: frozenset[str] = frozenset({"system", "vendor", "product"})
_OPTIONAL_PARTITIONS: frozenset[str] = frozenset({
    "system_ext", "odm", "mi_ext", "system_dlkm", "vendor_dlkm",
})
_ALL_PARTITIONS: list[str] = [
    "system",
    "product",
    "vendor",
    "system_ext",
    "odm",
    "mi_ext",
    "system_dlkm",
    "vendor_dlkm",
]

# ── Image format detection constants ─────────────────────────────────────────

_ANDROID_SPARSE_MAGIC = b"\x3a\xff\x26\xed"
_EXT4_MAGIC_OFFSET = 0x438
_EXT4_MAGIC = b"\x53\xef"
# LP metadata geometry magic: 0x616c4467 in little-endian byte order
_LP_GEOMETRY_MAGIC = b"\x67\x44\x6c\x61"
_LP_GEOMETRY_OFFSET = 4096

# ── Output subdirectory names ─────────────────────────────────────────────────

_RAW_IMAGES_SUBDIR = "raw_images"
_SUPER_IMAGES_SUBDIR = "super_images"


# ── Phase 8 public extraction primitives ─────────────────────────────────────

def mezo_detect_partition_image_format(
    img_path: Path,
    toolchain: Any,
) -> dict[str, str]:
    """Detect the filesystem format of a partition image.

    Checks (in order): android_sparse, raw_ext4, raw_erofs, super_lp, unknown.
    Zero-byte or missing images return format="unknown".

    Returns {"format": str, "detail": str}.
    """
    if not img_path.is_file() or img_path.stat().st_size == 0:
        return {"format": "unknown", "detail": "file missing or zero-byte"}

    try:
        with img_path.open("rb") as fh:
            header = fh.read(8192)
    except OSError as exc:
        return {"format": "unknown", "detail": str(exc)}

    if header.startswith(_ANDROID_SPARSE_MAGIC):
        return {"format": "android_sparse", "detail": "android sparse magic at offset 0"}

    if header[_EXT4_MAGIC_OFFSET:_EXT4_MAGIC_OFFSET + 2] == _EXT4_MAGIC:
        return {"format": "raw_ext4", "detail": "ext4 superblock magic at offset 0x438"}

    if b"EROFS" in header[:2048] or header[1024:1028] == b"EroS":
        return {"format": "raw_erofs", "detail": "erofs magic"}

    if (
        len(header) >= _LP_GEOMETRY_OFFSET + 4
        and header[_LP_GEOMETRY_OFFSET:_LP_GEOMETRY_OFFSET + 4] == _LP_GEOMETRY_MAGIC
    ):
        return {"format": "super_lp", "detail": "LP metadata geometry magic at offset 4096"}

    # Delegate remainder to the shared _detect_format (uses `file` tool if available)
    file_tool = toolchain.path("file") if toolchain else None
    fmt, detail = _detect_format(img_path, file_tool)
    return {"format": fmt, "detail": detail}


def mezo_convert_sparse_image_if_needed(
    img_path: Path,
    partition_name: str,
    ws: Workspace,
    toolchain: Any,
) -> dict[str, Any]:
    """Convert a sparse Android image to raw using simg2img.

    The raw image is written to ws.root/raw_images/{partition_name}.raw.img.
    The original image is never modified.

    Returns {
        "converted": bool,
        "raw_path": str | None,
        "error": str,
        "error_type": str,   # "" | "EXTRACTOR_TOOL_MISSING" | "SPARSE_CONVERSION_FAILED"
        "simg2img_path": str,
    }
    Non-sparse images return converted=False without error.
    """
    detection = mezo_detect_partition_image_format(img_path, toolchain)
    if detection["format"] != "android_sparse":
        return {
            "converted": False,
            "raw_path": None,
            "error": "",
            "error_type": "",
            "simg2img_path": "",
        }

    simg2img = toolchain.path("simg2img") if toolchain else None
    if not simg2img:
        return {
            "converted": False,
            "raw_path": None,
            "error": "simg2img not available",
            "error_type": "EXTRACTOR_TOOL_MISSING",
            "simg2img_path": "",
        }

    raw_dir = ws.root / _RAW_IMAGES_SUBDIR
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_img = raw_dir / f"{partition_name}.raw.img"
    log = ws.logs / f"sparse_convert_{partition_name}.log"

    code, error = _run([str(simg2img), str(img_path), str(raw_img)], log)
    if code == 0 and raw_img.is_file() and raw_img.stat().st_size > 0:
        return {
            "converted": True,
            "raw_path": str(raw_img),
            "error": "",
            "error_type": "",
            "simg2img_path": str(simg2img),
        }
    return {
        "converted": False,
        "raw_path": None,
        "error": error or f"simg2img exited {code}",
        "error_type": "SPARSE_CONVERSION_FAILED",
        "simg2img_path": str(simg2img),
    }


def mezo_extract_ext4_image(
    img_path: Path,
    partition_name: str,
    ws: Workspace,
    toolchain: Any,
) -> dict[str, Any]:
    """Extract a raw EXT4 image into ws.partitions/{partition_name}.

    Uses debugfs rdump first, then pure-Python ext4 extractor, then loop-mount.
    Fails cleanly with error_type="EXTRACTOR_TOOL_MISSING" when no method is available.

    Returns {
        "status": "extracted" | "failed",
        "extractor_used": str,
        "tool_path": str,
        "extracted_path": str,
        "error": str,
        "error_type": str,
    }
    """
    target = ws.partitions / partition_name
    log = ws.logs / f"ext4_extract_{partition_name}.log"
    status, method_or_reason, tool = _extract_ext4(img_path, target, toolchain, log)
    if status == "extracted":
        return {
            "status": "extracted",
            "extractor_used": method_or_reason,
            "tool_path": tool,
            "extracted_path": str(target),
            "error": "",
            "error_type": "",
        }
    reason_lower = method_or_reason.lower()
    if "missing" in reason_lower or "not available" in reason_lower or "no ext4" in reason_lower:
        error_type = "EXTRACTOR_TOOL_MISSING"
    else:
        error_type = "EXTRACTION_FAILED"
    return {
        "status": "failed",
        "extractor_used": "ext4",
        "tool_path": tool,
        "extracted_path": str(target),
        "error": method_or_reason,
        "error_type": error_type,
    }


def mezo_extract_erofs_image(
    img_path: Path,
    partition_name: str,
    ws: Workspace,
    toolchain: Any,
) -> dict[str, Any]:
    """Extract a raw EROFS image into ws.partitions/{partition_name}.

    Tries fsck.erofs → erofsfuse → dump.erofs listing.
    If no EROFS tool is available returns error_type="EXTRACTOR_TOOL_MISSING"
    rather than raising, so the caller can report cleanly.

    Returns {
        "status": "extracted" | "listed_only" | "failed",
        "extractor_used": str,
        "tool_path": str,
        "extracted_path": str,
        "error": str,
        "error_type": str,
    }
    """
    target = ws.partitions / partition_name
    log = ws.logs / f"erofs_extract_{partition_name}.log"
    cap_log: list[str] = []
    status, method_or_reason, tool = _extract_erofs(img_path, target, toolchain, log, cap_log)

    if status == "extracted":
        return {
            "status": "extracted",
            "extractor_used": method_or_reason,
            "tool_path": tool,
            "extracted_path": str(target),
            "error": "",
            "error_type": "",
        }
    if status == "listed_only":
        return {
            "status": "listed_only",
            "extractor_used": method_or_reason,
            "tool_path": tool,
            "extracted_path": str(target),
            "error": method_or_reason,
            "error_type": "LISTED_ONLY",
        }

    reason_lower = method_or_reason.lower()
    if (
        "not available" in reason_lower
        or "not installed" in reason_lower
        or "no erofs" in reason_lower
        or "install erofs" in reason_lower
    ):
        error_type = "EXTRACTOR_TOOL_MISSING"
    else:
        error_type = "EXTRACTION_FAILED"
    return {
        "status": "failed",
        "extractor_used": "erofs",
        "tool_path": tool,
        "extracted_path": str(target),
        "error": method_or_reason,
        "error_type": error_type,
    }


def mezo_extract_super_to_images(
    ws: Workspace,
    toolchain: Any,
) -> dict[str, Any]:
    """Extract super.img into ws.root/super_images/ using lpunpack.

    If lpunpack is not available or super.img is absent, returns status="not_wired"
    with a clear reason — never crashes.
    Extraction only — no partition build tools, no repacking, no super image creation.

    Returns {
        "status": "extracted" | "failed" | "not_wired",
        "reason": str,
        "tool": str,
        "super_images_dir": str,
        "extracted_partitions": list[str],
    }
    """
    super_img = ws.images / "super.img"
    if not super_img.is_file():
        return {
            "status": "not_wired",
            "reason": "super extraction not wired: super.img not found in workspace",
            "tool": "",
            "super_images_dir": "",
            "extracted_partitions": [],
        }

    lpunpack = toolchain.path("lpunpack") if toolchain else None
    if not lpunpack:
        return {
            "status": "not_wired",
            "reason": "super extraction not wired: lpunpack not available",
            "tool": "",
            "super_images_dir": "",
            "extracted_partitions": [],
        }

    super_images_dir = ws.root / _SUPER_IMAGES_SUBDIR
    super_images_dir.mkdir(parents=True, exist_ok=True)
    log = ws.logs / "super_extract_lpunpack.log"
    code, error = _run([str(lpunpack), str(super_img), str(super_images_dir)], log)

    if code == 0:
        extracted = sorted(p.name for p in super_images_dir.glob("*.img"))
        return {
            "status": "extracted",
            "reason": "",
            "tool": str(lpunpack),
            "super_images_dir": str(super_images_dir),
            "extracted_partitions": extracted,
        }
    return {
        "status": "failed",
        "reason": error or f"lpunpack exited {code}",
        "tool": str(lpunpack),
        "super_images_dir": str(super_images_dir),
        "extracted_partitions": [],
    }


# ── Public stage functions ────────────────────────────────────────────────────

def mezo_select_partition_images(
    smart_unpack_result: dict,
) -> dict[str, str | None]:
    """Select candidate partition images from a smart_unpack result.

    Returns {partition_name: abs_path_str | None} for all canonical partitions.
    Paths that are missing or zero-byte are normalised to None.
    """
    raw: dict = smart_unpack_result.get("images") or {}
    result: dict[str, str | None] = {}
    for name in _ALL_PARTITIONS:
        path_str = raw.get(name)
        if path_str:
            p = Path(path_str)
            if p.is_file() and p.stat().st_size > 0:
                result[name] = path_str
            else:
                result[name] = None
        else:
            result[name] = None
    return result


def mezo_extract_partition_image(
    img_path: Path,
    partition_name: str,
    ws: Workspace,
    toolchain: Any,
) -> dict[str, Any]:
    """Extract one partition image into ws.partitions/{partition_name}.

    Handles sparse → raw conversion (writes to ws.root/raw_images/).
    Routes EXT4 → mezo_extract_ext4_image, EROFS → mezo_extract_erofs_image,
    unknown → 7z fallback.

    Returns an extraction result entry dict.  Always includes a
    "converted_image" key (str path or None).
    Zero-byte or missing images are skipped with status='skipped'.
    """
    target = ws.partitions / partition_name
    log = ws.logs / f"partition_workspace_{partition_name}.log"

    if not img_path.is_file() or img_path.stat().st_size == 0:
        result = _entry(
            partition_name, img_path, "missing", "", "", target,
            "skipped", "image not found or zero-byte",
        )
        result["converted_image"] = None
        return result

    detection = mezo_detect_partition_image_format(img_path, toolchain)
    fmt = detection["format"]
    detail = detection["detail"]
    source = img_path
    converted_image: str | None = None

    if fmt == "android_sparse":
        conv = mezo_convert_sparse_image_if_needed(img_path, partition_name, ws, toolchain)
        if not conv["converted"]:
            result = _entry(
                partition_name, img_path, fmt,
                "simg2img", conv["simg2img_path"],
                target, "failed", conv["error"],
            )
            result["converted_image"] = None
            result["error_type"] = conv["error_type"]
            return result
        source = Path(conv["raw_path"])
        converted_image = conv["raw_path"]
        detection2 = mezo_detect_partition_image_format(source, toolchain)
        fmt = detection2["format"]
        detail = detection2["detail"]

    if fmt == "raw_ext4":
        ext4_res = mezo_extract_ext4_image(source, partition_name, ws, toolchain)
        status = ext4_res["status"]
        method = ext4_res["extractor_used"]
        tool = ext4_res["tool_path"]
        reason = ext4_res["error"]
    elif fmt == "raw_erofs":
        erofs_res = mezo_extract_erofs_image(source, partition_name, ws, toolchain)
        status = erofs_res["status"]
        method = erofs_res["extractor_used"]
        tool = erofs_res["tool_path"]
        reason = erofs_res["error"]
    else:
        status, reason, tool = _extract_7z(source, target, toolchain, log)
        method = "7z fallback"
        if status != "extracted" and not reason:
            reason = detail

    print(
        f"[PARTITION WORKSPACE] {partition_name}: "
        f"format={fmt} status={status}"
    )
    result = _entry(partition_name, img_path, fmt, method, tool, target, status, reason)
    result["converted_image"] = converted_image
    return result


def mezo_extract_partition_workspace(
    smart_unpack_result: dict,
    ws: Workspace,
) -> dict[str, Any]:
    """Extract all partition images from a smart_unpack result into ws.partitions.

    Handles the super.img route by attempting lpunpack via mezo_extract_super_to_images.
    If lpunpack is unavailable the result is reported as 'not_wired' without crashing.

    Returns a dict with per-partition entries, super-extraction metadata,
    zero_byte_ignored list, and converted_images map.
    """
    toolchain = resolve_toolchain(ws)
    route = smart_unpack_result.get("route", "unknown")
    super_img_path_str = smart_unpack_result.get("super_img")

    # ── zero-byte tracking ────────────────────────────────────────────────────
    zero_byte_ignored: list[str] = []
    raw_images_map: dict = smart_unpack_result.get("images") or {}
    for partition_name in _ALL_PARTITIONS:
        path_str = raw_images_map.get(partition_name)
        if path_str:
            p = Path(path_str)
            if p.exists() and p.stat().st_size == 0:
                zero_byte_ignored.append(partition_name)

    # ── super.img handling ────────────────────────────────────────────────────
    super_extraction: dict[str, Any] = {
        "status": "not_attempted",
        "reason": "not a super route",
    }

    is_super_route = route == "super"
    has_no_direct_images = not any(
        v
        for k, v in (smart_unpack_result.get("images") or {}).items()
        if k in _REQUIRED_PARTITIONS and v
    )

    if is_super_route or (super_img_path_str and has_no_direct_images):
        super_extraction = mezo_extract_super_to_images(ws, toolchain)

        if super_extraction.get("status") == "extracted":
            super_images_dir = Path(super_extraction.get("super_images_dir") or "")
            if super_images_dir.is_dir():
                refreshed: dict[str, str] = {}
                for img_file in super_images_dir.glob("*.img"):
                    base = img_file.stem.removesuffix("_a").removesuffix("_b")
                    refreshed[base] = str(img_file)
                merged = dict(raw_images_map)
                merged.update(refreshed)
                smart_unpack_result = dict(smart_unpack_result)
                smart_unpack_result["images"] = merged

    # ── image selection ───────────────────────────────────────────────────────
    selected = mezo_select_partition_images(smart_unpack_result)

    # ── per-partition extraction ──────────────────────────────────────────────
    partition_results: list[dict[str, Any]] = []
    skipped_optional: list[str] = []

    for partition_name in _ALL_PARTITIONS:
        img_str = selected.get(partition_name)

        if not img_str:
            if partition_name in _OPTIONAL_PARTITIONS:
                entry = _entry(
                    partition_name, None, "missing", "", "",
                    ws.partitions / partition_name,
                    "skipped", "optional partition not present",
                )
                skipped_optional.append(partition_name)
            else:
                entry = _entry(
                    partition_name, None, "missing", "", "",
                    ws.partitions / partition_name,
                    "skipped", "required image not found",
                )
            entry["converted_image"] = None
            partition_results.append(entry)
            continue

        entry = mezo_extract_partition_image(
            Path(img_str), partition_name, ws, toolchain
        )
        partition_results.append(entry)

    # ── converted_images map ──────────────────────────────────────────────────
    converted_images: dict[str, str] = {
        str(r["partition"]): r["converted_image"]
        for r in partition_results
        if r.get("converted_image")
    }

    # ── fs_config / file_contexts regeneration ────────────────────────────────
    fs_meta_results: list[dict] = []
    for entry in partition_results:
        if entry.get("status") != "extracted":
            continue
        part_name = str(entry.get("partition") or "")
        part_dir = ws.partitions / part_name
        if not part_dir.is_dir():
            part_dir = Path(str(entry.get("extracted_path") or ""))
        if part_dir.is_dir():
            fs_result = mezo_regenerate_fs_metadata(ws, part_name, part_dir)
            fs_meta_results.append(fs_result)

    return {
        "route": route,
        "super_extraction": super_extraction,
        "selected_images": selected,
        "partition_results": partition_results,
        "skipped_optional": skipped_optional,
        "zero_byte_ignored": zero_byte_ignored,
        "converted_images": converted_images,
        "fs_metadata": fs_meta_results,
    }


def mezo_validate_partition_workspace(
    extraction_result: dict,
) -> dict[str, Any]:
    """Validate that all required partitions were successfully extracted.

    Returns {"valid": bool, "missing_required": list, "errors": list}.
    Missing optional partitions are not counted as errors.
    """
    missing_required: list[str] = []
    errors: list[str] = []

    partition_results: list[dict] = extraction_result.get("partition_results") or []
    status_by_partition: dict[str, str] = {
        str(r.get("partition") or ""): str(r.get("status") or "skipped")
        for r in partition_results
    }

    for partition in sorted(_REQUIRED_PARTITIONS):
        status = status_by_partition.get(partition, "skipped")
        if status != "extracted":
            missing_required.append(partition)
            errors.append(
                f"Required partition '{partition}' not extracted (status: {status})"
            )

    super_extraction = extraction_result.get("super_extraction") or {}
    if super_extraction.get("status") == "not_wired":
        errors.append(
            "super extraction not wired: "
            + (super_extraction.get("reason") or "(unknown reason)")
        )

    return {
        "valid": len(missing_required) == 0,
        "missing_required": missing_required,
        "errors": errors,
    }


def deadzone_write_partition_workspace_report(
    ws: Workspace,
    result: dict,
) -> Path:
    """Write the partition workspace report and JSON metadata.

    Writes:
    - ws.reports/deadzone_partition_workspace_report.txt
    - ws.meta/partition_workspace.json

    Returns the report path.
    """
    report_path = ws.reports / "deadzone_partition_workspace_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    route = result.get("route", "unknown")
    status = result.get("status", "unknown")
    selected: dict = result.get("selected_images") or {}
    partition_results: list[dict] = result.get("partition_results") or []
    skipped_optional: list[str] = result.get("skipped_optional") or []
    missing_required: list[str] = result.get("missing_required") or []
    zero_byte_ignored: list[str] = result.get("zero_byte_ignored") or []
    converted_images: dict = result.get("converted_images") or {}
    super_extraction: dict = result.get("super_extraction") or {}
    fs_metadata: list[dict] = result.get("fs_metadata") or []

    fs_meta_by_partition: dict[str, dict] = {
        str(m.get("partition") or ""): m
        for m in fs_metadata
    }

    # ── per-partition detail lines ────────────────────────────────────────────
    part_lines: list[str] = []
    for entry in partition_results:
        part_name = str(entry.get("partition") or "")
        part_status = str(entry.get("status") or "skipped")
        part_fmt = str(entry.get("detected_format") or "(unknown)")
        part_method = str(entry.get("extraction_method") or "(none)")
        part_tool = str(entry.get("tool_path") or "(none)")
        part_dir = str(entry.get("extracted_path") or "(none)")
        part_reason = str(entry.get("failure_reason") or "(none)")
        part_converted = str(entry.get("converted_image") or "(none)")

        fs_meta = fs_meta_by_partition.get(part_name) or {}
        fs_cfg = (
            (fs_meta.get("fs_config") or {}).get("fs_config_path") or "(none)"
        )
        fc_path = (
            (fs_meta.get("file_contexts") or {}).get("file_contexts_path") or "(none)"
        )

        part_lines.extend([
            f"  partition        : {part_name}",
            f"  status           : {part_status}",
            f"  filesystem type  : {part_fmt}",
            f"  extractor used   : {part_method}",
            f"  tool             : {part_tool}",
            f"  output folder    : {part_dir}",
            f"  sparse converted : {part_converted}",
            f"  fs_config path   : {fs_cfg}",
            f"  file_contexts    : {fc_path}",
            f"  failure reason   : {part_reason}",
            "",
        ])

    extracted_count = sum(
        1 for r in partition_results if r.get("status") == "extracted"
    )
    selected_count = sum(1 for v in selected.values() if v)

    lines = [
        "DeadZone Partition Workspace Report",
        "===================================",
        f"smart_unpack route : {route}",
        f"status             : {status}",
        f"error              : {result.get('error') or '(none)'}",
        f"elapsed_seconds    : {result.get('elapsed_seconds', 0.0):.2f}",
        "",
        "super extraction:",
        f"  status  : {super_extraction.get('status') or '(none)'}",
        f"  reason  : {super_extraction.get('reason') or '(none)'}",
        f"  tool    : {super_extraction.get('tool') or '(none)'}",
        "",
        f"selected images ({selected_count}):",
        *[f"  {k}: {v or '(missing)'}" for k, v in selected.items()],
        "",
        f"extracted partitions ({extracted_count}):",
        *part_lines,
        f"skipped optional ({len(skipped_optional)}):",
        *([f"  {p}" for p in skipped_optional] or ["  (none)"]),
        "",
        f"missing required ({len(missing_required)}):",
        *([f"  {p}" for p in missing_required] or ["  (none)"]),
        "",
        f"zero-byte skipped ({len(zero_byte_ignored)}):",
        *([f"  {p}" for p in zero_byte_ignored] or ["  (none)"]),
        "",
        f"sparse converted ({len(converted_images)}):",
        *([f"  {k}: {v}" for k, v in converted_images.items()] or ["  (none)"]),
        "",
        "output partition folders:",
        *[
            f"  {r.get('partition')}: {r.get('extracted_path') or '(none)'}"
            for r in partition_results
            if r.get("status") == "extracted"
        ],
        "",
        "no mods executed   : True",
        "",
    ]

    report_path.write_text("\n".join(lines), encoding="utf-8")
    write_json(ws.meta / "partition_workspace.json", result)
    return report_path


def deadzone_partition_workspace_stage(
    ws: Workspace,
    smart_unpack_result: dict | None = None,
) -> dict[str, Any]:
    """Main partition workspace stage — canonical Phase 7/8 entry point.

    Reads smart_unpack result from ws.meta/smart_unpack.json when
    *smart_unpack_result* is not supplied.  Extracts partition images,
    regenerates fs_config/file_contexts metadata, validates required
    partitions, and writes the report + JSON.

    Safety guarantees:
    - Original ROM input is never deleted or modified.
    - All extraction is confined to ws.partitions/ (plus raw_images/ and super_images/).
    - No random temp folders are created outside the workspace.
    - No patch operations, UI changes, or HyperUR runtime are invoked.
    - Missing optional partitions are reported without raising.
    - Missing required partitions raise RuntimeError with a clear message
      after the report has been written.
    - No partition build tools, repack, or final super build is triggered.

    Writes:
    - ws.meta/partition_workspace.json
    - ws.reports/deadzone_partition_workspace_report.txt

    Returns the canonical result dict.
    """
    started = time.monotonic()

    if smart_unpack_result is None:
        smart_unpack_result = read_json(ws.meta / "smart_unpack.json", {})

    if not smart_unpack_result:
        raise RuntimeError(
            "partition_workspace: smart_unpack result not found — "
            "run smart_unpack first"
        )

    print(
        f"[PARTITION WORKSPACE] Route: "
        f"{smart_unpack_result.get('route', 'unknown')}"
    )

    extraction = mezo_extract_partition_workspace(smart_unpack_result, ws)
    validation = mezo_validate_partition_workspace(extraction)

    elapsed = time.monotonic() - started

    extracted_count = sum(
        1 for r in (extraction.get("partition_results") or [])
        if r.get("status") == "extracted"
    )

    if not validation["valid"]:
        status = "FAILED"
        error = "; ".join(validation["errors"])
    else:
        status = "OK" if extracted_count >= len(_REQUIRED_PARTITIONS) else "PARTIAL"
        error = ""

    # ── derive per-partition summary maps for JSON ───────────────────────────
    partition_results: list[dict] = extraction.get("partition_results") or []
    fs_metadata: list[dict] = extraction.get("fs_metadata") or []
    fs_meta_by_partition: dict[str, dict] = {
        str(m.get("partition") or ""): m for m in fs_metadata
    }

    image_format: dict[str, str] = {}
    extractor_used: dict[str, str] = {}
    extraction_status: dict[str, str] = {}
    fs_config_paths: dict[str, str] = {}
    file_contexts_paths: dict[str, str] = {}

    for r in partition_results:
        part = str(r.get("partition") or "")
        image_format[part] = str(r.get("detected_format") or "")
        extractor_used[part] = str(r.get("extraction_method") or "")
        extraction_status[part] = str(r.get("status") or "skipped")
        fs_m = fs_meta_by_partition.get(part) or {}
        fs_config_paths[part] = (
            (fs_m.get("fs_config") or {}).get("fs_config_path") or ""
        )
        file_contexts_paths[part] = (
            (fs_m.get("file_contexts") or {}).get("file_contexts_path") or ""
        )

    result: dict[str, Any] = {
        "route": extraction.get("route", "unknown"),
        "smart_unpack_route": extraction.get("route", "unknown"),
        "status": status,
        "error": error,
        "selected_images": extraction.get("selected_images") or {},
        "converted_images": extraction.get("converted_images") or {},
        "partition_results": partition_results,
        "extracted_partitions": [
            r.get("partition") for r in partition_results if r.get("status") == "extracted"
        ],
        "skipped_optional": extraction.get("skipped_optional") or [],
        "missing_required": validation.get("missing_required") or [],
        "zero_byte_ignored": extraction.get("zero_byte_ignored") or [],
        "image_format": image_format,
        "extractor_used": extractor_used,
        "extraction_status": extraction_status,
        "fs_config": fs_config_paths,
        "file_contexts": file_contexts_paths,
        "super_extraction": extraction.get("super_extraction") or {},
        "fs_metadata": fs_metadata,
        "validation": validation,
        "elapsed_seconds": elapsed,
        "no_mods_executed": True,
    }

    report_path = deadzone_write_partition_workspace_report(ws, result)
    result["report_path"] = str(report_path)

    # Update JSON with final report path
    write_json(ws.meta / "partition_workspace.json", result)

    print(f"[PARTITION WORKSPACE] Status: {status}")
    print(f"[PARTITION WORKSPACE] Report: {report_path}")

    if status == "FAILED":
        raise RuntimeError(error)

    return result
