"""Base port acceptance tests.

Covers:
- Method/function names use only mezo_* or deadzone_* for ported methods
- Original ROM input is preserved (cleanup cannot touch it)
- Cleanup cannot delete outside workspace
- Archive traversal (path-escape) is blocked
- Payload fallback: missing tool still reads manifest & lists partitions
- VAB _b zero-size placeholders are accepted by validate_pre_super_images
- fs_config and file_contexts are regenerated after extraction
- Mods are not executed in base port
- Workflows still call the canonical DeadZone CLI
"""
from __future__ import annotations

import ast
import re
import textwrap
import zipfile
from pathlib import Path
from typing import Any

import pytest

from factory.core.cleanup import cleanup, deadzone_safe_delete
from factory.core.fs_config import (
    mezo_patch_fs_config,
    mezo_regenerate_fs_config,
    mezo_regenerate_file_contexts,
    mezo_regenerate_fs_metadata,
    mezo_scan_fs_config,
    mezo_scan_partition_dir,
)
from factory.core.unpacker import _safe_destination
from factory.core.workspace import Workspace, create_workspace, write_json


# ── helpers ───────────────────────────────────────────────────────────────────

def _make_ws(tmp_path: Path) -> Workspace:
    return create_workspace(tmp_path / "workspace")


def _ported_module_paths() -> list[Path]:
    """Return paths to newly created ported modules (not existing updated modules)."""
    base = Path("factory/core")
    return [
        base / "fs_config.py",
        base / "base_port_reports.py",
    ]


def _public_names_in(path: Path) -> list[str]:
    """Return all top-level function and class names defined in a module."""
    if not path.is_file():
        return []
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Only top-level (direct children of Module)
            pass
        if isinstance(node, ast.Module):
            for child in node.body:
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    names.append(child.name)
                elif isinstance(child, ast.ClassDef):
                    names.append(child.name)
    return names


_FORBIDDEN_PREFIXES = ("hyperur_", "usagi_", "wukong_", "spider_", "kaori_", "mio_", "cn_")
_ALLOWED_PREFIXES = ("mezo_", "deadzone_")


# ── 1. Naming convention ──────────────────────────────────────────────────────

def test_ported_functions_use_mezo_or_deadzone_prefix():
    """Every top-level function in ported modules must start with mezo_ or deadzone_.

    Private helpers (leading underscore) and dunder names are excluded.
    """
    violations: list[str] = []
    for path in _ported_module_paths():
        for name in _public_names_in(path):
            if name.startswith("_"):
                continue
            if not any(name.startswith(p) for p in _ALLOWED_PREFIXES):
                violations.append(f"{path.name}::{name}")

    assert not violations, (
        "Ported public functions must start with mezo_* or deadzone_*.\n"
        "Violations:\n" + "\n".join(f"  {v}" for v in violations)
    )


def test_no_forbidden_prefix_in_ported_modules():
    """Ported modules must not define functions with forbidden prefixes."""
    violations: list[str] = []
    for path in _ported_module_paths():
        for name in _public_names_in(path):
            if any(name.startswith(p) for p in _FORBIDDEN_PREFIXES):
                violations.append(f"{path.name}::{name}")

    assert not violations, (
        "Forbidden function name prefixes found in ported modules.\n"
        "Violations:\n" + "\n".join(f"  {v}" for v in violations)
    )


# ── 2. Original ROM input preserved ──────────────────────────────────────────

def test_cleanup_preserves_original_rom_input(tmp_path):
    """cleanup() must not remove the ROM input file outside the workspace."""
    rom_file = tmp_path / "original_rom.zip"
    rom_file.write_bytes(b"ROM_DATA")

    ws = _make_ws(tmp_path)
    (ws.images / "super.img").write_bytes(b"super")
    (ws.final / "DeadZone.zip").write_bytes(b"final")

    cleanup(ws, keep_workspace=False)

    assert rom_file.is_file(), "original ROM input must not be deleted by cleanup"


def test_cleanup_does_not_delete_outside_workspace(tmp_path):
    """deadzone_safe_delete must refuse to delete a path outside the workspace root."""
    ws = _make_ws(tmp_path)
    outside_file = tmp_path / "important_file.txt"
    outside_file.write_text("do not delete")

    with pytest.raises(RuntimeError, match="outside workspace"):
        deadzone_safe_delete(outside_file, ws.root)

    assert outside_file.is_file(), "file outside workspace must not be deleted"


# ── 3. Archive traversal blocked ─────────────────────────────────────────────

def test_archive_traversal_member_is_blocked(tmp_path):
    """_safe_destination must raise for members that escape the workspace root."""
    root = tmp_path / "extracted"
    root.mkdir()

    with pytest.raises(RuntimeError, match="escapes workspace"):
        _safe_destination(root, "../../../etc/passwd")


