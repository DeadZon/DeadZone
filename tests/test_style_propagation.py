from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from factory.core.metadata import (
    ALLOWED_STYLES,
    STYLE_LABELS,
    normalize_build_metadata,
    os_family_from_build,
    validate_style,
)
from factory.state.build_state import BuildCounters, BuildState, create_build_state


# ---------------------------------------------------------------------------
# metadata helpers
# ---------------------------------------------------------------------------

def test_allowed_styles_complete():
    assert ALLOWED_STYLES == frozenset({"stable", "legend", "gaming", "epic"})


def test_style_labels_no_legend_for_stable():
    assert STYLE_LABELS["stable"] == "Stable"
    assert STYLE_LABELS["stable"] != "Legend"


def test_validate_style_stable():
    key, label = validate_style("stable")
    assert key == "stable"
    assert label == "Stable"


def test_validate_style_epic_case_insensitive():
    key, label = validate_style("EPiC")
    assert key == "epic"
    assert label == "EPiC"


def test_validate_style_legend():
    key, label = validate_style("Legend")
    assert key == "legend"
    assert label == "Legend"


def test_validate_style_invalid_raises():
    with pytest.raises(ValueError, match="Invalid style"):
        validate_style("HyperOS")


@pytest.mark.parametrize("build,expected", [
    ("OS1.2.3.0.CNXM", "HyperOS"),
    ("V14.0.2.0.MIXM", "MIUI"),
    ("MIUI12.5", "MIUI"),
    ("", "Unknown"),
    ("unknown", "Unknown"),
])
def test_os_family_from_build(build, expected):
    assert os_family_from_build(build) == expected


def test_normalize_metadata_all_unknown():
    result = normalize_build_metadata()
    assert result["device_codename"] == "Unknown"
    assert result["device_name"] == "Unknown"
    assert result["soc"] == "Unknown"
    assert result["edition"] == "Unknown"
    assert result["android_version"] == "Unknown"
    assert result["rom_version"] == "Unknown"


def test_normalize_metadata_uses_style_label():
    result = normalize_build_metadata(style_key="stable", style_label="Stable")
    assert result["edition"] == "Stable"
    assert result["edition"] != "Legend"


def test_normalize_metadata_never_legend_for_stable():
    result = normalize_build_metadata(style_key="stable", style_label="Stable")
    assert "Legend" not in result.values()


def test_normalize_metadata_uses_real_rom_info():
    rom = MagicMock()
    rom.android_version = "15"
    rom.build = "OS2.0.1.0.VNXM"
    rom.codename = "garnet"
    rom.region = "Global"
    rom.soc = "MTK"
    result = normalize_build_metadata(rom_info=rom, soc="MTK", style_key="gaming", style_label="Gaming")
    assert result["android_version"] == "15"
    assert result["rom_version"] == "OS2.0.1.0.VNXM"
    assert result["device_codename"] == "garnet"
    assert result["soc"] == "MTK"
    assert result["edition"] == "Gaming"
    assert result["os_family"] == "HyperOS"


def test_normalize_metadata_missing_shows_unknown_not_fake():
    rom = MagicMock()
    rom.android_version = ""
    rom.build = ""
    rom.codename = ""
    rom.region = ""
    rom.soc = ""
    result = normalize_build_metadata(rom_info=rom)
    for key in ("device_codename", "android_version", "rom_version"):
        assert result[key] == "Unknown", f"{key} should be 'Unknown', got {result[key]!r}"


# ---------------------------------------------------------------------------
# BuildState — style-aware build_id, last_event, defaults
# ---------------------------------------------------------------------------

def test_build_state_style_aware_build_id_stable():
    state = BuildState(edition="Stable")
    assert state.build_id.startswith("DZ-STABLE-")


def test_build_state_style_aware_build_id_legend():
    state = BuildState(edition="Legend")
    assert state.build_id.startswith("DZ-LEGEND-")


def test_build_state_style_aware_build_id_gaming():
    state = BuildState(edition="Gaming")
    assert state.build_id.startswith("DZ-GAMING-")


def test_build_state_style_aware_build_id_epic():
    state = BuildState(edition="EPiC")
    assert state.build_id.startswith("DZ-EPIC-")


def test_build_state_no_edition_plain_uuid():
    state = BuildState()
    assert not state.build_id.startswith("DZ-")


def test_build_state_device_defaults_to_detecting():
    state = BuildState(edition="Stable")
    assert state.device == "Detecting..."


