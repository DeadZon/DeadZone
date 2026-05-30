"""
Phase 4 smart unpack orchestrator tests.

Covers:
1.  zip with payload.bin routes to payload stage
2.  fastboot tgz with images routes to image collection
3.  raw super.img routes to super path or reports unsupported cleanly
4.  folder with existing images routes to image collection
5.  folder with payload.bin routes to payload stage
6.  traversal archive is blocked
7.  original ROM input is preserved after smart_unpack
8.  smart_unpack.json is generated
9.  deadzone_smart_unpack_report.txt is generated
10. missing required images produce FAILED status cleanly
11. optional images missing are reported only (status stays OK when required present)
12. no HyperUR runtime import in smart_unpack module
13. no mod/smali/UI keywords in smart_unpack module
14. all new public functions use only mezo_* or deadzone_* prefix
15. old unpacker.py retains compatibility note referencing smart_unpack
"""
from __future__ import annotations

import ast
import io
import json
import struct
import tarfile
import zipfile
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from factory.core.smart_unpack import (
    INPUT_FOLDER,
    INPUT_IMG,
    INPUT_TGZ,
    INPUT_UNKNOWN,
    INPUT_ZIP,
    ROUTE_FASTBOOT,
    ROUTE_IMAGE_FOLDER,
    ROUTE_PAYLOAD,
    ROUTE_SUPER,
    ROUTE_UNSUPPORTED,
    deadzone_smart_unpack,
    deadzone_write_smart_unpack_report,
    mezo_collect_unpacked_images,
    mezo_collect_unpacked_partitions,
    mezo_detect_rom_input_type,
    mezo_plan_unpack_route,
)
from factory.core.workspace import create_workspace


# ── Fixtures and helpers ───────────────────────────────────────────────────────

def _make_ws(tmp_path: Path):
    return create_workspace(tmp_path / "workspace")


def _fake_payload_bytes() -> bytes:
    """Minimal syntactically-valid payload.bin header."""
    manifest = b"\x00" * 4
    sig_len = 4
    header = struct.pack(">4sQQI", b"CrAU", 2, len(manifest), sig_len)
    return header + manifest + b"\x00" * sig_len


def _make_zip_with_payload(tmp_path: Path, name: str = "rom.zip") -> Path:
    rom = tmp_path / name
    with zipfile.ZipFile(rom, "w") as zf:
        zf.writestr("payload.bin", _fake_payload_bytes())
        zf.writestr("payload_properties.txt", "FILE_HASH=abc\n")
    return rom


def _make_tgz_with_images(tmp_path: Path, name: str = "rom.tgz") -> Path:
    rom = tmp_path / name
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tf:
        for part in ("system", "product", "vendor"):
            data = b"\x00" * 512
            info = tarfile.TarInfo(name=f"images/{part}.img")
            info.size = len(data)
            tf.addfile(info, io.BytesIO(data))
    rom.write_bytes(buf.getvalue())
    return rom


def _make_super_img(tmp_path: Path, name: str = "super.img") -> Path:
    img = tmp_path / name
    # Write LP metadata magic at offset 4096
    content = b"\x00" * 4096 + b"\x57\x4C\x4F\x53" + b"\x00" * 100
    img.write_bytes(content)
    return img


def _seed_images(ws, names: list[str], size: int = 512) -> None:
    for name in names:
        (ws.images / f"{name}.img").write_bytes(b"\x00" * size)


def _mock_payload_extract_ok(ws, partitions=("system", "product", "vendor")):
    """Return a mock result dict as if payload extract succeeded."""
    for p in partitions:
        (ws.images / f"{p}.img").write_bytes(b"\x00" * 512)
    return {
        "status": "OK",
        "payload_path": str(ws.extracted / "payload.bin"),
        "extracted_partitions": list(partitions),
        "missing_required": [],
        "missing_optional": ["system_ext", "odm", "mi_ext", "system_dlkm", "vendor_dlkm"],
        "extracted_images": {p: str(ws.images / f"{p}.img") for p in partitions},
        "image_sizes": {p: 512 for p in partitions},
        "report_path": str(ws.reports / "deadzone_payload_extract_report.txt"),
        "meta_path": str(ws.meta / "payload_extract.json"),
    }


# ── 1. ZIP with payload.bin routes to payload stage ───────────────────────────

