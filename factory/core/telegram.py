from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from factory.core.workspace import Workspace


MAX_TEXT_LEN = 4000


@dataclass
class TelegramResult:
    requested: bool = False
    enabled: bool = False
    status: str = "not requested"
    message_id: int | None = None
    failure_reason: str = ""
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    report_path: str = ""


def _env_first(*names: str) -> str:
    for name in names:
        value = os.environ.get(name, "").strip()
        if value:
            return value
    return ""


def _ascii(value: object) -> str:
    return ("" if value is None else str(value)).encode("ascii", errors="replace").decode("ascii")


def _credentials_for_soc(soc: str) -> tuple[str, str]:
    key = soc.strip().lower()
    if key == "mtk":
        return (
            _env_first("TELEGRAM_MTK_BOT_TOKEN", "TELEGRAM_BOT_TOKEN"),
            _env_first("TELEGRAM_MTK_CHAT_ID", "TELEGRAM_CHAT_ID"),
        )
    if key == "snapdragon":
        return (
            _env_first("TELEGRAM_SNAPDRAGON_BOT_TOKEN", "TELEGRAM_BOT_TOKEN"),
            _env_first("TELEGRAM_SNAPDRAGON_CHAT_ID", "TELEGRAM_CHAT_ID"),
        )
    return (_env_first("TELEGRAM_BOT_TOKEN"), _env_first("TELEGRAM_CHAT_ID"))