def test_archive_traversal_absolute_path_blocked(tmp_path):
    root = tmp_path / "extracted"
    root.mkdir()

    with pytest.raises(RuntimeError, match="escapes workspace"):
        _safe_destination(root, "/etc/passwd")


def test_archive_traversal_safe_member_allowed(tmp_path):
    root = tmp_path / "extracted"
    root.mkdir()

    result = _safe_destination(root, "images/system.img")
    assert result == (root / "images" / "system.img").resolve()


# ── 4. Payload fallback — manifest read without tool ─────────────────────────

def test_payload_fallback_reads_partitions_without_tool(tmp_path):
    """When payload-dumper-go is absent the adapter must still parse manifest metadata."""
    ws = _make_ws(tmp_path)

    # Build a minimal valid payload.bin (magic + header + zeroed manifest).
    import struct
    block_size = 4096
    manifest_bytes = b"\x00" * 4
    sig_len = 4
    header = struct.pack(">4sQQI", b"CrAU", 2, len(manifest_bytes), sig_len)
    payload_content = header + manifest_bytes + b"\x00" * sig_len

    payload_dir = ws.extracted / "payload"
    payload_dir.mkdir(parents=True, exist_ok=True)
    (payload_dir / "payload.bin").write_bytes(payload_content)

    # Import private helper to test manifest parsing only (does not invoke tool).
    from factory.adapters.payload import _payload_metadata
    meta = _payload_metadata(payload_dir / "payload.bin")

    # Even a zero-length manifest returns a dict with the right keys.
    assert isinstance(meta, dict)
    assert "partitions" in meta
    assert "partition_sizes" in meta


def test_payload_fallback_accepts_vab_b_partitions(tmp_path):
    """Payload metadata parser must correctly strip _a/_b slot suffixes."""
    from factory.adapters.payload import _base_partition, _slot_suffix

    assert _base_partition("system_a.img") == "system"
    assert _base_partition("vendor_b.img") == "vendor"
    assert _base_partition("product.img") == "product"
    assert _slot_suffix("system_a.img") == "_a"
    assert _slot_suffix("system_b.img") == "_b"
    assert _slot_suffix("product.img") == ""


# ── 5. VAB _b zero-size placeholders accepted ─────────────────────────────────

def test_vab_zero_b_partitions_accepted_by_pre_super_validation(tmp_path):
    """validate_pre_super_images must not fail when _b partitions have zero allocation."""
    from factory.core.super_builder import validate_pre_super_images

    ws = _make_ws(tmp_path)
    (ws.images / "system.img").write_bytes(b"x" * 3_000)
    (ws.images / "vendor.img").write_bytes(b"x" * 2_000)

    layout: dict[str, Any] = {
        "dynamic_images": {
            "system": str(ws.images / "system.img"),
            "vendor": str(ws.images / "vendor.img"),
        },
        "selected_partitions": ["system", "vendor"],
        "partitions": {
            "system": {"allocation_size": 4_000, "source": "test"},
            "vendor": {"allocation_size": 3_000, "source": "test"},
        },
        "group_size": 10_000,
        "virtual_ab": True,
        "vab_zero_b_partitions": [
            {"name": "system_b", "allocation_size": 0, "group_name": "qti_dynamic_partitions_b"},
            {"name": "vendor_b", "allocation_size": 0, "group_name": "qti_dynamic_partitions_b"},
        ],
    }
    write_json(ws.reports / "stable_partition_rebuild_report.json", {"partitions": []})

    result = validate_pre_super_images(ws, layout)
    assert result["status"] == "ok"
    assert result["errors"] == []


# ── 6. fs_config and file_contexts regenerated ───────────────────────────────

def test_mezo_scan_fs_config_parses_entries(tmp_path):
    fs_config = tmp_path / "fs_config"
    fs_config.write_text(
        "/ 0 0 0755\n"
        "/system 0 0 0755\n"
        "/system/bin/sh 0 2000 0755\n",
        encoding="utf-8",
    )
    result = mezo_scan_fs_config(fs_config)
    assert "/" in result
    assert "/system" in result
    assert "/system/bin/sh" in result
    assert result["/system/bin/sh"] == ["0", "2000", "0755"]


def test_mezo_regenerate_fs_config_adds_missing_entries(tmp_path):
    part_dir = tmp_path / "system"
    part_dir.mkdir()
    (part_dir / "build.prop").write_text("ro.build.version.sdk=34\n", encoding="utf-8")

    fs_config = tmp_path / "system_fs_config"
    fs_config.write_text("system 0 0 0755\n", encoding="utf-8")

    result = mezo_regenerate_fs_config(part_dir, fs_config)
    assert result["entries_added"] >= 1
    assert result["entries_after"] > result["entries_before"]

    updated = mezo_scan_fs_config(fs_config)
    # build.prop should now have an entry
    found = any("build.prop" in k for k in updated)
    assert found, f"build.prop entry expected in fs_config; got keys: {list(updated.keys())}"


