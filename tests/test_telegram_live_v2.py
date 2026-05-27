"""Tests for the v2 TelegramLiveStatus API (start_build / update_stage / success / fail / cancelled)."""
from __future__ import annotations

import os
import time
import unittest
from pathlib import Path
from unittest.mock import patch
import json

from factory.notify.telegram_live import (
    TelegramLiveStatus,
    generate_build_id,
    _THROTTLE_SECONDS,
    PIPELINE_STAGES,
    _STAGE_ALIAS,
    _progress_bar,
)

_BUILD_ID = "DZ-mtk-zircon-20260527-120000"
_CODENAME = "zircon"
_SOC      = "mtk"


def _make(tmp_path: Path, **kw) -> TelegramLiveStatus:
    defaults = dict(
        build_id=_BUILD_ID,
        soc=_SOC,
        codename=_CODENAME,
        edition="legend",
        mode="execute",
        enabled=True,
        token="BOT_TOKEN_TEST",
        chat_id="-100CHATID",
        output_dir=tmp_path,
    )
    defaults.update(kw)
    return TelegramLiveStatus(**defaults)


def _ok(method="sendMessage", message_id=999):
    def _fake(m, p):
        if m == "sendMessage":
            return {"ok": True, "result": {"message_id": message_id}}
        return {"ok": True, "result": {}}
    return _fake


def _ok_edit():
    return lambda m, p: {"ok": True, "result": {}}


class TestStartBuild(unittest.TestCase):
    """start_build() sends one message when no message_id exists."""

    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def test_sends_new_message_when_no_id(self):
        n = _make(self.tmp)
        calls = []
        def _fake(method, payload):
            calls.append(method)
            if method == "sendMessage":
                return {"ok": True, "result": {"message_id": 42}}
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            result = n.start_build()
        self.assertEqual(result["status"], "STARTED")
        self.assertEqual(n.message_id, 42)
        self.assertIn("sendMessage", calls)
        self.assertNotIn("editMessageText", calls)

    def test_edits_existing_message_when_id_set(self):
        n = _make(self.tmp, telegram_message_id=77)
        calls = []
        def _fake(method, payload):
            calls.append(method)
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            result = n.start_build()
        self.assertIn(result["status"], ("UPDATED", "UPDATED_AFTER_RETRY"))
        self.assertIn("editMessageText", calls)
        self.assertNotIn("sendMessage", calls)
        self.assertEqual(n.message_id, 77)

    def test_edits_existing_message_from_env(self):
        with patch.dict(os.environ, {"DEADZONE_TELEGRAM_MESSAGE_ID": "88"}):
            n = _make(self.tmp)
        self.assertEqual(n.message_id, 88)
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            result = n.start_build()
        self.assertIn(result["status"], ("UPDATED", "UPDATED_AFTER_RETRY"))

    def test_start_alias_works(self):
        n = _make(self.tmp)
        with patch.object(n, "_post", side_effect=_ok()):
            result = n.start()
        self.assertEqual(result["status"], "STARTED")


