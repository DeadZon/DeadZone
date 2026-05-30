"""
Phase 7 – Partition Workspace Stage tests.

Coverage (15 tests):
 1.  direct images are selected from smart_unpack result
 2.  required partition images are detected (all three present)
 3.  optional missing partitions are reported only (no failure)
 4.  missing required partition fails cleanly (RuntimeError)
 5.  zero-byte image is ignored (normalised to None)
 6.  output partition folders stay inside ws.partitions
 7.  original ROM input is preserved after stage
 8.  partition_workspace.json is generated
 9.  deadzone_partition_workspace_report.txt is generated
10.  fs_config/file_contexts metadata is recorded when extraction succeeds
11.  --stop-after partition_workspace stops before repack/super/app policy
12.  no HyperUR runtime import in partition_workspace module
13.  no mod/smali/UI keywords in partition_workspace module
14.  new public functions use only mezo_* or deadzone_* prefix
15.  existing Phase 1-6 core modules still import cleanly
"""
from __future__ import annotations

import ast
import importlib
import json
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from factory.core.partition_workspace import (
    deadzone_partition_workspace_stage,
    deadzone_write_partition_workspace_report,
    mezo_extract_partition_workspace,
    mezo_select_partition_images,
    mezo_validate_partition_workspace,
)
from factory.core.workspace import create_workspace


# ── Helpers ────────────────────────────────────────────────────────────────────

_ALL_PARTITIONS = [
    "system", "product", "vendor",
    "system_ext", "odm", "mi_ext", "system_dlkm", "vendor_dlkm",
]
_REQUIRED = {"system", "product", "vendor"}
_OPTIONAL = {"system_ext", "odm", "mi_ext", "system_dlkm", "vendor_dlkm"}


def _make_ws(tmp_path: Path):
    return create_workspace(tmp_path / "workspace")


def _make_image_folder(tmp_path: Path, partitions=("system", "product", "vendor")) -> Path:
    folder = tmp_path / "rom_images"
    folder.mkdir(exist_ok=True)
    for part in partitions:
        (folder / f"{part}.img").write_bytes(b"\x00" * 512)
    return folder


def _ok_smart_unpack_result(ws, route: str = "image_folder", img_dir: Path | None = None) -> dict[str, Any]:
    if img_dir is None:
        img_dir = ws.images
    images = {}
    for p in _ALL_PARTITIONS:
        candidate = img_dir / f"{p}.img"
        images[p] = str(candidate) if candidate.is_file() and candidate.stat().st_size > 0 else None
    return {
        "input_path": str(ws.root / "input" / "rom.zip"),
        "input_type": "folder",
        "route": route,
        "route_reason": "folder contains .img files",
        "status": "OK",
        "payload_path": None,
        "super_img": None,
        "images": images,
        "partitions": {},
        "missing_required": [],
        "missing_optional": list(_OPTIONAL),
        "reports": [],
        "error": "",
    }


def _mock_extraction_ok(partition_name: str, ws) -> dict[str, Any]:
    """Return a fake 'extracted' entry and create the target dir."""
    target = ws.partitions / partition_name
    target.mkdir(parents=True, exist_ok=True)
    (target / "build.prop").write_text(f"# {partition_name}\n", encoding="utf-8")
    return {
        "partition": partition_name,
        "source_image": str(ws.images / f"{partition_name}.img"),
        "detected_format": "raw_ext4",
        "extraction_method": "python-ext4",
        "tool_path": "factory.core._ext4",
        "extracted_path": str(target),
        "status": "extracted",
        "file_count": 1,
        "directory_count": 0,
        "total_extracted_bytes": 20,
        "failure_reason": "",
    }


# ── Test 1: direct images are selected from smart_unpack result ───────────────

def test_select_partition_images_from_result(tmp_path):
    ws = _make_ws(tmp_path)
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)
    result = _ok_smart_unpack_result(ws, img_dir=ws.images)
    selected = mezo_select_partition_images(result)
    assert selected["system"] is not None
    assert selected["product"] is not None
    assert selected["vendor"] is not None
    assert selected["system"].endswith("system.img")


