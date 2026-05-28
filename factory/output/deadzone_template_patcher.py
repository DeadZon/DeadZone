"""DeadZone_Mezo template patcher for dynamic image flash scripts.

Workflow:
  1. Validate selected_codename vs detected_codename (fail if mismatch unless force=True).
  2. Copy DeadZone_Mezo template directory to staging_dir.
  3. Clear staging_dir/images/ so caller can populate with final images.
  4. For each BAT/SH script in the staging copy:
     a. Replace the codename in the device-check line.
     b. Replace content between DEADZONE_BANNER markers with a colored banner.
     c. If DEADZONE_IMAGE_FLASH markers exist, replace that section with
        dynamically generated flash commands from actual images in images_dir.
  5. Write output/reports/dynamic_flash_script_report.txt.

Markers expected in template scripts:
  BAT:  :: DEADZONE_BANNER_START / :: DEADZONE_BANNER_END
        :: DEADZONE_IMAGE_FLASH_START / :: DEADZONE_IMAGE_FLASH_END
  SH:   # DEADZONE_BANNER_START / # DEADZONE_BANNER_END
        # DEADZONE_IMAGE_FLASH_START / # DEADZONE_IMAGE_FLASH_END

If a script lacks markers the patcher logs a warning and leaves that script unchanged.
"""
from __future__ import annotations

import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

from .dynamic_flash_commands import (
    bat_flash_lines,
    collect_commands,
    sh_flash_lines,
    skipped_images_report,
)

BRAND = "DeadZone"
DEVELOPER = "Mezo"

# ── Marker constants ──────────────────────────────────────────────────────────

_BAT_BANNER_START = ":: DEADZONE_BANNER_START"
_BAT_BANNER_END = ":: DEADZONE_BANNER_END"
_BAT_FLASH_START = ":: DEADZONE_IMAGE_FLASH_START"
_BAT_FLASH_END = ":: DEADZONE_IMAGE_FLASH_END"

_SH_BANNER_START = "# DEADZONE_BANNER_START"
_SH_BANNER_END = "# DEADZONE_BANNER_END"
_SH_FLASH_START = "# DEADZONE_IMAGE_FLASH_START"
_SH_FLASH_END = "# DEADZONE_IMAGE_FLASH_END"

_BANNER_ART = [
    "  ██████╗ ███████╗ █████╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗███████╗",
    "  ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║██╔════╝",
    "  ██║  ██║█████╗  ███████║██║  ██║  ███╔╝ ██║   ██║██╔██╗ ██║█████╗  ",
    "  ██║  ██║██╔══╝  ██╔══██║██║  ██║ ███╔╝  ██║   ██║██║╚██╗██║██╔══╝  ",
    "  ██████╔╝███████╗██║  ██║██████╔╝███████╗╚██████╔╝██║ ╚████║███████╗",
    "  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝",
]

_SEP = "============================================================"


# ── Codename validation ───────────────────────────────────────────────────────

def validate_codename(
    selected: str,
    detected: str | None,
    force: bool = False,
) -> tuple[bool, str | None]:
    """Check selected vs detected codename.

    Returns (match: bool, error_message: str | None).
    If force=True a mismatch returns match=False but error_message=None (warned, not hard-fail).
    """
    if not detected:
        return True, None
    if selected.lower() == detected.lower():
        return True, None
    msg = (
        f"Codename mismatch: selected={selected!r} detected={detected!r}. "
        f"Use force=True to override."
    )
    if force:
        return False, None  # mismatch but not a hard fail
    return False, msg


# ── Banner generators ─────────────────────────────────────────────────────────

