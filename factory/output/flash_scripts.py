"""Image-driven fastboot flash script generator for DeadZone.

Rules (per spec):
  - super.img    →  super  (no _ab suffix)
  - all others   →  <stem>_ab  (e.g. boot.img → boot_ab)

Scripts are generated from ACTUAL images present in images_dir.
Hardcoded image lists are NOT used to decide what to flash.

Hard restrictions (never in generated scripts):
  fastboot -w
  --disable-verity / --disable-verification
  lk1 / bootloader2 / tee1 / tee2 / scp1 / scp2

Preflight: every referenced image is verified to exist before
set_active, flash, or wipe. On any failure the script stops
immediately — no reboot, no wipe, device stays in fastboot.
Wipe (clean install only) runs AFTER all flash commands succeed.

Auto metadata: metadata_from_context() extracts FlashScriptMetadata
fields from a BuildContext produced by UnpackPipeline.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

BRAND: str = "DeadZone"
DEVELOPER: str = "Mezo"

SCRIPT_NAMES = [
    "windows_install_and_format_data.bat",
    "windows_install_upgrade.bat",
    "windows_format_data_only.bat",
]

# Ordered flash preference: images listed here flash in this order if present.
# Images NOT in this list but found in images_dir are appended alphabetically
# after, except super.img which always flashes last.
_PREFERRED_ORDER: list[str] = [
    "apusys.img",
    "audio_dsp.img",
    "boot.img",
    "ccu.img",
    "connsys_bt.img",
    "connsys_gnss.img",
    "connsys_wifi.img",
    "dpm.img",
    "dtbo.img",
    "gpueb.img",
    "gz.img",
    "init_boot.img",
    "lk.img",
    "logo.img",
    "mcf_ota.img",
    "mcupm.img",
    "md1img.img",
    "mvpu_algo.img",
    "pi_img.img",
    "preloader_raw.img",
    "scp.img",
    "spmfw.img",
    "sspm.img",
    "tee.img",
    "vbmeta.img",
    "vbmeta_system.img",
    "vbmeta_vendor.img",
    "vcp.img",
    "vendor_boot.img",
]

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

_SEP = "echo %C_CYAN%============================================================%C_RST%"
_BLK = "echo."

_EDITION_MAP: dict[str, str] = {
    "legend": "Legend",
    "gaming": "Gaming",
    "epic": "Epic",
    "base": "DeadZone",
    "deadzone": "DeadZone",
}


def metadata_from_context(ctx) -> dict:
    """Extract flash script keyword args from a BuildContext.

    Returns a dict suitable for unpacking into generate_windows_flash_scripts().
    Caller must still pass edition/soc/platform separately.
    """
    return {
        "device": getattr(ctx, "effective_device", None) or getattr(ctx, "factory_device", None),
        "device_model": getattr(ctx, "detected_device", None),
        "android_version": getattr(ctx, "android_version", None),
        "build_incremental": getattr(ctx, "mi_version", None),
    }


def _image_to_partition(image_name: str) -> str:
    """Derive fastboot partition name from image filename.

    super.img  →  super
    <stem>.img →  <stem>_ab
    """
    stem = Path(image_name).stem  # strip .img
    if stem == "super":
        return "super"
    return f"{stem}_ab"


def _collect_flash_commands(images_dir: Path) -> list[tuple[str, str]]:
    """Return (partition, image_filename) pairs from actual images present.

    Order: preferred list first (filtered to present), then alphabetical
    remainder, super.img always last.
    """
    images_dir = Path(images_dir)
    present = {f.name for f in images_dir.iterdir() if f.is_file() and f.suffix == ".img"}

    # Exclude unsparse intermediate files
    present = {n for n in present if "unsparse" not in n.lower()}

    ordered: list[str] = []
    for name in _PREFERRED_ORDER:
        if name in present:
            ordered.append(name)
            present.discard(name)

    # Remaining images not in preferred list (but present), alphabetical
    extras = sorted(n for n in present if n != "super.img")
    ordered.extend(extras)

    # super.img always last
    if "super.img" in present or (images_dir / "super.img").is_file():
        # super may already be removed from present set above
        ordered = [n for n in ordered if n != "super.img"]
        ordered.append("super.img")

    return [(_image_to_partition(name), name) for name in ordered]


# ── Metadata ──────────────────────────────────────────────────────────────────

@dataclass
class FlashScriptMetadata:
    edition: str = ""
    device_codename: str = ""
    device_model: str = ""
    os_name: str = ""
    android_version: str = ""
    build_incremental: str = ""
    region: str = ""
    image_count: int = 0

    @staticmethod
    def detect_os_name(incremental: str | None) -> str:
        if not incremental:
            return ""
        inc = incremental.upper()
        if "OS3" in inc:
            return "HyperOS 3"
        if "OS2" in inc:
            return "HyperOS 2"
        if "OS1" in inc:
            return "HyperOS 1"
        if "MIUI" in inc:
            return "MIUI"
        return ""

    @staticmethod
    def detect_region(incremental: str | None) -> str:
        if not incremental:
            return ""
        parts = incremental.upper().split(".")
        suffix = parts[-1] if parts else ""
        for key, region in _REGION_MAP.items():
            if suffix.endswith(key):
                return region
        return ""

    @classmethod
    def build(
        cls,
        edition: str | None = None,
        device_codename: str | None = None,
        device_model: str | None = None,
        android_version: str | None = None,
        build_incremental: str | None = None,
        image_count: int = 0,
    ) -> "FlashScriptMetadata":
        inc = (build_incremental or "").strip()
        edition_key = (edition or "base").strip().lower()
        # Strip deadzone_ prefix for lookup
        if edition_key.startswith("deadzone_"):
            edition_key = edition_key[len("deadzone_"):]
        edition_label = _EDITION_MAP.get(edition_key, "")
        os_name = cls.detect_os_name(inc)
        region = cls.detect_region(inc)
        resolved_model = (device_model or device_codename or "").strip()

        errors: list[str] = []
        if not edition_label:
            errors.append(f"edition {edition!r} does not map to a known label")
        if not device_codename or device_codename.lower() in ("unknown", ""):
            errors.append("device_codename is missing")
        if not resolved_model or resolved_model.lower() in ("unknown", ""):
            errors.append("device_model is missing")
        if not os_name:
            errors.append(f"OS name could not be determined from build_incremental={inc!r}")
        if not android_version or android_version.lower() in ("unknown", ""):
            errors.append("android_version is missing")
        if not inc or inc.lower() in ("unknown", ""):
            errors.append("build_incremental is missing")
        if not region:
            errors.append(f"region could not be determined from build_incremental={inc!r}")
        if errors:
            raise ValueError(
                "flash script metadata validation failed:\n"
                + "\n".join(f"  - {e}" for e in errors)
            )
        return cls(
            edition=edition_label,
            device_codename=device_codename,
            device_model=resolved_model,
            os_name=os_name,
            android_version=android_version,
            build_incremental=inc,
            region=region,
            image_count=image_count,
        )


# ── BAT builders ──────────────────────────────────────────────────────────────

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
        "chcp 65001 >nul",  # UTF-8 code page — required for banner box-drawing characters
        f"title {BRAND} by {DEVELOPER}  ^|  {mode_label}  ^|  {meta.device_codename}",
        "color 0B",
        "setlocal enabledelayedexpansion",
        "cd /d \"%~dp0\"",
        "set \"fastboot=bin\\windows\\fastboot.exe\"",
        *_ansi_setup(),
        "md \"flash_logs\" 2>nul",
        "for /f \"delims=\" %%T in ('powershell -nologo -noprofile -command"
        " \"Get-Date -Format yyyyMMdd_HHmmss\"') do set \"_TS=%%T\"",
        f"set \"LOG_FILE=flash_logs\\deadzone_{log_mode}_%_TS%.log\"",
        f"echo [%DATE% %TIME%] {BRAND} {mode_label} START > \"%LOG_FILE%\"",
        "cls",
        # ── Banner ──────────────────────────────────────────────────────────
        "echo %C_CYAN%",
        "echo  ██████╗ ███████╗ █████╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗███████╗",
        "echo  ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║██╔════╝",
        "echo  ██║  ██║█████╗  ███████║██║  ██║  ███╔╝ ██║   ██║██╔██╗ ██║█████╗  ",
        "echo  ██║  ██║██╔══╝  ██╔══██║██║  ██║ ███╔╝  ██║   ██║██║╚██╗██║██╔══╝  ",
        "echo  ██████╔╝███████╗██║  ██║██████╔╝███████╗╚██████╔╝██║ ╚████║███████╗",
        "echo  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝",
        "echo %C_RST%",
        _SEP,
        f"echo   {BRAND} Fastboot Installer",
        f"echo   Developer  : {DEVELOPER}",
        _BLK,
        f"echo   Device     : {meta.device_codename}",
        f"echo   Model      : {meta.device_model}",
        f"echo   Edition    : {meta.edition}",
        f"echo   OS         : {meta.os_name}",
        f"echo   Android    : {meta.android_version}",
        f"echo   Build      : {meta.build_incremental}",
        f"echo   Region     : {meta.region}",
        _BLK,
        f"echo   Mode       : %C_YELLOW%{mode_label}%C_RST%",
        f"echo   Images     : {meta.image_count}",
        _SEP,
        _BLK,
        # ── Pre-flight: fastboot binary ───────────────────────────────────
        "if not exist \"%fastboot%\" (",
        "    echo %C_RED%[FAILED] fastboot.exe not found at: %fastboot%%C_RST%",
        "    echo [%DATE% %TIME%] PREFLIGHT: fastboot.exe not found >> \"%LOG_FILE%\" 2>nul",
        "    goto :fail",
        ")",
        # ── Pre-flight: images folder ────────────────────────────────────
        "if not exist \"images\" (",
        "    echo %C_RED%[FAILED] images\\ folder not found in script directory.%C_RST%",
        "    echo [%DATE% %TIME%] PREFLIGHT: images folder missing >> \"%LOG_FILE%\" 2>nul",
        "    goto :fail",
        ")",
        # ── Device detection ─────────────────────────────────────────────
        _SEP,
        "echo   [SECTION] Device Detection",
        _SEP,
        "echo %C_YELLOW%[CHECK]%C_RST% Looking for device in fastboot mode ...",
        "call :run \"%fastboot% devices\"",
        "if errorlevel 1 goto :fail",
        "set \"detected=\"",
        "for /f \"tokens=2\" %%D in ('\"%fastboot%\" getvar product 2^>^&1"
        " ^| findstr /l /b /c:\"product:\"') do set \"detected=%%D\"",
        "if not defined detected (",
        "    echo %C_RED%[FAILED] No device detected in fastboot mode.%C_RST%",
        "    echo %C_YELLOW%  Make sure:  adb reboot bootloader  was run first.%C_RST%",
        "    goto :fail",
        ")",
        "echo %C_GREEN%[OK]%C_RST% Connected device: %detected%",
        "echo [%DATE% %TIME%] Device: %detected% >> \"%LOG_FILE%\" 2>nul",
        _BLK,
    ]


def _preflight_image_checks(commands: list[tuple[str, str]]) -> list[str]:
    lines: list[str] = [
        _SEP,
        "echo   [SECTION] Pre-flight Image Verification",
        _SEP,
    ]
    for _, image in commands:
        lines += [
            f"if not exist \"images\\{image}\" (",
            f"    echo %C_RED%[MISSING]%C_RST% images\\{image}",
            f"    goto :missing_image",
            f")",
        ]
    lines += [
        "echo %C_GREEN%[OK]%C_RST% All required images present.",
        _BLK,
    ]
    return lines


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
        f"echo %C_GREEN%  SUCCESS: {message}%C_RST%",
        "echo   Rebooting device to system ...",
        _SEP,
        "echo [%DATE% %TIME%] SUCCESS >> \"%LOG_FILE%\" 2>nul",
        "call :run \"%fastboot% reboot\"",
        "if errorlevel 1 goto :fail",
        "exit /b 0",
        "",
        # ── :run subroutine — logs every command + exit code ──────────────
        ":run",
        "echo %C_YELLOW%[RUN]%C_RST% %~1",
        "echo [%TIME%] RUN: %~1 >> \"%LOG_FILE%\" 2>nul",
        "%~1",
        "set \"_ERR=%errorlevel%\"",
        "echo [%TIME%] EXIT=%_ERR% >> \"%LOG_FILE%\" 2>nul",
        "if %_ERR% neq 0 exit /b 1",
        "exit /b 0",
        "",
        # ── :fail — strict handler: no reboot, no wipe on failure ─────────
        ":fail",
        "color 0C",
        _BLK,
        "echo %C_RED%============================================================%C_RST%",
        "echo %C_RED%  FAILED — A command returned a non-zero exit code.%C_RST%",
        "echo %C_RED%============================================================%C_RST%",
        "echo.",
        "echo   Do NOT disconnect or reboot the device.",
        "echo   Keep the phone in fastboot mode.",
        "echo   Review the output above and the log file before taking any action.",
        "echo.",
        "echo   Log: %LOG_FILE%",
        "echo %C_RED%============================================================%C_RST%",
        "echo [%DATE% %TIME%] FAILED >> \"%LOG_FILE%\" 2>nul",
        "exit /b 1",
        "",
        # ── :missing_image — preflight guard ─────────────────────────────
        ":missing_image",
        "color 0C",
        _BLK,
        "echo %C_RED%============================================================%C_RST%",
        "echo %C_RED%  FAILED — A required image file is missing from images\\.%C_RST%",
        "echo %C_RED%============================================================%C_RST%",
        "echo.",
        "echo   Do NOT disconnect or reboot the device.",
        "echo   Keep the phone in fastboot mode.",
        "echo.",
        "echo   Log: %LOG_FILE%",
        "echo %C_RED%============================================================%C_RST%",
        "echo [%DATE% %TIME%] MISSING_IMAGE >> \"%LOG_FILE%\" 2>nul",
        "exit /b 1",
    ]


def _script_text(kind: str, commands: list[tuple[str, str]], meta: FlashScriptMetadata) -> str:
    if kind == "clean":
        lines = _bat_header(meta, "Clean Install and Format Data")
        lines += _preflight_image_checks(commands)
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
        lines += _preflight_image_checks(commands)
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
        raise ValueError(f"Unknown script kind: {kind!r}")
    return "\r\n".join(lines) + "\r\n"


# ── Public API ────────────────────────────────────────────────────────────────

def generate_windows_flash_scripts(
    staging_dir: Path,
    images_dir: Path,
    device: str | None = None,
    soc: str | None = None,
    platform: str | None = None,
    edition: str | None = None,
    flavor: str | None = None,        # alias for edition, accepted for compat
    device_model: str | None = None,
    android_version: str | None = None,
    build_incremental: str | None = None,
    execute: bool = False,
) -> dict:
    """Generate three flash BAT scripts from actual images in images_dir.

    edition / flavor: accepts "base", "gaming", "legend", "epic",
    or prefixed forms like "deadzone_legend".
    """
    staging_dir = Path(staging_dir)
    images_dir = Path(images_dir)

    resolved_edition = edition or flavor or "base"
    commands = _collect_flash_commands(images_dir) if images_dir.is_dir() else []

    try:
        meta = FlashScriptMetadata.build(
            edition=resolved_edition,
            device_codename=device,
            device_model=device_model,
            android_version=android_version,
            build_incremental=build_incremental,
            image_count=len(commands),
        )
    except ValueError as exc:
        return {
            "status": "FAILED",
            "error": str(exc),
            "scripts_generated": [],
            "flash_commands": [],
            "flash_command_count": 0,
        }

    scripts = {
        "windows_install_and_format_data.bat": _script_text("clean", commands, meta),
        "windows_install_upgrade.bat": _script_text("upgrade", commands, meta),
        "windows_format_data_only.bat": _script_text("format", commands, meta),
    }

    generated = []
    if execute:
        staging_dir.mkdir(parents=True, exist_ok=True)
        for name, text in scripts.items():
            # UTF-8 with BOM so cmd.exe on Windows 10/11 renders the banner correctly.
            (staging_dir / name).write_text(text, encoding="utf-8-sig", newline="")
            generated.append(name)
    else:
        generated = list(scripts)

    return {
        "status": "APPLIED" if execute else "DRY_RUN",
        "scripts_generated": generated,
        "flash_commands": [{"partition": p, "image": i} for p, i in commands],
        "flash_command_count": len(commands),
    }


# ── Module-level ordered flash map and MTK validation ─────────────────────────
# Defined here (after _image_to_partition and _PREFERRED_ORDER) so the list
# comprehension can resolve both names at module load time.

# Ordered (partition_target, image_filename) pairs for the flash sequence.
# super.img always flashes last; all others derive partition via <stem>_ab rule.
FLASH_ORDER: list[tuple[str, str]] = [
    (_image_to_partition(name), name)
    for name in _PREFERRED_ORDER
] + [("super", "super.img")]

# MTK VAB firmware images required to be present before packaging.
MTK_VAB_REQUIRED_IMAGES: list[str] = [
    "super.img",
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "vbmeta.img",
    "vbmeta_system.img",
    "dtbo.img",
    "lk.img",
    "tee.img",
    "scp.img",
    "sspm.img",
    "gz.img",
    "logo.img",
]


def validate_mtk_required_images(images_dir: Path) -> list[str]:
    """Return filenames from MTK_VAB_REQUIRED_IMAGES that are absent from images_dir."""
    images_dir = Path(images_dir)
    present = {p.name for p in images_dir.glob("*.img") if p.is_file()} if images_dir.is_dir() else set()
    return [name for name in MTK_VAB_REQUIRED_IMAGES if name not in present]
