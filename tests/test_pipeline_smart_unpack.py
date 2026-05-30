"""
Phase 5 pipeline-wiring tests.

Verifies that deadzone_smart_unpack is the canonical unpack entry used by
the real build pipeline and that the compatibility layer in unpacker.py
behaves correctly.

Coverage:
 1.  _run_build unpack stage calls deadzone_smart_unpack (not the old adapters)
 2.  unpack_rom delegates to deadzone_smart_unpack (compatibility path)
 3.  smart_unpack result populates expected workspace metadata
 4.  unsupported input fails cleanly with a clear error message
 5.  original ROM input is preserved after pipeline unpack stage
 6.  selected route appears in build report and build summary
 7.  event bus receives smart_unpack stage events
 8.  Telegram add_event is called with smart_unpack route if telegram is active
 9.  no HyperUR runtime import in new pipeline wiring (deadzone.py / unpacker.py)
10.  no mod/smali/UI keywords in new pipeline wiring
11.  existing Phase 1–4 imports still resolvable (smoke test)
12.  unpack_rom raises RuntimeError for FAILED smart_unpack status
13.  unpack_rom raises RuntimeError for UNSUPPORTED smart_unpack status
14.  smart_unpack.json is written to ws.meta during pipeline unpack stage
15.  deadzone_smart_unpack_report.txt is written during pipeline unpack stage
"""
from __future__ import annotations

import ast
import json
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, call, patch

import pytest

from factory.core.smart_unpack import (
    ROUTE_PAYLOAD,
    ROUTE_UNSUPPORTED,
    deadzone_smart_unpack,
)
from factory.core.workspace import create_workspace


# ── Helpers ────────────────────────────────────────────────────────────────────

def _make_ws(tmp_path: Path):
    return create_workspace(tmp_path / "workspace")


def _make_zip_with_payload(tmp_path: Path, name: str = "rom.zip") -> Path:
    import struct
    rom = tmp_path / name
    manifest = b"\x00" * 4
    sig_len = 4
    header = struct.pack(">4sQQI", b"CrAU", 2, len(manifest), sig_len)
    payload_bytes = header + manifest + b"\x00" * sig_len
    with zipfile.ZipFile(rom, "w") as zf:
        zf.writestr("payload.bin", payload_bytes)
        zf.writestr("payload_properties.txt", "FILE_HASH=abc\n")
    return rom


def _make_image_folder(tmp_path: Path) -> Path:
    folder = tmp_path / "images"
    folder.mkdir(exist_ok=True)
    for part in ("system", "product", "vendor"):
        (folder / f"{part}.img").write_bytes(b"\x00" * 512)
    return folder


def _ok_smart_unpack_result(ws, route: str = "image_folder") -> dict[str, Any]:
    """Minimal smart_unpack result dict with OK status."""
    images = {p: str(ws.images / f"{p}.img") for p in ("system", "product", "vendor")}
    for p in ("system_ext", "odm", "mi_ext", "system_dlkm", "vendor_dlkm"):
        images[p] = None
    for p in ("system", "product", "vendor"):
        (ws.images / f"{p}.img").write_bytes(b"\x00" * 128)
    return {
        "input_path": str(ws.root / "rom.zip"),
        "input_type": "folder",
        "route": route,
        "route_reason": "folder contains .img files",
        "status": "OK",
        "payload_path": None,
        "super_img": None,
        "images": images,
        "partitions": {"system": None, "product": None, "vendor": None},
        "missing_required": [],
        "missing_optional": ["system_ext", "odm", "mi_ext", "system_dlkm", "vendor_dlkm"],
        "reports": [],
        "error": "",
        "elapsed_seconds": 0.01,
    }


