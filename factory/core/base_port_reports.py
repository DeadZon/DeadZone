from __future__ import annotations

import hashlib
import time
import zipfile
from pathlib import Path
from typing import Any

from factory.core.workspace import Workspace, read_json


# ── ROM intake report ─────────────────────────────────────────────────────────

def deadzone_rom_intake_report(ws: Workspace) -> Path:
    """Write ROM intake report summarising what the detector found about the input ROM."""
    rom_info = read_json(ws.meta / "rom_info.json", {})
    device_info = read_json(ws.meta / "device_info.json", {})
    partition_map = read_json(ws.meta / "partition_map.json", {})
    unpack_result = read_json(ws.meta / "unpack_result.json", {})

    by_partition = partition_map.get("by_partition") if isinstance(partition_map.get("by_partition"), dict) else {}
    seen_images = partition_map.get("source_images_seen") if isinstance(partition_map.get("source_images_seen"), list) else []

    lines = [
        "DeadZone ROM Intake Report",
        "==========================",
        f"rom_type          : {rom_info.get('rom_type', 'unknown')}",
        f"archive_type      : {rom_info.get('archive_type', 'unknown')}",
        f"codename          : {device_info.get('codename', 'unknown')}",
        f"android_version   : {device_info.get('android_version', 'unknown')}",
        f"build             : {device_info.get('build', 'unknown')}",
        f"region            : {rom_info.get('region', 'unknown')}",
        f"soc               : {device_info.get('soc', 'unknown')}",
        f"slot_mode         : {device_info.get('slot_mode', 'unknown')}",
        f"filesystem        : {device_info.get('filesystem', 'unknown')}",
        f"has_payload       : {rom_info.get('has_payload', False)}",
        f"has_super         : {rom_info.get('has_super', False)}",
        f"has_split_super   : {rom_info.get('has_split_super', False)}",
        f"has_new_dat_br    : {rom_info.get('has_new_dat_br', False)}",
        f"needs_super_rebuild: {rom_info.get('needs_super_rebuild', False)}",
        f"adapter           : {unpack_result.get('adapter', '(not run)')}",
        f"adapter_images    : {len(unpack_result.get('images') or [])}",
        "",
        "dynamic partitions seen in archive:",
        *([f"  - {name}: {path}" for name, path in sorted(by_partition.items())] or ["  (none)"]),
        "",
        f"source images seen: {len(seen_images)}",
        *([f"  - {img}" for img in seen_images[:80]] or ["  (none)"]),
        "",
    ]

    report_path = ws.reports / "deadzone_rom_intake_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


# ── Partition extract report ──────────────────────────────────────────────────

def deadzone_partition_extract_report(ws: Workspace) -> Path:
    """Write partition extraction report from image_extraction metadata."""
    extraction = read_json(ws.meta / "image_extraction.json", {})
    summary = extraction.get("summary") if isinstance(extraction.get("summary"), dict) else {}
    super_extraction = extraction.get("super_extraction") if isinstance(extraction.get("super_extraction"), dict) else {}
    partitions = extraction.get("partitions") if isinstance(extraction.get("partitions"), list) else []

    lines = [
        "DeadZone Partition Extract Report",
        "=================================",
        f"status            : {extraction.get('status', 'unknown')}",
        f"extracted         : {summary.get('extracted', 0)}",
        f"listed_only       : {summary.get('listed_only', 0)}",
        f"failed            : {summary.get('failed', 0)}",
        f"skipped           : {summary.get('skipped', 0)}",
        "",
        "super extraction:",
        f"  status  : {super_extraction.get('status', '(none)')}",
        f"  reason  : {super_extraction.get('reason', '(none)')}",
        f"  tool    : {super_extraction.get('tool', '(none)')}",
        "",
        "partition results:",
    ]
    for item in partitions:
        if not isinstance(item, dict):
            continue
        lines += [
            f"- partition       : {item.get('partition')}",
            f"  format          : {item.get('detected_format', 'unknown')}",
            f"  method          : {item.get('extraction_method', '(none)')}",
            f"  tool            : {item.get('tool_path', '(none)')}",
            f"  status          : {item.get('status', 'unknown')}",
            f"  files           : {item.get('file_count', 0)}",
            f"  bytes           : {item.get('total_extracted_bytes', 0)}",
            f"  failure_reason  : {item.get('failure_reason') or '(none)'}",
        ]
    lines.append("")

    report_path = ws.reports / "deadzone_partition_extract_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


