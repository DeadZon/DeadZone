from __future__ import annotations

import json
import tempfile
from pathlib import Path

from factory.core.event_bus import EventBus
from factory.state.build_state import create_build_state


def _make_temp_output() -> Path:
    tmp = tempfile.mkdtemp()
    return Path(tmp)


def test_event_bus_creates_events_file():
    output_dir = _make_temp_output()
    bus = EventBus(output_dir)
    assert bus.events_path.is_file()


def test_emit_event_writes_ndjson():
    output_dir = _make_temp_output()
    bus = EventBus(output_dir)
    bus.emit_event("test_stage", "OK", "hello world")
    lines = bus.events_path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 1
    event = json.loads(lines[0])
    assert event["stage"] == "test_stage"
    assert event["status"] == "OK"
    assert event["message"] == "hello world"


def test_emit_multiple_events_appends():
    output_dir = _make_temp_output()
    bus = EventBus(output_dir)
    bus.emit_event("stage1", "RUN", "starting")
    bus.emit_event("stage1", "OK", "done")
    bus.emit_event("stage2", "RUN", "next")
    lines = bus.events_path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 3


def test_emit_event_includes_timestamp():
    output_dir = _make_temp_output()
    bus = EventBus(output_dir)
    bus.emit_event("s", "OK", "msg")
    event = json.loads(bus.events_path.read_text(encoding="utf-8").strip())
    assert "timestamp" in event
    assert "Z" in event["timestamp"]


def test_emit_event_updates_build_state_json():
    output_dir = _make_temp_output()
    state = create_build_state(output_dir, soc="mtk", edition="Stable")
    bus = EventBus(output_dir, state)
    bus.emit_event("rom_detect", "OK", "detected", progress=15.0, file="payload.bin")
    state_path = output_dir / "state" / "build_state.json"
    assert state_path.is_file()
    data = json.loads(state_path.read_text(encoding="utf-8"))
    assert data["current_stage"] == "rom_detect"
    assert data["current_action"] == "detected"
    assert data["last_file"] == "payload.bin"
    assert data["progress"] == 15.0


def test_emit_fail_event_sets_state_failed():
    output_dir = _make_temp_output()
    state = create_build_state(output_dir)
    bus = EventBus(output_dir, state)
    bus.emit_event("super", "FAIL", "lpmake exploded")
    state_path = output_dir / "state" / "build_state.json"
    data = json.loads(state_path.read_text(encoding="utf-8"))
    assert data["status"] == "FAILED"
    assert any("lpmake exploded" in e for e in data["errors"])


def test_emit_ok_advances_progress():
    output_dir = _make_temp_output()
    state = create_build_state(output_dir)
    bus = EventBus(output_dir, state)
    bus.emit_event("prepare", "OK", "workspace ready")
    p1 = state.progress
    bus.emit_event("unpack", "OK", "payload extracted")
    p2 = state.progress
    assert p2 > p1


def test_read_recent_events():
    output_dir = _make_temp_output()
    bus = EventBus(output_dir)
    for i in range(25):
        bus.emit_event(f"stage_{i}", "OK", f"msg {i}")
    recent = bus.read_recent_events(10)
    assert len(recent) == 10
    assert recent[-1]["stage"] == "stage_24"


def test_copy_events_to():
    output_dir = _make_temp_output()
    bus = EventBus(output_dir)
    bus.emit_event("s", "OK", "test")
    dst = output_dir / "reports" / "live_events.ndjson"
    bus.copy_events_to(dst)
    assert dst.is_file()
    assert dst.read_text() == bus.events_path.read_text()
