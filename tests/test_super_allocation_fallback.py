"""Tests for super partition allocation size fallback from image files.

Covers the case where SuperConfig (e.g. zircon) provides layout metadata but
all partition sizes are 0 — the pipeline must derive allocation_size from the
actual image files rather than failing with SUPER_ALLOCATION_MISSING.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from factory.core.super_profile import (
    ALLOCATION_ALIGN,
    _align_up,
    build_super_profile,
    write_super_allocation_report,
)
from factory.core.workspace import Workspace, create_workspace, write_json


# ── Helpers ───────────────────────────────────────────────────────────────────

def _make_img(path: Path, size: int = 4096) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"\x00" * size)
    return path


def _write_rebuild_report(ws: Workspace, partitions: list[str], size: int = 4096) -> None:
    data = {
        "status": "ok",
        "partitions": [
            {"partition": p, "status": "rebuilt", "original_size": size, "rebuilt_size": size}
            for p in partitions
        ],
    }
    ws.reports.mkdir(parents=True, exist_ok=True)
    (ws.reports / "stable_partition_rebuild_report.json").write_text(
        json.dumps(data), encoding="utf-8"
    )


def _write_extract_meta(ws: Workspace, partitions: list[str]) -> None:
    extracted = {p: str(ws.images / f"{p}.img") for p in partitions}
    ws.meta.mkdir(parents=True, exist_ok=True)
    (ws.meta / "payload_extract.json").write_text(
        json.dumps({"extracted_images": extracted, "status": "OK"}), encoding="utf-8"
    )


def _minimal_device_config(codename: str = "nodevice_xyz") -> dict[str, Any]:
    """A device config with a codename that has no SuperConfig entry, forcing fallback."""
    return {
        "codename": codename,
        "resolved_codename": codename,
        "name": "Test Device",
        "soc": "unknown",
        "super": {},
        "_soc_super": {},
        "_device_super": {},
    }


def _setup_ws(
    tmp_path: Path,
    partitions_with_sizes: dict[str, int],
    rebuilt: list[str] | None = None,
    extracted: list[str] | None = None,
) -> Workspace:
    ws = create_workspace(tmp_path / "workspace")
    ws.meta.mkdir(parents=True, exist_ok=True)
    write_json(ws.meta / "rom_info.json", {"codename": "nodevice_xyz"})
    write_json(ws.meta / "device_info.json", {"codename": "nodevice_xyz"})
    write_json(ws.meta / "super_layout.json", {})
    write_json(ws.meta / "partition_map.json", {})
    for part, size in partitions_with_sizes.items():
        _make_img(ws.images / f"{part}.img", size)
    if rebuilt:
        _write_rebuild_report(ws, rebuilt)
    if extracted:
        _write_extract_meta(ws, extracted)
    return ws


# ── Unit tests for _align_up ──────────────────────────────────────────────────

def test_align_up_already_aligned():
    assert _align_up(1_048_576) == 1_048_576


def test_align_up_rounds_up():
    assert _align_up(1) == ALLOCATION_ALIGN
    assert _align_up(1_048_575) == 1_048_576
    assert _align_up(1_048_577) == 2 * 1_048_576


def test_align_up_zero_returns_zero():
    assert _align_up(0) == 0


def test_align_up_custom_alignment():
    assert _align_up(5000, 4096) == 8192
    assert _align_up(4096, 4096) == 4096


def test_align_up_result_gte_input():
    for size in [1, 100, 4095, 4096, 4097, 1_000_000, 1_048_575]:
        assert _align_up(size) >= size


# ── Fallback: allocation derived from image size ───────────────────────────────

def test_image_size_fallback_fills_allocation_when_no_metadata(tmp_path):
    """When no metadata provides allocation sizes, fallback to image file size."""
    ws = _setup_ws(tmp_path, {"system": 5_000_000})
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    part = profile["partitions"].get("system")
    assert part is not None, "system should be in partitions"
    assert part["allocation_size"] is not None, "allocation_size must not be None when image exists"
    assert part["allocation_size"] > 0
    assert "image_size_fallback" in part["source"]


def test_fallback_allocation_is_aligned(tmp_path):
    """Allocation from image fallback must be a multiple of ALLOCATION_ALIGN."""
    # Use a size that is not a multiple of 1 MiB
    ws = _setup_ws(tmp_path, {"system": 3_500_000})
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    alloc = profile["partitions"]["system"]["allocation_size"]
    assert alloc % ALLOCATION_ALIGN == 0, f"allocation {alloc} is not aligned to {ALLOCATION_ALIGN}"


def test_fallback_allocation_gte_image_size(tmp_path):
    """Fallback allocation must be >= the actual image file size."""
    ws = _setup_ws(tmp_path, {"system": 3_700_000})
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    entry = profile["partitions"]["system"]
    assert entry["allocation_size"] >= entry["image_size"]


def test_rebuilt_partition_uses_image_fallback_with_rebuilt_source(tmp_path):
    """Rebuilt partition's fallback allocation source must say 'image_size_fallback:rebuilt'."""
    ws = _setup_ws(
        tmp_path,
        {"product": 8_000_000, "system_ext": 4_000_000, "vendor": 12_000_000},
        rebuilt=["product", "system_ext", "vendor"],
    )
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    for part_name in ("product", "system_ext", "vendor"):
        entry = profile["partitions"].get(part_name)
        assert entry is not None, f"{part_name} missing from partitions"
        assert entry["allocation_size"] is not None
        assert entry["source"] == "image_size_fallback:rebuilt", (
            f"{part_name} source is {entry['source']!r}, expected image_size_fallback:rebuilt"
        )


