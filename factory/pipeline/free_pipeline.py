"""DeadZone Free edition pipeline.

Free = Smart Base Engine with edition="free", apply_mods=False.

Default behaviour (DEADZONE_LEGACY_ENGINE unset or "false"):
  Delegates to factory.engine.smart_base_engine.run_smart_base_engine().

Legacy fallback (DEADZONE_LEGACY_ENGINE=true):
  Falls back to the original run_legacy_engine() path so existing tests and
  CI jobs that depend on the old behaviour are not broken.

This module is responsible for:
  1. Running preflight cleanup before the build (smart engine handles this
     internally; the legacy path does it here).
  2. Delegating to the selected engine.
  3. Writing the Free-specific build report and engine report.
  4. Writing telegram_status.json for the workflow finalize step.
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any, Optional

_USE_SMART_ENGINE = os.environ.get("DEADZONE_LEGACY_ENGINE", "").lower() not in ("1", "true", "yes")


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
            status["previous_message_id"] = getattr(notifier, "previous_message_id", None)
            status["edit_failed"] = getattr(notifier, "edit_failed", False)
            status["replacement_message_created"] = getattr(notifier, "replacement_message_created", False)
            status["replacement_reason"] = getattr(notifier, "replacement_reason", None)
            status["last_api_error"] = getattr(notifier, "last_api_error", None)
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
        sr  = ctx.stage_reports.get("super_rebuild") or ctx.stage_reports.get("super_execute") or {}

        # Support both legacy DetectionResult (detected_device_codename) and
        # RomAnalysis (detected_codename) objects from the smart engine.
        def _det(attr: str, fallback: str = "N/A") -> str:
            if det is None:
                return fallback
            # try smart-engine RomAnalysis field names first, then legacy names
            for name in [attr, f"detected_{attr}", attr.replace("detected_", "")]:
                v = getattr(det, name, None)
                if v is not None:
                    return str(v)
            return fallback

        _detected_codename = (
            getattr(det, "detected_codename", None)
            or getattr(det, "detected_device_codename", None)
            or "N/A"
        ) if det else "N/A"
        _android = (
            getattr(det, "android_version", None)
            or getattr(det, "detected_android_version", None)
            or "N/A"
        ) if det else "N/A"
        _build = (
            getattr(det, "build_incremental", None)
            or getattr(det, "detected_hyperos_or_miui_version", None)
            or "N/A"
        ) if det else "N/A"
        _region = (
            getattr(det, "region", None)
            or getattr(det, "detected_region", None)
            or "N/A"
        ) if det else "N/A"
        _fmt = getattr(det, "rom_format", "N/A") if det else "N/A"

        lines = [
            "=" * 60,
            "  DeadZone Free Edition — Build Report",
            "=" * 60,
            f"  Device    : {ctx.codename}",
            f"  Edition   : Free",
            f"  Engine    : Smart Base Engine",
            f"  Mods      : Disabled",
            f"  ROM URL   : {ctx.rom_url or str(ctx.rom_path or '')}",
            f"  SoC       : {ctx.soc}",
            f"  Mode      : {ctx.mode}",
            "=" * 60,
            "  ROM Detection:",
            f"    Format    : {_fmt}",
            f"    Codename  : {_detected_codename}",
            f"    Android   : {_android}",
            f"    Build     : {_build}",
            f"    Version   : {_build}",
            f"    Region    : {_region}",
            f"    Metadata source : {getattr(ctx, 'metadata_source', '') or 'N/A'}",
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


def _write_smart_free_engine_report(
    reports_dir: Path,
    ctx: Any,
    result: dict,
) -> None:
    """Write free_engine_report.txt for the smart engine path (mirrors legacy format)."""
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "free_engine_report.txt"
    analysis = result.get("_analysis")
    unp = result.get("_unpack") or {}

    input_rom_path = getattr(ctx, "rom_path", None)
    input_rom_exists = input_rom_path is not None and Path(input_rom_path).exists()
    rom_url = getattr(ctx, "rom_url", "") or ""
    original_rom_url_filename = ""
    if rom_url:
        try:
            from urllib.parse import unquote, urlparse
            original_rom_url_filename = Path(unquote(urlparse(rom_url).path)).name
        except Exception:
            original_rom_url_filename = ""

    _fmt = getattr(analysis, "rom_format", "N/A") if analysis else "N/A"
    _strategy = result.get("_super_strategy", "unknown")

    lines = [
        "═══════════════════════════════════════════════════════",
        "  DeadZone Factory — Free Engine Report",
        "═══════════════════════════════════════════════════════",
        f"  Engine used           : smart_base_engine",
        f"  Edition               : {ctx.edition}",
        f"  apply_mods            : False",
        f"  Input ROM path        : {input_rom_path or '(none)'}",
        f"  local_rom_name        : {Path(input_rom_path).name if input_rom_path else ''}",
        f"  original_rom_url_filename: {original_rom_url_filename}",
        f"  metadata_source       : {getattr(ctx, 'metadata_source', '') or 'N/A'}",
        f"  Input ROM exists      : {input_rom_exists}",
        f"  ROM format            : {_fmt}",
        f"  Super strategy        : {_strategy}",
        f"  Payload dump method   : {unp.get('payload_dump_tool', 'N/A')}",
        "",
        "  Skipped patch stages:",
        "    - APK patching        (skipped)",
        "    - JAR patching        (skipped)",
        "    - smali patching      (skipped)",
        "    - overlay mods        (skipped)",
        "    - debloat             (skipped)",
        "    - build.prop tweaks   (skipped)",
        "    - Legend/Gaming/EPIC  (skipped)",
        "",
        f"  Final ZIP             : {ctx.final_zip or 'N/A'}",
        f"  PixelDrain link       : {ctx.pixeldrain_link or 'N/A'}",
    ]
    if ctx.errors:
        lines += ["", "  Errors:"]
        for e in ctx.errors:
            lines.append(f"    ! {e}")
    lines.append("═══════════════════════════════════════════════════════")
    try:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except Exception as exc:
        print(f"[free_pipeline] Warning: could not write free_engine_report.txt: {exc}")


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
    """Free edition pipeline — delegates to Smart Base Engine (default) or legacy engine."""
    output_dir = Path(output_dir)
    reports_dir = output_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    # ── Smart Base Engine path (default) ──────────────────────────────────────
    if _USE_SMART_ENGINE:
        from factory.engine.smart_base_engine import run_smart_base_engine

        result = run_smart_base_engine(
            context=ctx,
            edition="free",
            apply_mods=False,
            notifier=notifier,
            template_zip=template_zip,
            pipeline_start=pipeline_start,
        )
        # Write Free-specific surface reports from smart engine result
        _write_free_build_report(
            reports_dir=reports_dir,
            ctx=ctx,
            detection=result.get("_analysis"),
            collect=None,
            super_input=result.get("_super_input"),
            assemble=result.get("_assemble"),
            final_zip=ctx.final_zip,
            unpack=result.get("_unpack"),
            super_strategy=result.get("_super_strategy", "unknown"),
            original_super_existed=bool(
                (result.get("stage_reports") or {})
                .get("super_strategy", {})
                .get("original_super_exists")
            ),
            result=result,
        )
        # Write free_engine_report.txt (compat: tests expect this file)
        _write_smart_free_engine_report(reports_dir, ctx, result)
        _write_telegram_status(notifier, ctx.notify_telegram, soc or "", source, output_dir)
        # Strip internal _* fields before returning
        return {k: v for k, v in result.items() if not k.startswith("_")}

    # ── Legacy engine fallback (DEADZONE_LEGACY_ENGINE=true) ─────────────────
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

    return {k: v for k, v in result.items() if not k.startswith("_")}
