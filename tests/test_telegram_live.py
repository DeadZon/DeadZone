"""Dry tests for factory.notify.telegram_live.TelegramLiveStatus."""
from __future__ import annotations

import json
import os
import time
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from factory.notify.telegram_live import (
    TelegramLiveStatus,
    generate_build_id,
    _THROTTLE_SECONDS,
)

_BUILD_ID = "DZ-mtk-zircon-20260525-003500"
_CODENAME = "zircon"
_SOC      = "mtk"


def _make_notifier(tmp_path: Path, **kwargs) -> TelegramLiveStatus:
    defaults = dict(
        build_id=_BUILD_ID,
        soc=_SOC,
        codename=_CODENAME,
        mod="free",
        mode="dry_run",
        rom_url="https://example.com/rom.zip",
        upload_pixeldrain=True,
        enabled=True,
        token="BOT_TOKEN",
        chat_id="-100CHATID",
        output_dir=tmp_path,
    )
    defaults.update(kwargs)
    return TelegramLiveStatus(**defaults)


class TestMissingSecrets(unittest.TestCase):
    def test_disabled_when_no_token(self):
        n = TelegramLiveStatus(
            build_id=_BUILD_ID, soc=_SOC, codename=_CODENAME,
            mod="free", mode="dry_run", enabled=True,
            token="", chat_id="",
        )
        result = n.start()
        self.assertEqual(result["status"], "DISABLED")
        self.assertTrue(any("missing secrets" in w for w in n.warnings))

    def test_disabled_when_env_empty(self):
        with patch.dict(os.environ, {}, clear=True):
            n = TelegramLiveStatus(
                build_id=_BUILD_ID, soc=_SOC, codename=_CODENAME,
                mod="free", mode="dry_run", enabled=True,
            )
        result = n.update_stage("BUILDING_SUPER", "Building")
        self.assertEqual(result["status"], "DISABLED")

    def test_not_enabled(self):
        n = TelegramLiveStatus(
            build_id=_BUILD_ID, soc=_SOC, codename=_CODENAME,
            mod="free", mode="dry_run", enabled=False,
            token="tok", chat_id="-100",
        )
        self.assertEqual(n.start()["status"], "DISABLED")


class TestCreateMessage(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def _fake_send_ok(self, method, payload):
        if method == "sendMessage":
            return {"ok": True, "result": {"message_id": 999}}
        return {"ok": True, "result": {}}

    def test_start_sends_message(self):
        n = _make_notifier(self.tmp)
        with patch.object(n, "_post", side_effect=self._fake_send_ok):
            result = n.start()
        self.assertEqual(result["status"], "STARTED")
        self.assertEqual(n.message_id, 999)

    def test_start_reuses_message_id(self):
        n = _make_notifier(self.tmp, telegram_message_id=42)
        edits = []
        def _fake_edit(method, payload):
            edits.append(method)
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake_edit):
            result = n.start()
        self.assertIn(result["status"], ("UPDATED", "UPDATED_AFTER_RETRY"))
        self.assertIn("editMessageText", edits)
        self.assertEqual(n.message_id, 42)  # unchanged

    def test_start_failed_returns_send_failed(self):
        n = _make_notifier(self.tmp)
        with patch.object(n, "_post", return_value={"ok": False, "error": "bad"}):
            result = n.start()
        self.assertEqual(result["status"], "SEND_FAILED")
        self.assertIsNone(n.message_id)


