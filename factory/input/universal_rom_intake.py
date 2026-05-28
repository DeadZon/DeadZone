"""Universal ROM intake for DeadZone Factory.

Entry point: analyze_rom(rom_path, rom_url, selected_codename) -> RomAnalysis

Aggregates all ROM detection, metadata parsing, and codename validation into
one rich result.  Designed so that no downstream stage needs to re-parse.

Metadata sources (tried in priority order):
  1. build.prop extracted from the archive  (via detect_rom_format)
  2. ROM filename                            (via parse_xiaomi_rom_metadata)
  3. Original ROM URL filename               (key: downloads are often renamed
                                              to source_rom.tgz by the workflow)
  4. selected_codename from workflow         (fallback for codename only)

Never relies solely on the local filename — downloaded ROMs may be renamed.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from factory.input.rom_detector import (
    FORMAT_FASTBOOT_TAR,
    FORMAT_FASTBOOT_TGZ,
    FORMAT_IMAGES_ZIP,
    FORMAT_NEW_DAT_BR_ZIP,
    FORMAT_PAYLOAD_OTA,
    FORMAT_RAW_SUPER_ZIP,
    FORMAT_SPLIT_SUPER_ZIP,
    FORMAT_UNKNOWN,
    FORMAT_XIAOMI_EU_ZIP,
    check_codename_match,
    detect_rom_format,
)
from factory.input.xiaomi_rom_metadata import parse_xiaomi_rom_metadata_from_sources


# ── Channel mapping ───────────────────────────────────────────────────────────

_REGION_CHANNEL: dict[str, str] = {
    "CN":        "CN",
    "Global":    "Global",
    "EEA":       "EEA",
    "India":     "India",
    "Russia":    "Russia",
    "Turkey":    "Turkey",
    "Indonesia": "Indonesia",
    "Taiwan":    "Taiwan",
}

# ROM format string → canonical rom_type label
_FORMAT_ROM_TYPE: dict[str, str] = {
    FORMAT_PAYLOAD_OTA:    "recovery",
    FORMAT_FASTBOOT_TGZ:   "fastboot",
    FORMAT_FASTBOOT_TAR:   "fastboot",
    FORMAT_XIAOMI_EU_ZIP:  "eu",
    FORMAT_SPLIT_SUPER_ZIP: "split_super",
    FORMAT_IMAGES_ZIP:     "images_zip",
    FORMAT_RAW_SUPER_ZIP:  "payload",
    FORMAT_NEW_DAT_BR_ZIP: "recovery",
}


# ── RomAnalysis dataclass ─────────────────────────────────────────────────────

@dataclass
class RomAnalysis:
    """Rich ROM analysis returned by analyze_rom()."""

    # Archive / format
    rom_format: str = FORMAT_UNKNOWN
    archive_type: str = "unknown"

    # Source
    source_url: Optional[str] = None
    local_path: Optional[Path] = None
    original_filename: str = ""

    # Codename
    detected_codename: Optional[str] = None
    selected_codename: str = ""
    codename_match: bool = False

    # Build metadata
    android_version: Optional[str] = None
    build_incremental: Optional[str] = None
    os_family: str = ""
    os_major: str = ""
    os_name: str = ""
    region: Optional[str] = None

    # Derived labels
    rom_channel: str = "Unknown"
    rom_type: str = "unknown"
    soc_guess: str = "auto"

    # Detection quality
    confidence: float = 0.0
    reason: str = ""

    # Audit
    metadata_sources_used: list = field(default_factory=list)
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)


# ── Internal helpers ──────────────────────────────────────────────────────────

def _rom_channel(region: Optional[str]) -> str:
    if not region:
        return "Unknown"
    return _REGION_CHANNEL.get(region, "Unknown")


def _url_basename(url: str) -> str:
    """Extract the filename portion of a URL."""
    if not url:
        return ""
    try:
        from urllib.parse import unquote, urlparse
        return Path(unquote(urlparse(url).path)).name
    except Exception:
        return ""


# ── Public API ─────────────────────────────────────────────────────────────────

def analyze_rom(
    rom_path: Optional[Path],
    rom_url: Optional[str],
    selected_codename: str,
    force_codename: bool = False,
) -> "RomAnalysis":
    """Analyze a ROM archive and return a rich RomAnalysis.

    Parameters
    ----------
    rom_path:
        Local path to the ROM archive (may be renamed to source_rom.tgz by
        the download step — the original name is recovered from rom_url).
    rom_url:
        Original source URL (used to recover the original ROM filename for
        metadata parsing even when the local file was renamed).
    selected_codename:
        Codename from workflow selection — the source of truth.
    force_codename:
        When True, codename mismatch is a warning rather than an error.
    """
    result = RomAnalysis(
        source_url=rom_url,
        local_path=Path(rom_path) if rom_path else None,
        selected_codename=selected_codename,
    )

    # ── Step 1: Detect ROM format by inspecting the archive ───────────────────
    if rom_path is None or not Path(rom_path).is_file():
        result.errors.append(f"ROM file not found or not provided: {rom_path}")
        result.reason = "file not found"
        return result

    detection = detect_rom_format(Path(rom_path))
    result.rom_format    = detection.rom_format
    result.archive_type  = detection.archive_type
    result.confidence    = detection.confidence
    result.reason        = detection.reason
    result.warnings.extend(detection.warnings)
    result.errors.extend(detection.errors)

    # ── Step 2: Parse metadata from multiple sources ──────────────────────────
    # The download step renames the ROM to source_rom.tgz, so we must try the
    # URL-derived filename first — it carries the original Xiaomi build string.
    local_name = Path(rom_path).name if rom_path else ""
    url_name   = _url_basename(rom_url or "")

    # original_filename: URL-derived name wins over local name
    result.original_filename = url_name or local_name

    # Multi-source metadata: URL filename → local filename → full URL
    parsed = parse_xiaomi_rom_metadata_from_sources(
        url_name,          # 1st: original name from URL (before rename)
        local_name,        # 2nd: local file name
        rom_url or "",     # 3rd: full URL as last resort
    )

    # Merge: detection build.prop takes priority; filename parsing fills gaps
    result.detected_codename  = detection.detected_device_codename  or parsed.get("codename")
    result.android_version    = detection.detected_android_version   or parsed.get("android_version")
    result.build_incremental  = (
        detection.detected_hyperos_or_miui_version or parsed.get("build_incremental")
    )
    result.region = detection.detected_region or parsed.get("region")

    result.os_family = parsed.get("os_family", "")
    result.os_major  = parsed.get("os_major", "")
    result.os_name   = parsed.get("os_name", "")

    # Track which sources contributed metadata
    sources: list[str] = []
    if detection.detected_device_codename or detection.detected_android_version:
        sources.append("build.prop")
    if parsed.get("metadata_source"):
        sources.append(parsed["metadata_source"])
    if selected_codename and not result.detected_codename:
        sources.append("selected_codename_fallback")
    result.metadata_sources_used = sources

    # ── Step 3: Codename match check ──────────────────────────────────────────
    codename_ok, codename_msg = check_codename_match(
        result.detected_codename, selected_codename, force=force_codename
    )
    result.codename_match = codename_ok
    if codename_msg and not codename_ok:
        result.errors.append(codename_msg)
    elif not codename_ok and force_codename:
        result.warnings.append(
            f"Codename mismatch (forced): detected={result.detected_codename!r} "
            f"selected={selected_codename!r}"
        )

    # ── Step 4: Derive labels ─────────────────────────────────────────────────
    result.rom_channel = _rom_channel(result.region)
    result.rom_type    = _FORMAT_ROM_TYPE.get(result.rom_format, "unknown")
    result.soc_guess   = "auto"   # expanded in future via device registry lookup

    return result


# ── Report writers ─────────────────────────────────────────────────────────────

def write_rom_analysis_report(result: "RomAnalysis", reports_dir: Path) -> Path:
    """Write output/reports/rom_analysis_report.txt."""
    reports_dir = Path(reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    out_path = reports_dir / "rom_analysis_report.txt"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "=" * 60,
        "  DeadZone Factory — ROM Analysis Report",
        "=" * 60,
        f"  Generated          : {ts}",
        "",
        "  Source:",
        f"    URL              : {result.source_url or '(none)'}",
        f"    Local path       : {result.local_path or '(none)'}",
        f"    Original filename: {result.original_filename or '(unknown)'}",
        "",
        "  Detection:",
        f"    ROM format       : {result.rom_format}",
        f"    Archive type     : {result.archive_type}",
        f"    ROM type         : {result.rom_type}",
        f"    Confidence       : {result.confidence:.2f}",
        f"    Reason           : {result.reason}",
        "",
        "  Metadata:",
        f"    Detected codename: {result.detected_codename or '(unknown)'}",
        f"    Selected codename: {result.selected_codename}",
        f"    Codename match   : {result.codename_match}",
        f"    Android version  : {result.android_version or '(unknown)'}",
        f"    Build incremental: {result.build_incremental or '(unknown)'}",
        f"    OS family        : {result.os_family or '(unknown)'}",
        f"    OS major         : {result.os_major or '(unknown)'}",
        f"    OS name          : {result.os_name or '(unknown)'}",
        f"    Region           : {result.region or '(unknown)'}",
        f"    ROM channel      : {result.rom_channel}",
        f"    SoC guess        : {result.soc_guess}",
        f"    Metadata sources : {', '.join(result.metadata_sources_used) or '(none)'}",
    ]
    if result.warnings:
        lines += ["", f"  Warnings ({len(result.warnings)}):"]
        for w in result.warnings:
            lines.append(f"    - {w}")
    if result.errors:
        lines += ["", f"  Errors ({len(result.errors)}):"]
        for e in result.errors:
            lines.append(f"    ! {e}")
    lines.append("=" * 60)

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path


def write_codename_validation_report(
    result: "RomAnalysis",
    reports_dir: Path,
    action_taken: str = "",
) -> Path:
    """Write output/reports/codename_validation_report.txt."""
    reports_dir = Path(reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    out_path = reports_dir / "codename_validation_report.txt"

    if action_taken:
        action = action_taken
    elif result.codename_match:
        action = "passed"
    elif not result.detected_codename:
        action = "skipped — no detected codename; continuing with selected"
    else:
        action = "failed — codename mismatch (use force to override)"

    lines = [
        "=" * 60,
        "  DeadZone Factory — Codename Validation Report",
        "=" * 60,
        f"  Selected codename  : {result.selected_codename}",
        f"  Detected codename  : {result.detected_codename or '(not detected)'}",
        f"  Metadata sources   : {', '.join(result.metadata_sources_used) or 'none'}",
        f"  Match              : {result.codename_match}",
        f"  Action taken       : {action}",
        "=" * 60,
    ]
    if result.errors:
        lines += ["", "  Errors:"]
        for e in result.errors:
            lines.append(f"    ! {e}")
    if result.warnings:
        lines += ["", "  Warnings:"]
        for w in result.warnings:
            lines.append(f"    - {w}")
    lines.append("=" * 60)

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path
