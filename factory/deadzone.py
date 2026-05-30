from __future__ import annotations

import argparse
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from factory.core.artifacts import write_github_summary
from factory.core.app_inventory import generate_app_inventory
from factory.core.build_lock import BuildAlreadyRunningError, BuildLock, make_lock_key
from factory.core.cleanup import cleanup
from factory.core.error_classifier import classify_from_context
from factory.core.event_bus import EventBus
from factory.core.stable_app_policy import enforce_stable_app_policy
from factory.core.stable_partition_rebuild import rebuild_stable_partitions
from factory.core.detector import detect_rom
from factory.core.device_registry import list_devices, resolve_device
from factory.core.downloader import download_rom
from factory.core.errors import write_error_summary
from factory.core.final_zip import build_final_zip
from factory.core.image_extractor import extract_partition_images
from factory.core.inventory_package import build_inventory_package
from factory.core.inspector import inspect_workspace
from factory.core.reports import write_production_reports
from factory.core.repacker import build_repacked_super, repack_partitions
from factory.core.size_reducer import LEVELS as SIZE_REDUCTION_LEVELS
from factory.core.size_reducer import reduce_workspace_size
from factory.core.size_policy import SUPER_SIZE_POLICIES, bytes_from_decimal_gb, default_policy, enforce_final_zip_policy, write_policy_config
from factory.core.status import StageTracker
from factory.core.super_builder import validate_pre_super_images
from factory.core.super_profile import build_super_profile
from factory.core.style_runner import apply_style, normalize_style
from factory.core.telegram import TelegramResult, TelegramStatus
from factory.core.toolchain import resolve_toolchain
from factory.core.unpacker import unpack_rom
from factory.core.uploader import UploadResult, upload_final_zip_to_pixeldrain, write_skipped_upload_report
from factory.core.workspace import Workspace, create_workspace, read_json, write_json
from factory.live.live_screen import LiveScreen
from factory.reports.app_inventory import compare_app_policy
from factory.state.build_state import BuildState, create_build_state


ALLOWED_SOCS = ("mtk", "snapdragon")
ALLOWED_MODES = ("build", "production")


@dataclass
class BuildContext:
    rom_url: str
    style: str
    style_label: str
    soc: str
    mode: str
    workspace: Workspace
    device_codename: str = ""
    selected_codename: str = ""
    custom_codename: str = ""
    keep_workspace: bool = False
    rom_source: Path | None = None
    rom_metadata: Any | None = None
    device_profile: dict[str, Any] | None = None
    super_profile: dict[str, Any] | None = None
    final_zip_path: Path | None = None
    super_target_bytes: int = 8_500_000_000
    final_zip_max_bytes: int = 4_500_000_000
    super_size_policy: str = "stock_safe"
    allow_oversized_final: bool = False
    enable_size_reduction: bool = True
    size_reduction_level: str = "balanced"
    generate_app_inventory: bool = True
    app_inventory_zip_path: Path | None = None
    app_inventory: dict[str, Any] = field(default_factory=dict)
    app_policy: dict[str, Any] = field(default_factory=dict)
    image_extraction: dict[str, Any] = field(default_factory=dict)
    stable_app_policy: dict[str, Any] = field(default_factory=dict)
    stable_normalize: dict[str, Any] = field(default_factory=dict)
    stable_partition_rebuild: dict[str, Any] = field(default_factory=dict)
    stable_normalize_mode: str = "apply"
    run_stable_normalize: bool = True
    upload_pixeldrain: bool = False
    notify_telegram: bool = False
    live_screen_enabled: bool = False
    upload_result: UploadResult = field(default_factory=UploadResult)
    telegram_result: TelegramResult = field(default_factory=TelegramResult)
    telegram: TelegramStatus | None = None
    tracker: StageTracker | None = None
    build_state: BuildState | None = None
    event_bus: EventBus | None = None
    live_screen: LiveScreen | None = None
    build_lock: BuildLock | None = None
    build_id: str = ""
    reports: dict[str, str] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    status: str = "RUNNING"
    cleanup_status: str = "not run"
    started_stage: str = "(none)"
    completed_stage: str = "(none)"
    failed_stage: str = ""
    failure_error: str = ""
    stages: list[dict[str, Any]] = field(default_factory=list)
    started_at: float = field(default_factory=time.time)
    completed_at: float | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="MEZO / DeadZone production ROM builder")
    parser.add_argument("--rom-url")
    parser.add_argument("--style", choices=["Stable", "Legend", "Gaming", "EPiC", "stable", "legend", "gaming", "epic"])
    parser.add_argument("--soc", choices=ALLOWED_SOCS)
    parser.add_argument("--device-codename", default="")
    parser.add_argument("--custom-codename", default="")
    parser.add_argument("--mode", choices=ALLOWED_MODES, default="build")
    parser.add_argument("--output-dir", type=Path, default=Path("output"))
    parser.add_argument("--keep-workspace", action="store_true")
    parser.add_argument("--upload-pixeldrain", action="store_true")
    parser.add_argument("--notify-telegram", action="store_true")
    parser.add_argument("--list-devices", action="store_true")
    parser.add_argument("--show-device", default="")
    parser.add_argument("--check-toolchain", action="store_true")
    parser.add_argument("--super-target-gb", default="8.5")
    parser.add_argument("--final-zip-max-gb", default="4.5")
    parser.add_argument("--super-size-policy", choices=SUPER_SIZE_POLICIES, default="stock_safe")
    parser.add_argument("--allow-oversized-final", action="store_true")
    parser.add_argument("--enable-size-reduction", nargs="?", const="true", default="true")
    parser.add_argument("--size-reduction-level", choices=SIZE_REDUCTION_LEVELS, default="balanced")
    parser.add_argument("--generate-app-inventory", action="store_true")
    parser.add_argument("--skip-app-inventory", action="store_true")
    parser.add_argument("--stable-app-normalize", action="store_true")
    parser.add_argument("--skip-stable-app-normalize", action="store_true")
    parser.add_argument("--stable-normalize-mode", choices=["plan", "apply"], default="apply")
    parser.add_argument("--live-screen", nargs="?", const="true", default=None,
                        help="Enable animated live screen (true/false)")
    return parser.parse_args()


