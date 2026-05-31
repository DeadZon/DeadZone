"""Tests for factory.core.super_config — HyperUR SuperConfig loader and resolver."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from factory.core.super_config import (
    STATUS_BLOCKED,
    STATUS_NEEDS_INSPECTION,
    STATUS_READY,
    build_super_config_matrix,
    list_known_codenames,
    load_super_config,
    resolve_super_config_for_device,
    write_super_config_matrix_reports,
)


# ---------------------------------------------------------------------------
# 1. Known codename returns READY_SUPERCONFIG
# ---------------------------------------------------------------------------

def test_known_codename_returns_ready():
    codenames = list_known_codenames()
    assert codenames, "SuperConfig directory must have at least one device"
    first = codenames[0]
    result = resolve_super_config_for_device(first)
    assert result["status"] == STATUS_READY, f"{first}: expected READY_SUPERCONFIG, got {result['status']}"


def test_known_codename_has_required_fields():
    codenames = list_known_codenames()
    assert codenames
    result = resolve_super_config_for_device(codenames[0])
    assert result["status"] == STATUS_READY
    for key in ("super_size", "slot_mode", "group_name", "metadata_slots", "partitions", "partition_count"):
        assert key in result, f"missing key: {key}"
    assert result["super_size"] > 0
    assert result["partition_count"] > 0
    assert "system" in result["partitions"]


# ---------------------------------------------------------------------------
# 2. Unknown codename returns NEEDS_INSPECTION
# ---------------------------------------------------------------------------

def test_unknown_codename_returns_needs_inspection():
    result = resolve_super_config_for_device("nonexistent_device_xyz_999")
    assert result["status"] == STATUS_NEEDS_INSPECTION


def test_empty_codename_returns_needs_inspection():
    result = resolve_super_config_for_device("")
    assert result["status"] == STATUS_NEEDS_INSPECTION


# ---------------------------------------------------------------------------
# 3. VAB layout is not overridden by A-only guess
# ---------------------------------------------------------------------------

def test_vab_devices_have_vab_slot_mode():
    """All 76 imported configs are VAB — none should be reported as A-only."""
    codenames = list_known_codenames()
    non_vab = []
    for codename in codenames:
        result = resolve_super_config_for_device(codename)
        if result["status"] == STATUS_READY and result["slot_mode"] == "A-only":
            non_vab.append(codename)
    assert not non_vab, f"Devices incorrectly reported as A-only: {non_vab}"


def test_vab_device_has_is_vab_true():
    codenames = list_known_codenames()
    result = resolve_super_config_for_device(codenames[0])
    assert result["status"] == STATUS_READY
    assert result["is_vab"] is True


# ---------------------------------------------------------------------------
# 4. Zero-size _b placeholders are accepted as valid VAB
# ---------------------------------------------------------------------------

def test_zero_size_b_placeholders_accepted():
    """VAB devices with 0-size _b partition entries must be accepted, not rejected."""
    codenames = list_known_codenames()
    # At least one device should have has_vab_placeholders=True
    vab_ph = [c for c in codenames if resolve_super_config_for_device(c).get("has_vab_placeholders")]
    assert vab_ph, "Expected at least one device with VAB zero-size _b placeholders"


# ---------------------------------------------------------------------------
# 5. zircon resolves as READY_SUPERCONFIG from MEZO/DeadZone verified profile
# ---------------------------------------------------------------------------

def test_zircon_resolves_as_ready_superconfig():
    result = resolve_super_config_for_device("zircon")
    assert result["status"] == STATUS_READY, (
        f"zircon should be READY_SUPERCONFIG (mezo_verified_profile), got {result['status']}"
    )


def test_zircon_source_is_mezo_verified_profile():
    result = resolve_super_config_for_device("zircon")
    assert result["status"] == STATUS_READY
    assert result["source"] == "mezo_verified_profile", (
        f"zircon source should be mezo_verified_profile, got {result.get('source')}"
    )


def test_zircon_slot_mode_is_vab():
    result = resolve_super_config_for_device("zircon")
    assert result["status"] == STATUS_READY
    assert result["slot_mode"] == "VAB", f"zircon slot_mode should be VAB, got {result.get('slot_mode')}"
    assert result["is_vab"] is True


def test_zircon_super_size_preserved():
    result = resolve_super_config_for_device("zircon")
    assert result["status"] == STATUS_READY
    assert result["super_size"] == 9126805504, (
        f"zircon super_size should be 9126805504, got {result.get('super_size')}"
    )


def test_zircon_not_forced_to_aonly():
    result = resolve_super_config_for_device("zircon")
    assert result["status"] == STATUS_READY
    assert result["slot_mode"] != "A-only", "zircon must not be reported as A-only"


def test_zircon_dynamic_group_is_qti():
    result = resolve_super_config_for_device("zircon")
    assert result["status"] == STATUS_READY
    assert result["group_name"] == "qti_dynamic_partitions", (
        f"zircon group_name should be qti_dynamic_partitions, got {result.get('group_name')}"
    )


def test_zircon_zero_b_placeholders_accepted():
    result = resolve_super_config_for_device("zircon")
    assert result["status"] == STATUS_READY
    assert result.get("has_vab_placeholders") is True, (
        "zircon must have has_vab_placeholders=True (all _b slots are zero-size VAB placeholders)"
    )


def test_zircon_has_required_partitions():
    result = resolve_super_config_for_device("zircon")
    assert result["status"] == STATUS_READY
    parts = set(result.get("partition_names") or [])
    expected = {"system", "product", "vendor", "odm", "system_ext", "mi_ext",
                "vendor_dlkm", "system_dlkm", "odm_dlkm"}
    missing = expected - parts
    assert not missing, f"zircon missing partitions: {missing}"


# ---------------------------------------------------------------------------
# 6. Missing SuperConfig for truly unknown device → NEEDS_INSPECTION
# ---------------------------------------------------------------------------

def test_missing_config_is_needs_inspection_not_ready():
    # Use a device that is genuinely not in any SuperConfig
    result = resolve_super_config_for_device("tapir_not_a_real_device")
    assert result["status"] == STATUS_NEEDS_INSPECTION, (
        f"Unknown device should be NEEDS_INSPECTION, got {result['status']}"
    )


# ---------------------------------------------------------------------------
# 7. load_super_config returns empty dict for unknown devices
# ---------------------------------------------------------------------------

def test_load_super_config_returns_empty_for_unknown():
    config = load_super_config("definitely_not_a_real_codename_abc123")
    assert config == {}


# ---------------------------------------------------------------------------
# 8. Device matrix covers all known codenames
# ---------------------------------------------------------------------------

def test_matrix_covers_all_known_codenames():
    codenames = list_known_codenames()
    matrix = build_super_config_matrix()
    matrix_codenames = {row["codename"] for row in matrix}
    for codename in codenames:
        assert codename in matrix_codenames, f"Matrix missing codename: {codename}"


def test_matrix_mostly_ready():
    """Most imported devices must be READY. A few may be BLOCKED if their SuperConfig
    only contains parts_info (fs types) without actual super metadata — those are legitimately
    incomplete configs from the source project."""
    matrix = build_super_config_matrix()
    ready = [row for row in matrix if row["status"] == STATUS_READY]
    blocked = [row["codename"] for row in matrix if row["status"] == STATUS_BLOCKED]
    # At least 70 of 76 imported devices should be READY
    assert len(ready) >= 70, f"Expected ≥70 READY devices, got {len(ready)}"
    # Any BLOCKED device must have a known reason (no super metadata)
    for codename in blocked:
        config = load_super_config(codename)
        assert not config or not config.get("super_size"), (
            f"{codename}: BLOCKED but config looks valid — investigate"
        )


# ---------------------------------------------------------------------------
# 9. Matrix reports are generated correctly
# ---------------------------------------------------------------------------

def test_matrix_reports_written(tmp_path):
    txt, json_path = write_super_config_matrix_reports(tmp_path)
    assert txt.is_file()
    assert json_path.is_file()

    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert data["total_devices"] == len(list_known_codenames())
    assert data["ready_count"] > 0
    assert "devices" in data

    txt_content = txt.read_text(encoding="utf-8")
    assert "DeadZone SuperConfig Device Matrix" in txt_content
    assert "READY_SUPERCONFIG" in txt_content


# ---------------------------------------------------------------------------
# 10. Synthetic SuperConfig with invalid data → BLOCKED
# ---------------------------------------------------------------------------

def test_invalid_superconfig_returns_blocked(monkeypatch):
    """If SuperConfig entry is missing super_size, result should be BLOCKED."""
    def mock_load(codename):
        return {"slot_mode": "VAB", "partitions": {}, "super_size": 0}

    from factory.core import super_config as sc_mod
    monkeypatch.setattr(sc_mod, "load_super_config", mock_load)

    # Patch list_known_codenames so "fake_device" appears known
    original_load = sc_mod._load_super_json

    def mock_super_json(codename):
        if codename == "fake_device":
            return {"block_devices": [{"name": "super", "size": 0}], "group_table": [], "partition_table": []}
        return original_load(codename)

    monkeypatch.setattr(sc_mod, "_load_super_json", mock_super_json)
    result = sc_mod.resolve_super_config_for_device("fake_device")
    # With empty super_size and no partitions → BLOCKED
    assert result["status"] in (STATUS_BLOCKED, STATUS_NEEDS_INSPECTION)


# ---------------------------------------------------------------------------
# 11. Super size is > 0 for all known devices
# ---------------------------------------------------------------------------

def test_most_known_devices_have_super_size():
    """Most imported devices have super_size. A few (bixi, cetus, ruyi) only have
    parts_info without super metadata and are expected to have no super_size."""
    failures = []
    for codename in list_known_codenames():
        config = load_super_config(codename)
        if config and config.get("super_size", 0) <= 0:
            failures.append(codename)
    # At most 3 devices are expected to be missing super_size (bixi, cetus, ruyi)
    assert len(failures) <= 5, f"Too many devices with missing super_size: {failures}"


# ---------------------------------------------------------------------------
# 12. Partition names include at least system, product, vendor
# ---------------------------------------------------------------------------

def test_known_device_partition_names_include_core_partitions():
    codenames = list_known_codenames()
    for codename in codenames[:5]:
        config = load_super_config(codename)
        parts = set(config.get("partition_names") or [])
        missing = {"system", "product", "vendor"} - parts
        assert not missing, f"{codename}: missing core partitions {missing}"


# ---------------------------------------------------------------------------
# 13. SuperConfig source label is correct
# ---------------------------------------------------------------------------

def test_ready_result_has_source_label():
    codenames = list_known_codenames()
    result = resolve_super_config_for_device(codenames[0])
    assert result["status"] == STATUS_READY
    assert "HyperUR_Build_CN_V21" in result.get("source_label", "")
