"""DeadZone factory orchestrator — single entry point for the full build pipeline.

Flow
----
1.  Resolve device by codename (registry/device_groups + registry/devices)
2.  Resolve edition (registry/editions)
3.  Create BuildContext
4.  Download / unpack ROM
5.  Detect ROM metadata (build props)
6.  Apply base common layer
7.  Apply selected edition layer
8.  Repack changed partitions
9.  Build super from final patched state
10. Collect actual final images
11. Generate flash script from actual images
12. Build final ZIP
13. Validate final ZIP
14. Upload PixelDrain (if enabled)
15. Notify Telegram (if secrets exist)
16. Cleanup workspace

Editions only apply patches/assets.
Unpack / repack / super / output logic is never duplicated per edition.
"""
from __future__ import annotations

import importlib
import sys
import time
from pathlib import Path
from typing import Any, Optional

from factory.pipeline.context import BuildContext
from factory.pipeline.resolver import resolve_device, resolve_edition, resolve_super_size
from factory.pipeline.report import write_pipeline_report

_REPO_ROOT = Path(__file__).resolve().parents[2]


# ── Helpers ───────────────────────────────────────────────────────────────────

def _import(module: str) -> Any:
    try:
        return importlib.import_module(module)
    except ImportError:
        return None


def _run(ctx: BuildContext, stage_id: str, fn, *, critical: bool = False) -> bool:
    """Run one pipeline stage; return False if it failed and is critical."""
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

    status = str(
        report.get("final_status") or report.get("status") or "APPLIED"
    ).upper()
    duration = round(time.monotonic() - t0, 2)
    print(f"[orchestrator] {stage_id}: {status} ({duration}s)")

    if critical and status == "FAILED":
        return False
    return True


# ── Public API ────────────────────────────────────────────────────────────────