class TestEditMessage(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def _started_notifier(self) -> TelegramLiveStatus:
        n = _make_notifier(self.tmp, telegram_message_id=77)
        return n

    def test_update_stage_edits_message(self):
        n = self._started_notifier()
        calls = []
        def _fake(method, payload):
            calls.append((method, payload.get("text", "")[:30]))
            return {"ok": True, "result": {}}
        with patch.object(n, "_post", side_effect=_fake):
            result = n.update_stage("BUILDING_SUPER", "Building super.img")
        self.assertIn(result["status"], ("UPDATED", "UPDATED_AFTER_RETRY"))
        self.assertTrue(any("editMessageText" in c[0] for c in calls))

    def test_finish_success(self):
        n = self._started_notifier()
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            result = n.finish(success=True, final_zip="/out/final/Build.zip")
        self.assertIn(result["status"], ("UPDATED", "UPDATED_AFTER_RETRY"))
        self.assertEqual(n.current_stage, "DONE")

    def test_finish_failure(self):
        n = self._started_notifier()
        with patch.object(n, "_post", return_value={"ok": True, "result": {}}):
            result = n.finish(success=False, error="super.img overflow")
        self.assertIn(result["status"], ("UPDATED", "UPDATED_AFTER_RETRY"))
        self.assertEqual(n.current_stage, "FAILED")
        self.assertIn("super.img overflow", n.last_error)


class TestThrottling(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def test_throttle_suppresses_rapid_updates(self):
        n = _make_notifier(self.tmp, telegram_message_id=55)
        posts = []
        def _fake(method, payload):
            posts.append(method)
            return {"ok": True, "result": {}}

        with patch.object(n, "_post", side_effect=_fake):
            n.start()
            posts.clear()
            # Simulate back-to-back updates within throttle window
            n.update_stage("DOWNLOADING_ROM", "Downloading")
            result2 = n.update_stage("UNPACKING_ROM", "Unpacking")

        # First went through (after start reset _last_edit), second throttled
        self.assertEqual(result2["status"], "THROTTLED")

    def test_terminal_bypasses_throttle(self):
        n = _make_notifier(self.tmp, telegram_message_id=55)
        posts = []
        def _fake(method, payload):
            posts.append(method)
            return {"ok": True, "result": {}}

        with patch.object(n, "_post", side_effect=_fake):
            n.start()
            posts.clear()
            n.update_stage("BUILDING_SUPER", "Building")  # consume throttle
            result = n.finish(success=False, error="boom")  # must bypass

        self.assertIn(result["status"], ("UPDATED", "UPDATED_AFTER_RETRY"))


class TestGithubHandoff(unittest.TestCase):
    """GitHub passes telegram_message_id; Fly must reuse it."""

    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())

    def test_reuses_github_message_id(self):
        n = _make_notifier(self.tmp, telegram_message_id=1234)
        self.assertEqual(n.message_id, 1234)
        edits = []
        with patch.object(n, "_post", side_effect=lambda m, p: (edits.append(m), {"ok": True, "result": {}})[1]):
            n.start()
        self.assertIn("editMessageText", edits)
        self.assertEqual(n.message_id, 1234)  # not changed

    def test_fly_creates_if_no_message_id(self):
        n = _make_notifier(self.tmp, telegram_message_id=None)
        self.assertIsNone(n.message_id)
        with patch.object(n, "_post", return_value={"ok": True, "result": {"message_id": 999}}):
            result = n.start()
        self.assertEqual(result["status"], "STARTED")
        self.assertEqual(n.message_id, 999)


class TestGenerateBuildId(unittest.TestCase):
    def test_format(self):
        bid = generate_build_id("mtk", "zircon")
        self.assertTrue(bid.startswith("DZ-mtk-zircon-"))
        parts = bid.split("-")
        # DZ, soc, codename, date, time
        self.assertGreaterEqual(len(parts), 5)

    def test_soc_lowercased(self):
        bid = generate_build_id("MTK", "zircon")
        self.assertIn("-mtk-", bid)


class TestSocCredentialResolution(unittest.TestCase):
    def test_mtk_uses_mtk_secrets(self):
        env = {
            "TELEGRAM_MTK_BOT_TOKEN": "mtk_tok",
            "TELEGRAM_MTK_CHAT_ID":   "mtk_chat",
        }
        with patch.dict(os.environ, env, clear=True):
            n = TelegramLiveStatus(
                build_id=_BUILD_ID, soc="mtk", codename=_CODENAME,
                mod="free", mode="dry_run",
            )
        self.assertEqual(n.token, "mtk_tok")
        self.assertEqual(n.chat_id, "mtk_chat")

    def test_snapdragon_uses_snapdragon_secrets(self):
        env = {
            "TELEGRAM_SNAPDRAGON_BOT_TOKEN": "sd_tok",
            "TELEGRAM_SNAPDRAGON_CHAT_ID":   "sd_chat",
        }
        with patch.dict(os.environ, env, clear=True):
            n = TelegramLiveStatus(
                build_id=_BUILD_ID, soc="snapdragon", codename=_CODENAME,
                mod="free", mode="dry_run",
            )
        self.assertEqual(n.token, "sd_tok")
        self.assertEqual(n.chat_id, "sd_chat")

    def test_generic_fallback(self):
        env = {
            "TELEGRAM_BOT_TOKEN": "gen_tok",
            "TELEGRAM_CHAT_ID":   "gen_chat",
        }
        with patch.dict(os.environ, env, clear=True):
            n = TelegramLiveStatus(
                build_id=_BUILD_ID, soc="unknown", codename=_CODENAME,
                mod="free", mode="dry_run",
            )
        self.assertEqual(n.token, "gen_tok")
        self.assertEqual(n.chat_id, "gen_chat")

    def test_mtk_falls_back_to_generic(self):
        env = {"TELEGRAM_BOT_TOKEN": "fallback", "TELEGRAM_CHAT_ID": "fallback_chat"}
        with patch.dict(os.environ, env, clear=True):
            n = TelegramLiveStatus(
                build_id=_BUILD_ID, soc="mtk", codename=_CODENAME,
                mod="free", mode="dry_run",
            )
        self.assertEqual(n.token, "fallback")


if __name__ == "__main__":
    unittest.main()
