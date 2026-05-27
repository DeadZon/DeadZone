"""Shared legacy/legend engine runner for DeadZone Factory.

Both Free (apply_mods=False) and Legend/Gaming/EPIC (apply_mods=True) editions
use the same ROM intake, image collection, super handling, and ZIP packaging
pipeline.  This module is the canonical implementation of that shared engine.

run_legacy_engine() is called by free_pipeline.py (and optionally by other
edition pipelines).  All unpack / super / repack logic lives here — not in
individual edition pipelines.

Super strategy selection
------------------------
apply_mods=False  (Free edition):
  - Source has original super.img     → preserve_original_super  (copy, no lpmake)
  - Source has merged split super.img → preserve_merged_super    (copy, no lpmake)
  - Payload OTA → only dynamic parts  → rebuild_with_lpmake      (legacy lpmake path)
  - No super at all                   → no_super_available       (warning, non-fatal)

apply_mods=True  (Legend/Gaming/EPIC):
  - Always → rebuild_with_lpmake  (apply mod partitions, rebuild with lpmake)

Stage timeouts
--------------
Each stage has a configured timeout (minutes).  If a stage exceeds its limit
the stage is marked FAILED, ok is set to False, and subsequent critical stages
are skipped.  The background thread is left to finish on its own (Python cannot
force-kill threads); GitHub Actions job-level timeout provides the final safety net.

Heartbeat
---------
For heavy stages a daemon thread logs "[heartbeat] stage=… elapsed=…s" every 60
seconds so GitHub Actions does not kill the job for lack of output.
"""
from __future__ import annotations

import importlib
import os
import shutil
import threading
import time
from pathlib import Path
from typing import Any, Optional


# ── Stage timeout configuration (minutes) ────────────────────────────────────

STAGE_TIMEOUTS_MINUTES: dict[str, int] = {
    "detect_rom":         5,
    "unpack_rom":         60,
    "collect_images":     15,
    "super_inputs":       15,
    "super_rebuild":      60,
    "assemble_images":    15,
    "final_zip":          45,
    "pixeldrain_upload":  45,
    "cleanup":            10,
}

