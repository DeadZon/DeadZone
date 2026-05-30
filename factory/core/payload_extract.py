"""
DeadZone Phase 3 – Payload Extraction Stage.

Extracts default/base partition images from payload.bin into the DeadZone
workspace image directory (ws.images).

All public functions use mezo_* or deadzone_* prefix.
Private helpers use _ prefix.
This module never deletes or modifies the original ROM input or payload.bin.
All output is written exclusively to ws.images.
No patch operations, ROM modifications, or style changes are applied here.
"""
from __future__ import annotations

import subprocess
import time
from pathlib import Path
from typing import Any

from factory.adapters.payload import (
    _parse_manifest,
    _payload_manifest_bytes,
    _resolve_payload_tool,
)
from factory.core.workspace import Workspace, write_json


# Ordered list of partitions this stage targets by default.
DEFAULT_PARTITIONS: list[str] = [
    "system",
    "system_ext",
    "product",
    "vendor",
    "odm",
    "mi_ext",
    "system_dlkm",
    "vendor_dlkm",
]

# Partitions whose absence is a hard failure.
REQUIRED_PARTITIONS: frozenset[str] = frozenset({"system", "vendor", "product"})

# Partitions whose absence is non-fatal but reported.
OPTIONAL_PARTITIONS: frozenset[str] = frozenset({
    "system_ext", "odm", "mi_ext", "system_dlkm", "vendor_dlkm",
})


# ── Partition selection ───────────────────────────────────────────────────────

def mezo_select_default_payload_partitions(
    available_in_payload: list[str],
    requested: list[str],
) -> list[str]:
    """Return the subset of *requested* that exists in *available_in_payload*.

    Preserves *requested* order. Does not raise for absent partitions;
    callers must validate results with mezo_validate_extracted_payload_images.
    """
    payload_set = set(available_in_payload)
    return [p for p in requested if p in payload_set]


# ── Extraction ────────────────────────────────────────────────────────────────

