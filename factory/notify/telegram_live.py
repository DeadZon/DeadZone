"""Live Telegram status message for DeadZone builds.

One message per build — created on start, edited at every stage.
Rate-limited to one edit per 5 seconds (except FAILED/DONE).

SoC-specific bot credentials:
  TELEGRAM_MTK_BOT_TOKEN / TELEGRAM_MTK_CHAT_ID
  TELEGRAM_SNAPDRAGON_BOT_TOKEN / TELEGRAM_SNAPDRAGON_CHAT_ID
  TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID  (fallback)
"""
from __future__ import annotations

import datetime
import json
import logging
import os
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Optional

_MAX_TEXT_LEN = 4096
_THROTTLE_SECONDS = 5.0

ALL_STAGES = [
    "QUEUED",
    "FLY_RECEIVED",
    "VALIDATING_REQUEST",
    "RESOLVING_DEVICE",
    "DOWNLOADING_ROM",
    "UNPACKING_ROM",
    "DETECTING_METADATA",
    "APPLYING_BASE_PATCHES",
    "APPLYING_MOD_PATCHES",
    "REPACKING_PARTITIONS",
    "CAPTURING_ORIGINAL_SUPER_LAYOUT",
    "BUILDING_SUPER",
    "VALIDATING_SUPER",
    "COLLECTING_IMAGES",
    "GENERATING_FLASH_SCRIPT",
    "PACKAGING_ZIP",
    "VALIDATING_FINAL_ZIP",
    "UPLOADING_PIXELDRAIN",
    "CLEANUP",
    "DONE",
    "FAILED",
]

_PROGRESS_STAGES = [
    ("FLY_RECEIVED",           "Request received"),
    ("RESOLVING_DEVICE",       "Device resolved"),
    ("DOWNLOADING_ROM",        "ROM downloaded"),
    ("UNPACKING_ROM",          "ROM unpacked"),
    ("DETECTING_METADATA",     "Metadata detected"),
    ("APPLYING_BASE_PATCHES",  "Base patches applied"),
    ("APPLYING_MOD_PATCHES",   "Mod patches applied"),
    ("REPACKING_PARTITIONS",   "Partitions repacked"),
    ("BUILDING_SUPER",         "Super built"),
    ("PACKAGING_ZIP",          "ZIP packaged"),
    ("VALIDATING_FINAL_ZIP",   "ZIP validated"),
    ("UPLOADING_PIXELDRAIN",   "Uploaded to PixelDrain"),
]

_ICON_DONE    = "✅"       # ✅
_ICON_CURRENT = "\U0001f7e1"   # 🟡
_ICON_FAILED  = "❌"       # ❌
_ICON_PENDING = "⚪"       # ⚪


def _env(*names: str) -> str:
    for name in names:
        v = os.environ.get(name, "").strip()
        if v:
            return v
    return ""


def _resolve_credentials(soc: Optional[str]) -> tuple[str, str, str]:
    # MTK chat migrated to supergroup: update TELEGRAM_MTK_CHAT_ID=-1003908135274
    soc = (soc or "").lower()
    if soc == "mtk":
        token   = _env("TELEGRAM_MTK_BOT_TOKEN",       "TELEGRAM_BOT_TOKEN")
        chat_id = _env("TELEGRAM_MTK_CHAT_ID",          "TELEGRAM_CHAT_ID")
    elif soc == "snapdragon":
        token   = _env("TELEGRAM_SNAPDRAGON_BOT_TOKEN", "TELEGRAM_BOT_TOKEN")
        chat_id = _env("TELEGRAM_SNAPDRAGON_CHAT_ID",   "TELEGRAM_CHAT_ID")
    else:
        token   = _env("TELEGRAM_BOT_TOKEN")
        chat_id = _env("TELEGRAM_CHAT_ID")
    thread_id = _env("TELEGRAM_THREAD_ID", "TELEGRAM_MESSAGE_THREAD_ID")
    return token, chat_id, thread_id


def _short_url(url: Optional[str]) -> str:
    if not url:
        return "—"
    return url.split("/")[-1] if "/" in url else url


def _elapsed_str(seconds: float) -> str:
    s = int(max(0, seconds))
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def _now_utc() -> str:
    return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")


def generate_build_id(soc: str, codename: str) -> str:
    """Generate DZ-<soc>-<codename>-<yyyymmdd-hhmmss>."""
    ts = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    return f"DZ-{(soc or 'unk').lower()}-{codename}-{ts}"


