from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

# ── Fixed brand constants — only these two values are hardcoded ──────────────
BRAND: str = "DeadZone"
DEVELOPER: str = "Mezo"

SCRIPT_NAMES = [
    "windows_install_and_format_data.bat",
    "windows_install_upgrade.bat",
    "windows_format_data_only.bat",
]

MTK_VAB_REQUIRED_IMAGES: list[str] = [
    "apusys.img",
    "audio_dsp.img",
    "ccu.img",
    "connsys_bt.img",
    "connsys_gnss.img",
    "connsys_wifi.img",
    "dpm.img",
    "gpueb.img",
    "gz.img",
    "mcf_ota.img",
    "mcupm.img",
    "md1img.img",
    "mvpu_algo.img",
    "pi_img.img",
    "scp.img",
    "spmfw.img",
    "sspm.img",
    "tee.img",
    "vcp.img",
    "boot.img",
    "dtbo.img",
    "init_boot.img",
    "lk.img",
    "logo.img",
    "vendor_boot.img",
    "vbmeta.img",
    "vbmeta_system.img",
    "vbmeta_vendor.img",
    "super.img",
]

FLASH_ORDER: list[tuple[str, str]] = [
    ("apusys_ab", "apusys.img"),
    ("audio_dsp_ab", "audio_dsp.img"),
    ("boot_ab", "boot.img"),
    ("ccu_ab", "ccu.img"),
    ("connsys_bt_ab", "connsys_bt.img"),
    ("connsys_gnss_ab", "connsys_gnss.img"),
    ("connsys_wifi_ab", "connsys_wifi.img"),
    ("dpm_ab", "dpm.img"),
    ("dtbo_ab", "dtbo.img"),
    ("gpueb_ab", "gpueb.img"),
    ("gz_ab", "gz.img"),
    ("init_boot_ab", "init_boot.img"),
    ("lk_ab", "lk.img"),
    ("logo_ab", "logo.img"),
    ("mcf_ota_ab", "mcf_ota.img"),
    ("mcupm_ab", "mcupm.img"),
    ("md1img_ab", "md1img.img"),
    ("mvpu_algo_ab", "mvpu_algo.img"),
    ("pi_img_ab", "pi_img.img"),
    ("preloader_raw_ab", "preloader_raw.img"),
    ("scp_ab", "scp.img"),
    ("spmfw_ab", "spmfw.img"),
    ("sspm_ab", "sspm.img"),
    ("tee_ab", "tee.img"),
    ("vbmeta_ab", "vbmeta.img"),
    ("vbmeta_system_ab", "vbmeta_system.img"),
    ("vbmeta_vendor_ab", "vbmeta_vendor.img"),
    ("vcp_ab", "vcp.img"),
    ("vendor_boot_ab", "vendor_boot.img"),
    ("super", "super.img"),
]

# Incremental suffix → region name.  Matched against the last dot-segment of
# ro.mi.os.version.incremental (e.g. "OS3.0.303.0.WNOCNXM" → "CNXM" → China).
_REGION_MAP: dict[str, str] = {
    "CNXM": "China",
    "MIXM": "Global",
    "EUXM": "EEA",
    "INXM": "India",
    "RUXM": "Russia",
    "TRXM": "Turkey",
    "TWXM": "Taiwan",
    "IDXM": "Indonesia",
}

# Reusable separator and blank-line batch lines (use in list literals)
_SEP = "echo %C_CYAN%============================================================%C_RST%"
_BLK = "echo."


# ── Metadata ─────────────────────────────────────────────────────────────────

@dataclass
class FlashScriptMetadata:
    """All per-ROM metadata injected into generated BAT headers."""

    flavor: str = "unknown"
    device_codename: str = "unknown"
    device_model: str = "unknown"
    os_name: str = "Unknown OS"
    android_version: str = "unknown"
    build_incremental: str = "unknown"
    region: str = "Unknown"
    image_count: int = 0

    @staticmethod
    def detect_os_name(incremental: str | None) -> str:
        if not incremental:
            return "Unknown OS"
        inc = incremental.upper()
        if "OS3" in inc:
            return "HyperOS 3"
        if "OS2" in inc:
            return "HyperOS 2"
        if "OS1" in inc:
            return "HyperOS 1"
        if "MIUI" in inc:
            return "MIUI"
        return "Unknown OS"

    @staticmethod
    def detect_region(incremental: str | None) -> str:
        if not incremental:
            return "Unknown"
        parts = incremental.upper().split(".")
        suffix = parts[-1] if parts else ""
        for key, region in _REGION_MAP.items():
            if suffix.endswith(key):
                return region
        return "Unknown"

    @classmethod
    def build(
        cls,
        flavor: str | None = None,
        device_codename: str | None = None,
        device_model: str | None = None,
        android_version: str | None = None,
        build_incremental: str | None = None,
        image_count: int = 0,
    ) -> "FlashScriptMetadata":
        inc = build_incremental or ""
        return cls(
            flavor=flavor or "unknown",
            device_codename=device_codename or "unknown",
            device_model=device_model or device_codename or "unknown",
            os_name=cls.detect_os_name(inc),
            android_version=android_version or "unknown",
            build_incremental=inc or "unknown",
            region=cls.detect_region(inc),
            image_count=image_count,
        )


