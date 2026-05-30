from __future__ import annotations

import os
from pathlib import Path

import pytest

from factory.core.stable_partition_rebuild import StablePartitionRebuildError, rebuild_stable_partitions
from factory.core.workspace import create_workspace


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
    helper.mkdir()
    mkfs = helper / "mkfs.erofs"
    mkfs.write_text("#!/bin/sh\nprintf rebuilt > \"$1\"\n", encoding="utf-8")
    mkfs.chmod(0o755)
    monkeypatch.setenv("PATH", str(helper))
    result = rebuild_stable_partitions(ws, {"changed_partitions": ["product"]})
    entry = result["partitions"][0]
    assert entry["status"] == "rebuilt"
    assert entry["size_before"] > entry["size_after"]
    assert entry["bytes_saved"] > 0