def _print_device(device: dict) -> None:
    print(f"[DEVICE] Codename: {device.get('resolved_codename') or device.get('codename')}")
    print(f"[DEVICE] Name: {device.get('name')}")
    print(f"[SOC] {device.get('soc')}")
    print(f"[PROFILE] Source: {device.get('profile_source')}")
    super_cfg = device.get("super") if isinstance(device.get("super"), dict) else {}
    print(f"[SUPER PROFILE] Source: {super_cfg.get('metadata_source') or device.get('device_source')}")


def _print_device_list() -> None:
    grouped = list_devices()
    total = sum(len(values) for values in grouped.values())
    print(f"[DEVICES] total: {total}")
    for soc, devices in grouped.items():
        print(f"[{soc}] {len(devices)}")
        for device in devices:
            print(f"  {device.get('codename')} | {device.get('name')}")


def _print_toolchain() -> None:
    ws = create_workspace(Path("output/workspace"), clean=False)
    toolchain = resolve_toolchain(ws)
    for name, status in toolchain.tools.items():
        print(f"[TOOLCHAIN] {name}: {status.path or '(missing)'}")
    print(f"[TOOLCHAIN REPORT] {toolchain.report_path}")


def _selected_codename(device_codename: str, custom_codename: str) -> str:
    device = device_codename.strip().lower()
    custom = custom_codename.strip().lower()
    if device and device != "custom":
        return device
    if device == "custom":
        return custom
    return ""


def _bool_arg(value: Any, default: bool = True) -> bool:
    if isinstance(value, bool):
        return value
    raw = str(value or "").strip().lower()
    if raw in {"1", "true", "yes", "on", "enabled"}:
        return True
    if raw in {"0", "false", "no", "off", "disabled"}:
        return False
    return default


def _warn_on_codename_mismatch(ctx: BuildContext) -> None:
    selected = ctx.selected_codename.strip().lower()
    detected = str(getattr(ctx.rom_metadata, "codename", "") or "").strip().lower()
    if not selected or not detected or detected == "unknown" or selected == detected:
        return
    message = (
        "[WARNING] Selected device codename "
        f"'{selected}' differs from detected ROM codename '{detected}'. "
        "DeadZone will keep the selected device and will not switch silently."
    )
    ctx.warnings.append(message)
    print(message)


def _resolution_codename(ctx: BuildContext) -> str | None:
    device = ctx.device_codename.strip().lower()
    if device == "custom":
        return "custom"
    return ctx.selected_codename or None