class TelegramStatus:
    def __init__(self, enabled: bool, soc: str, style: str, device: str, workspace: Workspace):
        self.requested = bool(enabled)
        self.soc = soc
        self.style = style
        self.device = device or "unknown"
        self.workspace = workspace
        self.token, self.chat_id = _credentials_for_soc(soc)
        self.thread_id = _env_first("TELEGRAM_THREAD_ID", "TELEGRAM_MESSAGE_THREAD_ID")
        self.started_at = time.monotonic()
        self.events: list[dict[str, str]] = []
        self.warnings: list[str] = []
        self.errors: list[str] = []
        self.status = "not requested"
        self.enabled = False
        self.message_id = self._existing_message_id()

    def start(self) -> TelegramResult:
        if not self.requested:
            return self.result("not requested")
        if not self.token or not self.chat_id:
            self.status = "skipped"
            self.warnings.append("Telegram credentials are missing; status notifications skipped")
            print("[TELEGRAM] Status: skipped; missing TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID")
            return self.result("skipped")
        self.enabled = True
        self.add_event("build started", "RUN")
        if self.message_id is not None:
            response = self._edit(self._format("RUNNING"))
        else:
            response = self._send(self._format("RUNNING"))
        if response.get("ok"):
            self.status = "running"
            if isinstance(response.get("result"), dict):
                message_id = response["result"].get("message_id")
                if message_id is not None:
                    self.message_id = int(message_id)
            print("[TELEGRAM] Status: running")
            return self.result("running")
        self.status = "failed"
        self.errors.append(str(response.get("error") or "initial Telegram send failed"))
        print("[TELEGRAM] Status: initial send failed")
        return self.result("failed")

    def add_event(self, name: str, status: str, detail: str = "") -> TelegramResult:
        if not self.requested:
            return self.result("not requested")
        clean_status = status.upper()
        self.events.append({"name": name, "status": clean_status, "detail": detail})
        if not self.enabled or self.message_id is None:
            return self.result(self.status)
        response = self._edit(self._format("RUNNING"))
        if response.get("ok"):
            self.status = "updated"
            return self.result("updated")
        self.errors.append(str(response.get("error") or "Telegram update failed"))
        self.status = "failed"
        print("[TELEGRAM] Status: update failed")
        return self.result("failed")

    def finish(self, final_status: str, final_zip: Path | None = None, upload_url: str = "") -> TelegramResult:
        if not self.requested:
            return self.result("not requested")
        detail = ""
        if final_zip:
            detail = str(final_zip)
        if upload_url:
            detail = f"{detail} | upload: {upload_url}" if detail else f"upload: {upload_url}"
        self.events.append({"name": "final status", "status": final_status.upper(), "detail": detail})
        if not self.enabled:
            return self.result(self.status)
        text = self._format(final_status.upper(), final_zip=final_zip, upload_url=upload_url)
        response = self._edit(text) if self.message_id is not None else self._send(text)
        if response.get("ok"):
            self.status = "completed" if final_status.upper() == "OK" else "failed"
            if isinstance(response.get("result"), dict) and response["result"].get("message_id") is not None:
                self.message_id = int(response["result"]["message_id"])
            print(f"[TELEGRAM] Status: {self.status}")
            return self.result(self.status)
        self.errors.append(str(response.get("error") or "Telegram final update failed"))
        self.status = "failed"
        print("[TELEGRAM] Status: final update failed")
        return self.result("failed")

    def write_report(self) -> TelegramResult:
        result = self.result(self.status)
        self.workspace.reports.mkdir(parents=True, exist_ok=True)
        path = self.workspace.reports / "telegram_report.txt"
        lines = [
            "MEZO / DeadZone Telegram Report",
            "===============================",
            f"requested: {result.requested}",
            f"enabled: {result.enabled}",
            f"status: {result.status}",
            f"message id: {result.message_id or '(none)'}",
            f"failure reason: {result.failure_reason or '(none)'}",
            "",
            "events:",
        ]
        lines.extend(
            f"- {event.get('status', 'UNKNOWN')}: {event.get('name', '')}"
            + (f" ({event.get('detail')})" if event.get("detail") else "")
            for event in self.events
        )
        if not self.events:
            lines.append("- (none)")
        lines.extend(["", "warnings:", *(self.warnings or ["(none)"])])
        lines.extend(["", "errors:", *(self.errors or ["(none)"])])
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        result.report_path = str(path)
        return result

    def result(self, status: str | None = None) -> TelegramResult:
        failure = self.errors[-1] if self.errors else ""
        return TelegramResult(
            requested=self.requested,
            enabled=self.enabled,
            status=status or self.status,
            message_id=self.message_id,
            failure_reason=failure,
            warnings=list(self.warnings),
            errors=list(self.errors),
        )

    def _existing_message_id(self) -> int | None:
        raw = os.environ.get("DEADZONE_TELEGRAM_MESSAGE_ID", "").strip()
        if not raw:
            return None
        try:
            return int(raw)
        except ValueError:
            self.warnings.append("DEADZONE_TELEGRAM_MESSAGE_ID is not an integer; sending a new message")
            return None

    def _base_payload(self, text: str) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "chat_id": self.chat_id,
            "text": _ascii(text)[:MAX_TEXT_LEN],
            "disable_web_page_preview": True,
        }
        if self.thread_id:
            try:
                payload["message_thread_id"] = int(self.thread_id)
            except ValueError:
                if "Telegram thread id is not an integer; topic support skipped" not in self.warnings:
                    self.warnings.append("Telegram thread id is not an integer; topic support skipped")
        return payload

    def _send(self, text: str) -> dict[str, Any]:
        return self._post("sendMessage", self._base_payload(text))

    def _edit(self, text: str) -> dict[str, Any]:
        payload = self._base_payload(text)
        payload["message_id"] = self.message_id
        response = self._post("editMessageText", payload)
        if response.get("ok"):
            return response
        self.warnings.append("Telegram edit failed; sent a new status message")
        return self._send(text)

    def _post(self, method: str, payload: dict[str, Any]) -> dict[str, Any]:
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
                return {"ok": True, "result": {"message_id": self.message_id}}
            return {"ok": False, "error": f"HTTP {exc.code}: {body[:200]}"}
        except Exception as exc:
            return {"ok": False, "error": str(exc)}

    def _format(self, build_status: str, final_zip: Path | None = None, upload_url: str = "") -> str:
        lines = [
            "MEZO DeadZone Production Status",
            f"SoC: {_ascii(self.soc)}",
            f"Device: {_ascii(self.device)}",
            f"Style: {_ascii(self.style)}",
            f"Status: {_ascii(build_status)}",
            "",
            "Stages:",
        ]
        for event in self.events[-18:]:
            detail = f" - {_ascii(event['detail'])}" if event.get("detail") else ""
            lines.append(f"[{_ascii(event.get('status'))}] {_ascii(event.get('name'))}{detail}")
        elapsed = int(max(0, time.monotonic() - self.started_at))
        minutes, seconds = divmod(elapsed, 60)
        lines.append(f"Elapsed: {minutes:02d}:{seconds:02d}")
        if final_zip:
            lines.append(f"Final ZIP: {_ascii(final_zip)}")
        if upload_url:
            lines.append(f"Upload: {_ascii(upload_url)}")
        return "\n".join(lines)