def _failed_smart_unpack_result() -> dict[str, Any]:
    return {
        "input_path": "/tmp/rom.zip",
        "input_type": "unknown",
        "route": "unsupported",
        "route_reason": "input path does not exist",
        "status": "FAILED",
        "payload_path": None,
        "super_img": None,
        "images": {p: None for p in ("system", "product", "vendor",
                                      "system_ext", "odm", "mi_ext",
                                      "system_dlkm", "vendor_dlkm")},
        "partitions": {"system": None, "product": None, "vendor": None},
        "missing_required": ["product", "system", "vendor"],
        "missing_optional": [],
        "reports": [],
        "error": "smart unpack route 'unsupported' returned status: FAILED",
        "elapsed_seconds": 0.0,
    }


# ── 1. _run_build unpack stage calls deadzone_smart_unpack ────────────────────

def test_run_build_unpack_stage_calls_deadzone_smart_unpack(tmp_path):
    """The _run_smart_unpack_stage helper calls deadzone_smart_unpack."""
    import factory.deadzone as dz

    ws = _make_ws(tmp_path)

    @dataclass
    class FakeCtx:
        rom_source: Path = field(default_factory=lambda: tmp_path / "rom.zip")
        smart_unpack_result: dict = field(default_factory=dict)
        smart_unpack_route: str = ""
        event_bus: Any = None
        telegram: Any = None
        telegram_result: Any = None

    ctx = FakeCtx()

    with patch("factory.deadzone.deadzone_smart_unpack") as mock_su:
        mock_su.return_value = _ok_smart_unpack_result(ws)
        result = dz._run_smart_unpack_stage(ctx, ws)

    mock_su.assert_called_once_with(ctx.rom_source, ws)
    assert result["status"] == "OK"
    assert ctx.smart_unpack_route == "image_folder"


def test_run_smart_unpack_stage_stores_route_on_ctx(tmp_path):
    """_run_smart_unpack_stage stores smart_unpack_route on the context."""
    import factory.deadzone as dz

    ws = _make_ws(tmp_path)

    @dataclass
    class FakeCtx:
        rom_source: Path = field(default_factory=lambda: tmp_path / "rom.zip")
        smart_unpack_result: dict = field(default_factory=dict)
        smart_unpack_route: str = ""
        event_bus: Any = None
        telegram: Any = None
        telegram_result: Any = None

    ctx = FakeCtx()
    ok_result = _ok_smart_unpack_result(ws, route="payload")

    with patch("factory.deadzone.deadzone_smart_unpack", return_value=ok_result):
        dz._run_smart_unpack_stage(ctx, ws)

    assert ctx.smart_unpack_route == "payload"
    assert ctx.smart_unpack_result["route"] == "payload"


# ── 2. unpack_rom delegates to deadzone_smart_unpack ─────────────────────────

def test_unpack_rom_delegates_to_deadzone_smart_unpack(tmp_path):
    """unpack_rom must call deadzone_smart_unpack internally."""
    from factory.core.unpacker import unpack_rom
    from factory.core.detector import RomInfo

    ws = _make_ws(tmp_path)
    rom = tmp_path / "rom.zip"
    rom.write_bytes(b"fake")
    info = MagicMock(spec=RomInfo)

    ok_result = _ok_smart_unpack_result(ws)

    # The import is inside unpack_rom via 'from factory.core.smart_unpack import ...'
    # so we patch the function at its canonical location in the smart_unpack module.
    with patch("factory.core.smart_unpack.deadzone_smart_unpack", return_value=ok_result) as mock_su:
        result = unpack_rom(rom, info, ws)

    mock_su.assert_called_once_with(rom, ws)
    assert result["adapter"].startswith("smart_unpack:")
    assert isinstance(result["images"], list)
    assert result["partition_sizes"] == {}
    assert "smart_unpack" in result


def test_unpack_rom_writes_unpack_result_json(tmp_path):
    """unpack_rom writes unpack_result.json to ws.meta."""
    from factory.core.unpacker import unpack_rom
    from factory.core.detector import RomInfo

    ws = _make_ws(tmp_path)
    rom = tmp_path / "rom.zip"
    rom.write_bytes(b"fake")
    info = MagicMock(spec=RomInfo)

    with patch("factory.core.smart_unpack.deadzone_smart_unpack", return_value=_ok_smart_unpack_result(ws)):
        unpack_rom(rom, info, ws)

    assert (ws.meta / "unpack_result.json").is_file()