def _bat_banner_lines(
    codename: str,
    edition: str,
    android_version: str,
    build_incremental: str,
    region: str,
    rom_format: str = "fastboot_tgz",
) -> list[str]:
    """Generate BAT lines to inject between DEADZONE_BANNER markers."""
    lines = [
        "for /f \"delims=\" %%e in ('echo prompt $E^|cmd') do set \"ESC=%%e\"",
        "set \"C_CYAN=%ESC%[96m\"",
        "set \"C_GREEN=%ESC%[92m\"",
        "set \"C_RED=%ESC%[91m\"",
        "set \"C_YELLOW=%ESC%[93m\"",
        "set \"C_RST=%ESC%[0m\"",
        "chcp 65001 >nul",
        "cls",
        "echo %C_CYAN%",
    ]
    for art_line in _BANNER_ART:
        lines.append(f"echo {art_line}")
    lines += [
        "echo %C_RST%",
        f"echo %C_CYAN%{_SEP}%C_RST%",
        f"echo   {BRAND} Fastboot Installer",
        f"echo   Developer  : {DEVELOPER}",
        "echo.",
        f"echo   Device     : {codename}",
        f"echo   Edition    : {edition}",
        f"echo   Android    : {android_version}",
        f"echo   Build      : {build_incremental}",
        f"echo   Region     : {region}",
        f"echo   ROM Format : {rom_format}",
        f"echo %C_CYAN%{_SEP}%C_RST%",
        "echo.",
    ]
    return lines


def _sh_banner_lines(
    codename: str,
    edition: str,
    android_version: str,
    build_incremental: str,
    region: str,
    rom_format: str = "fastboot_tgz",
) -> list[str]:
    """Generate SH lines to inject between DEADZONE_BANNER markers."""
    lines: list[str] = []
    lines.append("printf '\\033[0;96m\\n'")
    for art_line in _BANNER_ART:
        # Escape single quotes in art_line (there are none, but be safe)
        safe = art_line.replace("'", "'\\''")
        lines.append(f"printf '{safe}\\n'")
    lines.append("printf '\\033[0m\\n'")
    lines.append(f"printf '\\033[0;96m{_SEP}\\033[0m\\n'")
    lines.append(f"printf '  {BRAND} Fastboot Installer\\n'")
    lines.append(f"printf '  Developer  : {DEVELOPER}\\n'")
    lines.append("printf '\\n'")
    lines.append(f"printf '  Device     : {codename}\\n'")
    lines.append(f"printf '  Edition    : {edition}\\n'")
    lines.append(f"printf '  Android    : {android_version}\\n'")
    lines.append(f"printf '  Build      : {build_incremental}\\n'")
    lines.append(f"printf '  Region     : {region}\\n'")
    lines.append(f"printf '  ROM Format : {rom_format}\\n'")
    lines.append(f"printf '\\033[0;96m{_SEP}\\033[0m\\n'")
    lines.append("printf '\\n'")
    return lines


# ── Script patching helpers ───────────────────────────────────────────────────

def _replace_between_markers(
    lines: list[str],
    start_marker: str,
    end_marker: str,
    replacement: list[str],
) -> tuple[list[str], bool]:
    """Replace lines between start_marker and end_marker (inclusive) with replacement.

    Returns (new_lines, found).  If markers not found, returns original lines unchanged.
    """
    try:
        start_idx = next(i for i, l in enumerate(lines) if l.strip() == start_marker)
        end_idx = next(i for i, l in enumerate(lines) if i > start_idx and l.strip() == end_marker)
    except StopIteration:
        return lines, False
    new_lines = lines[:start_idx] + [start_marker] + replacement + [end_marker] + lines[end_idx + 1:]
    return new_lines, True


def _replace_codename_bat(lines: list[str], codename: str) -> list[str]:
    """Replace hardcoded codename in BAT device-check lines."""
    out = []
    for line in lines:
        # Pattern: if "%device%" neq "<old>" echo Compatible devices: <old> & pause & exit /B 1
        new = re.sub(
            r'(if "%device%" neq ")([^"]+)(" echo Compatible devices: )([^ &]+)(.*)',
            lambda m: f'{m.group(1)}{codename}{m.group(3)}{codename}{m.group(5)}',
            line,
        )
        out.append(new)
    return out


def _replace_codename_sh(lines: list[str], codename: str) -> list[str]:
    """Replace hardcoded codename in SH device-check lines."""
    out = []
    for line in lines:
        # Pattern: if [ "$device" != "<old>" ]; then echo "Compatible devices: <old>"; exit 1; fi
        new = re.sub(
            r'(if \[ "\$device" != ")([^"]+)(" \]; then echo "Compatible devices: )([^"]+)(".*)',
            lambda m: f'{m.group(1)}{codename}{m.group(3)}{codename}{m.group(5)}',
            line,
        )
        out.append(new)
    return out