# ── fs metadata report ────────────────────────────────────────────────────────

def deadzone_fs_metadata_report(ws: Workspace) -> Path:
    """Write fs_config and file_contexts metadata report for all extracted partitions."""
    fs_metadata = read_json(ws.meta / "fs_metadata.json", {})
    results = fs_metadata.get("results") if isinstance(fs_metadata.get("results"), list) else []

    if not results:
        results = _scan_partition_fs_metadata(ws)

    lines = [
        "DeadZone FS Metadata Report",
        "===========================",
        f"partitions scanned: {len(results)}",
        "",
    ]
    for item in results:
        if not isinstance(item, dict):
            continue
        partition = item.get("partition", "unknown")
        status = item.get("status", "unknown")
        lines.append(f"partition: {partition}  status: {status}")
        if status == "skipped":
            lines.append(f"  reason: {item.get('reason', '(none)')}")
        else:
            fs = item.get("fs_config") if isinstance(item.get("fs_config"), dict) else {}
            fc = item.get("file_contexts") if isinstance(item.get("file_contexts"), dict) else {}
            lines += [
                f"  fs_config:",
                f"    path          : {fs.get('fs_config_path', '(none)')}",
                f"    entries_before: {fs.get('entries_before', 0)}",
                f"    entries_added : {fs.get('entries_added', 0)}",
                f"    entries_after : {fs.get('entries_after', 0)}",
                f"  file_contexts:",
                f"    path          : {fc.get('file_contexts_path', '(none)')}",
                f"    entries_before: {fc.get('entries_before', 0)}",
                f"    entries_added : {fc.get('entries_added', 0)}",
                f"    entries_after : {fc.get('entries_after', 0)}",
            ]
    lines.append("")

    report_path = ws.reports / "deadzone_fs_metadata_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def _scan_partition_fs_metadata(ws: Workspace) -> list[dict[str, Any]]:
    """Scan workspace partition directories for fs_config and file_contexts presence."""
    results: list[dict[str, Any]] = []
    if not ws.partitions.is_dir():
        return results
    for part_dir in sorted(ws.partitions.iterdir()):
        if not part_dir.is_dir() or part_dir.name.startswith("."):
            continue
        fs_config = part_dir / "fs_config"
        file_contexts = part_dir / "file_contexts"
        results.append({
            "partition": part_dir.name,
            "status": "present",
            "fs_config": {
                "fs_config_path": str(fs_config) if fs_config.is_file() else "(missing)",
                "entries_before": _count_fs_config_entries(fs_config),
                "entries_added": 0,
                "entries_after": _count_fs_config_entries(fs_config),
            },
            "file_contexts": {
                "file_contexts_path": str(file_contexts) if file_contexts.is_file() else "(missing)",
                "entries_before": _count_file_contexts_entries(file_contexts),
                "entries_added": 0,
                "entries_after": _count_file_contexts_entries(file_contexts),
            },
        })
    return results


def _count_fs_config_entries(path: Path) -> int:
    if not path.is_file():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip())


def _count_file_contexts_entries(path: Path) -> int:
    if not path.is_file():
        return 0
    return sum(
        1 for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
        if line.strip() and not line.strip().startswith("#")
    )


# ── Super layout report ───────────────────────────────────────────────────────

