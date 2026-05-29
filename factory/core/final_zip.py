from __future__ import annotations

import hashlib
import os
import shutil
import stat
import zipfile
from pathlib import Path

from factory.core.detector import RomInfo
from factory.core.super_builder import DYNAMIC_IMAGES
from factory.core.style_runner import STYLE_LABELS
from factory.core.workspace import Workspace, write_json

CORE_IMAGES = {
    "super.img", "boot.img", "init_boot.img", "vendor_boot.img", "vbmeta.img",
    "vbmeta_system.img", "vbmeta_vendor.img", "dtbo.img", "logo.img",
}
PROFILE_FIRMWARE = {
    "mtk": {
        "preloader_raw.img", "lk.img", "tee.img", "scp.img", "sspm.img", "spmfw.img",
        "md1img.img", "audio_dsp.img", "pi_img.img", "dpm.img", "mcupm.img", "gz.img",
        "vcp.img", "connsys_bt.img", "connsys_wifi.img", "connsys_gnss.img",
    },
    "snapdragon": {
        "abl.img", "aop.img", "bluetooth.img", "cpucp.img", "devcfg.img", "dsp.img",
        "featenabler.img", "hyp.img", "imagefv.img", "keymaster.img", "modem.img",
        "qupfw.img", "tz.img", "uefi.img", "xbl.img", "xbl_config.img",
    },
}


def _tool_source(name: str) -> Path | None:
    for base in [Path("tools/helper/bin/windows"), Path("tools/helper"), Path("bin/windows")]:
        candidate = base / name
        if candidate.is_file():
            return candidate
    return None


def _ensure_windows_tools(stage: Path) -> None:
    dst = stage / "bin/windows"
    dst.mkdir(parents=True, exist_ok=True)
    for name in ["fastboot.exe", "AdbWinApi.dll", "AdbWinUsbApi.dll"]:
        src = _tool_source(name)
        target = dst / name
        if src:
            shutil.copy2(src, target)
        else:
            target.write_bytes(b"")


def _bat_header(info: RomInfo, style_label: str) -> str:
    return f"""@echo off
setlocal EnableExtensions
set FB=bin\\windows\\fastboot.exe
echo ============================================================
echo DeadZone by Mezo
echo Style: {style_label}
echo Device: {info.codename}
echo Android: {info.android_version}
echo Build: {info.build}
echo ============================================================
if not exist "%FB%" (
  echo [ERROR] fastboot.exe is missing.
  exit /b 1
)
"""


def _flash_line(partition: str, image: str) -> str:
    return f"""if not exist "images\\{image}" (
  echo [ERROR] Missing images\\{image}
  exit /b 1
)
"%FB%" flash {partition} "images\\{image}"
if errorlevel 1 (
  echo [ERROR] Flash failed: {partition}. Phone remains in fastboot.
  exit /b 1
)
"""


def _partition_for(image: str) -> str:
    stem = Path(image).stem
    return "super" if stem == "super" else f"{stem}_ab"


def _write_scripts(stage: Path, info: RomInfo, style_label: str, flash_images: list[str]) -> None:
    flash = "".join(_flash_line(_partition_for(img), img) for img in flash_images)
    upgrade = _bat_header(info, style_label) + flash + '"%FB%" reboot\r\nexit /b 0\r\n'
    clean = _bat_header(info, style_label) + flash + (
        '"%FB%" erase metadata\r\nif errorlevel 1 exit /b 1\r\n'
        '"%FB%" erase userdata\r\nif errorlevel 1 exit /b 1\r\n'
        '"%FB%" reboot\r\nexit /b 0\r\n'
    )
    wipe = _bat_header(info, style_label) + (
        '"%FB%" erase metadata\r\nif errorlevel 1 exit /b 1\r\n'
        '"%FB%" erase userdata\r\nif errorlevel 1 exit /b 1\r\n'
        'echo [OK] Format complete. Phone remains in fastboot until you reboot it.\r\nexit /b 0\r\n'
    )
    (stage / "windows_install_upgrade.bat").write_text(upgrade.replace("\n", "\r\n"), encoding="utf-8")
    (stage / "windows_install_and_format_data.bat").write_text(clean.replace("\n", "\r\n"), encoding="utf-8")
    (stage / "windows_format_data_only.bat").write_text(wipe.replace("\n", "\r\n"), encoding="utf-8")


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_final_zip(ws: Workspace, info: RomInfo, style_key: str) -> Path:
    style_label = STYLE_LABELS[style_key]
    android = f"A{str(info.android_version).split('.')[0]}" if info.android_version != "unknown" else "Axx"
    codename = info.codename if info.codename != "unknown" else "codename"
    zip_name = f"DeadZone_{style_label}_{codename}_{android}.zip"
    stage = ws.final / "stage"
    if stage.exists():
        shutil.rmtree(stage)
    (stage / "images").mkdir(parents=True)
    required = CORE_IMAGES | PROFILE_FIRMWARE.get(info.soc.lower(), set())
    has_super = (ws.images / "super.img").is_file()
    selected: list[str] = []
    for img in sorted(ws.images.glob("*.img")):
        if has_super and img.name in DYNAMIC_IMAGES:
            continue
        if img.name in required or img.name == "super.img":
            shutil.copy2(img, stage / "images" / img.name)
            selected.append(img.name)
    if "super.img" not in selected:
        raise RuntimeError("final ZIP requires images/super.img")
    _ensure_windows_tools(stage)
    flash_order = [n for n in selected if n != "super.img"] + ["super.img"]
    _write_scripts(stage, info, style_label, flash_order)
    out = ws.final / zip_name
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_STORED) as zf:
        for path in sorted(stage.rglob("*")):
            if path.is_file():
                zi = zipfile.ZipInfo(str(path.relative_to(stage)).replace(os.sep, "/"))
                zi.external_attr = (stat.S_IMODE(path.stat().st_mode) or 0o644) << 16
                zf.writestr(zi, path.read_bytes())
    sha = _sha256(out)
    (ws.final / f"{zip_name}.sha256").write_text(f"{sha}  {zip_name}\n", encoding="utf-8")
    write_json(ws.final / f"{zip_name}.build_info.json", {"zip": zip_name, "sha256": sha, "images": selected})
    write_json(ws.meta / "final_zip.json", {"zip": str(out), "sha256": sha, "images": selected})
    print(f"[ZIP] {out}")
    return out
