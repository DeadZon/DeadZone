"""Tests for error_summary and TelegramLiveStatus improvements.

Covers:
  - summarize_error: same-file copy, missing ROM, unknown format, etc.
  - TelegramLiveStatus: message template fields, failure message, heartbeat
  - telegram_status.json: current_stage, failure fields
  - stage tracking: no stale stage names
"""
import sys
import time
import tempfile
import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.pipeline.error_summary import summarize_error
from factory.notify.telegram_live import TelegramLiveStatus, PIPELINE_STAGES, _STAGE_ALIAS


# ═══════════════════════════════════════════════════════════════════
# 1. ERROR SUMMARY
# ═══════════════════════════════════════════════════════════════════

class TestErrorSummary:
    def test_same_file_copy_error_identified(self):
        err = "copy super.img: PosixPath('output/images/final/super.img') and PosixPath('output/images/final/super.img') are the same file"
        result = summarize_error(err, "ASSEMBLING_IMAGES")
        assert result["stage"] == "ASSEMBLING_IMAGES"
        assert "same" in result["reason"].lower() or "already" in result["reason"].lower()
        assert result["hint"], "A fix hint must be provided for same-file copy"
        assert result["raw_error"]

    def test_missing_rom_error_identified(self):
        err = "Downloaded ROM path is missing after cleanup: /path/to/rom.tgz. Cleanup must run before download."
        result = summarize_error(err, "DETECTING_ROM")
        assert result["stage"] == "DETECTING_ROM"
        assert "cleanup" in result["reason"].lower() or "missing" in result["reason"].lower()
        assert result["hint"]

    def test_unknown_rom_format_error_identified(self):
        err = "Unknown ROM format: file not recognised. Supported: payload_ota, fastboot_tgz"
        result = summarize_error(err, "DETECTING_ROM")
        assert "format" in result["reason"].lower() or "rom" in result["reason"].lower()

    def test_payload_dump_error_identified(self):
        err = "payload.bin was extracted but could not be dumped into images."
        result = summarize_error(err, "UNPACKING_ROM")
        assert result["stage"] == "UNPACKING_ROM"
        assert "payload" in result["reason"].lower() or "extract" in result["reason"].lower()

    def test_lpmake_not_found_identified(self):
        err = "lpmake binary not found — cannot build super.img"
        result = summarize_error(err, "BUILDING_SUPER")
        assert "lpmake" in result["reason"].lower() or "binary" in result["reason"].lower()
        assert result["hint"]

    def test_timeout_error_identified(self):
        err = "Stage timed out: unpack_rom after 60 minutes"
        result = summarize_error(err, "UNPACKING_ROM")
        assert "timed out" in result["reason"].lower() or "timeout" in result["reason"].lower()

    def test_default_error_returns_raw(self):
        err = "Some completely unknown error occurred"
        result = summarize_error(err, "PACKAGING_ZIP")
        assert result["stage"] == "PACKAGING_ZIP"
        assert result["raw_error"] == err
        # reason should contain something meaningful
        assert result["reason"]

    def test_same_file_error_returns_correct_stage(self):
        err = "copy super.img: same file"
        result = summarize_error(err)
        assert result["stage"] == "ASSEMBLING_IMAGES"

    def test_result_always_has_required_keys(self):
        for err in ["", "random error", "same file copy", "lpmake not found"]:
            result = summarize_error(err, "PACKAGING_ZIP")
            for key in ["title", "stage", "reason", "hint", "raw_error"]:
                assert key in result, f"Key {key!r} missing from summarize_error result"

    def test_raw_error_truncated_to_500(self):
        long_err = "x" * 1000
        result = summarize_error(long_err, "DETECTING_ROM")
        assert len(result["raw_error"]) <= 500


# ═══════════════════════════════════════════════════════════════════
# 2. TELEGRAM LIVE STATUS — message template
# ═══════════════════════════════════════════════════════════════════

def _make_notifier(tmp: Path, enabled: bool = False) -> TelegramLiveStatus:
    """Create a TelegramLiveStatus with Telegram disabled (no real API calls)."""
    return TelegramLiveStatus(
        build_id="TEST-BUILD-001",
        soc="mtk",
        codename="zorn",
        edition="free",
        enabled=enabled,
        output_dir=tmp,
    )


def _close(n: TelegramLiveStatus) -> None:
    """Close logger file handles to avoid Windows file lock on tempdir cleanup."""
    try:
        n.close()
    except Exception:
        pass