class TelegramLiveStatus:
    """One live Telegram message per build, edited at every stage."""

    def __init__(
        self,
        build_id: str,
        soc: str,
        codename: str,
        mod: str,
        mode: str,
        rom_url: Optional[str] = None,
        upload_pixeldrain: bool = False,
        source: str = "Fly",
        enabled: bool = True,
        telegram_message_id: Optional[int] = None,
        token: Optional[str] = None,
        chat_id: Optional[str] = None,
        thread_id: Optional[str] = None,
        output_dir: Optional[Path] = None,
    ):
        self.build_id          = build_id
        self.soc               = soc
        self.codename          = codename
        self.mod               = mod
        self.mode              = mode
        self.rom_url           = rom_url
        self.upload_pixeldrain = upload_pixeldrain
        self.source            = source
        self.enabled           = bool(enabled)

        _auto_token, _auto_chat, _auto_thread = _resolve_credentials(soc)
        self.token     = token     or _auto_token
        self.chat_id   = chat_id   or _auto_chat
        self.thread_id = thread_id or _auto_thread

        self.message_id: Optional[int] = telegram_message_id
        if self.message_id is None:
            _existing = _env("DEADZONE_TELEGRAM_MESSAGE_ID")
            if _existing:
                try:
                    self.message_id = int(_existing)
                except ValueError:
                    pass

        self.started_at   = time.monotonic()
        self.started_wall = _now_utc()

        # Mutable state — protected by _state_lock for reads from other threads
        self._state_lock      = threading.Lock()
        self.current_stage    = "QUEUED"
        self.current_action   = "Waiting in queue"
        self.completed_stages: list[str] = []
        self.last_error: Optional[str]   = None
        self.final_zip: Optional[str]    = None
        self.pixeldrain_link: Optional[str] = None

        # Throttle — only accessed from the build thread
        self._last_edit: float = 0.0

        # Reporting metadata
        self.first_update_time: Optional[str] = None
        self.last_update_time:  Optional[str] = None
        self.final_status:      Optional[str] = None

        self.warnings: list[str] = []
        self.errors:   list[str] = []

        self.output_dir = Path(output_dir) if output_dir else Path("output")
        self._setup_logger()

    # ── Setup ─────────────────────────────────────────────────────────────────

    def _setup_logger(self) -> None:
        log_path = self.output_dir / "logs" / "telegram_live.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        self._logger = logging.getLogger(f"telegram_live.{self.build_id}")
        if not self._logger.handlers:
            h = logging.FileHandler(log_path, encoding="utf-8")
            h.setFormatter(logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            ))
            self._logger.addHandler(h)
        self._logger.setLevel(logging.DEBUG)

    def _log(self, event: str, detail: str = "") -> None:
        self._logger.info(
            "build_id=%s stage=%s message_id=%s %s %s",
            self.build_id, self.current_stage, self.message_id, event, detail,
        )

    # ── Public interface ──────────────────────────────────────────────────────

    def start(self) -> dict:
        """Send initial build card (or reuse existing message_id)."""
        if not self._usable():
            return self._result("DISABLED")

        with self._state_lock:
            text = self._format_message()
            existing_id = self.message_id

        if existing_id is not None:
            result = self._do_edit(text)
            self._last_edit = time.monotonic()
            self._record_update()
            self._log("start reused", f"message_id={existing_id} result={result['status']}")
            return result

        payload = self._base_payload(text)
        response = self._post("sendMessage", payload)
        if response.get("ok") and isinstance(response.get("result"), dict):
            with self._state_lock:
                self.message_id = response["result"].get("message_id")
            self._last_edit = time.monotonic()
            self._record_update()
            self._log("start new", f"message_id={self.message_id}")
            return self._result("STARTED")

        err = str(response.get("error", "")) or "sendMessage returned not-ok without error detail"
        self.warnings.append("Telegram initial send failed")
        self.errors.append(err)
        with self._state_lock:
            self.last_error = err
            self.final_status = "SEND_FAILED"
        self._log("start FAILED", err)
        return self._result("SEND_FAILED")

    def update_stage(
        self,
        stage: str,
        action: str,
        error: Optional[str] = None,
    ) -> dict:
        """Update current stage. Throttled to 1 edit/5s, except FAILED/DONE."""
        if not self._usable():
            return self._result("DISABLED")

        terminal = stage in ("FAILED", "DONE")

        with self._state_lock:
            self.current_stage  = stage
            self.current_action = action
            if error:
                self.last_error = error
            self._advance_progress(stage)
            if not terminal:
                now = time.monotonic()
                if now - self._last_edit < _THROTTLE_SECONDS:
                    return self._result("THROTTLED")
            if self.message_id is None:
                return self._result("DISABLED")
            text = self._format_message()

        result = self._do_edit(text)
        self._last_edit = time.monotonic()
        self._record_update()
        self._log(f"update stage={stage}", f"action={action!r} result={result['status']}")
        return result

    def finish(
        self,
        success: bool,
        final_zip: Optional[str] = None,
        pixeldrain_link: Optional[str] = None,
        error: Optional[str] = None,
    ) -> dict:
        """Send final success or failure card immediately (no throttle)."""
        if not self._usable():
            return self._result("DISABLED")

        stage = "DONE" if success else "FAILED"

        with self._state_lock:
            self.current_stage  = stage
            self.current_action = "Build complete" if success else (error or "Build failed")
            self.last_error     = error
            self.final_zip      = final_zip
            self.pixeldrain_link = pixeldrain_link
            self.final_status   = stage
            if success:
                for s_id, _ in _PROGRESS_STAGES:
                    if s_id not in self.completed_stages:
                        self.completed_stages.append(s_id)
            if self.message_id is None:
                return self._result("DISABLED")
            text = self._format_message()

        result = self._do_edit(text)
        self._last_edit = time.monotonic()
        self._record_update()
        self._log(f"finish success={success}", f"result={result['status']}")
        return result

    def report_section(self) -> dict:
        """Data for pipeline_report.json Telegram section."""
        masked_chat = (self.chat_id[:4] + "****") if self.chat_id else None
        return {
            "notify_telegram":    self.enabled,
            "telegram_message_id": self.message_id,
            "telegram_chat_id":   masked_chat,
            "first_update_time":  self.first_update_time,
            "last_update_time":   self.last_update_time,
            "final_status":       self.final_status,
        }

    def snapshot(self) -> dict:
        """Thread-safe state snapshot for status endpoint."""
        with self._state_lock:
            return {
                "build_id":      self.build_id,
                "stage":         self.current_stage,
                "action":        self.current_action,
                "message_id":    self.message_id,
                "started_at":    self.started_wall,
                "elapsed":       _elapsed_str(time.monotonic() - self.started_at),
                "final_status":  self.final_status,
            }

    # ── Internal helpers ──────────────────────────────────────────────────────

    def _usable(self) -> bool:
        if not self.enabled:
            return False
        if not self.token or not self.chat_id:
            if "Telegram skipped: missing secrets" not in self.warnings:
                self.warnings.append("Telegram skipped: missing secrets")
                self._logger.warning("build_id=%s Telegram skipped: missing secrets", self.build_id)
            return False
        return True

    def _advance_progress(self, new_stage: str) -> None:
        """Mark all _PROGRESS_STAGES before new_stage as completed."""
        ids = [s for s, _ in _PROGRESS_STAGES]
        try:
            cutoff = ids.index(new_stage)
        except ValueError:
            return
        for i, s_id in enumerate(ids):
            if i < cutoff and s_id not in self.completed_stages:
                self.completed_stages.append(s_id)

    def _record_update(self) -> None:
        now = _now_utc()
        if self.first_update_time is None:
            self.first_update_time = now
        self.last_update_time = now

    def _base_payload(self, text: str) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "chat_id":                 self.chat_id,
            "text":                    text[:_MAX_TEXT_LEN],
            "disable_web_page_preview": True,
        }
        if self.thread_id:
            try:
                payload["message_thread_id"] = int(self.thread_id)
            except ValueError:
                self.warnings.append("Telegram thread_id is not an integer; topic skipped")
        return payload

    def _do_edit(self, text: str) -> dict:
        payload = self._base_payload(text)
        with self._state_lock:
            payload["message_id"] = self.message_id
        response = self._post("editMessageText", payload)
        if response.get("ok"):
            return self._result("UPDATED")
        time.sleep(1)
        response = self._post("editMessageText", payload)
        if response.get("ok"):
            return self._result("UPDATED_AFTER_RETRY")
        self.warnings.append("Telegram edit failed after retry")
        err = str(response.get("error", ""))
        if err:
            self.errors.append(err)
            self._logger.error("build_id=%s edit failed: %s", self.build_id, err)
        return self._result("EDIT_FAILED")

    def _post(self, method: str, payload: dict[str, Any], _migration_retry: bool = False) -> dict:
        url  = f"https://api.telegram.org/bot{self.token}/{method}"
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        req  = urllib.request.Request(
            url, data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = resp.read().decode("utf-8", errors="replace")
                result = json.loads(body)
                self._logger.debug(
                    "build_id=%s POST %s ok=%s message_id=%s",
                    self.build_id, method,
                    result.get("ok"),
                    (result.get("result") or {}).get("message_id"),
                )
                return result
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if "message is not modified" in body.lower():
                return {"ok": True, "result": {"not_modified": True}}
            # Handle supergroup migration: retry once with the new chat_id
            if not _migration_retry and exc.code == 400:
                try:
                    err_json = json.loads(body)
                    migrate_id = (err_json.get("parameters") or {}).get("migrate_to_chat_id")
                    if migrate_id:
                        new_id = str(migrate_id)
                        self._logger.info(
                            "build_id=%s Telegram chat migrated to supergroup: %s",
                            self.build_id, new_id,
                        )
                        with self._state_lock:
                            self.chat_id = new_id
                        payload = dict(payload)
                        payload["chat_id"] = new_id
                        return self._post(method, payload, _migration_retry=True)
                except Exception:
                    pass
            return {"ok": False, "error": f"HTTP {exc.code}: {body[:300]}"}
        except Exception as exc:
            return {"ok": False, "error": str(exc)}

    def _result(self, status: str) -> dict:
        return {
            "status":     status,
            "enabled":    self.enabled,
            "message_id": self.message_id,
            "build_id":   self.build_id,
            "warnings":   list(self.warnings),
            "errors":     list(self.errors),
        }

    # ── Message formatting ────────────────────────────────────────────────────

    def _format_message(self) -> str:
        # Called while holding _state_lock — do not acquire it again
        stage   = self.current_stage
        elapsed = _elapsed_str(time.monotonic() - self.started_at)
        if stage == "DONE":
            return self._fmt_success(elapsed)
        if stage == "FAILED":
            return self._fmt_failure(elapsed)
        return self._fmt_live(stage, elapsed)

    def _fmt_live(self, stage: str, elapsed: str) -> str:
        soc_disp = self.soc.upper() if self.soc else "Unknown"
        pd_disp  = "yes" if self.upload_pixeldrain else "no"
        lines = [
            "\U0001f525 DeadZone Build Live",
            "",
            f"Build:    {self.build_id}",
            f"Device:   {self.codename}",
            f"SoC:      {soc_disp}",
            f"Mod:      {self.mod}",
            f"Mode:     {self.mode}",
            f"Source:   {self.source}",
            f"ROM:      {_short_url(self.rom_url)}",
            f"Upload:   {pd_disp}",
            f"Started:  {self.started_wall}",
            "",
            f"Status:   \U0001f7e1 {stage}",
            f"Action:   {self.current_action}",
            f"Elapsed:  {elapsed}",
            "",
            "Progress:",
        ]
        for s_id, label in _PROGRESS_STAGES:
            if s_id in self.completed_stages:
                icon = _ICON_DONE
            elif s_id == stage:
                icon = _ICON_CURRENT
            else:
                icon = _ICON_PENDING
            lines.append(f"{icon} {label}")
        lines.extend(["", f"Last update: {_now_utc()}"])
        return "\n".join(lines)

    def _fmt_success(self, elapsed: str) -> str:
        lines = [
            "✅ DeadZone Build Complete",
            "",
            f"Build:   {self.build_id}",
            f"Device:  {self.codename}",
            f"Mod:     {self.mod}",
            f"Elapsed: {elapsed}",
        ]
        if self.final_zip:
            fz = Path(self.final_zip)
            lines.append(f"Final ZIP: {fz.name}")
            try:
                size_mb = fz.stat().st_size / 1_048_576
                lines.append(f"Size:    {size_mb:.1f} MB")
            except OSError:
                pass
        if self.pixeldrain_link:
            lines.append(f"PixelDrain: {self.pixeldrain_link}")
        lines.extend(["", f"Completed: {_now_utc()}"])
        return "\n".join(lines)

    def _fmt_failure(self, elapsed: str) -> str:
        lines = [
            "❌ DeadZone Build Failed",
            "",
            f"Build:   {self.build_id}",
            f"Device:  {self.codename}",
            f"Mod:     {self.mod}",
            f"Stage:   {self.current_stage}",
            f"Elapsed: {elapsed}",
        ]
        if self.last_error:
            lines.extend(["", "Error:", self.last_error[:500]])
        lines.extend([
            "",
            "Device remains safe. No flashing was performed.",
            "",
            f"Failed: {_now_utc()}",
        ])
        return "\n".join(lines)
