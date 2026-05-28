"""Smart Base Engine — single shared build engine for all ROMs, all devices, all editions.

run_smart_base_engine() is the one canonical build function.  Every edition
(Free / Legend / Gaming / EPIC), every SoC (MTK / Snapdragon), every ROM
format, and every device goes through this single pipeline.

  Device differences   → registry metadata (factory_devices.json)
  ROM format differences → format adapters (rom_unpacker)
  Edition differences  → mod layers only (apply_mods flag)

No production code may branch on a device codename.  All device-specific
behaviour is driven by registry metadata or ROM analysis results.

Pipeline stages
---------------
 1. Preflight cleanup
 2. Analyze ROM (format + metadata via universal_rom_intake)
 3. Validate codename (part of analyze_rom; errors surface here)
 4. Unpack ROM (universal_unpacker.unpack_with_analysis)
 5. Build source image manifest (source_image_manifest)
 6. Collect super inputs (super_input_collector)
 7. Select super strategy (universal_super_engine.select_super_strategy)
 8. Execute super strategy (universal_super_engine.execute_super_strategy)
 9. Assemble final images (final_image_assembler)
10. Apply edition mods — only when apply_mods=True
11. Package final ZIP (final_zip_legacy) — includes template patching + flash commands
12. Upload PixelDrain — if upload_pixeldrain=True
13. Cleanup workspace
14. Write runtime guard report
15. Finalize Telegram + write telegram_status.json

Reports written
---------------
output/reports/rom_analysis_report.txt
output/reports/codename_validation_report.txt
output/reports/source_image_manifest.txt
output/reports/source_image_manifest.json
output/reports/super_metadata_report.txt
output/reports/super_rebuild_report.txt       (written by super_rebuilder)
output/reports/dynamic_flash_script_report.txt  (written by final_zip_legacy)
output/reports/template_packaging_report.txt    (written by final_zip_legacy)
output/reports/final_zip_report.txt
output/reports/runtime_guard_report.txt
output/reports/telegram_status.json

PixelDrain status logic
-----------------------
ZIP created + upload_pixeldrain=False  → final_status = APPLIED
ZIP created + upload succeeds          → final_status = APPLIED
ZIP created + upload fails             → final_status = ZIP_CREATED_UPLOAD_FAILED
    failed_stage = UPLOADING_PIXELDRAIN
    ZIP is NOT deleted after a failed upload
    Telegram: "Build finished, upload failed"
"""
from __future__ import annotations

import importlib
import json
import os
import threading
import time
from pathlib import Path
from typing import Any, Optional

_REPO_ROOT = Path(__file__).resolve().parents[2]


# ── Stage timeout configuration (minutes) ────────────────────────────────────

STAGE_TIMEOUTS_MINUTES: dict[str, int] = {
    "preflight":         2,
    "analyze_rom":       5,
    "unpack_rom":        60,
    "source_manifest":   10,
    "super_inputs":             15,
    "listmezo_free_normalize":  15,
    "super_strategy":           1,
    "super_execute":     60,
    "assemble_images":   15,
    "apply_mods":        30,
    "final_zip":         45,
    "pixeldrain_upload": 45,
    "cleanup":           10,
}

_HEARTBEAT_STAGES: frozenset[str] = frozenset({
    "unpack_rom",
    "super_execute",
    "apply_mods",
    "final_zip",
    "pixeldrain_upload",
})


# ── Internal helpers ──────────────────────────────────────────────────────────

def _import(module: str) -> Any:
    try:
        return importlib.import_module(module)
    except ImportError:
        return None


class _Heartbeat:
    """Daemon thread that logs a heartbeat line every `interval` seconds."""

    def __init__(self, stage: str, interval: int = 60, notifier: Optional[Any] = None):
        self._stage = stage
        self._interval = interval
        self._notifier = notifier
        self._stop = threading.Event()
        self._t0 = time.monotonic()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def __enter__(self) -> "_Heartbeat":
        self._thread.start()
        return self

    def __exit__(self, *_: Any) -> None:
        self._stop.set()
        self._thread.join(timeout=2)

    def _run(self) -> None:
        tick = 0
        while not self._stop.wait(self._interval):
            tick += 1
            elapsed = int(time.monotonic() - self._t0)
            print(
                f"[heartbeat] stage={self._stage} elapsed={elapsed}s tick={tick}",
                flush=True,
            )
            if self._notifier is not None:
                try:
                    self._notifier.heartbeat()
                except Exception:
                    pass


class _NullCtx:
    def __enter__(self) -> "_NullCtx":
        return self
    def __exit__(self, *_: Any) -> None:
        pass