def test_extracted_partition_uses_image_fallback_with_extracted_source(tmp_path):
    """Extracted partition's fallback allocation source must say 'image_size_fallback:extracted'."""
    ws = _setup_ws(
        tmp_path,
        {"system": 10_000_000, "odm": 2_000_000, "mi_ext": 1_500_000},
        extracted=["system", "odm", "mi_ext"],
    )
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    for part_name in ("system", "odm", "mi_ext"):
        entry = profile["partitions"].get(part_name)
        assert entry is not None, f"{part_name} missing from partitions"
        assert entry["source"] == "image_size_fallback:extracted", (
            f"{part_name} source is {entry['source']!r}"
        )


def test_rebuilt_takes_priority_over_extracted_for_source_label(tmp_path):
    """When a partition is in both rebuilt and extracted, source label is rebuilt."""
    ws = _setup_ws(
        tmp_path,
        {"vendor": 9_000_000},
        rebuilt=["vendor"],
        extracted=["vendor"],
    )
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    entry = profile["partitions"]["vendor"]
    assert entry["source"] == "image_size_fallback:rebuilt"


# ── VAB _b placeholders ────────────────────────────────────────────────────────

def test_vab_b_placeholders_are_zero_size(tmp_path):
    """_b VAB placeholder entries must have allocation_size == 0."""
    ws = _setup_ws(tmp_path, {"system": 4_096_000, "vendor": 8_192_000})
    # Force VAB by writing slot_mode into device_info
    write_json(ws.meta / "device_info.json", {"codename": "nodevice_xyz", "slot_mode": "VAB"})
    write_json(ws.meta / "rom_info.json", {"codename": "nodevice_xyz", "slot_mode": "VAB"})

    profile = build_super_profile(ws, device_config=_minimal_device_config())

    zero_b = profile.get("vab_zero_b_partitions") or []
    assert zero_b, "VAB profile must have _b zero-size placeholder entries"
    for entry in zero_b:
        assert entry["allocation_size"] == 0, (
            f"{entry['name']} _b placeholder has non-zero allocation: {entry['allocation_size']}"
        )


def test_vab_b_placeholders_have_no_image(tmp_path):
    """_b entries must not be assigned image files."""
    ws = _setup_ws(tmp_path, {"system": 4_096_000})
    write_json(ws.meta / "device_info.json", {"codename": "nodevice_xyz", "slot_mode": "VAB"})
    write_json(ws.meta / "rom_info.json", {"codename": "nodevice_xyz", "slot_mode": "VAB"})

    profile = build_super_profile(ws, device_config=_minimal_device_config())

    zero_b = profile.get("vab_zero_b_partitions") or []
    for entry in zero_b:
        assert "image_path" not in entry or entry.get("image_path") is None, (
            f"{entry['name']}: _b placeholder must not have an image_path"
        )


# ── Group size computation ─────────────────────────────────────────────────────

def test_group_size_nonzero_when_metadata_absent(tmp_path):
    """When no metadata provides group_size, the default (super_size - overhead) must be > 0."""
    ws = _setup_ws(tmp_path, {"system": 4_000_000, "vendor": 8_000_000})
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    assert profile["group_size"] > 0, "group_size must not be zero"
    assert profile["group_size"] < profile["super_size"], "group_size must be < super_size"


def test_group_size_gte_sum_of_allocations(tmp_path):
    """group_size must be at least as large as the sum of _a allocations."""
    ws = _setup_ws(tmp_path, {"system": 5_000_000, "vendor": 9_000_000, "product": 3_000_000})
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    alloc_sum = sum(
        entry.get("allocation_size") or 0
        for entry in profile["partitions"].values()
    )
    assert profile["group_size"] >= alloc_sum, (
        f"group_size {profile['group_size']} < sum of allocations {alloc_sum}"
    )


