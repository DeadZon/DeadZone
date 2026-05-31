"""
Tests for factory/core/repacker.py — real partition repack engine.

Modification is driven by ws.meta/partition_modifications.json, NOT by the mere
presence of an extracted partition tree.  Tool-invocation tests (EROFS actual
rebuild) use a cross-platform fake mkfs.erofs (tests/fake_bin.py) so they run on
every platform.
"""
from __future__ import annotations

import os
from pathlib import Path

import pytest

from factory.core.partition_modifications import (
    is_partition_modified,
    mark_partition_modified,
)
from factory.core.repacker import (
    PartitionRepackError,
    _detect_erofs_compression,
    _find_ext4_tool,
    _rebuild_erofs,
    _rebuild_ext4,
    _tree_is_non_empty,
    repack_partitions,
)
from factory.core.workspace import create_workspace
from tests.fake_bin import write_fake_mkfs_erofs


# ── helpers ───────────────────────────────────────────────────────────────────

def _erofs_header() -> bytes:
    return b"\x00" * 1024 + b"EroS" + b"\x00" * 1024


def _ext4_header() -> bytes:
    buf = bytearray(2048)
    buf[0x438] = 0x53
    buf[0x439] = 0xEF
    return bytes(buf)


def _make_tree(tree: Path, filename: str = "file.txt", content: str = "hello") -> None:
    tree.mkdir(parents=True, exist_ok=True)
    (tree / filename).write_text(content, encoding="utf-8")


# ── _tree_is_non_empty ────────────────────────────────────────────────────────

def test_non_empty_tree_detected(tmp_path):
    tree = tmp_path / "vendor"
    _make_tree(tree)
    assert _tree_is_non_empty(tree) is True


def test_missing_tree_is_not_modified(tmp_path):
    assert _tree_is_non_empty(tmp_path / "vendor") is False


def test_empty_tree_is_not_modified(tmp_path):
    tree = tmp_path / "vendor"
    tree.mkdir()
    assert _tree_is_non_empty(tree) is False


# ── filesystem type detection ─────────────────────────────────────────────────

def test_erofs_fs_type_detected_from_image(tmp_path):
    from factory.core.image_extractor import _detect_format
    img = tmp_path / "vendor.img"
    img.write_bytes(_erofs_header())
    fmt, _ = _detect_format(img, None)
    assert fmt == "raw_erofs"


def test_ext4_fs_type_detected_from_image(tmp_path):
    from factory.core.image_extractor import _detect_format
    img = tmp_path / "system.img"
    img.write_bytes(_ext4_header())
    fmt, _ = _detect_format(img, None)
    assert fmt == "raw_ext4"


def test_erofs_compression_detection(tmp_path):
    img = tmp_path / "vendor.img"
    img.write_bytes(b"\x00" * 512 + b"lz4hc" + b"\x00" * 512)
    assert _detect_erofs_compression(img) == "lz4hc"


def test_erofs_compression_detection_unknown(tmp_path):
    img = tmp_path / "vendor.img"
    img.write_bytes(b"\x00" * 1024)
    assert _detect_erofs_compression(img) == "unknown"


# ── unmodified partition is staged / skipped ──────────────────────────────────

