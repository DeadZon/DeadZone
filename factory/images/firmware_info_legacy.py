"""Legacy DeadZone firmware info generation.

This module carries over the firmware-info portion of
MEZOBuildRom.py:find_and_read_build_props while adding dry-run reporting and
the factory codename override rule required by the modular factory stage.
"""
from __future__ import annotations

import os
from pathlib import Path

from factory.unpack.build_prop import read_build_props

GENERIC_CODENAMES: frozenset[str] = frozenset({
    "",
    "generic",
    "qssi",
    "system",
    "unknown",
    "mgvi_64_armv82",
    "armv82",
})


def _clean(value: str | None) -> str | None:
    if value is None:
        return None
    value = str(value).strip()
    return value or None


def _select_factory_device(cli_device: str | None) -> tuple[str | None, str | None]:
    cli_device = _clean(cli_device)
    if cli_device:
        return cli_device, "cli"
    env_device = _clean(os.environ.get("DEADZONE_DEVICE_CODENAME"))
    if env_device:
        return env_device, "env"
    return None, None


def _read_first_prop_value(project_dir: Path, keys: tuple[str, ...]) -> str | None:
    for build_prop_path in project_dir.rglob("build.prop"):
        try:
            with build_prop_path.open("r", encoding="utf-8", errors="ignore") as handle:
                for raw_line in handle:
                    line = raw_line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, _, value = line.partition("=")
                    if key.strip() in keys and value.strip():
                        return value.strip()
        except Exception:
            continue
    return None


def resolve_effective_device(
    detected_device_from_build_prop: str | None,
    factory_device: str | None,
) -> tuple[str | None, str]:
    """Resolve the final codename using the factory override rule."""
    detected = _clean(detected_device_from_build_prop)
    factory = _clean(factory_device)

    if factory:
        if detected and detected != factory:
            return factory, (
                f"factory device '{factory}' overrides build.prop '{detected}'"
            )
        return factory, f"using factory device '{factory}'"

    if detected and detected.lower() not in GENERIC_CODENAMES:
        return detected, f"using build.prop device '{detected}'"

    if detected:
        return detected, (
            f"build.prop device '{detected}' is generic and no factory device was set"
        )
    return None, "no device codename found"


def generate_deadzone_firmware_info(
    project_dir: Path,
    images_dir: Path,
    flavor: str,
    device: str | None = None,
    soc: str | None = None,
    platform: str | None = None,
    android_version: str | None = None,
    mi_incremental: str | None = None,
    execute: bool = False,
) -> dict:
    """Read build.prop data and optionally write images/DeadZone_firmware.txt."""
    project_dir = Path(project_dir)
    images_dir = Path(images_dir)
    props = read_build_props(project_dir)

    detected_device = _clean(props.get("ro.product.odm.device"))
    factory_device, factory_source = _select_factory_device(device)
    effective_device, device_decision = resolve_effective_device(
        detected_device, factory_device
    )

    marketname = _clean(props.get("ro.product.odm.marketname"))
    model = _clean(props.get("ro.product.odm.model"))
    brand = _clean(props.get("ro.product.odm.brand"))
    build_android = _clean(props.get("ro.system.build.version.release"))
    build_mi = _clean(props.get("ro.mi.os.version.incremental"))
    build_fingerprint = _read_first_prop_value(
        project_dir,
        (
            "ro.build.fingerprint",
            "ro.system.build.fingerprint",
            "ro.vendor.build.fingerprint",
        ),
    )

    android_release = _clean(android_version) or build_android
    mi_version = _clean(mi_incremental) or build_mi
    device_name = marketname or model or ""

    generated_files: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    if detected_device and detected_device.lower() in GENERIC_CODENAMES and factory_device:
        warnings.append(
            f"build.prop device '{detected_device}' is generic; using factory device '{factory_device}'"
        )
    if not effective_device:
        warnings.append("effective device could not be determined")

    firmware_info_path = images_dir / "DeadZone_firmware.txt"
    content = (
        f"Codename={effective_device or ''}\n"
        f"Device name={device_name}\n"
        f"MI version={mi_version or ''}\n"
        f"Android release={android_release or ''}\n"
    )

    status = "DRY_RUN"
    if execute:
        try:
            images_dir.mkdir(parents=True, exist_ok=True)
            firmware_info_path.write_text(content, encoding="utf-8", newline="\n")
            generated_files.append(str(firmware_info_path))
            status = "APPLIED"
            print(f"[images] Firmware info written: {firmware_info_path}")
        except Exception as exc:
            errors.append(f"DeadZone_firmware.txt: {exc}")
            status = "FAILED"
    else:
        print(f"[images] Dry-run: would write firmware info: {firmware_info_path}")

    return {
        "status": status,
        "project_dir": str(project_dir),
        "images_dir": str(images_dir),
        "flavor": flavor,
        "device": device,
        "soc": soc,
        "platform": platform,
        "android_version": android_release,
        "mi_incremental": mi_version,
        "detected_device_from_build_prop": detected_device,
        "factory_device": factory_device,
        "factory_device_source": factory_source,
        "effective_device": effective_device,
        "device_decision": device_decision,
        "brand": brand,
        "device_name": device_name,
        "market_name": marketname,
        "model": model,
        "build_fingerprint": build_fingerprint,
        "firmware_info_path": str(firmware_info_path),
        "firmware_info_content": content,
        "generated_files": generated_files,
        "warnings": warnings,
        "errors": errors,
    }
