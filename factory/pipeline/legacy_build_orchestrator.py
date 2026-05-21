"""Central orchestrator for the legacy DeadZone build pipeline."""
from __future__ import annotations

import argparse
import importlib
import sys
import time
from pathlib import Path
from typing import Any, Callable

from factory.notify.telegram_live import TelegramLiveStatus
from factory.pipeline.pipeline_report import write_legacy_build_pipeline_report


_REPO_ROOT = Path(__file__).resolve().parents[2]
_LEGEND_FLAVORS = {"legend", "deadzone_legend"}


def _is_legend(flavor: str) -> bool:
    return flavor.lower().replace("-", "_") in _LEGEND_FLAVORS


def _clean_status(value: object) -> str:
    return str(value or "").upper()


def _report_path(report: dict) -> str | None:
    files = report.get("report_files")
    if isinstance(files, dict):
        return files.get("json") or files.get("txt")
    if isinstance(files, (list, tuple)) and files:
        return str(files[0])
    return None


def _warnings(report: dict) -> list:
    warnings = report.get("warnings") or []
    return warnings if isinstance(warnings, list) else [warnings]


def _errors(report: dict) -> list:
    errors = report.get("errors") or []
    return errors if isinstance(errors, list) else [errors]


def _stage_status(report: dict, execute: bool) -> str:
    status = _clean_status(
        report.get("final_status")
        or report.get("status")
        or report.get("validation_status")
    )
    if status.startswith("SKIPPED"):
        return "SKIP"
    if status in {"APPLIED", "DRY_RUN", "PASSED", "OK", "SUCCESS", "PATCHED", "WOULD_PATCH"}:
        return "OK"
    if status == "FAILED" or _errors(report):
        return "FAIL"
    return "OK" if not execute else "FAIL"


def _known_report_path(stage_id: str, output_dir: Path) -> str | None:
    candidates = {
        "common_rom_patches": _REPO_ROOT / "output" / "reports" / "03_common_rom_legacy_report.json",
        "legend_jar": _REPO_ROOT / "output" / "reports" / "03_legend_jar_patch_report.json",
        "provision_apk": _REPO_ROOT / "output" / "reports" / "09_provision_apk_legacy_report.json",
        "powerkeeper_legend": _REPO_ROOT / "output" / "reports" / "legend_powerkeeper_report.json",
        "images_vbmeta": output_dir / "reports" / "12_images_vbmeta_legacy_report.json",
        "erofs_repack": _REPO_ROOT / "output" / "reports" / "13_erofs_repack_legacy_report.json",
        "super_build": _REPO_ROOT / "output" / "reports" / "14_super_build_legacy_report.json",
        "mtk_firmware": output_dir / "reports" / "mtk_firmware_image_collection_report.json",
        "final_zip": output_dir / "reports" / "15_final_fastboot_zip_report.json",
    }
    path = candidates.get(stage_id)
    if path is not None and path.exists():
        return str(path)
    return None


def _stage_record(stage_id: str, name: str, critical: bool = False) -> dict:
    return {
        "id": stage_id,
        "name": name,
        "status": "WAIT",
        "critical": critical,
        "duration_seconds": 0.0,
        "reason": None,
        "report_path": None,
        "warnings": [],
        "errors": [],
        "raw_status": None,
    }


def _skip_stage(stage: dict, reason: str) -> dict:
    stage["status"] = "SKIP"
    stage["reason"] = reason
    stage["raw_status"] = "SKIPPED"
    return {
        "stage": stage["id"],
        "status": "SKIPPED",
        "final_status": "SKIPPED",
        "warnings": [reason],
        "errors": [],
    }


def _workspace_images_size_mib(images_dir: Path) -> float | None:
    """Return total size of output/images in MiB, or None on error."""
    try:
        total = sum(f.stat().st_size for f in images_dir.rglob("*") if f.is_file())
        return round(total / (1024 * 1024), 1)
    except Exception:
        return None



