"""
Tests for factory/core/partition_modifications.py and its integration with the
repacker and pipeline ordering.
"""
from __future__ import annotations

import inspect
import json

import pytest

from factory.core.partition_modifications import (
    is_partition_modified,
    list_modified_partitions,
    load_partition_modifications,
    mark_partition_modified,
    save_partition_modifications,
)
from factory.core.repacker import repack_partitions
from factory.core.workspace import create_workspace


def _erofs_header() -> bytes:
    return b"\x00" * 1024 + b"EroS" + b"\x00" * 1024


# ── manifest basics ───────────────────────────────────────────────────────────

def test_empty_manifest_when_absent(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    manifest = load_partition_modifications(ws)
    assert manifest["partitions"] == {}
    assert manifest["modified_partitions"] == []
    assert is_partition_modified(ws, "product") is False


def test_mark_partition_modified_writes_manifest(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    mark_partition_modified(ws, "product", "renamed app", stage="stable_app_policy")

    assert (ws.meta / "partition_modifications.json").is_file()
    assert is_partition_modified(ws, "product") is True
    assert list_modified_partitions(ws) == ["product"]

    entry = load_partition_modifications(ws)["partitions"]["product"]
    assert entry["modified"] is True
    assert entry["stages"] == ["stable_app_policy"]
    assert entry["reasons"] == ["renamed app"]


def test_deterministic_index_assignment(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    mark_partition_modified(ws, "product", "a")
    mark_partition_modified(ws, "vendor", "b")
    mark_partition_modified(ws, "system", "c")
    parts = load_partition_modifications(ws)["partitions"]
    assert parts["product"]["index"] == 0
    assert parts["vendor"]["index"] == 1
    assert parts["system"]["index"] == 2


def test_repeated_mark_accumulates_without_duplicates(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    mark_partition_modified(ws, "product", "reason1", stage="stage_a")
    mark_partition_modified(ws, "product", "reason1", stage="stage_a")  # dup
    mark_partition_modified(ws, "product", "reason2", stage="stage_b")
    entry = load_partition_modifications(ws)["partitions"]["product"]
    assert entry["index"] == 0  # unchanged on re-mark
    assert entry["stages"] == ["stage_a", "stage_b"]
    assert entry["reasons"] == ["reason1", "reason2"]


def test_files_dict_is_recorded(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    mark_partition_modified(
        ws, "product", "edits",
        files={"changed": ["a.apk"], "added": ["b.apk"], "removed": ["c.apk"]},
    )
    entry = load_partition_modifications(ws)["partitions"]["product"]
    assert entry["files_changed"] == ["a.apk"]
    assert entry["files_added"] == ["b.apk"]
    assert entry["files_removed"] == ["c.apk"]


def test_files_list_treated_as_changed(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    mark_partition_modified(ws, "product", "edits", files=["x.apk", "y.apk"])
    entry = load_partition_modifications(ws)["partitions"]["product"]
    assert entry["files_changed"] == ["x.apk", "y.apk"]


def test_save_recomputes_modified_partitions(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    manifest = {
        "partitions": {
            "product": {"partition": "product", "modified": True, "index": 0},
            "vendor": {"partition": "vendor", "modified": False, "index": 1},
        }
    }
    save_partition_modifications(ws, manifest)
    reloaded = load_partition_modifications(ws)
    assert reloaded["modified_partitions"] == ["product"]


# ── repacker integration ──────────────────────────────────────────────────────

def test_repacker_reads_manifest_and_skips_unmodified(tmp_path, monkeypatch):
    ws = create_workspace(tmp_path / "workspace")
    # Two partitions extracted; only product is marked modified.
    (ws.images / "product.img").write_bytes(_erofs_header())
    (ws.partitions / "product").mkdir(parents=True)
    (ws.partitions / "product" / "f.txt").write_text("x", encoding="utf-8")
    (ws.images / "vendor.img").write_bytes(_erofs_header())
    (ws.partitions / "vendor").mkdir(parents=True)
    (ws.partitions / "vendor" / "f.txt").write_text("x", encoding="utf-8")

    mark_partition_modified(ws, "vendor", "modified for test")
    monkeypatch.setenv("PATH", "")  # no mkfs.erofs → modified vendor will fail

    # product is unmodified (copied), vendor is modified (rebuild fails w/o tool)
    with pytest.raises(Exception):
        repack_partitions(ws)

    data = json.loads((ws.meta / "partition_repack.json").read_text(encoding="utf-8"))
    product = next(e for e in data["partitions"] if e["partition"] == "product")
    vendor = next(e for e in data["partitions"] if e["partition"] == "vendor")
    assert product["status"] == "copied"
    assert vendor["status"] == "failed"
    assert data["failed_partitions"] == ["vendor"]


def test_repacker_writes_reports_when_no_modifications(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "system.img").write_bytes(b"\x00" * 2048)
    # No partition marked modified at all.
    result = repack_partitions(ws)
    assert result["status"] == "ok"
    assert result["failed_partitions"] == []
    assert (ws.meta / "partition_repack.json").is_file()
    assert (ws.reports / "partition_repack_report.txt").is_file()
    # every partition is either copied or skipped — none rebuilt
    assert all(e["status"] in ("copied", "skipped") for e in result["partitions"])


# ── pipeline ordering ─────────────────────────────────────────────────────────

def test_pipeline_calls_repack_before_super_builder():
    """The build stage order must run repack before the super build."""
    from factory import deadzone

    source = inspect.getsource(deadzone._run_build)
    style_idx = source.index('"style"')
    repack_idx = source.index('"repack"')
    pre_super_idx = source.index('"pre_super_image_validation"')
    super_idx = source.index('"super"')
    assert style_idx < repack_idx < pre_super_idx < super_idx


def test_stable_partition_rebuild_marks_modified(tmp_path):
    """rebuild_stable_partitions records modifications consumable by the repacker."""
    from factory.core.stable_partition_rebuild import rebuild_stable_partitions

    ws = create_workspace(tmp_path / "workspace")
    # No changed partitions → nothing marked.
    rebuild_stable_partitions(ws, {"changed_partitions": []})
    assert list_modified_partitions(ws) == []