def test_unmodified_partition_with_image_is_copied(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(_erofs_header())
    result = repack_partitions(ws)
    vendor_entry = next(e for e in result["partitions"] if e["partition"] == "vendor")
    assert vendor_entry["status"] == "copied"
    assert vendor_entry["modified"] is False


def test_partition_with_no_image_and_no_tree_is_skipped(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    result = repack_partitions(ws)
    odm_entry = next(e for e in result["partitions"] if e["partition"] == "odm")
    assert odm_entry["status"] == "skipped"


def test_unmodified_partitions_do_not_raise(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "system.img").write_bytes(_ext4_header())
    result = repack_partitions(ws)
    assert result["status"] == "ok"
    assert result["failed_partitions"] == []


# ── EROFS route selection and tool-missing failure ───────────────────────────

def test_erofs_route_selected_when_image_is_erofs(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(_erofs_header())
    _make_tree(ws.partitions / "vendor")
    mark_partition_modified(ws, "vendor", "test modification")
    monkeypatch.setenv("PATH", "")  # no mkfs.erofs available

    with pytest.raises(PartitionRepackError) as exc:
        repack_partitions(ws)

    assert exc.value.payload["error_type"] == "PARTITION_REPACK_FAILED"
    assert "vendor" in exc.value.payload["failed_partitions"]


def test_erofs_missing_tool_records_clear_reason(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "product.img").write_bytes(_erofs_header())
    _make_tree(ws.partitions / "product")
    mark_partition_modified(ws, "product", "test modification")
    monkeypatch.setenv("PATH", "")

    with pytest.raises(PartitionRepackError):
        repack_partitions(ws)

    entry = next(
        e for e in (
            __import__("json").loads(
                (ws.meta / "partition_repack.json").read_text(encoding="utf-8")
            )["partitions"]
        )
        if e["partition"] == "product"
    )
    assert "mkfs.erofs" in entry["reason"]


# ── EXT4 route selection and tool-missing failure ────────────────────────────

def test_ext4_route_selected_when_image_is_ext4(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "system_ext.img").write_bytes(_ext4_header())
    _make_tree(ws.partitions / "system_ext")
    mark_partition_modified(ws, "system_ext", "test modification")
    monkeypatch.setattr(
        "factory.core.repacker._find_ext4_tool", lambda: None
    )

    with pytest.raises(PartitionRepackError) as exc:
        repack_partitions(ws)

    assert "system_ext" in exc.value.payload["failed_partitions"]


def test_ext4_missing_tool_records_clear_reason(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "system.img").write_bytes(_ext4_header())
    _make_tree(ws.partitions / "system")
    mark_partition_modified(ws, "system", "test modification")
    monkeypatch.setattr("factory.core.repacker._find_ext4_tool", lambda: None)

    with pytest.raises(PartitionRepackError):
        repack_partitions(ws)

    data = __import__("json").loads(
        (ws.meta / "partition_repack.json").read_text(encoding="utf-8")
    )
    entry = next(e for e in data["partitions"] if e["partition"] == "system")
    assert "EXT4" in entry["reason"] or "ext4" in entry["reason"].lower() or "tool" in entry["reason"].lower()


# ── failed rebuild blocks super build ────────────────────────────────────────

def test_failed_modified_partition_raises_partition_repack_error(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(_erofs_header())
    _make_tree(ws.partitions / "vendor")
    mark_partition_modified(ws, "vendor", "test modification")
    monkeypatch.setenv("PATH", "")

    with pytest.raises(PartitionRepackError) as exc:
        repack_partitions(ws)

    assert exc.value.payload["error_type"] == "PARTITION_REPACK_FAILED"
    assert "vendor" in exc.value.payload["failed_partitions"]
    # Error contains a suggested fix
    assert "suggested_fix" in exc.value.payload


def test_only_failed_partition_is_in_failed_list(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    # vendor: modified + erofs, will fail (no tool)
    (ws.images / "vendor.img").write_bytes(_erofs_header())
    _make_tree(ws.partitions / "vendor")
    mark_partition_modified(ws, "vendor", "test modification")
    # system: unmodified, will pass (copied)
    (ws.images / "system.img").write_bytes(_ext4_header())
    monkeypatch.setenv("PATH", "")

    with pytest.raises(PartitionRepackError) as exc:
        repack_partitions(ws)

    assert exc.value.payload["failed_partitions"] == ["vendor"]


def test_extracted_but_unmodified_partition_is_not_rebuilt(tmp_path, monkeypatch):
    """A populated tree with NO modification mark must NOT trigger a rebuild."""
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(_erofs_header())
    _make_tree(ws.partitions / "vendor")  # extracted but not marked modified
    monkeypatch.setenv("PATH", "")  # no mkfs.erofs — would fail IF it tried

    result = repack_partitions(ws)  # must not raise

    vendor = next(e for e in result["partitions"] if e["partition"] == "vendor")
    assert vendor["modified"] is False
    assert vendor["status"] == "copied"
    # original image is left untouched
    assert (ws.images / "vendor.img").read_bytes() == _erofs_header()


def test_modified_partition_with_empty_tree_fails(tmp_path):
    """Marked modified but nothing extracted to rebuild from → clean failure."""
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(_erofs_header())
    mark_partition_modified(ws, "vendor", "marked but no tree")

    with pytest.raises(PartitionRepackError) as exc:
        repack_partitions(ws)

    assert "vendor" in exc.value.payload["failed_partitions"]
    data = __import__("json").loads(
        (ws.meta / "partition_repack.json").read_text(encoding="utf-8")
    )
    entry = next(e for e in data["partitions"] if e["partition"] == "vendor")
    assert "no extracted tree" in entry["reason"]


# ── report files are written ──────────────────────────────────────────────────

def test_partition_repack_json_written_on_success(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "system.img").write_bytes(_ext4_header())
    repack_partitions(ws)
    assert (ws.meta / "partition_repack.json").is_file()


def test_partition_repack_report_txt_written_on_success(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(_erofs_header())
    repack_partitions(ws)
    assert (ws.reports / "partition_repack_report.txt").is_file()


def test_partition_repack_json_written_on_failure(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(_erofs_header())
    _make_tree(ws.partitions / "vendor")
    mark_partition_modified(ws, "vendor", "test modification")
    monkeypatch.setenv("PATH", "")

    with pytest.raises(PartitionRepackError):
        repack_partitions(ws)

    assert (ws.meta / "partition_repack.json").is_file()


def test_partition_repack_report_txt_written_on_failure(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(_erofs_header())
    _make_tree(ws.partitions / "vendor")
    mark_partition_modified(ws, "vendor", "test modification")
    monkeypatch.setenv("PATH", "")

    with pytest.raises(PartitionRepackError):
        repack_partitions(ws)

    report = ws.reports / "partition_repack_report.txt"
    assert report.is_file()
    content = report.read_text(encoding="utf-8")
    assert "vendor" in content
    assert "failed" in content


def test_partition_repack_json_contains_required_fields(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "system.img").write_bytes(_ext4_header())
    repack_partitions(ws)

    import json
    data = json.loads((ws.meta / "partition_repack.json").read_text(encoding="utf-8"))
    assert "status" in data
    assert "partitions" in data
    assert "failed_partitions" in data
    entry = next(e for e in data["partitions"] if e["partition"] == "system")
    for field in (
        "partition", "original_image", "workspace_folder",
        "filesystem_type", "modified", "original_size",
        "rebuilt_size", "command", "status",
    ):
        assert field in entry, f"missing field: {field}"


# ── EROFS rebuild with cross-platform fake tool ───────────────────────────────

def test_erofs_rebuild_succeeds_with_fake_mkfs(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "product.img").write_bytes(_erofs_header())
    _make_tree(ws.partitions / "product")
    mark_partition_modified(ws, "product", "test modification")

    helper = tmp_path / "bin"
    write_fake_mkfs_erofs(helper, content=b"rebuilt")
    monkeypatch.setenv("PATH", str(helper))

    result = repack_partitions(ws)
    entry = next(e for e in result["partitions"] if e["partition"] == "product")
    assert entry["status"] == "rebuilt"
    assert entry["modified"] is True
    assert entry["filesystem_type"] == "raw_erofs"


def test_erofs_rebuilt_image_replaces_original(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    original_content = _erofs_header()
    (ws.images / "vendor.img").write_bytes(original_content)
    _make_tree(ws.partitions / "vendor")
    mark_partition_modified(ws, "vendor", "test modification")

    helper = tmp_path / "bin"
    write_fake_mkfs_erofs(helper, content=b"rebuilt_content")
    monkeypatch.setenv("PATH", str(helper))

    repack_partitions(ws)
    assert (ws.images / "vendor.img").read_bytes() == b"rebuilt_content"


def test_erofs_failed_tool_raises(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(_erofs_header())
    _make_tree(ws.partitions / "vendor")
    mark_partition_modified(ws, "vendor", "test modification")

    helper = tmp_path / "bin"
    write_fake_mkfs_erofs(helper, fail=True)
    monkeypatch.setenv("PATH", str(helper))

    with pytest.raises(PartitionRepackError) as exc:
        repack_partitions(ws)

    assert "vendor" in exc.value.payload["failed_partitions"]