# ── Test 2: required partition images are detected ────────────────────────────

def test_required_partitions_detected(tmp_path):
    ws = _make_ws(tmp_path)
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)
    result = _ok_smart_unpack_result(ws, img_dir=ws.images)
    selected = mezo_select_partition_images(result)
    for req in _REQUIRED:
        assert selected[req] is not None, f"Required partition {req!r} not selected"


# ── Test 3: optional missing partitions are reported only (no failure) ─────────

def test_optional_missing_reported_only(tmp_path):
    ws = _make_ws(tmp_path)
    # Only write required partition images
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)
    su_result = _ok_smart_unpack_result(ws, img_dir=ws.images)

    # Mock out actual extraction so we get clean "extracted" entries
    extracted_entries = {
        p: _mock_extraction_ok(p, ws) for p in ("system", "product", "vendor")
    }

    def fake_extract(img_path, partition_name, _ws, _tc):
        return extracted_entries.get(partition_name, {
            "partition": partition_name, "status": "skipped",
            "detected_format": "missing", "extraction_method": "",
            "tool_path": "", "extracted_path": str(_ws.partitions / partition_name),
            "failure_reason": "optional partition not present",
            "file_count": 0, "directory_count": 0, "total_extracted_bytes": 0,
            "source_image": "",
        })

    with patch("factory.core.partition_workspace.mezo_extract_partition_image", side_effect=fake_extract), \
         patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()):
        extraction = mezo_extract_partition_workspace(su_result, ws)

    skipped = extraction["skipped_optional"]
    for opt in _OPTIONAL:
        assert opt in skipped, f"Optional partition {opt!r} not in skipped_optional"

    validation = mezo_validate_partition_workspace(extraction)
    assert validation["valid"] is True
    assert validation["missing_required"] == []


# ── Test 4: missing required partition fails cleanly ──────────────────────────

def test_missing_required_partition_fails_cleanly(tmp_path):
    ws = _make_ws(tmp_path)
    # Only vendor present — system and product missing
    (ws.images / "vendor.img").write_bytes(b"\x00" * 512)
    su_result = _ok_smart_unpack_result(ws, img_dir=ws.images)

    def fake_extract(img_path, partition_name, _ws, _tc):
        if partition_name == "vendor":
            return _mock_extraction_ok(partition_name, _ws)
        return {
            "partition": partition_name,
            "source_image": "",
            "detected_format": "missing",
            "extraction_method": "",
            "tool_path": "",
            "extracted_path": str(_ws.partitions / partition_name),
            "status": "skipped",
            "file_count": 0, "directory_count": 0, "total_extracted_bytes": 0,
            "failure_reason": "required image not found",
        }

    with patch("factory.core.partition_workspace.mezo_extract_partition_image", side_effect=fake_extract), \
         patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()), \
         patch("factory.core.partition_workspace.mezo_regenerate_fs_metadata", return_value={}):
        with pytest.raises(RuntimeError) as exc_info:
            deadzone_partition_workspace_stage(ws, smart_unpack_result=su_result)

    msg = str(exc_info.value)
    assert "system" in msg or "product" in msg
    # Report and JSON must still be written before the raise
    assert (ws.reports / "deadzone_partition_workspace_report.txt").is_file()
    assert (ws.meta / "partition_workspace.json").is_file()


# ── Test 5: zero-byte image is ignored ───────────────────────────────────────

def test_zero_byte_image_is_ignored(tmp_path):
    ws = _make_ws(tmp_path)
    # Write zero-byte files
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"")
    result = {
        "route": "image_folder",
        "images": {p: str(ws.images / f"{p}.img") for p in _ALL_PARTITIONS},
    }
    selected = mezo_select_partition_images(result)
    for req in _REQUIRED:
        assert selected[req] is None, f"Zero-byte {req}.img should be ignored (None)"


# ── Test 6: output partition folders stay inside ws.partitions ────────────────