def _output_path(result: Any) -> str:
    if isinstance(result, Path):
        return str(result)
    if isinstance(result, dict):
        for key in ("path", "zip", "output", "report_path", "links_path"):
            value = result.get(key)
            if value:
                return str(value)
    return ""


def _stage(ctx: BuildContext, name: str, fn: Callable[[], Any]) -> Any:
    ctx.started_stage = name
    print(f"[DeadZone] Stage: {name}")
    print("[MEZO] Status: started")
    if ctx.tracker:
        ctx.tracker.start(name)
    if ctx.event_bus:
        ctx.event_bus.emit_event(name, "RUN", f"Stage started: {name}")
    if ctx.telegram:
        ctx.telegram_result = ctx.telegram.add_event(name, "RUN")
    started = time.monotonic()
    try:
        result = fn()
    except Exception as exc:
        duration = time.monotonic() - started
        ctx.failed_stage = name
        ctx.failure_error = str(exc)
        ctx.status = "FAILED"
        if ctx.tracker:
            ctx.tracker.finish(name, "FAILED", error=str(exc))
        ctx.stages.append({
            "name": name,
            "status": "FAILED",
            "duration_seconds": duration,
            "error": str(exc),
        })
        print("[MEZO] Status: failed")
        if ctx.event_bus:
            ctx.event_bus.emit_event(name, "FAIL", str(exc))
        if ctx.telegram:
            detail = "Final ZIP exceeds 4.5GB policy" if name == "size_policy" else str(exc)
            ctx.telegram_result = ctx.telegram.add_event(name, "FAIL", detail)
        raise
    duration = time.monotonic() - started
    ctx.completed_stage = name
    output_path = _output_path(result)
    if ctx.tracker:
        ctx.tracker.finish(name, "OK", output_path=output_path)
    ctx.stages.append({
        "name": name,
        "status": "OK",
        "duration_seconds": duration,
        "output_path": output_path,
    })
    print("[MEZO] Status: completed")
    if ctx.event_bus:
        ctx.event_bus.emit_event(name, "OK", f"Stage completed: {name}", file=output_path or None)
    if ctx.telegram:
        ctx.telegram_result = ctx.telegram.add_event(name, "OK")
    return result


def _update_resolved_device_metadata(ctx: BuildContext) -> None:
    ws = ctx.workspace
    device = ctx.device_profile or {}
    info = ctx.rom_metadata
    codename = str(device.get("resolved_codename") or device.get("codename") or "unknown")
    device_info = read_json(ws.meta / "device_info.json", {})
    device_info.update({
        "codename": codename,
        "detected_codename": device.get("detected_codename") or getattr(info, "codename", "unknown"),
        "name": device.get("name"),
        "soc": str(device.get("soc") or ctx.soc).upper(),
        "resolution_source": device.get("resolution_source"),
        "android_version": getattr(info, "android_version", device_info.get("android_version", "unknown")),
        "build": getattr(info, "build", device_info.get("build", "unknown")),
    })
    write_json(ws.meta / "device_info.json", device_info)
    if info is not None:
        info.codename = codename


def _prepare_workspace(ctx: BuildContext) -> Workspace:
    write_policy_config(
        ctx.workspace,
        default_policy(
            super_target_bytes=ctx.super_target_bytes,
            final_zip_max_bytes=ctx.final_zip_max_bytes,
            allow_oversized_final=ctx.allow_oversized_final,
            super_size_policy=ctx.super_size_policy,
        ),
    )
    return ctx.workspace


def _sync_device_to_state(ctx: BuildContext) -> None:
    if ctx.build_state is None:
        return
    device = ctx.device_profile or {}
    info = ctx.rom_metadata
    codename = str(device.get("resolved_codename") or device.get("codename") or "unknown")
    ctx.build_state.device = codename
    ctx.build_state.android_version = str(getattr(info, "android_version", ctx.build_state.android_version) or "unknown")
    ctx.build_state.rom_version = str(getattr(info, "build", ctx.build_state.rom_version) or "unknown")
    if ctx.live_screen:
        ctx.live_screen.update_rom_info(
            device=codename,
            rom_version=ctx.build_state.rom_version,
            android_version=ctx.build_state.android_version,
        )
    ctx.build_state.save()


def _acquire_build_lock(ctx: BuildContext) -> None:
    device = ctx.device_profile or {}
    info = ctx.rom_metadata
    codename = str(device.get("resolved_codename") or device.get("codename") or "unknown")
    build_ver = str(getattr(info, "build", "") or "unknown")
    ws = ctx.workspace
    key = make_lock_key(ctx.soc, ctx.style, codename, build_ver)
    lock = BuildLock(ws.root.parent, key)
    lock.acquire()
    ctx.build_lock = lock