# ── 3. smart_unpack result populates workspace metadata ──────────────────────

def test_smart_unpack_json_written_during_unpack(tmp_path):
    """deadzone_smart_unpack writes smart_unpack.json to ws.meta during the unpack stage."""
    ws = _make_ws(tmp_path)
    folder = _make_image_folder(tmp_path)

    deadzone_smart_unpack(folder, ws)

    meta_file = ws.meta / "smart_unpack.json"
    assert meta_file.is_file()
    data = json.loads(meta_file.read_text())
    assert "route" in data
    assert "status" in data
    assert "images" in data


def test_smart_unpack_report_written_during_unpack(tmp_path):
    """deadzone_smart_unpack writes deadzone_smart_unpack_report.txt during the unpack stage."""
    ws = _make_ws(tmp_path)
    folder = _make_image_folder(tmp_path)

    deadzone_smart_unpack(folder, ws)

    report = ws.reports / "deadzone_smart_unpack_report.txt"
    assert report.is_file()
    content = report.read_text()
    assert "route" in content
    assert "status" in content


def test_workspace_images_populated_after_smart_unpack(tmp_path):
    """After deadzone_smart_unpack, ws.images contains at least one non-null image path."""
    ws = _make_ws(tmp_path)
    folder = _make_image_folder(tmp_path)

    result = deadzone_smart_unpack(folder, ws)

    images = result.get("images") or {}
    found = [v for v in images.values() if v]
    assert found, "No images found after smart_unpack over image folder"


# ── 4. Unsupported input fails cleanly ───────────────────────────────────────

def test_unsupported_input_fails_with_clear_error(tmp_path):
    """_run_smart_unpack_stage raises RuntimeError with a clear message for unsupported input."""
    import factory.deadzone as dz

    ws = _make_ws(tmp_path)

    @dataclass
    class FakeCtx:
        rom_source: Path = field(default_factory=lambda: tmp_path / "rom.zip")
        smart_unpack_result: dict = field(default_factory=dict)
        smart_unpack_route: str = ""
        event_bus: Any = None
        telegram: Any = None
        telegram_result: Any = None

    ctx = FakeCtx()

    failed = _failed_smart_unpack_result()
    with patch("factory.deadzone.deadzone_smart_unpack", return_value=failed):
        with pytest.raises(RuntimeError) as exc_info:
            dz._run_smart_unpack_stage(ctx, ws)

    msg = str(exc_info.value)
    assert msg  # message is not empty
    # Should mention the missing partitions or status
    assert "FAILED" in msg or "missing" in msg or "unsupported" in msg.lower()


def test_unsupported_status_does_not_leave_ws_corrupted(tmp_path):
    """When smart_unpack returns UNSUPPORTED, workspace meta still contains smart_unpack.json."""
    ws = _make_ws(tmp_path)
    # Empty folder → UNSUPPORTED route
    empty = tmp_path / "empty"
    empty.mkdir()

    result = deadzone_smart_unpack(empty, ws)

    assert result["status"] in ("UNSUPPORTED", "FAILED")
    assert (ws.meta / "smart_unpack.json").is_file()
    assert (ws.reports / "deadzone_smart_unpack_report.txt").is_file()


def test_unpack_rom_raises_for_failed_status(tmp_path):
    """unpack_rom raises RuntimeError when deadzone_smart_unpack returns FAILED."""
    from factory.core.unpacker import unpack_rom
    from factory.core.detector import RomInfo

    ws = _make_ws(tmp_path)
    rom = tmp_path / "rom.zip"
    rom.write_bytes(b"fake")
    info = MagicMock(spec=RomInfo)

    with patch("factory.core.smart_unpack.deadzone_smart_unpack", return_value=_failed_smart_unpack_result()):
        with pytest.raises(RuntimeError) as exc_info:
            unpack_rom(rom, info, ws)

    assert "[UNPACK]" in str(exc_info.value)


