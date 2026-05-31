"""Tests for super image input priority, source tracking, and error classification."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from factory.core.error_classifier import classify_error
from factory.core.super_profile import resolve_image_sources
from factory.core.workspace import create_workspace


# ── Helpers ───────────────────────────────────────────────────────────────────

def _make_img(path: Path, size: int = 1024) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"\x00" * size)
    return path


def _write_rebuild_report(ws, partitions: list[str]) -> None:
    data = {
        "status": "ok",
        "changed_partitions": partitions,
        "partitions": [
            {"partition": p, "status": "rebuilt", "original_size": 1024, "rebuilt_size": 900}
            for p in partitions
        ],
    }
    ws.reports.mkdir(parents=True, exist_ok=True)
    (ws.reports / "stable_partition_rebuild_report.json").write_text(
        json.dumps(data), encoding="utf-8"
    )


def _write_extract_meta(ws, partitions: list[str]) -> None:
    extracted = {p: str(ws.images / f"{p}.img") for p in partitions}
    data = {
        "extracted_images": extracted,
        "status": "OK",
    }
    ws.meta.mkdir(parents=True, exist_ok=True)
    (ws.meta / "payload_extract.json").write_text(json.dumps(data), encoding="utf-8")


# ── Source priority tests ──────────────────────────────────────────────────────

def test_rebuilt_image_source_is_rebuilt(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    _make_img(ws.images / "product.img")
    _write_rebuild_report(ws, ["product"])
    _write_extract_meta(ws, ["product"])

    images = {"product": ws.images / "product.img"}
    sources = resolve_image_sources(ws, images)

    assert sources["product"] == "rebuilt"


def test_extracted_image_source_is_extracted(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    _make_img(ws.images / "system.img")
    _write_rebuild_report(ws, [])
    _write_extract_meta(ws, ["system"])

    images = {"system": ws.images / "system.img"}
    sources = resolve_image_sources(ws, images)

    assert sources["system"] == "extracted"


def test_workspace_image_not_in_rebuild_or_extract(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    _make_img(ws.images / "odm.img")
    _write_rebuild_report(ws, [])
    _write_extract_meta(ws, [])

    images = {"odm": ws.images / "odm.img"}
    sources = resolve_image_sources(ws, images)

    assert sources["odm"] == "workspace"


def test_rebuilt_partitions_take_priority_over_extracted(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    _make_img(ws.images / "vendor.img")
    _write_rebuild_report(ws, ["vendor"])
    _write_extract_meta(ws, ["vendor"])

    images = {"vendor": ws.images / "vendor.img"}
    sources = resolve_image_sources(ws, images)

    assert sources["vendor"] == "rebuilt", "Rebuilt must win over extracted"


def test_multiple_partitions_mixed_sources(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    for part in ["product", "system_ext", "vendor", "system", "odm", "mi_ext"]:
        _make_img(ws.images / f"{part}.img")
    _write_rebuild_report(ws, ["product", "system_ext", "vendor"])
    _write_extract_meta(ws, ["product", "system_ext", "vendor", "system", "odm", "mi_ext"])

    images = {p: ws.images / f"{p}.img" for p in ["product", "system_ext", "vendor", "system", "odm", "mi_ext"]}
    sources = resolve_image_sources(ws, images)

    assert sources["product"] == "rebuilt"
    assert sources["system_ext"] == "rebuilt"
    assert sources["vendor"] == "rebuilt"
    assert sources["system"] == "extracted"
    assert sources["odm"] == "extracted"
    assert sources["mi_ext"] == "extracted"


def test_no_rebuild_report_falls_back_to_extracted(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    _make_img(ws.images / "system.img")
    _write_extract_meta(ws, ["system"])
    # No rebuild report written

    images = {"system": ws.images / "system.img"}
    sources = resolve_image_sources(ws, images)

    assert sources["system"] == "extracted"


def test_no_extract_meta_falls_back_to_workspace(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    _make_img(ws.images / "odm.img")
    # No rebuild or extract metadata

    images = {"odm": ws.images / "odm.img"}
    sources = resolve_image_sources(ws, images)

    assert sources["odm"] == "workspace"


# ── Error classifier: super stage must not get PAYLOAD_UNPACK_FAILED ──────────

def test_super_allocation_error_not_classified_as_payload_unpack():
    """The old _allocation error included 'payload_manifest' in its message and
    was mis-classified as PAYLOAD_UNPACK_FAILED.  The new message must not be."""
    error_msg = (
        "allocation metadata not found for system.img — "
        "check super_image_input_report.txt and super_profile_report.txt for details"
    )
    result = classify_error(error_msg, "super")
    assert result["error_type"] != "PAYLOAD_UNPACK_FAILED", (
        f"Super allocation error was mis-classified as PAYLOAD_UNPACK_FAILED: {result}"
    )
    assert result["error_type"] == "SUPER_ALLOCATION_MISSING"


def test_super_image_input_missing_classified_correctly():
    error_msg = (
        "SUPER_IMAGE_INPUT_MISSING: partition image missing for super build: odm_dlkm. "
        "Check super_image_input_report.txt for details."
    )
    result = classify_error(error_msg, "super")
    assert result["error_type"] == "SUPER_IMAGE_INPUT_MISSING"


def test_payload_unpack_still_works_for_unpack_stage():
    result = classify_error("payload.bin extraction failed: bad magic", "unpack")
    assert result["error_type"] == "PAYLOAD_UNPACK_FAILED"


def test_payload_unpack_not_triggered_by_payload_word_in_super_stage():
    """Error message containing 'payload' during super stage must not be PAYLOAD_UNPACK_FAILED."""
    error_msg = "payload_manifest allocation not resolved for vendor"
    result = classify_error(error_msg, "super")
    assert result["error_type"] != "PAYLOAD_UNPACK_FAILED", (
        f"'payload' in super stage error should not trigger PAYLOAD_UNPACK_FAILED: {result}"
    )


def test_payload_unpack_not_triggered_in_super_profile_stage():
    error_msg = "payload partitions metadata unavailable"
    result = classify_error(error_msg, "super_profile")
    assert result["error_type"] != "PAYLOAD_UNPACK_FAILED"


def test_payload_unpack_not_triggered_in_repack_stage():
    error_msg = "payload metadata missing during repack"
    result = classify_error(error_msg, "repack")
    assert result["error_type"] != "PAYLOAD_UNPACK_FAILED"


# ── Input report generation ───────────────────────────────────────────────────

def test_super_image_input_report_written(tmp_path):
    """_write_super_image_input_report creates both txt and json reports."""
    from factory.core.super_builder import _write_super_image_input_report

    ws = create_workspace(tmp_path / "workspace")
    img = _make_img(ws.images / "system.img")

    layout = {
        "device": {"codename": "zircon"},
        "superconfig_source": "mezo_verified_profile",
        "target_super_size": 9126805504,
        "dynamic_group_name": "qti_dynamic_partitions",
        "slot_mode": "VAB",
        "selected_partitions": ["system"],
        "metadata_source": "hyperur_superconfig",
    }
    dynamic_images = {"system": img}
    image_sources = {"system": "extracted"}

    _write_super_image_input_report(
        ws, layout, dynamic_images, image_sources,
        missing_images=[], lpmake_args=["lpmake", "--out", "super.img"],
        payload_reextraction_skipped=True,
    )

    txt = ws.reports / "super_image_input_report.txt"
    js = ws.reports / "super_image_input_report.json"
    assert txt.is_file()
    assert js.is_file()

    content = txt.read_text(encoding="utf-8")
    assert "zircon" in content
    assert "mezo_verified_profile" in content
    assert "9126805504" in content
    assert "qti_dynamic_partitions" in content
    assert "VAB" in content
    assert "payload_reextraction_skipped" in content

    data = json.loads(js.read_text(encoding="utf-8"))
    assert data["codename"] == "zircon"
    assert data["payload_reextraction_skipped"] is True
    assert data["partitions"][0]["name"] == "system"
    assert data["partitions"][0]["image_source"] == "extracted"


def test_super_image_input_report_lists_missing(tmp_path):
    from factory.core.super_builder import _write_super_image_input_report

    ws = create_workspace(tmp_path / "workspace")
    layout = {
        "device": {"codename": "zircon"},
        "target_super_size": 9126805504,
        "dynamic_group_name": "qti_dynamic_partitions",
        "slot_mode": "VAB",
        "selected_partitions": ["system", "odm_dlkm"],
    }

    _write_super_image_input_report(
        ws, layout, {}, {},
        missing_images=["odm_dlkm"], lpmake_args=[],
        payload_reextraction_skipped=True,
    )

    data = json.loads((ws.reports / "super_image_input_report.json").read_text(encoding="utf-8"))
    assert "odm_dlkm" in data["missing_images"]
    assert data["status"] == "missing_images"


# ── payload.bin absent after extraction must not fail if images exist ─────────

def test_payload_bin_missing_does_not_affect_source_resolution(tmp_path):
    """payload.bin being absent post-extraction is irrelevant to image source tracking."""
    ws = create_workspace(tmp_path / "workspace")
    _make_img(ws.images / "system.img")
    # Write extract meta WITHOUT a payload.bin path that exists
    data = {
        "extracted_images": {"system": str(ws.images / "system.img")},
        "status": "OK",
    }
    ws.meta.mkdir(parents=True, exist_ok=True)
    (ws.meta / "payload_extract.json").write_text(json.dumps(data), encoding="utf-8")
    # payload.bin does NOT exist on disk

    images = {"system": ws.images / "system.img"}
    sources = resolve_image_sources(ws, images)

    assert sources["system"] == "extracted", "Should resolve as extracted even if payload.bin is gone"
