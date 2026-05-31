from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from factory.core.telegram import (
    TelegramStatus,
    _mask_chat_id,
    _parse_chat_ids,
    resolve_telegram_recipients,
)
from factory.core.workspace import Workspace


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_ws(tmp_path: Path) -> Workspace:
    root = tmp_path / "workspace"
    root.mkdir(parents=True, exist_ok=True)
    for sub in ("input", "extracted", "images", "partitions", "meta", "reports", "logs"):
        (root / sub).mkdir(exist_ok=True)
    (tmp_path / "final").mkdir(exist_ok=True)
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


def _make_tg(ws: Workspace, soc: str = "mtk") -> TelegramStatus:
    tg = TelegramStatus(enabled=True, soc=soc, style="Stable", device="zircon", workspace=ws)
    tg.enabled = True
    tg.token = "fake_token"
    return tg


def _fake_send(chat_ids: list[str], base_msg_id: int = 100):
    """Return a _post mock that tracks calls and assigns sequential message IDs."""
    calls: list[tuple[str, dict]] = []
    counter = [base_msg_id]

    def _post(method: str, payload: dict) -> dict:
        calls.append((method, dict(payload)))
        msg_id = payload.get("message_id") or counter[0]
        counter[0] += 1
        return {"ok": True, "result": {"message_id": msg_id}}

    return calls, _post


# ---------------------------------------------------------------------------
# resolve_telegram_recipients
# ---------------------------------------------------------------------------


def test_single_chat_id_fallback(monkeypatch):
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "123456789")
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_IDS", raising=False)

    result = resolve_telegram_recipients("mtk")

    assert result == ["123456789"]


def test_chat_ids_multiple_recipients(monkeypatch):
    monkeypatch.setenv("TELEGRAM_MTK_CHAT_IDS", "111, 222, 333")
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)

    result = resolve_telegram_recipients("mtk")

    assert result == ["111", "222", "333"]


def test_mtk_chat_ids_overrides_generic(monkeypatch):
    monkeypatch.setenv("TELEGRAM_MTK_CHAT_IDS", "mtk_only")
    monkeypatch.setenv("TELEGRAM_CHAT_IDS", "generic_1,generic_2")
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)

    result = resolve_telegram_recipients("mtk")

    assert result == ["mtk_only"]


def test_snapdragon_chat_ids_overrides_generic(monkeypatch):
    monkeypatch.setenv("TELEGRAM_SNAPDRAGON_CHAT_IDS", "snap_only")
    monkeypatch.setenv("TELEGRAM_CHAT_IDS", "generic_1,generic_2")
    monkeypatch.delenv("TELEGRAM_SNAPDRAGON_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)

    result = resolve_telegram_recipients("snapdragon")

    assert result == ["snap_only"]


def test_duplicate_ids_are_removed(monkeypatch):
    monkeypatch.setenv("TELEGRAM_CHAT_IDS", "111, 222, 111, 333, 222")
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)

    result = resolve_telegram_recipients(None)

    assert result == ["111", "222", "333"]


def test_negative_group_ids_accepted(monkeypatch):
    monkeypatch.setenv("TELEGRAM_MTK_CHAT_IDS", "-1001234567890,987654321")
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)

    result = resolve_telegram_recipients("mtk")

    assert "-1001234567890" in result
    assert "987654321" in result


def test_empty_entries_ignored(monkeypatch):
    monkeypatch.setenv("TELEGRAM_CHAT_IDS", "111,,  ,222,  ")
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)

    result = resolve_telegram_recipients(None)

    assert result == ["111", "222"]


def test_group_id_appended_as_extra(monkeypatch):
    monkeypatch.setenv("TELEGRAM_MTK_CHAT_IDS", "111")
    monkeypatch.setenv("TELEGRAM_MTK_GROUP_ID", "-1009999")
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)

    result = resolve_telegram_recipients("mtk")

    assert "111" in result
    assert "-1009999" in result
    assert result.index("111") < result.index("-1009999")