def test_unpack_rom_raises_for_unsupported_status(tmp_path):
    """unpack_rom raises RuntimeError when deadzone_smart_unpack returns UNSUPPORTED."""
    from factory.core.unpacker import unpack_rom
    from factory.core.detector import RomInfo

    ws = _make_ws(tmp_path)
    rom = tmp_path / "rom.zip"
    rom.write_bytes(b"fake")
    info = MagicMock(spec=RomInfo)

    unsupported = _failed_smart_unpack_result()
    unsupported["status"] = "UNSUPPORTED"
    with patch("factory.core.smart_unpack.deadzone_smart_unpack", return_value=unsupported):
        with pytest.raises(RuntimeError):
            unpack_rom(rom, info, ws)


# ── 5. Original ROM input is preserved ───────────────────────────────────────

def test_original_rom_preserved_by_smart_unpack(tmp_path):
    """deadzone_smart_unpack never deletes or modifies the original ROM input."""
    ws = _make_ws(tmp_path)
    folder = _make_image_folder(tmp_path)
    original_files = {p: p.read_bytes() for p in folder.iterdir() if p.is_file()}

    deadzone_smart_unpack(folder, ws)

    for p, original_bytes in original_files.items():
        assert p.is_file(), f"{p.name} was deleted"
        assert p.read_bytes() == original_bytes, f"{p.name} was modified"


def test_unpack_rom_does_not_delete_source(tmp_path):
    """unpack_rom never deletes the source ROM input."""
    from factory.core.unpacker import unpack_rom
    from factory.core.detector import RomInfo

    ws = _make_ws(tmp_path)
    rom = tmp_path / "rom.zip"
    rom.write_bytes(b"fakecontent" * 100)
    original_bytes = rom.read_bytes()
    info = MagicMock(spec=RomInfo)

    with patch("factory.core.smart_unpack.deadzone_smart_unpack", return_value=_ok_smart_unpack_result(ws)):
        unpack_rom(rom, info, ws)

    assert rom.is_file(), "Source ROM was deleted"
    assert rom.read_bytes() == original_bytes, "Source ROM was modified"


# ── 6. Route appears in build report and build summary ───────────────────────

def test_build_report_includes_smart_unpack_route(tmp_path):
    """write_production_reports includes the smart_unpack_route in build_report.txt."""
    from factory.core.reports import write_production_reports
    from factory.core.workspace import create_workspace

    ws = create_workspace(tmp_path / "ws")

    @dataclass
    class FakeCtx:
        rom_url: str = "http://example.com/rom.zip"
        smart_unpack_route: str = "payload"
        smart_unpack_result: dict = field(default_factory=dict)
        rom_metadata: Any = None
        device_profile: dict = field(default_factory=dict)
        final_zip_path: Any = None
        cleanup_status: str = "not run"
        upload_result: Any = None
        telegram_result: Any = None
        status: str = "OK"
        failed_stage: str = ""
        started_at: float = 0.0
        completed_at: float = 1.0
        started_stage: str = "unpack"
        completed_stage: str = "unpack"
        selected_codename: str = ""
        style_label: str = "Stable"
        soc: str = "mtk"
        mode: str = "build"
        stages: list = field(default_factory=list)
        warnings: list = field(default_factory=list)
        build_id: str = "test-123"
        tracker: Any = None
        build_state: Any = None
        app_inventory: dict = field(default_factory=dict)
        app_inventory_zip_path: Any = None
        stable_normalize: dict = field(default_factory=dict)
        image_extraction: dict = field(default_factory=dict)
        generate_app_inventory: bool = False
        notify_telegram: bool = False

    ctx = FakeCtx()
    reports = write_production_reports(ctx, ws)

    build_report = Path(reports["build"]).read_text()
    assert "smart unpack route" in build_report
    assert "payload" in build_report


