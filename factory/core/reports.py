from __future__ import annotations

import time
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any

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
                duration=float(stage.get("duration_seconds") or 0.0),
            )
        )
        if stage.get("error"):
            lines.append(f"  error: {stage['error']}")
    return lines or ["(none)"]


def write_production_reports(ctx: Any, ws: Workspace) -> dict[str, str]:
    reports_dir = ws.reports
    reports_dir.mkdir(parents=True, exist_ok=True)

    rom = getattr(ctx, "rom_metadata", None)
    device = getattr(ctx, "device_profile", {}) or {}
    final_zip = getattr(ctx, "final_zip_path", None)
    cleanup_status = getattr(ctx, "cleanup_status", "not run")
    status = getattr(ctx, "status", "UNKNOWN")
    failed_stage = getattr(ctx, "failed_stage", "") or "(none)"
    started_at = getattr(ctx, "started_at", time.time())
    completed_at = getattr(ctx, "completed_at", None)
    elapsed = (completed_at or time.time()) - started_at

    codename = (
        str(device.get("resolved_codename") or device.get("codename") or "")
        or _value(rom, "codename")
    )
    android = _value(rom, "android_version")
    build = _value(rom, "build")

    build_lines = [
        "MEZO / DeadZone Build Report",
        "============================",
        f"status: {status}",
        f"ROM URL: {getattr(ctx, 'rom_url', '')}",
        f"detected codename: {codename}",
        f"Android version: {android}",
        f"build version: {build}",
        f"style: {getattr(ctx, 'style_label', '')}",
        f"soc: {getattr(ctx, 'soc', '')}",
        f"mode: {getattr(ctx, 'mode', '')}",
        f"workspace: {ws.root}",
        f"final ZIP path: {final_zip or '(none)'}",
        f"cleanup status: {cleanup_status}",
        f"started stage: {getattr(ctx, 'started_stage', '(none)')}",
        f"completed stage: {getattr(ctx, 'completed_stage', '(none)')}",
        f"failed stage: {failed_stage}",
        f"elapsed seconds: {elapsed:.2f}",
        "",
        "stages:",
        *_stage_lines(getattr(ctx, "stages", [])),
        "",
    ]

    orchestration_lines = [
        "MEZO / DeadZone Orchestration Report",
        "====================================",
        f"started stage: {getattr(ctx, 'started_stage', '(none)')}",
        f"completed stage: {getattr(ctx, 'completed_stage', '(none)')}",
        f"failed stage: {failed_stage}",
        f"ROM URL: {getattr(ctx, 'rom_url', '')}",
        f"detected codename: {codename}",
        f"Android version: {android}",
        f"build version: {build}",
        f"style: {getattr(ctx, 'style_label', '')}",
        f"soc: {getattr(ctx, 'soc', '')}",
        f"final ZIP path: {final_zip or '(none)'}",
        f"cleanup status: {cleanup_status}",
        "",
        "stage timeline:",
        *_stage_lines(getattr(ctx, "stages", [])),
        "",
    ]

    build_path = reports_dir / "build_report.txt"
    orchestration_path = reports_dir / "orchestration_report.txt"
    build_path.write_text("\n".join(build_lines), encoding="utf-8")
    orchestration_path.write_text("\n".join(orchestration_lines), encoding="utf-8")
    return {"build": str(build_path), "orchestration": str(orchestration_path)}
