"""
Phase 2 ROM intake tests.

Covers:
- zip safe extraction
- tar safe extraction
- traversal blocked (../ and absolute paths)
- raw img passthrough
- payload.bin detection (root and nested)
- missing payload reported cleanly
- build.prop metadata parsed (codename, model, marketname, brand, mi_version, android_release)
- original ROM input preserved after intake
- intake report contains all required sections
- archive type detection
"""
from __future__ import annotations

import io
import struct
import tarfile
import zipfile
from pathlib import Path
from typing import Any

import pytest

from factory.core.rom_intake import (
    ARCHIVE_RAW,
    ARCHIVE_TAR,
    ARCHIVE_TGZ,
    ARCHIVE_ZIP,
    deadzone_rom_intake,
    deadzone_write_rom_intake_report,
    mezo_detect_archive_type,
    mezo_extract_rom_archive,
    mezo_find_payload_bin,
    mezo_parse_single_build_prop,
    mezo_read_build_prop_metadata,
)
from factory.core.unpacker import _safe_destination
from factory.core.workspace import create_workspace


def _make_ws(tmp_path: Path):
    return create_workspace(tmp_path / "workspace")


def _fake_payload_bytes() -> bytes:
    """Build a minimal syntactically-valid payload.bin header."""
    manifest = b"\x00" * 4
    sig_len = 4
    header = struct.pack(">4sQQI", b"CrAU", 2, len(manifest), sig_len)
    return header + manifest + b"\x00" * sig_len


# ── 1. ZIP safe extraction ────────────────────────────────────────────────────

def test_zip_safe_extraction(tmp_path):
    """mezo_extract_rom_archive extracts a valid zip and returns 'zip'."""
    rom_zip = tmp_path / "rom.zip"
    with zipfile.ZipFile(rom_zip, "w") as zf:
        zf.writestr("system/build.prop", "ro.product.device=marble\n")
        zf.writestr("payload.bin", _fake_payload_bytes())

    dst = tmp_path / "extracted"
    archive_type = mezo_extract_rom_archive(rom_zip, dst)

    assert archive_type == ARCHIVE_ZIP
    assert (dst / "system" / "build.prop").is_file()
    assert (dst / "payload.bin").is_file()
    # original must survive
    assert rom_zip.is_file(), "original ROM zip must not be deleted"


# ── 2. TAR safe extraction ────────────────────────────────────────────────────

def test_tar_safe_extraction(tmp_path):
    """mezo_extract_rom_archive extracts a valid tar and returns 'tar'."""
    rom_tar = tmp_path / "rom.tar"
    with tarfile.open(rom_tar, "w") as tf:
        data = b"fake_img_content"
        info = tarfile.TarInfo(name="images/system.img")
        info.size = len(data)
        tf.addfile(info, io.BytesIO(data))

    dst = tmp_path / "extracted"
    archive_type = mezo_extract_rom_archive(rom_tar, dst)

    assert archive_type == ARCHIVE_TAR
    assert (dst / "images" / "system.img").is_file()
    assert rom_tar.is_file(), "original ROM tar must not be deleted"


def test_tgz_safe_extraction(tmp_path):
    """mezo_extract_rom_archive extracts a .tgz and returns 'tgz'."""
    rom_tgz = tmp_path / "rom.tgz"
    with tarfile.open(rom_tgz, "w:gz") as tf:
        data = b"vendor_data"
        info = tarfile.TarInfo(name="vendor/build.prop")
        info.size = len(data)
        tf.addfile(info, io.BytesIO(data))

    dst = tmp_path / "extracted"
    archive_type = mezo_extract_rom_archive(rom_tgz, dst)

    assert archive_type == ARCHIVE_TGZ
    assert (dst / "vendor" / "build.prop").is_file()
    assert rom_tgz.is_file()


# ── 3. Traversal protection ───────────────────────────────────────────────────

def test_traversal_dotdot_in_zip_is_blocked(tmp_path):
    """mezo_extract_rom_archive refuses zip members with ../ path components."""
    evil_zip = tmp_path / "evil.zip"
    with zipfile.ZipFile(evil_zip, "w") as zf:
        zf.writestr("../../../etc/passwd", "evil")

    dst = tmp_path / "extracted"
    with pytest.raises(RuntimeError, match="escapes workspace"):
        mezo_extract_rom_archive(evil_zip, dst)


