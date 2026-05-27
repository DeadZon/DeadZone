"""Live Telegram status message for DeadZone builds.

One message per build — created on start_build(), edited at every stage.
Rate-limited to one edit per 3 seconds (use force=True to bypass).

Secret priority:
  MTK:        TELEGRAM_MTK_BOT_TOKEN / TELEGRAM_MTK_CHAT_ID
  Snapdragon: TELEGRAM_SNAPDRAGON_BOT_TOKEN / TELEGRAM_SNAPDRAGON_CHAT_ID
  Fallback:   TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID
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

_MAX_TEXT_LEN     = 4096
_THROTTLE_SECONDS = 3.0
_RETRY_BACKOFF    = [1.0, 2.0, 4.0]
_HEARTBEAT_INTERVAL = 60  # seconds between heartbeat Telegram edits during long stages

# 11 canonical pipeline stages (stage_id, display_label, stage_number)
PIPELINE_STAGES: list[tuple[str, str, int]] = [
    ("STARTING",            "Starting build",         1),
    ("DOWNLOADING_ROM",     "Download ROM",           2),
    ("DETECTING_ROM",       "Detect ROM format",      3),
    ("UNPACKING_ROM",       "Unpack ROM",             4),
    ("COLLECTING_IMAGES",   "Collect images",         5),
    ("PRESERVING_SUPER",    "Preserve super image",   6),
    ("ASSEMBLING_IMAGES",   "Assemble final images",  7),
    ("PACKAGING_ZIP",       "Package fastboot ZIP",   8),
    ("UPLOADING_PIXELDRAIN","Upload to PixelDrain",   9),
    ("VALIDATING_ZIP",      "Validate final ZIP",    10),
    ("CLEANUP",             "Cleanup workspace",     11),
]

_STAGE_ID_TO_NUM: dict[str, int] = {s: n for s, _, n in PIPELINE_STAGES}
_TOTAL_STAGES = len(PIPELINE_STAGES)

# Map legacy/orchestrator stage IDs → canonical stage IDs
_STAGE_ALIAS: dict[str, str] = {
    "QUEUED":                          "STARTING",
    "FLY_RECEIVED":                    "STARTING",
    "VALIDATING":                      "STARTING",
    "VALIDATING_REQUEST":              "STARTING",
    "RESOLVING_DEVICE":                "STARTING",
    "DETECTING_METADATA":              "DETECTING_ROM",
    "APPLYING_PATCHES":                "ASSEMBLING_IMAGES",
    "APPLYING_BASE_PATCHES":           "ASSEMBLING_IMAGES",
    "APPLYING_MOD_PATCHES":            "ASSEMBLING_IMAGES",
    "REPACKING_PARTITIONS":            "PRESERVING_SUPER",
    "CAPTURING_ORIGINAL_SUPER_LAYOUT": "PRESERVING_SUPER",
    "BUILDING_SUPER":                  "PRESERVING_SUPER",
    "REPACKING_SUPER":                 "PRESERVING_SUPER",
    "VALIDATING_SUPER":                "PRESERVING_SUPER",
    "GENERATING_FLASH_SCRIPT":         "PACKAGING_ZIP",
    "VALIDATING_FINAL_ZIP":            "VALIDATING_ZIP",
    "UPLOADING":                       "UPLOADING_PIXELDRAIN",
}


def _env(*names: str) -> str:
    for name in names:
        v = os.environ.get(name, "").strip()
        if v:
            return v
    return ""


def _resolve_credentials(soc: Optional[str]) -> tuple[str, str, str]:
    soc = (soc or "").lower()
    if soc == "mtk":
        token   = _env("TELEGRAM_MTK_BOT_TOKEN",        "TELEGRAM_BOT_TOKEN")
        chat_id = _env("TELEGRAM_MTK_CHAT_ID",           "TELEGRAM_CHAT_ID")
    elif soc == "snapdragon":
        token   = _env("TELEGRAM_SNAPDRAGON_BOT_TOKEN",  "TELEGRAM_BOT_TOKEN")
        chat_id = _env("TELEGRAM_SNAPDRAGON_CHAT_ID",    "TELEGRAM_CHAT_ID")
    else:
        token   = _env("TELEGRAM_BOT_TOKEN")
        chat_id = _env("TELEGRAM_CHAT_ID")
    thread_id = _env("TELEGRAM_THREAD_ID", "TELEGRAM_MESSAGE_THREAD_ID")
    return token, chat_id, thread_id


def _elapsed_str(seconds: float) -> str:
    s = int(max(0, seconds))
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h:02d}h {m:02d}m"
    return f"{m:02d}m {s:02d}s"


def _now_hhmm() -> str:
    return datetime.datetime.utcnow().strftime("%H:%M")


def _now_utc() -> str:
    return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")


def _progress_bar(percent: int, width: int = 10) -> str:
    pct = max(0, min(100, percent))
    filled = round(pct / 100 * width)
    return "▓" * filled + "░" * (width - filled) + f" {pct}%"


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
        edition: Optional[str] = None,
        mode: str = "dry_run",
        rom_url: Optional[str] = None,
        upload_pixeldrain: bool = False,
        source: str = "GitHub",
        enabled: bool = True,
        telegram_message_id: Optional[int] = None,
        token: Optional[str] = None,
        chat_id: Optional[str] = None,
        thread_id: Optional[str] = None,
        output_dir: Optional[Path] = None,
        android_version: Optional[str] = None,
        os_version: Optional[str] = None,
        build_name: Optional[str] = None,
        developer: str = "Mezo",
        rom_format: Optional[str] = None,
        super_strategy: Optional[str] = None,
        engine: Optional[str] = None,
        # Legacy compat alias
        mod: Optional[str] = None,
    ):
        self.build_id          = build_id
        self.soc               = soc
        self.codename          = codename
        self.edition           = edition or mod or "base"   # mod is the legacy alias
        self.mode              = mode
        self.rom_url           = rom_url
        self.upload_pixeldrain = upload_pixeldrain
        self.source            = source
        self.enabled           = bool(enabled)
        self.android_version   = android_version or ""
        self.os_version        = os_version or ""
        self.build_name        = build_name or f"DeadZone_{self.edition.capitalize()}_{codename}"
        self.developer         = developer
        self.rom_format        = rom_format or ""
        self.super_strategy    = super_strategy or ""
        self.engine            = engine or "Legacy"

        _auto_token, _auto_chat, _auto_thread = _resolve_credentials(soc)
        self.token     = token     or _auto_token
        self.chat_id   = chat_id   or _auto_chat
        self.thread_id = thread_id or _auto_thread

        self.message_id: Optional[int] = telegram_message_id
        self.previous_message_id: Optional[int] = None
        self.edit_failed: bool = False
        self.replacement_message_created: bool = False
        self.replacement_reason: Optional[str] = None
        self.last_api_error: Optional[str] = None
        if self.message_id is None:
            _existing = _env("DEADZONE_TELEGRAM_MESSAGE_ID")
            if _existing:
                try:
                    self.message_id = int(_existing)
                except ValueError:
                    pass

        self.started_at   = time.monotonic()
        self.started_wall = _now_utc()

        self._state_lock       = threading.Lock()
        self.current_stage     = "QUEUED"
        self.current_detail    = "Waiting to start"
        self.current_progress: Optional[int] = None
        self.last_error: Optional[str]       = None
        self._is_final         = False

        self._last_edit: float = 0.0

        self.first_update_time: Optional[str] = None
        self.last_update_time:  Optional[str] = None
        self.final_status:      Optional[str] = None

        # Failure details (populated by fail())
        self.failure_stage:  Optional[str] = None
        self.failure_reason: Optional[str] = None
        self.failure_hint:   Optional[str] = None
        self.raw_error:      Optional[str] = None

        self._heartbeat_count: int = 0
        self._last_heartbeat: float = 0.0

        self.warnings: list[str] = []
        self.errors:   list[str] = []

        self.output_dir = Path(output_dir) if output_dir else Path("output")
        self._setup_logger()

    # Legacy compat property
    @property
    def mod(self) -> str:
        return self.edition

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

    def close(self) -> None:
        """Close logger file handlers. Call when done to release file locks (especially on Windows)."""
        for handler in list(self._logger.handlers):
            try:
                handler.close()
            except Exception:
                pass
        self._logger.handlers.clear()

    def _log(self, event: str, detail: str = "") -> None:
        self._logger.info(
            "build_id=%s stage=%s message_id=%s %s %s",
            self.build_id, self.current_stage, self.message_id, event, detail,
        )

    # ── Public API ────────────────────────────────────────────────────────────

    def start_build(self) -> dict:
        """Send initial build card immediately; edit if message_id already exists."""
        if not self._usable():
            return self._result("DISABLED")

        with self._state_lock:
            self.current_stage  = "STARTING"
            self.current_detail = "Build pipeline starting..."
            text = self._render_live()
            existing_id = self.message_id

        if existing_id is not None:
            result = self._do_edit(text)
            self._last_edit = time.monotonic()
            self._record_update()
            self._log("start_build reused", f"message_id={existing_id}")
            return result

        payload  = self._base_payload(text)
        response = self._post("sendMessage", payload)
        if response.get("ok") and isinstance(response.get("result"), dict):
            with self._state_lock:
                self.message_id = response["result"].get("message_id")
            self._last_edit = time.monotonic()
            self._record_update()
            self._log("start_build new", f"message_id={self.message_id}")
            return self._result("STARTED")

        err = str(response.get("error", "")) or "sendMessage failed"
        self.warnings.append("Telegram initial send failed")
        self.errors.append(err)
        with self._state_lock:
            self.last_error = err
        self._log("start_build FAILED", err)
        return self._result("SEND_FAILED")

    # Backward compat alias
    def start(self) -> dict:
        return self.start_build()

    def update_stage(
        self,
        stage: str,
        detail: str = "",
        progress: Optional[int] = None,
        force: bool = False,
        # Legacy compat positional args
        action: Optional[str] = None,
        error: Optional[str] = None,
    ) -> dict:
        """Edit live message for the given stage. Throttled to 3s unless force=True."""
        if not self._usable():
            return self._result("DISABLED")

        # Accept legacy (stage, action) positional call
        if action and not detail:
            detail = action

        canonical = _STAGE_ALIAS.get(stage, stage)
        stage_num = _STAGE_ID_TO_NUM.get(canonical)

        with self._state_lock:
            if self._is_final:
                return self._result("DISABLED")

            self.current_stage  = canonical or stage
            self.current_detail = detail or stage
            if progress is not None:
                self.current_progress = progress
            elif stage_num:
                self.current_progress = round((stage_num - 1) / _TOTAL_STAGES * 100)
            if error:
                self.last_error = error

            if not force:
                now = time.monotonic()
                if now - self._last_edit < _THROTTLE_SECONDS:
                    return self._result("THROTTLED")

            if self.message_id is None:
                return self._result("DISABLED")
            text = self._render_live()

        result = self._do_edit(text)
        self._last_edit = time.monotonic()
        self._record_update()
        self._write_status_json()
        self._log(f"update_stage={stage}", f"detail={detail!r}")
        return result

    def success(
        self,
        final_zip_name: Optional[str] = None,
        pixeldrain_link: Optional[str] = None,
        duration: Optional[float] = None,
        report_summary: Optional[str] = None,
    ) -> dict:
        """Force final COMPLETED edit. Removes loading/spinner line."""
        if not self._usable():
            return self._result("DISABLED")

        elapsed = _elapsed_str(
            duration if duration is not None else (time.monotonic() - self.started_at)
        )

        with self._state_lock:
            self._is_final     = True
            self.current_stage = "DONE"
            self.final_status  = "DONE"
            text = self._render_success(elapsed, final_zip_name, pixeldrain_link, report_summary)
            if self.message_id is None:
                return self._result("DISABLED")

        result = self._do_edit(text)
        self._last_edit = time.monotonic()
        self._record_update()
        self._log("success")
        return result

    def fail(
        self,
        stage: Optional[str] = None,
        error_summary: Optional[str] = None,
        duration: Optional[float] = None,
        reason: Optional[str] = None,
        hint: Optional[str] = None,
        raw_error: Optional[str] = None,
    ) -> dict:
        """Force final FAILED state. Always updates internal state and status JSON.
        Edits Telegram message only when enabled and message_id is set."""
        elapsed = _elapsed_str(
            duration if duration is not None else (time.monotonic() - self.started_at)
        )

        with self._state_lock:
            self._is_final     = True
            failed_stage = stage or self.current_stage
            self.current_stage = "FAILED"
            self.final_status  = "FAILED"
            err = error_summary or self.last_error or ""
            if error_summary:
                self.last_error = error_summary
            self.failure_stage  = failed_stage
            self.failure_reason = reason or err
            self.failure_hint   = hint
            self.raw_error      = raw_error or err

        self._write_status_json()
        self._log("fail", f"stage={failed_stage} reason={str(reason or err)[:100]!r}")

        if not self._usable():
            return self._result("DISABLED")

        with self._state_lock:
            text = self._render_fail(failed_stage, reason or err, elapsed, hint=hint)
            if self.message_id is None:
                return self._result("DISABLED")

        result = self._do_edit(text)
        self._last_edit = time.monotonic()
        self._record_update()
        return result

    def cancelled(self, duration: Optional[float] = None) -> dict:
        """Force final CANCELLED edit. Removes loading line."""
        if not self._usable():
            return self._result("DISABLED")

        elapsed = _elapsed_str(
            duration if duration is not None else (time.monotonic() - self.started_at)
        )

        with self._state_lock:
            self._is_final    = True
            self.final_status = "CANCELLED"
            text = self._render_cancelled(elapsed)
            if self.message_id is None:
                return self._result("DISABLED")

        result = self._do_edit(text)
        self._last_edit = time.monotonic()
        self._record_update()
        self._log("cancelled")
        return result

    def finish(
        self,
        success: bool,
        final_zip: Optional[str] = None,
        pixeldrain_link: Optional[str] = None,
        error: Optional[str] = None,
    ) -> dict:
        """Backward compat: routes to success() or fail()."""
        if success:
            return self.success(
                final_zip_name=Path(final_zip).name if final_zip else None,
                pixeldrain_link=pixeldrain_link,
            )
        return self.fail(error_summary=error)

    def report_section(self) -> dict:
        masked_chat = (self.chat_id[:4] + "****") if self.chat_id else None
        return {
            "notify_telegram":     self.enabled,
            "telegram_message_id": self.message_id,
            "previous_message_id": self.previous_message_id,
            "edit_failed": self.edit_failed,
            "replacement_message_created": self.replacement_message_created,
            "replacement_reason": self.replacement_reason,
            "last_api_error": self.last_api_error,
            "telegram_chat_id":    masked_chat,
            "first_update_time":   self.first_update_time,
            "last_update_time":    self.last_update_time,
            "final_status":        self.final_status,
        }

    def snapshot(self) -> dict:
        with self._state_lock:
            return {
                "build_id":      self.build_id,
                "stage":         self.current_stage,
                "action":        self.current_detail,
                "message_id":    self.message_id,
                "started_at":    self.started_wall,
                "elapsed":       _elapsed_str(time.monotonic() - self.started_at),
                "final_status":  self.final_status,
                "failure_stage": self.failure_stage,
                "failure_reason":self.failure_reason,
            }

    def update_fields(
        self,
        rom_format: Optional[str] = None,
        super_strategy: Optional[str] = None,
        engine: Optional[str] = None,
    ) -> None:
        """Update build metadata fields (ROM format, super strategy, engine label)."""
        if rom_format is not None:
            self.rom_format = rom_format
        if super_strategy is not None:
            self.super_strategy = super_strategy
        if engine is not None:
            self.engine = engine

    def heartbeat(self) -> dict:
        """Send a heartbeat edit if _HEARTBEAT_INTERVAL seconds have passed.

        Does NOT create a new message — only edits the existing one.
        Telegarm API failures are logged but do not raise.
        """
        if not self._usable():
            return self._result("DISABLED")
        now = time.monotonic()
        if now - self._last_heartbeat < _HEARTBEAT_INTERVAL:
            return self._result("THROTTLED")
        if self._is_final:
            return self._result("DISABLED")
        with self._state_lock:
            if self.message_id is None:
                return self._result("DISABLED")
            self._heartbeat_count += 1
            elapsed = _elapsed_str(now - self.started_at)
            detail_save = self.current_detail
            self.current_detail = f"Still working... ({elapsed})"
            text = self._render_live()
            self.current_detail = detail_save
        self._last_heartbeat = now
        result = self._do_edit(text)
        self._log("heartbeat", f"tick={self._heartbeat_count} elapsed={elapsed}")
        return result

    # ── Internals ─────────────────────────────────────────────────────────────

    def _usable(self) -> bool:
        if not self.enabled:
            return False
        if not self.token or not self.chat_id:
            if "Telegram skipped: missing secrets" not in self.warnings:
                self.warnings.append("Telegram skipped: missing secrets")
                self._logger.warning("build_id=%s Telegram skipped: missing secrets", self.build_id)
            return False
        return True

    def _write_status_json(self) -> None:
        try:
            status_dir = self.output_dir / "reports"
            status_dir.mkdir(parents=True, exist_ok=True)
            with self._state_lock:
                data = {
                    "build_id":         self.build_id,
                    "current_stage":    self.current_stage,
                    "last_stage_detail": self.current_detail,
                    "final_status":     self.final_status,
                    "failure_stage":    self.failure_stage,
                    "failure_reason":   self.failure_reason,
                    "failure_hint":     self.failure_hint,
                    "raw_error":        self.raw_error,
                    "last_update_time": self.last_update_time,
                    "message_id":       self.message_id,
                    "previous_message_id": self.previous_message_id,
                    "edit_failed":      self.edit_failed,
                    "replacement_message_created": self.replacement_message_created,
                    "replacement_reason": self.replacement_reason,
                    "last_api_error":   self.last_api_error,
                    "heartbeat_count":  self._heartbeat_count,
                }
            import json as _json
            (status_dir / "telegram_status.json").write_text(
                _json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
            )
        except Exception as exc:
            self._logger.warning("build_id=%s could not write telegram_status.json: %s", self.build_id, exc)

    def _record_update(self) -> None:
        now = _now_utc()
        if self.first_update_time is None:
            self.first_update_time = now
        self.last_update_time = now

    def _base_payload(self, text: str) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "chat_id":                  self.chat_id,
            "text":                     text[:_MAX_TEXT_LEN],
            "disable_web_page_preview": True,
        }
        if self.thread_id:
            try:
                payload["message_thread_id"] = int(self.thread_id)
            except ValueError:
                self.warnings.append("TELEGRAM_THREAD_ID is not an integer; topic skipped")
        return payload

    def _do_edit(self, text: str) -> dict:
        payload = self._base_payload(text)
        with self._state_lock:
            payload["message_id"] = self.message_id
        old_message_id = payload.get("message_id")
        self._replacement_text = text
        self._log("edit attempt", f"message_id={old_message_id}")

        response: dict = {"ok": False, "error": "no attempts made"}
        for attempt, backoff in enumerate(_RETRY_BACKOFF):
            response = self._post("editMessageText", payload)
            if response.get("ok"):
                return self._result("UPDATED" if attempt == 0 else "UPDATED_AFTER_RETRY")
            err = str(response.get("error", ""))
            # Retry only on 5xx
            is_5xx = any(code in err for code in ("500", "502", "503", "504"))
            if not is_5xx or attempt == len(_RETRY_BACKOFF) - 1:
                break
            time.sleep(backoff)

        self.warnings.append("Telegram edit failed")
        err = str(response.get("error", ""))
        with self._state_lock:
            self.edit_failed = True
            self.last_api_error = err or None
        if err:
            self.errors.append(err)
            self._logger.error(
                "build_id=%s edit failed old_message_id=%s reason=%s",
                self.build_id, old_message_id, err,
            )
        if self._is_unrecoverable_edit_error(err):
            return self._send_new_live_message(err or "edit failed")
        return self._result("EDIT_FAILED")

    @staticmethod
    def _is_unrecoverable_edit_error(error: str) -> bool:
        text = (error or "").lower()
        return any(
            marker in text
            for marker in (
                "message can't be edited",
                "message to edit not found",
                "message_id_invalid",
                "chat not found",
            )
        )

    def _send_new_live_message(self, reason: str) -> dict:
        text = getattr(self, "_replacement_text", None) or self._render_live()
        payload = self._base_payload(text)
        previous_id = self.message_id
        response = self._post("sendMessage", payload)
        if response.get("ok") and isinstance(response.get("result"), dict):
            new_id = response["result"].get("message_id")
            with self._state_lock:
                self.previous_message_id = previous_id
                self.message_id = new_id
                self.edit_failed = True
                self.replacement_message_created = True
                self.replacement_reason = reason
                self.last_api_error = reason
            self._record_update()
            self._write_status_json()
            self._export_message_id_to_github_env(new_id)
            self._logger.info(
                "build_id=%s edit failed, sent replacement live message_id=%s old_message_id=%s reason=%s",
                self.build_id, new_id, previous_id, reason,
            )
            return self._result("REPLACED")

        err = str(response.get("error", "")) or "sendMessage replacement failed"
        self.warnings.append("Telegram replacement send failed")
        self.errors.append(err)
        with self._state_lock:
            self.last_api_error = err
            self.replacement_reason = reason
        self._logger.error(
            "build_id=%s replacement send failed old_message_id=%s reason=%s send_error=%s",
            self.build_id, previous_id, reason, err,
        )
        self._write_status_json()
        return self._result("EDIT_FAILED")

    def _export_message_id_to_github_env(self, message_id: Any) -> None:
        env_path = os.environ.get("GITHUB_ENV", "").strip()
        if not env_path or message_id is None:
            return
        try:
            with open(env_path, "a", encoding="utf-8") as fh:
                fh.write(f"DEADZONE_TELEGRAM_MESSAGE_ID={message_id}\n")
        except Exception as exc:
            self._logger.warning("build_id=%s could not append GITHUB_ENV: %s", self.build_id, exc)

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
                return json.loads(body)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")

            # 400 "message is not modified" → treat as success, do not retry
            if exc.code == 400 and "message is not modified" in body.lower():
                return {"ok": True, "result": {"not_modified": True}}

            # 400 supergroup migration → retry once with new chat_id
            if exc.code == 400 and not _migration_retry:
                try:
                    err_json = json.loads(body)
                    migrate_id = (err_json.get("parameters") or {}).get("migrate_to_chat_id")
                    if migrate_id:
                        new_id = str(migrate_id)
                        self._logger.info(
                            "build_id=%s chat migrated to supergroup %s", self.build_id, new_id
                        )
                        with self._state_lock:
                            self.chat_id = new_id
                        payload = dict(payload)
                        payload["chat_id"] = new_id
                        return self._post(method, payload, _migration_retry=True)
                except Exception:
                    pass

            # 429 rate limit → respect retry_after, then retry once
            if exc.code == 429:
                retry_after = 5.0
                try:
                    err_json = json.loads(body)
                    retry_after = float(
                        (err_json.get("parameters") or {}).get("retry_after", 5)
                    )
                except Exception:
                    pass
                self._logger.warning(
                    "build_id=%s 429 rate limit, sleeping %.0fs", self.build_id, retry_after
                )
                time.sleep(retry_after)
                try:
                    with urllib.request.urlopen(req, timeout=30) as resp2:
                        body2 = resp2.read().decode("utf-8", errors="replace")
                        return json.loads(body2)
                except Exception as exc2:
                    return {"ok": False, "error": str(exc2)}

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

    # ── Message renderers ─────────────────────────────────────────────────────

    def _device_block(self) -> list[str]:
        soc_disp     = self.soc.upper() if self.soc else "Unknown"
        android_disp = self.android_version or "—"
        os_disp      = self.os_version or "—"
        lines = [
            f"Device:  {self.codename}",
            f"Edition: {self.edition.capitalize()}",
            f"Engine:  {self.engine or 'Legacy'}",
            f"SoC:     {soc_disp}",
            f"OS:      {os_disp}",
            f"Android: {android_disp}",
        ]
        if self.rom_format:
            lines.append(f"ROM:     {self.rom_format}")
        if self.super_strategy:
            lines.append(f"Super:   {self.super_strategy}")
        lines.append(f"Build:   {self.build_name}")
        return lines

    def _render_live(self) -> str:
        """Render running build message with progress bar and loading line."""
        stage    = self.current_stage
        detail   = self.current_detail
        progress = self.current_progress

        canonical  = _STAGE_ALIAS.get(stage, stage)
        stage_num  = _STAGE_ID_TO_NUM.get(canonical, 0)
        stage_label = ""
        for s, label, _ in PIPELINE_STAGES:
            if s == canonical:
                stage_label = label
                break

        if progress is None and stage_num:
            progress = round((stage_num - 1) / _TOTAL_STAGES * 100)

        elapsed = _elapsed_str(time.monotonic() - self.started_at)

        lines = [
            "DeadZone Factory",
            f"Developer: {self.developer}",
            "",
            "Status: \U0001f504 BUILDING",
        ]
        lines.extend(self._device_block())
        lines.append("")
        lines.append("Stage:")
        if stage_num:
            lines.append(f"[{stage_num}/{_TOTAL_STAGES}] {stage_label or canonical}")
        else:
            lines.append(canonical or stage)
        if detail and detail != stage:
            lines.append(detail)
        lines.append("")
        if progress is not None:
            lines.append("Progress:")
            lines.append(_progress_bar(progress))
            lines.append("")
        lines.append(f"Runtime: {elapsed}")
        lines.append(f"Last update: {_now_utc()}")
        lines.append("")
        lines.append("Warning: Do not start another build for the same device until this finishes.")
        return "\n".join(lines)

    def _render_success(
        self,
        elapsed: str,
        final_zip_name: Optional[str] = None,
        pixeldrain_link: Optional[str] = None,
        report_summary: Optional[str] = None,
    ) -> str:
        lines = [
            "DeadZone Factory",
            f"Developer: {self.developer}",
            "",
            "Status: ✅ COMPLETED",
        ]
        lines.extend(self._device_block())
        if pixeldrain_link:
            lines.extend(["", "Result:", "ROM ZIP uploaded to PixelDrain:", pixeldrain_link])
        elif final_zip_name:
            lines.extend(["", "Result:", f"ZIP: {final_zip_name}"])
        lines.extend(["", "Duration:", elapsed])
        if report_summary:
            lines.extend(["", "Summary:", report_summary])
        lines.extend(["", "Reports:", "GitHub artifact contains reports/logs only."])
        return "\n".join(lines)

    def _render_fail(
        self,
        failed_stage: str,
        error_summary: str,
        elapsed: str,
        hint: Optional[str] = None,
    ) -> str:
        canonical   = _STAGE_ALIAS.get(failed_stage, failed_stage)
        stage_label = ""
        for s, label, _ in PIPELINE_STAGES:
            if s == canonical:
                stage_label = label
                break
        display_stage = stage_label or canonical or failed_stage

        lines = [
            "DeadZone Factory",
            f"Developer: {self.developer}",
            "",
            "Status: ❌ FAILED",
        ]
        lines.extend(self._device_block())
        lines.extend(["", "Stage:", display_stage])
        if error_summary:
            lines.extend(["", "Reason:", error_summary[:400]])
        if hint:
            lines.extend(["", "Fix hint:", hint[:200]])
        lines.extend([
            "",
            f"Duration: {elapsed}",
            "",
            "Check reports artifact for full logs.",
            "",
            "Device remains safe. No flashing was performed.",
        ])
        return "\n".join(lines)

    def _render_cancelled(self, elapsed: str) -> str:
        lines = [
            "DeadZone Factory",
            f"Developer: {self.developer}",
            "",
            "Status: ⚠️ CANCELLED",
        ]
        lines.extend(self._device_block())
        lines.extend([
            "",
            f"Duration: {elapsed}",
            "",
            "Build was cancelled before completion.",
            "Device remains safe. No flashing was performed.",
        ])
        return "\n".join(lines)


# ── CLI entrypoint (used by GitHub Actions steps) ─────────────────────────────

def _cli_main() -> int:
    import argparse
    import sys

    p = argparse.ArgumentParser(description="DeadZone Telegram notifier CLI")
    p.add_argument("--soc",             default="")
    p.add_argument("--codename",        default="unknown")
    p.add_argument("--edition",         default="base")
    p.add_argument("--android-version", dest="android_version", default="")
    p.add_argument("--os-version",      dest="os_version",      default="")
    p.add_argument("--build-name",      dest="build_name",      default="")
    p.add_argument("--build-id",        dest="build_id",        default="")
    p.add_argument(
        "--action",
        choices=["start", "success", "fail", "cancelled"],
        required=True,
    )
    p.add_argument("--pixeldrain-link", dest="pixeldrain_link", default="")
    p.add_argument("--failed-stage",    dest="failed_stage",    default="")
    p.add_argument("--error-summary",   dest="error_summary",   default="")
    p.add_argument("--duration",        type=float,             default=None)
    args = p.parse_args()

    build_id = args.build_id or generate_build_id(args.soc or "unk", args.codename)
    notifier = TelegramLiveStatus(
        build_id=build_id,
        soc=args.soc,
        codename=args.codename,
        edition=args.edition,
        android_version=args.android_version or None,
        os_version=args.os_version or None,
        build_name=args.build_name or None,
    )

    if args.action == "start":
        result = notifier.start_build()
        mid = result.get("message_id")
        if mid:
            # Print ONLY the message_id so the shell can capture it
            print(mid, flush=True)
        return 0 if result["status"] not in ("SEND_FAILED",) else 1

    if args.action == "success":
        notifier.success(
            pixeldrain_link=args.pixeldrain_link or None,
            duration=args.duration,
        )
        return 0

    if args.action == "fail":
        notifier.fail(
            stage=args.failed_stage or None,
            error_summary=args.error_summary or None,
            duration=args.duration,
        )
        return 0

    if args.action == "cancelled":
        notifier.cancelled(duration=args.duration)
        return 0

    return 1


if __name__ == "__main__":
    import sys
    sys.exit(_cli_main())
