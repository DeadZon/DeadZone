"""
DeadZone Phase 7 – Partition Workspace Stage.

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
  super        – lpunpack attempted; reported cleanly if unavailable
  new_dat      – images collected via new_dat adapter

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
# Reuse existing extraction helpers rather than rewriting them.
# These are internal to image_extractor but the spec requires us to
# preserve the same extraction logic rather than duplicate it.
from factory.core.image_extractor import (  # noqa: PLC2701
    _detect_format,
    _entry,
    _extract_7z,
    _extract_erofs,
    _extract_ext4,
    _extract_super_if_needed,
    _sparse_to_raw,
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

    Returns an extraction result entry dict (same schema as image_extractor).
    Zero-byte or missing images are skipped with status 'skipped'.
    """
    target = ws.partitions / partition_name
    log = ws.logs / f"partition_workspace_{partition_name}.log"
    cap_log: list[str] = []

    if not img_path.is_file() or img_path.stat().st_size == 0:
        return _entry(
            partition_name, img_path, "missing", "", "", target,
            "skipped", "image not found or zero-byte",
        )

    fmt, detail = _detect_format(img_path, toolchain.path("file"))
    source = img_path

    if fmt == "android_sparse":
        simg2img = toolchain.path("simg2img")
        if not simg2img:
            return _entry(
                partition_name, img_path, fmt, "simg2img", "", target,
                "failed", "simg2img not available",
            )
        raw_img, error = _sparse_to_raw(img_path, partition_name, ws, simg2img, log)
        if not raw_img:
            return _entry(
                partition_name, img_path, fmt, "simg2img", str(simg2img), target,
                "failed", error,
            )
        source = raw_img
        fmt, detail = _detect_format(source, toolchain.path("file"))

    if fmt == "raw_ext4":
        status, method_or_reason, tool = _extract_ext4(source, target, toolchain, log)
        method = method_or_reason if status == "extracted" else "ext4 extraction"
        reason = "" if status == "extracted" else method_or_reason
    elif fmt == "raw_erofs":
        status, method_or_reason, tool = _extract_erofs(
            source, target, toolchain, log, cap_log
        )
        method = (
            method_or_reason
            if status in ("extracted", "listed_only")
            else "erofs extraction"
        )
        reason = "" if status == "extracted" else method_or_reason
    else:
        status, reason, tool = _extract_7z(source, target, toolchain, log)
        method = "7z fallback"
        if status != "extracted" and not reason:
            reason = detail

    print(
        f"[PARTITION WORKSPACE] {partition_name}: "
        f"format={fmt} status={status}"
    )
    return _entry(partition_name, img_path, fmt, method, tool, target, status, reason)


def mezo_extract_partition_workspace(
    smart_unpack_result: dict,
    ws: Workspace,
) -> dict[str, Any]:
    """Extract all partition images from a smart_unpack result into ws.partitions.

    Handles the super.img route by attempting lpunpack first.
    If lpunpack is unavailable the result is reported as 'not_wired' and
    this function does not crash.

    Returns a dict with per-partition entries and super-extraction metadata.
    """
    toolchain = resolve_toolchain(ws)
    route = smart_unpack_result.get("route", "unknown")
    super_img_path_str = smart_unpack_result.get("super_img")

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
        if super_img_path_str and Path(super_img_path_str).is_file():
            # Pass empty dict so _extract_super_if_needed checks ws.images/super.img
            super_extraction = _extract_super_if_needed(ws, {}, toolchain)

            if super_extraction.get("status") == "extracted":
                # Refresh image map after lpunpack populated ws.images
                from factory.core.smart_unpack import mezo_collect_unpacked_images
                refreshed = mezo_collect_unpacked_images(ws.images)
                smart_unpack_result = dict(smart_unpack_result)
                smart_unpack_result["images"] = refreshed

            elif "lpunpack not available" in (super_extraction.get("reason") or ""):
                super_extraction = {
                    "status": "not_wired",
                    "reason": "super extraction not wired: lpunpack not available",
                }
            elif super_extraction.get("status") == "skipped":
                super_extraction = {
                    "status": "not_wired",
                    "reason": (
                        "super extraction not wired: "
                        + (super_extraction.get("reason") or "unknown reason")
                    ),
                }
        else:
            super_extraction = {
                "status": "not_wired",
                "reason": "super extraction not wired: super.img not found in workspace",
            }

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
            partition_results.append(entry)
            continue

        entry = mezo_extract_partition_image(
            Path(img_str), partition_name, ws, toolchain
        )
        partition_results.append(entry)

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
    """Main partition workspace stage — canonical Phase 7 entry point.

    Reads smart_unpack result from ws.meta/smart_unpack.json when
    *smart_unpack_result* is not supplied.  Extracts partition images,
    regenerates fs_config/file_contexts metadata, validates required
    partitions, and writes the report + JSON.

    Safety guarantees:
    - Original ROM input is never deleted or modified.
    - All extraction is confined to ws.partitions/.
    - No random temp folders are created outside the workspace.
    - No patch operations, UI changes, or HyperUR runtime are invoked.
    - Missing optional partitions are reported without raising.
    - Missing required partitions raise RuntimeError with a clear message
      after the report has been written.

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

    result: dict[str, Any] = {
        "route": extraction.get("route", "unknown"),
        "status": status,
        "error": error,
        "selected_images": extraction.get("selected_images") or {},
        "partition_results": extraction.get("partition_results") or [],
        "skipped_optional": extraction.get("skipped_optional") or [],
        "missing_required": validation.get("missing_required") or [],
        "super_extraction": extraction.get("super_extraction") or {},
        "fs_metadata": extraction.get("fs_metadata") or [],
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