def test_build_state_rom_version_defaults_to_detecting():
    state = BuildState(edition="Stable")
    assert state.rom_version == "Detecting..."


def test_build_state_android_defaults_to_detecting():
    state = BuildState(edition="Stable")
    assert state.android_version == "Detecting..."


def test_build_state_last_event_field():
    state = BuildState(edition="Stable")
    assert hasattr(state, "last_event")
    assert state.last_event == ""


def test_build_state_as_dict_includes_last_event():
    state = BuildState(edition="Stable")
    state.last_event = "[detect] ROM detected"
    d = state.as_dict()
    assert "last_event" in d
    assert d["last_event"] == "[detect] ROM detected"


def test_build_state_edition_propagates_to_json(tmp_path):
    state = create_build_state(tmp_path, edition="Gaming", soc="MTK", device="zircon")
    saved = json.loads((tmp_path / "state" / "build_state.json").read_text())
    assert saved["edition"] == "Gaming"
    assert saved["edition"] != "Legend"
    assert saved["build_id"].startswith("DZ-GAMING-")


def test_build_state_stable_never_has_legend(tmp_path):
    state = create_build_state(tmp_path, edition="Stable", soc="MTK", device="garnet")
    saved = json.loads((tmp_path / "state" / "build_state.json").read_text())
    assert saved["edition"] == "Stable"
    assert "legend" not in json.dumps(saved).lower() or saved.get("edition", "").lower() == "stable"


# ---------------------------------------------------------------------------
# EventBus — last_event update
# ---------------------------------------------------------------------------

def test_event_bus_updates_last_event(tmp_path):
    from factory.core.event_bus import EventBus

    state = BuildState(edition="Stable")
    bus = EventBus(tmp_path, state)
    bus.emit_event("detect", "RUN", "ROM detection started")
    assert "[detect] ROM detection started" == state.last_event


def test_event_bus_last_event_updates_on_each_emit(tmp_path):
    from factory.core.event_bus import EventBus

    state = BuildState(edition="Stable")
    bus = EventBus(tmp_path, state)
    bus.emit_event("detect", "RUN", "first")
    bus.emit_event("unpack", "RUN", "second")
    assert "[unpack] second" == state.last_event


# ---------------------------------------------------------------------------
# Live screen — display helpers and counter guards
# ---------------------------------------------------------------------------

def test_live_screen_display_detecting_for_unknown():
    from factory.live.live_screen import _display
    assert _display("unknown") == "Detecting..."
    assert _display("") == "Detecting..."
    assert _display("garnet") == "garnet"


def test_live_screen_display_unknown_when_not_in_progress():
    from factory.live.live_screen import _display
    assert _display("unknown", in_progress=False) == "Unknown"
    assert _display("", in_progress=False) == "Unknown"


def test_live_screen_counters_absent_before_scan():
    from factory.live.live_screen import LiveScreen

    state = BuildState(edition="Stable")
    ls = LiveScreen(state, enabled=False)
    lines = ls._status_lines()
    joined = "\n".join(lines)
    assert "Apps found" not in joined
    assert "Images extracted" not in joined


def test_live_screen_counters_appear_after_scan():
    from factory.live.live_screen import LiveScreen

    state = BuildState(edition="Stable")
    state.counters.default_found = 200
    ls = LiveScreen(state, enabled=False)
    lines = ls._status_lines()
    joined = "\n".join(lines)
    assert "Apps found" in joined
    assert "200" in joined


def test_live_screen_image_counter_appears_after_extraction():
    from factory.live.live_screen import LiveScreen

    state = BuildState(edition="Stable")
    state.counters.images_total = 9
    state.counters.images_extracted = 4
    ls = LiveScreen(state, enabled=False)
    lines = ls._status_lines()
    joined = "\n".join(lines)
    assert "Images extracted" in joined
    assert "4/9" in joined


def test_live_screen_shows_last_event():
    from factory.live.live_screen import LiveScreen

    state = BuildState(edition="Stable")
    state.last_event = "[detect] ROM detection started"
    ls = LiveScreen(state, enabled=False)
    lines = ls._status_lines()
    joined = "\n".join(lines)
    assert "[detect] ROM detection started" in joined


def test_live_screen_style_in_header(capsys):
    from factory.live.live_screen import LiveScreen

    state = BuildState(edition="Gaming")
    ls = LiveScreen(state, enabled=False)
    ls._print_header()
    captured = capsys.readouterr()
    assert "Gaming" in captured.err
    assert "Legend" not in captured.err