# ── No SUPER_ALLOCATION_MISSING when images exist ─────────────────────────────

def test_no_missing_metadata_when_all_images_present(tmp_path):
    """build_super_profile must not put partitions in missing_metadata when their image exists."""
    ws = _setup_ws(
        tmp_path,
        {"system": 4_096_000, "product": 2_048_000, "vendor": 8_192_000},
    )
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    assert profile["missing_metadata"] == [], (
        f"missing_metadata should be empty when images exist, got {profile['missing_metadata']}"
    )


def test_allocation_size_not_none_when_image_exists(tmp_path):
    """No partition with a real image should have allocation_size=None."""
    ws = _setup_ws(tmp_path, {
        "system": 4_000_000,
        "product": 2_000_000,
        "vendor": 6_000_000,
        "system_ext": 1_500_000,
        "odm": 500_000,
    })
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    for name, entry in profile["partitions"].items():
        assert entry["allocation_size"] is not None and entry["allocation_size"] > 0, (
            f"{name}: allocation_size is None/zero but image exists"
        )


def test_allow_image_size_allocations_true_when_fallback_used(tmp_path):
    """allow_image_size_allocations flag must be True when fallback is in use."""
    ws = _setup_ws(tmp_path, {"system": 4_096_000})
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    assert profile["allow_image_size_allocations"] is True


# ── Allocation report generation ──────────────────────────────────────────────

def test_super_allocation_report_written(tmp_path):
    """write_super_allocation_report creates both txt and json reports."""
    ws = _setup_ws(tmp_path, {"system": 4_096_000, "vendor": 8_192_000})
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    json_path = ws.reports / "super_allocation_report.json"
    txt_path = ws.reports / "super_allocation_report.txt"
    assert json_path.is_file(), "super_allocation_report.json must be written"
    assert txt_path.is_file(), "super_allocation_report.txt must be written"


def test_super_allocation_report_json_fields(tmp_path):
    """super_allocation_report.json must contain the required fields."""
    ws = _setup_ws(
        tmp_path,
        {"system": 4_000_000, "vendor": 8_000_000},
        extracted=["system", "vendor"],
    )
    profile = build_super_profile(ws, device_config=_minimal_device_config())

    data = json.loads((ws.reports / "super_allocation_report.json").read_text())
    for key in ("codename", "super_size", "group_name", "slot_mode",
                "allocation_source", "partitions", "group_required_size",
                "group_available_size", "lpmake_partition_args"):
        assert key in data, f"super_allocation_report.json missing key: {key}"
    assert data["allocation_source"] == "image_size_fallback"
    assert len(data["partitions"]) >= 2


def test_super_allocation_report_lpmake_args_non_empty(tmp_path):
    """lpmake_partition_args in the report must be populated for existing images."""
    ws = _setup_ws(tmp_path, {"system": 4_096_000, "vendor": 8_192_000})
    build_super_profile(ws, device_config=_minimal_device_config())

    data = json.loads((ws.reports / "super_allocation_report.json").read_text())
    assert data["lpmake_partition_args"], "lpmake_partition_args must not be empty"
    for arg in data["lpmake_partition_args"]:
        assert "--partition" in arg


# ── SUPER_IMAGE_INPUT_MISSING when image is absent ────────────────────────────

def test_check_super_image_inputs_detects_missing_partitions(tmp_path):
    """_check_super_image_inputs must report missing images as SUPER_IMAGE_INPUT_MISSING."""
    from factory.core.super_builder import _check_super_image_inputs

    ws = create_workspace(tmp_path / "workspace")
    # Layout says odm_dlkm and system_dlkm should be present, but no images exist
    layout = {
        "selected_partitions": ["odm_dlkm", "system_dlkm"],
        "image_sources": {},
    }
    _, missing = _check_super_image_inputs(ws, layout, {})
    assert "odm_dlkm" in missing
    assert "system_dlkm" in missing


def test_super_image_input_missing_error_message_format():
    """SUPER_IMAGE_INPUT_MISSING message must be classifiable by the error classifier."""
    from factory.core.error_classifier import classify_error

    msg = (
        "SUPER_IMAGE_INPUT_MISSING: partition image missing for super build: odm_dlkm. "
        "Check super_image_input_report.txt for details."
    )
    result = classify_error(msg, "super")
    assert result["error_type"] == "SUPER_IMAGE_INPUT_MISSING"