class TestUpdateStage(unittest.TestCase):
    """update_stage() throttling and force bypass."""

    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def _started(self) -> TelegramLiveStatus:
        n = _make(self.tmp, telegram_message_id=55)
        return n

    def test_respects_throttle(self):
        n = self._started()
        posts = []
        with patch.object(n, "_post", side_effect=lambda m, p: (posts.append(m), {"ok": True, "result": {}})[1]):
            n.start_build()
            posts.clear()
            n.update_stage("DOWNLOADING_ROM", "Downloading")
            result2 = n.update_stage("UNPACKING_ROM", "Unpacking")
        self.assertEqual(result2["status"], "THROTTLED")

    def test_force_bypasses_throttle(self):
        n = self._started()
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            n.start_build()
            n.update_stage("DOWNLOADING_ROM", "Downloading")
            result = n.update_stage("UNPACKING_ROM", "Unpacking", force=True)
        self.assertIn(result["status"], ("UPDATED", "UPDATED_AFTER_RETRY"))

    def test_progress_auto_derived_from_stage(self):
        n = self._started()
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            n.start_build()
            # Force past throttle
            n._last_edit = 0.0
            n.update_stage("APPLYING_PATCHES", "Patching")
        # Stage 5 of 9 → (5-1)/9 * 100 = ~44%
        self.assertIsNotNone(n.current_progress)
        self.assertGreater(n.current_progress, 0)

    def test_explicit_progress_overrides_auto(self):
        n = self._started()
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            n.start_build()
            n._last_edit = 0.0
            n.update_stage("APPLYING_PATCHES", "Patching", progress=75)
        self.assertEqual(n.current_progress, 75)

    def test_legacy_positional_action_arg(self):
        """Accepts (stage, action) positional call for backward compat."""
        n = self._started()
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            n.start_build()
            n._last_edit = 0.0
            result = n.update_stage("REPACKING_PARTITIONS", "Repacking", action="Repacking")
        self.assertIn(result["status"], ("UPDATED", "UPDATED_AFTER_RETRY", "THROTTLED"))

    def test_disabled_after_final_call(self):
        n = self._started()
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            n.start_build()
            n.success()
            result = n.update_stage("APPLYING_PATCHES", "Too late")
        self.assertEqual(result["status"], "DISABLED")

    def test_edit_failure_sends_replacement_and_reuses_it(self):
        n = _make(self.tmp, telegram_message_id=21)
        calls = []

        def _fake(method, payload):
            calls.append((method, dict(payload)))
            if method == "editMessageText" and payload.get("message_id") == 21:
                return {"ok": False, "error": "Bad Request: message can't be edited"}
            if method == "sendMessage":
                return {"ok": True, "result": {"message_id": 99}}
            return {"ok": True, "result": {}}

        with patch.object(n, "_post", side_effect=_fake):
            result = n.update_stage("DOWNLOADING_ROM", "Downloading", force=True)
            n._last_edit = 0.0
            later = n.update_stage("UNPACKING_ROM", "Unpacking", force=True)
            n._last_heartbeat = 0.0
            n.heartbeat()

        self.assertEqual(result["status"], "REPLACED")
        self.assertIn(later["status"], ("UPDATED", "UPDATED_AFTER_RETRY"))
        self.assertEqual(n.message_id, 99)
        edit_ids = [payload.get("message_id") for method, payload in calls if method == "editMessageText"]
        self.assertIn(21, edit_ids)
        self.assertGreaterEqual(edit_ids.count(99), 2)

        status = json.loads((self.tmp / "reports" / "telegram_status.json").read_text(encoding="utf-8"))
        self.assertEqual(status["message_id"], 99)
        self.assertEqual(status["previous_message_id"], 21)
        self.assertTrue(status["replacement_message_created"])
        self.assertTrue(status["edit_failed"])


class TestSuccess(unittest.TestCase):
    """success() removes loading line and includes PixelDrain link."""

    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def test_success_removes_loading_line(self):
        n = _make(self.tmp, telegram_message_id=10)
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            result = n.success(pixeldrain_link="https://pd.example/abc")
        self.assertIn(result["status"], ("UPDATED", "UPDATED_AFTER_RETRY"))
        self.assertEqual(n.final_status, "DONE")
        text = sent_texts[-1]
        self.assertIn("COMPLETED", text)
        self.assertNotIn("Working...", text)
        self.assertNotIn("⏳", text)

    def test_success_includes_pixeldrain_link(self):
        n = _make(self.tmp, telegram_message_id=10)
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            n.success(pixeldrain_link="https://pixeldrain.com/u/TESTID")
        text = sent_texts[-1]
        self.assertIn("https://pixeldrain.com/u/TESTID", text)

    def test_success_includes_device_info(self):
        n = _make(self.tmp, telegram_message_id=10, android_version="16", os_version="HyperOS 3")
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            n.success()
        text = sent_texts[-1]
        self.assertIn("zircon", text)
        self.assertIn("16", text)
        self.assertIn("HyperOS 3", text)

    def test_success_final_status_set(self):
        n = _make(self.tmp, telegram_message_id=10)
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            n.success()
        self.assertEqual(n.final_status, "DONE")


