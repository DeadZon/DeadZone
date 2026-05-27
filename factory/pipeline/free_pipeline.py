"""DeadZone Free edition pipeline — Universal ROM Intake, no mods applied.

Pipeline stages
---------------
1. Detect ROM format   (factory.input.rom_detector)
2. Unpack ROM          (factory.input.rom_unpacker)
3. Collect images      (factory.images.source_image_collector)
4. Collect super parts (factory.super.super_input_collector)
5. Rebuild super.img   (factory.super.super_rebuilder)
6. Assemble final dir  (factory.images.final_image_assembler)
7. Package fastboot ZIP (factory.output.final_zip_legacy)
8. Upload PixelDrain
9. Cleanup
"""
from __future__ import annotations

import importlib
import json
import os
import time
from pathlib import Path
from typing import Any, Optional


# ── Helpers ───────────────────────────────────────────────────────────────────

def _import(module: str) -> Any:
    try:
        return importlib.import_module(module)
    except ImportError:
        return None


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
        except Exception:
            pass

    try:
        reports_dir = output_dir / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)
        out_path = reports_dir / "telegram_status.json"
        out_path.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8")
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
) -> None:
    """Write output/reports/free_build_report.txt."""
    try:
        det = detection
        col = collect or {}
        si  = super_input or {}
        asm = assemble or {}
        unp = unpack or {}

        lines = [
            "=" * 60,
            "  DeadZone Free Edition — Build Report",
            "=" * 60,
            f"  Device   : {ctx.codename}",
            f"  Edition  : Free",
            f"  ROM URL  : {ctx.rom_url or str(ctx.rom_path or '')}",
            f"  SoC      : {ctx.soc}",
            f"  Mode     : {ctx.mode}",
            "=" * 60,
            "  ROM Detection:",
            f"    Format    : {det.rom_format if det else 'N/A'}",
            f"    Codename  : {det.detected_device_codename if det else 'N/A'}",
            f"    Android   : {det.detected_android_version if det else 'N/A'}",
            f"    Version   : {det.detected_hyperos_or_miui_version if det else 'N/A'}",
            f"    Region    : {det.detected_region if det else 'N/A'}",
        ]

        # Payload dump section (only present for payload_ota ROMs)
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
            "  Image Collection:",
            f"    Normal images    : {len(col.get('standalone_images', {}))}",
            f"    Dynamic parts    : {len(si.get('found_dynamic_partitions', []))}",
        ]

        final_imgs = asm.get("final_images", [])
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
    """Full Free edition pipeline. Returns the same dict shape as run_factory."""

    ok = True
    output_dir = Path(output_dir)
    work_dir   = output_dir / "work"
    reports_dir = output_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Intake metadata tracked for the final report
    _detection:   Any           = None
    _unpack:      Optional[dict] = None
    _collect:     Optional[dict] = None
    _super_input: Optional[dict] = None
    _assemble:    Optional[dict] = None

    def _notify(stage: str, detail: str, error: Optional[str] = None, force: bool = False) -> None:
        if notifier is not None:
            try:
                notifier.update_stage(stage, detail=detail, error=error, force=force)
            except Exception:
                pass

    def _run(stage_id: str, fn, *, critical: bool = False) -> bool:
        nonlocal ok
        t0 = time.monotonic()
        try:
            report = fn()
            if not isinstance(report, dict):
                report = {"status": "APPLIED", "warnings": [], "errors": []}
        except Exception as exc:
            report = {"status": "FAILED", "errors": [str(exc)], "warnings": []}

        ctx.stage_reports[stage_id] = report
        ctx.warnings.extend(report.get("warnings") or [])
        ctx.errors.extend(report.get("errors") or [])

        status   = str(report.get("final_status") or report.get("status") or "APPLIED").upper()
        duration = round(time.monotonic() - t0, 2)
        print(f"[free_pipeline] {stage_id}: {status} ({duration}s)")

        if critical and status == "FAILED":
            ok = False
            return False
        return True

    # ── Stage 1: Detect ROM ───────────────────────────────────────────────────
    _notify("DETECTING_ROM", "Edition: Free | Stage: Detecting ROM", force=True)

    if ctx.execute and ctx.rom_path:
        from factory.input.rom_detector import (
            detect_rom_format,
            FORMAT_UNKNOWN,
            check_codename_match,
        )

        def _detect():
            nonlocal _detection
            result = detect_rom_format(ctx.rom_path)
            _detection = result

            if result.rom_format == FORMAT_UNKNOWN:
                return {
                    "status": "FAILED",
                    "errors": [
                        f"Unknown ROM format: {result.reason}. "
                        "Supported: payload_ota, fastboot_tgz/tar, images_zip, "
                        "xiaomi_eu_zip, split_super_zip, new_dat_br_zip, raw_super_zip."
                    ],
                    "warnings": result.warnings,
                }

            codename_ok, codename_msg = check_codename_match(
                result.detected_device_codename, ctx.codename
            )
            errs = [] if codename_ok else [codename_msg]
            return {
                "status": "FAILED" if errs else "APPLIED",
                "rom_format": result.rom_format,
                "confidence": result.confidence,
                "detected_codename": result.detected_device_codename,
                "errors": errs,
                "warnings": result.warnings,
            }

        ok = _run("detect_rom", _detect, critical=True)
    else:
        ctx.stage_reports["detect_rom"] = {
            "status": "DRY_RUN" if not ctx.execute else "SKIPPED_NO_ROM",
            "warnings": [],
            "errors": [],
        }

    # ── Stage 2: Unpack ROM ───────────────────────────────────────────────────
    _notify("UNPACKING_ROM", "Edition: Free | Stage: Unpacking ROM")

    if ok and ctx.execute and ctx.rom_path and _detection is not None:
        from factory.input.rom_unpacker import unpack_rom

        def _do_unpack():
            nonlocal _unpack
            result = unpack_rom(ctx.rom_path, _detection.rom_format, work_dir)
            _unpack = result
            return result

        ok = _run("unpack_rom", _do_unpack, critical=True)
    elif not ctx.execute:
        ctx.stage_reports["unpack_rom"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ── Stage 3: Collect normal images ────────────────────────────────────────
    _notify("COLLECTING_IMAGES", "Edition: Free | Stage: Collecting Images")

    source_images_out = output_dir / "images" / "source"
    if ok and ctx.execute:
        from factory.images.source_image_collector import collect_source_images

        def _do_collect():
            nonlocal _collect
            # Search unpacked_rom/ plus images/ and firmware-update/ subdirs
            source_dirs = [work_dir / "source_images"]
            unpacked_dir = work_dir / "unpacked_rom"
            for sub in ["images", "firmware-update"]:
                candidate = unpacked_dir / sub
                if candidate.is_dir():
                    source_dirs.append(candidate)
            if unpacked_dir.is_dir():
                source_dirs.append(unpacked_dir)

            result = collect_source_images(
                source_dirs,
                source_images_out,
                soc=ctx.soc,
                execute=True,
            )
            _collect = result
            return result

        _run("collect_images", _do_collect)
    elif not ctx.execute:
        ctx.stage_reports["collect_images"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ── Stage 4: Collect dynamic partitions ───────────────────────────────────
    super_parts_dir = work_dir / "super_parts"
    if ok and ctx.execute:
        from factory.super.super_input_collector import collect_super_inputs

        def _do_super_input():
            nonlocal _super_input
            source_dirs = [work_dir / "source_images"]
            if source_images_out.is_dir():
                source_dirs.append(source_images_out)
            result = collect_super_inputs(
                source_dirs, super_parts_dir, reports_dir, execute=True
            )
            _super_input = result
            return result

        _run("super_inputs", _do_super_input)
    elif not ctx.execute:
        ctx.stage_reports["super_inputs"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ── Stage 5: Rebuild super.img ────────────────────────────────────────────
    _notify("BUILDING_SUPER", "Edition: Free | Stage: Building Super")

    final_img_dir = output_dir / "images" / "final"
    final_img_dir.mkdir(parents=True, exist_ok=True)
    super_img = final_img_dir / "super.img"

    if ok and ctx.execute:
        from factory.super.super_rebuilder import rebuild_super

        def _do_rebuild():
            # Prefer super.img from source_images/ (e.g. from split-super merge or raw super)
            original_super = None
            for candidate in [
                work_dir / "source_images" / "super.img",
                work_dir / "unpacked_rom" / "super.img",
            ]:
                if candidate.is_file():
                    original_super = candidate
                    break

            return rebuild_super(
                super_parts_dir=super_parts_dir,
                output_super=super_img,
                reports_dir=reports_dir,
                original_super_img=original_super,
                execute=True,
            )

        ok = _run("super_rebuild", _do_rebuild, critical=True)
    elif not ctx.execute:
        ctx.stage_reports["super_rebuild"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ── Stage 6: Assemble final images ────────────────────────────────────────
    if ok and ctx.execute:
        from factory.images.final_image_assembler import assemble_final_images, write_intake_report

        def _do_assemble():
            nonlocal _assemble
            result = assemble_final_images(
                super_img=super_img,
                source_images_dir=work_dir / "source_images",
                final_dir=final_img_dir,
                execute=True,
            )
            _assemble = result
            return result

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
                original_super_exists=(work_dir / "source_images" / "super.img").is_file(),
                split_super_merged=bool(_unpack and _unpack.get("split_super_merged")),
                super_rebuilt=ok,
                final_image_list=list(asm.get("final_images", [])),
                cleanup_status="PENDING",
            )
        except Exception as exc:
            print(f"[free_pipeline] Warning: could not write rom_intake_report.txt: {exc}")
    elif not ctx.execute:
        ctx.stage_reports["assemble_images"] = {"status": "DRY_RUN", "warnings": [], "errors": []}

    # ── Write free_build_report.txt ───────────────────────────────────────────
    _write_free_build_report(
        reports_dir=reports_dir,
        ctx=ctx,
        detection=_detection,
        collect=_collect,
        super_input=_super_input,
        assemble=_assemble,
        final_zip=ctx.final_zip,
        unpack=_unpack,
    )

    # ── Stage 7: Package fastboot ZIP ─────────────────────────────────────────
    _notify("PACKAGING_ZIP", "Edition: Free | Stage: Packaging Fastboot ZIP")

    if ok and ctx.execute:
        zip_mod = _import("factory.output.final_zip_legacy")
        if zip_mod and hasattr(zip_mod, "build_final_fastboot_zip"):
            def _do_zip():
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

    # Update free_build_report.txt with final ZIP path
    _write_free_build_report(
        reports_dir=reports_dir,
        ctx=ctx,
        detection=_detection,
        collect=_collect,
        super_input=_super_input,
        assemble=_assemble,
        final_zip=ctx.final_zip,
        unpack=_unpack,
    )

    # ── Stage 8: Upload PixelDrain ────────────────────────────────────────────
    if ok and ctx.execute and ctx.upload_pixeldrain and ctx.final_zip:
        _notify("UPLOADING_PIXELDRAIN", "Edition: Free | Stage: Uploading PixelDrain")
        pd_mod = _import("factory.upload.pixeldrain")
        if pd_mod and hasattr(pd_mod, "upload"):
            def _pd():
                return pd_mod.upload(ctx.final_zip, output_dir=output_dir)

            _run("pixeldrain_upload", _pd)
            ctx.pixeldrain_link = ctx.stage_reports.get("pixeldrain_upload", {}).get("link")

    # ── Stage 9: Cleanup ──────────────────────────────────────────────────────
    if ctx.execute:
        _notify("CLEANUP", "Edition: Free | Stage: Cleanup")
        from factory.cleanup.cleanup_workspace import cleanup

        def _do_cleanup():
            return cleanup(output_dir, keep_final_zip=not bool(ctx.pixeldrain_link))

        _run("cleanup", _do_cleanup)

    # ── Finalize Telegram ──────────────────────────────────────────────────────
    final_status = (
        "FAILED" if (ctx.errors and ctx.execute)
        else ("APPLIED" if ctx.execute else "DRY_RUN")
    )
    _duration = time.monotonic() - pipeline_start

    if notifier is not None:
        try:
            if final_status == "FAILED":
                first_error = ctx.errors[0][:300] if ctx.errors else None
                notifier.fail(
                    stage=notifier.current_stage,
                    error_summary=first_error,
                    duration=_duration,
                )
            else:
                zip_name = Path(ctx.final_zip).name if ctx.final_zip else None
                notifier.success(
                    final_zip_name=zip_name,
                    pixeldrain_link=ctx.pixeldrain_link,
                    duration=_duration,
                )
        except Exception as _tg_exc:
            print(f"[free_pipeline] Telegram finalize error: {_tg_exc}")

    # Export message_id for GitHub Actions handoff
    if notifier is not None and notifier.message_id is not None:
        _gha_env = os.environ.get("GITHUB_ENV", "")
        if _gha_env:
            try:
                with open(_gha_env, "a", encoding="utf-8") as _f:
                    _f.write(f"DEADZONE_TELEGRAM_MESSAGE_ID={notifier.message_id}\n")
            except Exception:
                pass

    # ── Write pipeline reports ────────────────────────────────────────────────
    from factory.pipeline.report import write_pipeline_report

    build_id       = notifier.build_id if notifier is not None else None
    telegram_section = notifier.report_section() if notifier is not None else None
    report_files   = write_pipeline_report(ctx, output_dir, telegram=telegram_section, build_id=build_id)
    _write_telegram_status(notifier, ctx.notify_telegram, soc or "", source, output_dir)

    print(f"[free_pipeline] final_status={final_status}")
    if ctx.errors:
        print(f"[free_pipeline] ERRORS ({len(ctx.errors)}):")
        for i, e in enumerate(ctx.errors, 1):
            print(f"  [{i}] {e}")
    if ctx.warnings:
        print(f"[free_pipeline] WARNINGS ({len(ctx.warnings)}):")
        for i, w in enumerate(ctx.warnings, 1):
            print(f"  [{i}] {w}")

    return {
        "final_status": final_status,
        "build_id": build_id,
        "build_name": ctx.build_name,
        "codename": ctx.codename,
        "edition": ctx.edition,
        "soc": ctx.soc,
        "final_zip": ctx.final_zip,
        "pixeldrain_link": ctx.pixeldrain_link,
        "telegram_message_id": notifier.message_id if notifier is not None else None,
        "warnings": ctx.warnings,
        "errors": ctx.errors,
        "stage_reports": ctx.stage_reports,
        "report_files": report_files,
    }