def test_group_id_not_duplicated_if_already_in_chat_ids(monkeypatch):
    monkeypatch.setenv("TELEGRAM_MTK_CHAT_IDS", "-1009999,111")
    monkeypatch.setenv("TELEGRAM_MTK_GROUP_ID", "-1009999")
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)

    result = resolve_telegram_recipients("mtk")

    assert result.count("-1009999") == 1


# ---------------------------------------------------------------------------
# _mask_chat_id
# ---------------------------------------------------------------------------


def test_mask_chat_id_long():
    assert _mask_chat_id("123456789") == "***6789"


def test_mask_chat_id_negative_group():
    assert _mask_chat_id("-1001234567890") == "***7890"


def test_mask_chat_id_short():
    assert _mask_chat_id("12") == "***"


def test_mask_chat_id_empty():
    assert _mask_chat_id("") == "(empty)"


# ---------------------------------------------------------------------------
# Multi-recipient message_id map
# ---------------------------------------------------------------------------


def test_message_id_map_stores_per_chat(tmp_path, monkeypatch):
    """start() sends to every recipient and stores individual message IDs."""
    monkeypatch.setenv("TELEGRAM_MTK_CHAT_IDS", "111,222")
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    monkeypatch.setenv("TELEGRAM_MTK_BOT_TOKEN", "tok")
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws, soc="mtk")

    sent: list[tuple[str, int]] = []

    def _post(method: str, payload: dict) -> dict:
        chat_id = payload.get("chat_id")
        if method == "sendMessage":
            msg_id = 100 if chat_id == "111" else 200
            sent.append((chat_id, msg_id))
            return {"ok": True, "result": {"message_id": msg_id}}
        return {"ok": True, "result": {"message_id": payload.get("message_id")}}

    tg._post = _post
    with patch("factory.core.telegram._TELEGRAM_THROTTLE_SECONDS", 0):
        tg.start()

    assert tg._message_ids.get("111") == 100
    assert tg._message_ids.get("222") == 200


def test_edit_updates_all_chats(tmp_path, monkeypatch):
    """add_event() sends editMessageText for each chat's own message_id."""
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.chat_id = "111"
    tg._recipients = ["111", "222"]
    tg._message_ids = {"111": 10, "222": 20}
    tg._last_edit_at = 0.0
    tg._last_stage = ""

    edits: list[tuple[str, int]] = []

    def _post(method: str, payload: dict) -> dict:
        if method == "editMessageText":
            edits.append((payload["chat_id"], payload["message_id"]))
        return {"ok": True, "result": {"message_id": payload.get("message_id")}}

    tg._post = _post
    with patch("factory.core.telegram._TELEGRAM_THROTTLE_SECONDS", 0):
        tg.add_event("super", "RUN")

    assert ("111", 10) in edits
    assert ("222", 20) in edits


def test_failed_edit_falls_back_to_send(tmp_path, monkeypatch):
    """If editMessageText fails for one chat, that chat gets sendMessage instead."""
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.chat_id = "111"
    tg._recipients = ["111", "222"]
    tg._message_ids = {"111": 10, "222": 20}
    tg._last_edit_at = 0.0
    tg._last_stage = ""

    calls: list[tuple[str, str]] = []

    def _post(method: str, payload: dict) -> dict:
        chat_id = payload["chat_id"]
        calls.append((method, chat_id))
        if method == "editMessageText" and chat_id == "222":
            return {"ok": False, "error": "simulated edit failure"}
        return {"ok": True, "result": {"message_id": payload.get("message_id", 99)}}

    tg._post = _post
    with patch("factory.core.telegram._TELEGRAM_THROTTLE_SECONDS", 0):
        tg.add_event("super", "RUN")

    methods_for_222 = [m for m, c in calls if c == "222"]
    assert "editMessageText" in methods_for_222
    assert "sendMessage" in methods_for_222


