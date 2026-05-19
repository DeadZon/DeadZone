"""Live Telegram status message support for DeadZone Factory builds."""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from typing import Any


_MAX_TEXT_LEN = 4000
_VALID_STATUS = {"WAIT", "RUN", "OK", "SKIP", "FAIL"}


def _ascii_text(value: object) -> str:
    text = "" if value is None else str(value)
    return text.encode("ascii", errors="replace").decode("ascii")


def _env_first(*names: str) -> str | None:
    for name in names:
        value = os.environ.get(name, "").strip()
        if value:
            return value
    return None


class TelegramLiveStatus:
    def __init__(
        self,
        enabled: bool,
        build_name: str,
        device: str,
        flavor: str,
        platform: str | None = None,
        token: str | None = None,
        chat_id: str | None = None,
        thread_id: str | None = None,
    ):
        self.enabled = bool(enabled)
        self.build_name = build_name
        self.device = device
        self.flavor = flavor
        self.platform = platform
        self.token = token or _env_first("TELEGRAM_BOT_TOKEN")
        self.chat_id = chat_id or _env_first("TELEGRAM_CHAT_ID")
        self.thread_id = thread_id or _env_first(
            "TELEGRAM_THREAD_ID",
            "TELEGRAM_MESSAGE_THREAD_ID",
        )
        existing = os.environ.get("DEADZONE_TELEGRAM_MESSAGE_ID", "").strip()
        try:
            self.message_id: int | None = int(existing) if existing else None
        except ValueError:
            self.message_id = None
        self.started_at = time.monotonic()
        self.warnings: list[str] = []
        self.errors: list[str] = []

    def start(self, stages: list[dict]) -> dict:
        if not self._usable():
            return self._result("DISABLED")
        text = self._format_message(stages, final_status="RUNNING")
        if self.message_id is not None:
            # Workflow already sent the initial message; reuse it.
            return self._edit(text)
        payload = self._base_payload(text)
        response = self._post("sendMessage", payload)
        if response.get("ok") and isinstance(response.get("result"), dict):
            self.message_id = response["result"].get("message_id")
            return self._result("STARTED")
        self.warnings.append("Telegram initial send failed; live status disabled for this build")
        if response.get("error"):
            self.errors.append(str(response["error"]))
        return self._result("SEND_FAILED")

    def update(
        self,
        stages: list[dict],
        current: str | None = None,
        final_status: str | None = None,
    ) -> dict:
        if not self._usable() or self.message_id is None:
            return self._result("DISABLED")
        text = self._format_message(stages, current=current, final_status=final_status or "RUNNING")
        return self._edit(text)

    def finish(
        self,
        stages: list[dict],
        final_status: str,
        final_zip: str | None = None,
    ) -> dict:
        if not self._usable() or self.message_id is None:
            return self._result("DISABLED")
        text = self._format_message(stages, final_status=final_status, final_zip=final_zip)
        return self._edit(text)

    def _usable(self) -> bool:
        if not self.enabled:
            return False
        if not self.token or not self.chat_id:
            if "Telegram credentials are missing" not in self.warnings:
                self.warnings.append("Telegram credentials are missing; live status skipped")
            return False
        return True

    def _base_payload(self, text: str) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "chat_id": self.chat_id,
            "text": _ascii_text(text)[:_MAX_TEXT_LEN],
            "disable_web_page_preview": True,
        }
        if self.thread_id:
            try:
                payload["message_thread_id"] = int(self.thread_id)
            except ValueError:
                self.warnings.append("Telegram thread id is not an integer; topic support skipped")
        return payload

    def _edit(self, text: str) -> dict:
        payload = self._base_payload(text)
        payload["message_id"] = self.message_id
        response = self._post("editMessageText", payload)
        if response.get("ok"):
            return self._result("UPDATED")
        response = self._post("editMessageText", payload)
        if response.get("ok"):
            return self._result("UPDATED_AFTER_RETRY")
        self.warnings.append("Telegram edit failed after retry")
        if response.get("error"):
            self.errors.append(str(response["error"]))
        return self._result("EDIT_FAILED")

    def _post(self, method: str, payload: dict[str, Any]) -> dict:
        url = f"https://api.telegram.org/bot{self.token}/{method}"
        data = json.dumps(payload, ensure_ascii=True).encode("utf-8")
        request = urllib.request.Request(
            url,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read().decode("utf-8", errors="replace")
                return json.loads(body)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if "message is not modified" in body.lower():
                return {"ok": True, "result": {"not_modified": True}}
            return {"ok": False, "error": f"HTTP {exc.code}: {body}"}
        except Exception as exc:
            return {"ok": False, "error": str(exc)}

    def _format_message(
        self,
        stages: list[dict],
        current: str | None = None,
        final_status: str | None = None,
        final_zip: str | None = None,
    ) -> str:
        status = final_status or "RUNNING"
        lines = [
            "DeadZone Build Live Status",
            f"Build: {_ascii_text(self.build_name)}",
            f"Device: {_ascii_text(self.device or 'unknown')}",
            f"Flavor: {_ascii_text(self.flavor or 'unknown')}",
        ]
        if self.platform:
            lines.append(f"Platform: {_ascii_text(self.platform)}")
        lines.extend(["", f"Status: {_ascii_text(status)}", "", "Stages:"])
        for stage in stages:
            stage_status = str(stage.get("status") or "WAIT").upper()
            if stage_status not in _VALID_STATUS:
                stage_status = "WAIT"
            lines.append(f"[{stage_status}] {_ascii_text(stage.get('name') or stage.get('id') or 'Stage')}")
        if current:
            lines.extend(["", f"Current: {_ascii_text(current)}"])
        elapsed = int(max(0, time.monotonic() - self.started_at))
        hours, rem = divmod(elapsed, 3600)
        minutes, seconds = divmod(rem, 60)
        lines.append(f"Elapsed: {hours:02d}:{minutes:02d}:{seconds:02d}")
        if final_zip:
            lines.append(f"Final ZIP: {_ascii_text(final_zip)}")
        return "\n".join(lines)

    def _result(self, status: str) -> dict:
        return {
            "status": status,
            "enabled": self.enabled,
            "message_id": self.message_id,
            "warnings": list(self.warnings),
            "errors": list(self.errors),
        }