def _write_runtime_guard_report(
    reports_dir: Path,
    codename: str,
    edition: str,
    stage_durations: dict[str, float],
    timed_out_stage: Optional[str],
    input_rom_path: Optional[Path] = None,
    input_rom_exists_before_detect: Optional[bool] = None,
    cleanup_ran_before_download: Optional[bool] = True,
) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "runtime_guard_report.txt"
    longest = max(stage_durations, key=stage_durations.get) if stage_durations else "(none)"
    longest_dur = stage_durations.get(longest, 0.0)

    def _bool(v: Optional[bool]) -> str:
        return "true" if v is True else ("false" if v is False else "N/A")

    lines = [
        "═══════════════════════════════════════════════════════",
        "  DeadZone Factory — Runtime Guard Report",
        "═══════════════════════════════════════════════════════",
        f"  Device (codename)     : {codename}",
        f"  Edition               : {edition}",
        f"  Engine                : smart_base_engine",
        f"  Timed-out stage       : {timed_out_stage or '(none)'}",
        f"  Heartbeat enabled     : True",
        f"  Longest stage         : {longest} ({longest_dur:.1f}s)",
        "",
        "  ROM integrity checks:",
        f"    cleanup ran before download   : {_bool(cleanup_ran_before_download)}",
        f"    input ROM exists before detect: {_bool(input_rom_exists_before_detect)}",
        f"    input ROM path                : {input_rom_path or '(none)'}",
        "",
        "  Stage timeout config (minutes):",
    ]
    for stage, mins in STAGE_TIMEOUTS_MINUTES.items():
        dur = stage_durations.get(stage, 0.0)
        flag = " ← EXCEEDED" if dur > mins * 60 else ""
        lines.append(f"    {stage:<24} limit={mins}min  actual={dur:.1f}s{flag}")
    lines.append("═══════════════════════════════════════════════════════")
    try:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except Exception as exc:
        print(f"[smart_base_engine] Warning: could not write runtime_guard_report.txt: {exc}")


def _write_final_zip_report(
    reports_dir: Path,
    ctx: Any,
    zip_ok: bool,
) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "final_zip_report.txt"
    lines = [
        "=" * 60,
        "  DeadZone Factory — Final ZIP Report",
        "=" * 60,
        f"  Codename    : {ctx.codename}",
        f"  Edition     : {ctx.edition}",
        f"  Engine      : smart_base_engine",
        f"  ZIP created : {zip_ok}",
        f"  ZIP path    : {ctx.final_zip or '(none)'}",
        f"  PixelDrain  : {ctx.pixeldrain_link or '(none)'}",
        "=" * 60,
    ]
    try:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except Exception as exc:
        print(f"[smart_base_engine] Warning: could not write final_zip_report.txt: {exc}")


