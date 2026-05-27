"""DeadZone Free edition pipeline.

Free = legacy/legend engine + apply_mods=False + preflight cleanup.

All unpack / super / repack / ZIP logic lives in legacy_engine_runner.
This module is only responsible for:
  1. Running preflight cleanup before the build.
  2. Delegating to run_legacy_engine() with edition="free", apply_mods=False.
  3. Writing the Free-specific build report and engine report.
  4. Writing telegram_status.json for the workflow finalize step.
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any, Optional


# ── Report helpers ────────────────────────────────────────────────────────────

def _write_telegram_status(
    notifier: Optional[Any],
    enabled: bool,
    soc: str,
    source: str,
    output_dir: Path,
) -> None:
    soc_norm = (soc or "").lower()
    if soc_norm == "mtk":
        token_present   = bool(os.environ.get("TELEGRAM_MTK_BOT_TOKEN") or os.environ.get("TELEGRAM_BOT_TOKEN"))
        chat_id_present = bool(os.environ.get("TELEGRAM_MTK_CHAT_ID") or os.environ.get("TELEGRAM_CHAT_ID"))
    elif soc_norm == "snapdragon":
        token_present   = bool(os.environ.get("TELEGRAM_SNAPDRAGON_BOT_TOKEN") or os.environ.get("TELEGRAM_BOT_TOKEN"))
        chat_id_present = bool(os.environ.get("TELEGRAM_SNAPDRAGON_CHAT_ID") or os.environ.get("TELEGRAM_CHAT_ID"))
    else:
        token_present   = bool(os.environ.get("TELEGRAM_BOT_TOKEN"))
        chat_id_present = bool(os.environ.get("TELEGRAM_CHAT_ID"))

    status: dict = {
        "enabled":           enabled,
        "soc":               soc_norm or "unknown",
        "source":            source,
        "token_present":     token_present,
        "chat_id_present":   chat_id_present,
        "message_id":        None,
        "first_update_time": None,
        "last_update_time":  None,
        "final_status":      None,
        "last_error":        None,
    }

    if notifier is not None:
        try:
            status["message_id"]        = notifier.message_id
            status["first_update_time"] = notifier.first_update_time
            status["last_update_time"]  = notifier.last_update_time
            status["final_status"]      = notifier.final_status
            last_err = getattr(notifier, "last_error", None)
            status["last_error"] = str(last_err)[:500] if last_err else None
            status["current_stage"]     = getattr(notifier, "current_stage", None)
            status["failure_stage"]     = getattr(notifier, "failure_stage", None)
            status["failure_reason"]    = getattr(notifier, "failure_reason", None)
            status["failure_hint"]      = getattr(notifier, "failure_hint", None)
            status["raw_error"]         = getattr(notifier, "raw_error", None)
        except Exception:
            pass

    try:
        reports_dir = output_dir / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)
        (reports_dir / "telegram_status.json").write_text(
            json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    except Exception as exc:
        print(f"[free_pipeline] Warning: could not write telegram_status.json: {exc}")


def _write_free_build_report(
    reports_dir: Path,
    ctx: Any,
    detection: Any,
    collect: Optional[dict],
    super_input: Optional[dict],
    assemble: Optional[dict],
    final_zip: Optional[str],
    unpack: Optional[dict] = None,
    super_strategy: str = "unknown",
    original_super_existed: bool = False,
    result: Optional[dict] = None,
) -> None:
    try:
        det = detection
        col = collect or {}
        si  = super_input or {}
        asm = assemble or {}
        unp = unpack or {}
        sr  = ctx.stage_reports.get("super_rebuild") or {}

        lines = [
            "=" * 60,
            "  DeadZone Free Edition — Build Report",
            "=" * 60,
            f"  Device    : {ctx.codename}",
            f"  Edition   : Free",
            f"  Engine    : Legacy/Legend engine",
            f"  Mods      : Disabled",
            f"  ROM URL   : {ctx.rom_url or str(ctx.rom_path or '')}",
            f"  SoC       : {ctx.soc}",
            f"  Mode      : {ctx.mode}",
            "=" * 60,
            "  ROM Detection:",
            f"    Format    : {det.rom_format if det else 'N/A'}",
            f"    Codename  : {det.detected_device_codename if det else 'N/A'}",
            f"    Android   : {det.detected_android_version if det else 'N/A'}",
            f"    Version   : {det.detected_hyperos_or_miui_version if det else 'N/A'}",
            f"    Region    : {det.detected_region if det else 'N/A'}",
        ]

        # Payload dump section
        if unp.get("payload_dump_status") is not None:
            dump_status = unp.get("payload_dump_status", "N/A")
            dump_count  = len(unp.get("payload_dump_images") or [])
            dump_tool   = unp.get("payload_dump_tool", "unknown")
            dump_errs   = unp.get("payload_dump_errors") or []
            lines += [
                "=" * 60,
                "  Payload Dump:",
                f"    Status        : {dump_status}",
                f"    Tool used     : {dump_tool}",
                f"    Dumped images : {dump_count}",
            ]
            if dump_errs:
                lines.append(f"    Error         : {dump_errs[0]}")

        lines += [
            "=" * 60,
            "  Super Handling:",
            f"    Strategy              : {super_strategy}",
            f"    Original super exists : {original_super_existed}",
            f"    Preserved orig super  : {sr.get('strategy') == 'preserve_original_super'}",
            f"    Rebuilt super         : {sr.get('strategy') == 'rebuild_with_lpmake'}",
            f"    lpmake executed       : {bool(sr.get('lpmake_executed'))}",
            "=" * 60,
            "  Image Collection:",
            f"    Normal images    : {len(col.get('standalone_images', {}))}",
            f"    Dynamic parts    : {len(si.get('found_dynamic_partitions', []))}",
        ]

        final_imgs = asm.get("final_manifest") or asm.get("final_images") or []
        if final_imgs:
            lines.append("  Final Images:")
            for img in sorted(final_imgs):
                lines.append(f"    - {img}")
        else:
            lines.append("  Final Images : (none / dry_run)")

        lines += [
            "=" * 60,
            "  Skipped Mods:",
            "    - Legend mods         (skipped)",
            "    - Gaming mods         (skipped)",
            "    - EPIC mods           (skipped)",
            "    - APK/JAR patching    (skipped)",
            "    - smali patching      (skipped)",
            "    - debloat             (skipped)",
            "=" * 60,
            f"  Final ZIP : {final_zip or 'N/A'}",
            f"  Cleanup   : {'DONE' if ctx.stage_reports.get('cleanup') else 'PENDING'}",
        ]

        # Include failure summary if available
        failure_summary = result.get("_failure_summary") if result else None
        if failure_summary:
            lines += [
                "=" * 60,
                "  Failure:",
                f"    Stage  : {failure_summary.get('stage', 'unknown')}",
                f"    Reason : {failure_summary.get('reason', '')}",
                f"    Hint   : {failure_summary.get('hint', '')}",
            ]

        if ctx.errors:
            lines.append("  Errors:")
            for e in ctx.errors:
                lines.append(f"    ! {e}")
        if ctx.warnings:
            lines.append("  Warnings:")
            for w in ctx.warnings:
                lines.append(f"    - {w}")

        lines.append("=" * 60)

        reports_dir.mkdir(parents=True, exist_ok=True)
        (reports_dir / "free_build_report.txt").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )
    except Exception as exc:
        print(f"[free_pipeline] Warning: could not write free_build_report.txt: {exc}")


# ── Main pipeline ─────────────────────────────────────────────────────────────

def run_free_pipeline(
    ctx: Any,
    notifier: Optional[Any],
    soc: str,
    source: str,
    output_dir: Path,
    template_zip: Optional[Path],
    pipeline_start: float,
) -> dict:
    """Free edition pipeline — delegates to legacy_engine_runner with apply_mods=False."""
    output_dir = Path(output_dir)
    reports_dir = output_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    # ── Preflight cleanup ────────────────────────────────────────────────────
    # Pass the active ROM path so preflight_cleanup does NOT delete _input_roms/
    # when the workflow has already downloaded the ROM there.  The cleanup must
    # always run before detect_rom; preserving the ROM directory is the safe way
    # to achieve that without changing the download-then-pipeline workflow order.
    preflight_status = "SKIPPED"
    try:
        from factory.cleanup.preflight_cleanup import preflight_cleanup
        _preserve = [ctx.rom_path] if getattr(ctx, "rom_path", None) else None
        preflight_result = preflight_cleanup(output_dir, preserve_paths=_preserve)
        preflight_status = preflight_result.get("status", "APPLIED")
        _phase = preflight_result.get("cleanup_phase", "unknown")
        print(f"[free_pipeline] preflight_cleanup: {preflight_status} (phase={_phase})")
    except Exception as exc:
        print(f"[free_pipeline] Warning: preflight_cleanup failed (non-fatal): {exc}")

    # ── Delegate to shared legacy engine ─────────────────────────────────────
    from factory.pipeline.legacy_engine_runner import run_legacy_engine, _write_free_engine_report

    result = run_legacy_engine(
        context=ctx,
        notifier=notifier,
        output_dir=output_dir,
        template_zip=template_zip,
        pipeline_start=pipeline_start,
        edition="free",
        apply_mods=False,
        fast_mode=True,
        use_universal_detector=True,
    )
    result["_preflight_cleanup_status"] = preflight_status

    # ── Write Free-specific reports ───────────────────────────────────────────
    _write_free_build_report(
        reports_dir=reports_dir,
        ctx=ctx,
        detection=result.get("_detection"),
        collect=result.get("_collect"),
        super_input=result.get("_super_input"),
        assemble=result.get("_assemble"),
        final_zip=ctx.final_zip,
        unpack=result.get("_unpack"),
        super_strategy=result.get("_super_strategy", "unknown"),
        original_super_existed=bool(result.get("_original_super_existed")),
        result=result,
    )
    _write_free_engine_report(reports_dir, ctx, result)
    _write_telegram_status(notifier, ctx.notify_telegram, soc or "", source, output_dir)

    # Strip internal _* fields before returning
    public = {k: v for k, v in result.items() if not k.startswith("_")}
    return public
