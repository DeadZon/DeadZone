from __future__ import annotations

import hashlib
import os
import shutil
import zipfile
from pathlib import Path
from typing import Any

import yaml

from factory.core.detector import RomInfo
from factory.core.size_policy import load_policy
from factory.core.super_builder import DYNAMIC_IMAGES
from factory.core.style_runner import STYLE_LABELS
from factory.core.vbmeta_patch import patch_vbmeta_images
from factory.core.workspace import Workspace, read_json, write_json

CORE_IMAGES = [
    "super.img",
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "vbmeta.img",
    "vbmeta_system.img",
    "vbmeta_vendor.img",
    "dtbo.img",
    "logo.img",
]
WINDOWS_TOOLS = ["fastboot.exe", "AdbWinApi.dll", "AdbWinUsbApi.dll"]
WINDOWS_SCRIPTS = [
    "windows_install_upgrade.bat",
    "windows_install_and_format_data.bat",
    "windows_format_data_only.bat",
]
SLOT_AWARE_PARTITIONS = {
    "boot",
    "init_boot",
    "vendor_boot",
    "dtbo",
    "vbmeta",
    "vbmeta_system",
    "vbmeta_vendor",
    "logo",
}
FORBIDDEN_ZIP_PARTS = {
    "logs",
    "reports",
    "workspace",
    "output",
    "DeadZone" + "_Mezo",
    "List" + "Mezo",
}
FORBIDDEN_ZIP_TEXT = {
    "build_info",
    "build_report",
    "sha256sums",
    "upload_links",
    "upload_report",
    "telegram_report",
    "secrets",
    "factory.pipeline." + "orchestrator",
    "scripts" + "/",
}


def _load_profile(soc: str) -> dict[str, Any]:
    key = soc.strip().lower()
    path = Path("profiles") / f"{key}.yml"
    if not path.is_file():
        raise RuntimeError(f"profile not found for SoC {soc!r}: {path}")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _profile_super(profile: dict[str, Any]) -> dict[str, Any]:
    data = profile.get("super") or {}
    if not isinstance(data, dict):
        raise RuntimeError("profile super section must be a mapping")
    return data


def _tool_source(name: str) -> Path | None:
    for base in [Path("tools/helper/windows"), Path("tools/helper/bin/windows")]:
        candidate = base / name
        if candidate.is_file() and candidate.stat().st_size > 0:
            return candidate
    return None


def _copy_windows_tools(stage: Path) -> list[str]:
    missing = [name for name in WINDOWS_TOOLS if _tool_source(name) is None]
    if missing:
        raise RuntimeError(
            "missing Windows fastboot binaries: "
            + ", ".join(missing)
            + "; place them in tools/helper/windows/"
        )
    dst = stage / "bin/windows"
    dst.mkdir(parents=True, exist_ok=True)
    copied = []
    for name in WINDOWS_TOOLS:
        shutil.copy2(_tool_source(name), dst / name)  # type: ignore[arg-type]
        copied.append(f"bin/windows/{name}")
    return copied


def _metadata_value(meta: dict[str, dict[str, Any]], key: str, fallback: str = "unknown") -> str:
    for name in ["rom_info.json", "device_info.json"]:
        value = meta.get(name, {}).get(key)
        if value not in (None, "", "unknown"):
            return str(value)
    return fallback


def _android_tag(version: str) -> str:
    if not version or version == "unknown":
        return "Axx"
    major = str(version).split(".", 1)[0]
    return f"A{major}" if major.isdigit() else "Axx"


def _partition_for(image: str, slot_mode: str) -> str:
    stem = Path(image).stem
    if stem == "super":
        return "super"
    if stem in SLOT_AWARE_PARTITIONS and slot_mode.upper() in {"A/B", "VAB", "VIRTUAL_AB"}:
        return f"{stem}_ab"
    return stem