def _run_app_policy_compare(ctx: BuildContext) -> None:
    scanned_apps = (ctx.app_inventory or {}).get("apps") or []
    if not scanned_apps:
        return
    try:
        if ctx.event_bus:
            ctx.event_bus.emit_event("app_policy_compare", "RUN", "Comparing apps against policy list")
        ctx.app_policy = compare_app_policy(
            ctx.workspace.reports,
            scanned_apps,
            build_state=ctx.build_state,
        )
        if ctx.event_bus:
            counters = (ctx.app_policy or {}).get("counters", {})
            ctx.event_bus.emit_event(
                "app_policy_compare",
                "OK",
                "App policy comparison complete",
                data=counters,
            )
    except Exception as exc:
        print(f"[APP POLICY] Warning: comparison failed (non-fatal): {exc}")
        if ctx.event_bus:
            ctx.event_bus.emit_event("app_policy_compare", "WARN", f"App policy compare failed: {exc}")


def _build_super_after_repack(ctx: BuildContext, unpack_result: Any) -> Any:
    inspection = inspect_workspace(ctx.workspace, ctx.rom_metadata, unpack_result)
    return build_repacked_super(ctx.workspace, ctx.rom_metadata, inspection)


def _run_build(ctx: BuildContext) -> BuildContext:
    ws = _stage(ctx, "prepare", lambda: _prepare_workspace(ctx))
    ctx.rom_source = _stage(ctx, "download", lambda: download_rom(ctx.rom_url, ws))
    ctx.rom_metadata = _stage(
        ctx,
        "detect",
        lambda: detect_rom(
            ctx.rom_source,
            ws,
            soc=ctx.soc,
            custom_codename=ctx.custom_codename if ctx.device_codename.strip().lower() == "custom" else "",
        ),  # type: ignore[arg-type]
    )
    _warn_on_codename_mismatch(ctx)
    ctx.device_profile = _stage(
        ctx,
        "device",
        lambda: resolve_device(_resolution_codename(ctx), rom_metadata=ctx.rom_metadata, custom_codename=ctx.custom_codename, ws=ws),
    )
    _update_resolved_device_metadata(ctx)
    _print_device(ctx.device_profile)
    _sync_device_to_state(ctx)
    if ctx.telegram:
        codename = ctx.device_profile.get("resolved_codename") or ctx.device_profile.get("codename") or "unknown"
        ctx.telegram.device = str(codename)
        ctx.telegram.detected_device = str(ctx.device_profile.get("detected_codename") or getattr(ctx.rom_metadata, "codename", "unknown"))
        ctx.telegram_result = ctx.telegram.add_event("device resolved", "OK", str(codename))
    _acquire_build_lock(ctx)
    unpack_result = _stage(
        ctx,
        "unpack",
        lambda: unpack_rom(ctx.rom_source, ctx.rom_metadata, ws),  # type: ignore[arg-type]
    )
    inspection = _stage(
        ctx,
        "inspect",
        lambda: inspect_workspace(ws, ctx.rom_metadata, unpack_result),  # type: ignore[arg-type]
    )
    if ctx.generate_app_inventory:
        ctx.image_extraction = _stage(
            ctx,
            "image_extraction",
            lambda: extract_partition_images(ws, ctx.rom_metadata, inspection),  # type: ignore[arg-type]
        )
        ctx.app_inventory = _stage(
            ctx,
            "app_inventory",
            lambda: generate_app_inventory(ws, ctx.image_extraction),
        )
        if ctx.style == "stable":
            ctx.stable_app_policy = _stage(
                ctx,
                "stable_app_policy",
                lambda: enforce_stable_app_policy(
                    reports_dir=ws.reports,
                    partitions_root=ws.partitions,
                    scanned_apps=(ctx.app_inventory or {}).get("apps") or [],
                    style=ctx.style,
                    build_state=ctx.build_state,
                ),
            )
            ctx.stable_partition_rebuild = _stage(
                ctx,
                "stable_partition_rebuild",
                lambda: rebuild_stable_partitions(ws, ctx.stable_app_policy),
            )
        if ctx.run_stable_normalize and ctx.style in ("stable",):
            ctx.stable_normalize = {
                "skipped": True,
                "reason": "Stable App Policy is the source of truth for stable app actions",
            }
        ctx.app_inventory_zip_path = _stage(
            ctx,
            "inventory_package",
            lambda: build_inventory_package(ws, ctx.rom_metadata, ctx.app_inventory),  # type: ignore[arg-type]
        )
        _run_app_policy_compare(ctx)
    _stage(
        ctx,
        "size_reduction",
        lambda: reduce_workspace_size(
            ws,
            enabled=ctx.enable_size_reduction and not ctx.generate_app_inventory,
            level=ctx.size_reduction_level,
            disabled_reason="Stable App Inventory is inspect-only; deletion is disabled for this stage"
            if ctx.generate_app_inventory
            else "size reduction disabled by CLI",
        ),
    )
    ctx.super_profile = _stage(
        ctx,
        "super_profile",
        lambda: build_super_profile(ws, ctx.rom_metadata, inspection, ctx.device_profile),  # type: ignore[arg-type]
    )
    _stage(ctx, "style", lambda: apply_style(ctx.style, ws, ctx.rom_metadata))  # type: ignore[arg-type]
    _stage(ctx, "repack", lambda: repack_partitions(ws))
    _stage(ctx, "pre_super_image_validation", lambda: validate_pre_super_images(ws, ctx.super_profile or {}))
    _stage(ctx, "super", lambda: _build_super_after_repack(ctx, unpack_result))  # type: ignore[arg-type]
    ctx.final_zip_path = _stage(
        ctx,
        "final_zip",
        lambda: build_final_zip(ws, ctx.rom_metadata, ctx.style),  # type: ignore[arg-type]
    )
    _stage(
        ctx,
        "size_policy",
        lambda: enforce_final_zip_policy(ws, ctx.final_zip_path, ctx.allow_oversized_final),  # type: ignore[arg-type]
    )
    print(f"[FINAL ZIP] {ctx.final_zip_path}")
    ctx.status = "OK"
    return ctx