_HEARTBEAT_STAGES: frozenset[str] = frozenset({
    "unpack_rom",
    "super_rebuild",
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
    """Daemon thread that logs a one-liner every `interval` seconds."""

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
            print(f"[heartbeat] stage={self._stage} elapsed={elapsed}s tick={tick}", flush=True)
            if self._notifier is not None:
                try:
                    self._notifier.heartbeat()
                except Exception:
                    pass


def _write_runtime_guard_report(
    reports_dir: Path,
    workflow: str,
    codename: str,
    edition: str,
    stage_durations: dict[str, float],
    timed_out_stage: Optional[str],
    input_rom_path: Optional[Path] = None,
    input_rom_exists_before_detect: Optional[bool] = None,
    cleanup_ran_before_download: Optional[bool] = None,
) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "runtime_guard_report.txt"
    longest_stage = max(stage_durations, key=stage_durations.get) if stage_durations else "(none)"
    longest_dur = stage_durations.get(longest_stage, 0)

    def _bool(v: Optional[bool]) -> str:
        return "true" if v is True else ("false" if v is False else "N/A")

    lines = [
        "═══════════════════════════════════════════════════════",
        "  DeadZone Factory — Runtime Guard Report",
        "═══════════════════════════════════════════════════════",
        f"  Workflow              : {workflow}",
        f"  Device (codename)     : {codename}",
        f"  Edition               : {edition}",
        f"  Concurrency group     : deadzone-{workflow}-{codename}-{edition}",
        f"  Timed-out stage       : {timed_out_stage or '(none)'}",
        f"  Heartbeat enabled     : True",
        f"  Longest stage         : {longest_stage} ({longest_dur:.1f}s)",
        "",
        "  ROM integrity checks:",
        f"    cleanup ran before download   : {_bool(cleanup_ran_before_download)}",
        f"    input ROM exists before detect: {_bool(input_rom_exists_before_detect)}",
        f"    input ROM path                : {input_rom_path or '(none)'}",
        "",
        "  Stage timeout config (minutes):",
    ]
    for stage, mins in STAGE_TIMEOUTS_MINUTES.items():
        dur = stage_durations.get(stage, 0)
        over = " ← EXCEEDED" if dur > mins * 60 else ""
        lines.append(f"    {stage:<24} limit={mins}min  actual={dur:.1f}s{over}")
    lines.append("═══════════════════════════════════════════════════════")
    try:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except Exception as exc:
        print(f"[legacy_engine] Warning: could not write runtime_guard_report.txt: {exc}")


def _write_free_engine_report(
    reports_dir: Path,
    ctx: Any,
    result: dict,
) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "free_engine_report.txt"
    det = result.get("_detection")
    unp = result.get("_unpack") or {}
    asm = result.get("_assemble") or {}
    sr = ctx.stage_reports.get("super_rebuild") or {}

    input_rom_path = getattr(ctx, "rom_path", None)
    input_rom_exists = input_rom_path is not None and Path(input_rom_path).exists()
    lines = [
        "═══════════════════════════════════════════════════════",
        "  DeadZone Factory — Free Engine Report",
        "═══════════════════════════════════════════════════════",
        f"  Engine used           : legacy/legend",
        f"  Edition               : {ctx.edition}",
        f"  apply_mods            : False",
        f"  fast_mode             : True",
        f"  Input ROM path        : {input_rom_path or '(none)'}",
        f"  Input ROM exists      : {input_rom_exists}",
        f"  ROM format            : {det.rom_format if det else 'N/A'}",
        f"  Super strategy        : {result.get('_super_strategy', 'unknown')}",
        f"  Original super exists : {bool(result.get('_original_super_existed'))}",
        f"  Preserved orig super  : {sr.get('strategy') == 'preserve_original_super'}",
        f"  Rebuilt super         : {sr.get('strategy') == 'rebuild_with_lpmake'}",
        f"  lpmake executed       : {bool(sr.get('lpmake_executed'))}",
        f"  Payload dump method   : {unp.get('payload_dump_tool', 'N/A')}",
        f"  lpmake cmd source     : {sr.get('super_metadata_source', 'N/A')}",
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
        "",
        "  Stage durations:",
    ]
    for stage, rep in (ctx.stage_reports or {}).items():
        if isinstance(rep, dict) and "_duration" in rep:
            lines.append(f"    {stage:<24} {rep['_duration']:.1f}s")
    lines += [
        "",
        f"  Cleanup before build  : {result.get('_preflight_cleanup_status', 'N/A')}",
        f"  Cleanup after build   : {ctx.stage_reports.get('cleanup', {}).get('status', 'N/A')}",
    ]
    if ctx.errors:
        lines += ["", "  Errors:"]
        for e in ctx.errors:
            lines.append(f"    ! {e}")
    lines.append("═══════════════════════════════════════════════════════")
    try:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except Exception as exc:
        print(f"[legacy_engine] Warning: could not write free_engine_report.txt: {exc}")


# ── Public API ─────────────────────────────────────────────────────────────────

def run_legacy_engine(
    context: Any,
    notifier: Optional[Any],
    output_dir: Path,
    template_zip: Optional[Path],
    pipeline_start: float,
    edition: str = "free",
    apply_mods: bool = False,
    fast_mode: bool = True,
    use_universal_detector: bool = True,
) -> dict:
    """Run the full legacy pipeline for the given edition.

    Parameters
    ----------
    context:
        BuildContext — carries codename, soc, rom_path, mode, etc.
    apply_mods:
        False → Free edition (no APK/smali/overlay patching; preserve original
        super.img when possible).
        True  → Legend/Gaming/EPIC (always rebuild super with lpmake).
    fast_mode:
        When True, enables threading-optimised extract and store-mode ZIP
        compression (DEADZONE_ZIP_LEVEL=0).
    """
    ctx = context
    output_dir = Path(output_dir)
    work_dir = output_dir / "work"
    reports_dir = output_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    ok: bool = True
    _detection:    Any            = None
    _unpack:       Optional[dict] = None
    _collect:      Optional[dict] = None
    _super_input:  Optional[dict] = None
    _assemble:     Optional[dict] = None
    _super_strategy: str          = "unknown"
    _original_super_existed: bool = False
    _timed_out_stage: Optional[str] = None
    _stage_durations: dict[str, float] = {}
    _input_rom_exists_before_detect: Optional[bool] = None
    _failed_stage: Optional[str] = None  # canonical Telegram stage of failure

    # Map engine stage_id → canonical Telegram stage used in failure messages
    _STAGE_TO_TELEGRAM: dict[str, str] = {
        "detect_rom":        "DETECTING_ROM",
        "unpack_rom":        "UNPACKING_ROM",
        "collect_images":    "COLLECTING_IMAGES",
        "super_inputs":      "COLLECTING_IMAGES",
        "super_rebuild":     "PRESERVING_SUPER",
        "assemble_images":   "ASSEMBLING_IMAGES",
        "final_zip":         "PACKAGING_ZIP",
        "pixeldrain_upload": "UPLOADING_PIXELDRAIN",
        "cleanup":           "CLEANUP",
    }

    def _notify(stage: str, detail: str, error: Optional[str] = None, force: bool = False) -> None:
        if notifier is not None:
            try:
                notifier.update_stage(stage, detail=detail, error=error, force=force)
            except Exception:
                pass

    def _run(stage_id: str, fn: Any, *, critical: bool = False) -> bool:
        nonlocal ok, _timed_out_stage, _failed_stage
        timeout_min = STAGE_TIMEOUTS_MINUTES.get(stage_id, 60)
        use_heartbeat = stage_id in _HEARTBEAT_STAGES

        t0 = time.monotonic()
        timed_out = False

        result_box: list[Any] = [None]
        exc_box:    list[Any] = [None]

        def _worker() -> None:
            try:
                result_box[0] = fn()
            except Exception as exc:
                exc_box[0] = exc

        thread = threading.Thread(target=_worker, daemon=True)
        ctx_mgr = _Heartbeat(stage_id, notifier=notifier) if use_heartbeat else _NullCtx()

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
                "errors": [f"Stage timed out: {stage_id} after {timeout_min} minutes"],
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
        print(f"[legacy_engine] {stage_id}: {status} ({duration}s){timeout_tag}")

        if critical and status == "FAILED":
            ok = False
            if _failed_stage is None:
                _failed_stage = _STAGE_TO_TELEGRAM.get(stage_id, stage_id.upper())
            return False
        return True

    # ── Stage 1: Detect ROM ───────────────────────────────────────────────────
    edition_title = edition.title()
    _notify(
        "DETECTING_ROM",
        f"Edition: {edition_title} | Engine: Legacy | Mods: {'On' if apply_mods else 'Off'} | Detecting ROM",
        force=True,
    )

    if ctx.execute and ctx.rom_path:
        from factory.input.rom_detector import (
            detect_rom_format, FORMAT_UNKNOWN, check_codename_match,
        )

        # Guard: verify the ROM file exists before attempting detection.
        # If preflight_cleanup deleted _input_roms/ after the workflow had
        # already downloaded the ROM there, detect_rom would silently receive
        # FORMAT_UNKNOWN with reason "file not found".  Catching this early
        # gives a clear, actionable error message.
        _input_rom_exists_before_detect = Path(ctx.rom_path).exists()
        if not _input_rom_exists_before_detect:
            ctx.errors.append(
                f"Downloaded ROM path is missing after cleanup: {ctx.rom_path}. "
                "Cleanup must run before download or must preserve the active ROM path. "
                "Ensure preflight_cleanup is called with preserve_paths=[rom_path] when "
                "the workflow downloads the ROM before the pipeline starts."
            )
            ctx.stage_reports["detect_rom"] = {
                "status": "FAILED",
                "errors": ctx.errors[-1:],
                "warnings": [],
            }
            ok = False

        if ok:
            def _detect() -> dict:
                nonlocal _detection
                res = detect_rom_format(ctx.rom_path)
                _detection = res
                # Propagate detected format to Telegram live message
                if notifier is not None:
                    try:
                        notifier.update_fields(rom_format=res.rom_format)
                    except Exception:
                        pass
                if res.rom_format == FORMAT_UNKNOWN:
                    return {
                        "status": "FAILED",
                        "errors": [
                            f"Unknown ROM format: {res.reason}. "
                            "Supported: payload_ota, fastboot_tgz/tar, images_zip, "
                            "xiaomi_eu_zip, split_super_zip, new_dat_br_zip, raw_super_zip."
                        ],
                        "warnings": res.warnings,
                    }
                codename_ok, codename_msg = check_codename_match(
                    res.detected_device_codename, ctx.codename
                )
                errs = [] if codename_ok else [codename_msg]
                return {
                    "status": "FAILED" if errs else "APPLIED",
                    "rom_format": res.rom_format,
                    "confidence": res.confidence,
                    "detected_codename": res.detected_device_codename,
                    "errors": errs,
                    "warnings": res.warnings,
                }

            ok = _run("detect_rom", _detect, critical=True)

        # Propagate filename-parsed metadata to context if build.prop left them empty.
        if _detection is not None:
            if not ctx.android_version and _detection.detected_android_version:
                ctx.android_version = _detection.detected_android_version
            if not ctx.mi_incremental and _detection.detected_hyperos_or_miui_version:
                ctx.mi_incremental = _detection.detected_hyperos_or_miui_version
    else:
        ctx.stage_reports["detect_rom"] = {
            "status": "DRY_RUN" if not ctx.execute else "SKIPPED_NO_ROM",
            "warnings": [], "errors": [],
        }

    # ── Stage 2: Unpack ROM ───────────────────────────────────────────────────
    _notify("UNPACKING_ROM", f"Edition: {edition_title} | Engine: Legacy | Unpacking ROM")

    if ok and ctx.execute and ctx.rom_path and _detection is not None:
        from factory.input.rom_unpacker import unpack_rom

        def _do_unpack() -> dict:
            nonlocal _unpack
            res = unpack_rom(ctx.rom_path, _detection.rom_format, work_dir)
            _unpack = res
            return res

        ok = _run("unpack_rom", _do_unpack, critical=True)
    elif not ctx.execute:
        ctx.stage_reports["unpack_rom"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ── Stage 3: Collect source images ────────────────────────────────────────
    source_images_out = output_dir / "images" / "source"
    _notify("COLLECTING_IMAGES", f"Edition: {edition_title} | Collecting images from ROM")

    if ok and ctx.execute:
        from factory.images.source_image_collector import collect_source_images

        def _do_collect() -> dict:
            nonlocal _collect
            source_dirs = [work_dir / "source_images"]
            unpacked_dir = work_dir / "unpacked_rom"
            for sub in ["images", "firmware-update"]:
                cand = unpacked_dir / sub
                if cand.is_dir():
                    source_dirs.append(cand)
            if unpacked_dir.is_dir():
                source_dirs.append(unpacked_dir)
            res = collect_source_images(source_dirs, source_images_out, soc=ctx.soc, execute=True)
            _collect = res
            return res

        _run("collect_images", _do_collect)
    elif not ctx.execute:
        ctx.stage_reports["collect_images"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ── Stage 4: Collect dynamic partition images ─────────────────────────────
    super_parts_dir = work_dir / "super_parts"

    if ok and ctx.execute:
        from factory.super.super_input_collector import collect_super_inputs

        def _do_super_input() -> dict:
            nonlocal _super_input
            source_dirs = [work_dir / "source_images"]
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

    # ── Stage 5: Super handling ───────────────────────────────────────────────
    final_img_dir = output_dir / "images" / "final"
    final_img_dir.mkdir(parents=True, exist_ok=True)
    super_img = final_img_dir / "super.img"

    if ok and ctx.execute:
        original_super: Optional[Path] = None
        for cand in [
            work_dir / "source_images" / "super.img",
            work_dir / "unpacked_rom" / "super.img",
        ]:
            if cand.is_file():
                original_super = cand
                break

        _original_super_existed = original_super is not None
        split_merged = bool(_unpack and _unpack.get("split_super_merged"))
        has_dynamic = bool(_super_input and _super_input.get("found_dynamic_partitions"))

        # Choose strategy
        if not apply_mods and original_super is not None:
            _super_strategy = "preserve_original_super"
        elif not apply_mods and split_merged and original_super is not None:
            _super_strategy = "preserve_merged_super"
        elif not apply_mods and not has_dynamic and original_super is None:
            _super_strategy = "no_super_available"
        else:
            _super_strategy = "rebuild_with_lpmake"

        _tg_super_stage = (
            "PRESERVING_SUPER"
            if _super_strategy in ("preserve_original_super", "preserve_merged_super")
            else "BUILDING_SUPER"
        )
        _notify(
            _tg_super_stage,
            f"Edition: {edition_title} | Super strategy: {_super_strategy}",
        )
        # Let notifier know the super strategy for display in the live message
        if notifier is not None:
            try:
                notifier.update_fields(super_strategy=_super_strategy)
            except Exception:
                pass

        if _super_strategy in ("preserve_original_super", "preserve_merged_super"):
            def _do_preserve() -> dict:
                from factory.super.super_rebuilder import rebuild_super
                return rebuild_super(
                    super_parts_dir=super_parts_dir,
                    output_super=super_img,
                    reports_dir=reports_dir,
                    original_super_img=original_super,
                    execute=True,
                    preserve_original_super=True,
                )
            ok = _run("super_rebuild", _do_preserve, critical=True)

        elif _super_strategy == "rebuild_with_lpmake":
            def _do_rebuild() -> dict:
                from factory.super.super_rebuilder import rebuild_super
                return rebuild_super(
                    super_parts_dir=super_parts_dir,
                    output_super=super_img,
                    reports_dir=reports_dir,
                    original_super_img=original_super,
                    execute=True,
                    preserve_original_super=False,
                )
            ok = _run("super_rebuild", _do_rebuild, critical=True)

        else:
            # no_super_available — non-fatal for Free
            ctx.stage_reports["super_rebuild"] = {
                "status": "SKIPPED",
                "strategy": "no_super_available",
                "warnings": ["No super.img available — final ZIP may lack super.img"],
                "errors": [],
            }
            ctx.warnings.append("No super.img available — skipping super handling")

    elif not ctx.execute:
        ctx.stage_reports["super_rebuild"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ── Stage 6: Assemble final images ────────────────────────────────────────
    _notify("ASSEMBLING_IMAGES", f"Edition: {edition_title} | Assembling final images")
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
            det = _detection
            col = _collect or {}
            si  = _super_input or {}
            asm = _assemble or {}
            write_intake_report(
                reports_dir=reports_dir,
                rom_url_or_path=str(ctx.rom_url or ctx.rom_path or ""),
                detected_format=det.rom_format if det else "unknown",
                detected_codename=det.detected_device_codename if det else None,
                selected_codename=ctx.codename,
                codename_match=True,
                detected_android_version=det.detected_android_version if det else None,
                detected_miui_hyper_version=det.detected_hyperos_or_miui_version if det else None,
                detected_region=det.detected_region if det else None,
                found_images_count=len(col.get("standalone_images", {})),
                found_dynamic_count=len(si.get("found_dynamic_partitions", [])),
                original_super_exists=_original_super_existed,
                split_super_merged=bool(_unpack and _unpack.get("split_super_merged")),
                super_rebuilt=ok,
                final_image_list=list(asm.get("final_manifest") or asm.get("final_images") or []),
                cleanup_status="PENDING",
            )
        except Exception as exc:
            print(f"[legacy_engine] Warning: could not write rom_intake_report.txt: {exc}")

    elif not ctx.execute:
        ctx.stage_reports["assemble_images"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ── Stage 7: Package fastboot ZIP ─────────────────────────────────────────
    _notify("PACKAGING_ZIP", f"Edition: {edition_title} | Engine: Legacy | Packaging ZIP")

    if ok and ctx.execute:
        zip_mod = _import("factory.output.final_zip_legacy")
        if zip_mod and hasattr(zip_mod, "build_final_fastboot_zip"):
            def _do_zip() -> dict:
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
                    execute=True,
                )
            ok = _run("final_zip", _do_zip, critical=True)
            ctx.final_zip = ctx.stage_reports.get("final_zip", {}).get("final_zip")
        else:
            ctx.errors.append("factory.output.final_zip_legacy module not found")
            ok = False
    elif not ctx.execute:
        ctx.stage_reports["final_zip"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ── Stage 8: Upload PixelDrain ────────────────────────────────────────────
    if ok and ctx.execute and ctx.upload_pixeldrain and ctx.final_zip:
        _notify(
            "UPLOADING_PIXELDRAIN",
            f"Edition: {edition_title} | Engine: Legacy | Uploading to PixelDrain",
        )
        pd_mod = _import("factory.upload.pixeldrain")
        if pd_mod and hasattr(pd_mod, "upload"):
            def _pd() -> dict:
                return pd_mod.upload(ctx.final_zip, output_dir=output_dir)
            _run("pixeldrain_upload", _pd)
            ctx.pixeldrain_link = ctx.stage_reports.get("pixeldrain_upload", {}).get("link")

    # ── Stage 9: Post-run cleanup ─────────────────────────────────────────────
    if ctx.execute:
        _notify("CLEANUP", f"Edition: {edition_title} | Engine: Legacy | Cleanup")
        from factory.cleanup.cleanup_workspace import cleanup

        def _do_cleanup() -> dict:
            return cleanup(output_dir, keep_final_zip=not bool(ctx.pixeldrain_link))

        _run("cleanup", _do_cleanup)

    # ── Write runtime guard report ────────────────────────────────────────────
    workflow_name = os.environ.get("GITHUB_WORKFLOW", "local")
    _write_runtime_guard_report(
        reports_dir=reports_dir,
        workflow=workflow_name,
        codename=ctx.codename,
        edition=edition,
        stage_durations=_stage_durations,
        timed_out_stage=_timed_out_stage,
        input_rom_path=getattr(ctx, "rom_path", None),
        input_rom_exists_before_detect=_input_rom_exists_before_detect,
        cleanup_ran_before_download=True,  # preflight_cleanup always runs first in free_pipeline
    )

    # ── Finalize Telegram ─────────────────────────────────────────────────────
    final_status = (
        "FAILED" if (ctx.errors and ctx.execute)
        else ("APPLIED" if ctx.execute else "DRY_RUN")
    )
    _duration = time.monotonic() - pipeline_start

    if notifier is not None:
        try:
            if final_status == "FAILED":
                from factory.pipeline.error_summary import summarize_error
                raw_err = ctx.errors[0] if ctx.errors else ""
                tg_stage = _failed_stage or getattr(notifier, "current_stage", "unknown")
                summary = summarize_error(raw_err, tg_stage)
                notifier.fail(
                    stage=tg_stage,
                    error_summary=summary["reason"],
                    duration=_duration,
                    reason=summary["reason"],
                    hint=summary["hint"],
                    raw_error=summary["raw_error"],
                )
            else:
                zip_name = Path(ctx.final_zip).name if ctx.final_zip else None
                notifier.success(
                    final_zip_name=zip_name,
                    pixeldrain_link=ctx.pixeldrain_link,
                    duration=_duration,
                )
        except Exception as _tg_exc:
            print(f"[legacy_engine] Telegram finalize error: {_tg_exc}")

    # Export message_id for GitHub Actions handoff
    if notifier is not None and getattr(notifier, "message_id", None) is not None:
        _gha_env = os.environ.get("GITHUB_ENV", "")
        if _gha_env:
            try:
                with open(_gha_env, "a", encoding="utf-8") as _f:
                    _f.write(f"DEADZONE_TELEGRAM_MESSAGE_ID={notifier.message_id}\n")
            except Exception:
                pass

    # ── Write pipeline report ─────────────────────────────────────────────────
    from factory.pipeline.report import write_pipeline_report
    build_id = getattr(notifier, "build_id", None) if notifier is not None else None
    telegram_section = (
        notifier.report_section() if notifier is not None and hasattr(notifier, "report_section") else None
    )
    # Include failure details in pipeline report
    _failure_summary: Optional[dict] = None
    if final_status == "FAILED" and ctx.errors:
        from factory.pipeline.error_summary import summarize_error
        _failure_summary = summarize_error(ctx.errors[0], _failed_stage or "")
    report_files = write_pipeline_report(
        ctx, output_dir,
        telegram=telegram_section,
        build_id=build_id,
        failure_summary=_failure_summary,
    )

    print(f"[legacy_engine] final_status={final_status}")
    if ctx.errors:
        print(f"[legacy_engine] ERRORS ({len(ctx.errors)}):")
        for i, e in enumerate(ctx.errors, 1):
            print(f"  [{i}] {e}")
    if ctx.warnings:
        print(f"[legacy_engine] WARNINGS ({len(ctx.warnings)}):")
        for i, w in enumerate(ctx.warnings, 1):
            print(f"  [{i}] {w}")

    return {
        "final_status":          final_status,
        "build_id":              build_id,
        "build_name":            ctx.build_name,
        "codename":              ctx.codename,
        "edition":               ctx.edition,
        "soc":                   ctx.soc,
        "final_zip":             ctx.final_zip,
        "pixeldrain_link":       ctx.pixeldrain_link,
        "telegram_message_id":   getattr(notifier, "message_id", None),
        "warnings":              ctx.warnings,
        "errors":                ctx.errors,
        "stage_reports":         ctx.stage_reports,
        "report_files":          report_files,
        # Internal fields used by free_pipeline for its own reports — prefixed _
        "_super_strategy":            _super_strategy,
        "_original_super_existed":    _original_super_existed,
        "_detection":                 _detection,
        "_unpack":                    _unpack,
        "_collect":                   _collect,
        "_super_input":               _super_input,
        "_assemble":                  _assemble,
        "_stage_durations":           _stage_durations,
        "_timed_out_stage":           _timed_out_stage,
        "_failed_stage":              _failed_stage,
        "_failure_summary":           _failure_summary,
    }


class _NullCtx:
    """No-op context manager (used when heartbeat is not needed)."""
    def __enter__(self) -> "_NullCtx":
        return self
    def __exit__(self, *_: Any) -> None:
        pass
