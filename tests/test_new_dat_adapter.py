"""
Tests for factory/adapters/new_dat.py — new_dat adapter hardening (Task 2).

Covers:
 1.  detect_new_dat_partitions finds *.new.dat.br
 2.  detect returns None transfer when absent
 3.  detect returns Path transfer when present
 4.  detect returns empty list when no .br files
 5.  missing transfer.list raises clearly
 6.  parse_dynamic_partitions_op_list returns partition names
 7.  parse_dynamic_partitions_op_list ignores comments and add_group lines
 8.  parse_dynamic_partitions_op_list returns [] for absent file
 9.  successful fake conversion writes ws.images/system.img
10.  report TXT is written with CONVERTED status
11.  report JSON is written with correct keys
12.  missing brotli gives clear error (mentions 'brotli')
13.  missing sdat2img gives clear error (mentions 'sdat2img')
14.  smart_unpack selects ROUTE_NEW_DAT for folder with *.new.dat.br
15.  payload.bin priority remains ROUTE_PAYLOAD when both exist
16.  op_list skipped partitions appear in JSON report
17.  tmp files go inside ws; original .br is untouched
18.  smart_unpack result includes new_dat report in sub_reports
"""
from __future__ import annotations

import json
import struct
from pathlib import Path
from unittest.mock import patch

import pytest

from factory.adapters.new_dat import (
    adapt,
    detect_new_dat_partitions,
    parse_dynamic_partitions_op_list,
    resolve_brotli_tool,
    resolve_sdat2img_tool,
)
from factory.core.smart_unpack import (
    ROUTE_NEW_DAT,
    ROUTE_PAYLOAD,
    mezo_detect_rom_input_type,
    mezo_plan_unpack_route,
)
from factory.core.workspace import create_workspace


# ── Shared helpers ─────────────────────────────────────────────────────────────

def _make_ws(tmp_path: Path):
    return create_workspace(tmp_path / "workspace")


def _fake_br(folder: Path, part: str, *, with_transfer: bool = True) -> Path:
    br = folder / f"{part}.new.dat.br"
    br.write_bytes(b"fake_br_content")
    if with_transfer:
        tl = folder / f"{part}.transfer.list"
        tl.write_text("4\n0\n0\n1 0\n", encoding="utf-8")
    return br


def _brotli_ok() -> dict:
    return {"method": "module", "available": True, "detail": "mock", "error": ""}


def _sdat2img_ok() -> dict:
    return {"method": "mezo_core", "available": True, "detail": "mock", "error": ""}


def _fake_decompress(br_path: Path, out_path: Path, tool: dict) -> None:
    out_path.write_bytes(b"decompressed_content")


def _fake_sdat2img(transfer: Path, new_dat: Path, out_img: Path, tool: dict) -> None:
    out_img.write_bytes(b"fake_img_data" + b"\x00" * 512)


def _fake_payload_bytes() -> bytes:
    manifest = b"\x00" * 4
    sig_len = 4
    header = struct.pack(">4sQQI", b"CrAU", 2, len(manifest), sig_len)
    return header + manifest + b"\x00" * sig_len


# ── 1. detect_new_dat_partitions finds *.new.dat.br ───────────────────────────

def test_detect_finds_br_files(tmp_path):
    _fake_br(tmp_path, "system")
    _fake_br(tmp_path, "vendor")
    results = detect_new_dat_partitions(tmp_path)
    names = [p for p, _, _ in results]
    assert "system" in names
    assert "vendor" in names


# ── 2. detect returns None transfer when absent ───────────────────────────────

def test_detect_returns_none_transfer_when_absent(tmp_path):
    _fake_br(tmp_path, "system", with_transfer=False)
    results = detect_new_dat_partitions(tmp_path)
    assert len(results) == 1
    part, br, transfer = results[0]
    assert part == "system"
    assert transfer is None


# ── 3. detect returns Path transfer when present ──────────────────────────────

