from __future__ import annotations

import json
import time
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from factory.core.workspace import Workspace
from factory.core.workspace import read_json


def _value(data: Any, key: str, default: str = "unknown") -> str:
    if data is None:
        return default
    if is_dataclass(data):
        data = asdict(data)
    if isinstance(data, dict):
        value = data.get(key)
        if value not in (None, "", "unknown"):
            return str(value)
    value = getattr(data, key, None)
    if value not in (None, "", "unknown"):
        return str(value)
    return default


def _stage_lines(stages: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    for stage in stages:
        lines.append(
            "{status}: {name} ({duration:.2f}s)".format(
                status=stage.get("status", "UNKNOWN"),
                name=stage.get("name", "unknown"),
                duration=float(stage.get("duration_seconds") or stage.get("duration") or 0.0),
            )
        )
        if stage.get("error"):
            lines.append(f"  error: {stage['error']}")
    return lines or ["(none)"]


def _safe_rom_source(value: str) -> str:
    raw = str(value or "").strip()
    parsed = urlparse(raw)
    if parsed.scheme and parsed.netloc:
        name = Path(parsed.path).name
        return f"{parsed.netloc}/{name}" if name else parsed.netloc
    return Path(raw).name or "(none)"


def _zip_size(final_zip: Any) -> str:
    if not final_zip:
        return "(none)"
    path = Path(final_zip)
    if not path.is_file():
        return "(missing)"
    return f"{path.stat().st_size / 1024 / 1024:.1f} MiB"


def write_production_reports(ctx: Any, ws: Workspace) -> dict[str, str]:
    reports_dir = ws.reports
    reports_dir.mkdir(parents=True, exist_ok=True)

    rom = getattr(ctx, "rom_metadata", None)
    device = getattr(ctx, "device_profile", {}) or {}
    final_zip = getattr(ctx, "final_zip_path", None)
    cleanup_status = getattr(ctx, "cleanup_status", "not run")
    upload_result = getattr(ctx, "upload_result", None)
    telegram_result = getattr(ctx, "telegram_result", None)
    status = getattr(ctx, "status", "UNKNOWN")
    size_policy = read_json(ws.meta / "size_policy.json", {})
    size_reduction = read_json(ws.meta / "size_reduction.json", {})
    failed_stage = getattr(ctx, "failed_stage", "") or "(none)"
    started_at = getattr(ctx, "started_at", time.time())
    completed_at = getattr(ctx, "completed_at", None)
    elapsed = (completed_at or time.time()) - started_at

    resolved_codename = (
        str(device.get("resolved_codename") or device.get("codename") or "")
        or _value(rom, "codename")
    )
    detected_codename = str(device.get("detected_codename") or "")
    if not detected_codename or detected_codename == "unknown":
        detected_codename = _value(rom, "codename")
    android = _value(rom, "android_version")
    build = _value(rom, "build")
    warnings = list(getattr(ctx, "warnings", []) or [])

    tracker = getattr(ctx, "tracker", None)
    stage_timeline = tracker.timeline() if tracker else getattr(ctx, "stages", [])
    if tracker:
        tracker.write()

    build_lines = [
        "MEZO / DeadZone Build Report",
        "============================",
        f"status: {status}",
        f"ROM source: {_safe_rom_source(getattr(ctx, 'rom_url', ''))}",
        f"selected codename: {getattr(ctx, 'selected_codename', '') or '(none)'}",
        f"detected codename: {detected_codename}",
        f"resolved codename: {resolved_codename}",
        f"Android version: {android}",
        f"build version: {build}",
        f"style: {getattr(ctx, 'style_label', '')}",
        f"soc: {getattr(ctx, 'soc', '')}",
        f"mode: {getattr(ctx, 'mode', '')}",
        f"workspace: {ws.root}",
        f"final ZIP path: {final_zip or '(none)'}",
        f"final ZIP name: {Path(final_zip).name if final_zip else '(none)'}",
        f"final ZIP size: {_zip_size(final_zip)}",
        f"final ZIP max allowed: {size_policy.get('final_zip_max_allowed') or size_policy.get('final_zip_max_bytes') or '(unknown)'}",
        f"size reduction status: {size_reduction.get('status') or 'not run'}",
        f"size reduction level: {size_reduction.get('level') or '(none)'}",
        f"size reduction removed bytes: {size_reduction.get('removed_bytes') or 0}",
        f"size policy reason: {size_policy.get('reason') or '(none)'}",
        f"upload requested: {getattr(upload_result, 'requested', False)}",
        f"upload provider: {getattr(upload_result, 'provider', 'PixelDrain')}",
        f"upload status: {getattr(upload_result, 'status', 'not requested')}",
        f"upload URL: {getattr(upload_result, 'url', '') or '(none)'}",
        f"upload failure reason: {getattr(upload_result, 'failure_reason', '') or '(none)'}",
        f"telegram requested: {getattr(telegram_result, 'requested', False)}",
        f"telegram status: {getattr(telegram_result, 'status', 'not requested')}",
        f"telegram message id: {getattr(telegram_result, 'message_id', None) or '(none)'}",
        f"telegram failure reason: {getattr(telegram_result, 'failure_reason', '') or '(none)'}",
        f"cleanup status: {cleanup_status}",
        f"started stage: {getattr(ctx, 'started_stage', '(none)')}",
        f"completed stage: {getattr(ctx, 'completed_stage', '(none)')}",
        f"failed stage: {failed_stage}",
        f"elapsed seconds: {elapsed:.2f}",
        "",
        "stages:",
        *_stage_lines(stage_timeline),
        "",
        "warnings:",
        *(warnings or ["(none)"]),
        "",
    ]

    orchestration_lines = [
        "MEZO / DeadZone Orchestration Report",
        "====================================",
        f"started stage: {getattr(ctx, 'started_stage', '(none)')}",
        f"completed stage: {getattr(ctx, 'completed_stage', '(none)')}",
        f"failed stage: {failed_stage}",
        f"ROM source: {_safe_rom_source(getattr(ctx, 'rom_url', ''))}",
        f"selected codename: {getattr(ctx, 'selected_codename', '') or '(none)'}",
        f"detected codename: {detected_codename}",
        f"resolved codename: {resolved_codename}",
        f"Android version: {android}",
        f"build version: {build}",
        f"style: {getattr(ctx, 'style_label', '')}",
        f"soc: {getattr(ctx, 'soc', '')}",
        f"final ZIP path: {final_zip or '(none)'}",
        f"final ZIP size: {_zip_size(final_zip)}",
        f"final ZIP max allowed: {size_policy.get('final_zip_max_allowed') or size_policy.get('final_zip_max_bytes') or '(unknown)'}",
        f"size reduction status: {size_reduction.get('status') or 'not run'}",
        f"size reduction level: {size_reduction.get('level') or '(none)'}",
        f"size reduction removed bytes: {size_reduction.get('removed_bytes') or 0}",
        f"size policy reason: {size_policy.get('reason') or '(none)'}",
        f"upload status: {getattr(upload_result, 'status', 'not requested')}",
        f"upload URL: {getattr(upload_result, 'url', '') or '(none)'}",
        f"telegram status: {getattr(telegram_result, 'status', 'not requested')}",
        f"telegram message id: {getattr(telegram_result, 'message_id', None) or '(none)'}",
        f"cleanup status: {cleanup_status}",
        "",
        "stage timeline:",
        *_stage_lines(stage_timeline),
        "",
    ]

    build_path = reports_dir / "build_report.txt"
    orchestration_path = reports_dir / "orchestration_report.txt"
    build_path.write_text("\n".join(build_lines), encoding="utf-8")
    orchestration_path.write_text("\n".join(orchestration_lines), encoding="utf-8")
    reports = {"build": str(build_path), "orchestration": str(orchestration_path)}
    stage_path = reports_dir / "stage_status.json"
    if stage_path.exists():
        reports["stage_status"] = str(stage_path)
    error_path = reports_dir / "error_summary.txt"
    if error_path.exists():
        reports["error_summary"] = str(error_path)
    toolchain_path = reports_dir / "toolchain_report.txt"
    if toolchain_path.exists():
        reports["toolchain"] = str(toolchain_path)
    size_reduction_path = reports_dir / "size_reduction_report.txt"
    if size_reduction_path.exists():
        reports["size_reduction"] = str(size_reduction_path)
    partition_size_path = reports_dir / "partition_size_report.txt"
    if partition_size_path.exists():
        reports["partition_size"] = str(partition_size_path)

    # --- Structured build summary ---
    summary_txt, summary_json = _write_build_summary(ctx, ws, reports_dir)
    reports["build_summary"] = str(summary_txt)
    reports["build_summary_json"] = str(summary_json)

    # --- Copy events log into reports dir ---
    events_src = ws.root.parent / "logs" / "events.ndjson"
    if events_src.is_file():
        events_dst = reports_dir / "live_events.ndjson"
        try:
            events_dst.write_bytes(events_src.read_bytes())
            reports["live_events"] = str(events_dst)
        except Exception:
            pass

    return reports


def _write_build_summary(ctx: Any, ws: Workspace, reports_dir: Path) -> tuple[Path, Path]:
    rom = getattr(ctx, "rom_metadata", None)
    device = getattr(ctx, "device_profile", {}) or {}
    final_zip = getattr(ctx, "final_zip_path", None)
    status = getattr(ctx, "status", "UNKNOWN")
    started_at = getattr(ctx, "started_at", time.time())
    completed_at = getattr(ctx, "completed_at", None)
    elapsed = (completed_at or time.time()) - started_at
    upload_result = getattr(ctx, "upload_result", None)
    telegram_result = getattr(ctx, "telegram_result", None)
    failed_stage = getattr(ctx, "failed_stage", "") or ""
    failure_error = getattr(ctx, "failure_error", "") or ""
    build_id = getattr(ctx, "build_id", "")

    resolved_codename = str(
        device.get("resolved_codename") or device.get("codename") or _value(rom, "codename")
    )

    # Classified error (if any)
    classified_error: dict[str, Any] = {}
    if status != "OK" and (failed_stage or failure_error):
        try:
            from factory.core.error_classifier import classify_error
            classified_error = classify_error(failure_error, failed_stage)
        except Exception:
            pass

    # Build state counters (if available)
    build_state_data = read_json(ws.root.parent / "state" / "build_state.json", {})
    counters = build_state_data.get("counters", {})

    summary: dict[str, Any] = {
        "build_id": build_id,
        "status": status,
        "soc": getattr(ctx, "soc", ""),
        "style": getattr(ctx, "style_label", ""),
        "device": resolved_codename,
        "android_version": _value(rom, "android_version"),
        "rom_version": _value(rom, "build"),
        "final_zip": str(final_zip) if final_zip else "",
        "final_zip_name": Path(final_zip).name if final_zip else "",
        "final_zip_size_bytes": final_zip.stat().st_size if final_zip and Path(final_zip).is_file() else 0,
        "upload_url": getattr(upload_result, "url", "") or "",
        "upload_status": getattr(upload_result, "status", "not requested"),
        "telegram_message_id": getattr(telegram_result, "message_id", None),
        "telegram_status": getattr(telegram_result, "status", "not requested"),
        "failed_stage": failed_stage,
        "elapsed_seconds": round(elapsed, 2),
        "started_at": build_state_data.get("started_at", ""),
        "finished_at": build_state_data.get("finished_at", ""),
        "app_counters": counters,
        "classified_error": classified_error,
        "warnings": list(getattr(ctx, "warnings", []) or []),
    }

    json_path = reports_dir / "build_summary.json"
    txt_path = reports_dir / "build_summary.txt"

    try:
        json_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    except Exception as exc:
        print(f"[REPORTS] Warning: failed to write build_summary.json: {exc}")

    txt_lines = [
        "MEZO / DeadZone Build Summary",
        "==============================",
        f"build_id         : {summary['build_id']}",
        f"status           : {summary['status']}",
        f"device           : {summary['device']}",
        f"android_version  : {summary['android_version']}",
        f"rom_version      : {summary['rom_version']}",
        f"soc              : {summary['soc']}",
        f"style            : {summary['style']}",
        f"elapsed_seconds  : {summary['elapsed_seconds']}",
        f"final_zip        : {summary['final_zip_name'] or '(none)'}",
        f"final_zip_size   : {summary['final_zip_size_bytes']} bytes",
        f"upload_url       : {summary['upload_url'] or '(none)'}",
        f"upload_status    : {summary['upload_status']}",
        f"telegram_status  : {summary['telegram_status']}",
        f"failed_stage     : {summary['failed_stage'] or '(none)'}",
        "",
        "app counters:",
        *[f"  {k}: {v}" for k, v in counters.items()],
    ]
    if classified_error:
        txt_lines += [
            "",
            "classified error:",
            f"  error_type   : {classified_error.get('error_type', '')}",
            f"  stage        : {classified_error.get('stage', '')}",
            f"  cause        : {classified_error.get('cause', '')}",
            f"  suggested_fix: {classified_error.get('suggested_fix', '')}",
        ]
    if summary["warnings"]:
        txt_lines += ["", "warnings:", *[f"  - {w}" for w in summary["warnings"]]]

    try:
        txt_path.write_text("\n".join(txt_lines) + "\n", encoding="utf-8")
    except Exception as exc:
        print(f"[REPORTS] Warning: failed to write build_summary.txt: {exc}")

    return txt_path, json_path