def _run_upload(ctx: BuildContext) -> UploadResult:
    if ctx.upload_pixeldrain:
        print("[DeadZone] Upload: starting PixelDrain upload")
        result = upload_final_zip_to_pixeldrain(ctx.final_zip_path, ctx.workspace)
        ctx.upload_result = result
        if not result.ok:
            raise RuntimeError(result.failure_reason or "PixelDrain upload failed")
        return result
    ctx.upload_result = write_skipped_upload_report(ctx.workspace, requested=False)
    return ctx.upload_result


def _run_telegram_finish(ctx: BuildContext, final_status: str) -> TelegramResult:
    if not ctx.telegram:
        return ctx.telegram_result
    upload_url = ctx.upload_result.url if ctx.upload_result.ok else ""
    error_summary = ""
    error_path = ctx.workspace.reports / "error_summary.txt"
    if error_path.is_file():
        error_summary = error_path.read_text(encoding="utf-8", errors="replace")[:800]
    try:
        classified_error: dict[str, Any] = {}
        if final_status.upper() != "OK":
            try:
                classified_error = classify_from_context(ctx)
            except Exception:
                pass
        ctx.telegram_result = ctx.telegram.finish(
            final_status,
            final_zip=ctx.final_zip_path,
            upload_url=upload_url,
            failed_stage=ctx.failed_stage,
            error_summary=error_summary,
            classified_error=classified_error,
        )
        if ctx.generate_app_inventory:
            norm = ctx.stable_normalize or {}
            ctx.telegram_result = ctx.telegram.send_app_inventory_document(
                ctx.app_inventory_zip_path,
                total_apps=int((ctx.app_inventory or {}).get("total_apps_found") or 0),
                android_version=str(getattr(ctx.rom_metadata, "android_version", "unknown")),
                extraction_summary=(ctx.image_extraction or {}).get("summary") if isinstance(ctx.image_extraction, dict) else {},
                normalize_summary={
                    "kept": norm.get("kept", 0),
                    "removed": norm.get("removed_count", 0),
                    "renamed": norm.get("renamed", 0),
                    "missing": norm.get("missing", 0),
                    "protected_extra": norm.get("protected_extra", 0),
                    "removed_bytes": norm.get("removed_bytes", 0),
                } if not norm.get("skipped") else {},
            )
        ctx.telegram_result = ctx.telegram.write_report()
    except Exception as exc:
        report = ctx.workspace.reports / "telegram_report.txt"
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(
            "MEZO / DeadZone Telegram Report\n"
            "===============================\n"
            f"requested: {ctx.notify_telegram}\n"
            "enabled: False\n"
            "attempted: True\n"
            "status: failed\n"
            "message id: (none)\n"
            f"failure reason: {exc}\n",
            encoding="utf-8",
        )
        ctx.telegram_result = TelegramResult(
            requested=ctx.notify_telegram,
            enabled=False,
            attempted=True,
            status="failed",
            failure_reason=str(exc),
            errors=[str(exc)],
        )
    return ctx.telegram_result