def _write_bat(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\r\n")


def _bat_header(style: str, codename: str, android: str, build: str) -> str:
    return f"""@echo off
setlocal EnableExtensions
cd /d "%~dp0"
set "fastboot=bin\\windows\\fastboot.exe"
if not exist "%fastboot%" (
  echo [ERROR] bin\\windows\\fastboot.exe not found.
  echo Do not disconnect your device. Leave it in fastboot and fix the package.
  pause
  exit /b 1
)
echo Waiting for device...
set "device="
for /f "tokens=2" %%A in ('"%fastboot%" getvar product 2^>^&1 ^| findstr "\\<product:"') do set "device=%%A"
if "%device%" equ "" (
  echo [ERROR] Your device could not be detected.
  echo Do not disconnect your device. Leave it in fastboot and try again.
  pause
  exit /b 1
)
echo Your device: %device%
if /i "%device%" neq "{codename}" (
  echo [ERROR] Compatible device: {codename}
  echo Do not disconnect your device unless you intentionally stop here.
  pause
  exit /b 1
)
set "hwc="
for /f "tokens=2" %%A in ('"%fastboot%" getvar hwc 2^>^&1 ^| findstr "\\<hwc:"') do set "hwc=%%A"

echo ============================================================
echo DeadZone
echo Developer: Mezo
echo Style: {style}
echo Device codename: {codename}
echo Android version: {android}
echo ROM build: {build}
echo ============================================================
echo Safe warning:
echo Keep the USB cable connected. If a command fails, this script stops.
echo The device will remain in fastboot on failure.
echo ============================================================
"""


def _run_checked(command: str, action: str) -> str:
    return f"""{command}
if errorlevel 1 (
  echo [ERROR] {action} failed.
  echo Do not disconnect your device. Leave it in fastboot and fix the issue.
  pause
  exit /b 1
)
"""


def _flash_block(images: list[str], slot_mode: str) -> str:
    lines = ['"%fastboot%" set_active a']
    lines.append(
        "if errorlevel 1 (\n"
        "  echo [ERROR] Could not set active slot.\n"
        "  echo Do not disconnect your device. Leave it in fastboot and fix the issue.\n"
        "  pause\n"
        "  exit /b 1\n"
        ")"
    )
    for image in images:
        partition = _partition_for(image, slot_mode)
        lines.append(
            f"""if not exist "images\\{image}" (
  echo [ERROR] Missing images\\{image}
  echo Do not disconnect your device. Leave it in fastboot and fix the package.
  pause
  exit /b 1
)
"%fastboot%" flash {partition} "images\\{image}"
if errorlevel 1 (
  echo [ERROR] Flash failed: {partition}
  echo Do not disconnect your device. Leave it in fastboot and fix the issue.
  pause
  exit /b 1
)"""
        )
    return "\n".join(lines) + "\n"


def _write_scripts(
    stage: Path,
    style: str,
    codename: str,
    android: str,
    build: str,
    flash_images: list[str],
    slot_mode: str,
) -> list[str]:
    header = _bat_header(style, codename, android, build)
    flash = _flash_block(flash_images, slot_mode)
    upgrade = header + """echo Your device will be flashed without formatting the data partition.
echo You will keep your apps, settings and files on internal storage.
echo Continue if you are upgrading from an older ROM version.
set /p choice=Do you want to continue? [y/N] 
if /i "%choice%" neq "y" exit /b 0

echo ##############################################################
echo Please wait. The device will reboot once flashing is complete.
echo ##############################################################
""" + flash + _run_checked('"%fastboot%" reboot', "Reboot") + "exit /b 0\n"

    clean = header + """echo Your device will be flashed and the data partition will be formatted.
echo You will lose your apps, settings and files on internal storage.
echo Continue if you are flashing for the first time or downgrading.
set /p choice=Do you want to continue? [y/N] 
if /i "%choice%" neq "y" exit /b 0

echo ##############################################################
echo Please wait. Data wipe starts only after flashing succeeds.
echo ##############################################################
""" + flash
    clean += _run_checked('"%fastboot%" erase metadata', "Erase metadata")
    clean += _run_checked('"%fastboot%" erase userdata', "Erase userdata")
    clean += _run_checked('"%fastboot%" reboot', "Reboot") + "exit /b 0\n"

    wipe = header + """echo The data partition on your device will be formatted.
echo You will lose your apps, settings and files on internal storage.
echo Continue if you want to perform a factory reset.
set /p choice=Do you want to continue? [y/N] 
if /i "%choice%" neq "y" exit /b 0

"""
    wipe += _run_checked('"%fastboot%" set_active a', "Set active slot")
    wipe += _run_checked('"%fastboot%" erase metadata', "Erase metadata")
    wipe += _run_checked('"%fastboot%" erase userdata', "Erase userdata")
    wipe += _run_checked('"%fastboot%" reboot', "Reboot") + "exit /b 0\n"

    scripts = {
        "windows_install_upgrade.bat": upgrade,
        "windows_install_and_format_data.bat": clean,
        "windows_format_data_only.bat": wipe,
    }
    for name, text in scripts.items():
        _write_bat(stage / name, text)
    return list(scripts)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _write_sidecars(ws: Workspace, zip_path: Path, sha: str, style: str, codename: str, android: str, build: str) -> None:
    ws.final.mkdir(parents=True, exist_ok=True)
    (zip_path.with_name(zip_path.name + ".sha256")).write_text(f"{sha}  {zip_path.name}\n", encoding="utf-8")
    lines = [
        "MEZO / DeadZone Build Info",
        "==========================",
        f"final ZIP: {zip_path.name}",
        f"style: {style}",
        f"codename: {codename}",
        f"Android version: {android}",
        f"build version: {build}",
        f"sha256: {sha}",
        f"size bytes: {zip_path.stat().st_size}",
        "",
    ]
    (ws.final / "build_info.txt").write_text("\n".join(lines), encoding="utf-8")


def _copy_images(ws: Workspace, stage: Path, profile_super: dict[str, Any]) -> tuple[list[str], list[str]]:
    required = list(dict.fromkeys(CORE_IMAGES + list(profile_super.get("required_images") or [])))
    firmware = list(profile_super.get("firmware_images") or [])
    allowed = set(required) | set(firmware)
    has_super = (ws.images / "super.img").is_file()
    missing = [name for name in required if not (ws.images / name).is_file()]
    if missing:
        raise RuntimeError(f"required final ZIP images are missing: {', '.join(missing)}")

    included: list[str] = []
    excluded: list[str] = []
    for img in sorted(ws.images.glob("*.img")):
        if has_super and img.name in DYNAMIC_IMAGES and img.name not in firmware:
            excluded.append(f"images/{img.name} (dynamic partition excluded because super.img exists)")
            continue
        if img.name in allowed:
            shutil.copy2(img, stage / "images" / img.name)
            included.append(img.name)
        else:
            excluded.append(f"images/{img.name} (not allowed by final ZIP profile)")
    return included, excluded


def _flash_order(included: list[str], profile_super: dict[str, Any]) -> list[str]:
    present = set(included)
    configured = [name for name in profile_super.get("flash_order") or [] if name in present]
    remainder = [name for name in CORE_IMAGES if name in present and name not in configured]
    firmware = [
        name
        for name in profile_super.get("firmware_images") or []
        if name in present and name not in configured and name not in remainder
    ]
    if configured:
        return configured + remainder + firmware
    default = [
        "boot.img",
        "init_boot.img",
        "vendor_boot.img",
        "dtbo.img",
        "vbmeta.img",
        "vbmeta_system.img",
        "vbmeta_vendor.img",
        "super.img",
        "logo.img",
    ]
    return [name for name in default + firmware if name in present]


def _zip_entries(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as zf:
        return sorted(zf.namelist())


def _validate_zip(
    zip_path: Path,
    included_images: list[str],
    profile_super: dict[str, Any],
    has_super: bool,
) -> list[str]:
    errors: list[str] = []
    entries = _zip_entries(zip_path)
    entry_set = set(entries)
    allowed_entries = {f"images/{name}" for name in included_images}
    allowed_entries.update(f"bin/windows/{name}" for name in WINDOWS_TOOLS)
    allowed_entries.update(WINDOWS_SCRIPTS)
    for entry in entries:
        if entry not in allowed_entries:
            errors.append(f"ZIP contains non-final-package file {entry}")
    if has_super and "images/super.img" not in entry_set:
        errors.append("ZIP is missing images/super.img")
    for image in CORE_IMAGES + list(profile_super.get("required_images") or []):
        if f"images/{image}" not in entry_set:
            errors.append(f"ZIP is missing required image images/{image}")
    for image in profile_super.get("firmware_images") or []:
        if image in included_images and f"images/{image}" not in entry_set:
            errors.append(f"ZIP is missing included firmware image images/{image}")
    for script in WINDOWS_SCRIPTS:
        if script not in entry_set:
            errors.append(f"ZIP is missing {script}")
    for tool in WINDOWS_TOOLS:
        if f"bin/windows/{tool}" not in entry_set:
            errors.append(f"ZIP is missing bin/windows/{tool}")
    for entry in entries:
        parts = set(Path(entry).parts)
        if parts & FORBIDDEN_ZIP_PARTS:
            errors.append(f"ZIP contains forbidden path {entry}")
        if any(text.lower() in entry.lower() for text in FORBIDDEN_ZIP_TEXT):
            errors.append(f"ZIP contains forbidden file {entry}")
        if has_super and Path(entry).name in DYNAMIC_IMAGES:
            errors.append(f"ZIP contains unpacked dynamic image while super.img exists: {entry}")
    return errors


def _write_report(
    ws: Workspace,
    zip_path: Path,
    zip_name: str,
    style: str,
    codename: str,
    android: str,
    build: str,
    included: list[str],
    excluded: list[str],
    scripts: list[str],
    validation_errors: list[str],
    compressed_size: int,
    uncompressed_size: int,
    compression_ratio: float,
) -> None:
    lines = [
        "DeadZone final ZIP report",
        f"final ZIP path: {zip_path}",
        f"output name: {zip_name}",
        f"style: {style}",
        f"codename: {codename}",
        f"Android version: {android}",
        f"build: {build}",
        f"compression: ZIP_DEFLATED level 9",
        f"compressed size: {compressed_size}",
        f"uncompressed size: {uncompressed_size}",
        f"compression ratio: {compression_ratio:.6f}",
        "included files:",
    ]
    lines.extend(f"- {name}" for name in included)
    lines.append("excluded files:")
    lines.extend(f"- {name}" for name in excluded)
    lines.append("flash scripts generated:")
    lines.extend(f"- {name}" for name in scripts)
    lines.append("validation result:")
    if validation_errors:
        lines.extend(f"- FAIL: {error}" for error in validation_errors)
    else:
        lines.append("- PASS")
    ws.reports.mkdir(parents=True, exist_ok=True)
    (ws.reports / "final_zip_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_final_zip(ws: Workspace, info: RomInfo, style_key: str) -> Path:
    style = STYLE_LABELS[style_key]
    meta = {
        "rom_info.json": read_json(ws.meta / "rom_info.json", {}),
        "device_info.json": read_json(ws.meta / "device_info.json", {}),
        "super_layout.json": read_json(ws.meta / "super_layout.json", {}),
    }
    codename = _metadata_value(meta, "codename", info.codename if info.codename != "unknown" else "codename")
    android = _metadata_value(meta, "android_version", info.android_version)
    build = _metadata_value(meta, "build", info.build)
    soc = _metadata_value(meta, "soc", info.soc).lower()
    slot_mode = _metadata_value(meta, "slot_mode", info.slot_mode)
    profile = _load_profile(soc)
    profile_super = _profile_super(profile)
    size_policy = load_policy(ws)
    zip_name = f"DeadZone_{style}_{codename}_{_android_tag(android)}.zip"

    stage = ws.final / "stage"
    if stage.exists():
        shutil.rmtree(stage)
    (stage / "images").mkdir(parents=True)

    patch_vbmeta_images(ws.images, ws.reports, ws.meta)
    included_images, excluded = _copy_images(ws, stage, profile_super)
    included_tools = _copy_windows_tools(stage)
    flash_images = _flash_order(included_images, profile_super)
    scripts = _write_scripts(stage, style, codename, android, build, flash_images, slot_mode)

    out = ws.final / zip_name
    if out.exists():
        out.unlink()
    uncompressed_size = sum(path.stat().st_size for path in stage.rglob("*") if path.is_file())
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(stage.rglob("*")):
            if path.is_file():
                arcname = str(path.relative_to(stage)).replace(os.sep, "/")
                zf.write(path, arcname, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    included = [f"images/{name}" for name in included_images] + included_tools + scripts
    validation_errors = _validate_zip(out, included_images, profile_super, (ws.images / "super.img").is_file())
    compressed_size = out.stat().st_size
    compression_ratio = (compressed_size / uncompressed_size) if uncompressed_size else 0.0
    _write_report(
        ws,
        out,
        zip_name,
        style,
        codename,
        android,
        build,
        included,
        excluded,
        scripts,
        validation_errors,
        compressed_size,
        uncompressed_size,
        compression_ratio,
    )
    if validation_errors:
        raise RuntimeError("final ZIP validation failed: " + "; ".join(validation_errors))

    sha = _sha256(out)
    _write_sidecars(ws, out, sha, style, codename, android, build)
    write_json(ws.meta / "final_zip.json", {
        "zip": str(out),
        "sha256": sha,
        "images": included_images,
        "compressed_size": compressed_size,
        "uncompressed_size": uncompressed_size,
        "compression_ratio": compression_ratio,
        "compression": "ZIP_DEFLATED",
        "compresslevel": 9,
        "final_zip_max_bytes": size_policy.get("final_zip_max_bytes"),
    })
    print(f"[ZIP] {out}")
    print(f"[ZIP] compressed={compressed_size} uncompressed={uncompressed_size} ratio={compression_ratio:.6f}")
    return out