def test_output_folders_inside_workspace(tmp_path):
    ws = _make_ws(tmp_path)
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)
    su_result = _ok_smart_unpack_result(ws, img_dir=ws.images)

    captured_targets: list[Path] = []

    def fake_extract(img_path, partition_name, _ws, _tc):
        entry = _mock_extraction_ok(partition_name, _ws)
        captured_targets.append(Path(entry["extracted_path"]))
        return entry

    with patch("factory.core.partition_workspace.mezo_extract_partition_image", side_effect=fake_extract), \
         patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()), \
         patch("factory.core.partition_workspace.mezo_regenerate_fs_metadata", return_value={}):
        deadzone_partition_workspace_stage(ws, smart_unpack_result=su_result)

    partitions_root = ws.partitions.resolve()
    for target in captured_targets:
        resolved = target.resolve()
        assert str(resolved).startswith(str(partitions_root)), (
            f"Partition folder {resolved} is outside ws.partitions {partitions_root}"
        )


# ── Test 7: original ROM input is preserved ───────────────────────────────────

def test_original_rom_input_preserved(tmp_path):
    # Place a fake ROM image outside the workspace
    rom_dir = tmp_path / "original_rom"
    rom_dir.mkdir()
    for part in ("system", "product", "vendor"):
        (rom_dir / f"{part}.img").write_bytes(b"\xAB\xCD" * 256)
    original_sizes = {
        p: (rom_dir / f"{p}.img").stat().st_size
        for p in ("system", "product", "vendor")
    }

    ws = _make_ws(tmp_path)
    # Simulate smart_unpack pointing to original paths
    images = {p: str(rom_dir / f"{p}.img") for p in _ALL_PARTITIONS if (rom_dir / f"{p}.img").exists()}
    for p in _ALL_PARTITIONS:
        images.setdefault(p, None)
    su_result = {
        "route": "image_folder",
        "images": images,
        "super_img": None,
    }

    def fake_extract(img_path, partition_name, _ws, _tc):
        return _mock_extraction_ok(partition_name, _ws)

    with patch("factory.core.partition_workspace.mezo_extract_partition_image", side_effect=fake_extract), \
         patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()), \
         patch("factory.core.partition_workspace.mezo_regenerate_fs_metadata", return_value={}):
        deadzone_partition_workspace_stage(ws, smart_unpack_result=su_result)

    for part, original_size in original_sizes.items():
        current_size = (rom_dir / f"{part}.img").stat().st_size
        assert current_size == original_size, (
            f"Original ROM input {part}.img was modified (size changed)"
        )


# ── Test 8: partition_workspace.json is generated ─────────────────────────────

def test_partition_workspace_json_generated(tmp_path):
    ws = _make_ws(tmp_path)
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)
    su_result = _ok_smart_unpack_result(ws, img_dir=ws.images)

    def fake_extract(img_path, partition_name, _ws, _tc):
        return _mock_extraction_ok(partition_name, _ws)

    with patch("factory.core.partition_workspace.mezo_extract_partition_image", side_effect=fake_extract), \
         patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()), \
         patch("factory.core.partition_workspace.mezo_regenerate_fs_metadata", return_value={}):
        deadzone_partition_workspace_stage(ws, smart_unpack_result=su_result)

    json_path = ws.meta / "partition_workspace.json"
    assert json_path.is_file(), "partition_workspace.json not generated"
    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert data.get("status") in ("OK", "PARTIAL")
    assert "partition_results" in data
    assert data.get("no_mods_executed") is True


# ── Test 9: deadzone_partition_workspace_report.txt is generated ──────────────