def test_traversal_absolute_path_blocked_via_safe_destination(tmp_path):
    """_safe_destination raises for absolute-path archive members."""
    root = tmp_path / "extracted"
    root.mkdir()
    with pytest.raises(RuntimeError, match="escapes workspace"):
        _safe_destination(root, "/etc/shadow")


def test_traversal_dotdot_blocked_via_safe_destination(tmp_path):
    """_safe_destination raises for ../ escape attempts."""
    root = tmp_path / "extracted"
    root.mkdir()
    with pytest.raises(RuntimeError, match="escapes workspace"):
        _safe_destination(root, "../../outside/secret.txt")


def test_traversal_safe_member_passes(tmp_path):
    """_safe_destination allows legitimate nested paths."""
    root = tmp_path / "extracted"
    root.mkdir()
    result = _safe_destination(root, "images/system.img")
    assert result == (root / "images" / "system.img").resolve()


# ── 4. Raw img passthrough ────────────────────────────────────────────────────

def test_raw_img_passthrough(tmp_path):
    """A raw .img file is copied as-is without extraction; returns 'raw'."""
    raw_img = tmp_path / "super.img"
    raw_img.write_bytes(b"\x53\xEF" + b"\x00" * 510)  # ext4-like magic

    dst = tmp_path / "extracted"
    archive_type = mezo_extract_rom_archive(raw_img, dst)

    assert archive_type == ARCHIVE_RAW
    assert (dst / "super.img").is_file()
    assert (dst / "super.img").read_bytes()[:2] == b"\x53\xEF"
    assert raw_img.is_file(), "original img must not be deleted"
    assert raw_img.stat().st_size > 0, "original img must not be modified"


# ── 5. Payload.bin detection ──────────────────────────────────────────────────

def test_payload_bin_found_at_root(tmp_path):
    """mezo_find_payload_bin detects payload.bin at the extracted root."""
    extracted = tmp_path / "extracted"
    extracted.mkdir()
    payload = extracted / "payload.bin"
    payload.write_bytes(_fake_payload_bytes())

    found = mezo_find_payload_bin(extracted)
    assert len(found) == 1
    assert found[0] == payload


def test_payload_bin_found_nested(tmp_path):
    """mezo_find_payload_bin detects payload.bin nested in a subdirectory."""
    extracted = tmp_path / "extracted"
    nested = extracted / "META-INF" / "com" / "google" / "android"
    nested.mkdir(parents=True)
    (nested / "payload.bin").write_bytes(b"CrAU")

    found = mezo_find_payload_bin(extracted)
    assert len(found) == 1
    assert found[0].name == "payload.bin"


def test_payload_bin_multiple_found(tmp_path):
    """mezo_find_payload_bin returns all matches when multiple exist."""
    extracted = tmp_path / "extracted"
    (extracted / "a").mkdir(parents=True)
    (extracted / "b").mkdir(parents=True)
    (extracted / "a" / "payload.bin").write_bytes(b"CrAU")
    (extracted / "b" / "payload.bin").write_bytes(b"CrAU")

    found = mezo_find_payload_bin(extracted)
    assert len(found) == 2


# ── 6. Missing payload reported cleanly ──────────────────────────────────────

def test_missing_payload_returns_empty_list(tmp_path):
    """mezo_find_payload_bin returns [] (no exception) when payload.bin is absent."""
    extracted = tmp_path / "extracted"
    extracted.mkdir()
    (extracted / "system").mkdir()
    (extracted / "system" / "build.prop").write_text("ro.product.device=test\n")

    found = mezo_find_payload_bin(extracted)
    assert found == []


def test_intake_missing_payload_in_report(tmp_path):
    """deadzone_rom_intake writes MISSING to the report when no payload.bin exists."""
    rom_zip = tmp_path / "no_payload.zip"
    with zipfile.ZipFile(rom_zip, "w") as zf:
        zf.writestr("system/build.prop", "ro.product.device=marble\n")

    ws = _make_ws(tmp_path)
    result = deadzone_rom_intake(rom_zip, ws)

    assert result["payload_found"] is False
    assert result["payload_locations"] == []

    report = ws.reports / "deadzone_rom_intake_report.txt"
    assert report.is_file()
    content = report.read_text()
    assert "MISSING" in content


# ── 7. Build.prop metadata parsed ────────────────────────────────────────────