# ── Helpers ───────────────────────────────────────────────────────────────────

def validate_mtk_required_images(images_dir: Path) -> list[str]:
    """Return names of MTK VAB required images absent from images_dir."""
    images_dir = Path(images_dir)
    return [name for name in MTK_VAB_REQUIRED_IMAGES if not (images_dir / name).is_file()]


def _present_flash_commands(images_dir: Path) -> list[tuple[str, str]]:
    return [(partition, image) for partition, image in FLASH_ORDER if (images_dir / image).is_file()]


# ── BAT section builders ──────────────────────────────────────────────────────

def _ansi_setup() -> list[str]:
    return [
        "for /f \"delims=\" %%e in ('echo prompt $E^|cmd') do set \"ESC=%%e\"",
        "set \"C_CYAN=%ESC%[96m\"",
        "set \"C_GREEN=%ESC%[92m\"",
        "set \"C_RED=%ESC%[91m\"",
        "set \"C_YELLOW=%ESC%[93m\"",
        "set \"C_RST=%ESC%[0m\"",
    ]


def _bat_header(meta: FlashScriptMetadata, mode_label: str) -> list[str]:
    log_mode = mode_label.lower().replace(" ", "_").replace("/", "_")
    return [
        "@echo off",
        f"title {BRAND} Fastboot Installer - {mode_label}",
        "color 0B",
        "setlocal",
        "cd /d \"%~dp0\"",
        "set \"fastboot=bin\\windows\\fastboot.exe\"",
        *_ansi_setup(),
        # Runtime log setup — log is created when user runs the BAT, never pre-generated
        "md \"flash_logs\" 2>nul",
        "for /f \"delims=\" %%T in ('powershell -nologo -noprofile -command \"Get-Date -Format yyyyMMdd_HHmmss\"') do set \"_TS=%%T\"",
        f"set \"LOG_FILE=flash_logs\\deadzone_{log_mode}_%_TS%.log\"",
        f"echo [%DATE% %TIME%] {BRAND} {mode_label} - START > \"%LOG_FILE%\"",
        "cls",
        _SEP,
        f"echo   {BRAND}",
        f"echo   Developer  : {DEVELOPER}",
        f"echo   Device     : {meta.device_codename}",
        f"echo   Model      : {meta.device_model}",
        f"echo   Flavor     : {meta.flavor}",
        f"echo   OS         : {meta.os_name}",
        f"echo   Android    : {meta.android_version}",
        f"echo   Build      : {meta.build_incremental}",
        f"echo   Region     : {meta.region}",
        f"echo   Images     : {meta.image_count}",
        f"echo   Mode       : {mode_label}",
        _SEP,
        _BLK,
        "if not exist \"%fastboot%\" (",
        "    echo %C_RED%[FAILED] fastboot.exe not found at: %fastboot%%C_RST%",
        "    goto :fail",
        ")",
        "if not exist \"images\" (",
        "    echo %C_RED%[FAILED] images folder not found.%C_RST%",
        "    goto :fail",
        ")",
        "echo %C_YELLOW%[CHECK]%C_RST% Detecting connected device ...",
        "call :run \"%fastboot% devices\"",
        "if errorlevel 1 goto :fail",
        "set \"detected=unknown\"",
        "for /f \"tokens=2\" %%D in ('\"%fastboot%\" getvar product 2^>^&1 ^| findstr /l /b /c:\"product:\"') do set \"detected=%%D\"",
        "if \"%detected%\"==\"unknown\" (",
        "    echo %C_RED%[FAILED] No device in fastboot mode detected.%C_RST%",
        "    goto :fail",
        ")",
        "echo %C_GREEN%[OK]%C_RST% Connected: %detected%",
        _BLK,
    ]


def _run_flash_commands(commands: list[tuple[str, str]]) -> list[str]:
    total = len(commands)
    lines: list[str] = [
        _SEP,
        "echo   [SECTION] Setting Active Slot",
        _SEP,
        "call :run \"%fastboot% set_active a\"",
        "if errorlevel 1 goto :fail",
        _BLK,
        _SEP,
        f"echo   [SECTION] Flashing {total} Image(s)",
        _SEP,
    ]
    for index, (partition, image) in enumerate(commands, start=1):
        step = f"{index:02d}/{total:02d}"
        lines.extend([
            f"echo %C_YELLOW%[{step}]%C_RST% Flashing {image} -^> {partition}",
            f"call :run \"%fastboot% flash {partition} images\\{image}\"",
            "if errorlevel 1 goto :fail",
        ])
    lines.append(_BLK)
    return lines