def test_partition_workspace_report_generated(tmp_path):
    ws = _make_ws(tmp_path)
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)
    su_result = _ok_smart_unpack_result(ws, img_dir=ws.images)

    def fake_extract(img_path, partition_name, _ws, _tc):
        return _mock_extraction_ok(partition_name, _ws)

    with patch("factory.core.partition_workspace.mezo_extract_partition_image", side_effect=fake_extract), \
         patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()), \
         patch("factory.core.partition_workspace.mezo_regenerate_fs_metadata", return_value={}):
        deadzone_partition_workspace_stage(ws, smart_unpack_result=su_result)

    report_path = ws.reports / "deadzone_partition_workspace_report.txt"
    assert report_path.is_file(), "deadzone_partition_workspace_report.txt not generated"
    text = report_path.read_text(encoding="utf-8")
    assert "DeadZone Partition Workspace Report" in text
    assert "no mods executed" in text
    assert "smart_unpack route" in text


# ── Test 10: fs_config/file_contexts metadata recorded when available ─────────

def test_fs_metadata_recorded_when_available(tmp_path):
    ws = _make_ws(tmp_path)
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)
    su_result = _ok_smart_unpack_result(ws, img_dir=ws.images)

    fake_fs_result = {
        "partition": "system",
        "status": "ok",
        "fs_config": {
            "partition": "system",
            "fs_config_path": str(ws.partitions / "system" / "fs_config"),
            "entries_before": 0, "entries_added": 5, "entries_after": 5,
        },
        "file_contexts": {
            "partition": "system",
            "file_contexts_path": str(ws.partitions / "system" / "file_contexts"),
            "entries_before": 0, "entries_added": 5, "entries_after": 5,
        },
    }

    def fake_extract(img_path, partition_name, _ws, _tc):
        return _mock_extraction_ok(partition_name, _ws)

    with patch("factory.core.partition_workspace.mezo_extract_partition_image", side_effect=fake_extract), \
         patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()), \
         patch("factory.core.partition_workspace.mezo_regenerate_fs_metadata", return_value=fake_fs_result):
        result = deadzone_partition_workspace_stage(ws, smart_unpack_result=su_result)

    assert result["fs_metadata"], "fs_metadata should not be empty when partitions extracted"
    first_meta = result["fs_metadata"][0]
    assert "fs_config" in first_meta
    assert "file_contexts" in first_meta

    # Also verify it appears in the report text
    report_text = (ws.reports / "deadzone_partition_workspace_report.txt").read_text(encoding="utf-8")
    assert "fs_config path" in report_text
    assert "file_contexts" in report_text


# ── Test 11: --stop-after partition_workspace stops before repack/super/mods ──

def test_stop_after_partition_workspace_no_repack(tmp_path):
    """Verify the deadzone CLI pipeline does not invoke repack/super/app policy."""
    from factory.deadzone import BuildContext, _run_partition_workspace_only
    from factory.core.workspace import create_workspace
    import time

    ws = create_workspace(tmp_path / "workspace")
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)

    ok_su_result = {
        "route": "image_folder",
        "status": "OK",
        "images": {p: str(ws.images / f"{p}.img") for p in _ALL_PARTITIONS if (ws.images / f"{p}.img").exists()},
        "super_img": None,
        "missing_required": [],
        "missing_optional": list(_OPTIONAL),
        "reports": [],
        "error": "",
    }
    for p in _ALL_PARTITIONS:
        ok_su_result["images"].setdefault(p, None)

    ctx = BuildContext(
        rom_url=str(tmp_path / "rom.zip"),
        style="stable",
        style_label="Stable",
        soc="mtk",
        mode="build",
        workspace=ws,
        stop_after="partition_workspace",
        started_at=time.time(),
    )

    repack_called = []
    super_called = []
    app_policy_called = []

    def fake_extract_img(img_path, partition_name, _ws, _tc):
        return _mock_extraction_ok(partition_name, _ws)

    with patch("factory.deadzone._prepare_workspace", return_value=ws), \
         patch("factory.deadzone.download_rom", return_value=tmp_path / "rom.zip"), \
         patch("factory.deadzone.detect_rom", return_value=MagicMock(codename="test", android_version="14", build="V21")), \
         patch("factory.deadzone.resolve_device", return_value={"codename": "test", "resolved_codename": "test", "name": "Test", "soc": "mtk", "profile_source": "test", "super": {}}), \
         patch("factory.deadzone._acquire_build_lock"), \
         patch("factory.deadzone._update_resolved_device_metadata"), \
         patch("factory.deadzone._sync_device_to_state"), \
         patch("factory.deadzone._warn_on_codename_mismatch"), \
         patch("factory.deadzone._run_smart_unpack_stage", return_value=ok_su_result), \
         patch("factory.core.partition_workspace.mezo_extract_partition_image", side_effect=fake_extract_img), \
         patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()), \
         patch("factory.core.partition_workspace.mezo_regenerate_fs_metadata", return_value={}), \
         patch("factory.deadzone.repack_partitions", side_effect=lambda *a, **k: repack_called.append(1)), \
         patch("factory.deadzone.build_repacked_super", side_effect=lambda *a, **k: super_called.append(1)), \
         patch("factory.deadzone.enforce_stable_app_policy", side_effect=lambda *a, **k: app_policy_called.append(1)):
        # Assign smart_unpack_result so the partition_workspace stage can read it
        ctx.smart_unpack_result = ok_su_result
        ctx.smart_unpack_route = "image_folder"
        _run_partition_workspace_only(ctx)

    assert not repack_called, "repack_partitions must not be called in partition_workspace mode"
    assert not super_called, "build_repacked_super must not be called in partition_workspace mode"
    assert not app_policy_called, "enforce_stable_app_policy must not be called in partition_workspace mode"
    assert ctx.status == "OK"