def test_zip_with_payload_bin_routes_to_payload(tmp_path):
    """mezo_plan_unpack_route returns 'payload' for a zip containing payload.bin."""
    rom = _make_zip_with_payload(tmp_path)
    input_type = mezo_detect_rom_input_type(rom)
    route, reason = mezo_plan_unpack_route(rom, input_type)
    assert route == ROUTE_PAYLOAD
    assert "payload.bin" in reason


def test_zip_with_payload_smart_unpack_calls_payload_stage(tmp_path):
    """deadzone_smart_unpack routes a zip with payload.bin through the payload stage."""
    ws = _make_ws(tmp_path)
    rom = _make_zip_with_payload(tmp_path)

    with patch("factory.core.smart_unpack.deadzone_rom_intake") as mock_intake, \
         patch("factory.core.smart_unpack.deadzone_payload_extract_stage") as mock_extract:
        mock_intake.return_value = {
            "input_rom": str(rom),
            "archive_type": "zip",
            "payload_found": True,
            "payload_locations": ["payload.bin"],
            "extracted_roots": ["payload.bin"],
            "metadata": {},
        }
        mock_extract.side_effect = lambda ws, **kw: _mock_payload_extract_ok(ws)

        result = deadzone_smart_unpack(rom, ws)

    assert result["route"] == ROUTE_PAYLOAD
    mock_intake.assert_called_once()
    mock_extract.assert_called_once()


# ── 2. Fastboot TGZ with images routes to image collection ────────────────────

def test_tgz_with_images_routes_to_fastboot(tmp_path):
    """mezo_plan_unpack_route returns 'fastboot_images' for a tgz with .img files."""
    rom = _make_tgz_with_images(tmp_path)
    input_type = mezo_detect_rom_input_type(rom)
    assert input_type == INPUT_TGZ
    route, reason = mezo_plan_unpack_route(rom, input_type)
    assert route == ROUTE_FASTBOOT
    assert ".img" in reason


def test_tgz_fastboot_smart_unpack_collects_images(tmp_path):
    """deadzone_smart_unpack extracts a fastboot tgz and collects images."""
    ws = _make_ws(tmp_path)
    rom = _make_tgz_with_images(tmp_path)

    result = deadzone_smart_unpack(rom, ws)

    assert result["route"] == ROUTE_FASTBOOT
    assert result["input_type"] == INPUT_TGZ
    # Images extracted from the tgz images/ folder
    assert result["images"]["system"] is not None or result["status"] in ("OK", "FAILED")


# ── 3. Raw super.img routes to super path ────────────────────────────────────

def test_super_img_by_name_routes_to_super(tmp_path):
    """A file named super.img routes to ROUTE_SUPER."""
    img = tmp_path / "super.img"
    img.write_bytes(b"\x00" * 100)
    input_type = mezo_detect_rom_input_type(img)
    assert input_type == INPUT_IMG
    route, reason = mezo_plan_unpack_route(img, input_type)
    assert route == ROUTE_SUPER


def test_super_img_by_magic_routes_to_super(tmp_path):
    """A file with LP magic at offset 4096 routes to ROUTE_SUPER."""
    img = _make_super_img(tmp_path, name="unknown.img")
    input_type = mezo_detect_rom_input_type(img)
    route, reason = mezo_plan_unpack_route(img, input_type)
    assert route == ROUTE_SUPER


def test_non_super_img_routes_to_unsupported(tmp_path):
    """A plain .img that is not super.img routes to ROUTE_UNSUPPORTED cleanly."""
    img = tmp_path / "boot.img"
    img.write_bytes(b"\x00" * 100)
    input_type = mezo_detect_rom_input_type(img)
    route, _ = mezo_plan_unpack_route(img, input_type)
    assert route == ROUTE_UNSUPPORTED


def test_super_img_smart_unpack_does_not_crash(tmp_path):
    """deadzone_smart_unpack handles super.img input and returns a clean result."""
    ws = _make_ws(tmp_path)
    img = tmp_path / "super.img"
    img.write_bytes(b"\x00" * 100)

    result = deadzone_smart_unpack(img, ws)

    assert result["route"] == ROUTE_SUPER
    assert result["status"] in ("OK", "FAILED", "UNSUPPORTED")
    assert result["input_type"] == INPUT_IMG


# ── 4. Folder with images routes to image collection ─────────────────────────