def test_build_summary_json_includes_smart_unpack_route(tmp_path):
    """write_production_reports includes smart_unpack_route in build_summary.json."""
    from factory.core.reports import write_production_reports
    from factory.core.workspace import create_workspace

    ws = create_workspace(tmp_path / "ws")

    @dataclass
    class FakeCtx:
        rom_url: str = "http://example.com/rom.zip"
        smart_unpack_route: str = "fastboot_images"
        smart_unpack_result: dict = field(default_factory=dict)
        rom_metadata: Any = None
        device_profile: dict = field(default_factory=dict)
        final_zip_path: Any = None
        cleanup_status: str = "not run"
        upload_result: Any = None
        telegram_result: Any = None
        status: str = "OK"
        failed_stage: str = ""
        started_at: float = 0.0
        completed_at: float = 1.0
        started_stage: str = "unpack"
        completed_stage: str = "unpack"
        selected_codename: str = ""
        style_label: str = "Stable"
        soc: str = "snapdragon"
        mode: str = "build"
        stages: list = field(default_factory=list)
        warnings: list = field(default_factory=list)
        build_id: str = "test-456"
        tracker: Any = None
        build_state: Any = None
        app_inventory: dict = field(default_factory=dict)
        app_inventory_zip_path: Any = None
        stable_normalize: dict = field(default_factory=dict)
        image_extraction: dict = field(default_factory=dict)
        generate_app_inventory: bool = False
        notify_telegram: bool = False

    ctx = FakeCtx()
    reports = write_production_reports(ctx, ws)

    summary = json.loads(Path(reports["build_summary_json"]).read_text())
    assert "smart_unpack_route" in summary
    assert summary["smart_unpack_route"] == "fastboot_images"


def test_build_summary_txt_includes_smart_unpack_route(tmp_path):
    """build_summary.txt includes the smart_unpack_route line."""
    from factory.core.reports import write_production_reports
    from factory.core.workspace import create_workspace

    ws = create_workspace(tmp_path / "ws")

    @dataclass
    class FakeCtx:
        rom_url: str = "http://example.com/rom.zip"
        smart_unpack_route: str = "super"
        smart_unpack_result: dict = field(default_factory=dict)
        rom_metadata: Any = None
        device_profile: dict = field(default_factory=dict)
        final_zip_path: Any = None
        cleanup_status: str = "not run"
        upload_result: Any = None
        telegram_result: Any = None
        status: str = "FAILED"
        failed_stage: str = "unpack"
        started_at: float = 0.0
        completed_at: float = 1.0
        started_stage: str = "unpack"
        completed_stage: str = ""
        selected_codename: str = ""
        style_label: str = "Legend"
        soc: str = "mtk"
        mode: str = "build"
        stages: list = field(default_factory=list)
        warnings: list = field(default_factory=list)
        build_id: str = "test-789"
        tracker: Any = None
        build_state: Any = None
        app_inventory: dict = field(default_factory=dict)
        app_inventory_zip_path: Any = None
        stable_normalize: dict = field(default_factory=dict)
        image_extraction: dict = field(default_factory=dict)
        generate_app_inventory: bool = False
        notify_telegram: bool = False

    ctx = FakeCtx()
    reports = write_production_reports(ctx, ws)

    summary_txt = Path(reports["build_summary"]).read_text()
    assert "smart_unpack_route" in summary_txt
    assert "super" in summary_txt


# ── 7. Event bus receives smart_unpack stage events ──────────────────────────

def test_event_bus_receives_smart_unpack_run_event(tmp_path):
    """_run_smart_unpack_stage emits a 'smart_unpack' RUN event to the event bus."""
    import factory.deadzone as dz

    ws = _make_ws(tmp_path)
    mock_bus = MagicMock()

    @dataclass
    class FakeCtx:
        rom_source: Path = field(default_factory=lambda: tmp_path / "rom.zip")
        smart_unpack_result: dict = field(default_factory=dict)
        smart_unpack_route: str = ""
        event_bus: Any = None
        telegram: Any = None
        telegram_result: Any = None

    ctx = FakeCtx(event_bus=mock_bus)

    with patch("factory.deadzone.deadzone_smart_unpack", return_value=_ok_smart_unpack_result(ws)):
        dz._run_smart_unpack_stage(ctx, ws)

    run_calls = [c for c in mock_bus.emit_event.call_args_list if c.args[1] == "RUN"]
    ok_calls = [c for c in mock_bus.emit_event.call_args_list if c.args[1] == "OK"]
    assert any(c.args[0] == "smart_unpack" for c in run_calls), "No RUN event emitted for smart_unpack"
    assert any(c.args[0] == "smart_unpack" for c in ok_calls), "No OK event emitted for smart_unpack"