def test_mezo_regenerate_file_contexts_adds_missing_entries(tmp_path):
    part_dir = tmp_path / "vendor"
    part_dir.mkdir()
    (part_dir / "build.prop").write_text("ro.vendor.build.version.sdk=34\n", encoding="utf-8")

    fc_path = tmp_path / "vendor_file_contexts"

    result = mezo_regenerate_file_contexts(part_dir, fc_path)
    assert result["entries_added"] >= 1
    assert fc_path.is_file()


def test_mezo_regenerate_fs_metadata_skips_missing_dir(tmp_path):
    ws = _make_ws(tmp_path)
    result = mezo_regenerate_fs_metadata(ws, "odm", tmp_path / "nonexistent_odm")
    assert result["status"] == "skipped"
    assert "not found" in result["reason"]


def test_mezo_regenerate_fs_metadata_ok_for_extracted_partition(tmp_path):
    ws = _make_ws(tmp_path)
    part_dir = ws.partitions / "system"
    part_dir.mkdir(parents=True, exist_ok=True)
    (part_dir / "build.prop").write_text("ro.build.version.sdk=34\n", encoding="utf-8")

    result = mezo_regenerate_fs_metadata(ws, "system", part_dir)
    assert result["status"] == "ok"
    assert "fs_config" in result
    assert "file_contexts" in result


# ── 7. Mods not executed in base port ────────────────────────────────────────

_MOD_SYMBOLS = [
    "miui_systemui", "provision_apk", "wukong", "usagi_ui",
    "change_clock_format", "icon_style", "private_chip", "battery_style",
    "smali_patch", "disable_signature_verification", "flag_secure", "spoofing",
]

_MOD_MODULES = [
    "factory/core/miui_systemui.py",
    "factory/core/provision.py",
    "factory/core/wukong.py",
    "factory/core/usagi_ui.py",
    "factory/core/clock_style.py",
    "factory/core/icon_style.py",
    "factory/mods/",
]


def test_mod_modules_do_not_exist_in_base_port():
    """Mod-specific modules must not be present in the base port."""
    existing = [p for p in _MOD_MODULES if Path(p).exists()]
    assert not existing, (
        "Mod modules must not exist in base port:\n"
        + "\n".join(f"  {p}" for p in existing)
    )


def test_base_port_reports_mod_status_is_disabled(tmp_path):
    """deadzone_base_port_audit must report all mods as DISABLED."""
    from factory.core.base_port_reports import deadzone_base_port_audit

    ws = _make_ws(tmp_path)
    path = deadzone_base_port_audit(ws, stages=[], status="OK")
    content = path.read_text(encoding="utf-8")
    assert "DISABLED" in content
    assert "miui_systemui" in content


# ── 8. Workflows call the canonical DeadZone CLI ─────────────────────────────

_WORKFLOW_FILES = [
    ".github/workflows/deadzone_mtk.yml",
    ".github/workflows/deadzone_snapdragon.yml",
]
_CANONICAL_CLI = "python3 -m factory.deadzone"


def test_workflows_call_canonical_deadzone_cli():
    """Both workflow YAML files must invoke the canonical DeadZone CLI entry point."""
    missing_cli: list[str] = []
    missing_file: list[str] = []
    for wf in _WORKFLOW_FILES:
        path = Path(wf)
        if not path.is_file():
            missing_file.append(wf)
            continue
        content = path.read_text(encoding="utf-8")
        if _CANONICAL_CLI not in content:
            missing_cli.append(wf)

    assert not missing_file, f"Workflow files not found: {missing_file}"
    assert not missing_cli, (
        f"Workflows missing canonical CLI call '{_CANONICAL_CLI}': {missing_cli}"
    )


def test_workflows_do_not_call_hyperur():
    """Workflow files must not invoke HyperURBuild.py or any hyperur_ entry point."""
    violations: list[str] = []
    for wf in _WORKFLOW_FILES:
        path = Path(wf)
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8").lower()
        if "hyperurbuild" in content or "hyperur_" in content:
            violations.append(wf)

    assert not violations, f"Workflow files must not reference HyperUR: {violations}"


# ── 9. Cleanup safe-delete guard (edge cases) ─────────────────────────────────

def test_deadzone_safe_delete_inside_workspace_succeeds(tmp_path):
    ws = _make_ws(tmp_path)
    target = ws.extracted / "old_rom_files"
    target.mkdir(parents=True)
    (target / "dummy.img").write_bytes(b"x" * 100)

    deadzone_safe_delete(target, ws.root)

    assert not target.exists()


def test_deadzone_safe_delete_refuses_parent_escape(tmp_path):
    ws = _make_ws(tmp_path)
    outside = tmp_path / "shared_config"
    outside.mkdir()

    with pytest.raises(RuntimeError, match="outside workspace"):
        deadzone_safe_delete(outside, ws.root)

    assert outside.is_dir()
