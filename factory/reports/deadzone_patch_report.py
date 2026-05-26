"""
DeadZone comprehensive patch report generator.

Produces  output/reports/deadzone_patch_report.txt  by aggregating data from
all pipeline stages.  Call write_deadzone_patch_report() at the end of the
build pipeline with whatever context is available — every field is optional
and absent sections are omitted gracefully.

Report sections
---------------
1.  ROM Source Format
2.  Detected Device / Model / Region / OS / Android / Build
3.  Partitions Unpacked
4.  Super Metadata Source
5.  Original Partition Sizes Used
6.  Patches Applied
7.  APK / JAR / Smali Changes
8.  Files Added / Removed
9.  Final ZIP Manifest
10. PixelDrain Upload Link
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

REPORT_FILENAME = "deadzone_patch_report.txt"

_DIV = "═" * 62
_SEC = "─" * 62


def _fmt_bytes(n: int) -> str:
    if n >= 1_073_741_824:
        return f"{n / 1_073_741_824:.2f} GiB  ({n:,} bytes)"
    if n >= 1_048_576:
        return f"{n / 1_048_576:.2f} MiB  ({n:,} bytes)"
    return f"{n:,} bytes"


def _section(title: str, lines: list[str]) -> list[str]:
    return ["", _SEC, f"  {title}", _SEC] + lines


# ── Section builders ───────────────────────────────────────────────────────────

def _build_rom_source_section(data: dict) -> list[str]:
    fmt = data.get("rom_source_format") or "(unknown)"
    rom_path = data.get("input_rom") or "(unknown)"
    archive_type = data.get("archive_type") or "(unknown)"
    return _section("ROM Source Format", [
        f"  Format       : {fmt}",
        f"  Archive type : {archive_type}",
        f"  Source path  : {rom_path}",
    ])


def _build_device_section(data: dict) -> list[str]:
    fields = [
        ("Device codename", data.get("effective_device") or data.get("factory_device") or "(unknown)"),
        ("Model / market", data.get("device_model") or "(unknown)"),
        ("Region",         data.get("region") or "(unknown)"),
        ("OS name",        data.get("os_name") or "(unknown)"),
        ("Android ver.",   data.get("android_version") or "(unknown)"),
        ("Build ID",       data.get("build_incremental") or "(unknown)"),
        ("Brand",          data.get("brand") or "(unknown)"),
    ]
    return _section("Detected Device Information", [
        f"  {label:16s}: {value}" for label, value in fields
    ])


def _build_partitions_section(data: dict) -> list[str]:
    partitions: list[str] = data.get("partitions_unpacked") or []
    images: list[str] = data.get("images_found") or []
    lines: list[str] = []
    if partitions:
        lines.append(f"  Partitions ({len(partitions)}):")
        for p in sorted(partitions):
            lines.append(f"    {p}")
    else:
        lines.append("  Partitions : (none recorded)")
    if images:
        lines.append(f"  Standalone images ({len(images)}):")
        for img in sorted(images):
            lines.append(f"    {img}")
    return _section("Partitions Unpacked", lines)


def _build_super_meta_section(data: dict) -> list[str]:
    source = data.get("super_meta_source") or "(unknown)"
    super_found = data.get("super_found", None)
    payload_found = data.get("payload_found", None)
    lines = [
        f"  Metadata source : {source}",
    ]
    if super_found is not None:
        lines.append(f"  super.img found : {super_found}")
    if payload_found is not None:
        lines.append(f"  payload.bin found: {payload_found}")
    return _section("Super Metadata Source", lines)


def _build_sizes_section(data: dict) -> list[str]:
    sizes: dict[str, int] = data.get("original_partition_sizes") or {}
    if not sizes:
        return _section("Original Partition Sizes", [
            "  (no sizes recorded — check super_layout or op_list availability)",
        ])
    lines: list[str] = [f"  {'Partition':20s}  {'Allocation':>20s}"]
    lines.append(f"  {'─'*20}  {'─'*20}")
    for part, sz in sorted(sizes.items()):
        lines.append(f"  {part:20s}  {sz:>20,} bytes")
    return _section("Original Partition Sizes Used", lines)


def _build_patches_section(data: dict) -> list[str]:
    patches: list[str] = data.get("patches_applied") or []
    if not patches:
        return _section("Patches Applied", ["  (none recorded)"])
    return _section("Patches Applied", [f"  {p}" for p in patches])


def _build_apk_jar_section(data: dict) -> list[str]:
    apk_changes: list[dict] = data.get("apk_changes") or []
    jar_changes: list[dict] = data.get("jar_changes") or []
    smali_changes: list[dict] = data.get("smali_changes") or []
    lines: list[str] = []

    def _fmt_changes(label: str, changes: list[dict]) -> None:
        if not changes:
            lines.append(f"  {label}: (none)")
            return
        lines.append(f"  {label} ({len(changes)}):")
        for c in changes:
            name = c.get("name") or c.get("file") or "(unknown)"
            action = c.get("action") or c.get("type") or ""
            lines.append(f"    {action:10s} {name}")

    _fmt_changes("APK changes", apk_changes)
    _fmt_changes("JAR changes", jar_changes)
    _fmt_changes("Smali changes", smali_changes)
    return _section("APK / JAR / Smali Changes", lines)


def _build_files_section(data: dict) -> list[str]:
    added: list[str] = data.get("files_added") or []
    removed: list[str] = data.get("files_removed") or []
    lines: list[str] = []
    if added:
        lines.append(f"  Added ({len(added)}):")
        for f in sorted(added):
            lines.append(f"    + {f}")
    else:
        lines.append("  Added: (none)")
    if removed:
        lines.append(f"  Removed ({len(removed)}):")
        for f in sorted(removed):
            lines.append(f"    - {f}")
    else:
        lines.append("  Removed: (none)")
    return _section("Files Added / Removed", lines)


def _build_zip_manifest_section(data: dict) -> list[str]:
    manifest: list[str] = data.get("final_zip_manifest") or []
    zip_size: Optional[int] = data.get("final_zip_size_bytes")
    zip_name: Optional[str] = data.get("final_zip_name")
    lines: list[str] = []
    if zip_name:
        lines.append(f"  File    : {zip_name}")
    if zip_size is not None:
        lines.append(f"  Size    : {_fmt_bytes(zip_size)}")
    if manifest:
        lines.append(f"  Contents ({len(manifest)} entries):")
        for entry in sorted(manifest):
            lines.append(f"    {entry}")
    else:
        lines.append("  Contents: (manifest not available)")
    return _section("Final ZIP Manifest", lines)


def _build_pixeldrain_section(data: dict) -> list[str]:
    link: Optional[str] = data.get("pixeldrain_link")
    file_id: Optional[str] = data.get("pixeldrain_file_id")
    if not link and not file_id:
        return _section("PixelDrain Upload", ["  Not uploaded."])
    lines = []
    if link:
        lines.append(f"  Link    : {link}")
    if file_id:
        lines.append(f"  File ID : {file_id}")
    return _section("PixelDrain Upload", lines)


# ── Public API ─────────────────────────────────────────────────────────────────

def build_report_text(data: dict) -> str:
    """
    Render the full patch report as a UTF-8 string.

    data keys (all optional):
        rom_source_format      str   — "split_super" / "payload" / "new_dat_br" / …
        archive_type           str   — "zip" / "tgz" / "img" / …
        input_rom              str   — path to original ROM file
        effective_device       str
        factory_device         str
        device_model           str
        region                 str
        os_name                str   — "HyperOS 3" / "MIUI" / …
        android_version        str
        build_incremental      str
        brand                  str
        partitions_unpacked    list[str]
        images_found           list[str]
        super_meta_source      str
        super_found            bool
        payload_found          bool
        original_partition_sizes  dict[str, int]
        patches_applied        list[str]
        apk_changes            list[dict]  — [{name, action}, …]
        jar_changes            list[dict]
        smali_changes          list[dict]
        files_added            list[str]
        files_removed          list[str]
        final_zip_manifest     list[str]
        final_zip_size_bytes   int
        final_zip_name         str
        pixeldrain_link        str
        pixeldrain_file_id     str
    """
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines: list[str] = [
        _DIV,
        "  DeadZone Factory — Comprehensive Patch Report",
        f"  Generated : {ts}",
        _DIV,
    ]

    lines += _build_rom_source_section(data)
    lines += _build_device_section(data)
    lines += _build_partitions_section(data)
    lines += _build_super_meta_section(data)
    lines += _build_sizes_section(data)
    lines += _build_patches_section(data)
    lines += _build_apk_jar_section(data)
    lines += _build_files_section(data)
    lines += _build_zip_manifest_section(data)
    lines += _build_pixeldrain_section(data)

    lines += ["", _DIV, "  End of report", _DIV, ""]
    return "\n".join(lines)


def data_from_context(ctx) -> dict:
    """Extract report data dict from a BuildContext produced by UnpackPipeline."""
    return {
        "archive_type": getattr(ctx, "archive_type", None),
        "input_rom": str(getattr(ctx, "input_rom", "") or ""),
        "effective_device": getattr(ctx, "effective_device", None),
        "factory_device": getattr(ctx, "factory_device", None),
        "android_version": getattr(ctx, "android_version", None),
        "build_incremental": getattr(ctx, "mi_version", None),
        "partitions_unpacked": list(getattr(ctx, "partitions", None) or []),
        "images_found": list(getattr(ctx, "images", None) or []),
        "super_found": getattr(ctx, "super_found", None),
        "payload_found": getattr(ctx, "payload_found", None),
        "original_partition_sizes": dict(
            getattr(ctx, "partition_sizes_from_manifest", None) or {}
        ),
    }


def write_deadzone_patch_report(
    data: dict,
    reports_dir: Path,
) -> Path:
    """
    Write output/reports/deadzone_patch_report.txt.

    Parameters
    ----------
    data:
        Report data dict.  Build with data_from_context() or supply manually.
        Any key can be absent — absent sections are listed as "(none recorded)".
    reports_dir:
        Directory where the report file is written.

    Returns
    -------
    Path to the written report file.
    """
    reports_dir = Path(reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    out_path = reports_dir / REPORT_FILENAME
    text = build_report_text(data)
    out_path.write_text(text, encoding="utf-8")
    print(f"[patch_report] {REPORT_FILENAME} → {out_path}")
    return out_path


def write_deadzone_patch_report_from_context(ctx, reports_dir: Path, **extra) -> Path:
    """Convenience wrapper: build data from a BuildContext, merge extra keys, write report."""
    data = data_from_context(ctx)
    data.update(extra)
    return write_deadzone_patch_report(data, reports_dir)