def _run_cleanup(ctx: BuildContext) -> dict[str, Any]:
    cleanup_result = cleanup(ctx.workspace, keep_workspace=ctx.keep_workspace or ctx.generate_app_inventory)
    ctx.cleanup_status = str(cleanup_result.get("status", "unknown"))
    if cleanup_result.get("status") == "FAILED":
        raise RuntimeError("; ".join(cleanup_result.get("errors") or ["cleanup failed"]))
    return cleanup_result


def _write_final_reports(ctx: BuildContext) -> None:
    ctx.completed_at = ctx.completed_at or time.time()
    ctx.reports = write_production_reports(ctx, ctx.workspace)
    summary = write_github_summary(ctx, ctx.workspace)
    ctx.reports["github_summary"] = str(summary)


def _validate_build_args(args: argparse.Namespace) -> None:
    errors: list[str] = []
    if not args.style:
        errors.append("--style is required (stable, legend, gaming, epic)")
    if not args.soc:
        errors.append("--soc is required (mtk, snapdragon)")
    if not args.rom_url:
        errors.append("--rom-url is required")
    if not args.device_codename and not args.custom_codename:
        print(
            "[WARNING] No --device-codename supplied; "
            "device will be auto-detected from ROM metadata.",
            flush=True,
        )
    if errors:
        for msg in errors:
            print(f"[ERROR] {msg}", flush=True)
        raise SystemExit("Build validation failed — see errors above")


def _print_startup_banner(ctx: BuildContext, args: argparse.Namespace, run_normalize: bool) -> None:
    device_display = ctx.selected_codename or ctx.custom_codename or "Detecting..."
    rom_display = ctx.rom_url or "(not provided)"
    print("=" * 60, flush=True)
    print("  DeadZone Factory", flush=True)
    print("  Developer: Mezo", flush=True)
    print(f"  Selected Style : {ctx.style_label}", flush=True)
    print(f"  Device         : {device_display}", flush=True)
    print(f"  ROM            : {rom_display}", flush=True)
    print(f"  SoC            : {ctx.soc}", flush=True)
    print(f"  Mode           : {ctx.mode}", flush=True)
    print(f"  Build ID       : {ctx.build_id}", flush=True)
    print("=" * 60, flush=True)
    print(f"[MEZO] Status: running", flush=True)
    if ctx.upload_pixeldrain:
        print("[DeadZone] Upload: PixelDrain requested", flush=True)
    if ctx.notify_telegram:
        print("[DeadZone] Telegram: notifications requested", flush=True)
    print(f"[SIZE] Super policy: {ctx.super_size_policy}", flush=True)
    print(f"[SIZE REDUCTION] Level: {ctx.size_reduction_level}, enabled: {ctx.enable_size_reduction and not ctx.generate_app_inventory}", flush=True)
    print(f"[APP INVENTORY] Enabled: {ctx.generate_app_inventory}", flush=True)
    print(f"[STABLE APPS] Normalize: {run_normalize}, mode: {args.stable_normalize_mode}", flush=True)
    print(f"[SIZE] Final ZIP max: {ctx.final_zip_max_bytes}", flush=True)