# ── Test 12: no HyperUR runtime import ───────────────────────────────────────

def test_no_hyperur_import(tmp_path):
    source = Path(__file__).parent.parent / "factory" / "core" / "partition_workspace.py"
    tree = ast.parse(source.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = (
                [alias.name for alias in node.names]
                if isinstance(node, ast.Import)
                else ([node.module] if node.module else [])
            )
            for name in names:
                assert "hyperur" not in (name or "").lower(), (
                    f"HyperUR runtime imported in partition_workspace.py: {name}"
                )


# ── Test 13: no mod/smali/UI keywords ────────────────────────────────────────

_BANNED_KEYWORDS = {
    "smali", "MiuiSystemUI", "Provision", "Wukong", "USAGI_UI",
    "clock_style", "icon_style", "framework.jar", "services.jar",
    "signature_bypass", "flag_secure", "spoofing",
}


def test_no_mod_keywords_in_module(tmp_path):
    source = Path(__file__).parent.parent / "factory" / "core" / "partition_workspace.py"
    text = source.read_text(encoding="utf-8")
    for keyword in _BANNED_KEYWORDS:
        assert keyword not in text, (
            f"Banned keyword {keyword!r} found in partition_workspace.py"
        )


# ── Test 14: public functions use mezo_* or deadzone_* ───────────────────────

def test_public_function_naming():
    source = Path(__file__).parent.parent / "factory" / "core" / "partition_workspace.py"
    tree = ast.parse(source.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            name = node.name
            if name.startswith("_"):
                continue  # private helper, exempt
            assert name.startswith("mezo_") or name.startswith("deadzone_"), (
                f"Public function {name!r} does not use mezo_* or deadzone_* prefix"
            )


# ── Test 15: existing Phase 1–6 core modules still import cleanly ─────────────

def test_existing_phase1_to_6_modules_import():
    modules = [
        "factory.core.smart_unpack",
        "factory.core.payload_extract",
        "factory.core.rom_intake",
        "factory.core.image_extractor",
        "factory.core.fs_config",
        "factory.core.workspace",
        "factory.core.reports",
        "factory.core.detector",
        "factory.adapters.super",
        "factory.adapters.images",
        "factory.core.unpacker",
        "factory.deadzone",
    ]
    for module_name in modules:
        try:
            mod = importlib.import_module(module_name)
            assert mod is not None, f"Module {module_name} imported as None"
        except ImportError as exc:
            pytest.fail(f"Existing module {module_name!r} failed to import: {exc}")
