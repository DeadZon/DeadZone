"""
DeadZone Phase 8 – Partition Workspace real extraction tests.

Coverage (18 tests):
 1.  sparse image is detected and simg2img conversion is called
 2.  sparse conversion output stays inside ws.root/raw_images/
 3.  original sparse image bytes are preserved after conversion
 4.  ext4 image routes to EXT4 extractor
 5.  erofs image fails cleanly with EXTRACTOR_TOOL_MISSING when no tool present
 6.  unknown image type fails cleanly via 7z fallback
 7.  zero-byte image is ignored and recorded in zero_byte_ignored
 8.  required partition extraction failure raises after report is written
 9.  optional partition extraction failure is reported but not fatal
10.  fs_config/file_contexts metadata is recorded when available
11.  super route reports not_wired cleanly when lpunpack missing
12.  no lpmake or final super build referenced in partition_workspace module
13.  no repack / app-policy / smali keywords in partition_workspace module
14.  no HyperUR runtime import in partition_workspace module (Phase 8 re-check)
15.  no banned mod/smali/UI keywords in partition_workspace module (Phase 8 re-check)
16.  all new Phase 8 public functions use mezo_* or deadzone_* prefix
17.  --stop-after partition_workspace does not call repack/super/app policy
18.  existing Phase 1–7 core modules still import cleanly
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
    mezo_convert_sparse_image_if_needed,
    mezo_detect_partition_image_format,
    mezo_extract_erofs_image,
    mezo_extract_ext4_image,
    mezo_extract_partition_image,
    mezo_extract_partition_workspace,
    mezo_extract_super_to_images,
    mezo_select_partition_images,
    mezo_validate_partition_workspace,
)
from factory.core.workspace import create_workspace

_ALL_PARTITIONS = [
    "system", "product", "vendor",
    "system_ext", "odm", "mi_ext", "system_dlkm", "vendor_dlkm",
]
_REQUIRED = {"system", "product", "vendor"}
_OPTIONAL = {"system_ext", "odm", "mi_ext", "system_dlkm", "vendor_dlkm"}

_ANDROID_SPARSE_MAGIC = b"\x3a\xff\x26\xed"
_EXT4_MAGIC_512 = (b"\x00" * 0x438) + b"\x53\xef" + (b"\x00" * (512 - 0x438 - 2))
_EROFS_MAGIC = b"EROFS" + b"\x00" * 2043


def _make_ws(tmp_path: Path):
    return create_workspace(tmp_path / "workspace")


def _mock_extraction_ok(partition_name: str, ws) -> dict[str, Any]:
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
        "converted_image": None,
    }


def _ok_su_result(ws, route="image_folder"):
    images = {}
    for p in _ALL_PARTITIONS:
        candidate = ws.images / f"{p}.img"
        images[p] = str(candidate) if candidate.is_file() and candidate.stat().st_size > 0 else None
    return {
        "route": route,
        "status": "OK",
        "images": images,
        "super_img": None,
        "missing_required": [],
        "missing_optional": list(_OPTIONAL),
        "reports": [],
        "error": "",
    }


# ── Test 1: sparse image detected → simg2img called ──────────────────────────

def test_sparse_image_simg2img_called(tmp_path):
    ws = _make_ws(tmp_path)
    sparse_img = ws.images / "system.img"
    sparse_img.write_bytes(_ANDROID_SPARSE_MAGIC + b"\x00" * 512)

    simg2img_calls: list[list[str]] = []
    mock_tc = MagicMock()
    mock_tc.path.side_effect = lambda name: Path("/fake/simg2img") if name == "simg2img" else None

    def fake_run(cmd, log, cwd=None):
        simg2img_calls.append(list(cmd))
        out = Path(cmd[-1])
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(b"\x00" * 1024)
        return 0, ""

    with patch("factory.core.partition_workspace._run", side_effect=fake_run):
        result = mezo_convert_sparse_image_if_needed(sparse_img, "system", ws, mock_tc)

    assert simg2img_calls, "simg2img was not called for sparse image"
    assert result["converted"] is True, "converted should be True after successful simg2img"
    assert any("simg2img" in str(c[0]) for c in simg2img_calls), (
        "simg2img binary not used in the command"
    )


# ── Test 2: sparse conversion output in ws.root/raw_images/ ──────────────────

def test_sparse_conversion_output_in_raw_images(tmp_path):
    ws = _make_ws(tmp_path)
    sparse_img = ws.images / "vendor.img"
    sparse_img.write_bytes(_ANDROID_SPARSE_MAGIC + b"\x00" * 512)

    mock_tc = MagicMock()
    mock_tc.path.side_effect = lambda name: Path("/fake/simg2img") if name == "simg2img" else None

    def fake_run(cmd, log, cwd=None):
        out = Path(cmd[-1])
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(b"\x00" * 1024)
        return 0, ""

    with patch("factory.core.partition_workspace._run", side_effect=fake_run):
        result = mezo_convert_sparse_image_if_needed(sparse_img, "vendor", ws, mock_tc)

    assert result["converted"] is True
    raw_path = Path(result["raw_path"])
    expected_dir = (ws.root / "raw_images").resolve()
    assert raw_path.resolve().parent == expected_dir, (
        f"Raw image {raw_path} is not inside {expected_dir}"
    )


# ── Test 3: original sparse image preserved ───────────────────────────────────

def test_original_sparse_image_preserved(tmp_path):
    ws = _make_ws(tmp_path)
    original_bytes = _ANDROID_SPARSE_MAGIC + b"\xDE\xAD\xBE\xEF" * 128
    sparse_img = ws.images / "product.img"
    sparse_img.write_bytes(original_bytes)

    mock_tc = MagicMock()
    mock_tc.path.side_effect = lambda name: Path("/fake/simg2img") if name == "simg2img" else None

    def fake_run(cmd, log, cwd=None):
        out = Path(cmd[-1])
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(b"\x00" * 1024)
        return 0, ""

    with patch("factory.core.partition_workspace._run", side_effect=fake_run):
        mezo_convert_sparse_image_if_needed(sparse_img, "product", ws, mock_tc)

    assert sparse_img.read_bytes() == original_bytes, (
        "Original sparse image was modified during conversion"
    )


# ── Test 4: ext4 image routes to EXT4 extractor ──────────────────────────────

def test_ext4_image_routes_to_ext4_extractor(tmp_path):
    ws = _make_ws(tmp_path)
    ext4_img = ws.images / "system.img"
    # Minimal fake EXT4: superblock magic at 0x438
    data = bytearray(4096)
    data[0x438] = 0x53
    data[0x439] = 0xEF
    ext4_img.write_bytes(bytes(data))

    mock_tc = MagicMock()
    mock_tc.path.return_value = None

    extract_ext4_calls: list[Path] = []

    def fake_extract_ext4(image, target, toolchain, log):
        extract_ext4_calls.append(image)
        target.mkdir(parents=True, exist_ok=True)
        (target / "build.prop").write_text("# fake ext4\n")
        return "extracted", "python-ext4", "factory.core._ext4"

    with patch("factory.core.partition_workspace._extract_ext4", side_effect=fake_extract_ext4):
        result = mezo_extract_ext4_image(ext4_img, "system", ws, mock_tc)

    assert extract_ext4_calls, "_extract_ext4 was not called for EXT4 image"
    assert result["status"] == "extracted"
    assert result["extractor_used"] == "python-ext4"


# ── Test 5: erofs fails cleanly with EXTRACTOR_TOOL_MISSING ──────────────────

def test_erofs_fails_cleanly_when_extractor_missing(tmp_path):
    ws = _make_ws(tmp_path)
    erofs_img = ws.images / "product.img"
    erofs_img.write_bytes(_EROFS_MAGIC + b"\x00" * 512)

    mock_tc = MagicMock()
    mock_tc.path.return_value = None  # No EROFS tools

    def fake_extract_erofs(image, target, toolchain, log, cap_log):
        return (
            "failed",
            "no EROFS extraction or listing method available — install erofs-utils",
            "",
        )

    with patch("factory.core.partition_workspace._extract_erofs", side_effect=fake_extract_erofs):
        result = mezo_extract_erofs_image(erofs_img, "product", ws, mock_tc)

    assert result["status"] == "failed"
    assert result["error_type"] == "EXTRACTOR_TOOL_MISSING", (
        f"Expected EXTRACTOR_TOOL_MISSING, got {result['error_type']!r}"
    )
    assert "erofs" in result["error"].lower()


# ── Test 6: unknown image type fails cleanly ──────────────────────────────────

def test_unknown_image_type_fails_cleanly(tmp_path):
    ws = _make_ws(tmp_path)
    unknown_img = ws.images / "system.img"
    unknown_img.write_bytes(b"\xFF\xFE\xFD\xFC" + b"\x00" * 512)

    mock_tc = MagicMock()
    mock_tc.path.return_value = None

    detection = mezo_detect_partition_image_format(unknown_img, mock_tc)
    assert detection["format"] == "unknown", (
        f"Expected 'unknown', got {detection['format']!r}"
    )

    def fake_7z(image, target, toolchain, log):
        return "failed", "7z not available", ""

    with patch("factory.core.partition_workspace._extract_7z", side_effect=fake_7z):
        result = mezo_extract_partition_image(unknown_img, "system", ws, mock_tc)

    assert result["status"] == "failed"
    assert result.get("failure_reason") or result.get("error"), (
        "Unknown-format failure should have a reason/error field"
    )


# ── Test 7: zero-byte image ignored and recorded ──────────────────────────────

def test_zero_byte_image_ignored_and_recorded(tmp_path):
    ws = _make_ws(tmp_path)
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"")

    su_result = {
        "route": "image_folder",
        "images": {p: str(ws.images / f"{p}.img") for p in ("system", "product", "vendor")},
        "super_img": None,
    }
    for p in _ALL_PARTITIONS:
        su_result["images"].setdefault(p, None)

    with patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()):
        extraction = mezo_extract_partition_workspace(su_result, ws)

    zero_byte = extraction.get("zero_byte_ignored") or []
    for part in ("system", "product", "vendor"):
        assert part in zero_byte, f"Zero-byte {part} not in zero_byte_ignored"


# ── Test 8: required partition failure raises after report is written ──────────

def test_required_partition_failure_raises_after_report(tmp_path):
    ws = _make_ws(tmp_path)
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)

    su_result = _ok_su_result(ws)

    def fake_extract(img_path, partition_name, _ws, _tc):
        return {
            "partition": partition_name,
            "source_image": str(img_path) if img_path else "",
            "detected_format": "raw_ext4",
            "extraction_method": "ext4",
            "tool_path": "",
            "extracted_path": str(_ws.partitions / partition_name),
            "status": "failed",
            "failure_reason": "no EXT4 extraction method available",
            "file_count": 0, "directory_count": 0, "total_extracted_bytes": 0,
            "converted_image": None,
        }

    with patch("factory.core.partition_workspace.mezo_extract_partition_image", side_effect=fake_extract), \
         patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()), \
         patch("factory.core.partition_workspace.mezo_regenerate_fs_metadata", return_value={}):
        with pytest.raises(RuntimeError) as exc_info:
            deadzone_partition_workspace_stage(ws, smart_unpack_result=su_result)

    msg = str(exc_info.value)
    assert any(p in msg for p in ("system", "product", "vendor")), (
        f"RuntimeError should name a required partition, got: {msg}"
    )
    # Report and JSON must be written before the raise
    assert (ws.reports / "deadzone_partition_workspace_report.txt").is_file(), (
        "Report must be written even on failure"
    )
    assert (ws.meta / "partition_workspace.json").is_file(), (
        "JSON must be written even on failure"
    )


# ── Test 9: optional partition failure not fatal ──────────────────────────────

def test_optional_partition_failure_not_fatal(tmp_path):
    ws = _make_ws(tmp_path)
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)
    (ws.images / "system_ext.img").write_bytes(b"\x00" * 512)

    su_result = {
        "route": "image_folder",
        "images": {p: str(ws.images / f"{p}.img")
                   for p in ("system", "product", "vendor", "system_ext")},
        "super_img": None,
    }
    for p in _ALL_PARTITIONS:
        su_result["images"].setdefault(p, None)

    def fake_extract(img_path, partition_name, _ws, _tc):
        if partition_name in ("system", "product", "vendor"):
            return _mock_extraction_ok(partition_name, _ws)
        return {
            "partition": partition_name,
            "source_image": str(img_path) if img_path else "",
            "detected_format": "unknown",
            "extraction_method": "",
            "tool_path": "",
            "extracted_path": str(_ws.partitions / partition_name),
            "status": "failed",
            "failure_reason": "extractor unavailable",
            "file_count": 0, "directory_count": 0, "total_extracted_bytes": 0,
            "converted_image": None,
        }

    with patch("factory.core.partition_workspace.mezo_extract_partition_image", side_effect=fake_extract), \
         patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()), \
         patch("factory.core.partition_workspace.mezo_regenerate_fs_metadata", return_value={}):
        result = deadzone_partition_workspace_stage(ws, smart_unpack_result=su_result)

    assert result["status"] in ("OK", "PARTIAL"), (
        f"Optional partition failure must not make status FAILED, got {result['status']}"
    )


# ── Test 10: fs_config/file_contexts metadata recorded ───────────────────────

def test_fs_metadata_paths_recorded(tmp_path):
    ws = _make_ws(tmp_path)
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)
    su_result = _ok_su_result(ws)

    fake_fs = {
        "partition": "system",
        "status": "ok",
        "fs_config": {
            "partition": "system",
            "fs_config_path": str(ws.partitions / "system" / "fs_config"),
            "entries_before": 0, "entries_added": 3, "entries_after": 3,
        },
        "file_contexts": {
            "partition": "system",
            "file_contexts_path": str(ws.partitions / "system" / "file_contexts"),
            "entries_before": 0, "entries_added": 3, "entries_after": 3,
        },
    }

    def fake_extract(img_path, partition_name, _ws, _tc):
        return _mock_extraction_ok(partition_name, _ws)

    with patch("factory.core.partition_workspace.mezo_extract_partition_image", side_effect=fake_extract), \
         patch("factory.core.partition_workspace.resolve_toolchain", return_value=MagicMock()), \
         patch("factory.core.partition_workspace.mezo_regenerate_fs_metadata", return_value=fake_fs):
        result = deadzone_partition_workspace_stage(ws, smart_unpack_result=su_result)

    assert result.get("fs_metadata"), "fs_metadata should not be empty"
    assert result.get("fs_config"), "fs_config map should be populated"
    assert result.get("file_contexts"), "file_contexts map should be populated"

    report_text = (ws.reports / "deadzone_partition_workspace_report.txt").read_text(encoding="utf-8")
    assert "fs_config path" in report_text
    assert "file_contexts" in report_text


# ── Test 11: super route → not_wired when lpunpack missing ───────────────────

def test_super_route_not_wired_when_lpunpack_missing(tmp_path):
    ws = _make_ws(tmp_path)
    (ws.images / "super.img").write_bytes(b"\x00" * 1024)

    mock_tc = MagicMock()
    mock_tc.path.return_value = None  # No lpunpack

    result = mezo_extract_super_to_images(ws, mock_tc)

    assert result["status"] == "not_wired", (
        f"Expected not_wired when lpunpack absent, got {result['status']!r}"
    )
    assert "lpunpack" in result["reason"].lower() or "not wired" in result["reason"].lower()
    assert result["extracted_partitions"] == []


def test_super_route_not_wired_when_super_img_absent(tmp_path):
    ws = _make_ws(tmp_path)
    # No super.img written
    mock_tc = MagicMock()
    mock_tc.path.side_effect = lambda name: Path("/fake/lpunpack") if name == "lpunpack" else None

    result = mezo_extract_super_to_images(ws, mock_tc)

    assert result["status"] == "not_wired"
    assert "super.img" in result["reason"].lower() or "not found" in result["reason"].lower()


# ── Test 12: no lpmake / final super build in module ─────────────────────────

def test_no_lpmake_or_final_super_build():
    source = Path(__file__).parent.parent / "factory" / "core" / "partition_workspace.py"
    text = source.read_text(encoding="utf-8")
    assert "lpmake" not in text, "lpmake referenced in partition_workspace.py"
    assert "build_repacked_super" not in text, (
        "build_repacked_super referenced in partition_workspace.py"
    )
    assert "final_super" not in text.lower(), (
        "final_super referenced in partition_workspace.py"
    )


# ── Test 13: no repack / app-policy / smali keywords ─────────────────────────

def test_no_repack_or_app_policy_keywords():
    source = Path(__file__).parent.parent / "factory" / "core" / "partition_workspace.py"
    text = source.read_text(encoding="utf-8")
    banned = [
        "repack_partitions",
        "enforce_stable_app_policy",
        "smali",
        "MiuiSystemUI",
        "Provision",
        "Wukong",
        "USAGI_UI",
        "clock_style",
        "icon_style",
    ]
    for keyword in banned:
        assert keyword not in text, (
            f"Banned keyword {keyword!r} found in partition_workspace.py"
        )


# ── Test 14: no HyperUR runtime import ───────────────────────────────────────

def test_no_hyperur_import_phase8():
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


# ── Test 15: no banned mod/smali/UI keywords ─────────────────────────────────

_BANNED_KEYWORDS = {
    "smali", "MiuiSystemUI", "Provision", "Wukong", "USAGI_UI",
    "clock_style", "icon_style", "framework.jar", "services.jar",
    "signature_bypass", "flag_secure", "spoofing",
}


def test_no_mod_keywords_phase8():
    source = Path(__file__).parent.parent / "factory" / "core" / "partition_workspace.py"
    text = source.read_text(encoding="utf-8")
    for keyword in _BANNED_KEYWORDS:
        assert keyword not in text, (
            f"Banned keyword {keyword!r} found in partition_workspace.py"
        )


# ── Test 16: new Phase 8 public functions use mezo_* or deadzone_* ───────────

def test_phase8_public_function_naming():
    source = Path(__file__).parent.parent / "factory" / "core" / "partition_workspace.py"
    tree = ast.parse(source.read_text(encoding="utf-8"))
    phase8_fns = {
        "mezo_detect_partition_image_format",
        "mezo_convert_sparse_image_if_needed",
        "mezo_extract_ext4_image",
        "mezo_extract_erofs_image",
        "mezo_extract_super_to_images",
    }
    found: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            name = node.name
            if name.startswith("_"):
                continue
            assert name.startswith("mezo_") or name.startswith("deadzone_"), (
                f"Public function {name!r} does not use mezo_* or deadzone_* prefix"
            )
            found.add(name)
    for fn in phase8_fns:
        assert fn in found, f"Expected Phase 8 public function {fn!r} not found in module"


# ── Test 17: --stop-after partition_workspace still stops ────────────────────

def test_stop_after_partition_workspace_no_repack_phase8(tmp_path):
    from factory.deadzone import BuildContext, _run_partition_workspace_only
    import time

    ws = create_workspace(tmp_path / "workspace")
    for part in ("system", "product", "vendor"):
        (ws.images / f"{part}.img").write_bytes(b"\x00" * 512)

    ok_su_result = {
        "route": "image_folder",
        "status": "OK",
        "images": {p: str(ws.images / f"{p}.img")
                   for p in ("system", "product", "vendor")},
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
    ctx.smart_unpack_result = ok_su_result
    ctx.smart_unpack_route = "image_folder"

    repack_called = []
    super_called = []
    app_policy_called = []

    def fake_extract_img(img_path, partition_name, _ws, _tc):
        return _mock_extraction_ok(partition_name, _ws)

    with patch("factory.deadzone._prepare_workspace", return_value=ws), \
         patch("factory.deadzone.download_rom", return_value=tmp_path / "rom.zip"), \
         patch("factory.deadzone.detect_rom", return_value=MagicMock(
             codename="test", android_version="14", build="V21")), \
         patch("factory.deadzone.resolve_device", return_value={
             "codename": "test", "resolved_codename": "test",
             "name": "Test", "soc": "mtk", "profile_source": "test", "super": {}}), \
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
        _run_partition_workspace_only(ctx)

    assert not repack_called, "repack_partitions must not be called in partition_workspace mode"
    assert not super_called, "build_repacked_super must not be called in partition_workspace mode"
    assert not app_policy_called, "enforce_stable_app_policy must not be called in partition_workspace mode"


# ── Test 18: existing Phase 1–7 core modules still import cleanly ─────────────

def test_existing_phase1_to_7_modules_import():
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
        "factory.core.partition_workspace",
        "factory.deadzone",
    ]
    for module_name in modules:
        try:
            mod = importlib.import_module(module_name)
            assert mod is not None, f"Module {module_name} imported as None"
        except ImportError as exc:
            pytest.fail(f"Module {module_name!r} failed to import: {exc}")
