from __future__ import annotations

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


def _size(path: Path | None) -> str:
    if not path or not path.is_file():
        return "(none)"
    size = path.stat().st_size
    if size >= 1024 * 1024 * 1024:
        return f"{size / 1024 / 1024 / 1024:.2f} GiB"
    return f"{size / 1024 / 1024:.1f} MiB"


def write_github_summary(ctx: Any, ws: Workspace) -> Path:
    rom = getattr(ctx, "rom_metadata", None)
    device = getattr(ctx, "device_profile", {}) or {}
    final_zip = getattr(ctx, "final_zip_path", None)
    final_path = Path(final_zip) if final_zip else None
    upload = getattr(ctx, "upload_result", None)
    telegram = getattr(ctx, "telegram_result", None)
    detected = str(device.get("detected_codename") or "") or _value(rom, "codename")
    selected = getattr(ctx, "selected_codename", "") or "(none)"
    resolved = str(device.get("resolved_codename") or device.get("codename") or selected)

    lines = [
        "## DeadZone Build Summary",
        "",
        f"- status: {getattr(ctx, 'status', 'UNKNOWN')}",
        f"- style: {getattr(ctx, 'style_label', '')}",
        f"- selected device: {selected}",
        f"- detected device: {detected}",
        f"- resolved device: {resolved}",
        f"- Android version: {_value(rom, 'android_version')}",
        f"- build version: {_value(rom, 'build')}",
        f"- final ZIP name: {final_path.name if final_path else '(none)'}",
        f"- final ZIP size: {_size(final_path)}",
        f"- PixelDrain link: {getattr(upload, 'url', '') or '(none)'}",
        f"- Telegram status: {getattr(telegram, 'status', 'not requested')}",
        f"- failed stage: {getattr(ctx, 'failed_stage', '') or '(none)'}",
        "",
        "Reports and logs are attached as workflow artifacts: `deadzone-reports`, `deadzone-logs`, `deadzone-sidecars`, and `deadzone-final-info`.",
        "",
    ]
    path = ws.reports / "github_summary.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return path