def _run_wipe_commands() -> list[str]:
    return [
        _SEP,
        "echo   [SECTION] Wiping Data Partitions",
        _SEP,
        "echo %C_YELLOW%[WIPE]%C_RST% Erasing metadata ...",
        "call :run \"%fastboot% erase metadata\"",
        "if errorlevel 1 goto :fail",
        "echo %C_YELLOW%[WIPE]%C_RST% Erasing userdata ...",
        "call :run \"%fastboot% erase userdata\"",
        "if errorlevel 1 goto :fail",
        _BLK,
    ]


def _success_footer(message: str) -> list[str]:
    return [
        "color 0A",
        _SEP,
        f"echo   SUCCESS: {message}",
        "echo   Rebooting device ...",
        _SEP,
        "echo [%DATE% %TIME%] SUCCESS >> \"%LOG_FILE%\" 2>nul",
        "call :run \"%fastboot% reboot\"",
        "if errorlevel 1 goto :fail",
        "exit /b 0",
        "",
        ":run",
        "echo %C_YELLOW%[RUN]%C_RST% %~1",
        "%~1",
        "set \"_ERR=%errorlevel%\"",
        "echo [%TIME%] %~1 exit=%_ERR% >> \"%LOG_FILE%\" 2>nul",
        "if %_ERR% neq 0 exit /b 1",
        "exit /b 0",
        "",
        ":fail",
        "color 0C",
        _BLK,
        "echo %C_RED%============================================================%C_RST%",
        "echo   FAILED. Do not disconnect the device.",
        "echo   Keep the phone in fastboot mode.",
        "echo   Review the command output above before taking any action.",
        "echo %C_RED%============================================================%C_RST%",
        "echo [%DATE% %TIME%] FAILED >> \"%LOG_FILE%\" 2>nul",
        "exit /b 1",
    ]


def _script_text(kind: str, commands: list[tuple[str, str]], meta: FlashScriptMetadata) -> str:
    if kind == "clean":
        lines = _bat_header(meta, "Clean Install and Format Data")
        lines += _run_flash_commands(commands)
        lines += _run_wipe_commands()
        lines += _success_footer("Clean install completed.")
    elif kind == "upgrade":
        lines = _bat_header(meta, "Upgrade Install")
        lines += [
            _SEP,
            "echo   [NOTE] Upgrade mode: userdata and metadata will NOT be erased.",
            _SEP,
            _BLK,
        ]
        lines += _run_flash_commands(commands)
        lines += _success_footer("Upgrade install completed.")
    elif kind == "format":
        lines = _bat_header(meta, "Format Data Only")
        lines += [
            _SEP,
            "echo   [SECTION] Setting Active Slot",
            _SEP,
            "call :run \"%fastboot% set_active a\"",
            "if errorlevel 1 goto :fail",
            _BLK,
        ]
        lines += _run_wipe_commands()
        lines += _success_footer("Format data completed.")
    else:
        raise ValueError(f"Unknown script kind: {kind}")
    return "\r\n".join(lines) + "\r\n"


def generate_windows_flash_scripts(
    staging_dir: Path,
    images_dir: Path,
    device: str | None = None,
    soc: str | None = None,
    platform: str | None = None,
    flavor: str | None = None,
    device_model: str | None = None,
    android_version: str | None = None,
    build_incremental: str | None = None,
    execute: bool = False,
) -> dict:
    staging_dir = Path(staging_dir)
    images_dir = Path(images_dir)
    commands = _present_flash_commands(images_dir)
    meta = FlashScriptMetadata.build(
        flavor=flavor,
        device_codename=device,
        device_model=device_model,
        android_version=android_version,
        build_incremental=build_incremental,
        image_count=len(commands),
    )
    scripts = {
        "windows_install_and_format_data.bat": _script_text("clean", commands, meta),
        "windows_install_upgrade.bat": _script_text("upgrade", commands, meta),
        "windows_format_data_only.bat": _script_text("format", commands, meta),
    }

    generated = []
    if execute:
        staging_dir.mkdir(parents=True, exist_ok=True)
        for name, text in scripts.items():
            path = staging_dir / name
            path.write_text(text, encoding="ascii", newline="")
            generated.append(name)
    else:
        generated = list(scripts)

    return {
        "status": "APPLIED" if execute else "DRY_RUN",
        "scripts_generated": generated,
        "flash_commands": [{"partition": partition, "image": image} for partition, image in commands],
        "flash_command_count": len(commands),
    }