class TestFail(unittest.TestCase):
    """fail() removes loading line and includes failed stage + error."""

    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def test_fail_removes_loading_line(self):
        n = _make(self.tmp, telegram_message_id=10)
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            n.fail(stage="BUILDING_SUPER", error_summary="super.img overflow")
        text = sent_texts[-1]
        self.assertIn("FAILED", text)
        self.assertNotIn("Working...", text)
        self.assertNotIn("⏳", text)

    def test_fail_includes_failed_stage(self):
        n = _make(self.tmp, telegram_message_id=10)
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            n.fail(stage="BUILDING_SUPER", error_summary="overflow at byte 0x1A2B")
        text = sent_texts[-1]
        # BUILDING_SUPER maps to PRESERVING_SUPER → "Preserve super image"
        self.assertIn("Preserve super image", text)
        self.assertIn("overflow at byte 0x1A2B", text)

    def test_fail_final_status_set(self):
        n = _make(self.tmp, telegram_message_id=10)
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            n.fail()
        self.assertEqual(n.final_status, "FAILED")

    def test_fail_uses_current_stage_if_none_provided(self):
        n = _make(self.tmp, telegram_message_id=10)
        n.current_stage = "UNPACKING_ROM"
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            n.fail(error_summary="unpack failed")
        text = sent_texts[-1]
        self.assertIn("Unpack ROM", text)


class TestCancelled(unittest.TestCase):
    """cancelled() removes loading line."""

    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def test_cancelled_removes_loading_line(self):
        n = _make(self.tmp, telegram_message_id=10)
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            result = n.cancelled()
        text = sent_texts[-1]
        self.assertIn("CANCELLED", text)
        self.assertNotIn("Working...", text)
        self.assertNotIn("⏳", text)
        self.assertEqual(n.final_status, "CANCELLED")


class TestApiEdgeCases(unittest.TestCase):
    """400 not-modified, 429 retry_after, 5xx backoff."""

    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def test_400_not_modified_is_ignored(self):
        """HTTP 400 'message is not modified' should not be treated as failure."""
        import urllib.error
        n = _make(self.tmp, telegram_message_id=10)

        def _fake_post(method, payload, _migration_retry=False):
            body = b'{"ok":false,"description":"Bad Request: message is not modified"}'
            exc = urllib.error.HTTPError("url", 400, "Bad Request", {}, None)
            exc.read = lambda: body
            raise exc

        with patch.object(n, "_post", wraps=n._post):
            with patch("urllib.request.urlopen") as mock_open:
                import io
                body = b'{"ok":false,"description":"Bad Request: message is not modified"}'
                mock_resp = type("R", (), {
                    "read": lambda self: body,
                    "status": 400,
                    "__enter__": lambda self: self,
                    "__exit__": lambda self, *a: None,
                })()
                import urllib.error as ue
                http_err = ue.HTTPError("url", 400, "Bad Request", {}, io.BytesIO(body))
                mock_open.side_effect = http_err
                result = n._post("editMessageText", {"chat_id": "-100", "message_id": 10, "text": "x"})
        self.assertTrue(result.get("ok"), f"Expected ok=True, got {result}")

    def test_429_retry_after_respected(self):
        """HTTP 429 should sleep retry_after seconds then retry."""
        import io
        import urllib.error as ue

        n = _make(self.tmp, telegram_message_id=10)
        sleep_calls = []

        body_429 = json_bytes({"ok": False, "parameters": {"retry_after": 2}})
        body_ok  = json_bytes({"ok": True, "result": {}})
        call_count = [0]

        def _mock_urlopen(req, timeout=30):
            call_count[0] += 1
            if call_count[0] == 1:
                raise ue.HTTPError("url", 429, "Too Many Requests", {}, io.BytesIO(body_429))
            return FakeResponse(body_ok)

        with patch("urllib.request.urlopen", side_effect=_mock_urlopen):
            with patch("time.sleep", side_effect=lambda s: sleep_calls.append(s)):
                result = n._post("editMessageText", {"chat_id": "-100", "message_id": 10, "text": "x"})

        self.assertTrue(result.get("ok"))
        self.assertTrue(any(s >= 2 for s in sleep_calls), f"Expected sleep >= 2s, got {sleep_calls}")

    def test_missing_token_returns_disabled(self):
        n = _make(self.tmp, token="", chat_id="")
        result = n.start_build()
        self.assertEqual(result["status"], "DISABLED")
        self.assertTrue(any("missing secrets" in w for w in n.warnings))

    def test_start_build_send_failed_on_bad_response(self):
        n = _make(self.tmp)
        with patch.object(n, "_post", return_value={"ok": False, "error": "bad token"}):
            result = n.start_build()
        self.assertEqual(result["status"], "SEND_FAILED")
        self.assertIsNone(n.message_id)