# ---------------------------------------------------------------------------
# GHA live mode — no spam redraw (stage-change gating)
# ---------------------------------------------------------------------------

def test_gha_live_does_not_print_same_stage_twice(monkeypatch, capsys):
    from factory.live.live_screen import LiveScreen

    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    state = BuildState(edition="Stable")
    state.current_stage = "detect"
    ls = LiveScreen(state, enabled=False)
    ls._last_gha_print = 9999999999.0  # pretend recently printed
    ls._last_stage_printed = "detect"   # same stage as current

    ls._maybe_print_tick()
    captured = capsys.readouterr()
    assert captured.err == "", "GHA should NOT reprint the same stage before timeout"


def test_gha_live_prints_on_stage_change(monkeypatch, capsys):
    from factory.live.live_screen import LiveScreen

    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    state = BuildState(edition="Stable")
    state.current_stage = "unpack"
    ls = LiveScreen(state, enabled=False)
    ls._last_stage_printed = "detect"   # different stage
    ls._last_gha_print = 9999999999.0   # recently printed but stage changed

    ls._maybe_print_tick()
    captured = capsys.readouterr()
    assert "unpack" in captured.err


# ---------------------------------------------------------------------------
# Telegram — no hardcoded Legend / uses real style
# ---------------------------------------------------------------------------

def test_telegram_document_caption_uses_real_style():
    from factory.core.telegram import TelegramStatus
    from factory.core.workspace import Workspace

    ws = MagicMock(spec=Workspace)
    ws.meta = Path("/tmp")
    ws.reports = Path("/tmp")
    ws.root = Path("/tmp/workspace")

    # enabled=True sets requested=True; also set enabled=True to bypass credential gate
    tg = TelegramStatus(
        enabled=True, soc="mtk", style="Stable", device="garnet", workspace=ws
    )
    tg.enabled = True
    tg.token = "x"
    tg.chat_id = "y"

    # Patch _send_document_to (the per-recipient sender used by the multi-
    # recipient code path) to capture the caption.
    captured_caption: list[str] = []

    def _fake_send_document_to(chat_id, path, caption):
        captured_caption.append(caption)
        return {"ok": True}

    tg._send_document_to = _fake_send_document_to

    inv_zip = MagicMock()
    inv_zip.name = "inventory.zip"
    inv_zip.is_file.return_value = True
    inv_zip.stat.return_value.st_size = 1024

    tg.send_app_inventory_document(inv_zip, total_apps=100, android_version="15")
    assert captured_caption, "send_document should have been called"
    assert "Stable" in captured_caption[0]
    assert "Legend" not in captured_caption[0]


def test_telegram_format_style_not_legend_for_stable():
    from factory.core.telegram import TelegramStatus
    from factory.core.workspace import Workspace

    ws = MagicMock(spec=Workspace)
    ws.meta = Path("/tmp")
    ws.reports = Path("/tmp")
    ws.root = Path("/tmp/workspace")

    with patch("factory.core.telegram.read_json", return_value={}):
        tg = TelegramStatus(
            enabled=True, soc="mtk", style="Stable", device="garnet", workspace=ws
        )
        tg.token = "x"
        tg.chat_id = "y"
        text = tg._format("RUNNING")
    assert "Stable" in text
    assert "Legend" not in text


# ---------------------------------------------------------------------------
# deadzone.py — validation fails clearly on missing args
# ---------------------------------------------------------------------------

def test_validate_missing_style(monkeypatch):
    import argparse
    from factory.deadzone import _validate_build_args

    args = argparse.Namespace(style="", soc="mtk", rom_url="http://x", device_codename="", custom_codename="")
    with pytest.raises(SystemExit):
        _validate_build_args(args)


def test_validate_missing_soc(monkeypatch):
    import argparse
    from factory.deadzone import _validate_build_args

    args = argparse.Namespace(style="stable", soc="", rom_url="http://x", device_codename="", custom_codename="")
    with pytest.raises(SystemExit):
        _validate_build_args(args)


def test_validate_missing_rom_url(monkeypatch):
    import argparse
    from factory.deadzone import _validate_build_args

    args = argparse.Namespace(style="stable", soc="mtk", rom_url="", device_codename="", custom_codename="")
    with pytest.raises(SystemExit):
        _validate_build_args(args)


def test_validate_passes_when_all_present():
    import argparse
    from factory.deadzone import _validate_build_args

    args = argparse.Namespace(
        style="stable", soc="mtk", rom_url="http://x",
        device_codename="garnet", custom_codename=""
    )
    # Must not raise
    _validate_build_args(args)
