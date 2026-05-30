"""
Phase 3 payload extraction stage tests.

Covers:
1.  payload extraction wrapper calls existing DeadZone adapter correctly
2.  output images are written to workspace only
3.  required partitions missing fails cleanly with RuntimeError
4.  optional partitions missing are reported only (no exception)
5.  original ROM and payload.bin are preserved
6.  report is generated with required sections
7.  JSON metadata is generated with required keys
8.  all public functions use mezo_* or deadzone_* prefix only
9.  no mod/smali imports or calls appear in the module
"""
from __future__ import annotations

import ast
import json
import struct
import zipfile
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from factory.core.payload_extract import (
    DEFAULT_PARTITIONS,
    OPTIONAL_PARTITIONS,
    REQUIRED_PARTITIONS,
    deadzone_payload_extract_stage,
    deadzone_write_payload_extract_report,
    mezo_extract_payload_partitions,
    mezo_select_default_payload_partitions,
    mezo_validate_extracted_payload_images,
)
from factory.core.workspace import create_workspace


# ── Fixtures ──────────────────────────────────────────────────────────────────

def _make_ws(tmp_path: Path):
    return create_workspace(tmp_path / "workspace")


def _fake_payload_bytes() -> bytes:
    """Minimal valid payload.bin header (no real manifest data)."""
    manifest = b"\x00" * 4
    sig_len = 4
    header = struct.pack(">4sQQI", b"CrAU", 2, len(manifest), sig_len)
    return header + manifest + b"\x00" * sig_len


def _place_payload(ws, content: bytes | None = None) -> Path:
    """Write a payload.bin into ws.extracted and return its path."""
    payload = ws.extracted / "payload.bin"
    payload.write_bytes(content or _fake_payload_bytes())
    return payload


def _seed_images(ws, names: list[str], size: int = 1024) -> None:
    """Create fake .img files in ws.images to simulate successful extraction."""
    for name in names:
        img = ws.images / f"{name}.img"
        img.write_bytes(b"\x00" * size)


def _fake_tool_run(ws, partitions: list[str]) -> MagicMock:
    """Mock subprocess.run that creates .img files in ws.images."""
    def _run_side_effect(cmd, **kwargs):
        out_dir = Path(cmd[cmd.index("-o") + 1])
        parts_str = cmd[cmd.index("-partitions") + 1]
        for name in parts_str.split(","):
            (out_dir / f"{name}.img").write_bytes(b"\x00" * 512)
        m = MagicMock()
        m.returncode = 0
        m.stderr = ""
        return m

    return _run_side_effect


# ── 1. Wrapper calls existing adapter correctly ───────────────────────────────

def test_extraction_calls_resolve_payload_tool(tmp_path):
    """mezo_extract_payload_partitions resolves the tool via the DeadZone adapter."""
    payload = tmp_path / "payload.bin"
    payload.write_bytes(_fake_payload_bytes())
    out_dir = tmp_path / "out"
    fake_tool = tmp_path / "payload-dumper-go"
    fake_tool.write_bytes(b"")

    with patch("factory.core.payload_extract._resolve_payload_tool", return_value=fake_tool), \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        result = mezo_extract_payload_partitions(payload, out_dir, ["system", "vendor"])

    mock_run.assert_called_once()
    call_args = mock_run.call_args[0][0]
    assert str(fake_tool) in call_args[0]
    assert "-partitions" in call_args
    assert "system,vendor" in call_args
    assert "-o" in call_args
    assert str(payload) in call_args


def test_extraction_uses_partition_flag(tmp_path):
    """-partitions flag is passed with comma-joined list to payload-dumper-go."""
    payload = tmp_path / "payload.bin"
    payload.write_bytes(b"data")
    out_dir = tmp_path / "out"
    fake_tool = tmp_path / "tool"

    with patch("factory.core.payload_extract._resolve_payload_tool", return_value=fake_tool), \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        mezo_extract_payload_partitions(payload, out_dir, ["system", "product", "vendor"])

    cmd = mock_run.call_args[0][0]
    idx = cmd.index("-partitions")
    assert cmd[idx + 1] == "system,product,vendor"


def test_extraction_creates_output_dir(tmp_path):
    """mezo_extract_payload_partitions creates out_dir if it does not exist."""
    payload = tmp_path / "payload.bin"
    payload.write_bytes(b"data")
    out_dir = tmp_path / "new" / "subdir"
    assert not out_dir.exists()

    with patch("factory.core.payload_extract._resolve_payload_tool", return_value=None):
        mezo_extract_payload_partitions(payload, out_dir, ["system"])

    assert out_dir.is_dir()