def run_factory(
    codename: str,
    edition: str,
    rom_url: Optional[str] = None,
    rom_path: Optional[Path] = None,
    project_dir: Optional[Path] = None,
    output_dir: Optional[Path] = None,
    mode: str = "dry_run",
    soc: Optional[str] = None,
    platform: Optional[str] = None,
    android_version: Optional[str] = None,
    mi_incremental: Optional[str] = None,
    vbmeta_mode: Optional[str] = None,
    upload_pixeldrain: bool = False,
    notify_telegram: bool = False,
    template_zip: Optional[Path] = None,
) -> dict:
    """Run the full DeadZone factory pipeline."""
    output_dir = (Path(output_dir) if output_dir else _REPO_ROOT / "output").resolve()

    # ── Step 1-3: Resolve and create context ─────────────────────────────────
    device_profile = resolve_device(codename, soc_hint=soc)
    edition_profile = resolve_edition(edition)
    resolved_soc = device_profile.get("soc") or soc or "unknown"
    super_size = resolve_super_size(device_profile, resolved_soc)

    ctx = BuildContext(
        codename=codename,
        edition=edition,
        rom_url=rom_url,
        mode=mode,
        soc=resolved_soc,
        platform=platform or device_profile.get("platform"),
        device_model=device_profile.get("model"),
        super_size=super_size,
        rom_path=Path(rom_path).resolve() if rom_path else None,
        project_dir=Path(project_dir).resolve() if project_dir else None,
        output_dir=output_dir,
        images_dir=output_dir / "images",
        final_dir=output_dir / "final",
        android_version=android_version,
        mi_incremental=mi_incremental,
        upload_pixeldrain=upload_pixeldrain,
        notify_telegram=notify_telegram,
    )

    if device_profile.get("_warning"):
        ctx.warnings.append(device_profile["_warning"])
    if edition_profile.get("_warning"):
        ctx.warnings.append(edition_profile["_warning"])

    ok = True

    # ── Step 4: Download / unpack ROM ─────────────────────────────────────────
    if ctx.execute and ctx.rom_path and ctx.project_dir is None:
        unpack_mod = _import("factory.unpack.pipeline")
        if unpack_mod and hasattr(unpack_mod, "UnpackPipeline"):
            def _unpack():
                nonlocal ctx
                pipe = unpack_mod.UnpackPipeline(
                    ctx.rom_path,
                    factory_device=ctx.codename,
                    soc=ctx.soc,
                    platform=ctx.platform,
                    output_root=ctx.output_dir,
                )
                unpack_ctx = pipe.run()
                ctx.project_dir = unpack_ctx.project_dir
                ctx.android_version = ctx.android_version or unpack_ctx.android_version
                ctx.mi_incremental = ctx.mi_incremental or unpack_ctx.mi_version
                return {
                    "status": "APPLIED" if not unpack_ctx.errors else "FAILED",
                    "warnings": list(unpack_ctx.warnings),
                    "errors": list(unpack_ctx.errors),
                }
            ok = _run(ctx, "unpack", _unpack, critical=True)
        else:
            ctx.errors.append("unpack pipeline module missing")
            ok = False

    if ok and ctx.project_dir is None:
        ctx.errors.append("project_dir is required (no execute-mode unpack result)")
        ok = False

    if ok:
        ctx.project_dir = Path(ctx.project_dir).resolve()

    # ── Step 6: Base common layer ─────────────────────────────────────────────
    if ok:
        def _common():
            from factory.patch.common_rom.project_legacy import (
                _write_reports, apply_common_project_legacy_patches,
            )
            r = apply_common_project_legacy_patches(
                project_dir=ctx.project_dir,
                root_dir=_REPO_ROOT,
                flavor=f"deadzone_{edition}" if edition != "base" else "deadzone",
                execute=ctx.execute,
            )
            _write_reports(r)
            return r
        ok = _run(ctx, "common_layer", _common)

    # ── Step 7: Edition layer ─────────────────────────────────────────────────
    if ok:
        runner_module = edition_profile.get("runner", f"factory.patch.editions.{edition}.runner")
        edition_mod = _import(runner_module)
        if edition_mod and hasattr(edition_mod, "run_edition"):
            def _edition():
                return edition_mod.run_edition(
                    root=ctx.project_dir,
                    output_dir=ctx.output_dir,
                    context={
                        "flavor": edition,
                        "execute": ctx.execute,
                        "android_major": _android_major(ctx.android_version),
                        "os_family": _os_family(ctx.mi_incremental),
                    },
                )
            ok = _run(ctx, f"edition_{edition}", _edition)
        else:
            ctx.warnings.append(f"Edition runner not found: {runner_module} — skipped")

    # ── Steps 8-9: Repack + super ─────────────────────────────────────────────
    if ok and ctx.execute:
        erofs_mod = _import("factory.repack.pipeline_erofs_legacy")
        if erofs_mod and hasattr(erofs_mod, "apply_erofs_repack_legacy_stage"):
            staging = ctx.output_dir / "work" / "super_partitions"
            def _erofs():
                return erofs_mod.apply_erofs_repack_legacy_stage(
                    project_dir=ctx.project_dir,
                    images_dir=ctx.images_dir,
                    staging_dir=staging,
                    flavor=edition,
                    execute=True,
                )
            ok = _run(ctx, "erofs_repack", _erofs, critical=True)

        if ok:
            super_mod = _import("factory.repack.pipeline_super_legacy")
            if super_mod and hasattr(super_mod, "apply_super_build_legacy_stage"):
                def _super():
                    return super_mod.apply_super_build_legacy_stage(
                        project_dir=ctx.project_dir,
                        images_dir=ctx.images_dir,
                        output_super=ctx.images_dir / "super.img",
                        partition_staging_dir=staging,
                        flavor=edition,
                        device=ctx.codename,
                        soc=ctx.soc,
                        platform=ctx.platform,
                        execute=True,
                    )
                ok = _run(ctx, "super_build", _super, critical=True)

    # ── Step 10: Collect images ───────────────────────────────────────────────
    if ok and ctx.execute and ctx.soc == "mtk":
        mtk_mod = _import("factory.images.mtk_firmware_collector_legacy")
        if mtk_mod and hasattr(mtk_mod, "collect_mtk_firmware_images_legacy"):
            def _mtk():
                return mtk_mod.collect_mtk_firmware_images_legacy(
                    project_dir=ctx.project_dir,
                    output_dir=ctx.output_dir,
                    images_dir=ctx.images_dir,
                    device=ctx.codename,
                    soc=ctx.soc,
                    execute=True,
                )
            ok = _run(ctx, "mtk_firmware", _mtk, critical=True)

    # ── Steps 11-12: Flash scripts + final ZIP ────────────────────────────────
    if ok:
        zip_mod = _import("factory.output.final_zip_legacy")
        if zip_mod and hasattr(zip_mod, "build_final_fastboot_zip"):
            def _zip():
                from factory.pipeline.resolver import _load_yaml_simple
                model = ctx.device_model
                if not model:
                    for soc_sub in ["mtk", "snapdragon"]:
                        dev_f = _REPO_ROOT / "registry" / "devices" / soc_sub / f"{ctx.codename}.yml"
                        if dev_f.is_file():
                            model = _load_yaml_simple(dev_f).get("model")
                            break
                return zip_mod.build_final_fastboot_zip(
                    images_dir=ctx.images_dir,
                    output_dir=ctx.final_dir,
                    build_name=ctx.build_name,
                    device=ctx.codename,
                    flavor=f"deadzone_{edition}" if edition != "base" else "deadzone",
                    soc=ctx.soc,
                    platform=ctx.platform,
                    template_zip=template_zip,
                    device_model=model,
                    android_version=ctx.android_version,
                    build_incremental=ctx.mi_incremental,
                    execute=ctx.execute,
                )
            r_ok = _run(ctx, "final_zip", _zip, critical=True)
            fz = ctx.stage_reports.get("final_zip", {})
            ctx.final_zip = fz.get("final_zip")
            ok = r_ok

    # ── Step 14: Upload PixelDrain ────────────────────────────────────────────
    if ok and ctx.execute and ctx.upload_pixeldrain and ctx.final_zip:
        pd_mod = _import("factory.upload.pixeldrain")
        if pd_mod and hasattr(pd_mod, "upload"):
            def _pd():
                return pd_mod.upload(ctx.final_zip, output_dir=ctx.output_dir)
            _run(ctx, "pixeldrain_upload", _pd)
            ctx.pixeldrain_link = ctx.stage_reports.get("pixeldrain_upload", {}).get("link")

    # ── Step 15: Telegram ─────────────────────────────────────────────────────
    if ctx.notify_telegram:
        tg_mod = _import("factory.notify.telegram_live")
        if tg_mod:
            pass  # TelegramLiveStatus is wired in the orchestrating workflow

    # ── Step 16: Cleanup ─────────────────────────────────────────────────────
    if ctx.execute:
        cleanup_mod = _import("factory.cleanup.cleanup_workspace")
        if cleanup_mod and hasattr(cleanup_mod, "cleanup"):
            def _cleanup():
                return cleanup_mod.cleanup(
                    output_dir=ctx.output_dir,
                    keep_final_zip=not bool(ctx.pixeldrain_link),
                )
            _run(ctx, "cleanup", _cleanup)

    # ── Write reports ─────────────────────────────────────────────────────────
    report_files = write_pipeline_report(ctx, ctx.output_dir)

    final_status = "FAILED" if (ctx.errors and ctx.execute) else ("APPLIED" if ctx.execute else "DRY_RUN")
    print(f"[orchestrator] final_status={final_status}")

    return {
        "final_status": final_status,
        "build_name": ctx.build_name,
        "codename": ctx.codename,
        "edition": ctx.edition,
        "soc": ctx.soc,
        "final_zip": ctx.final_zip,
        "pixeldrain_link": ctx.pixeldrain_link,
        "warnings": ctx.warnings,
        "errors": ctx.errors,
        "stage_reports": ctx.stage_reports,
        "report_files": report_files,
    }


