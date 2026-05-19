"""Legacy-compatible super config persistence and SuperConfig sync."""
from __future__ import annotations

import json
import os
import shutil
from pathlib import Path
from typing import Any

from factory.repack.super_info_legacy import load_super_info_legacy

_REPO_ROOT = Path(__file__).resolve().parents[2]
_LEGACY_ROOT = _REPO_ROOT / "third_party" / "mezo_core"

_GENERIC_DEVICE_NAMES = frozenset({
    "mgvi_64_armv82",
    "armv82",
    "generic",
    "unknown",
})


def _read_json(path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def _write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=4, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def _read_build_prop_device(project_dir: Path) -> str | None:
    for build_prop in project_dir.rglob("build.prop"):
        try:
            for line in build_prop.read_text(encoding="utf-8", errors="ignore").splitlines():
                if line.startswith("ro.product.odm.device="):
                    value = line.split("=", 1)[1].strip()
                    if value:
                        return value
        except Exception:
            continue
    return None


def save_super_config_legacy(
    super_info: dict[str, Any],
    output_path: Path,
    execute: bool = False,
) -> dict[str, Any]:
    """Persist a legacy super config file, or report the dry-run write."""
    output_path = Path(output_path).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    would_overwrite = output_path.exists()

    if execute:
        try:
            _write_json(output_path, super_info)
        except Exception as exc:
            errors.append(f"Could not write super config: {exc}")

    return {
        "dry_run": not execute,
        "output_path": str(output_path),
        "would_write": True,
        "would_overwrite": would_overwrite,
        "written": execute and not errors,
        "warnings": warnings,
        "errors": errors,
        "status": "APPLIED" if execute and not errors else ("FAILED" if errors else "DRY_RUN"),
    }


def _inject_parts_info_super(project_dir: Path, super_info: dict[str, Any], execute: bool) -> dict[str, Any]:
    parts_info_path = project_dir / "config" / "parts_info"
    parts_info = _read_json(parts_info_path) or {}
    already_present = "super_info" in parts_info
    if execute and not already_present:
        parts_info["super_info"] = super_info
        _write_json(parts_info_path, parts_info)
    return {
        "parts_info_path": str(parts_info_path),
        "already_present": already_present,
        "would_inject": not already_present,
        "injected": execute and not already_present,
    }


def sync_super_config_for_device_legacy(
    project_dir: Path,
    images_dir: Path,
    device: str | None,
    soc: str | None,
    platform: str | None,
    execute: bool = False,
) -> dict[str, Any]:
    """Sync project config/super and parts_info with legacy SuperConfig."""
    project_dir = Path(project_dir).resolve()
    images_dir = Path(images_dir).resolve()
    warnings: list[str] = []
    errors: list[str] = []
    copied: list[dict[str, str]] = []

    factory_codename = (device or os.environ.get("DEADZONE_DEVICE_CODENAME", "")).strip()
    build_prop_name = _read_build_prop_device(project_dir)
    if factory_codename:
        device_name = factory_codename
    elif build_prop_name and build_prop_name.lower() not in _GENERIC_DEVICE_NAMES:
        device_name = build_prop_name
    else:
        if build_prop_name:
            warnings.append(f"build.prop device is a generic SoC identifier; skipping SuperConfig sync: {build_prop_name}")
        else:
            warnings.append("Could not read ro.product.odm.device from build.prop; skipping SuperConfig sync")
        return {
            "dry_run": not execute,
            "device_name": None,
            "copied": copied,
            "warnings": warnings,
            "errors": errors,
            "status": "DRY_RUN" if not execute else "SKIPPED",
        }

    config_dir = project_dir / "config"
    config_super_path = config_dir / "super"
    config_parts_info_path = config_dir / "parts_info"
    device_dir = _LEGACY_ROOT / "SuperConfig" / device_name
    device_super_path = device_dir / "super"
    device_parts_info_path = device_dir / "parts_info"

    try:
        if execute:
            device_dir.mkdir(parents=True, exist_ok=True)

        if config_super_path.is_file():
            copied.append({"from": str(config_super_path), "to": str(device_super_path)})
            if execute:
                shutil.copy2(config_super_path, device_super_path)
        elif device_super_path.is_file():
            copied.append({"from": str(device_super_path), "to": str(config_super_path)})
            if execute:
                config_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(device_super_path, config_super_path)
        else:
            warnings.append(f"No super file found in project config or SuperConfig for device: {device_name}")

        if config_parts_info_path.is_file():
            parts_info = _read_json(config_parts_info_path)
            if isinstance(parts_info, dict) and "super_info" not in parts_info:
                warnings.append("parts_info exists but super_info is missing; skipping SuperConfig parts_info save")
            else:
                copied.append({"from": str(config_parts_info_path), "to": str(device_parts_info_path)})
                if execute:
                    shutil.copy2(config_parts_info_path, device_parts_info_path)
        elif device_parts_info_path.is_file():
            copied.append({"from": str(device_parts_info_path), "to": str(config_parts_info_path)})
            if execute:
                config_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(device_parts_info_path, config_parts_info_path)
        else:
            warnings.append("No parts_info found in project config or SuperConfig for this device")

        super_info = load_super_info_legacy(project_dir, images_dir, device, soc, platform, execute=False)
        if super_info.get("_super_info_source") != "missing":
            save_result = save_super_config_legacy(super_info, config_super_path, execute=execute)
            inject_result = _inject_parts_info_super(project_dir, super_info, execute=execute)
        else:
            save_result = None
            inject_result = None
    except Exception as exc:
        errors.append(f"Error syncing SuperConfig for device {device_name}: {exc}")
        save_result = None
        inject_result = None

    return {
        "dry_run": not execute,
        "device_name": device_name,
        "device_dir": str(device_dir),
        "copied": copied,
        "save_result": save_result,
        "parts_info_result": inject_result,
        "warnings": warnings,
        "errors": errors,
        "status": "FAILED" if errors else ("APPLIED" if execute else "DRY_RUN"),
    }