# ── 2. Output images written to workspace only ────────────────────────────────

def test_stage_images_written_inside_workspace(tmp_path):
    """deadzone_payload_extract_stage places all images under ws.images."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.side_effect = _fake_tool_run(ws, DEFAULT_PARTITIONS)
        _seed_images(ws, ["system", "product", "vendor"])
        result = deadzone_payload_extract_stage(ws, payload_bin=payload)

    for name, img_path in result["extracted_images"].items():
        assert Path(img_path).is_relative_to(ws.root), (
            f"Image for {name!r} was written outside workspace: {img_path}"
        )


def test_stage_images_not_written_outside_workspace(tmp_path):
    """Extraction never writes images to a path outside ws.root."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)
    outside = tmp_path / "outside.img"

    _seed_images(ws, ["system", "product", "vendor"])

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        deadzone_payload_extract_stage(ws, payload_bin=payload)

    assert not outside.exists(), "A file was written outside the workspace"


# ── 3. Required partitions missing → clean RuntimeError ──────────────────────

def test_stage_fails_when_all_required_missing(tmp_path):
    """deadzone_payload_extract_stage raises RuntimeError when system/vendor/product absent."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        # No .img files created → all required missing
        with pytest.raises(RuntimeError, match="Required partition"):
            deadzone_payload_extract_stage(ws, payload_bin=payload)


def test_stage_fails_with_clear_message_naming_missing_partitions(tmp_path):
    """RuntimeError message names the specific missing required partitions."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)
    # Only system is created; vendor and product are missing
    _seed_images(ws, ["system"])

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        with pytest.raises(RuntimeError) as exc_info:
            deadzone_payload_extract_stage(ws, payload_bin=payload)

    msg = str(exc_info.value)
    # At least one missing required partition name must appear in the message
    assert any(name in msg for name in ("vendor", "product"))


def test_validation_separates_required_from_optional(tmp_path):
    """mezo_validate_extracted_payload_images puts missing partitions in right buckets."""
    out_dir = tmp_path / "images"
    out_dir.mkdir()
    # system present; vendor missing (required); odm missing (optional)
    (out_dir / "system.img").write_bytes(b"\x00" * 512)

    result = mezo_validate_extracted_payload_images(
        out_dir, ["system", "vendor", "odm"]
    )

    assert "vendor" in result["missing_required"]
    assert "odm" in result["missing_optional"]
    assert "system" in result["extracted_partitions"]
    assert "vendor" not in result["extracted_partitions"]


# ── 4. Optional partitions missing → reported only, no exception ──────────────

def test_stage_succeeds_when_only_optional_missing(tmp_path):
    """Stage succeeds (returns result) when only optional partitions are absent."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)
    # Required core present; optional absent
    _seed_images(ws, ["system", "product", "vendor"])

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        result = deadzone_payload_extract_stage(ws, payload_bin=payload)

    assert result["status"] == "OK"
    assert set(result["missing_optional"]) <= OPTIONAL_PARTITIONS
    assert result["missing_required"] == []


def test_stage_report_lists_missing_optional(tmp_path):
    """Report includes a non-empty missing optional section when partitions are absent."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)
    _seed_images(ws, ["system", "product", "vendor"])

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        result = deadzone_payload_extract_stage(ws, payload_bin=payload)

    report = (ws.reports / "deadzone_payload_extract_report.txt").read_text()
    assert "missing optional partitions" in report


# ── 5. Original ROM and payload.bin preserved ─────────────────────────────────

def test_original_rom_preserved_after_stage(tmp_path):
    """deadzone_payload_extract_stage never deletes or modifies the original ROM."""
    ws = _make_ws(tmp_path)

    # Place original ROM in ws.input (simulate post-intake state)
    rom_zip = ws.input / "original_rom.zip"
    with zipfile.ZipFile(rom_zip, "w") as zf:
        zf.writestr("system/build.prop", "ro.product.device=test\n")
    original_size = rom_zip.stat().st_size

    payload = _place_payload(ws)
    payload_original_size = payload.stat().st_size
    _seed_images(ws, ["system", "product", "vendor"])

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        deadzone_payload_extract_stage(ws, payload_bin=payload)

    assert rom_zip.is_file(), "Original ROM was deleted"
    assert rom_zip.stat().st_size == original_size, "Original ROM was modified"
    assert payload.is_file(), "payload.bin was deleted"
    assert payload.stat().st_size == payload_original_size, "payload.bin was modified"


