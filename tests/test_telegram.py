from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from factory.core.telegram import STAGE_DISPLAY, TelegramStatus, _stage_title
from factory.core.workspace import Workspace


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_ws(tmp_path: Path, state: dict | None = None) -> Workspace:
    """Create a minimal workspace rooted at tmp_path/workspace."""
    root = tmp_path / "workspace"
    root.mkdir(parents=True, exist_ok=True)
    for sub in ("input", "extracted", "images", "partitions", "meta", "reports", "logs"):
        (root / sub).mkdir(exist_ok=True)
    (tmp_path / "final").mkdir(exist_ok=True)

    # Write build_state.json if state dict supplied
    if state is not None:
        state_dir = tmp_path / "state"
        state_dir.mkdir(exist_ok=True)
        (state_dir / "build_state.json").write_text(json.dumps(state), encoding="utf-8")

    return Workspace(
        root=root,
        input=root / "input",
        extracted=root / "extracted",
        images=root / "images",
        partitions=root / "partitions",
        meta=root / "meta",
        reports=root / "reports",
        logs=root / "logs",
        final=tmp_path / "final",
    )


def _make_tg(ws: Workspace, style: str = "Ultra", device: str = "miatoll", soc: str = "Snapdragon") -> TelegramStatus:
    """Create a TelegramStatus with credentials pre-set for formatting tests."""
    tg = TelegramStatus(enabled=True, soc=soc, style=style, device=device, workspace=ws)
    tg.enabled = True
    tg.token = "fake_token"
    tg.chat_id = "fake_chat"
    return tg


# ---------------------------------------------------------------------------
# test_telegram_uses_human_stage_titles
# ---------------------------------------------------------------------------