def deadzone_super_layout_report(ws: Workspace) -> Path:
    """Write super layout report: VAB structure, _b zero placeholders, metadata sources."""
    super_layout = read_json(ws.meta / "super_layout.json", {})
    super_profile = read_json(ws.meta / "super_profile.json", {})
    build_result = read_json(ws.meta / "super_build_result.json", {})

    layout = super_profile if super_profile else super_layout
    selected = layout.get("selected_partitions") if isinstance(layout.get("selected_partitions"), list) else []
    virtual_ab = bool(layout.get("virtual_ab"))
    vab_zero_b = layout.get("vab_zero_b_partitions") if isinstance(layout.get("vab_zero_b_partitions"), list) else []
    partitions_meta = layout.get("partitions") if isinstance(layout.get("partitions"), dict) else {}

    lines = [
        "DeadZone Super Layout Report",
        "============================",
        f"slot_mode         : {layout.get('slot_mode', 'unknown')}",
        f"virtual_ab        : {virtual_ab}",
        f"target_super_size : {layout.get('target_super_size', 'unknown')}",
        f"group_size        : {layout.get('group_size', 'unknown')}",
        f"group_name        : {layout.get('dynamic_group_name') or layout.get('group_a_name', 'unknown')}",
        f"metadata_source   : {layout.get('metadata_source', 'unknown')}",
        f"output_format     : {layout.get('output_format', 'unknown')}",
        f"selected_partitions: {len(selected)}",
        f"build_action      : {build_result.get('action', '(not built yet)')}",
        f"build_status      : {build_result.get('status', '(not built yet)')}",
        f"super_img_size    : {build_result.get('super_size', '(none)')}",
        f"super_img_sparse  : {build_result.get('super_is_sparse', '(none)')}",
        "",
        "_a partitions (real images):",
    ]
    for part in selected:
        meta = partitions_meta.get(part, {})
        alloc = meta.get("allocation_size", "(unknown)")
        source = meta.get("source", "(unknown)")
        lines.append(f"  - {part}_a: allocation={alloc} source={source}")
    if not selected:
        lines.append("  (none)")

    lines += ["", "_b partitions (VAB zero-size placeholders):"]
    if virtual_ab:
        for entry in vab_zero_b:
            if isinstance(entry, dict):
                lines.append(f"  - {entry.get('name')}: allocation=0 group={entry.get('group_name', '(unknown)')}")
            else:
                lines.append(f"  - {entry}_b: allocation=0")
        if not vab_zero_b and selected:
            for part in selected:
                lines.append(f"  - {part}_b: allocation=0 (implicit VAB zero placeholder)")
    else:
        lines.append("  (not VAB — no _b zero entries)")

    lines += [
        "",
        "validation:",
        f"  lpdump_status : {(build_result.get('validation') or {}).get('status', '(not run)')}",
        f"  lpdump_reason : {(build_result.get('validation') or {}).get('reason', '(none)')}",
        "",
    ]

    report_path = ws.reports / "deadzone_super_layout_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


# ── Repack report ─────────────────────────────────────────────────────────────

def deadzone_repack_report(ws: Workspace) -> Path:
    """Write repack stage report summarising which partitions were repacked."""
    repack_result = read_json(ws.meta / "repack_result.json", {})
    super_build = read_json(ws.meta / "super_build_result.json", {})
    rebuild_report = read_json(ws.reports / "stable_partition_rebuild_report.json", {})
    partitions_rebuilt = rebuild_report.get("partitions") if isinstance(rebuild_report.get("partitions"), list) else []

    lines = [
        "DeadZone Repack Report",
        "======================",
        f"repack_status     : {repack_result.get('status', '(not run)')}",
        f"super_build_action: {super_build.get('action', '(not run)')}",
        f"super_build_status: {super_build.get('status', '(not run)')}",
        f"super_build_reason: {super_build.get('reason', '(none)')}",
        f"partitions_rebuilt: {len(partitions_rebuilt)}",
        "",
        "rebuilt partitions:",
    ]
    for item in partitions_rebuilt:
        if not isinstance(item, dict):
            continue
        lines += [
            f"  - {item.get('partition', 'unknown')}:",
            f"      status        : {item.get('status', 'unknown')}",
            f"      tool          : {item.get('tool', '(none)')}",
            f"      size_before   : {item.get('size_before') or item.get('original_size', 0)}",
            f"      size_after    : {item.get('size_after') or item.get('new_size', 0)}",
        ]
    if not partitions_rebuilt:
        lines.append("  (none — partitions were preserved from original super or not rebuilt)")

    lines += ["", "super image:", f"  path: {super_build.get('super_img', '(none)')}", ""]

    report_path = ws.reports / "deadzone_repack_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