def test_detect_returns_transfer_path_when_present(tmp_path):
    _fake_br(tmp_path, "system", with_transfer=True)
    results = detect_new_dat_partitions(tmp_path)
    part, br, transfer = results[0]
    assert transfer is not None
    assert transfer.name == "system.transfer.list"
    assert transfer.is_file()


# ── 4. detect returns empty list when no .br files ───────────────────────────

def test_detect_empty_when_no_br(tmp_path):
    assert detect_new_dat_partitions(tmp_path) == []


# ── 5. missing transfer.list raises clearly ───────────────────────────────────

def test_missing_transfer_list_raises_clearly(tmp_path):
    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom"
    folder.mkdir()
    _fake_br(folder, "system", with_transfer=False)

    with patch("factory.adapters.new_dat.resolve_brotli_tool", return_value=_brotli_ok()), \
         patch("factory.adapters.new_dat.resolve_sdat2img_tool", return_value=_sdat2img_ok()):
        with pytest.raises(RuntimeError, match="missing transfer"):
            adapt(folder, ws)


# ── 6. parse_dynamic_partitions_op_list returns partition names ───────────────

def test_parse_op_list_returns_partition_names(tmp_path):
    op_list = tmp_path / "dynamic_partitions_op_list"
    op_list.write_text(
        "# comment\n"
        "remove_group qti_dynamic_partitions_a\n"
        "add_group qti_dynamic_partitions_a 9663676416\n"
        "add system_a qti_dynamic_partitions_a\n"
        "add vendor_a qti_dynamic_partitions_a\n"
        "add product_a qti_dynamic_partitions_a\n",
        encoding="utf-8",
    )
    parts = parse_dynamic_partitions_op_list(op_list)
    assert "system_a" in parts
    assert "vendor_a" in parts
    assert "product_a" in parts


# ── 7. parse ignores comments and add_group lines ────────────────────────────

def test_parse_op_list_ignores_comments_and_add_group(tmp_path):
    op_list = tmp_path / "dynamic_partitions_op_list"
    op_list.write_text(
        "# this is a comment\n"
        "add_group some_group 1234\n"
        "add system_a grp\n",
        encoding="utf-8",
    )
    parts = parse_dynamic_partitions_op_list(op_list)
    assert parts == ["system_a"]
    assert not any("group" in p for p in parts)


# ── 8. parse returns [] for absent file ───────────────────────────────────────

def test_parse_op_list_missing_file_returns_empty(tmp_path):
    assert parse_dynamic_partitions_op_list(tmp_path / "nonexistent") == []


# ── 9. successful fake conversion writes ws.images/system.img ─────────────────

def test_successful_conversion_writes_img(tmp_path):
    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom"
    folder.mkdir()
    _fake_br(folder, "system")

    with patch("factory.adapters.new_dat.resolve_brotli_tool", return_value=_brotli_ok()), \
         patch("factory.adapters.new_dat.resolve_sdat2img_tool", return_value=_sdat2img_ok()), \
         patch("factory.adapters.new_dat._decompress_brotli", side_effect=_fake_decompress), \
         patch("factory.adapters.new_dat._run_sdat2img", side_effect=_fake_sdat2img):
        result = adapt(folder, ws)

    assert "system.img" in result["images"]
    assert (ws.images / "system.img").is_file()
    assert (ws.images / "system.img").stat().st_size > 0


# ── 10. report TXT is written with CONVERTED status ───────────────────────────

def test_report_txt_is_written(tmp_path):
    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom"
    folder.mkdir()
    _fake_br(folder, "system")

    with patch("factory.adapters.new_dat.resolve_brotli_tool", return_value=_brotli_ok()), \
         patch("factory.adapters.new_dat.resolve_sdat2img_tool", return_value=_sdat2img_ok()), \
         patch("factory.adapters.new_dat._decompress_brotli", side_effect=_fake_decompress), \
         patch("factory.adapters.new_dat._run_sdat2img", side_effect=_fake_sdat2img):
        adapt(folder, ws)

    report = ws.reports / "new_dat_adapter_report.txt"
    assert report.is_file()
    content = report.read_text()
    assert "system" in content
    assert "CONVERTED" in content
    assert "source_dir" in content
    assert "brotli_tool" in content
    assert "sdat2img_tool" in content