def main() -> int:
    args = parse_args()
    if args.list_devices:
        _print_device_list()
        return 0
    if args.show_device:
        ws = create_workspace(Path("output/workspace"), clean=False)
        device = resolve_device(args.show_device, ws=ws)
        _print_device(device)
        return 0
    if args.check_toolchain:
        _print_toolchain()
        return 0
    _validate_build_args(args)
    style_key, style_label = normalize_style(args.style)
    output_dir = args.output_dir
    ws = create_workspace(output_dir / "workspace", clean=True)
    selected_codename = _selected_codename(args.device_codename, args.custom_codename)
    super_target_bytes = bytes_from_decimal_gb(args.super_target_gb, 8_500_000_000)
    final_zip_max_bytes = bytes_from_decimal_gb(args.final_zip_max_gb, 4_500_000_000)
    generate_inventory = not args.skip_app_inventory
    run_normalize = bool(style_key != "stable" and not args.skip_stable_app_normalize)
    live_screen_enabled = _bool_arg(getattr(args, "live_screen", None), False)

    build_state = create_build_state(
        output_dir,
        soc=args.soc,
        edition=style_label,
        device=selected_codename or args.custom_codename or "Detecting...",
    )
    event_bus = EventBus(output_dir, build_state)

    ctx = BuildContext(
        rom_url=args.rom_url,
        style=style_key,
        style_label=style_label,
        soc=args.soc,
        mode=args.mode,
        device_codename=args.device_codename,
        selected_codename=selected_codename,
        custom_codename=args.custom_codename,
        keep_workspace=args.keep_workspace,
        upload_pixeldrain=args.upload_pixeldrain,
        notify_telegram=args.notify_telegram,
        live_screen_enabled=live_screen_enabled,
        workspace=ws,
        super_target_bytes=super_target_bytes,
        final_zip_max_bytes=final_zip_max_bytes,
        super_size_policy=args.super_size_policy,
        allow_oversized_final=args.allow_oversized_final,
        enable_size_reduction=_bool_arg(args.enable_size_reduction, True),
        size_reduction_level=args.size_reduction_level,
        generate_app_inventory=generate_inventory,
        run_stable_normalize=run_normalize,
        stable_normalize_mode=args.stable_normalize_mode,
        build_state=build_state,
        event_bus=event_bus,
        build_id=build_state.build_id,
    )
    ctx.tracker = StageTracker(ws)
    ctx.live_screen = LiveScreen(build_state, enabled=live_screen_enabled)
    _print_startup_banner(ctx, args, run_normalize)
    ctx.telegram = TelegramStatus(
        enabled=ctx.notify_telegram,
        soc=ctx.soc,
        style=ctx.style_label,
        device=ctx.selected_codename or ctx.custom_codename or "Detecting...",
        workspace=ws,
        rom_source=ctx.rom_url,
    )
    ctx.telegram_result = ctx.telegram.start()
    ctx.event_bus.emit_event("build", "RUN", f"Build started: {ctx.style_label} {ctx.soc}")
    if ctx.live_screen:
        ctx.live_screen.start()
    try:
        try:
            _run_build(ctx)
        except BuildAlreadyRunningError as lock_exc:
            print(f"[BUILD LOCK] {lock_exc}")
            print("[MEZO] Status: blocked by existing build lock")
            if ctx.live_screen:
                ctx.live_screen.stop("BLOCKED")
            return 1
        _stage(ctx, "upload", lambda: _run_upload(ctx))
        _stage(ctx, "telegram", lambda: _run_telegram_finish(ctx, "OK"))
        _stage(ctx, "cleanup", lambda: _run_cleanup(ctx))
    except Exception as exc:
        ctx.completed_at = time.time()
        if not ctx.failed_stage:
            ctx.failed_stage = ctx.started_stage
        ctx.failure_error = str(exc)
        if ctx.status == "OK":
            ctx.status = "FAILED"
        ctx.cleanup_status = "not run after failure"
        if ctx.build_state:
            ctx.build_state.finish("FAILED")
        if ctx.build_lock:
            ctx.build_lock.release()
        if ctx.live_screen:
            ctx.live_screen.stop("FAILED")
        if ctx.failed_stage != "upload":
            reason = "build failed after final ZIP; upload skipped" if ctx.final_zip_path else "build failed before final ZIP"
            ctx.upload_result = write_skipped_upload_report(ws, requested=ctx.upload_pixeldrain, reason=reason)
        write_error_summary(ctx, ws, exc)
        try:
            _stage(ctx, "telegram", lambda: _run_telegram_finish(ctx, "FAIL"))
        except Exception:
            pass
        _write_final_reports(ctx)
        print(f"[MEZO] Status: failed at {ctx.failed_stage}")
        return 1

    ctx.completed_at = time.time()
    if ctx.build_state:
        ctx.build_state.finish("OK")
    if ctx.build_lock:
        ctx.build_lock.release()
    if ctx.live_screen:
        ctx.live_screen.stop("DONE")
    _write_final_reports(ctx)
    print("[MEZO] Status: completed")
    print(f"[FINAL ZIP] {ctx.final_zip_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