class TestRenderer(unittest.TestCase):
    """Message format rules."""

    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def test_live_message_has_progress_line(self):
        n = _make(self.tmp, telegram_message_id=10, android_version="16", os_version="HyperOS 3")
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            n.start_build()
            n._last_edit = 0.0
            texts = []
            def _capture(m, p):
                texts.append(p.get("text", ""))
                return {"ok": True, "result": {}}
            with patch.object(n, "_post", side_effect=_capture):
                n.update_stage("APPLYING_PATCHES", "Applying mods", progress=50)
        self.assertTrue(any("▓" in t or "░" in t for t in texts))
        self.assertTrue(any("50%" in t for t in texts))

    def test_success_no_progress_bar(self):
        n = _make(self.tmp, telegram_message_id=10)
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            n.success(pixeldrain_link="https://pd.example/x")
        text = sent_texts[-1]
        # Progress bar should NOT appear in final success
        self.assertNotIn("▓", text)
        self.assertNotIn("░", text)

    def test_success_pixeldrain_link_present(self):
        n = _make(self.tmp, telegram_message_id=10)
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            n.success(pixeldrain_link="https://pixeldrain.com/u/ABCDEF")
        self.assertIn("https://pixeldrain.com/u/ABCDEF", sent_texts[-1])

    def test_renderer_never_exposes_token(self):
        n = _make(self.tmp, telegram_message_id=10, token="SECRET_BOT_TOKEN_12345")
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            n.start_build()
            n._last_edit = 0.0
            n.update_stage("DOWNLOADING_ROM", "Downloading")
            n.success()
        for text in sent_texts:
            self.assertNotIn("SECRET_BOT_TOKEN_12345", text)

    def test_fail_no_loading_spinner(self):
        n = _make(self.tmp, telegram_message_id=10)
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            n.fail(stage="PACKAGING_ZIP", error_summary="zip error")
        text = sent_texts[-1]
        self.assertNotIn("⏳", text)
        self.assertNotIn("Working...", text)

    def test_cancelled_no_loading_spinner(self):
        n = _make(self.tmp, telegram_message_id=10)
        sent_texts = []
        def _fake(m, p):
            sent_texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            n.cancelled()
        text = sent_texts[-1]
        self.assertNotIn("⏳", text)
        self.assertNotIn("Working...", text)

    def test_progress_bar_format(self):
        self.assertEqual(_progress_bar(0),   "░░░░░░░░░░ 0%")
        self.assertEqual(_progress_bar(100), "▓▓▓▓▓▓▓▓▓▓ 100%")
        bar_50 = _progress_bar(50)
        self.assertIn("▓", bar_50)
        self.assertIn("░", bar_50)
        self.assertIn("50%", bar_50)

    def test_stage_numbering_in_live_message(self):
        n = _make(self.tmp, telegram_message_id=10)
        texts = []
        def _fake(m, p):
            texts.append(p.get("text", ""))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            n.start_build()
            n._last_edit = 0.0
            with patch.object(n, "_post", side_effect=_fake):
                n.update_stage("UNPACKING_ROM", "Extracting payload")
        # UNPACKING_ROM is stage 4/11
        self.assertTrue(any("[4/11]" in t for t in texts))


class TestBackwardCompat(unittest.TestCase):
    """Legacy finish() and mod property still work."""

    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def test_finish_success_routes_to_success(self):
        n = _make(self.tmp, telegram_message_id=10)
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            result = n.finish(success=True, final_zip="/out/Build.zip")
        self.assertEqual(n.final_status, "DONE")

    def test_finish_fail_routes_to_fail(self):
        n = _make(self.tmp, telegram_message_id=10)
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            result = n.finish(success=False, error="something went wrong")
        self.assertEqual(n.final_status, "FAILED")

    def test_mod_property_returns_edition(self):
        n = _make(self.tmp, edition="legend")
        self.assertEqual(n.mod, "legend")

    def test_legacy_mod_kwarg(self):
        n = TelegramLiveStatus(
            build_id=_BUILD_ID, soc=_SOC, codename=_CODENAME,
            mod="gaming", mode="dry_run", token="tok", chat_id="-100",
            output_dir=self.tmp,
        )
        self.assertEqual(n.edition, "gaming")
        self.assertEqual(n.mod, "gaming")


# ── Helpers ───────────────────────────────────────────────────────────────────

def json_bytes(obj: dict) -> bytes:
    import json
    return json.dumps(obj).encode()


class FakeResponse:
    def __init__(self, body: bytes):
        self._body = body

    def read(self) -> bytes:
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *a):
        pass


if __name__ == "__main__":
    unittest.main()
