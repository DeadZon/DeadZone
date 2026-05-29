from __future__ import annotations

import time
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from factory.core.workspace import Workspace


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
    return reports