def test_payload_bin_not_modified_during_extraction(tmp_path):
    """payload.bin bytes are unchanged after mezo_extract_payload_partitions runs."""
    payload = tmp_path / "payload.bin"
    payload_bytes = _fake_payload_bytes()
    payload.write_bytes(payload_bytes)
    out_dir = tmp_path / "out"

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        mezo_extract_payload_partitions(payload, out_dir, ["system"])

    assert payload.read_bytes() == payload_bytes, "payload.bin was modified"


# ── 6. Report is generated ────────────────────────────────────────────────────

def test_stage_generates_report_file(tmp_path):
    """deadzone_payload_extract_stage writes the report to ws.reports."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)
    _seed_images(ws, ["system", "product", "vendor"])

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        deadzone_payload_extract_stage(ws, payload_bin=payload)

    report = ws.reports / "deadzone_payload_extract_report.txt"
    assert report.is_file(), "Report file not generated"


def test_report_contains_required_sections(tmp_path):
    """Report includes all sections required by the Phase 3 spec."""
    ws = _make_ws(tmp_path)
    _seed_images(ws, ["system", "product", "vendor"])
    payload = _place_payload(ws)

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        deadzone_payload_extract_stage(ws, payload_bin=payload)

    content = (ws.reports / "deadzone_payload_extract_report.txt").read_text()
    for section in (
        "payload.bin path",
        "requested partitions",
        "extracted partitions",
        "missing optional partitions",
        "missing required partitions",
        "output image paths and sizes",
        "extraction status",
        "elapsed time",
    ):
        assert section in content, f"Report missing section: {section!r}"


def test_write_report_directly(tmp_path):
    """deadzone_write_payload_extract_report writes the report independently."""
    ws = _make_ws(tmp_path)
    report_path = deadzone_write_payload_extract_report(
        ws,
        payload_path="/some/payload.bin",
        requested_partitions=["system", "vendor", "product"],
        extracted_partitions=["system", "vendor", "product"],
        missing_optional=["odm", "mi_ext"],
        missing_required=[],
        extracted_images={
            "system": str(ws.images / "system.img"),
            "vendor": str(ws.images / "vendor.img"),
            "product": str(ws.images / "product.img"),
        },
        image_sizes={"system": 1024, "vendor": 512, "product": 256},
        extraction_status="OK",
        elapsed_seconds=3.14,
        error="",
    )
    assert report_path.is_file()
    content = report_path.read_text()
    assert "OK" in content
    assert "odm" in content
    assert "3.14s" in content


# ── 7. JSON metadata is generated ────────────────────────────────────────────

def test_stage_generates_payload_extract_json(tmp_path):
    """deadzone_payload_extract_stage writes payload_extract.json to ws.meta."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)
    _seed_images(ws, ["system", "product", "vendor"])

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        deadzone_payload_extract_stage(ws, payload_bin=payload)

    meta_file = ws.meta / "payload_extract.json"
    assert meta_file.is_file(), "payload_extract.json not generated"


def test_json_metadata_contains_required_keys(tmp_path):
    """payload_extract.json contains all required top-level keys."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)
    _seed_images(ws, ["system", "product", "vendor"])

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        deadzone_payload_extract_stage(ws, payload_bin=payload)

    data = json.loads((ws.meta / "payload_extract.json").read_text())
    for key in (
        "payload_path",
        "requested_partitions",
        "extracted_images",
        "missing_partitions",
        "failed_partitions",
        "status",
    ):
        assert key in data, f"payload_extract.json missing key: {key!r}"


def test_json_metadata_status_ok_when_core_present(tmp_path):
    """payload_extract.json status is 'OK' when all required partitions are extracted."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)
    _seed_images(ws, ["system", "product", "vendor"])

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        deadzone_payload_extract_stage(ws, payload_bin=payload)

    data = json.loads((ws.meta / "payload_extract.json").read_text())
    assert data["status"] == "OK"


