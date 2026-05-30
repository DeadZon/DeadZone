from __future__ import annotations

from factory.core.stage_registry import (
    BUILD_STAGE_MAP,
    STAGE_DEFINITIONS,
    ordered_stage_ids,
    progress_at_stage_start,
    progress_for_completed_stages,
    registry_stage_for,
    total_weight,
)


EXPECTED_STAGE_IDS = [
    "preflight",
    "rom_detect",
    "payload_unpack",
    "image_mount",
    "app_inventory_scan",
    "app_policy_compare",
    "stable_app_policy",
    "legend_patches",
    "image_repack",
    "super_build",
    "fastboot_validation",
    "zip_package",
    "upload",
    "final_report",
]


def test_stage_order():
    assert ordered_stage_ids() == EXPECTED_STAGE_IDS


def test_all_stages_have_required_fields():
    required = {"id", "title", "description", "weight", "success_text", "fail_text"}
    for stage in STAGE_DEFINITIONS:
        missing = required - stage.keys()
        assert not missing, f"Stage {stage.get('id')} missing fields: {missing}"


def test_all_weights_positive():
    for stage in STAGE_DEFINITIONS:
        assert stage["weight"] > 0, f"Stage {stage['id']} has non-positive weight"


def test_total_weight_positive():
    assert total_weight() > 0


def test_progress_zero_when_nothing_complete():
    assert progress_for_completed_stages(set()) == 0.0


def test_progress_100_when_all_complete():
    all_ids = {s["id"] for s in STAGE_DEFINITIONS}
    result = progress_for_completed_stages(all_ids)
    assert result == 100.0


def test_progress_partial():
    completed = {"preflight"}
    result = progress_for_completed_stages(completed)
    assert 0.0 < result < 100.0


def test_progress_monotonic():
    prev = 0.0
    seen: set[str] = set()
    for s in STAGE_DEFINITIONS:
        seen.add(s["id"])
        current = progress_for_completed_stages(seen)
        assert current >= prev, f"Progress went backwards at {s['id']}"
        prev = current


def test_progress_at_stage_start_preflight():
    result = progress_at_stage_start("prepare")
    assert result == 0.0


def test_progress_at_stage_start_non_zero_for_later_stages():
    result = progress_at_stage_start("super")
    assert result > 0.0


def test_build_stage_map_all_map_to_known_registry_ids():
    known = {s["id"] for s in STAGE_DEFINITIONS}
    for build_stage, registry_id in BUILD_STAGE_MAP.items():
        assert registry_id in known, (
            f"BUILD_STAGE_MAP[{build_stage!r}] = {registry_id!r} is not a known registry stage"
        )


def test_registry_stage_for_known():
    assert registry_stage_for("prepare") == "preflight"
    assert registry_stage_for("super") == "super_build"
    assert registry_stage_for("upload") == "upload"
    assert registry_stage_for("cleanup") == "final_report"


def test_registry_stage_for_unknown_returns_input():
    assert registry_stage_for("unknown_custom_stage") == "unknown_custom_stage"
