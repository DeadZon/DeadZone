"""Pipeline report writer — produces deadzone_patch_report.txt and pipeline_report.json."""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Optional


def write_pipeline_report(
    ctx: Any,
    output_dir: Path,
    telegram: Optional[dict] = None,
    build_id: Optional[str] = None,
    failure_summary: Optional[dict] = None,
) -> dict[str, str]:
    """Write both txt and json pipeline reports. Returns {txt, json} paths."""
    output_dir = Path(output_dir)
    reports_dir = output_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    txt_path  = reports_dir / "deadzone_patch_report.txt"
    json_path = reports_dir / "pipeline_report.json"

    data = _build_report_data(ctx, telegram=telegram, build_id=build_id, failure_summary=failure_summary)

    txt_path.write_text(_format_txt(data), encoding="utf-8")
    json_path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")

    return {"txt": str(txt_path), "json": str(json_path)}


def _build_report_data(
    ctx: Any,
    telegram: Optional[dict] = None,
    build_id: Optional[str] = None,
    failure_summary: Optional[dict] = None,
) -> dict:
    fs = failure_summary or {}
    return {
        "timestamp":          time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "build_id":           build_id or getattr(ctx, "build_id", None),
        "codename":           getattr(ctx, "codename", None),
        "soc":                getattr(ctx, "soc", None),
        "platform":           getattr(ctx, "platform", None),
        "edition":            getattr(ctx, "edition", None),
        "rom_url":            getattr(ctx, "rom_url", None),
        "android_version":    getattr(ctx, "android_version", None),
        "mi_incremental":     getattr(ctx, "mi_incremental", None),
        "super_size":         getattr(ctx, "super_size", 9126805504),
        "mode":               getattr(ctx, "mode", "dry_run"),
        "final_zip":          getattr(ctx, "final_zip", None),
        "pixeldrain_link":    getattr(ctx, "pixeldrain_link", None),
        "telegram_message_id": getattr(ctx, "telegram_message_id", None),
        "telegram":           telegram or {},
        "warnings":           getattr(ctx, "warnings", []),
        "errors":             getattr(ctx, "errors", []),
        "stage_reports":      getattr(ctx, "stage_reports", {}),
        "failed_stage":       fs.get("stage"),
        "failed_stage_human": fs.get("title"),
        "failure_reason":     fs.get("reason"),
        "failure_hint":       fs.get("hint"),
        "raw_error":          fs.get("raw_error"),
    }


def _format_txt(data: dict) -> str:
    tg = data.get("telegram") or {}
    lines = [
        "=" * 60,
        "  DeadZone Factory — Pipeline Report",
        "=" * 60,
        f"  Timestamp   : {data['timestamp']}",
        f"  Build ID    : {data.get('build_id') or 'n/a'}",
        f"  Codename    : {data['codename']}",
        f"  SoC         : {data['soc']}",
        f"  Platform    : {data['platform']}",
        f"  Edition     : {data['edition']}",
        f"  ROM URL     : {data['rom_url'] or '(local)'}",
        f"  Android     : {data['android_version']}",
        f"  Build       : {data['mi_incremental']}",
        f"  Super size  : {data['super_size']} bytes",
        f"  Mode        : {data['mode']}",
        "=" * 60,
        f"  Final ZIP   : {data['final_zip'] or 'n/a'}",
        f"  PixelDrain  : {data['pixeldrain_link'] or 'n/a'}",
        f"  Telegram ID : {data['telegram_message_id'] or 'n/a'}",
        "=" * 60,
        "  Telegram Notifications:",
        f"    notify_telegram    : {tg.get('notify_telegram', False)}",
        f"    message_id         : {tg.get('telegram_message_id', 'n/a')}",
        f"    chat_id (masked)   : {tg.get('telegram_chat_id', 'n/a')}",
        f"    first_update       : {tg.get('first_update_time', 'n/a')}",
        f"    last_update        : {tg.get('last_update_time', 'n/a')}",
        f"    final_status       : {tg.get('final_status', 'n/a')}",
        "=" * 60,
    ]
    if data.get("failed_stage"):
        lines += [
            "  Failure:",
            f"    Stage  : {data.get('failed_stage') or 'n/a'}",
            f"    Title  : {data.get('failed_stage_human') or 'n/a'}",
            f"    Reason : {data.get('failure_reason') or 'n/a'}",
            f"    Hint   : {data.get('failure_hint') or 'n/a'}",
            "=" * 60,
        ]
    if data["warnings"]:
        lines.append("  Warnings:")
        for w in data["warnings"]:
            lines.append(f"    - {w}")
    if data["errors"]:
        lines.append("  Errors:")
        for e in data["errors"]:
            lines.append(f"    ! {e}")
    lines.append("=" * 60)
    return "\n".join(lines) + "\n"