def test_telegram_uses_human_stage_titles(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.add_event("image_extraction", "RUN")

    text = tg._format("RUNNING")

    assert "Extracting Images" in text or "Extracting images" in text
    assert "Scanning App Inventory" in text or "Super image" in text or "Timeline:" in text


def test_telegram_done_uses_human_labels(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    for sid in ("image_extraction", "app_inventory", "super"):
        tg.add_event(sid, "RUN")
        tg.add_event(sid, "OK")

    text = tg._format("OK")

    assert "✅ DeadZone Build Completed" in text


# ---------------------------------------------------------------------------
# test_telegram_does_not_show_raw_stage_ids
# ---------------------------------------------------------------------------


def test_telegram_does_not_show_raw_stage_ids(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.add_event("image_extraction", "RUN")
    tg.add_event("image_extraction", "OK")
    tg.add_event("app_inventory", "RUN")

    text = tg._format("RUNNING")

    for raw_id in STAGE_DISPLAY:
        # Raw IDs must not appear as bare words (outside of their human labels)
        # We check they don't appear at a line start or standalone
        for line in text.splitlines():
            stripped = line.strip()
            assert stripped != raw_id, (
                f"Raw stage ID '{raw_id}' appeared as a standalone line: {stripped!r}"
            )


# ---------------------------------------------------------------------------
# test_telegram_collapses_run_ok_duplicates
# ---------------------------------------------------------------------------


def test_telegram_collapses_run_ok_duplicates(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    # Add RUN then OK for the same stage — timeline should show only ✅, not 🔄 as well
    tg.add_event("image_extraction", "RUN")
    tg.add_event("image_extraction", "OK")
    tg.add_event("app_inventory", "RUN")

    text = tg._format("RUNNING")

    # image_extraction should appear only in its done form (✅), not also as 🔄
    assert "✅ Images extracted" in text
    assert "🔄 Extracting images" not in text


# ---------------------------------------------------------------------------
# test_telegram_no_developer_recommendation
# ---------------------------------------------------------------------------


def test_telegram_no_developer_recommendation(tmp_path):
    ws = _make_ws(tmp_path)
    # Write a size_policy.json with a recommendation field
    (ws.meta / "size_policy.json").write_text(
        json.dumps({
            "final_zip_max_bytes": 4_500_000_000,
            "recommendation": "implement image mount/extract/rebuild stage",
        }),
        encoding="utf-8",
    )
    tg = _make_tg(ws)
    tg.add_event("image_extraction", "RUN")

    text = tg._format("RUNNING")

    assert "Recommendation:" not in text
    assert "implement image mount" not in text


# ---------------------------------------------------------------------------
# test_telegram_current_stage_not_done_stage
# ---------------------------------------------------------------------------


def test_telegram_current_stage_not_done_stage(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    # super is done; current running stage should be fastboot_validation
    for sid in ("image_extraction", "app_inventory", "super"):
        tg.add_event(sid, "RUN")
        tg.add_event(sid, "OK")
    tg.add_event("fastboot_validation", "RUN")

    text = tg._format("RUNNING")

    # Current stage indicator must point at fastboot_validation, not super
    assert "▶ Validating Fastboot Package" in text
    assert "▶ Building Super Image" not in text
    # super must show as done in timeline
    assert "✅ Super image built" in text


# ---------------------------------------------------------------------------
# test_telegram_stable_policy_counters_visible
# ---------------------------------------------------------------------------


def test_telegram_stable_policy_counters_visible(tmp_path):
    state = {
        "counters": {
            "stable_kept_apps": 142,
            "stable_renamed_apps": 3,
            "stable_missing_apps": 0,
            "stable_deleted_extra_apps": 12,
        }
    }
    ws = _make_ws(tmp_path, state=state)
    tg = _make_tg(ws)
    tg.add_event("stable_app_policy", "RUN")

    text = tg._format("RUNNING")

    assert "Stable App Policy:" in text
    assert "✅ Kept: 142" in text
    assert "🔁 Renamed: 3" in text
    assert "🧹 Deleted extra: 12" in text


def test_telegram_stable_policy_block_absent_when_no_counters(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)

    text = tg._format("RUNNING")

    assert "Stable App Policy:" not in text


# ---------------------------------------------------------------------------
# test_telegram_done_message_has_pixeldrain_if_available
# ---------------------------------------------------------------------------


def test_telegram_done_message_has_pixeldrain_if_available(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    for sid in ("image_extraction", "super", "upload"):
        tg.add_event(sid, "RUN")
        tg.add_event(sid, "OK")

    text = tg._format("OK", upload_url="https://pixeldrain.com/u/abc123")

    assert "✅ DeadZone Build Completed" in text
    assert "https://pixeldrain.com/u/abc123" in text
    assert "Reports generated ✅" in text


def test_telegram_done_message_no_pixeldrain_when_missing(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)

    text = tg._format("OK")

    assert "✅ DeadZone Build Completed" in text
    assert "PixelDrain:" not in text


# ---------------------------------------------------------------------------
# test_telegram_failed_message_has_error_type_and_suggested_check
# ---------------------------------------------------------------------------


def test_telegram_failed_message_has_error_type_and_suggested_check(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.failed_stage = "super"
    tg.error_summary = "lpmake returned exit code 1"
    tg._classified_error = {
        "error_type": "LPMAKE_FAILED",
        "cause": "lpmake exit code 1",
        "suggested_fix": "Check lpmake binary",
        "suggested_check": "Verify super partition layout",
    }

    text = tg._format("FAILED")

    assert "❌ DeadZone Build Failed" in text
    assert "Failed stage: Building Super Image" in text
    assert "Error type: LPMAKE_FAILED" in text
    assert "Suggested check: Verify super partition layout" in text


def test_telegram_failed_message_fallback_suggested_check(tmp_path):
    """When suggested_check is absent, suggested_fix is shown as fallback."""
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.failed_stage = "upload"
    tg._classified_error = {
        "error_type": "PIXELDRAIN_UPLOAD_FAILED",
        "cause": "unauthorized",
        "suggested_fix": "Check PIXELDRAIN_API_KEY",
        "suggested_check": "",
    }

    text = tg._format("FAILED")

    assert "Suggested check: Check PIXELDRAIN_API_KEY" in text


def test_telegram_failed_message_cleans_structured_error_summary(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws, style="Stable", device="zircon", soc="mtk")
    tg.failed_stage = "stable_app_policy"
    tg.error_summary = "\n".join(
        [
            "MEZO / DeadZone Error Summary",
            "status: FAILED",
            "failed stage: stable_app_policy",
            "title: Required file is missing",
            "reason: Stable App Policy requires ListMezo/free/apps.list but the file was not found",
            "recommendation: Check the previous stage report and workspace logs.",
            "hint: C",
        ]
    )
    tg._classified_error = {
        "error_type": "APPS_LIST_MISSING",
        "cause": "ListMezo/free/apps.list was not found",
        "suggested_fix": "Add ListMezo/free/apps.list to the repository",
        "suggested_check": "Verify the file exists at repo root before Stable App Policy runs",
    }

    text = tg._format("FAILED")

    assert "MEZO / DeadZone Error Summary" not in text
    for raw in ("status:", "failed stage:", "title:", "reason:", "recommendation:", "hint:"):
        assert raw not in text
    assert "Failed stage: Applying Stable App Policy" in text
    assert "Error type: APPS_LIST_MISSING" in text
    assert "Cause: ListMezo/free/apps.list was not found" in text
    assert "Suggested fix: Add ListMezo/free/apps.list to the repository" in text
    assert "Suggested check: Verify the file exists at repo root before Stable App Policy runs" in text
    assert "Suggested check: C" not in text


def test_telegram_failed_message_omits_malformed_hint(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.failed_stage = "stable_app_policy"
    tg.error_summary = "\n".join(
        [
            "reason: ListMezo/free/apps.list was not found",
            "recommendation: Add ListMezo/free/apps.list to the repository",
            "hint: C",
        ]
    )
    tg._classified_error = {}

    text = tg._format("FAILED")

    assert "Suggested check: Add ListMezo/free/apps.list to the repository" in text
    assert "Suggested check: C" not in text


def test_telegram_unsafe_matching_failure_message_is_clear(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.failed_stage = "stable_app_policy"
    tg._classified_error = {
        "error_type": "STABLE_APP_MATCHING_UNSAFE",
        "cause": "Matching unsafe: kept=1, missing=217, delete_candidates=175",
        "suggested_fix": "Fix package extraction/matching before deleting apps",
        "suggested_check": "stable_package_scan_report.json and stable_app_policy_report.json",
    }

    text = tg._format("FAILED")

    assert "Failed stage: Applying Stable App Policy" in text
    assert "Error type: STABLE_APP_MATCHING_UNSAFE" in text
    assert "Cause: Matching unsafe: kept=1, missing=217, delete_candidates=175" in text


def test_telegram_rebuilt_image_too_large_failure_message_is_clear(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.failed_stage = "pre_super_image_validation"
    tg._classified_error = {
        "error_type": "REBUILT_IMAGE_TOO_LARGE",
        "cause": "vendor.img grew from 2137452544 to 3085180928",
        "suggested_fix": "Rebuild EROFS with correct compression/options",
        "suggested_check": "stable_partition_rebuild_report.json and super_profile_report.txt",
    }

    text = tg._format("FAILED")

    assert "Failed stage: Validating Rebuilt Images" in text
    assert "Error type: REBUILT_IMAGE_TOO_LARGE" in text
    assert "LPMAKE_FAILED" not in text
    assert "Cause: vendor.img grew from 2137452544 to 3085180928" in text


# ---------------------------------------------------------------------------
# test_telegram_edits_same_message_id
# ---------------------------------------------------------------------------


def test_telegram_edits_same_message_id(tmp_path):
    """sendMessage is called once; subsequent updates use editMessageText."""
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)

    api_calls: list[str] = []

    def _fake_post(method: str, payload: dict) -> dict:
        api_calls.append(method)
        if method == "sendMessage":
            return {"ok": True, "result": {"message_id": 42}}
        return {"ok": True, "result": {"message_id": 42}}

    tg._post = _fake_post  # type: ignore[assignment]
    tg._last_edit_at = 0.0

    # Bypass throttle by setting _TELEGRAM_THROTTLE_SECONDS to 0
    with patch("factory.core.telegram._TELEGRAM_THROTTLE_SECONDS", 0):
        tg.start()
        tg.add_event("image_extraction", "RUN")
        tg.add_event("image_extraction", "OK")
        tg.finish("OK")

    sends = [m for m in api_calls if m == "sendMessage"]
    edits = [m for m in api_calls if m == "editMessageText"]

    assert len(sends) == 1, f"Expected 1 sendMessage, got {len(sends)}: {api_calls}"
    assert len(edits) >= 1, f"Expected at least 1 editMessageText, got {len(edits)}: {api_calls}"
    assert tg.message_id == 42


def test_telegram_stage_change_forces_update_immediately(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.message_id = 42
    tg._last_edit_at = 99.0
    api_calls: list[tuple[str, dict]] = []
    tg._post = lambda method, payload: api_calls.append((method, payload)) or {"ok": True, "result": {"message_id": 42}}  # type: ignore[assignment]

    with patch("factory.core.telegram.time.monotonic", return_value=100.0):
        tg.add_event("super", "RUN")

    assert [m for m, _ in api_calls] == ["editMessageText"]


def test_telegram_long_stage_updates_after_configured_interval(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.message_id = 42
    tg._last_stage = "super"
    tg._last_edit_at = 80.0
    tg._update_interval_seconds = 20.0
    api_calls: list[str] = []
    tg._post = lambda method, payload: api_calls.append(method) or {"ok": True, "result": {"message_id": 42}}  # type: ignore[assignment]

    with patch("factory.core.telegram.time.monotonic", return_value=100.0):
        tg.add_event("super", "OK")

    assert api_calls == ["editMessageText"]


def test_telegram_throttle_blocks_too_fast_updates(tmp_path, capsys):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.message_id = 42
    tg._last_stage = "super"
    tg._last_edit_at = 96.0
    api_calls: list[str] = []
    tg._post = lambda method, payload: api_calls.append(method) or {"ok": True, "result": {"message_id": 42}}  # type: ignore[assignment]

    with patch("factory.core.telegram.time.monotonic", return_value=100.0):
        tg.add_event("super", "OK")

    assert api_calls == []
    assert "[TELEGRAM] skipped update: reason=throttle elapsed=4s" in capsys.readouterr().out


def test_telegram_github_actions_default_interval_is_20_seconds(tmp_path, monkeypatch):
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    monkeypatch.delenv("DEADZONE_TELEGRAM_UPDATE_INTERVAL_SECONDS", raising=False)
    monkeypatch.delenv("DEADZONE_TELEGRAM_STAGE_UPDATE_INTERVAL_SECONDS", raising=False)
    ws = _make_ws(tmp_path)

    tg = _make_tg(ws)

    assert tg._update_interval_seconds == 20.0


def test_telegram_local_default_interval_is_15_seconds(tmp_path, monkeypatch):
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    monkeypatch.delenv("DEADZONE_TELEGRAM_UPDATE_INTERVAL_SECONDS", raising=False)
    monkeypatch.delenv("DEADZONE_TELEGRAM_STAGE_UPDATE_INTERVAL_SECONDS", raising=False)
    ws = _make_ws(tmp_path)

    tg = _make_tg(ws)

    assert tg._update_interval_seconds == 15.0


def test_telegram_update_interval_env_override(tmp_path, monkeypatch):
    monkeypatch.setenv("DEADZONE_TELEGRAM_UPDATE_INTERVAL_SECONDS", "11")
    monkeypatch.delenv("DEADZONE_TELEGRAM_STAGE_UPDATE_INTERVAL_SECONDS", raising=False)
    ws = _make_ws(tmp_path)

    tg = _make_tg(ws)

    assert tg._update_interval_seconds == 11.0


def test_telegram_success_and_failure_force_final_edit(tmp_path):
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.message_id = 42
    tg._last_edit_at = 99.0
    api_calls: list[tuple[str, int | None]] = []
    tg._post = lambda method, payload: api_calls.append((method, payload.get("message_id"))) or {"ok": True, "result": {"message_id": 42}}  # type: ignore[assignment]

    with patch("factory.core.telegram.time.monotonic", return_value=100.0):
        tg.finish("OK")
        tg.finish("FAIL")

    assert api_calls == [("editMessageText", 42), ("editMessageText", 42)]