def _patch_bat_script(
    script_path: Path,
    codename: str,
    banner_lines: list[str],
    flash_lines: list[str] | None,
) -> tuple[str, list[str]]:
    """Patch a BAT script in-place. Returns (patched_content, warnings)."""
    warnings: list[str] = []
    raw = script_path.read_text(encoding="utf-8-sig", errors="replace")
    # Normalise to LF for processing, then re-join with CRLF at end.
    lines = raw.replace("\r\n", "\n").replace("\r", "\n").splitlines()

    lines = _replace_codename_bat(lines, codename)

    lines, found_banner = _replace_between_markers(lines, _BAT_BANNER_START, _BAT_BANNER_END, banner_lines)
    if not found_banner:
        warnings.append(f"{script_path.name}: banner markers not found — banner not injected")

    if flash_lines is not None:
        lines, found_flash = _replace_between_markers(lines, _BAT_FLASH_START, _BAT_FLASH_END, flash_lines)
        if not found_flash:
            warnings.append(f"{script_path.name}: image flash markers not found — flash section not replaced")

    content = "\r\n".join(lines) + "\r\n"
    return content, warnings


def _patch_sh_script(
    script_path: Path,
    codename: str,
    banner_lines: list[str],
    flash_lines: list[str] | None,
) -> tuple[str, list[str]]:
    """Patch a SH script in-place. Returns (patched_content, warnings)."""
    warnings: list[str] = []
    raw = script_path.read_text(encoding="utf-8", errors="replace")
    lines = raw.replace("\r\n", "\n").replace("\r", "\n").splitlines()

    lines = _replace_codename_sh(lines, codename)

    lines, found_banner = _replace_between_markers(lines, _SH_BANNER_START, _SH_BANNER_END, banner_lines)
    if not found_banner:
        warnings.append(f"{script_path.name}: banner markers not found — banner not injected")

    if flash_lines is not None:
        lines, found_flash = _replace_between_markers(lines, _SH_FLASH_START, _SH_FLASH_END, flash_lines)
        if not found_flash:
            warnings.append(f"{script_path.name}: image flash markers not found — flash section not replaced")

    content = "\n".join(lines) + "\n"
    return content, warnings


# ── Report writer ─────────────────────────────────────────────────────────────

def _write_report(
    reports_dir: Path,
    selected_codename: str,
    detected_codename: str | None,
    codename_match: bool,
    force: bool,
    final_images: list[str],
    flash_commands: list[tuple[str, str]],
    skipped: list[dict],
    warnings: list[str],
    errors: list[str],
    edition: str,
    android_version: str,
    build_incremental: str,
    region: str,
) -> Path:
    reports_dir.mkdir(parents=True, exist_ok=True)
    out_path = reports_dir / "dynamic_flash_script_report.txt"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "=== DeadZone Dynamic Flash Script Report ===",
        f"Generated : {ts}",
        "",
        "--- Codename ---",
        f"Selected   : {selected_codename}",
        f"Detected   : {detected_codename or '(not provided)'}",
        f"Match      : {codename_match}",
        f"Force      : {force}",
        "",
        "--- Build Metadata ---",
        f"Edition    : {edition}",
        f"Android    : {android_version}",
        f"Build      : {build_incremental}",
        f"Region     : {region}",
        "",
        "--- Template ---",
        "Template used        : DeadZone_Mezo",
        "Flash method changed : false",
        "",
        f"--- Final Images ({len(final_images)}) ---",
    ]
    for img in sorted(final_images):
        lines.append(f"  {img}")
    lines += [
        "",
        f"--- Generated Flash Commands ({len(flash_commands)}) ---",
    ]
    for partition, image in flash_commands:
        lines.append(f"  fastboot flash {partition} images/{image}")
    lines += [
        "",
        f"--- Skipped Images ({len(skipped)}) ---",
    ]
    for entry in skipped:
        lines.append(f"  {entry['image']}  ({entry['reason']})")
    if warnings:
        lines += ["", f"--- Warnings ({len(warnings)}) ---"]
        for w in warnings:
            lines.append(f"  WARNING: {w}")
    if errors:
        lines += ["", f"--- Errors ({len(errors)}) ---"]
        for e in errors:
            lines.append(f"  ERROR: {e}")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