def test_json_metadata_status_failed_when_required_missing(tmp_path):
    """payload_extract.json status is 'FAILED' when required partitions are absent."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)
    # No .img files — all required missing

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        with pytest.raises(RuntimeError):
            deadzone_payload_extract_stage(ws, payload_bin=payload)

    data = json.loads((ws.meta / "payload_extract.json").read_text())
    assert data["status"] == "FAILED"
    assert len(data["failed_partitions"]) > 0


# ── 8. Naming convention — payload_extract module ────────────────────────────

def test_payload_extract_module_naming_convention():
    """All public functions in payload_extract.py must use mezo_* or deadzone_* prefix."""
    path = Path("factory/core/payload_extract.py")
    assert path.is_file(), f"payload_extract.py not found at {path}"
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
        "Public functions must use mezo_* or deadzone_* prefix.\n"
        "Violations: " + ", ".join(violations)
    )


# ── 9. No mod/smali functions called ─────────────────────────────────────────

_MOD_KEYWORDS = frozenset({
    "smali", "baksmali", "apktool", "mod_", "_mod",
    "MiuiSystemUI", "Provision", "Wukong", "USAGI_UI",
    "flag_secure", "spoof", "signature_bypass",
    "framework_jar", "services_jar",
    "style_runner", "apply_style",
})


def test_payload_extract_has_no_mod_imports():
    """payload_extract.py must not import or reference any mod/smali symbols."""
    path = Path("factory/core/payload_extract.py")
    source = path.read_text(encoding="utf-8").lower()
    for keyword in _MOD_KEYWORDS:
        assert keyword.lower() not in source, (
            f"payload_extract.py references a forbidden mod symbol: {keyword!r}"
        )


def test_payload_extract_no_hyperur_import():
    """payload_extract.py must not import HyperURBuild or any HyperUR src module."""
    path = Path("factory/core/payload_extract.py")
    source = path.read_text(encoding="utf-8")
    assert "HyperURBuild" not in source
    assert "from src." not in source
    assert "import src." not in source


# ── Standalone callable ───────────────────────────────────────────────────────

def test_stage_callable_standalone_without_pipeline(tmp_path):
    """deadzone_payload_extract_stage can be called standalone without running full pipeline."""
    ws = _make_ws(tmp_path)
    payload = _place_payload(ws)
    _seed_images(ws, ["system", "product", "vendor"])

    with patch("factory.core.payload_extract._resolve_payload_tool") as mock_tool, \
         patch("factory.core.payload_extract.subprocess.run") as mock_run:
        mock_tool.return_value = Path("/fake/tool")
        mock_run.return_value = MagicMock(returncode=0, stderr="")
        result = deadzone_payload_extract_stage(ws, payload_bin=payload)

    assert result["status"] == "OK"
    assert (ws.meta / "payload_extract.json").is_file()
    assert (ws.reports / "deadzone_payload_extract_report.txt").is_file()


def test_stage_raises_when_no_payload_bin_in_workspace(tmp_path):
    """deadzone_payload_extract_stage raises FileNotFoundError when payload.bin is absent."""
    ws = _make_ws(tmp_path)
    # Don't create payload.bin

    with pytest.raises(FileNotFoundError, match="payload.bin"):
        deadzone_payload_extract_stage(ws)


# ── mezo_select_default_payload_partitions unit tests ────────────────────────

def test_select_returns_intersection_in_requested_order():
    """mezo_select_default_payload_partitions returns only partitions present in manifest."""
    available = ["system", "vendor", "product", "odm"]
    requested = ["system", "product", "mi_ext", "vendor"]
    result = mezo_select_default_payload_partitions(available, requested)
    assert result == ["system", "product", "vendor"]


def test_select_returns_empty_when_no_overlap():
    """mezo_select_default_payload_partitions returns [] when nothing overlaps."""
    result = mezo_select_default_payload_partitions(["boot", "dtbo"], DEFAULT_PARTITIONS)
    assert result == []


def test_select_returns_all_when_fully_available():
    """mezo_select_default_payload_partitions returns all requested when all available."""
    result = mezo_select_default_payload_partitions(DEFAULT_PARTITIONS, DEFAULT_PARTITIONS)
    assert result == DEFAULT_PARTITIONS


# ── mezo_validate_extracted_payload_images unit tests ─────────────────────────

def test_validate_accepts_slot_suffixed_images(tmp_path):
    """Validation accepts system_a.img as a match for the 'system' partition."""
    out_dir = tmp_path / "images"
    out_dir.mkdir()
    (out_dir / "system_a.img").write_bytes(b"\x00" * 512)

    result = mezo_validate_extracted_payload_images(out_dir, ["system"])
    assert "system" in result["extracted_partitions"]


def test_validate_zero_byte_image_is_not_counted(tmp_path):
    """A zero-byte .img file is treated as missing."""
    out_dir = tmp_path / "images"
    out_dir.mkdir()
    (out_dir / "system.img").write_bytes(b"")

    result = mezo_validate_extracted_payload_images(out_dir, ["system"])
    assert "system" not in result["extracted_partitions"]
    assert "system" in result["missing_required"]
