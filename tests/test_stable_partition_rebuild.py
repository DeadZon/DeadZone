from __future__ import annotations

import os
from pathlib import Path

import pytest

from factory.core.stable_partition_rebuild import StablePartitionRebuildError, rebuild_stable_partitions
from factory.core.workspace import create_workspace
from tests.fake_bin import write_fake_mkfs_erofs


def test_no_changed_partitions_writes_ok_report(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    result = rebuild_stable_partitions(ws, {"changed_partitions": []})
    assert result["status"] == "ok"
    assert (ws.reports / "stable_partition_rebuild_report.json").is_file()


def test_changed_erofs_partition_requires_mkfs_erofs(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.partitions / "product").mkdir(parents=True)
    image = ws.images / "product.img"
    image.write_bytes(b"\0" * 1024 + b"EroS" + b"\0" * 1024)
    monkeypatch.setenv("PATH", "")
    with pytest.raises(StablePartitionRebuildError) as exc:
        rebuild_stable_partitions(ws, {"changed_partitions": ["product"]})
    assert exc.value.payload["error_type"] == "PARTITION_REBUILD_TOOL_MISSING"


def test_changed_ext4_partition_fails_not_implemented(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    (ws.partitions / "system_ext").mkdir(parents=True)
    header = bytearray(2048)
    header[0x438:0x43A] = b"\x53\xef"
    (ws.images / "system_ext.img").write_bytes(bytes(header))
    with pytest.raises(StablePartitionRebuildError) as exc:
        rebuild_stable_partitions(ws, {"changed_partitions": ["system_ext"]})
    assert exc.value.payload["error_type"] == "EXT_PARTITION_REBUILD_NOT_IMPLEMENTED"


def test_erofs_rebuild_report_contains_sizes(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    tree = ws.partitions / "product"
    tree.mkdir(parents=True)
    (tree / "file.txt").write_text("x", encoding="utf-8")
    image = ws.images / "product.img"
    image.write_bytes(b"\0" * 1024 + b"EroS" + b"\0" * 4096)
    helper = tmp_path / "bin"
    write_fake_mkfs_erofs(helper, content=b"rebuilt")
    monkeypatch.setenv("PATH", str(helper))
    result = rebuild_stable_partitions(ws, {"changed_partitions": ["product"]})
    entry = result["partitions"][0]
    assert entry["status"] == "rebuilt"
    assert entry["size_before"] > entry["size_after"]
    assert entry["bytes_saved"] > 0


def _write_fake_mkfs(helper: Path, payload_size: int) -> None:
    write_fake_mkfs_erofs(helper, size=payload_size, content=None)


def test_rebuilt_image_growth_more_than_tolerance_fails(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.partitions / "vendor").mkdir(parents=True)
    (ws.images / "vendor.img").write_bytes(b"\0" * 1024 + b"EroS" + b"\0" * 1024)
    helper = tmp_path / "bin"
    _write_fake_mkfs(helper, 40 * 1024 * 1024)
    monkeypatch.setenv("PATH", f"{helper}{os.pathsep}{os.environ.get('PATH', '')}")

    with pytest.raises(StablePartitionRebuildError) as exc:
        rebuild_stable_partitions(ws, {"changed_partitions": ["vendor"]})

    assert exc.value.payload["error_type"] == "REBUILT_IMAGE_TOO_LARGE"
    assert "vendor.img grew" in exc.value.payload["cause"]


def test_rebuilt_image_growth_within_tolerance_passes(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.partitions / "vendor").mkdir(parents=True)
    (ws.images / "vendor.img").write_bytes(b"\0" * 1024 + b"EroS" + b"\0" * (2 * 1024 * 1024))
    helper = tmp_path / "bin"
    _write_fake_mkfs(helper, 3 * 1024 * 1024)
    monkeypatch.setenv("PATH", f"{helper}{os.pathsep}{os.environ.get('PATH', '')}")

    result = rebuild_stable_partitions(ws, {"changed_partitions": ["vendor"]})

    assert result["partitions"][0]["validation_status"] == "passed"
    assert result["partitions"][0]["size_delta"] > 0


def test_allow_rebuilt_image_growth_records_warning(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    (ws.partitions / "vendor").mkdir(parents=True)
    (ws.images / "vendor.img").write_bytes(b"\0" * 1024 + b"EroS")
    helper = tmp_path / "bin"
    _write_fake_mkfs(helper, 40 * 1024 * 1024)
    monkeypatch.setenv("PATH", f"{helper}{os.pathsep}{os.environ.get('PATH', '')}")
    monkeypatch.setenv("DEADZONE_ALLOW_REBUILT_IMAGE_GROWTH", "true")

    result = rebuild_stable_partitions(ws, {"changed_partitions": ["vendor"]})

    assert result["partitions"][0]["status"] == "rebuilt"
    assert result["partitions"][0]["growth_allowed"] is True
    assert result["partitions"][0]["warnings"]


def test_vendor_growth_real_failure_numbers(tmp_path, monkeypatch):
    ok, reason = __import__("factory.core.stable_partition_rebuild", fromlist=["_validate_growth"])._validate_growth(
        "vendor", 2137452544, 3085180928
    )
    assert not ok
    assert "tolerance" in reason