def test_failed_recipient_does_not_break_others(tmp_path, monkeypatch):
    """One chat failing to receive the message must not prevent others from succeeding."""
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.chat_id = "111"
    tg._recipients = ["111", "222", "333"]
    tg._message_ids = {}
    tg._last_edit_at = 0.0

    successes: list[str] = []
    failures: list[str] = []

    def _post(method: str, payload: dict) -> dict:
        chat_id = payload["chat_id"]
        if chat_id == "222":
            failures.append(chat_id)
            return {"ok": False, "error": "network error"}
        successes.append(chat_id)
        return {"ok": True, "result": {"message_id": 42}}

    tg._post = _post
    with patch("factory.core.telegram._TELEGRAM_THROTTLE_SECONDS", 0):
        tg.start()

    assert "111" in successes
    assert "333" in successes
    assert "222" in failures
    assert tg._message_ids.get("111") == 42
    assert tg._message_ids.get("333") == 42
    assert "222" not in tg._message_ids


def test_no_token_in_logs(tmp_path, monkeypatch, capsys):
    """Token must never appear in printed output."""
    secret_token = "SECRET_BOT_TOKEN_12345"
    monkeypatch.setenv("TELEGRAM_MTK_BOT_TOKEN", secret_token)
    monkeypatch.setenv("TELEGRAM_MTK_CHAT_IDS", "111")
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws, soc="mtk")

    def _post(method: str, payload: dict) -> dict:
        return {"ok": True, "result": {"message_id": 1}}

    tg._post = _post
    with patch("factory.core.telegram._TELEGRAM_THROTTLE_SECONDS", 0):
        tg.start()
        tg.finish("OK")

    out = capsys.readouterr().out
    assert secret_token not in out


def test_message_id_property_backward_compat(tmp_path, monkeypatch):
    """message_id property getter/setter must behave as before for single-chat code."""
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.chat_id = "fake_chat"

    assert tg.message_id is None
    tg.message_id = 42
    assert tg.message_id == 42
    assert tg._message_ids["fake_chat"] == 42

    tg.message_id = None
    assert tg.message_id is None
    assert "fake_chat" not in tg._message_ids


def test_finish_edits_all_chats(tmp_path, monkeypatch):
    """finish() must edit each chat's own message_id."""
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws)
    tg.chat_id = "111"
    tg._recipients = ["111", "222"]
    tg._message_ids = {"111": 10, "222": 20}

    edits: list[tuple[str, int]] = []

    def _post(method: str, payload: dict) -> dict:
        if method == "editMessageText":
            edits.append((payload["chat_id"], payload["message_id"]))
        return {"ok": True, "result": {"message_id": payload.get("message_id")}}

    tg._post = _post
    tg.finish("OK")

    assert ("111", 10) in edits
    assert ("222", 20) in edits


def test_generic_fallback_no_soc(monkeypatch):
    """With no SoC, resolver uses TELEGRAM_CHAT_IDS then TELEGRAM_CHAT_ID."""
    monkeypatch.setenv("TELEGRAM_CHAT_IDS", "aaa,bbb")
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)

    result = resolve_telegram_recipients(None)
    assert result == ["aaa", "bbb"]


def test_generic_single_id_fallback(monkeypatch):
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "solo")

    result = resolve_telegram_recipients(None)
    assert result == ["solo"]


def test_write_report_creates_file(tmp_path, monkeypatch):
    """write_report() must create the debug file without printing the token."""
    monkeypatch.setenv("TELEGRAM_MTK_CHAT_IDS", "111,222")
    monkeypatch.setenv("TELEGRAM_MTK_BOT_TOKEN", "SECRET")
    monkeypatch.delenv("TELEGRAM_CHAT_IDS", raising=False)
    monkeypatch.delenv("TELEGRAM_MTK_CHAT_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    ws = _make_ws(tmp_path)
    tg = _make_tg(ws, soc="mtk")
    tg._message_ids = {"111": 10, "222": 20}

    tg.write_report()

    report = ws.reports / "telegram_recipients_debug.txt"
    assert report.is_file()
    content = report.read_text(encoding="utf-8")
    assert "SECRET" not in content
    assert "***" in content  # masked IDs present
    assert "recipient_count: 2" in content
    assert "TELEGRAM_MTK_CHAT_IDS" in content