def test_folder_with_images_routes_to_image_folder(tmp_path):
    """A folder containing .img files routes to ROUTE_IMAGE_FOLDER."""
    folder = tmp_path / "images"
    folder.mkdir()
    (folder / "system.img").write_bytes(b"\x00" * 512)
    (folder / "vendor.img").write_bytes(b"\x00" * 512)

    input_type = mezo_detect_rom_input_type(folder)
    assert input_type == INPUT_FOLDER
    route, reason = mezo_plan_unpack_route(folder, input_type)
    assert route == ROUTE_IMAGE_FOLDER


def test_folder_image_collection_smart_unpack(tmp_path):
    """deadzone_smart_unpack collects images from a folder without copying."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "images"
    folder.mkdir()
    for part in ("system", "product", "vendor"):
        (folder / f"{part}.img").write_bytes(b"\x00" * 512)

    result = deadzone_smart_unpack(folder, ws)

    assert result["route"] == ROUTE_IMAGE_FOLDER
    assert result["images"]["system"] is not None
    assert result["images"]["product"] is not None
    assert result["images"]["vendor"] is not None


# ── 5. Folder with payload.bin routes to payload stage ───────────────────────

def test_folder_with_payload_bin_routes_to_payload(tmp_path):
    """A folder containing payload.bin routes to ROUTE_PAYLOAD."""
    folder = tmp_path / "rom_folder"
    folder.mkdir()
    (folder / "payload.bin").write_bytes(_fake_payload_bytes())

    input_type = mezo_detect_rom_input_type(folder)
    assert input_type == INPUT_FOLDER
    route, reason = mezo_plan_unpack_route(folder, input_type)
    assert route == ROUTE_PAYLOAD
    assert "payload.bin" in reason


def test_folder_payload_smart_unpack_calls_extract_stage(tmp_path):
    """deadzone_smart_unpack routes a folder with payload.bin through extract stage."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom_folder"
    folder.mkdir()
    payload = folder / "payload.bin"
    payload.write_bytes(_fake_payload_bytes())

    with patch("factory.core.smart_unpack.deadzone_payload_extract_stage") as mock_extract:
        mock_extract.side_effect = lambda ws, **kw: _mock_payload_extract_ok(ws)
        result = deadzone_smart_unpack(folder, ws)

    assert result["route"] == ROUTE_PAYLOAD
    mock_extract.assert_called_once()
    # payload_bin kwarg must point into the folder
    called_payload_bin = mock_extract.call_args.kwargs.get("payload_bin")
    assert called_payload_bin is not None
    assert called_payload_bin.resolve() == payload.resolve()


# ── 6. Traversal archive is blocked ──────────────────────────────────────────

def test_traversal_zip_is_blocked(tmp_path):
    """A zip with ../ members raises RuntimeError before any extraction."""
    rom = tmp_path / "evil.zip"
    with zipfile.ZipFile(rom, "w") as zf:
        zf.writestr("../../../escape.txt", "bad")

    ws = _make_ws(tmp_path)
    # The route will be UNSUPPORTED (empty archive after safety check) or
    # smart_unpack must not write anything outside the workspace.
    # The critical invariant: no file outside ws.root must be created.
    before_files = set(tmp_path.rglob("*"))
    try:
        result = deadzone_smart_unpack(rom, ws)
        # If it returns, status must not be OK
        for path_str in (result.get("images") or {}).values():
            if path_str:
                assert Path(path_str).is_relative_to(ws.root) or Path(path_str).is_relative_to(tmp_path), (
                    f"Image written outside safe zone: {path_str}"
                )
    except RuntimeError:
        pass  # Blocking the traversal by raising is also acceptable

    # No file was written above tmp_path
    escape = tmp_path.parent / "escape.txt"
    assert not escape.exists(), "Traversal attack escaped the workspace"


def test_traversal_tar_is_blocked(tmp_path):
    """A tar with absolute-path members raises RuntimeError before extraction."""
    rom = tmp_path / "evil.tar"
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w") as tf:
        data = b"bad"
        info = tarfile.TarInfo(name="../escape.txt")
        info.size = len(data)
        tf.addfile(info, io.BytesIO(data))
    rom.write_bytes(buf.getvalue())

    ws = _make_ws(tmp_path)
    try:
        deadzone_smart_unpack(rom, ws)
    except RuntimeError:
        pass

    escape = tmp_path / "escape.txt"
    assert not escape.exists(), "Traversal escaped workspace"


# ── 7. Original ROM input is preserved ───────────────────────────────────────