def _run_stage(
    stage: dict,
    stages: list[dict],
    live: TelegramLiveStatus,
    callable_: Callable[[], dict],
    *,
    execute: bool,
    fail_on_skip: bool = False,
) -> tuple[dict, bool]:
    stage["status"] = "RUN"
    live.update(stages, current=stage["name"])
    started = time.monotonic()
    failed = False
    try:
        report = callable_()
        if not isinstance(report, dict):
            report = {"status": "APPLIED", "result": str(report), "warnings": [], "errors": []}
    except Exception as exc:
        report = {"status": "FAILED", "final_status": "FAILED", "warnings": [], "errors": [str(exc)]}
    stage["duration_seconds"] = round(time.monotonic() - started, 3)
    stage["warnings"] = _warnings(report)
    stage["errors"] = _errors(report)
    stage["report_path"] = _report_path(report)
    stage["raw_status"] = report.get("final_status") or report.get("status")
    stage["status"] = _stage_status(report, execute)
    if execute and (stage["status"] == "FAIL" or (fail_on_skip and stage["status"] == "SKIP")):
        failed = True
        if stage["status"] == "SKIP":
            stage["status"] = "FAIL"
            stage["errors"].append("Required stage was skipped in execute mode")
    live.update(stages, current=stage["name"], final_status="FAILED" if failed else "RUNNING")
    return report, failed


def _import_optional(module_name: str) -> Any | None:
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def _android_major(android_version: str | None) -> int | None:
    if not android_version:
        return None
    digits = "".join(ch for ch in str(android_version) if ch.isdigit())
    return int(digits) if digits else None


