from __future__ import annotations

from pathlib import Path


SCRIPT_NAMES = [
    "windows_install_and_format_data.bat",
    "windows_install_upgrade.bat",
    "windows_format_data_only.bat",
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


def _present_flash_commands(images_dir: Path) -> list[tuple[str, str]]:
    return [(partition, image) for partition, image in FLASH_ORDER if (images_dir / image).is_file()]


def _bat_header(mode: str, device: str | None, soc: str | None, platform: str | None) -> list[str]:
    device_value = device or "unspecified"
    soc_value = soc or "unspecified"
    platform_value = platform or "unspecified"
    return [
        "@echo off",
        "title DeadZone Fastboot Installer - MEZO Developer",
        "color 0B",
        "setlocal",
        "cd /d \"%~dp0\"",
        "set \"fastboot=bin\\windows\\fastboot.exe\"",
        "cls",
        "echo ============================================================",
        "echo   DeadZone",
        "echo   MEZO Developer",
        "echo   Premium Fastboot Installer",
        "echo ============================================================",
        f"echo   Flash mode : {mode}",
        f"echo   Device     : {device_value}",
        f"echo   SOC        : {soc_value}",
        f"echo   Platform   : {platform_value}",
        "echo ============================================================",
        "echo.",
        "if not exist \"%fastboot%\" (",
        "    color 0C",
        "    echo [FAILED] fastboot.exe not found at: %fastboot%",
        "    goto :fail",
        ")",
        "if not exist \"images\" (",
        "    color 0C",
        "    echo [FAILED] images folder not found.",
        "    goto :fail",
        ")",
        "echo [SECTION] Device detection",
        "call :run \"%fastboot% devices\"",
        "if errorlevel 1 goto :fail",
        "set \"detected=unknown\"",
        "for /f \"tokens=2\" %%D in ('\"%fastboot%\" getvar product 2^>^&1 ^| findstr /l /b /c:\"product:\"') do set \"detected=%%D\"",
        "if \"%detected%\"==\"unknown\" (",
        "    color 0C",
        "    echo [FAILED] No device detected. Is fastboot mode active?",
        "    goto :fail",
        ")",
        "echo [OK] Connected device: %detected%",
        "echo.",
    ]


def _confirm_wipe() -> list[str]:
    return [
        "echo [SECTION] Data wipe confirmation",
        "echo This will erase userdata and metadata after flashing succeeds.",
        "echo Internal storage files will be deleted.",
        "set /p choice=Type Y to continue: ",
        "if /i not \"%choice%\"==\"Y\" (",
        "    echo [CANCELLED] No changes were made.",
        "    pause",
        "    exit /b 0",
        ")",
        "echo.",
    ]


def _run_flash_commands(commands: list[tuple[str, str]]) -> list[str]:
    lines = [
        "echo [SECTION] Flash mode",
        "echo [STEP] Setting active slot A",
        "call :run \"%fastboot% set_active a\"",
        "if errorlevel 1 goto :fail",
        "echo.",
        "echo [SECTION] Flashing images",
    ]
    for index, (partition, image) in enumerate(commands, start=1):
        lines.extend(
            [
                f"echo [STEP {index}] Flashing {partition} from {image}",
                f"call :run \"%fastboot% flash {partition} images\\{image}\"",
                "if errorlevel 1 goto :fail",
                "echo.",
            ]
        )
    return lines


def _run_wipe_commands() -> list[str]:
    return [
        "echo [SECTION] Format data",
        "echo [STEP] Erasing metadata",
        "call :run \"%fastboot% erase metadata\"",
        "if errorlevel 1 goto :fail",
        "echo [STEP] Erasing userdata",
        "call :run \"%fastboot% erase userdata\"",
        "if errorlevel 1 goto :fail",
        "echo.",
    ]


def _success_footer(message: str) -> list[str]:
    return [
        "color 0A",
        "echo ============================================================",
        f"echo   SUCCESS. {message}",
        "echo   Rebooting device now.",
        "echo ============================================================",
        "call :run \"%fastboot% reboot\"",
        "if errorlevel 1 goto :fail",
        "pause",
        "exit /b 0",
        "",
        ":run",
        "echo [RUN] %~1",
        "%~1",
        "if errorlevel 1 exit /b 1",
        "exit /b 0",
        "",
        ":fail",
        "color 0C",
        "echo.",
        "echo FAILED. Do not disconnect the device. Keep the phone in fastboot mode.",
        "echo Review the command output above before taking any action.",
        "pause",
        "exit /b 1",
    ]


def _script_text(kind: str, commands: list[tuple[str, str]], device: str | None, soc: str | None, platform: str | None) -> str:
    if kind == "clean":
        lines = _bat_header("Clean install and format data", device, soc, platform)
        lines += _confirm_wipe()
        lines += _run_flash_commands(commands)
        lines += _run_wipe_commands()
        lines += _success_footer("Clean install completed.")
    elif kind == "upgrade":
        lines = _bat_header("Upgrade install", device, soc, platform)
        lines += [
            "echo [SECTION] Upgrade mode",
            "echo Userdata and metadata will not be erased.",
            "pause",
            "echo.",
        ]
        lines += _run_flash_commands(commands)
        lines += _success_footer("Upgrade install completed.")
    elif kind == "format":
        lines = _bat_header("Format data only", device, soc, platform)
        lines += _confirm_wipe()
        lines += [
            "echo [SECTION] Format mode",
            "echo [STEP] Setting active slot A",
            "call :run \"%fastboot% set_active a\"",
            "if errorlevel 1 goto :fail",
            "echo.",
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
    execute: bool = False,
) -> dict:
    staging_dir = Path(staging_dir)
    images_dir = Path(images_dir)
    commands = _present_flash_commands(images_dir)
    scripts = {
        "windows_install_and_format_data.bat": _script_text("clean", commands, device, soc, platform),
        "windows_install_upgrade.bat": _script_text("upgrade", commands, device, soc, platform),
        "windows_format_data_only.bat": _script_text("format", commands, device, soc, platform),
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