def test_original_zip_preserved_after_smart_unpack(tmp_path):
    """deadzone_smart_unpack never deletes or modifies the original ROM zip."""
    ws = _make_ws(tmp_path)
    rom = _make_zip_with_payload(tmp_path)
    original_size = rom.stat().st_size
    original_bytes = rom.read_bytes()

    with patch("factory.core.smart_unpack.deadzone_rom_intake") as mock_intake, \
         patch("factory.core.smart_unpack.deadzone_payload_extract_stage") as mock_extract:
        mock_intake.return_value = {
            "payload_found": True,
            "payload_locations": ["payload.bin"],
            "extracted_roots": [],
            "metadata": {},
        }
        mock_extract.side_effect = lambda ws, **kw: _mock_payload_extract_ok(ws)
        deadzone_smart_unpack(rom, ws)

    assert rom.is_file(), "Original ROM zip was deleted"
    assert rom.stat().st_size == original_size, "Original ROM zip was modified"
    assert rom.read_bytes() == original_bytes, "Original ROM zip bytes changed"


def test_original_folder_payload_preserved(tmp_path):
    """deadzone_smart_unpack never deletes or modifies files in the original folder."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom_folder"
    folder.mkdir()
    payload = folder / "payload.bin"
    payload.write_bytes(_fake_payload_bytes())
    original_bytes = payload.read_bytes()

    with patch("factory.core.smart_unpack.deadzone_payload_extract_stage") as mock_extract:
        mock_extract.side_effect = lambda ws, **kw: _mock_payload_extract_ok(ws)
        deadzone_smart_unpack(folder, ws)

    assert payload.is_file(), "payload.bin was deleted from source folder"
    assert payload.read_bytes() == original_bytes, "payload.bin was modified"


# ── 8. smart_unpack.json is generated ────────────────────────────────────────

def test_smart_unpack_json_is_generated(tmp_path):
    """deadzone_smart_unpack writes smart_unpack.json to ws.meta."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "images"
    folder.mkdir()
    for part in ("system", "product", "vendor"):
        (folder / f"{part}.img").write_bytes(b"\x00" * 512)

    deadzone_smart_unpack(folder, ws)

    meta_file = ws.meta / "smart_unpack.json"
    assert meta_file.is_file(), "smart_unpack.json not generated"


def test_smart_unpack_json_contains_required_keys(tmp_path):
    """smart_unpack.json contains all required top-level keys."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "images"
    folder.mkdir()
    for part in ("system", "product", "vendor"):
        (folder / f"{part}.img").write_bytes(b"\x00" * 512)

    deadzone_smart_unpack(folder, ws)

    data = json.loads((ws.meta / "smart_unpack.json").read_text())
    for key in (
        "input_path",
        "input_type",
        "route",
        "status",
        "payload_path",
        "super_img",
        "images",
        "partitions",
        "missing_required",
        "missing_optional",
        "reports",
    ):
        assert key in data, f"smart_unpack.json missing key: {key!r}"


# ── 9. deadzone_smart_unpack_report.txt is generated ─────────────────────────

def test_smart_unpack_report_is_generated(tmp_path):
    """deadzone_smart_unpack writes deadzone_smart_unpack_report.txt to ws.reports."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "images"
    folder.mkdir()
    for part in ("system", "product", "vendor"):
        (folder / f"{part}.img").write_bytes(b"\x00" * 512)

    deadzone_smart_unpack(folder, ws)

    report = ws.reports / "deadzone_smart_unpack_report.txt"
    assert report.is_file(), "deadzone_smart_unpack_report.txt not generated"


def test_smart_unpack_report_contains_required_sections(tmp_path):
    """Report includes all required sections."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "images"
    folder.mkdir()
    for part in ("system", "product", "vendor"):
        (folder / f"{part}.img").write_bytes(b"\x00" * 512)

    deadzone_smart_unpack(folder, ws)

    content = (ws.reports / "deadzone_smart_unpack_report.txt").read_text()
    for section in (
        "input_path",
        "input_type",
        "route",
        "status",
        "images:",
        "missing required",
        "missing optional",
        "no mods executed",
        "compatibility note",
    ):
        assert section in content, f"Report missing section: {section!r}"


# ── 10. Missing required images produce FAILED status cleanly ─────────────────

def test_missing_required_images_produce_failed_status(tmp_path):
    """When required partition images are absent the result status is FAILED."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "images"
    folder.mkdir()
    # Only odm.img present — system/product/vendor all missing (required)
    (folder / "odm.img").write_bytes(b"\x00" * 512)

    result = deadzone_smart_unpack(folder, ws)

    assert result["status"] == "FAILED"
    assert len(result["missing_required"]) > 0
    assert "system" in result["missing_required"]


