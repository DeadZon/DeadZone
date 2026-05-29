from __future__ import annotations

from pathlib import Path
from typing import Any

from factory.core.workspace import Workspace


def summarize_error(error: object, stage: str = "") -> dict[str, str]:
    raw = str(error or "").strip()
    lower = raw.lower()
    clean_stage = stage or "unknown"

    if "pixeldrain" in lower or "upload" in lower:
        title = "PixelDrain upload failed"
        hint = "Check PIXELDRAIN_API_KEY and the network path to PixelDrain."
    elif "payload" in lower:
        title = "ROM payload unpack failed"
        hint = "Check that the ROM URL points to a complete OTA package."
    elif "super" in lower or "lpmake" in lower:
        title = "Super image build failed"
        hint = "Check super build and super profile reports."
    elif "missing" in lower or "not found" in lower or "no such file" in lower:
        title = "Required file is missing"
        hint = "Check the previous stage report and workspace logs."
    elif "download" in lower or "url" in lower:
        title = "ROM download failed"
        hint = "Check that the ROM URL is reachable and does not require hidden credentials."
    else:
        title = "Build failed"
        hint = "Check reports and logs artifacts for the failing stage."

    return {
        "title": title,
        "stage": clean_stage,
        "reason": raw[:800] if raw else "Unknown failure.",
        "hint": hint,
        "raw_error": raw[:1200],
    }


def write_error_summary(ctx: Any, ws: Workspace, error: object | None = None) -> Path:
    failed_stage = getattr(ctx, "failed_stage", "") or "unknown"
    summary = summarize_error(error if error is not None else getattr(ctx, "failure_error", ""), failed_stage)
    path = ws.reports / "error_summary.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "MEZO / DeadZone Error Summary",
        "=============================",
        f"status: {getattr(ctx, 'status', 'FAILED')}",
        f"failed stage: {summary['stage']}",
        f"title: {summary['title']}",
        f"reason: {summary['reason']}",
        f"hint: {summary['hint']}",
        f"final ZIP: {getattr(ctx, 'final_zip_path', None) or '(none)'}",
        "",
        "raw error:",
        summary["raw_error"] or "(none)",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path