def test_event_bus_receives_smart_unpack_fail_event(tmp_path):
    """_run_smart_unpack_stage emits a 'smart_unpack' FAIL event on failure."""
    import factory.deadzone as dz

    ws = _make_ws(tmp_path)
    mock_bus = MagicMock()

    @dataclass
    class FakeCtx:
        rom_source: Path = field(default_factory=lambda: tmp_path / "rom.zip")
        smart_unpack_result: dict = field(default_factory=dict)
        smart_unpack_route: str = ""
        event_bus: Any = None
        telegram: Any = None
        telegram_result: Any = None

    ctx = FakeCtx(event_bus=mock_bus)

    with patch("factory.deadzone.deadzone_smart_unpack", return_value=_failed_smart_unpack_result()):
        with pytest.raises(RuntimeError):
            dz._run_smart_unpack_stage(ctx, ws)

    fail_calls = [c for c in mock_bus.emit_event.call_args_list if c.args[1] == "FAIL"]
    assert any(c.args[0] == "smart_unpack" for c in fail_calls), "No FAIL event emitted for smart_unpack"


# ── 8. Telegram add_event called with smart_unpack route ─────────────────────

def test_telegram_receives_smart_unpack_route_on_success(tmp_path):
    """_run_smart_unpack_stage calls telegram.add_event with the unpack route."""
    import factory.deadzone as dz

    ws = _make_ws(tmp_path)
    mock_telegram = MagicMock()
    mock_telegram.add_event.return_value = MagicMock()

    @dataclass
    class FakeCtx:
        rom_source: Path = field(default_factory=lambda: tmp_path / "rom.zip")
        smart_unpack_result: dict = field(default_factory=dict)
        smart_unpack_route: str = ""
        event_bus: Any = None
        telegram: Any = None
        telegram_result: Any = None

    ctx = FakeCtx(telegram=mock_telegram)
    ok_result = _ok_smart_unpack_result(ws, route="payload")

    with patch("factory.deadzone.deadzone_smart_unpack", return_value=ok_result):
        dz._run_smart_unpack_stage(ctx, ws)

    calls = mock_telegram.add_event.call_args_list
    assert calls, "telegram.add_event was never called"
    # One of the calls must mention the route
    route_mentioned = any("payload" in str(c) for c in calls)
    assert route_mentioned, f"Route 'payload' not mentioned in any Telegram call: {calls}"


# ── 9. No HyperUR runtime import in new wiring ───────────────────────────────

_PIPELINE_FILES = [
    "factory/deadzone.py",
    "factory/core/unpacker.py",
]


@pytest.mark.parametrize("filepath", _PIPELINE_FILES)
def test_no_hyperur_import_in_pipeline_file(filepath):
    """Pipeline wiring files must not import HyperURBuild or any src.* module."""
    source = Path(filepath).read_text(encoding="utf-8")
    assert "HyperURBuild" not in source, f"{filepath} imports HyperURBuild"
    assert "from src." not in source, f"{filepath} imports from src.*"
    assert "import src." not in source, f"{filepath} imports from src.*"


# ── 10. No mod/smali/UI keywords in new pipeline wiring ──────────────────────

_FORBIDDEN_PIPELINE_KEYWORDS = frozenset({
    "smali", "baksmali", "apktool",
    "MiuiSystemUI", "Provision", "Wukong", "USAGI_UI",
    "flag_secure", "signature_bypass",
    "framework_jar", "services_jar",
    "clock_style", "icon_style",
})