# ── 11. report JSON is written with correct keys ──────────────────────────────

def test_report_json_is_written(tmp_path):
    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom"
    folder.mkdir()
    _fake_br(folder, "system")

    with patch("factory.adapters.new_dat.resolve_brotli_tool", return_value=_brotli_ok()), \
         patch("factory.adapters.new_dat.resolve_sdat2img_tool", return_value=_sdat2img_ok()), \
         patch("factory.adapters.new_dat._decompress_brotli", side_effect=_fake_decompress), \
         patch("factory.adapters.new_dat._run_sdat2img", side_effect=_fake_sdat2img):
        adapt(folder, ws)

    json_path = ws.meta / "new_dat_adapter.json"
    assert json_path.is_file()
    data = json.loads(json_path.read_text())
    for key in ("source_dir", "brotli_tool", "sdat2img_tool", "detected_partitions",
                "op_list_partitions", "partitions", "converted_count", "skipped_count",
                "failed_count"):
        assert key in data, f"new_dat_adapter.json missing key: {key!r}"
    assert data["converted_count"] == 1
    assert data["skipped_count"] == 0
    assert data["failed_count"] == 0


# ── 12. missing brotli gives clear error ──────────────────────────────────────

def test_missing_brotli_gives_clear_error(tmp_path):
    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom"
    folder.mkdir()
    _fake_br(folder, "system")

    no_brotli = {
        "method": "none", "available": False, "detail": "",
        "error": "brotli decompressor not found. Install the Python brotli module ('pip install brotli') or place the brotli CLI in PATH.",
    }
    with patch("factory.adapters.new_dat.resolve_brotli_tool", return_value=no_brotli), \
         patch("factory.adapters.new_dat.resolve_sdat2img_tool", return_value=_sdat2img_ok()):
        with pytest.raises(RuntimeError) as exc_info:
            adapt(folder, ws)
    assert "brotli" in str(exc_info.value).lower()


# ── 13. missing sdat2img gives clear error ────────────────────────────────────

def test_missing_sdat2img_gives_clear_error(tmp_path):
    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom"
    folder.mkdir()
    _fake_br(folder, "system")

    no_sdat2img = {
        "method": "none", "available": False, "detail": "",
        "error": "sdat2img not found. Ensure third_party/mezo_core contains src/core/utils.py with Sdat2img, or install the sdat2img CLI in PATH.",
    }
    with patch("factory.adapters.new_dat.resolve_brotli_tool", return_value=_brotli_ok()), \
         patch("factory.adapters.new_dat.resolve_sdat2img_tool", return_value=no_sdat2img):
        with pytest.raises(RuntimeError) as exc_info:
            adapt(folder, ws)
    assert "sdat2img" in str(exc_info.value).lower()


# ── 14. smart_unpack selects ROUTE_NEW_DAT for folder with *.new.dat.br ───────

def test_smart_unpack_selects_new_dat_route(tmp_path):
    folder = tmp_path / "rom_folder"
    folder.mkdir()
    (folder / "system.new.dat.br").write_bytes(b"fake")
    (folder / "system.transfer.list").write_text("4\n0\n0\n1 0\n", encoding="utf-8")

    input_type = mezo_detect_rom_input_type(folder)
    route, reason = mezo_plan_unpack_route(folder, input_type)
    assert route == ROUTE_NEW_DAT
    assert "new.dat.br" in reason


# ── 15. payload.bin priority over new_dat ────────────────────────────────────