def _android_major(android_version: Optional[str]) -> Optional[int]:
    if not android_version:
        return None
    digits = "".join(c for c in str(android_version) if c.isdigit())
    return int(digits) if digits else None


def _os_family(incremental: Optional[str]) -> str:
    if not incremental:
        return "OS3"
    inc = incremental.upper()
    if "OS3" in inc:
        return "OS3"
    if "OS2" in inc:
        return "OS2"
    if "OS1" in inc:
        return "OS1"
    return "OS3"


# ── CLI ───────────────────────────────────────────────────────────────────────

def _parser():
    import argparse
    p = argparse.ArgumentParser(description="DeadZone factory orchestrator")
    p.add_argument("--codename", required=True)
    p.add_argument("--edition", default="base")
    p.add_argument("--rom-url", dest="rom_url", default=None)
    p.add_argument("--rom", type=Path, default=None)
    p.add_argument("--project", type=Path, default=None)
    p.add_argument("--output-dir", type=Path, default=None)
    p.add_argument("--mode", choices=["dry_run", "execute"], default="dry_run")
    p.add_argument("--soc", default=None)
    p.add_argument("--platform", default=None)
    p.add_argument("--android-version", dest="android_version", default=None)
    p.add_argument("--mi-version", dest="mi_version", default=None)
    p.add_argument("--vbmeta-mode", dest="vbmeta_mode", default=None)
    p.add_argument("--template-zip", type=Path, default=None)
    p.add_argument("--upload-pixeldrain", dest="upload_pixeldrain", action="store_true")
    p.add_argument("--notify-telegram", dest="notify_telegram", action="store_true")
    return p


def main(argv=None) -> int:
    args = _parser().parse_args(argv)
    result = run_factory(
        codename=args.codename,
        edition=args.edition,
        rom_url=args.rom_url,
        rom_path=args.rom,
        project_dir=args.project,
        output_dir=args.output_dir,
        mode=args.mode,
        soc=args.soc,
        platform=args.platform,
        android_version=args.android_version,
        mi_incremental=args.mi_version,
        vbmeta_mode=args.vbmeta_mode,
        upload_pixeldrain=args.upload_pixeldrain,
        notify_telegram=args.notify_telegram,
        template_zip=args.template_zip,
    )
    return 0 if result.get("final_status") in {"DRY_RUN", "APPLIED"} else 1


if __name__ == "__main__":
    sys.exit(main())