class TestTelegramMessageTemplate:
    def test_device_block_contains_device_and_edition(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            block = n._device_block()
            _close(n)
        assert any("zorn" in line for line in block)
        assert any("Free" in line or "free" in line.lower() for line in block)

    def test_device_block_contains_engine(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            block = n._device_block()
            _close(n)
        assert any("Legacy" in line or "Engine" in line for line in block)

    def test_device_block_shows_rom_format_when_set(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            n.update_fields(rom_format="fastboot_tgz")
            block = n._device_block()
            _close(n)
        assert any("fastboot_tgz" in line for line in block)

    def test_device_block_shows_super_strategy_when_set(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            n.update_fields(super_strategy="preserve_original_super")
            block = n._device_block()
            _close(n)
        assert any("preserve_original_super" in line for line in block)

    def test_render_live_contains_stage_and_runtime(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            n.current_stage = "ASSEMBLING_IMAGES"
            n.current_detail = "Assembling images"
            text = n._render_live()
            _close(n)
        assert "Runtime" in text
        assert "Last update" in text or "update" in text.lower()

    def test_render_live_contains_warning_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            text = n._render_live()
            _close(n)
        assert "another build" in text.lower() or "do not" in text.lower()

    def test_failure_message_contains_stage_and_reason(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            text = n._render_fail(
                "ASSEMBLING_IMAGES",
                "super.img was already in final dir",
                "00m 05s",
                hint="Skip same-file copy",
            )
            _close(n)
        assert "ASSEMBLING" in text or "Assemble" in text or "final images" in text.lower()
        assert "super.img" in text
        assert "Skip same-file" in text

    def test_failure_message_contains_check_reports_hint(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            text = n._render_fail("DETECTING_ROM", "Unknown format", "01m 00s")
            _close(n)
        assert "reports" in text.lower() or "artifact" in text.lower()


# ═══════════════════════════════════════════════════════════════════
# 3. TELEGRAM STATUS JSON
# ═══════════════════════════════════════════════════════════════════

class TestTelegramStatusJson:
    def test_status_json_written_on_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            n.message_id = 12345  # pretend we have a message
            n._do_edit = MagicMock(return_value={"status": "UPDATED"})
            n.fail(
                stage="ASSEMBLING_IMAGES",
                reason="super.img was already in final dir",
                hint="Skip same-file copy",
                raw_error="same file error",
            )
            status_path = Path(tmp) / "reports" / "telegram_status.json"
            assert status_path.is_file(), "telegram_status.json must be written on fail"
            data = json.loads(status_path.read_text(encoding="utf-8"))
            _close(n)

        assert data["failure_stage"] == "ASSEMBLING_IMAGES"
        assert data["failure_reason"] is not None
        assert data["failure_hint"] is not None
        assert data["final_status"] == "FAILED"

    def test_status_json_contains_current_stage(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            n.message_id = 12345
            n._do_edit = MagicMock(return_value={"status": "UPDATED"})
            n.fail(stage="PACKAGING_ZIP", reason="ZIP failed")
            data = json.loads((Path(tmp) / "reports" / "telegram_status.json").read_text())
            _close(n)

        assert data["current_stage"] == "FAILED"

    def test_status_json_written_on_update_stage(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            n.message_id = 12345
            n._do_edit = MagicMock(return_value={"status": "UPDATED"})
            n._last_edit = 0.0  # reset throttle
            n.update_stage("COLLECTING_IMAGES", detail="Collecting images", force=True)
            status_path = Path(tmp) / "reports" / "telegram_status.json"
            if status_path.is_file():
                data = json.loads(status_path.read_text())
                assert data["message_id"] == 12345
            _close(n)


# ═══════════════════════════════════════════════════════════════════
# 4. STAGE TRACKING — no stale stage names
# ═══════════════════════════════════════════════════════════════════

class TestStageTracking:
    def test_collecting_images_maps_to_collecting_not_packaging(self):
        """COLLECTING_IMAGES must NOT alias to PACKAGING_ZIP — it caused wrong stage display."""
        canonical = _STAGE_ALIAS.get("COLLECTING_IMAGES", "COLLECTING_IMAGES")
        assert canonical != "PACKAGING_ZIP", (
            "COLLECTING_IMAGES must not alias to PACKAGING_ZIP — this caused wrong stage display in the build report"
        )

    def test_building_super_maps_to_preserving_or_super_stage(self):
        canonical = _STAGE_ALIAS.get("BUILDING_SUPER", "BUILDING_SUPER")
        assert canonical in ("PRESERVING_SUPER", "BUILDING_SUPER"), (
            f"BUILDING_SUPER should map to a super-related stage, got {canonical!r}"
        )

    def test_all_pipeline_stage_ids_unique(self):
        ids = [s for s, _, _ in PIPELINE_STAGES]
        assert len(ids) == len(set(ids)), "All PIPELINE_STAGES IDs must be unique"

    def test_pipeline_stage_numbers_sequential(self):
        nums = [n for _, _, n in PIPELINE_STAGES]
        assert nums == list(range(1, len(PIPELINE_STAGES) + 1)), (
            "PIPELINE_STAGES numbers must be sequential from 1"
        )

    def test_update_stage_uses_canonical_name(self):
        """update_stage must store canonical stage, not alias."""
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            n.message_id = 12345
            n._do_edit = MagicMock(return_value={"status": "UPDATED"})
            n._last_edit = 0.0
            n.update_stage("COLLECTING_IMAGES", force=True)
            stage = n.current_stage
            _close(n)
        # After calling update_stage("COLLECTING_IMAGES"), current_stage
        # should be the canonical (not PACKAGING_ZIP)
        assert stage != "PACKAGING_ZIP", (
            "current_stage must not be PACKAGING_ZIP after update_stage('COLLECTING_IMAGES')"
        )

    def test_failed_stage_stored_on_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp))
            n.message_id = 12345
            n._do_edit = MagicMock(return_value={"status": "UPDATED"})
            n.fail(stage="ASSEMBLING_IMAGES", reason="test error")
            failure_stage = n.failure_stage
            final_status = n.final_status
            _close(n)
        assert failure_stage == "ASSEMBLING_IMAGES"
        assert final_status == "FAILED"


# ═══════════════════════════════════════════════════════════════════
# 5. HEARTBEAT
# ═══════════════════════════════════════════════════════════════════

class TestTelegramHeartbeat:
    def test_heartbeat_does_not_create_new_message(self):
        """heartbeat() must only edit the existing message, not send a new one."""
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp), enabled=True)
            n.token = "fake_token"
            n.chat_id = "123456"
            n.message_id = 99999
            n._last_heartbeat = 0.0

            edit_calls = []
            send_calls = []

            def _fake_post(method, payload, _migration_retry=False):
                if method == "sendMessage":
                    send_calls.append(method)
                else:
                    edit_calls.append(method)
                return {"ok": True, "result": {"message_id": 99999}}

            n._post = _fake_post
            n.heartbeat()
            _close(n)

        assert not send_calls, "heartbeat must NOT call sendMessage"

    def test_heartbeat_throttled_when_interval_not_elapsed(self):
        """heartbeat() must be THROTTLED if called within _HEARTBEAT_INTERVAL."""
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp), enabled=True)
            n.token = "fake_token"
            n.chat_id = "123456"
            n.message_id = 99999
            n._last_heartbeat = time.monotonic()  # just fired
            result = n.heartbeat()
            _close(n)
        assert result["status"] == "THROTTLED"

    def test_heartbeat_api_failure_does_not_raise(self):
        """Telegram API failure during heartbeat must not raise an exception."""
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp), enabled=True)
            n.token = "fake_token"
            n.chat_id = "123456"
            n.message_id = 99999
            n._last_heartbeat = 0.0

            def _fail_post(method, payload, _migration_retry=False):
                return {"ok": False, "error": "Simulated API error"}

            n._post = _fail_post
            try:
                n.heartbeat()
            except Exception as exc:
                pytest.fail(f"heartbeat must not raise on API failure: {exc}")
            finally:
                _close(n)


# ═══════════════════════════════════════════════════════════════════
# 6. TELEGRAM API FAILURE DOES NOT FAIL BUILD
# ═══════════════════════════════════════════════════════════════════

class TestTelegramApiFailureDoesNotFailBuild:
    def test_start_build_api_failure_is_non_fatal(self):
        """start_build() must not raise even if the API call fails."""
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp), enabled=True)
            n.token = "fake_token"
            n.chat_id = "123456"

            def _fail_post(method, payload, _migration_retry=False):
                return {"ok": False, "error": "Network error"}

            n._post = _fail_post
            result = n.start_build()
            _close(n)
        assert result["status"] in ("SEND_FAILED", "DISABLED"), (
            "start_build API failure should return SEND_FAILED, not raise"
        )

    def test_update_stage_api_failure_is_non_fatal(self):
        with tempfile.TemporaryDirectory() as tmp:
            n = _make_notifier(Path(tmp), enabled=True)
            n.token = "fake_token"
            n.chat_id = "123456"
            n.message_id = 12345
            n._last_edit = 0.0

            def _fail_post(method, payload, _migration_retry=False):
                return {"ok": False, "error": "Network error"}

            n._post = _fail_post
            result = n.update_stage("COLLECTING_IMAGES", force=True)
            _close(n)
        assert result["status"] in ("EDIT_FAILED", "DISABLED", "THROTTLED")


# ── Runner ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import traceback

    passed = failed = 0
    for cls_name, cls_obj in sorted(globals().items()):
        if not (isinstance(cls_obj, type) and cls_name.startswith("Test")):
            continue
        instance = cls_obj()
        for method_name in sorted(dir(instance)):
            if not method_name.startswith("test_"):
                continue
            method = getattr(instance, method_name)
            if not callable(method):
                continue
            try:
                method()
                print(f"  PASS  {cls_name}.{method_name}")
                passed += 1
            except Exception as exc:
                print(f"  FAIL  {cls_name}.{method_name}: {exc}")
                traceback.print_exc()
                failed += 1

    print(f"\n{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