def mezo_extract_payload_partitions(
    payload_bin: Path,
    out_dir: Path,
    partitions: list[str],
) -> dict[str, Any]:
    """Extract *partitions* from *payload_bin* into *out_dir* using payload-dumper-go.

    Uses the -partitions flag to limit extraction to only the requested set.
    *out_dir* is created if absent.

    Returns a dict with keys: tool, command, exit_code, error.
    Never deletes or modifies *payload_bin*.
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    tool = _resolve_payload_tool()
    if tool is None:
        return {
            "tool": None,
            "command": [],
            "exit_code": None,
            "error": (
                "payload-dumper-go is missing. "
                "Add it to tools/helper or install it in PATH."
            ),
        }

    command: list[str] = [
        str(tool),
        "-partitions", ",".join(partitions),
        "-o", str(out_dir),
        str(payload_bin),
    ]
    print(f"[PAYLOAD EXTRACT] Tool: {tool}")
    print(f"[PAYLOAD EXTRACT] Command: {' '.join(command)}")

    proc = subprocess.run(command, capture_output=True, text=True)
    exit_code = proc.returncode
    error = ""
    if exit_code != 0:
        error = proc.stderr.strip() or f"payload-dumper-go exited with code {exit_code}"

    return {
        "tool": str(tool),
        "command": command,
        "exit_code": exit_code,
        "error": error,
    }


# ── Validation ────────────────────────────────────────────────────────────────

def mezo_validate_extracted_payload_images(
    out_dir: Path,
    requested: list[str],
) -> dict[str, Any]:
    """Scan *out_dir* for extracted .img files and validate against *requested*.

    Also accepts slot-suffixed names (e.g. system_a.img) as matches.

    Returns:
        extracted_partitions  – sorted list of successfully extracted names
        missing_required      – required partitions that are absent
        missing_optional      – optional partitions that are absent
        extracted_images      – {partition_name: absolute_path_str}
        image_sizes           – {partition_name: size_bytes}
    """
    extracted_images: dict[str, str] = {}
    image_sizes: dict[str, int] = {}

    for name in requested:
        # Prefer slot-free name, fall back to _a slot
        candidate = out_dir / f"{name}.img"
        if not (candidate.is_file() and candidate.stat().st_size > 0):
            candidate = out_dir / f"{name}_a.img"
        if candidate.is_file() and candidate.stat().st_size > 0:
            extracted_images[name] = str(candidate)
            image_sizes[name] = candidate.stat().st_size

    extracted_set = set(extracted_images)
    missing = [p for p in requested if p not in extracted_set]
    missing_required = [p for p in missing if p in REQUIRED_PARTITIONS]
    missing_optional = [p for p in missing if p in OPTIONAL_PARTITIONS]

    return {
        "extracted_partitions": sorted(extracted_set),
        "missing_required": missing_required,
        "missing_optional": missing_optional,
        "extracted_images": extracted_images,
        "image_sizes": image_sizes,
    }


# ── Report ────────────────────────────────────────────────────────────────────

def deadzone_write_payload_extract_report(
    ws: Workspace,
    *,
    payload_path: str,
    requested_partitions: list[str],
    extracted_partitions: list[str],
    missing_optional: list[str],
    missing_required: list[str],
    extracted_images: dict[str, str],
    image_sizes: dict[str, int],
    extraction_status: str,
    elapsed_seconds: float | None = None,
    error: str = "",
) -> Path:
    """Write the payload extraction report to ws.reports/deadzone_payload_extract_report.txt.

    Includes all fields required by the Phase 3 spec.
    Returns the report path.
    """
    report_path = ws.reports / "deadzone_payload_extract_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    elapsed_str = f"{elapsed_seconds:.2f}s" if elapsed_seconds is not None else "(not measured)"

    image_lines: list[str] = []
    for name in sorted(extracted_images):
        size = image_sizes.get(name, 0)
        path = extracted_images[name]
        image_lines.append(f"  {name}: {path} ({size} bytes)")
    if not image_lines:
        image_lines = ["  (none)"]

    lines = [
        "DeadZone Payload Extract Report",
        "================================",
        f"payload.bin path    : {payload_path}",
        f"extraction status   : {extraction_status}",
        f"elapsed time        : {elapsed_str}",
        f"error               : {error or '(none)'}",
        "",
        f"requested partitions ({len(requested_partitions)}):",
        *[f"  {p}" for p in requested_partitions],
        "",
        f"extracted partitions ({len(extracted_partitions)}):",
        *([f"  {p}" for p in extracted_partitions] or ["  (none)"]),
        "",
        f"missing optional partitions ({len(missing_optional)}):",
        *([f"  {p}" for p in missing_optional] or ["  (none)"]),
        "",
        f"missing required partitions ({len(missing_required)}):",
        *([f"  {p}" for p in missing_required] or ["  (none)"]),
        "",
        "output image paths and sizes:",
        *image_lines,
        "",
    ]

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


# ── Stage orchestrator ────────────────────────────────────────────────────────

def deadzone_payload_extract_stage(
    ws: Workspace,
    payload_bin: Path | None = None,
    partitions: list[str] | None = None,
) -> dict[str, Any]:
    """Orchestrate the payload extraction stage (Phase 3).

    Locates payload.bin (from ws.extracted if not supplied), extracts the
    requested default partitions into ws.images, validates results, and
    writes both the extraction report and JSON metadata.

    Safety guarantees:
    - The original ROM input and payload.bin are never deleted or modified.
    - All output images are written exclusively to ws.images.
    - Missing optional partitions are reported but do not raise.
    - Missing required partitions raise RuntimeError with a clear message.
    - No patch operations or ROM modifications are applied.

    Writes:
    - ws.meta/payload_extract.json
    - ws.reports/deadzone_payload_extract_report.txt

    Returns the full extraction result dict.
    """
    requested: list[str] = list(partitions or DEFAULT_PARTITIONS)
    started = time.monotonic()

    # ── Locate payload.bin ────────────────────────────────────────────────────
    if payload_bin is None:
        candidates: list[Path] = (
            sorted(ws.extracted.rglob("payload.bin"))
            if ws.extracted.is_dir()
            else []
        )
        if not candidates:
            raise FileNotFoundError(
                f"payload.bin not found under {ws.extracted}. "
                "Run deadzone_rom_intake first."
            )
        payload_bin = candidates[0]

    if not payload_bin.is_file():
        raise FileNotFoundError(f"payload.bin not found: {payload_bin}")

    print(f"[PAYLOAD EXTRACT] payload.bin: {payload_bin}")
    print(f"[PAYLOAD EXTRACT] Requested: {', '.join(requested)}")

    # ── Determine available partitions from manifest ──────────────────────────
    try:
        manifest = _parse_manifest(_payload_manifest_bytes(payload_bin))
        available: list[str] = []
        for p in manifest.get("partitions") or []:
            raw = str(p.get("partition_name") or "")
            base = raw.removesuffix("_a").removesuffix("_b")
            if base:
                available.append(base)
    except Exception as exc:
        print(f"[PAYLOAD EXTRACT] Warning: manifest parse failed ({exc}); attempting all requested")
        available = list(requested)

    to_extract = mezo_select_default_payload_partitions(available, requested)
    if not to_extract:
        # Manifest empty or unreadable — attempt all requested anyway
        to_extract = list(requested)
    print(f"[PAYLOAD EXTRACT] Selected from manifest: {', '.join(to_extract)}")

    # ── Run extraction ────────────────────────────────────────────────────────
    extract_result = mezo_extract_payload_partitions(payload_bin, ws.images, to_extract)
    tool_error: str = extract_result.get("error") or ""

    # ── Validate output ───────────────────────────────────────────────────────
    validation = mezo_validate_extracted_payload_images(ws.images, requested)
    elapsed = time.monotonic() - started

    extracted_partitions: list[str] = validation["extracted_partitions"]
    missing_required: list[str] = validation["missing_required"]
    missing_optional: list[str] = validation["missing_optional"]
    extracted_images: dict[str, str] = validation["extracted_images"]
    image_sizes: dict[str, int] = validation["image_sizes"]

    for name in extracted_partitions:
        print(f"[PAYLOAD EXTRACT] OK: {name} ({image_sizes.get(name, 0)} bytes)")
    for name in missing_optional:
        print(f"[PAYLOAD EXTRACT] Optional missing (non-fatal): {name}")
    for name in missing_required:
        print(f"[PAYLOAD EXTRACT] REQUIRED MISSING (fatal): {name}")

    # Tool missing is always a hard failure regardless of partition state
    tool_missing = extract_result.get("tool") is None
    status = "FAILED" if (missing_required or tool_missing) else "OK"
    report_error = tool_error if tool_missing else (tool_error if tool_error else "")

    # ── Write report ──────────────────────────────────────────────────────────
    report_path = deadzone_write_payload_extract_report(
        ws,
        payload_path=str(payload_bin),
        requested_partitions=requested,
        extracted_partitions=extracted_partitions,
        missing_optional=missing_optional,
        missing_required=missing_required,
        extracted_images=extracted_images,
        image_sizes=image_sizes,
        extraction_status=status,
        elapsed_seconds=elapsed,
        error=report_error,
    )
    print(f"[PAYLOAD EXTRACT] Report: {report_path}")

    # ── Write JSON metadata ───────────────────────────────────────────────────
    meta: dict[str, Any] = {
        "payload_path": str(payload_bin),
        "requested_partitions": requested,
        "extracted_images": extracted_images,
        "missing_partitions": missing_required + missing_optional,
        "failed_partitions": missing_required,
        "status": status,
    }
    write_json(ws.meta / "payload_extract.json", meta)
    print(f"[PAYLOAD EXTRACT] Metadata: {ws.meta / 'payload_extract.json'}")

    result: dict[str, Any] = {
        "payload_path": str(payload_bin),
        "requested_partitions": requested,
        "extracted_partitions": extracted_partitions,
        "missing_optional": missing_optional,
        "missing_required": missing_required,
        "extracted_images": extracted_images,
        "image_sizes": image_sizes,
        "report_path": str(report_path),
        "meta_path": str(ws.meta / "payload_extract.json"),
        "status": status,
        "elapsed_seconds": elapsed,
    }

    # ── Raise on hard failures ────────────────────────────────────────────────
    if tool_missing:
        raise RuntimeError(tool_error)

    if missing_required:
        raise RuntimeError(
            f"Required partition(s) missing after extraction: "
            f"{', '.join(missing_required)}. "
            f"See {report_path}"
        )

    return result