def apply_legacy_build_pipeline(
    rom_path: Path | None = None,
    project_dir: Path | None = None,
    output_dir: Path | None = None,
    build_name: str = "DeadZone_v1",
    device: str | None = None,
    soc: str | None = None,
    platform: str | None = None,
    flavor: str = "legend",
    android_version: str | None = None,
    mi_incremental: str | None = None,
    vbmeta_mode: str | int | None = None,
    template_zip: Path | None = None,
    execute: bool = False,
    telegram: bool = False,
) -> dict:
    output_dir = (Path(output_dir) if output_dir is not None else (_REPO_ROOT / "output")).resolve()
    images_dir = output_dir / "images"
    # MEZOBuildRom-style: dynamic partition EROFS images land in this temporary
    # directory, never in output/images/.  Super build reads from here, writes
    # super.img to output/images/super.img, then deletes this dir on success.
    partition_staging_dir = output_dir / "work" / "super_partitions"
    final_output_dir = output_dir / "final"
    final_zip: str | None = None
    warnings: list[str] = []
    errors: list[str] = []
    stage_reports: dict[str, dict] = {}

    stages = [
        _stage_record("unpack", "Unpack", critical=bool(rom_path)),
        _stage_record("common_rom_patches", "Common ROM patches"),
        _stage_record("common_rom_assets", "Common ROM assets"),
        _stage_record("legend_jar", "Legend JAR"),
        _stage_record("provision_apk", "Provision APK"),
        _stage_record("systemui_legend", "MiuiSystemUI APK"),
        _stage_record("powerkeeper_legend", "PowerKeeper APK"),
        _stage_record("images_vbmeta", "Images + vbmeta", critical=True),
        _stage_record("erofs_repack", "EROFS repack", critical=True),
        _stage_record("super_build", "Super build", critical=True),
        _stage_record("mtk_firmware", "MTK firmware images", critical=True),
        _stage_record("final_zip", "Final ZIP", critical=True),
    ]

    live = TelegramLiveStatus(
        enabled=telegram,
        build_name=build_name,
        device=device or "unknown",
        flavor=flavor,
        platform=platform,
    )
    telegram_state = live.start(stages)

    def stop_if_needed(stage: dict, failed: bool) -> bool:
        if failed:
            errors.extend(stage.get("errors") or [f"{stage['name']} failed"])
            return True
        warnings.extend(stage.get("warnings") or [])
        errors.extend(stage.get("errors") or [])
        return False

    stopped = False

    unpack_stage = stages[0]
    if project_dir is not None:
        stage_reports["unpack"] = _skip_stage(unpack_stage, "existing project provided")
        live.update(stages, current=unpack_stage["name"])
    elif rom_path is None:
        stage_reports["unpack"] = _skip_stage(unpack_stage, "no ROM path provided")
        live.update(stages, current=unpack_stage["name"])
    elif not execute:
        stage_reports["unpack"] = _skip_stage(unpack_stage, "dry-run does not unpack ROM")
        live.update(stages, current=unpack_stage["name"])
    else:
        unpack_mod = _import_optional("factory.unpack.pipeline")
        if unpack_mod is None or not hasattr(unpack_mod, "UnpackPipeline"):
            stage_reports["unpack"] = {"status": "FAILED", "errors": ["unpack pipeline module missing"]}
            unpack_stage["status"] = "FAIL"
            unpack_stage["errors"] = ["unpack pipeline module missing"]
            stopped = True
        else:
            def run_unpack() -> dict:
                nonlocal project_dir, android_version, mi_incremental, device
                pipeline = unpack_mod.UnpackPipeline(
                    Path(rom_path),
                    factory_device=device,
                    soc=soc,
                    platform=platform,
                    output_root=output_dir,
                )
                ctx = pipeline.run()
                project_dir = ctx.project_dir
                android_version = android_version or ctx.android_version
                mi_incremental = mi_incremental or ctx.mi_version
                device = device or ctx.effective_device
                return {
                    "status": "APPLIED" if not ctx.errors else "FAILED",
                    "project_dir": str(ctx.project_dir),
                    "warnings": list(ctx.warnings),
                    "errors": list(ctx.errors),
                }

            report, failed = _run_stage(unpack_stage, stages, live, run_unpack, execute=execute)
            stage_reports["unpack"] = report
            stopped = stop_if_needed(unpack_stage, failed)

    if project_dir is None:
        stopped = True
        errors.append("Project directory is required when no execute-mode unpack result is available")
    else:
        project_dir = Path(project_dir).resolve()

    stage_plan: list[tuple[int, Callable[[], tuple[dict, bool]]]] = []

    if not stopped:
        common_stage = stages[1]

        def common_call() -> dict:
            from factory.patch.common_rom.project_legacy import (
                _write_reports,
                apply_common_project_legacy_patches,
            )
            report = apply_common_project_legacy_patches(
                project_dir=project_dir,
                root_dir=_REPO_ROOT,
                mi_incremental=mi_incremental,
                flavor=flavor,
                execute=execute,
            )
            _write_reports(report)
            return report

        report, failed = _run_stage(common_stage, stages, live, common_call, execute=execute)
        stage_reports[common_stage["id"]] = report
        stopped = stop_if_needed(common_stage, failed)

    if not stopped:
        assets_stage = stages[2]
        assets_mod = _import_optional("factory.patch.common_rom.assets_legacy")
        if assets_mod is None or not hasattr(assets_mod, "apply_common_rom_assets_legacy"):
            stage_reports[assets_stage["id"]] = _skip_stage(assets_stage, "missing module")
            live.update(stages, current=assets_stage["name"])
        else:
            def assets_call() -> dict:
                return assets_mod.apply_common_rom_assets_legacy(
                    project_dir=project_dir,
                    flavor=flavor,
                    execute=execute,
                )

            report, failed = _run_stage(assets_stage, stages, live, assets_call, execute=execute)
            stage_reports[assets_stage["id"]] = report
            stopped = stop_if_needed(assets_stage, failed)

    if not stopped:
        jar_stage = stages[3]
        if not _is_legend(flavor):
            stage_reports[jar_stage["id"]] = _skip_stage(jar_stage, "non-Legend flavor")
            live.update(stages, current=jar_stage["name"])
        else:
            # Prefer the modular MTCR runner; fall back to legacy LegendJarPatcher.
            mtcr_runner = _import_optional("factory.patch.legend.mtcr.runner")
            if mtcr_runner is not None and hasattr(mtcr_runner, "apply_legend_mtcr_patches"):
                def jar_call() -> dict:
                    return mtcr_runner.apply_legend_mtcr_patches(
                        project_dir=project_dir,
                        flavor=flavor,
                        execute=execute,
                    )

                report, failed = _run_stage(jar_stage, stages, live, jar_call, execute=execute)
                stage_reports[jar_stage["id"]] = report
                stopped = stop_if_needed(jar_stage, failed)
            else:
                jar_mod = _import_optional("factory.patch.legend.jar_patch")
                if jar_mod is None or not hasattr(jar_mod, "LegendJarPatcher"):
                    stage_reports[jar_stage["id"]] = {"status": "FAILED", "errors": ["Legend JAR module missing"]}
                    jar_stage["status"] = "FAIL"
                    jar_stage["errors"] = ["Legend JAR module missing"]
                    live.update(stages, current=jar_stage["name"], final_status="FAILED")
                    stopped = execute
                else:
                    def jar_call() -> dict:  # type: ignore[misc]
                        from factory.patch.common.patch_report import session_to_dict
                        patcher = jar_mod.LegendJarPatcher(
                            project_dir,
                            flavor=flavor,
                            android_major=_android_major(android_version),
                            dry_run=not execute,
                        )
                        return session_to_dict(patcher.run())

                    report, failed = _run_stage(jar_stage, stages, live, jar_call, execute=execute)
                    stage_reports[jar_stage["id"]] = report
                    stopped = stop_if_needed(jar_stage, failed)

    if not stopped:
        provision_stage = stages[4]

        def provision_call() -> dict:
            from factory.patch.apk.provision_legacy import _write_reports, apply_provision_legacy_patch
            report = apply_provision_legacy_patch(
                project_dir=project_dir,
                flavor=flavor,
                execute=execute,
            )
            _write_reports(report)
            return report

        report, failed = _run_stage(
            provision_stage,
            stages,
            live,
            provision_call,
            execute=execute,
            fail_on_skip=True,
        )
        stage_reports[provision_stage["id"]] = report
        stopped = stop_if_needed(provision_stage, failed)

    if not stopped:
        systemui_stage = stages[5]
        if not _is_legend(flavor):
            stage_reports[systemui_stage["id"]] = _skip_stage(systemui_stage, "non-Legend flavor")
            live.update(stages, current=systemui_stage["name"])
        else:
            systemui_mod = _import_optional("factory.patch.apk.systemui_legend")
            if systemui_mod is None or not hasattr(systemui_mod, "apply_legend_systemui_patch"):
                stage_reports[systemui_stage["id"]] = _skip_stage(systemui_stage, "missing module")
                live.update(stages, current=systemui_stage["name"])
            else:
                def systemui_call() -> dict:
                    return systemui_mod.apply_legend_systemui_patch(
                        project_dir=project_dir,
                        flavor=flavor,
                        execute=execute,
                    )

                report, failed = _run_stage(systemui_stage, stages, live, systemui_call, execute=execute)
                stage_reports[systemui_stage["id"]] = report
                stopped = stop_if_needed(systemui_stage, failed)

    if not stopped:
        powerkeeper_stage = stages[6]
        if not _is_legend(flavor):
            stage_reports[powerkeeper_stage["id"]] = _skip_stage(powerkeeper_stage, "non-Legend flavor")
            live.update(stages, current=powerkeeper_stage["name"])
        else:
            powerkeeper_mod = _import_optional("factory.patch.apk.powerkeeper_legend")
            if powerkeeper_mod is None or not hasattr(powerkeeper_mod, "apply_legend_powerkeeper_patch"):
                stage_reports[powerkeeper_stage["id"]] = _skip_stage(powerkeeper_stage, "missing module")
                live.update(stages, current=powerkeeper_stage["name"])
            else:
                def powerkeeper_call() -> dict:
                    return powerkeeper_mod.apply_legend_powerkeeper_patch(
                        project_dir=project_dir,
                        flavor=flavor,
                        execute=execute,
                    )

                report, failed = _run_stage(powerkeeper_stage, stages, live, powerkeeper_call, execute=execute)
                stage_reports[powerkeeper_stage["id"]] = report
                stopped = stop_if_needed(powerkeeper_stage, failed)

    if not stopped:
        images_stage = stages[7]

        def images_call() -> dict:
            from factory.images.pipeline_legacy import apply_images_vbmeta_legacy_stage
            return apply_images_vbmeta_legacy_stage(
                project_dir=project_dir,
                output_dir=output_dir,
                images_dir=images_dir,
                partition_staging_dir=partition_staging_dir,
                flavor=flavor,
                device=device,
                soc=soc,
                platform=platform,
                android_version=android_version,
                mi_incremental=mi_incremental,
                vbmeta_mode=vbmeta_mode,
                execute=execute,
            )

        report, failed = _run_stage(images_stage, stages, live, images_call, execute=execute)
        stage_reports[images_stage["id"]] = report
        stopped = stop_if_needed(images_stage, failed)

    if not stopped:
        erofs_stage = stages[8]

        def erofs_call() -> dict:
            from factory.repack.pipeline_erofs_legacy import apply_erofs_repack_legacy_stage
            return apply_erofs_repack_legacy_stage(
                project_dir=project_dir,
                images_dir=images_dir,
                staging_dir=partition_staging_dir,
                flavor=flavor,
                execute=execute,
            )

        report, failed = _run_stage(erofs_stage, stages, live, erofs_call, execute=execute)
        stage_reports[erofs_stage["id"]] = report
        stopped = stop_if_needed(erofs_stage, failed)

    if not stopped:
        super_stage = stages[9]

        def super_call() -> dict:
            from factory.repack.pipeline_super_legacy import apply_super_build_legacy_stage
            return apply_super_build_legacy_stage(
                project_dir=project_dir,
                images_dir=images_dir,
                output_super=images_dir / "super.img",
                partition_staging_dir=partition_staging_dir,
                flavor=flavor,
                device=device,
                soc=soc,
                platform=platform,
                execute=execute,
            )

        report, failed = _run_stage(super_stage, stages, live, super_call, execute=execute)
        stage_reports[super_stage["id"]] = report
        stopped = stop_if_needed(super_stage, failed)

    # ── Post-super-build: measure final images workspace ─────────────────────
    # The partition staging dir (output/work/super_partitions/) has already
    # been deleted by pipeline_super_legacy.py after super.img validation.
    # output/images/ now contains only super.img + standalone images, matching
    # MEZOBuildRom's images_output_dir layout.
    super_img_validated: bool = (
        stage_reports.get("super_build", {}).get("validation_status") == "PASSED"
    )
    workspace_images_size_mib: float | None = None

    if not stopped and images_dir.is_dir():
        workspace_images_size_mib = _workspace_images_size_mib(images_dir)
        if workspace_images_size_mib is not None:
            print(
                f"[legacy_pipeline] workspace_images_size_before_final_packaging="
                f"{workspace_images_size_mib} MiB"
            )
        print(f"[legacy_pipeline] super_img_validated={super_img_validated}")
        print(f"[legacy_pipeline] partition_staging_dir={partition_staging_dir}")

    if not stopped:
        mtk_stage = stages[10]
        if str(soc or "").lower() != "mtk":
            stage_reports[mtk_stage["id"]] = _skip_stage(mtk_stage, "non-MTK SoC")
            live.update(stages, current=mtk_stage["name"])
        else:
            def mtk_firmware_call() -> dict:
                from factory.images.mtk_firmware_collector_legacy import collect_mtk_firmware_images_legacy
                return collect_mtk_firmware_images_legacy(
                    project_dir=project_dir,
                    output_dir=output_dir,
                    images_dir=images_dir,
                    device=device,
                    soc=soc,
                    execute=execute,
                )

            report, failed = _run_stage(mtk_stage, stages, live, mtk_firmware_call, execute=execute)
            stage_reports[mtk_stage["id"]] = report
            if failed:
                missing = report.get("missing_images") or []
                message = (
                    "MTK firmware images not present in source ROM. "
                    "Provide matching fastboot TGZ or firmware pack."
                )
                if missing:
                    mtk_stage["errors"].append(f"missing MTK firmware images: {', '.join(missing)}")
                mtk_stage["errors"].append(message)
            stopped = stop_if_needed(mtk_stage, failed)

    if not stopped:
        final_stage = stages[11]

        def final_call() -> dict:
            from factory.output.final_zip_legacy import build_final_fastboot_zip
            return build_final_fastboot_zip(
                images_dir=images_dir,
                output_dir=final_output_dir,
                build_name=build_name,
                device=device or "unknown",
                flavor=flavor,
                soc=soc,
                template_zip=template_zip,
                execute=execute,
            )

        report, failed = _run_stage(final_stage, stages, live, final_call, execute=execute)
        stage_reports[final_stage["id"]] = report
        final_zip = report.get("final_zip")
        stopped = stop_if_needed(final_stage, failed)

        # ── Extract final packaging metrics from the ZIP report ──────────────
        fz = stage_reports.get("final_zip", {})
        dynamic_images_excluded_from_final_zip: list[str] = fz.get("images_excluded_dynamic", [])
        final_zip_image_list: list[str] = fz.get("images_included", [])
        final_zip_size_mib: float | None = fz.get("zip_size_mib")
        print(f"[legacy_pipeline] final_zip_image_list={final_zip_image_list}")
        print(f"[legacy_pipeline] final_zip_size_mib={final_zip_size_mib}")
    else:
        dynamic_images_excluded_from_final_zip = []
        final_zip_image_list = []
        final_zip_size_mib = None

    if stopped:
        for stage in stages:
            if stage["status"] == "WAIT":
                stage["status"] = "SKIP"
                stage["reason"] = "pipeline stopped before this stage"

    if execute:
        final_status = "FAILED" if stopped or any(stage["status"] == "FAIL" for stage in stages) else "APPLIED"
    else:
        final_status = "DRY_RUN"

    telegram_finish = live.finish(stages, final_status="FAILED" if final_status == "FAILED" else final_status, final_zip=final_zip)
    telegram_state = telegram_finish if telegram_finish.get("message_id") else telegram_state

    for stage in stages:
        if not stage.get("report_path"):
            stage["report_path"] = _known_report_path(stage["id"], output_dir)

    report = {
        "stage": "legacy_build_pipeline",
        "dry_run": not execute,
        "execute": execute,
        "build_name": build_name,
        "device": device,
        "soc": soc,
        "platform": platform,
        "flavor": flavor,
        "android_version": android_version,
        "mi_incremental": mi_incremental,
        "project_dir": str(project_dir) if project_dir is not None else None,
        "rom_path": str(rom_path) if rom_path is not None else None,
        "images_dir": str(images_dir),
        "partition_staging_dir": str(partition_staging_dir),
        "output_dir": str(output_dir),
        "final_zip": final_zip,
        "workspace_images_size_before_final_packaging_mib": workspace_images_size_mib,
        "super_img_validated": super_img_validated,
        "dynamic_images_excluded_from_final_zip": dynamic_images_excluded_from_final_zip,
        "final_zip_image_list": final_zip_image_list,
        "final_zip_size_mib": final_zip_size_mib,
        "telegram_enabled": bool(telegram),
        "telegram_message_id": live.message_id,
        "telegram_status": telegram_state,
        "stages": stages,
        "stage_reports": stage_reports,
        "warnings": warnings + live.warnings,
        "errors": errors + live.errors,
        "final_status": final_status,
    }
    report["report_files"] = write_legacy_build_pipeline_report(report, output_dir)
    print(f"[legacy_pipeline] final_status={final_status}")
    print(f"[legacy_pipeline] report_json={report['report_files']['json']}")
    print(f"[legacy_pipeline] report_txt={report['report_files']['txt']}")
    return report


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="DeadZone legacy build pipeline orchestrator")
    parser.add_argument("--rom", type=Path, default=None, help="Source ROM path")
    parser.add_argument("--project", type=Path, default=None, help="Unpacked project path")
    parser.add_argument("--output-dir", type=Path, default=None, help="Output directory")
    parser.add_argument("--build-name", default="DeadZone_v1")
    parser.add_argument("--device", default=None)
    parser.add_argument("--soc", default=None)
    parser.add_argument("--platform", default=None)
    parser.add_argument("--flavor", default="legend")
    parser.add_argument("--android-version", default=None)
    parser.add_argument("--mi-version", dest="mi_version", default=None)
    parser.add_argument("--vbmeta-mode", default=None)
    parser.add_argument("--template-zip", type=Path, default=None)
    parser.add_argument("--telegram", action="store_true")
    parser.add_argument("--execute", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    report = apply_legacy_build_pipeline(
        rom_path=args.rom,
        project_dir=args.project,
        output_dir=args.output_dir,
        build_name=args.build_name,
        device=args.device,
        soc=args.soc,
        platform=args.platform,
        flavor=args.flavor,
        android_version=args.android_version,
        mi_incremental=args.mi_version,
        vbmeta_mode=args.vbmeta_mode,
        template_zip=args.template_zip,
        execute=args.execute,
        telegram=args.telegram,
    )
    return 0 if report.get("final_status") in {"DRY_RUN", "APPLIED"} else 1


if __name__ == "__main__":
    sys.exit(main())