def test_payload_priority_over_new_dat(tmp_path):
    folder = tmp_path / "rom_folder"
    folder.mkdir()
    (folder / "payload.bin").write_bytes(_fake_payload_bytes())
    (folder / "system.new.dat.br").write_bytes(b"fake")

    input_type = mezo_detect_rom_input_type(folder)
    route, reason = mezo_plan_unpack_route(folder, input_type)
    assert route == ROUTE_PAYLOAD
    assert "payload.bin" in reason


# ── 16. op_list skipped partitions appear in JSON report ──────────────────────

def test_op_list_skipped_partitions_in_report(tmp_path):
    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom"
    folder.mkdir()
    _fake_br(folder, "system")
    op = folder / "dynamic_partitions_op_list"
    op.write_text("add system_a grp\nadd odm_a grp\n", encoding="utf-8")

    with patch("factory.adapters.new_dat.resolve_brotli_tool", return_value=_brotli_ok()), \
         patch("factory.adapters.new_dat.resolve_sdat2img_tool", return_value=_sdat2img_ok()), \
         patch("factory.adapters.new_dat._decompress_brotli", side_effect=_fake_decompress), \
         patch("factory.adapters.new_dat._run_sdat2img", side_effect=_fake_sdat2img):
        adapt(folder, ws)

    data = json.loads((ws.meta / "new_dat_adapter.json").read_text())
    skipped = [e for e in data["partitions"] if e["status"] == "SKIPPED"]
    assert len(skipped) >= 1
    skipped_names = [e["partition"] for e in skipped]
    assert "odm_a" in skipped_names
    assert data["skipped_count"] >= 1


# ── 17. tmp files inside ws; original .br untouched ──────────────────────────

def test_tmp_files_inside_workspace_original_untouched(tmp_path):
    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom"
    folder.mkdir()
    br = _fake_br(folder, "system")
    original_bytes = br.read_bytes()

    with patch("factory.adapters.new_dat.resolve_brotli_tool", return_value=_brotli_ok()), \
         patch("factory.adapters.new_dat.resolve_sdat2img_tool", return_value=_sdat2img_ok()), \
         patch("factory.adapters.new_dat._decompress_brotli", side_effect=_fake_decompress), \
         patch("factory.adapters.new_dat._run_sdat2img", side_effect=_fake_sdat2img):
        adapt(folder, ws)

    assert br.read_bytes() == original_bytes, "original .br was modified"
    tmp_new_dat = ws.partitions / "_new_dat_tmp" / "system.new.dat"
    assert tmp_new_dat.is_file(), "tmp .new.dat not written inside ws"
    assert str(ws.partitions) in str(tmp_new_dat), "tmp file escaped workspace"


# ── 18. smart_unpack result includes new_dat report in sub_reports ────────────

def test_smart_unpack_route_new_dat_includes_report_in_sub_reports(tmp_path):
    from factory.core.smart_unpack import deadzone_smart_unpack

    ws = _make_ws(tmp_path)
    folder = tmp_path / "rom"
    folder.mkdir()
    _fake_br(folder, "system")

    def _fake_adapt(source_dir, ws_arg):
        (ws_arg.images / "system.img").write_bytes(b"\x00" * 512)
        txt = ws_arg.reports / "new_dat_adapter_report.txt"
        txt.write_text("report", encoding="utf-8")
        meta = ws_arg.meta / "new_dat_adapter.json"
        meta.write_text("{}", encoding="utf-8")
        return {
            "adapter": "new_dat",
            "images": ["system.img"],
            "report_path": str(txt),
            "meta_path": str(meta),
        }

    with patch("factory.adapters.new_dat.adapt", side_effect=_fake_adapt):
        result = deadzone_smart_unpack(folder, ws)

    assert result["route"] == ROUTE_NEW_DAT
    report_paths = result.get("reports", [])
    assert any("new_dat_adapter_report" in r for r in report_paths)
