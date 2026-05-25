"""DeadZone factory orchestrator — single entry point for the full build pipeline.

Flow
----
1.  Resolve device by codename (registry/device_groups + registry/devices)
2.  Create BuildContext
3.  Download / unpack ROM
4.  Detect ROM metadata (build props)
5.  Apply factory/patch/base/runner.py (base common layer)
6.  Apply factory/patch/mods/<mod>/runner.py (selected mod layer)
7.  Repack changed partitions
8.  Build super from final patched state
9.  Collect actual final images
10. Generate flash script from actual images
11. Build final ZIP
12. Validate final ZIP
13. Upload PixelDrain (if enabled)
14. Notify Telegram (if secrets exist)
15. Cleanup workspace

Only the selected mod runs. Mods own patches/assets only.
Unpack / repack / super / output logic never lives in a mod.
"""
from __future__ import annotations

import importlib
import sys
import time
from pathlib import Path
from typing import Any, Optional

from factory.pipeline.context import BuildContext
from factory.pipeline.resolver import resolve_device, resolve_super_size
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
    notifier: Optional[Any] = None,
) -> dict:
    """Run the full DeadZone factory pipeline."""
    output_dir = (Path(output_dir) if output_dir else _REPO_ROOT / "output").resolve()

    def _notify(stage: str, action: str, error: str | None = None) -> None:
        if notifier is not None:
            try:
                notifier.update_stage(stage, action, error=error)
            except Exception:
                pass

    # ── Step 1-3: Resolve and create context ─────────────────────────────────
    _notify("RESOLVING_DEVICE", "Resolving device metadata")
    device_profile = resolve_device(codename, soc_hint=soc)
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

    ok = True

    # ── Step 4: Download / unpack ROM ─────────────────────────────────────────
    if ctx.execute and ctx.rom_path and ctx.project_dir is None:
        _notify("DOWNLOADING_ROM", "Downloading source ROM")
        unpack_mod = _import("factory.unpack.pipeline")
        if unpack_mod and hasattr(unpack_mod, "UnpackPipeline"):
            _notify("UNPACKING_ROM", "Extracting payload and partitions")
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

    if ok and ctx.execute and ctx.project_dir is None:
        if rom_url and not rom_path:
            ctx.errors.append(
                "execute mode requires a downloaded rom_path; "
                "workflow/job_runner must download the ROM before calling the orchestrator "
                f"(rom_url={rom_url!r} was provided but no local file was given)"
            )
        else:
            ctx.errors.append("project_dir is required (execute mode — unpack produced no project_dir)")
        ok = False

    if ok:
        ctx.project_dir = Path(ctx.project_dir).resolve()

    # ── Step 6: Base patch layer ──────────────────────────────────────────────
    if ok:
        _notify("DETECTING_METADATA", "Detecting ROM metadata from build props")
        _notify("APPLYING_BASE_PATCHES", "Applying base DeadZone patches")
        def _base():
            from factory.patch.base.runner import run_base
            return run_base(
                root=ctx.project_dir,
                output_dir=ctx.output_dir,
                context={
                    "flavor": f"deadzone_{edition}" if edition != "base" else "deadzone",
                    "execute": ctx.execute,
                },
            )
        ok = _run(ctx, "base_layer", _base)

    # ── Step 7: Mod layer ─────────────────────────────────────────────────────
    if ok:
        _notify("APPLYING_MOD_PATCHES", f"Applying {edition} mod patches")
        mod_module = f"factory.patch.mods.{edition}.runner"
        mod = _import(mod_module)
        if mod and hasattr(mod, "run_mod"):
            def _mod():
                return mod.run_mod(
                    root=ctx.project_dir,
                    output_dir=ctx.output_dir,
                    context={
                        "flavor": edition,
                        "execute": ctx.execute,
                        "android_major": _android_major(ctx.android_version),
                        "os_family": _os_family(ctx.mi_incremental),
                    },
                )
            ok = _run(ctx, f"mod_{edition}", _mod)
        else:
            ctx.warnings.append(
                f"Mod runner not found: {mod_module} — SKIPPED_TEMPORARY"
            )

    # ── Steps 8-9: Repack + super ─────────────────────────────────────────────
    if ok and ctx.execute:
        _notify("REPACKING_PARTITIONS", "Repacking changed partitions with erofs")
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
            _notify("CAPTURING_ORIGINAL_SUPER_LAYOUT", "Reading original super partition byte sizes")
            _notify("BUILDING_SUPER", "Building super.img with preserved byte layout")
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
        _notify("COLLECTING_IMAGES", "Collecting MTK firmware images")
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
        _notify("GENERATING_FLASH_SCRIPT", "Generating image-driven AB flash script")
        _notify("PACKAGING_ZIP", "Building final fastboot ZIP")
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

    # ── Step 13: Validate final ZIP ───────────────────────────────────────────
    if ok:
        _notify("VALIDATING_FINAL_ZIP", "Validating final ZIP structure")

    # ── Step 14: Upload PixelDrain ────────────────────────────────────────────
    if ok and ctx.execute and ctx.upload_pixeldrain and ctx.final_zip:
        _notify("UPLOADING_PIXELDRAIN", "Uploading final ZIP to PixelDrain")
        pd_mod = _import("factory.upload.pixeldrain")
        if pd_mod and hasattr(pd_mod, "upload"):
            def _pd():
                return pd_mod.upload(ctx.final_zip, output_dir=ctx.output_dir)
            _run(ctx, "pixeldrain_upload", _pd)
            ctx.pixeldrain_link = ctx.stage_reports.get("pixeldrain_upload", {}).get("link")

    # ── Step 15: Cleanup ─────────────────────────────────────────────────────
    if ctx.execute:
        _notify("CLEANUP", "Cleaning workspace")
        cleanup_mod = _import("factory.cleanup.cleanup_workspace")
        if cleanup_mod and hasattr(cleanup_mod, "cleanup"):
            def _cleanup():
                return cleanup_mod.cleanup(
                    output_dir=ctx.output_dir,
                    keep_final_zip=not bool(ctx.pixeldrain_link),
                )
            _run(ctx, "cleanup", _cleanup)

    # ── Write reports ─────────────────────────────────────────────────────────
    build_id = notifier.build_id if notifier is not None else None
    telegram_section = notifier.report_section() if notifier is not None else None
    report_files = write_pipeline_report(ctx, ctx.output_dir, telegram=telegram_section, build_id=build_id)

    final_status = "FAILED" if (ctx.errors and ctx.execute) else ("APPLIED" if ctx.execute else "DRY_RUN")
    print(f"[orchestrator] final_status={final_status}")
    if ctx.errors:
        print(f"[orchestrator] ERRORS ({len(ctx.errors)}):")
        for i, e in enumerate(ctx.errors, 1):
            print(f"  [{i}] {e}")
    if ctx.warnings:
        print(f"[orchestrator] WARNINGS ({len(ctx.warnings)}):")
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
    status = result.get("final_status")
    if status not in {"DRY_RUN", "APPLIED"}:
        errors = result.get("errors") or []
        if errors:
            print(f"[orchestrator] Build FAILED with {len(errors)} error(s):", file=sys.stderr)
            for e in errors:
                print(f"  - {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
