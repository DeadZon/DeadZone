from __future__ import annotations

import json
import mimetypes
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from factory.core.workspace import Workspace, read_json


MAX_TEXT_LEN = 4000
MAX_DOCUMENT_BYTES = int(os.environ.get("TELEGRAM_MAX_DOCUMENT_BYTES", str(50 * 1024 * 1024)))


@dataclass
class TelegramResult:
    requested: bool = False
    enabled: bool = False
    attempted: bool = False
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


def _display_source(value: str) -> str:
    raw = str(value or "").strip()
    parsed = urlparse(raw)
    if parsed.scheme and parsed.netloc:
        name = Path(parsed.path).name
        return f"{parsed.netloc}/{name}" if name else parsed.netloc
    return Path(raw).name or "(none)"


class TelegramStatus:
    def __init__(self, enabled: bool, soc: str, style: str, device: str, workspace: Workspace, rom_source: str = ""):
        self.requested = bool(enabled)
        self.soc = soc
        self.style = style
        self.device = device or "unknown"
        self.detected_device = "unknown"
        self.rom_source = _display_source(rom_source)
        self.failed_stage = ""
        self.error_summary = ""
        self.workspace = workspace
        self.token, self.chat_id = _credentials_for_soc(soc)
        self.thread_id = _env_first("TELEGRAM_THREAD_ID", "TELEGRAM_MESSAGE_THREAD_ID")
        self.started_at = time.monotonic()
        self.events: list[dict[str, str]] = []
        self.warnings: list[str] = []
        self.errors: list[str] = []
        self.status = "not requested"
        self.enabled = False
        self.attempted = False
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
        self.attempted = True
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

    def finish(
        self,
        final_status: str,
        final_zip: Path | None = None,
        upload_url: str = "",
        failed_stage: str = "",
        error_summary: str = "",
    ) -> TelegramResult:
        if not self.requested:
            return self.result("not requested")
        detail = ""
        if final_zip:
            detail = str(final_zip)
        if upload_url:
            detail = f"{detail} | upload: {upload_url}" if detail else f"upload: {upload_url}"
        self.failed_stage = failed_stage or self.failed_stage
        self.error_summary = error_summary or self.error_summary
        self.events.append({"name": "final status", "status": final_status.upper(), "detail": detail})
        if not self.enabled:
            return self.result(self.status)
        text = self._format(final_status.upper(), final_zip=final_zip, upload_url=upload_url)
        self.attempted = True
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
            f"attempted: {result.attempted}",
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

    def send_app_inventory_document(
        self,
        inventory_zip: Path | None,
        *,
        total_apps: int = 0,
        android_version: str = "unknown",
        extraction_summary: dict[str, Any] | None = None,
        normalize_summary: dict[str, Any] | None = None,
    ) -> TelegramResult:
        print(f"[TELEGRAM] App inventory: {inventory_zip or '(none)'}")
        if not self.requested:
            return self.result("not requested")
        if not inventory_zip or not inventory_zip.is_file():
            self.warnings.append("App Inventory ZIP is missing; document upload skipped")
            return self.result(self.status)
        size = inventory_zip.stat().st_size
        if size > MAX_DOCUMENT_BYTES:
            message = f"App Inventory ZIP is too large for Telegram document upload: {inventory_zip} ({size} bytes)"
            self.warnings.append(message)
            self.add_event("app inventory document", "SKIP", message)
            return self.result(self.status)
        if not self.enabled:
            return self.result(self.status)
        summary = extraction_summary or {}
        norm = normalize_summary or {}
        caption_parts = [
            "Stable App Inventory generated",
            f"device: {_ascii(self.device)}",
            f"android version: {_ascii(android_version)}",
            f"total apps found: {_ascii(total_apps)}",
            f"inventory ZIP name: {_ascii(inventory_zip.name)}",
            "extraction status summary: "
            f"extracted={_ascii(summary.get('extracted', 0))}, "
            f"listed_only={_ascii(summary.get('listed_only', 0))}, "
            f"failed={_ascii(summary.get('failed', 0))}, "
            f"skipped={_ascii(summary.get('skipped', 0))}",
        ]
        if norm:
            caption_parts.append(
                "stable normalization: "
                f"kept={_ascii(norm.get('kept', 0))}, "
                f"removed={_ascii(norm.get('removed', 0))}, "
                f"renamed={_ascii(norm.get('renamed', 0))}, "
                f"missing={_ascii(norm.get('missing', 0))}, "
                f"protected={_ascii(norm.get('protected_extra', 0))}, "
                f"removed_bytes={_ascii(norm.get('removed_bytes', 0))}"
            )
        caption = "\n".join(caption_parts)
        response = self._send_document(inventory_zip, caption)
        self.attempted = True
        if response.get("ok"):
            self.events.append({"name": "app inventory document", "status": "OK", "detail": inventory_zip.name})
            self.status = "updated"
            return self.result(self.status)
        error = str(response.get("error") or "Telegram App Inventory document upload failed")
        self.warnings.append(error)
        self.events.append({"name": "app inventory document", "status": "FAIL", "detail": error})
        return self.result(self.status)

    def result(self, status: str | None = None) -> TelegramResult:
        failure = self.errors[-1] if self.errors else ""
        return TelegramResult(
            requested=self.requested,
            enabled=self.enabled,
            attempted=self.attempted,
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

    def _send_document(self, path: Path, caption: str) -> dict[str, Any]:
        fields: dict[str, Any] = {
            "chat_id": self.chat_id,
            "caption": _ascii(caption)[:1024],
        }
        if self.thread_id:
            try:
                fields["message_thread_id"] = int(self.thread_id)
            except ValueError:
                if "Telegram thread id is not an integer; topic support skipped" not in self.warnings:
                    self.warnings.append("Telegram thread id is not an integer; topic support skipped")
        return self._post_multipart("sendDocument", fields, "document", path)

    def _post_multipart(self, method: str, fields: dict[str, Any], file_field: str, path: Path) -> dict[str, Any]:
        boundary = f"----DeadZone{int(time.time() * 1000)}"
        body = bytearray()
        for name, value in fields.items():
            body.extend(f"--{boundary}\r\n".encode("ascii"))
            body.extend(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode("ascii"))
            body.extend(_ascii(value).encode("utf-8"))
            body.extend(b"\r\n")
        filename = path.name
        content_type = mimetypes.guess_type(filename)[0] or "application/zip"
        body.extend(f"--{boundary}\r\n".encode("ascii"))
        body.extend(
            (
                f'Content-Disposition: form-data; name="{file_field}"; filename="{filename}"\r\n'
                f"Content-Type: {content_type}\r\n\r\n"
            ).encode("ascii")
        )
        body.extend(path.read_bytes())
        body.extend(b"\r\n")
        body.extend(f"--{boundary}--\r\n".encode("ascii"))
        request = urllib.request.Request(
            f"https://api.telegram.org/bot{self.token}/{method}",
            data=bytes(body),
            headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.loads(response.read().decode("utf-8", errors="replace"))
        except urllib.error.HTTPError as exc:
            body_text = exc.read().decode("utf-8", errors="replace")
            return {"ok": False, "error": f"HTTP {exc.code}: {body_text[:200]}"}
        except Exception as exc:
            return {"ok": False, "error": str(exc)}

    def _format(self, build_status: str, final_zip: Path | None = None, upload_url: str = "") -> str:
        final_name = final_zip.name if final_zip else ""
        final_size = ""
        if final_zip and final_zip.is_file():
            final_size = f"{final_zip.stat().st_size / 1024 / 1024:.1f} MiB"
        current = ""
        for event in reversed(self.events):
            if event.get("status") == "RUN":
                current = event.get("name", "")
                break
        lines = [
            "MEZO DeadZone Production Status",
            f"SoC: {_ascii(self.soc)}",
            f"Selected device: {_ascii(self.device)}",
            f"Detected device: {_ascii(self.detected_device)}",
            f"Style: {_ascii(self.style)}",
            f"ROM source: {_ascii(self.rom_source)}",
            f"Status: {_ascii(build_status)}",
        ]
        if current:
            lines.append(f"Current stage: {_ascii(current)}")
        if self.failed_stage:
            lines.append(f"Failed stage: {_ascii(self.failed_stage)}")
        if self.error_summary:
            lines.append(f"Error: {_ascii(self.error_summary)[:500]}")
        lines.extend(["", "Stages:"])
        for event in self.events[-18:]:
            detail = f" - {_ascii(event['detail'])}" if event.get("detail") else ""
            lines.append(f"[{_ascii(event.get('status'))}] {_ascii(event.get('name'))}{detail}")
        elapsed = int(max(0, time.monotonic() - self.started_at))
        minutes, seconds = divmod(elapsed, 60)
        lines.append(f"Elapsed: {minutes:02d}:{seconds:02d}")
        if final_name:
            lines.append(f"Final ZIP: {_ascii(final_name)}")
        if final_size:
            lines.append(f"Final size: {_ascii(final_size)}")
        size_policy = read_json(self.workspace.meta / "size_policy.json", {})
        size_reduction = read_json(self.workspace.meta / "size_reduction.json", {})
        if build_status != "OK" and size_policy:
            lines.append(f"Max allowed: {_ascii(size_policy.get('final_zip_max_allowed') or size_policy.get('final_zip_max_bytes') or '')}")
            lines.append(f"Size reduction: {_ascii(size_reduction.get('level') or '(none)')} / removed {_ascii(size_reduction.get('removed_bytes') or 0)} bytes")
            recommendation = size_policy.get("recommendation") or size_reduction.get("recommendation")
            if recommendation:
                lines.append(f"Recommendation: {_ascii(recommendation)}")
        if upload_url:
            lines.append(f"PixelDrain: {_ascii(upload_url)}")
        return "\n".join(lines)