# ── Final ZIP report ──────────────────────────────────────────────────────────

def deadzone_final_zip_report(ws: Workspace, final_zip_path: Path | None) -> Path:
    """Write final ZIP validation report: existence, size, SHA-256, member list."""
    final_zip_meta = read_json(ws.meta / "final_zip.json", {})
    size_policy = read_json(ws.meta / "size_policy.json", {})

    zip_path = final_zip_path or (Path(str(final_zip_meta.get("path", ""))) if final_zip_meta.get("path") else None)
    zip_exists = zip_path is not None and Path(zip_path).is_file()
    zip_size = Path(zip_path).stat().st_size if zip_exists else 0
    sha256 = _sha256(Path(zip_path)) if zip_exists else "(file missing)"
    members = _zip_members(Path(zip_path)) if zip_exists else []

    lines = [
        "DeadZone Final ZIP Report",
        "=========================",
        f"path              : {zip_path or '(none)'}",
        f"exists            : {zip_exists}",
        f"size_bytes        : {zip_size}",
        f"size_mib          : {zip_size / 1024 / 1024:.1f}" if zip_size else "size_mib          : 0",
        f"sha256            : {sha256}",
        f"member_count      : {len(members)}",
        f"max_allowed_bytes : {size_policy.get('final_zip_max_bytes') or size_policy.get('final_zip_max_allowed') or '(unknown)'}",
        f"policy_status     : {size_policy.get('status', '(unknown)')}",
        f"policy_reason     : {size_policy.get('reason', '(none)')}",
        "",
        "members:",
        *([f"  - {m}" for m in sorted(members)[:200]] or ["  (none)"]),
        "",
    ]

    report_path = ws.reports / "deadzone_final_zip_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def _sha256(path: Path) -> str:
    try:
        h = hashlib.sha256()
        with path.open("rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception as exc:
        return f"(error: {exc})"


def _zip_members(path: Path) -> list[str]:
    try:
        with zipfile.ZipFile(path) as zf:
            return zf.namelist()
    except Exception:
        return []


# ── Base port audit ───────────────────────────────────────────────────────────

def deadzone_base_port_audit(ws: Workspace, stages: list[dict[str, Any]], status: str) -> Path:
    """Write comprehensive base port audit: all stages, safety guards, mod status."""
    rom_info = read_json(ws.meta / "rom_info.json", {})
    device_info = read_json(ws.meta / "device_info.json", {})
    super_build = read_json(ws.meta / "super_build_result.json", {})
    super_layout = read_json(ws.meta / "super_layout.json", {})
    extraction = read_json(ws.meta / "image_extraction.json", {})

    virtual_ab = bool(super_layout.get("virtual_ab") or super_build.get("slot_mode") == "VAB")
    mods_disabled = _check_mods_disabled()
    original_input_present = _check_original_input(ws)
    cleanup_guard = "deadzone_safe_delete (active)"

    lines = [
        "DeadZone Base Port Audit",
        "========================",
        f"generated_at      : {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}",
        f"build_status      : {status}",
        "",
        "rom intake:",
        f"  rom_type        : {rom_info.get('rom_type', 'unknown')}",
        f"  archive_type    : {rom_info.get('archive_type', 'unknown')}",
        f"  codename        : {device_info.get('codename', 'unknown')}",
        f"  android_version : {device_info.get('android_version', 'unknown')}",
        f"  build           : {device_info.get('build', 'unknown')}",
        f"  slot_mode       : {device_info.get('slot_mode', 'unknown')}",
        f"  has_payload     : {rom_info.get('has_payload', False)}",
        f"  has_super       : {rom_info.get('has_super', False)}",
        "",
        "safety:",
        f"  original_input_present : {original_input_present}",
        f"  cleanup_guard          : {cleanup_guard}",
        f"  archive_traversal_guard: deadzone_safe_destination (active in unpacker)",
        "",
        "partition extraction:",
        f"  status          : {(extraction.get('summary') or {}).get('extracted', 0)} extracted",
        f"  super_action    : {(extraction.get('super_extraction') or {}).get('status', '(none)')}",
        "",
        "super build:",
        f"  action          : {super_build.get('action', '(not built)')}",
        f"  status          : {super_build.get('status', '(not built)')}",
        f"  virtual_ab      : {virtual_ab}",
        f"  _b_zero_placeholders: {'yes — _b partitions written with allocation=0' if virtual_ab else 'no (not VAB)'}",
        "",
        "mods:",
        f"  status          : {mods_disabled}",
        "",
        "naming convention:",
        "  ported functions : mezo_* / deadzone_* only",
        "  forbidden names  : hyperur_* usagi_* wukong_* spider_* kaori_* mio_* cn_*",
        "",
        "stage timeline:",
    ]
    for stage in stages:
        dur = float(stage.get("duration_seconds") or stage.get("duration") or 0.0)
        lines.append(
            f"  {stage.get('status', 'UNKNOWN'):6}: {stage.get('name', 'unknown')} ({dur:.2f}s)"
        )
    if not stages:
        lines.append("  (no stages recorded)")
    lines.append("")

    report_path = ws.reports / "deadzone_base_port_audit.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def _check_mods_disabled() -> str:
    """Return a description of mod status (they are always disabled in base port)."""
    mod_names = [
        "miui_systemui", "provision", "wukong", "usagi_ui",
        "clock_style", "icon_style", "private_chip", "battery_style",
        "smali_patch", "signature_bypass", "flag_secure", "spoofing",
    ]
    return "DISABLED — base port only: " + ", ".join(mod_names)


def _check_original_input(ws: Workspace) -> str:
    """Check whether the original ROM input is still present in the workspace."""
    input_files = list(ws.input.glob("*")) if ws.input.is_dir() else []
    extracted = list(ws.extracted.glob("**/*")) if ws.extracted.is_dir() else []
    if input_files or extracted:
        return f"present (input={len(input_files)} items, extracted={len(extracted)} items)"
    return "not found (may have been moved during download stage)"


# ── Main entry: write all 7 reports ──────────────────────────────────────────

def deadzone_write_base_port_reports(ws: Workspace, ctx: Any) -> dict[str, str]:
    """Generate all 7 base port reports and return a dict of report name → path.

    Called from _write_final_reports in deadzone.py. All report functions read
    from already-generated workspace metadata; no pipeline data is duplicated.
    """
    reports: dict[str, str] = {}
    final_zip_path = getattr(ctx, "final_zip_path", None)
    stages = list(getattr(ctx, "stages", []) or [])
    status = str(getattr(ctx, "status", "UNKNOWN"))

    _report_steps: list[tuple[str, Any]] = [
        ("rom_intake", lambda: deadzone_rom_intake_report(ws)),
        ("partition_extract", lambda: deadzone_partition_extract_report(ws)),
        ("fs_metadata", lambda: deadzone_fs_metadata_report(ws)),
        ("super_layout", lambda: deadzone_super_layout_report(ws)),
        ("repack", lambda: deadzone_repack_report(ws)),
        ("final_zip", lambda: deadzone_final_zip_report(ws, Path(final_zip_path) if final_zip_path else None)),
        ("base_port_audit", lambda: deadzone_base_port_audit(ws, stages, status)),
    ]

    for name, fn in _report_steps:
        try:
            path = fn()
            reports[name] = str(path)
            print(f"[BASE PORT REPORTS] {name}: {path.name}")
        except Exception as exc:
            print(f"[BASE PORT REPORTS] Warning: {name} failed (non-fatal): {exc}")

    return reports