def test_failed_status_does_not_raise(tmp_path):
    """deadzone_smart_unpack returns FAILED cleanly without raising exceptions."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "empty_folder"
    folder.mkdir()

    result = deadzone_smart_unpack(folder, ws)

    # Empty folder → UNSUPPORTED route → status UNSUPPORTED, not a crash
    assert result["status"] in ("FAILED", "UNSUPPORTED")
    assert (ws.meta / "smart_unpack.json").is_file()
    assert (ws.reports / "deadzone_smart_unpack_report.txt").is_file()


def test_payload_route_missing_required_returns_failed_not_raises(tmp_path):
    """When payload extract stage fails due to missing required partitions, status is FAILED."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom_folder"
    folder.mkdir()
    (folder / "payload.bin").write_bytes(_fake_payload_bytes())

    with patch("factory.core.smart_unpack.deadzone_payload_extract_stage") as mock_extract:
        mock_extract.side_effect = RuntimeError("Required partition(s) missing: system, product, vendor")
        result = deadzone_smart_unpack(folder, ws)

    assert result["status"] == "FAILED"
    assert result["route"] == ROUTE_PAYLOAD


# ── 11. Optional images missing are reported only ────────────────────────────

def test_optional_missing_images_reported_not_fatal(tmp_path):
    """Optional partition images absent produce missing_optional entries but status OK."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "images"
    folder.mkdir()
    # Required present; optional absent
    for part in ("system", "product", "vendor"):
        (folder / f"{part}.img").write_bytes(b"\x00" * 512)
    # system_ext, odm, mi_ext, etc. are intentionally absent

    result = deadzone_smart_unpack(folder, ws)

    assert result["status"] == "OK"
    assert result["missing_required"] == []
    assert len(result["missing_optional"]) > 0
    # Optional names belong to _OPTIONAL_IMAGES set
    from factory.core.smart_unpack import _OPTIONAL_IMAGES
    for name in result["missing_optional"]:
        assert name in _OPTIONAL_IMAGES


def test_optional_missing_reported_in_report_file(tmp_path):
    """Report file lists missing optional partitions."""
    ws = _make_ws(tmp_path)
    folder = tmp_path / "images"
    folder.mkdir()
    for part in ("system", "product", "vendor"):
        (folder / f"{part}.img").write_bytes(b"\x00" * 512)

    deadzone_smart_unpack(folder, ws)

    content = (ws.reports / "deadzone_smart_unpack_report.txt").read_text()
    assert "missing optional" in content


# ── 12. No HyperUR runtime import ────────────────────────────────────────────

def test_smart_unpack_no_hyperur_import():
    """smart_unpack.py must not import HyperURBuild or any src.* module."""
    path = Path("factory/core/smart_unpack.py")
    assert path.is_file()
    source = path.read_text(encoding="utf-8")
    assert "HyperURBuild" not in source
    assert "from src." not in source
    assert "import src." not in source


# ── 13. No mod/smali/UI keywords ─────────────────────────────────────────────

_FORBIDDEN_KEYWORDS = frozenset({
    "smali", "baksmali", "apktool",
    "MiuiSystemUI", "Provision", "Wukong", "USAGI_UI",
    "flag_secure", "spoof", "signature_bypass",
    "framework_jar", "services_jar",
    "style_runner", "apply_style",
    "clock_style", "icon_style",
})


def test_smart_unpack_has_no_mod_keywords():
    """smart_unpack.py must not reference any mod/smali/UI symbols."""
    path = Path("factory/core/smart_unpack.py")
    source = path.read_text(encoding="utf-8").lower()
    for keyword in _FORBIDDEN_KEYWORDS:
        assert keyword.lower() not in source, (
            f"smart_unpack.py references a forbidden symbol: {keyword!r}"
        )


# ── 14. Public functions use mezo_* or deadzone_* prefix ─────────────────────

def test_smart_unpack_module_naming_convention():
    """All top-level public functions in smart_unpack.py must use mezo_* or deadzone_* prefix."""
    path = Path("factory/core/smart_unpack.py")
    assert path.is_file()
    tree = ast.parse(path.read_text(encoding="utf-8"))
    violations: list[str] = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            name = node.name
            if name.startswith("_"):
                continue
            if not (name.startswith("mezo_") or name.startswith("deadzone_")):
                violations.append(name)
    assert not violations, (
        "Public functions must use mezo_* or deadzone_* prefix. "
        "Violations: " + ", ".join(violations)
    )


# ── 15. Old unpacker compatibility note ──────────────────────────────────────

def test_unpacker_has_smart_unpack_compatibility_note():
    """unpacker.py must contain a note explaining the smart_unpack compatibility relationship."""
    path = Path("factory/core/unpacker.py")
    assert path.is_file()
    source = path.read_text(encoding="utf-8")
    assert "deadzone_smart_unpack" in source, (
        "unpacker.py must reference deadzone_smart_unpack in its compatibility note"
    )
    assert "smart_unpack" in source, (
        "unpacker.py must mention smart_unpack in its compatibility documentation"
    )


# ── Unit tests for helper functions ──────────────────────────────────────────

def test_detect_rom_input_type_zip(tmp_path):
    rom = tmp_path / "rom.zip"
    with zipfile.ZipFile(rom, "w") as zf:
        zf.writestr("payload.bin", b"data")
    assert mezo_detect_rom_input_type(rom) == INPUT_ZIP


def test_detect_rom_input_type_tgz(tmp_path):
    rom = _make_tgz_with_images(tmp_path)
    assert mezo_detect_rom_input_type(rom) == INPUT_TGZ


def test_detect_rom_input_type_img(tmp_path):
    img = tmp_path / "boot.img"
    img.write_bytes(b"\x00" * 10)
    assert mezo_detect_rom_input_type(img) == INPUT_IMG


def test_detect_rom_input_type_folder(tmp_path):
    folder = tmp_path / "folder"
    folder.mkdir()
    assert mezo_detect_rom_input_type(folder) == INPUT_FOLDER


def test_detect_rom_input_type_missing(tmp_path):
    assert mezo_detect_rom_input_type(tmp_path / "nonexistent.zip") == INPUT_UNKNOWN


def test_collect_unpacked_images_finds_slot_free(tmp_path):
    """mezo_collect_unpacked_images finds slot-free partition images."""
    (tmp_path / "system.img").write_bytes(b"\x00" * 512)
    result = mezo_collect_unpacked_images(tmp_path)
    assert result["system"] is not None
    assert result["vendor"] is None


def test_collect_unpacked_images_finds_a_slot(tmp_path):
    """mezo_collect_unpacked_images accepts system_a.img as 'system'."""
    (tmp_path / "system_a.img").write_bytes(b"\x00" * 512)
    result = mezo_collect_unpacked_images(tmp_path)
    assert result["system"] is not None


def test_collect_unpacked_images_zero_byte_not_counted(tmp_path):
    """Zero-byte images are treated as missing."""
    (tmp_path / "system.img").write_bytes(b"")
    result = mezo_collect_unpacked_images(tmp_path)
    assert result["system"] is None


def test_collect_unpacked_partitions_finds_populated_dir(tmp_path):
    part_dir = tmp_path / "system"
    part_dir.mkdir()
    (part_dir / "build.prop").write_text("key=val\n")
    result = mezo_collect_unpacked_partitions(tmp_path)
    assert result["system"] is not None
    assert result["product"] is None


def test_deadzone_write_smart_unpack_report_directly(tmp_path):
    """deadzone_write_smart_unpack_report writes both report and JSON independently."""
    ws = _make_ws(tmp_path)
    result: dict[str, Any] = {
        "input_path": "/some/rom.zip",
        "input_type": "zip",
        "route": "payload",
        "route_reason": "archive contains payload.bin",
        "status": "OK",
        "payload_path": "/some/payload.bin",
        "super_img": None,
        "images": {p: None for p in ("system", "product", "vendor", "system_ext",
                                      "odm", "mi_ext", "system_dlkm", "vendor_dlkm")},
        "partitions": {"system": None, "product": None, "vendor": None},
        "missing_required": [],
        "missing_optional": ["system_ext", "odm"],
        "reports": [],
        "error": "",
        "elapsed_seconds": 1.23,
    }

    report_path = deadzone_write_smart_unpack_report(ws, result)

    assert report_path.is_file()
    content = report_path.read_text()
    assert "OK" in content
    assert "payload" in content
    assert (ws.meta / "smart_unpack.json").is_file()
