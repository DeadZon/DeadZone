from __future__ import annotations

import argparse
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from factory.core.cleanup import cleanup
from factory.core.detector import detect_rom
from factory.core.device_registry import list_devices, resolve_device
from factory.core.downloader import download_rom
from factory.core.final_zip import build_final_zip
from factory.core.inspector import inspect_workspace
from factory.core.reports import write_production_reports
from factory.core.repacker import build_repacked_super, repack_partitions
from factory.core.super_profile import build_super_profile
from factory.core.style_runner import apply_style, normalize_style
from factory.core.unpacker import unpack_rom
from factory.core.workspace import Workspace, create_workspace, read_json, write_json


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
    reports: dict[str, str] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    status: str = "RUNNING"
    cleanup_status: str = "not run"
    started_stage: str = "(none)"
    completed_stage: str = "(none)"
    failed_stage: str = ""
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
    parser.add_argument("--list-devices", action="store_true")
    parser.add_argument("--show-device", default="")
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


def _selected_codename(device_codename: str, custom_codename: str) -> str:
    device = device_codename.strip().lower()
    custom = custom_codename.strip().lower()
    if device and device != "custom":
        return device
    if device == "custom":
        return custom
    return ""


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


def _stage(ctx: BuildContext, name: str, fn: Callable[[], Any]) -> Any:
    ctx.started_stage = name
    print(f"[DeadZone] Stage: {name}")
    print("[MEZO] Status: started")
    started = time.monotonic()
    try:
        result = fn()
    except Exception as exc:
        duration = time.monotonic() - started
        ctx.failed_stage = name
        ctx.status = "FAILED"
        ctx.stages.append({
            "name": name,
            "status": "FAILED",
            "duration_seconds": duration,
            "error": str(exc),
        })
        print("[MEZO] Status: failed")
        raise
    duration = time.monotonic() - started
    ctx.completed_stage = name
    ctx.stages.append({
        "name": name,
        "status": "OK",
        "duration_seconds": duration,
    })
    print("[MEZO] Status: completed")
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
    return ctx.workspace


def _run_build(ctx: BuildContext) -> BuildContext:
    ws = _stage(ctx, "prepare workspace", lambda: _prepare_workspace(ctx))
    ctx.rom_source = _stage(ctx, "download ROM", lambda: download_rom(ctx.rom_url, ws))
    ctx.rom_metadata = _stage(
        ctx,
        "detect ROM type and metadata",
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
        "resolve device from registry",
        lambda: resolve_device(_resolution_codename(ctx), rom_metadata=ctx.rom_metadata, custom_codename=ctx.custom_codename, ws=ws),
    )
    _update_resolved_device_metadata(ctx)
    _print_device(ctx.device_profile)
    unpack_result = _stage(
        ctx,
        "unpack ROM into workspace",
        lambda: unpack_rom(ctx.rom_source, ctx.rom_metadata, ws),  # type: ignore[arg-type]
    )
    inspection = _stage(
        ctx,
        "inspect workspace and metadata",
        lambda: inspect_workspace(ws, ctx.rom_metadata, unpack_result),  # type: ignore[arg-type]
    )
    ctx.super_profile = _stage(
        ctx,
        "resolve super profile",
        lambda: build_super_profile(ws, ctx.rom_metadata, inspection, ctx.device_profile),  # type: ignore[arg-type]
    )
    _stage(ctx, "run style stage", lambda: apply_style(ctx.style, ws, ctx.rom_metadata))  # type: ignore[arg-type]
    _stage(ctx, "repack partitions", lambda: repack_partitions(ws))
    inspection = _stage(
        ctx,
        "inspect repacked workspace",
        lambda: inspect_workspace(ws, ctx.rom_metadata, unpack_result),  # type: ignore[arg-type]
    )
    _stage(ctx, "build or preserve super", lambda: build_repacked_super(ws, ctx.rom_metadata, inspection))  # type: ignore[arg-type]
    ctx.final_zip_path = _stage(
        ctx,
        "generate final ZIP",
        lambda: build_final_zip(ws, ctx.rom_metadata, ctx.style),  # type: ignore[arg-type]
    )
    print(f"[FINAL ZIP] {ctx.final_zip_path}")
    cleanup_result = _stage(ctx, "cleanup temporary files", lambda: cleanup(ws, keep_workspace=ctx.keep_workspace))
    ctx.cleanup_status = str(cleanup_result.get("status", "unknown"))
    ctx.status = "OK"
    return ctx


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
    if not args.rom_url or not args.style or not args.soc:
        raise SystemExit("--rom-url, --style, and --soc are required for build mode")

    style_key, style_label = normalize_style(args.style)
    output_dir = args.output_dir
    ws = create_workspace(output_dir / "workspace", clean=True)
    selected_codename = _selected_codename(args.device_codename, args.custom_codename)
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
        workspace=ws,
    )
    print("[DeadZone] Stage: production build")
    print("[MEZO] Status: running")
    print(f"[SOC] {ctx.soc}")
    print(f"[STYLE] {ctx.style_label}")
    if ctx.selected_codename:
        print(f"[SELECTED DEVICE] {ctx.selected_codename}")
    try:
        _run_build(ctx)
    except Exception:
        ctx.completed_at = time.time()
        ctx.cleanup_status = "not run after failure"
        ctx.reports = write_production_reports(ctx, ws)
        print(f"[MEZO] Status: failed at {ctx.failed_stage}")
        return 1
    ctx.completed_at = time.time()
    ctx.reports = write_production_reports(ctx, ws)
    print("[MEZO] Status: completed")
    print(f"[FINAL ZIP] {ctx.final_zip_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