def test_deadzone_smart_unpack_stage_helper_has_no_mod_keywords():
    """The _run_smart_unpack_stage function source must not reference mod/smali/UI symbols."""
    source = Path("factory/deadzone.py").read_text(encoding="utf-8").lower()
    # Only check lines that belong to _run_smart_unpack_stage
    in_helper = False
    lines: list[str] = []
    for line in source.splitlines():
        if "def _run_smart_unpack_stage" in line:
            in_helper = True
        elif in_helper and line.startswith("def ") and "_run_smart_unpack_stage" not in line:
            break
        if in_helper:
            lines.append(line)
    helper_source = "\n".join(lines)
    for kw in _FORBIDDEN_PIPELINE_KEYWORDS:
        assert kw.lower() not in helper_source, (
            f"_run_smart_unpack_stage references forbidden keyword: {kw!r}"
        )


def test_unpacker_delegate_has_no_mod_keywords():
    """The new unpack_rom body must not reference mod/smali/UI symbols."""
    source = Path("factory/core/unpacker.py").read_text(encoding="utf-8").lower()
    for kw in _FORBIDDEN_PIPELINE_KEYWORDS:
        assert kw.lower() not in source, (
            f"unpacker.py references forbidden keyword: {kw!r}"
        )


# ── 11. Existing Phase 1–4 imports still resolvable ──────────────────────────

def test_phase1_rom_intake_still_importable():
    from factory.core.rom_intake import deadzone_rom_intake  # noqa: F401


def test_phase2_detector_still_importable():
    from factory.core.detector import detect_rom, RomInfo  # noqa: F401


def test_phase3_payload_extract_still_importable():
    from factory.core.payload_extract import deadzone_payload_extract_stage  # noqa: F401


def test_phase4_smart_unpack_still_importable():
    from factory.core.smart_unpack import deadzone_smart_unpack  # noqa: F401


def test_deadzone_pipeline_still_importable():
    import factory.deadzone  # noqa: F401


# ── 12–13. unpack_rom error paths (covered above, extra guard) ────────────────

def test_unpack_rom_error_message_mentions_missing_partitions(tmp_path):
    """RuntimeError from unpack_rom mentions missing required partitions."""
    from factory.core.unpacker import unpack_rom
    from factory.core.detector import RomInfo

    ws = _make_ws(tmp_path)
    rom = tmp_path / "rom.zip"
    rom.write_bytes(b"fake")
    info = MagicMock(spec=RomInfo)

    failed = _failed_smart_unpack_result()
    failed["missing_required"] = ["product", "system", "vendor"]
    with patch("factory.core.smart_unpack.deadzone_smart_unpack", return_value=failed):
        with pytest.raises(RuntimeError) as exc_info:
            unpack_rom(rom, info, ws)

    msg = str(exc_info.value)
    assert "missing" in msg.lower() or "product" in msg or "system" in msg


# ── 14. smart_unpack.json in ws.meta after smart_unpack ──────────────────────

def test_smart_unpack_json_has_required_keys_from_image_folder(tmp_path):
    """smart_unpack.json from an image_folder run has all required top-level keys."""
    ws = _make_ws(tmp_path)
    folder = _make_image_folder(tmp_path)

    deadzone_smart_unpack(folder, ws)

    data = json.loads((ws.meta / "smart_unpack.json").read_text())
    for key in ("input_path", "input_type", "route", "status", "images",
                "partitions", "missing_required", "missing_optional", "reports"):
        assert key in data, f"smart_unpack.json missing key: {key!r}"
    assert data["route"] == "image_folder"


# ── 15. deadzone_smart_unpack_report.txt in ws.reports ───────────────────────

def test_smart_unpack_report_contains_route(tmp_path):
    """deadzone_smart_unpack_report.txt contains the route name."""
    ws = _make_ws(tmp_path)
    folder = _make_image_folder(tmp_path)

    deadzone_smart_unpack(folder, ws)

    content = (ws.reports / "deadzone_smart_unpack_report.txt").read_text()
    assert "image_folder" in content
    assert "no mods executed" in content
    assert "compatibility note" in content