def test_build_prop_metadata_all_fields(tmp_path):
    """mezo_read_build_prop_metadata extracts all expected fields from odm/build.prop."""
    extracted = tmp_path / "extracted"
    odm = extracted / "odm"
    odm.mkdir(parents=True)
    (odm / "build.prop").write_text(
        "ro.product.odm.device=camellia\n"
        "ro.product.odm.model=2201117TY\n"
        "ro.product.odm.marketname=Redmi Note 11\n"
        "ro.product.odm.brand=Redmi\n"
        "ro.mi.os.version.incremental=OS1.0.3.0.TGCMIXM\n"
        "ro.system.build.version.release=13\n",
        encoding="utf-8",
    )

    meta = mezo_read_build_prop_metadata(extracted)

    assert meta["codename"] == "camellia"
    assert meta["model"] == "2201117TY"
    assert meta["marketname"] == "Redmi Note 11"
    assert meta["brand"] == "Redmi"
    assert meta["mi_version"] == "OS1.0.3.0.TGCMIXM"
    assert meta["android_release"] == "13"
    assert meta["prop_files_found"] == 1


def test_build_prop_metadata_vendor_fallback(tmp_path):
    """mezo_read_build_prop_metadata falls back to vendor props when odm is absent."""
    extracted = tmp_path / "extracted"
    vendor = extracted / "vendor"
    vendor.mkdir(parents=True)
    (vendor / "build.prop").write_text(
        "ro.product.vendor.device=sunstone\n"
        "ro.product.vendor.marketname=POCO X5\n"
        "ro.product.vendor.brand=POCO\n"
        "ro.system.build.version.release=12\n",
        encoding="utf-8",
    )

    meta = mezo_read_build_prop_metadata(extracted)
    assert meta["codename"] == "sunstone"
    assert meta["marketname"] == "POCO X5"
    assert meta["brand"] == "POCO"
    assert meta["android_release"] == "12"


def test_parse_single_build_prop_filters_unknown_keys(tmp_path):
    """mezo_parse_single_build_prop discards keys not in the intake key set."""
    prop_file = tmp_path / "build.prop"
    prop_file.write_text(
        "ro.product.odm.device=marble\n"
        "ro.product.odm.marketname=POCO F4 GT\n"
        "ro.some.random.unknown.key=ignored\n"
        "# this is a comment\n"
        "malformed_no_equals\n",
        encoding="utf-8",
    )

    result = mezo_parse_single_build_prop(prop_file)
    assert result["ro.product.odm.device"] == "marble"
    assert result["ro.product.odm.marketname"] == "POCO F4 GT"
    assert "ro.some.random.unknown.key" not in result


def test_parse_single_build_prop_missing_file(tmp_path):
    """mezo_parse_single_build_prop returns {} for a non-existent file."""
    result = mezo_parse_single_build_prop(tmp_path / "nonexistent.prop")
    assert result == {}


def test_read_build_prop_metadata_empty_extracted(tmp_path):
    """mezo_read_build_prop_metadata returns zeroed fields when no build.prop exists."""
    extracted = tmp_path / "empty_extracted"
    extracted.mkdir()

    meta = mezo_read_build_prop_metadata(extracted)
    assert meta["codename"] == ""
    assert meta["prop_files_found"] == 0


# ── 8. Original ROM input preserved ──────────────────────────────────────────

def test_original_rom_preserved_after_zip_intake(tmp_path):
    """deadzone_rom_intake never deletes or modifies the original ROM zip."""
    rom_zip = tmp_path / "original_rom.zip"
    with zipfile.ZipFile(rom_zip, "w") as zf:
        zf.writestr("system/build.prop", "ro.product.device=marble\n")
    original_size = rom_zip.stat().st_size

    ws = _make_ws(tmp_path)
    deadzone_rom_intake(rom_zip, ws)

    assert rom_zip.is_file(), "original ROM must still exist after intake"
    assert rom_zip.stat().st_size == original_size, "original ROM must not be modified"


def test_original_rom_preserved_after_raw_intake(tmp_path):
    """deadzone_rom_intake never deletes or modifies a raw .img input."""
    raw_img = tmp_path / "super.img"
    raw_img.write_bytes(b"\x00" * 1024)
    original_size = raw_img.stat().st_size

    ws = _make_ws(tmp_path)
    deadzone_rom_intake(raw_img, ws)

    assert raw_img.is_file()
    assert raw_img.stat().st_size == original_size


# ── 9. Intake report completeness ─────────────────────────────────────────────