# ── SUPER_GROUP_SIZE_EXCEEDED ─────────────────────────────────────────────────

def test_super_group_size_exceeded_when_images_exceed_group(tmp_path):
    """validate_pre_super_images must raise when image total exceeds group size."""
    from factory.core.super_builder import validate_pre_super_images, PreSuperValidationError

    ws = create_workspace(tmp_path / "workspace")
    ws.meta.mkdir(parents=True, exist_ok=True)
    ws.images.mkdir(parents=True, exist_ok=True)

    # Two partitions, each 600 MiB — total 1.2 GiB > group limit 800 MiB
    img_size = 600 * 1024 * 1024
    _make_img(ws.images / "system.img", img_size)
    _make_img(ws.images / "vendor.img", img_size)

    group_limit = 800 * 1024 * 1024
    layout = {
        "selected_partitions": ["system", "vendor"],
        "dynamic_images": {
            "system": str(ws.images / "system.img"),
            "vendor": str(ws.images / "vendor.img"),
        },
        "partitions": {
            "system": {"allocation_size": img_size},
            "vendor": {"allocation_size": img_size},
        },
        "group_size": group_limit,
    }

    ws.reports.mkdir(parents=True, exist_ok=True)

    with pytest.raises((RuntimeError, PreSuperValidationError)) as exc_info:
        validate_pre_super_images(ws, layout)
    err = str(exc_info.value)
    assert "SUPER_GROUP_SIZE_EXCEEDED" in err or "group" in err.lower(), (
        f"Expected SUPER_GROUP_SIZE_EXCEEDED, got: {err}"
    )


# ── zircon zero-size SuperConfig triggers fallback ────────────────────────────

def test_zircon_superconfig_zero_sizes_triggers_image_fallback(tmp_path):
    """zircon SuperConfig has all-zero partition sizes; profile must use image fallback."""
    ws = create_workspace(tmp_path / "workspace")
    ws.meta.mkdir(parents=True, exist_ok=True)
    write_json(ws.meta / "rom_info.json", {"codename": "zircon"})
    write_json(ws.meta / "device_info.json", {"codename": "zircon", "slot_mode": "VAB"})
    write_json(ws.meta / "super_layout.json", {})
    write_json(ws.meta / "partition_map.json", {})

    # Create representative image files
    for part, size in {
        "system": 10_000_000,
        "product": 8_000_000,
        "vendor": 12_000_000,
        "system_ext": 4_000_000,
        "odm": 2_000_000,
        "mi_ext": 1_000_000,
        "system_dlkm": 500_000,
        "vendor_dlkm": 500_000,
    }.items():
        _make_img(ws.images / f"{part}.img", size)

    _write_rebuild_report(ws, ["product", "system_ext", "vendor"])
    _write_extract_meta(ws, ["system", "odm", "mi_ext", "system_dlkm", "vendor_dlkm"])

    device_config = {
        "codename": "zircon",
        "resolved_codename": "zircon",
        "name": "Redmi Note 13 Pro+ 5G",
        "soc": "sm7550",
        "super": {},
        "_soc_super": {},
        "_device_super": {},
    }
    profile = build_super_profile(ws, device_config=device_config)

    # zircon SuperConfig is active but has zero sizes — fallback must kick in
    assert profile["allow_image_size_allocations"] is True, (
        "zircon should use image_size_fallback since all SuperConfig sizes are 0"
    )
    assert profile["missing_metadata"] == [], (
        f"No partitions should be missing metadata when images exist: {profile['missing_metadata']}"
    )
    for name, entry in profile["partitions"].items():
        assert entry["allocation_size"] is not None and entry["allocation_size"] > 0, (
            f"zircon partition {name} has no allocation_size"
        )
        assert "image_size_fallback" in entry["source"], (
            f"zircon partition {name} source {entry['source']!r} should be image_size_fallback"
        )

    # Rebuilt partitions must use rebuilt source label
    for part_name in ("product", "system_ext", "vendor"):
        assert profile["partitions"][part_name]["source"] == "image_size_fallback:rebuilt", (
            f"{part_name}: expected rebuilt source"
        )

    # Extracted partitions must use extracted source label
    for part_name in ("system", "odm", "mi_ext"):
        assert profile["partitions"][part_name]["source"] == "image_size_fallback:extracted", (
            f"{part_name}: expected extracted source"
        )

    # group_size must be valid (from SuperConfig: 9116319744)
    assert profile["group_size"] > 0
    # VAB zero_b entries must all be zero
    for entry in profile.get("vab_zero_b_partitions") or []:
        assert entry["allocation_size"] == 0