# ── Script classification ─────────────────────────────────────────────────────

# Scripts that contain an image flash section (need DEADZONE_IMAGE_FLASH markers replaced)
_FLASH_SCRIPTS: frozenset[str] = frozenset({
    "windows_install_and_format_data.bat",
    "windows_install_upgrade.bat",
    "linux_install_and_format_data.sh",
    "linux_install_upgrade.sh",
    "macos_install_and_format_data.sh",
    "macos_install_upgrade.sh",
})

# All scripts that receive a banner
_ALL_SCRIPTS: frozenset[str] = frozenset({
    "windows_install_and_format_data.bat",
    "windows_install_upgrade.bat",
    "windows_format_data_only.bat",
    "linux_install_and_format_data.sh",
    "linux_install_upgrade.sh",
    "linux_format_data_only.sh",
    "macos_install_and_format_data.sh",
    "macos_install_upgrade.sh",
    "macos_format_data_only.sh",
})


# ── Public API ────────────────────────────────────────────────────────────────

def patch_deadzone_template(
    template_dir: Path,
    staging_dir: Path,
    images_dir: Path,
    selected_codename: str,
    detected_codename: str | None = None,
    edition: str = "Free",
    android_version: str = "",
    build_incremental: str = "",
    region: str = "",
    rom_format: str = "fastboot_tgz",
    force: bool = False,
    execute: bool = False,
    reports_dir: Path | None = None,
) -> dict:
    """Patch DeadZone_Mezo template with dynamic image flash commands.

    Parameters
    ----------
    template_dir:       Path to DeadZone_Mezo source directory.
    staging_dir:        Destination for the patched copy.
    images_dir:         Directory containing final .img files to flash.
    selected_codename:  Codename from workflow selection (source of truth).
    detected_codename:  Codename detected from ROM filename / build metadata.
    edition:            Edition label (Free, Legend, …).
    android_version:    Android version string (e.g. "16.0").
    build_incremental:  Build string (e.g. "OS3.0.303.0.WOKCNXM").
    region:             Region string (e.g. "CN", "Global").
    rom_format:         ROM format tag for banner (default "fastboot_tgz").
    force:              If True, codename mismatch is a warning, not an error.
    execute:            If False, performs a dry-run (no files written).
    reports_dir:        Where to write dynamic_flash_script_report.txt.
    """
    template_dir = Path(template_dir)
    staging_dir = Path(staging_dir)
    images_dir = Path(images_dir)
    if reports_dir:
        reports_dir = Path(reports_dir)

    errors: list[str] = []
    warnings: list[str] = []

    # 1. Codename validation
    codename_match, codename_error = validate_codename(selected_codename, detected_codename, force)
    if codename_error:
        errors.append(codename_error)
        report_path = None
        if reports_dir:
            report_path = _write_report(
                reports_dir, selected_codename, detected_codename, codename_match, force,
                [], [], [], warnings, errors, edition, android_version, build_incremental, region,
            )
        return {
            "status": "FAILED",
            "errors": errors,
            "warnings": warnings,
            "codename_match": codename_match,
            "report_file": str(report_path) if report_path else None,
        }
    if not codename_match:
        warnings.append(
            f"Codename mismatch (force=True): selected={selected_codename!r} "
            f"detected={detected_codename!r}"
        )

    # 2. Collect flash commands from final images
    if images_dir.is_dir():
        commands = collect_commands(images_dir)
        skipped = skipped_images_report(images_dir)
        final_images = [f.name for f in images_dir.iterdir() if f.is_file() and f.suffix == ".img"]
    else:
        commands = []
        skipped = []
        final_images = []
        warnings.append(f"images_dir not found: {images_dir}")

    # 3. Validate: exactly one super.img
    super_variants = [n for n in final_images if n.lower().startswith("super")]
    if "super.img" not in final_images:
        errors.append("final images must contain exactly one super.img")
    bad_super = [n for n in super_variants if n != "super.img"]
    if bad_super:
        errors.append(f"forbidden super artifacts in images_dir: {bad_super}")

    # 4. Validate: no fastboot -w in generated commands
    all_cmd_lines = bat_flash_lines(commands) + sh_flash_lines(commands)
    if any("-w" in line for line in all_cmd_lines):
        errors.append("generated flash commands contain forbidden fastboot -w")

    # Dry-run: return planned output without writing
    if not execute:
        planned_scripts = list(_ALL_SCRIPTS)
        report_path = None
        if reports_dir:
            report_path = _write_report(
                reports_dir, selected_codename, detected_codename, codename_match, force,
                final_images, commands, skipped, warnings, errors,
                edition, android_version, build_incremental, region,
            )
        return {
            "status": "DRY_RUN" if not errors else "FAILED",
            "codename_match": codename_match,
            "codename_selected": selected_codename,
            "codename_detected": detected_codename,
            "flash_commands": [{"partition": p, "image": i} for p, i in commands],
            "flash_command_count": len(commands),
            "final_images": sorted(final_images),
            "skipped_images": skipped,
            "scripts_patched": planned_scripts,
            "warnings": warnings,
            "errors": errors,
            "report_file": str(report_path) if report_path else None,
        }

    if errors:
        report_path = None
        if reports_dir:
            report_path = _write_report(
                reports_dir, selected_codename, detected_codename, codename_match, force,
                final_images, commands, skipped, warnings, errors,
                edition, android_version, build_incremental, region,
            )
        return {
            "status": "FAILED",
            "errors": errors,
            "warnings": warnings,
            "codename_match": codename_match,
            "report_file": str(report_path) if report_path else None,
        }

    # 5. Copy template to staging
    if staging_dir.exists():
        shutil.rmtree(staging_dir)
    shutil.copytree(template_dir, staging_dir)

    # Clear images dir — caller populates it with final images
    staged_images = staging_dir / "images"
    if staged_images.exists():
        shutil.rmtree(staged_images)
    staged_images.mkdir(parents=True)

    # 6. Build banner + flash lines for each platform
    bat_banner = _bat_banner_lines(
        selected_codename, edition, android_version, build_incremental, region, rom_format
    )
    sh_banner = _sh_banner_lines(
        selected_codename, edition, android_version, build_incremental, region, rom_format
    )
    bat_flash = bat_flash_lines(commands)
    sh_flash = sh_flash_lines(commands)

    # 7. Patch each script
    scripts_patched: list[str] = []
    for script_name in sorted(_ALL_SCRIPTS):
        script_path = staging_dir / script_name
        if not script_path.is_file():
            warnings.append(f"Script not found in staging: {script_name}")
            continue

        is_flash_script = script_name in _FLASH_SCRIPTS
        is_bat = script_name.endswith(".bat")

        if is_bat:
            flash_arg = bat_flash if is_flash_script else None
            content, script_warns = _patch_bat_script(
                script_path, selected_codename, bat_banner, flash_arg
            )
            script_path.write_text(content, encoding="utf-8-sig", newline="")
        else:
            flash_arg = sh_flash if is_flash_script else None
            content, script_warns = _patch_sh_script(
                script_path, selected_codename, sh_banner, flash_arg
            )
            script_path.write_text(content, encoding="utf-8", newline="")

        warnings.extend(script_warns)
        scripts_patched.append(script_name)

    # 8. Write report
    report_path = None
    if reports_dir:
        report_path = _write_report(
            reports_dir, selected_codename, detected_codename, codename_match, force,
            final_images, commands, skipped, warnings, errors,
            edition, android_version, build_incremental, region,
        )

    return {
        "status": "APPLIED",
        "codename_match": codename_match,
        "codename_selected": selected_codename,
        "codename_detected": detected_codename,
        "flash_commands": [{"partition": p, "image": i} for p, i in commands],
        "flash_command_count": len(commands),
        "final_images": sorted(final_images),
        "skipped_images": skipped,
        "scripts_patched": scripts_patched,
        "staging_dir": str(staging_dir),
        "warnings": warnings,
        "errors": errors,
        "report_file": str(report_path) if report_path else None,
    }