def test_intake_report_sections_present(tmp_path):
    """deadzone_write_rom_intake_report produces a report with all required sections."""
    ws = _make_ws(tmp_path)
    intake_result: dict[str, Any] = {
        "input_rom": str(tmp_path / "rom.zip"),
        "archive_type": "zip",
        "payload_found": True,
        "payload_locations": ["payload.bin"],
        "extracted_roots": ["payload.bin", "system"],
        "metadata": {
            "codename": "marble",
            "model": "22101320G",
            "marketname": "POCO F4 GT",
            "brand": "POCO",
            "mi_version": "OS1.0.4.0.TLMMIXM",
            "android_release": "13",
            "prop_files_found": 2,
        },
    }

    report_path = deadzone_write_rom_intake_report(ws, intake_result)

    assert report_path.is_file()
    content = report_path.read_text()
    assert "input_rom" in content
    assert "archive_type" in content
    assert "payload_status    : FOUND" in content
    assert "codename        : marble" in content
    assert "marketname      : POCO F4 GT" in content
    assert "mi_version      : OS1.0.4.0.TLMMIXM" in content
    assert "android_release : 13" in content


def test_intake_report_missing_payload_label(tmp_path):
    """Report labels payload as MISSING when payload_found is False."""
    ws = _make_ws(tmp_path)
    intake_result: dict[str, Any] = {
        "input_rom": "/some/rom.zip",
        "archive_type": "zip",
        "payload_found": False,
        "payload_locations": [],
        "extracted_roots": ["system"],
        "metadata": {
            "codename": "redwood",
            "model": "",
            "marketname": "",
            "brand": "",
            "mi_version": "",
            "android_release": "14",
            "prop_files_found": 1,
        },
    }

    report_path = deadzone_write_rom_intake_report(ws, intake_result)
    content = report_path.read_text()
    assert "MISSING" in content


def test_full_intake_creates_meta_json(tmp_path):
    """deadzone_rom_intake writes rom_intake.json to the meta directory."""
    rom_zip = tmp_path / "rom.zip"
    with zipfile.ZipFile(rom_zip, "w") as zf:
        zf.writestr("odm/build.prop", "ro.product.odm.device=stone\n")

    ws = _make_ws(tmp_path)
    deadzone_rom_intake(rom_zip, ws)

    meta_file = ws.meta / "rom_intake.json"
    assert meta_file.is_file()
    import json
    data = json.loads(meta_file.read_text())
    assert data["archive_type"] == "zip"
    assert data["metadata"]["codename"] == "stone"


# ── 10. Archive type detection ────────────────────────────────────────────────

def test_detect_archive_type_zip(tmp_path):
    rom = tmp_path / "rom.zip"
    with zipfile.ZipFile(rom, "w") as zf:
        zf.writestr("f.txt", "data")
    assert mezo_detect_archive_type(rom) == ARCHIVE_ZIP


def test_detect_archive_type_tar(tmp_path):
    rom = tmp_path / "rom.tar"
    with tarfile.open(rom, "w") as tf:
        info = tarfile.TarInfo(name="f.txt")
        info.size = 4
        tf.addfile(info, io.BytesIO(b"data"))
    assert mezo_detect_archive_type(rom) == ARCHIVE_TAR


def test_detect_archive_type_tgz_by_name(tmp_path):
    rom = tmp_path / "rom.tgz"
    with tarfile.open(rom, "w:gz") as tf:
        info = tarfile.TarInfo(name="f.txt")
        info.size = 4
        tf.addfile(info, io.BytesIO(b"data"))
    assert mezo_detect_archive_type(rom) == ARCHIVE_TGZ


def test_detect_archive_type_raw_img(tmp_path):
    rom = tmp_path / "super.img"
    rom.write_bytes(b"\x00" * 512)
    assert mezo_detect_archive_type(rom) == ARCHIVE_RAW


# ── 11. Naming convention — rom_intake module ─────────────────────────────────

def test_rom_intake_module_naming_convention():
    """All public functions in rom_intake.py must start with mezo_* or deadzone_*."""
    import ast
    path = Path("factory/core/rom_intake.py")
    assert path.is_file(), f"rom_intake.py not found at {path}"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    violations = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            name = node.name
            if name.startswith("_"):
                continue
            if not (name.startswith("mezo_") or name.startswith("deadzone_")):
                violations.append(name)
    assert not violations, (
        "Public functions in rom_intake.py must use mezo_* or deadzone_* prefix.\n"
        "Violations: " + ", ".join(violations)
    )