def _write_telegram_status_json(
    notifier: Optional[Any],
    enabled: bool,
    soc: str,
    final_status: str,
    reports_dir: Path,
) -> None:
    soc_norm = (soc or "").lower()
    if soc_norm == "mtk":
        token_present   = bool(os.environ.get("TELEGRAM_MTK_BOT_TOKEN") or os.environ.get("TELEGRAM_BOT_TOKEN"))
        chat_id_present = bool(os.environ.get("TELEGRAM_MTK_CHAT_ID")   or os.environ.get("TELEGRAM_CHAT_ID"))
    elif soc_norm == "snapdragon":
        token_present   = bool(os.environ.get("TELEGRAM_SNAPDRAGON_BOT_TOKEN") or os.environ.get("TELEGRAM_BOT_TOKEN"))
        chat_id_present = bool(os.environ.get("TELEGRAM_SNAPDRAGON_CHAT_ID")   or os.environ.get("TELEGRAM_CHAT_ID"))
    else:
        token_present   = bool(os.environ.get("TELEGRAM_BOT_TOKEN"))
        chat_id_present = bool(os.environ.get("TELEGRAM_CHAT_ID"))

    status: dict = {
        "enabled":         enabled,
        "soc":             soc_norm or "unknown",
        "token_present":   token_present,
        "chat_id_present": chat_id_present,
        "final_status":    final_status,
        "message_id":      None,
        "first_update_time": None,
        "last_update_time":  None,
        "last_error":      None,
    }
    if notifier is not None:
        try:
            status["message_id"]        = notifier.message_id
            status["first_update_time"] = notifier.first_update_time
            status["last_update_time"]  = notifier.last_update_time
            last_err = getattr(notifier, "last_error", None)
            status["last_error"] = str(last_err)[:500] if last_err else None
            for attr in [
                "current_stage", "failure_stage", "failure_reason", "failure_hint",
                "raw_error", "previous_message_id", "edit_failed",
                "replacement_message_created", "replacement_reason", "last_api_error",
            ]:
                status[attr] = getattr(notifier, attr, None)
        except Exception:
            pass

    reports_dir.mkdir(parents=True, exist_ok=True)
    try:
        (reports_dir / "telegram_status.json").write_text(
            json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    except Exception as exc:
        print(f"[smart_base_engine] Warning: could not write telegram_status.json: {exc}")


def _android_major(android_version: Optional[str]) -> Optional[int]:
    if not android_version:
        return None
    digits = "".join(c for c in str(android_version) if c.isdigit())
    return int(digits) if digits else None


def _os_family(incremental: Optional[str]) -> str:
    if not incremental:
        return "OS3"
    s = incremental.upper()
    for tag in ("OS3", "OS2", "OS1"):
        if tag in s:
            return tag
    return "OS3"


# ── Public API ─────────────────────────────────────────────────────────────────

def run_smart_base_engine(
    context: Any,
    edition: str,
    apply_mods: bool,
    force_codename: bool = False,
    *,
    notifier: Optional[Any] = None,
    template_zip: Optional[Path] = None,
    pipeline_start: Optional[float] = None,
) -> dict:
    """Run the unified Smart Base Engine for any edition, device, and ROM format.

    Parameters
    ----------
    context:
        BuildContext — carries codename, soc, rom_path, rom_url, mode, etc.
    edition:
        "free", "legend", "gaming", "epic", or any future edition string.
    apply_mods:
        False → Free edition (no patching; preserve original super when possible).
        True  → Legend / Gaming / EPIC (mod layer runs; super always rebuilt).
    force_codename:
        When True, a codename mismatch is recorded as a warning, not a hard error.
    notifier:
        Optional TelegramLiveStatus instance for live progress updates.
    template_zip:
        Optional path to a DeadZone_Mezo template ZIP; when None the engine
        uses the default DeadZone_Mezo/ directory in the repository.
    pipeline_start:
        Monotonic timestamp of when the outer pipeline started (for duration
        reporting).  Defaults to now if not supplied.
    """
    ctx = context
    output_dir = Path(ctx.output_dir) if ctx.output_dir else Path("output")
    work_dir = output_dir / "work"
    reports_dir = output_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    if pipeline_start is None:
        pipeline_start = time.monotonic()

    ok: bool = True
    _timed_out_stage: Optional[str] = None
    _stage_durations: dict[str, float] = {}
    _failed_stage: Optional[str] = None
    _pixeldrain_failed: bool = False
    _failure_summary: Optional[dict] = None

    _analysis: Any = None       # RomAnalysis from universal_rom_intake
    _unpack: Optional[dict] = None
    _super_input: Optional[dict] = None
    _assemble: Optional[dict] = None
    _super_strategy: str = "unknown"

    edition_title = edition.title()

    # ── Notify helper ─────────────────────────────────────────────────────────

    def _notify(stage: str, detail: str, error: Optional[str] = None, force: bool = False) -> None:
        if notifier is not None:
            try:
                notifier.update_stage(stage, detail=detail, error=error, force=force)
            except Exception:
                pass

    # ── Stage runner ──────────────────────────────────────────────────────────

    def _run(stage_id: str, fn: Any, *, critical: bool = False) -> bool:
        nonlocal ok, _timed_out_stage, _failed_stage
        timeout_min = STAGE_TIMEOUTS_MINUTES.get(stage_id, 60)
        use_hb = stage_id in _HEARTBEAT_STAGES

        t0 = time.monotonic()
        result_box: list[Any] = [None]
        exc_box: list[Any] = [None]
        timed_out = False

        def _worker() -> None:
            try:
                result_box[0] = fn()
            except Exception as exc:
                exc_box[0] = exc

        thread = threading.Thread(target=_worker, daemon=True)
        ctx_mgr = _Heartbeat(stage_id, notifier=notifier) if use_hb else _NullCtx()

        with ctx_mgr:
            thread.start()
            thread.join(timeout=timeout_min * 60)
            if thread.is_alive():
                timed_out = True

        duration = round(time.monotonic() - t0, 2)
        _stage_durations[stage_id] = duration

        if timed_out:
            _timed_out_stage = stage_id
            report: dict = {
                "status": "FAILED",
                "errors": [f"Stage timed out after {timeout_min} minutes"],
                "warnings": [],
            }
        elif exc_box[0] is not None:
            report = {"status": "FAILED", "errors": [str(exc_box[0])], "warnings": []}
        else:
            report = result_box[0]
            if not isinstance(report, dict):
                report = {"status": "APPLIED", "warnings": [], "errors": []}

        ctx.stage_reports[stage_id] = report
        ctx.warnings.extend(report.get("warnings") or [])
        ctx.errors.extend(report.get("errors") or [])

        status = str(report.get("final_status") or report.get("status") or "APPLIED").upper()
        timeout_tag = " [TIMEOUT]" if timed_out else ""
        print(f"[smart_base_engine] {stage_id}: {status} ({duration}s){timeout_tag}")

        if critical and status == "FAILED":
            ok = False
            if _failed_stage is None:
                _failed_stage = stage_id.upper()
            return False
        return True

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 1 — Preflight cleanup
    # ══════════════════════════════════════════════════════════════════════════
    _notify(
        "CLEANUP_PREFLIGHT",
        f"Edition: {edition_title} | Engine: Smart | Preflight cleanup",
        force=True,
    )
    try:
        from factory.cleanup.preflight_cleanup import preflight_cleanup
        _preserve = [ctx.rom_path] if getattr(ctx, "rom_path", None) else None
        _pf_result = preflight_cleanup(output_dir, preserve_paths=_preserve)
        ctx.stage_reports["preflight"] = _pf_result
        _stage_durations["preflight"] = 0.0
        print(
            f"[smart_base_engine] preflight: "
            f"{_pf_result.get('status', 'APPLIED')} "
            f"(phase={_pf_result.get('cleanup_phase', 'unknown')})"
        )
    except Exception as _exc:
        print(f"[smart_base_engine] Warning: preflight_cleanup failed (non-fatal): {_exc}")
        ctx.stage_reports["preflight"] = {"status": "SKIPPED", "warnings": [str(_exc)], "errors": []}
        _stage_durations["preflight"] = 0.0

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 2+3 — Analyze ROM + Validate codename
    # ══════════════════════════════════════════════════════════════════════════
    _notify(
        "DETECTING_ROM",
        f"Edition: {edition_title} | Engine: Smart | Analyzing ROM and metadata",
    )

    if ctx.execute and ctx.rom_path:
        from factory.input.universal_rom_intake import (
            analyze_rom,
            write_rom_analysis_report,
            write_codename_validation_report,
        )
        from factory.input.rom_detector import FORMAT_UNKNOWN

        # Guard: ROM file must exist before detection.
        if not Path(ctx.rom_path).exists():
            ctx.errors.append(
                f"Downloaded ROM path is missing after cleanup: {ctx.rom_path}. "
                "Ensure preflight_cleanup is called with preserve_paths=[rom_path]."
            )
            ctx.stage_reports["analyze_rom"] = {
                "status": "FAILED",
                "errors": ctx.errors[-1:],
                "warnings": [],
            }
            ok = False
        else:
            def _analyze() -> dict:
                nonlocal _analysis
                _analysis = analyze_rom(
                    rom_path=ctx.rom_path,
                    rom_url=getattr(ctx, "rom_url", None),
                    selected_codename=ctx.codename,
                    force_codename=force_codename,
                )
                write_rom_analysis_report(_analysis, reports_dir)
                write_codename_validation_report(_analysis, reports_dir)

                if notifier is not None:
                    try:
                        notifier.update_fields(rom_format=_analysis.rom_format)
                    except Exception:
                        pass

                if _analysis.rom_format == FORMAT_UNKNOWN:
                    return {
                        "status": "FAILED",
                        "errors": [
                            f"Unknown ROM format: {_analysis.reason}. "
                            "Supported: payload_ota, fastboot_tgz/tar, images_zip, "
                            "xiaomi_eu_zip, split_super_zip, new_dat_br_zip, raw_super_zip."
                        ],
                        "warnings": list(_analysis.warnings),
                        "rom_format": FORMAT_UNKNOWN,
                    }
                if _analysis.errors:
                    return {
                        "status": "FAILED",
                        "errors": list(_analysis.errors),
                        "warnings": list(_analysis.warnings),
                        "rom_format": _analysis.rom_format,
                    }
                return {
                    "status": "APPLIED",
                    "rom_format": _analysis.rom_format,
                    "detected_codename": _analysis.detected_codename,
                    "codename_match": _analysis.codename_match,
                    "warnings": list(_analysis.warnings),
                    "errors": [],
                }

            ok = _run("analyze_rom", _analyze, critical=True)

        # Propagate rich metadata to context
        if _analysis is not None:
            if not ctx.android_version and _analysis.android_version:
                ctx.android_version = _analysis.android_version
            if not ctx.mi_incremental and _analysis.build_incremental:
                ctx.mi_incremental = _analysis.build_incremental
            if not getattr(ctx, "region", None) and _analysis.region:
                ctx.region = _analysis.region
            if not getattr(ctx, "os_name", None) and _analysis.os_name:
                ctx.os_name = _analysis.os_name
            if not getattr(ctx, "metadata_source", None) and _analysis.metadata_sources_used:
                ctx.metadata_source = ", ".join(_analysis.metadata_sources_used)

    else:
        _status = "DRY_RUN" if not ctx.execute else "SKIPPED_NO_ROM"
        ctx.stage_reports["analyze_rom"] = {"status": _status, "warnings": [], "errors": []}
        # Write placeholder reports so downstream validation scripts don't fail.
        try:
            from factory.input.universal_rom_intake import (
                RomAnalysis, write_rom_analysis_report, write_codename_validation_report,
            )
            _analysis = RomAnalysis(selected_codename=ctx.codename)
            write_rom_analysis_report(_analysis, reports_dir)
            write_codename_validation_report(
                _analysis, reports_dir, action_taken="dry_run — no ROM analyzed"
            )
        except Exception:
            pass

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 4 — Unpack ROM
    # ══════════════════════════════════════════════════════════════════════════
    _notify("UNPACKING_ROM", f"Edition: {edition_title} | Engine: Smart | Unpacking ROM")

    if ok and ctx.execute and _analysis is not None:
        from factory.unpack.universal_unpacker import unpack_with_analysis

        def _do_unpack() -> dict:
            nonlocal _unpack
            res = unpack_with_analysis(
                analysis=_analysis,
                work_dir=work_dir,
                execute=True,
            )
            _unpack = res
            return res

        ok = _run("unpack_rom", _do_unpack, critical=True)
    elif not ctx.execute:
        ctx.stage_reports["unpack_rom"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 5 — Build source image manifest
    # ══════════════════════════════════════════════════════════════════════════
    if ok and ctx.execute:
        from factory.images.source_image_manifest import build_source_image_manifest

        def _do_manifest() -> dict:
            source_roots = [
                work_dir / "source_images",
                work_dir / "unpacked_rom",
            ]
            manifest = build_source_image_manifest(
                source_roots=source_roots,
                work_root=work_dir,
            )
            # Write JSON + TXT reports (private helper accessed directly)
            try:
                from factory.images.source_image_manifest import _write_reports as _mw
                _mw(manifest, reports_dir)
            except Exception as _exc:
                print(
                    f"[smart_base_engine] Warning: source manifest report write failed: {_exc}"
                )
            return {
                "status": "APPLIED",
                "standalone_count": sum(
                    1 for e in manifest.get("images", [])
                    if e.get("role") == "standalone" and e.get("include_in_final")
                ),
                "warnings": [],
                "errors": [],
            }

        _run("source_manifest", _do_manifest)
    elif not ctx.execute:
        ctx.stage_reports["source_manifest"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 6 — Collect super inputs (dynamic partition images)
    # ══════════════════════════════════════════════════════════════════════════
    super_parts_dir = work_dir / "super_parts"

    if ok and ctx.execute:
        from factory.super.super_input_collector import collect_super_inputs

        def _do_super_input() -> dict:
            nonlocal _super_input
            source_dirs = [work_dir / "source_images"]
            source_images_out = output_dir / "images" / "source"
            if source_images_out.is_dir():
                source_dirs.append(source_images_out)
            res = collect_super_inputs(
                source_dirs, super_parts_dir, reports_dir, execute=True
            )
            _super_input = res
            return res

        _run("super_inputs", _do_super_input)
    elif not ctx.execute:
        ctx.stage_reports["super_inputs"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 6b — ListMezo Free Normalize (free edition only)
    # Positioned after super_inputs so partition .img files are available,
    # and before super_execute so any filesystem modifications can influence
    # a future repack stage.
    # ══════════════════════════════════════════════════════════════════════════
    if edition == "free":
        _enable_listmezo: bool = (
            getattr(ctx, "enable_listmezo", None) is not False
            and os.environ.get("ENABLE_LISTMEZO", "true").lower() not in ("0", "false", "no")
        )
        _listmezo_mode: str = (
            getattr(ctx, "listmezo_mode", None)
            or os.environ.get("LISTMEZO_MODE", "dry_run")
        )
        _lm_reports_dir = str(output_dir / "reports" / "listmezo" / "free")

        if _enable_listmezo:
            _notify(
                "LISTMEZO_NORMALIZE",
                f"Edition: Free | ListMezo normalize ({_listmezo_mode})",
            )

            def _do_listmezo() -> dict:
                from factory.apps.listmezo_engine import run_listmezo_pipeline_stage  # noqa: PLC0415
                return run_listmezo_pipeline_stage(
                    edition="free",
                    work_dir=work_dir,
                    output_dir=output_dir,
                    listmezo_mode=_listmezo_mode,
                    execute=ctx.execute,
                )

            _run("listmezo_free_normalize", _do_listmezo)
        else:
            ctx.stage_reports["listmezo_free_normalize"] = {
                "status": "SKIPPED",
                "mode": _listmezo_mode,
                "guide": "ListMezo/free/apps.list",
                "reports_dir": _lm_reports_dir,
                "found_ok": 0, "renamed": 0, "missing": 0,
                "wrong_location": 0, "removed_extras": 0, "unknown": 0,
                "conflicts": 0,
                "warnings": ["enable_listmezo=false"],
                "errors": [],
            }
            _stage_durations["listmezo_free_normalize"] = 0.0

    # ══════════════════════════════════════════════════════════════════════════
    # Stages 7+8 — Select and execute super strategy
    # ══════════════════════════════════════════════════════════════════════════
    final_img_dir = output_dir / "images" / "final"
    final_img_dir.mkdir(parents=True, exist_ok=True)
    super_img = final_img_dir / "super.img"

    if ok and ctx.execute:
        from factory.super.universal_super_engine import (
            select_super_strategy,
            execute_super_strategy,
        )
        from factory.input.rom_detector import FORMAT_PAYLOAD_OTA

        # Locate original super.img if present in the unpacked workspace
        original_super: Optional[Path] = None
        for _cand in [
            work_dir / "source_images" / "super.img",
            work_dir / "unpacked_rom" / "super.img",
        ]:
            if _cand.is_file():
                original_super = _cand
                break

        split_super_merged  = bool(_unpack and _unpack.get("split_super_merged"))
        has_dynamic         = bool(_super_input and _super_input.get("found_dynamic_partitions"))
        is_payload_ota      = bool(
            _analysis is not None
            and getattr(_analysis, "rom_format", None) == FORMAT_PAYLOAD_OTA
        )

        _super_strategy = select_super_strategy(
            original_super_img=original_super,
            split_super_merged=split_super_merged,
            has_dynamic_partitions=has_dynamic,
            apply_mods=apply_mods,
            is_payload_ota=is_payload_ota,
        )

        ctx.stage_reports["super_strategy"] = {
            "status": "APPLIED",
            "strategy": _super_strategy,
            "original_super_exists": original_super is not None,
            "split_super_merged": split_super_merged,
            "has_dynamic_partitions": has_dynamic,
            "is_payload_ota": is_payload_ota,
            "apply_mods": apply_mods,
            "warnings": [],
            "errors": [],
        }
        _stage_durations["super_strategy"] = 0.0

        _tg_super = (
            "PRESERVING_SUPER"
            if _super_strategy in (
                "preserve_original_super",
                "preserve_merged_super",
                "preserve_payload_super",
            )
            else "BUILDING_SUPER"
        )
        _notify(_tg_super, f"Edition: {edition_title} | Super strategy: {_super_strategy}")
        if notifier is not None:
            try:
                notifier.update_fields(super_strategy=_super_strategy)
            except Exception:
                pass

        # ── Recover payload super metadata when rebuilding without original super.img ──
        # For payload OTA ROMs that have dynamic partition images but no super.img,
        # recover partition allocation sizes + group/device profile before calling lpmake.
        _payload_super_meta: Optional[dict] = None
        if is_payload_ota and _super_strategy in (
            "rebuild_with_lpmake", "rebuild_modified_super"
        ) and original_super is None:
            try:
                from factory.super.payload_super_metadata import (  # noqa: PLC0415
                    recover_super_metadata_from_payload,
                )
                # Find payload.bin under work_dir (left behind after unpack)
                _payload_bin: Optional[Path] = None
                for _pb in work_dir.rglob("payload.bin"):
                    if _pb.is_file():
                        _payload_bin = _pb
                        break

                # Locate device registry YAML
                _soc_lc = (getattr(ctx, "soc", None) or "").lower()
                _reg_yml: Optional[Path] = None
                if _soc_lc and ctx.codename:
                    _reg_cand = (
                        Path("registry") / "devices" / _soc_lc / f"{ctx.codename}.yml"
                    )
                    if _reg_cand.is_file():
                        _reg_yml = _reg_cand
                    else:
                        # Try absolute path relative to repo root
                        _reg_abs = _REPO_ROOT / "registry" / "devices" / _soc_lc / f"{ctx.codename}.yml"
                        if _reg_abs.is_file():
                            _reg_yml = _reg_abs

                _payload_super_meta = recover_super_metadata_from_payload(
                    payload_manifest_path=_payload_bin,
                    source_images_dir=work_dir / "source_images",
                    selected_codename=ctx.codename,
                    registry_path=_reg_yml,
                )
                ctx.warnings.extend(_payload_super_meta.get("warnings") or [])
                _psm_errors = _payload_super_meta.get("errors") or []
                if _psm_errors:
                    # Errors here are non-fatal; lpmake will fail with a clear message
                    ctx.warnings.extend(
                        [f"[payload_super_metadata] {e}" for e in _psm_errors]
                    )
                print(
                    f"[smart_base_engine] payload_super_metadata: "
                    f"source={_payload_super_meta.get('metadata_source')} "
                    f"super_size={_payload_super_meta.get('super_size')} "
                    f"group={_payload_super_meta.get('group_name')} "
                    f"partitions={sorted((_payload_super_meta.get('partition_sizes') or {}).keys())}"
                )
            except Exception as _psm_exc:
                print(
                    f"[smart_base_engine] Warning: payload super metadata recovery failed "
                    f"(non-fatal — lpmake will report missing data): {_psm_exc}"
                )

        if _super_strategy == "no_super_available":
            ctx.stage_reports["super_execute"] = {
                "status": "SKIPPED",
                "strategy": "no_super_available",
                "warnings": ["No super.img available — final ZIP may lack super.img"],
                "errors": [],
            }
            ctx.warnings.append("No super.img available — skipping super handling")
            _stage_durations["super_execute"] = 0.0
        else:
            def _do_super_execute() -> dict:
                return execute_super_strategy(
                    strategy=_super_strategy,
                    original_super_img=original_super,
                    super_parts_dir=super_parts_dir,
                    output_super=super_img,
                    reports_dir=reports_dir,
                    execute=True,
                    payload_super_metadata=_payload_super_meta,
                )

            ok = _run("super_execute", _do_super_execute, critical=True)

    elif not ctx.execute:
        ctx.stage_reports["super_strategy"] = {"status": "DRY_RUN", "warnings": [], "errors": []}
        ctx.stage_reports["super_execute"]  = {"status": "DRY_RUN", "warnings": [], "errors": []}
        _stage_durations["super_strategy"]  = 0.0
        _stage_durations["super_execute"]   = 0.0

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 9 — Assemble final images
    # ══════════════════════════════════════════════════════════════════════════
    _notify("ASSEMBLING_IMAGES", f"Edition: {edition_title} | Engine: Smart | Assembling images")

    if ok and ctx.execute:
        from factory.images.final_image_assembler import assemble_final_images, write_intake_report

        def _do_assemble() -> dict:
            nonlocal _assemble
            res = assemble_final_images(
                super_img=super_img,
                source_images_dir=work_dir / "source_images",
                final_dir=final_img_dir,
                execute=True,
            )
            _assemble = res
            return res

        ok = _run("assemble_images", _do_assemble, critical=True)

        # Write rom_intake_report.txt
        try:
            _url_or_path = str(
                getattr(ctx, "rom_url", None) or ctx.rom_path or ""
            )
            write_intake_report(
                reports_dir=reports_dir,
                rom_url_or_path=_url_or_path,
                detected_format=getattr(_analysis, "rom_format", "unknown") if _analysis else "unknown",
                detected_codename=getattr(_analysis, "detected_codename", None) if _analysis else None,
                selected_codename=ctx.codename,
                codename_match=bool(getattr(_analysis, "codename_match", False)) if _analysis else False,
                detected_android_version=getattr(_analysis, "android_version", None) if _analysis else None,
                detected_miui_hyper_version=getattr(_analysis, "build_incremental", None) if _analysis else None,
                detected_region=getattr(_analysis, "region", None) if _analysis else None,
                found_images_count=ctx.stage_reports.get("source_manifest", {}).get("standalone_count", 0),
                found_dynamic_count=len((_super_input or {}).get("found_dynamic_partitions") or []),
                original_super_exists=super_img.is_file(),
                split_super_merged=bool(_unpack and _unpack.get("split_super_merged")),
                super_rebuilt=ok,
                final_image_list=list(
                    (_assemble or {}).get("final_manifest")
                    or (_assemble or {}).get("final_images")
                    or []
                ),
                cleanup_status="PENDING",
                extra_notes=[
                    f"engine: smart_base_engine",
                    f"edition: {edition}",
                    f"apply_mods: {apply_mods}",
                    f"super_strategy: {_super_strategy}",
                ],
            )
        except Exception as _exc:
            print(f"[smart_base_engine] Warning: could not write rom_intake_report.txt: {_exc}")

    elif not ctx.execute:
        ctx.stage_reports["assemble_images"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 10 — Apply edition mods (only when apply_mods=True)
    # ══════════════════════════════════════════════════════════════════════════
    if ok and apply_mods and ctx.execute:
        _notify("APPLYING_MOD_PATCHES", f"Edition: {edition_title} | Applying {edition} mods")
        _mod_mod = _import(f"factory.patch.mods.{edition}.runner")

        if _mod_mod and hasattr(_mod_mod, "run_mod"):
            def _do_mods() -> dict:
                return _mod_mod.run_mod(
                    root=ctx.project_dir,
                    output_dir=output_dir,
                    context={
                        "flavor": edition,
                        "execute": True,
                        "android_major": _android_major(ctx.android_version),
                        "os_family": _os_family(ctx.mi_incremental),
                    },
                )
            _run("apply_mods", _do_mods)
        else:
            ctx.warnings.append(
                f"Mod runner not found: factory.patch.mods.{edition}.runner — SKIPPED_TEMPORARY"
            )
            ctx.stage_reports["apply_mods"] = {
                "status": "SKIPPED",
                "warnings": [f"Mod runner not found: factory.patch.mods.{edition}.runner"],
                "errors": [],
            }
            _stage_durations["apply_mods"] = 0.0
    else:
        _mods_status = "SKIPPED" if not apply_mods else "DRY_RUN"
        _mods_warn: list[str] = []
        if not apply_mods:
            _mods_warn = [f"apply_mods=False — {edition} mods skipped"]
        ctx.stage_reports["apply_mods"] = {
            "status": _mods_status,
            "warnings": _mods_warn,
            "errors": [],
        }
        _stage_durations["apply_mods"] = 0.0

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 11 — Package final ZIP
    # (Template patching + dynamic flash script generation happen inside
    #  final_zip_legacy.build_final_fastboot_zip which calls deadzone_template_patcher
    #  and dynamic_flash_commands internally.)
    # ══════════════════════════════════════════════════════════════════════════
    _notify("PACKAGING_ZIP", f"Edition: {edition_title} | Engine: Smart | Packaging ZIP")

    if ok and ctx.execute:
        zip_mod = _import("factory.output.final_zip_legacy")
        if zip_mod and hasattr(zip_mod, "build_final_fastboot_zip"):
            def _do_zip() -> dict:
                missing_meta: list[str] = []
                if not ctx.android_version:
                    missing_meta.append("android_version")
                if not ctx.mi_incremental:
                    missing_meta.append("mi_incremental/build_incremental")
                if missing_meta:
                    attempted = getattr(ctx, "metadata_sources_attempted", [])
                    return {
                        "status": "FAILED",
                        "errors": [
                            "Missing flash script metadata: "
                            + ", ".join(missing_meta)
                            + f"; sources_attempted={attempted}"
                        ],
                        "warnings": [],
                    }
                return zip_mod.build_final_fastboot_zip(
                    images_dir=final_img_dir,
                    output_dir=output_dir / "final",
                    build_name=ctx.build_name,
                    device=ctx.codename,
                    flavor="deadzone",
                    soc=ctx.soc,
                    platform=ctx.platform,
                    template_zip=template_zip,
                    device_model=ctx.device_model,
                    android_version=ctx.android_version,
                    build_incremental=ctx.mi_incremental,
                    region=getattr(ctx, "region", None) or "",
                    execute=True,
                )

            ok = _run("final_zip", _do_zip, critical=True)
            ctx.final_zip = ctx.stage_reports.get("final_zip", {}).get("final_zip")
        else:
            ctx.errors.append("factory.output.final_zip_legacy module not found")
            ok = False

    elif not ctx.execute:
        ctx.stage_reports["final_zip"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # Write final_zip_report.txt
    try:
        _write_final_zip_report(reports_dir, ctx, ok and bool(ctx.final_zip))
    except Exception as _exc:
        print(f"[smart_base_engine] Warning: could not write final_zip_report.txt: {_exc}")

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 12 — Upload PixelDrain
    # ══════════════════════════════════════════════════════════════════════════
    if ctx.execute and getattr(ctx, "upload_pixeldrain", False) and ctx.final_zip:
        _notify(
            "UPLOADING_PIXELDRAIN",
            f"Edition: {edition_title} | Engine: Smart | Uploading to PixelDrain",
        )
        _pd_mod = _import("factory.upload.pixeldrain")
        if _pd_mod and hasattr(_pd_mod, "upload"):
            def _do_pd() -> dict:
                return _pd_mod.upload(ctx.final_zip, output_dir=output_dir)

            _pd_ok = _run("pixeldrain_upload", _do_pd)
            ctx.pixeldrain_link = ctx.stage_reports.get("pixeldrain_upload", {}).get("link")
            if not _pd_ok or not ctx.pixeldrain_link:
                _pixeldrain_failed = True
    elif ctx.execute and getattr(ctx, "upload_pixeldrain", False) and not ctx.final_zip:
        ctx.stage_reports["pixeldrain_upload"] = {
            "status": "SKIPPED",
            "warnings": ["No final ZIP to upload"],
            "errors": [],
        }
        _stage_durations["pixeldrain_upload"] = 0.0

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 13 — Cleanup workspace
    # ══════════════════════════════════════════════════════════════════════════
    if ctx.execute:
        _notify("CLEANUP", f"Edition: {edition_title} | Engine: Smart | Cleanup")
        from factory.cleanup.cleanup_workspace import cleanup

        # Keep the ZIP when: no upload configured, or upload failed.
        _keep_zip: bool
        if _pixeldrain_failed:
            _keep_zip = True        # upload failed → never delete the ZIP
        elif ctx.pixeldrain_link:
            _keep_zip = False       # successfully uploaded → can remove
        else:
            _keep_zip = True        # no upload → keep for the user

        def _do_cleanup() -> dict:
            return cleanup(output_dir, keep_final_zip=_keep_zip)

        _run("cleanup", _do_cleanup)

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 14 — Runtime guard report
    # ══════════════════════════════════════════════════════════════════════════
    _input_rom_path = getattr(ctx, "rom_path", None)
    _input_rom_exists = (
        _input_rom_path is not None and Path(_input_rom_path).exists()
    ) if _input_rom_path else None
    _write_runtime_guard_report(
        reports_dir=reports_dir,
        codename=ctx.codename,
        edition=edition,
        stage_durations=_stage_durations,
        timed_out_stage=_timed_out_stage,
        input_rom_path=_input_rom_path,
        input_rom_exists_before_detect=_input_rom_exists,
        cleanup_ran_before_download=True,  # preflight always runs before analyze_rom
    )

    # ══════════════════════════════════════════════════════════════════════════
    # Stage 15 — Determine final status + Telegram finalisation
    # ══════════════════════════════════════════════════════════════════════════
    if _pixeldrain_failed and ctx.final_zip:
        final_status = "ZIP_CREATED_UPLOAD_FAILED"
    elif ctx.errors and ctx.execute:
        final_status = "FAILED"
    elif ctx.execute:
        final_status = "APPLIED"
    else:
        final_status = "DRY_RUN"

    _duration = time.monotonic() - pipeline_start

    if notifier is not None:
        try:
            if final_status == "FAILED":
                _tg_err = ctx.errors[0] if ctx.errors else ""
                _tg_stage = _failed_stage or getattr(notifier, "current_stage", "unknown")
                _sum_mod = _import("factory.pipeline.error_summary")
                if _sum_mod and hasattr(_sum_mod, "summarize_error"):
                    _failure_summary = _sum_mod.summarize_error(_tg_err, _tg_stage)
                    notifier.fail(
                        stage=_tg_stage,
                        error_summary=_failure_summary["reason"],
                        duration=_duration,
                        reason=_failure_summary["reason"],
                        hint=_failure_summary.get("hint"),
                        raw_error=_failure_summary.get("raw_error"),
                    )
                else:
                    notifier.fail(
                        stage=_tg_stage,
                        error_summary=_tg_err[:300],
                        duration=_duration,
                    )
            elif final_status == "ZIP_CREATED_UPLOAD_FAILED":
                # Build finished; upload failed — tell Telegram clearly.
                _zip_name = Path(ctx.final_zip).name if ctx.final_zip else None
                if hasattr(notifier, "upload_failed"):
                    notifier.upload_failed(final_zip_name=_zip_name, duration=_duration)
                else:
                    notifier.success(
                        final_zip_name=_zip_name,
                        pixeldrain_link=None,
                        duration=_duration,
                    )
            else:
                _zip_name = Path(ctx.final_zip).name if ctx.final_zip else None
                notifier.success(
                    final_zip_name=_zip_name,
                    pixeldrain_link=ctx.pixeldrain_link,
                    duration=_duration,
                )
        except Exception as _tg_exc:
            print(f"[smart_base_engine] Telegram finalize error: {_tg_exc}")

    # Export message_id for GitHub Actions handoff
    if notifier is not None and getattr(notifier, "message_id", None) is not None:
        _gha_env = os.environ.get("GITHUB_ENV", "")
        if _gha_env:
            try:
                with open(_gha_env, "a", encoding="utf-8") as _gf:
                    _gf.write(f"DEADZONE_TELEGRAM_MESSAGE_ID={notifier.message_id}\n")
            except Exception:
                pass

    # Write telegram_status.json
    _write_telegram_status_json(
        notifier=notifier,
        enabled=getattr(ctx, "notify_telegram", False),
        soc=getattr(ctx, "soc", "") or "",
        final_status=final_status,
        reports_dir=reports_dir,
    )

    # Write pipeline_report.json via shared helper
    report_files: dict = {}
    build_id: Optional[str] = None
    try:
        from factory.pipeline.report import write_pipeline_report
        build_id = getattr(notifier, "build_id", None) if notifier is not None else None
        _tg_section = (
            notifier.report_section()
            if notifier is not None and hasattr(notifier, "report_section")
            else None
        )
        if final_status == "FAILED" and ctx.errors and _failure_summary is None:
            _sum_mod2 = _import("factory.pipeline.error_summary")
            if _sum_mod2 and hasattr(_sum_mod2, "summarize_error"):
                _failure_summary = _sum_mod2.summarize_error(
                    ctx.errors[0], _failed_stage or ""
                )
        report_files = write_pipeline_report(
            ctx, output_dir,
            telegram=_tg_section,
            build_id=build_id,
            failure_summary=_failure_summary,
        )
    except Exception as _exc:
        print(f"[smart_base_engine] Warning: could not write pipeline report: {_exc}")

    print(f"[smart_base_engine] final_status={final_status}")
    if ctx.errors:
        print(f"[smart_base_engine] ERRORS ({len(ctx.errors)}):")
        for _i, _e in enumerate(ctx.errors, 1):
            print(f"  [{_i}] {_e}")
    if ctx.warnings:
        print(f"[smart_base_engine] WARNINGS ({len(ctx.warnings)}):")
        for _i, _w in enumerate(ctx.warnings, 1):
            print(f"  [{_i}] {_w}")

    return {
        "final_status":        final_status,
        "build_id":            build_id,
        "build_name":          ctx.build_name,
        "codename":            ctx.codename,
        "edition":             edition,
        "soc":                 ctx.soc,
        "final_zip":           ctx.final_zip,
        "pixeldrain_link":     ctx.pixeldrain_link,
        "telegram_message_id": getattr(notifier, "message_id", None),
        "warnings":            ctx.warnings,
        "errors":              ctx.errors,
        "stage_reports":       ctx.stage_reports,
        "report_files":        report_files,
        # Internal fields for caller reporting (prefixed _)
        "_super_strategy":     _super_strategy,
        "_pixeldrain_failed":  _pixeldrain_failed,
        "_failure_summary":    _failure_summary,
        "_stage_durations":    _stage_durations,
        "_timed_out_stage":    _timed_out_stage,
        "_failed_stage":       _failed_stage,
        "_analysis":           _analysis,
        "_unpack":             _unpack,
        "_super_input":        _super_input,
        "_assemble":           _assemble,
    }
