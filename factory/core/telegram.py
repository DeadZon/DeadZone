#!/usr/bin/env python3
"""Telegram status notifications for DeadZone builds.

Sends live updates to all resolved recipients (editable messages per-chat) and
broadcasts final status + log documents to all targets. Supports multiple chat IDs
via TELEGRAM_*_CHAT_IDS (comma-separated) with backward compat for single-ID secrets.

Recipient priority (MTK example):
  1. TELEGRAM_MTK_CHAT_IDS   (comma-separated, preferred)
  2. TELEGRAM_CHAT_IDS       (generic multi, fallback)
  3. TELEGRAM_MTK_CHAT_ID    (single, backward compat)
  4. TELEGRAM_CHAT_ID        (generic single, fallback)
  Plus TELEGRAM_MTK_GROUP_ID appended if not already present.
"""
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

from factory.core.workspace import Workspace, read_json, write_json


MAX_TEXT_LEN = 4000

# Human-readable labels for each pipeline stage ID.
STAGE_DISPLAY: dict[str, dict[str, str]] = {
    "image_extraction": {
        "title": "Extracting Images",
        "done_label": "Images extracted",
        "running_label": "Extracting images",
    },
    "app_inventory": {
        "title": "Scanning App Inventory",
        "done_label": "App inventory scanned",
        "running_label": "Scanning app inventory",
    },
    "stable_app_policy": {
        "title": "Applying Stable App Policy",
        "done_label": "Stable app policy applied",
        "running_label": "Applying stable app policy",
    },
    "stable_partition_rebuild": {
        "title": "Rebuilding Stable Partitions",
        "done_label": "Stable partitions rebuilt",
        "running_label": "Rebuilding stable partitions",
    },
    "pre_super_image_validation": {
        "title": "Validating Rebuilt Images",
        "done_label": "Rebuilt images validated",
        "running_label": "Validating rebuilt images",
    },
    "stable_app_normalize": {
        "title": "Normalizing Stable Apps",
        "done_label": "Stable apps normalized",
        "running_label": "Normalizing stable apps",
    },
    "inventory_package": {
        "title": "Building Inventory Package",
        "done_label": "Inventory package built",
        "running_label": "Building inventory package",
    },
    "size_reduction": {
        "title": "Checking Size Policy",
        "done_label": "Size reduction checked",
        "running_label": "Checking size policy",
    },
    "super_profile": {
        "title": "Loading Super Profile",
        "done_label": "Super profile loaded",
        "running_label": "Loading super profile",
    },
    "style": {
        "title": "Applying Style Patches",
        "done_label": "Style patches applied",
        "running_label": "Applying style patches",
    },
    "repack": {
        "title": "Repacking Partitions",
        "done_label": "Partitions repacked",
        "running_label": "Repacking partitions",
    },
    "super": {
        "title": "Building Super Image",
        "done_label": "Super image built",
        "running_label": "Building super image",
    },
    "fastboot_validation": {
        "title": "Validating Fastboot Package",
        "done_label": "Fastboot package validated",
        "running_label": "Validating fastboot package",
    },
    "zip_package": {
        "title": "Packaging Fastboot ZIP",
        "done_label": "ZIP packaged",
        "running_label": "Packaging fastboot ZIP",
    },
    "upload": {
        "title": "Uploading to PixelDrain",
        "done_label": "PixelDrain upload done",
        "running_label": "Uploading to PixelDrain",
    },
    "final_report": {
        "title": "Writing Final Reports",
        "done_label": "Reports written",
        "running_label": "Writing final reports",
    },
}

# Ordered list of stages shown in the timeline block.
_TIMELINE_STAGES = [
    "image_extraction",
    "app_inventory",
    "stable_app_policy",
    "stable_partition_rebuild",
    "pre_super_image_validation",
    "stable_app_normalize",
    "inventory_package",
    "size_reduction",
    "super_profile",
    "style",
    "repack",
    "super",
    "fastboot_validation",
    "zip_package",
    "upload",
    "final_report",
]


def _stage_title(stage_id: str) -> str:
    return STAGE_DISPLAY.get(stage_id, {}).get("title", stage_id)


MAX_DOCUMENT_BYTES = int(os.environ.get("TELEGRAM_MAX_DOCUMENT_BYTES", str(50 * 1024 * 1024)))
_TELEGRAM_THROTTLE_SECONDS = float(os.environ.get("TELEGRAM_THROTTLE_SECONDS", "5"))
_TELEGRAM_MIN_UPDATE_SECONDS = 8.0


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


def _mask_chat_id(chat_id: str) -> str:
    """Return a masked version of a chat ID for safe logging (e.g. ***6789)."""
    s = str(chat_id or "")
    if not s:
        return "(empty)"
    if len(s) <= 4:
        return "***"
    return f"***{s[-4:]}"


def _parse_chat_ids(raw: str) -> list[str]:
    """Parse comma-separated chat IDs — trimmed, deduplicated, non-empty."""
    seen: set[str] = set()
    result: list[str] = []
    for cid in raw.split(","):
        cid = cid.strip()
        if cid and cid not in seen:
            seen.add(cid)
            result.append(cid)
    return result


def _resolve_recipients_with_source(soc: str | None) -> tuple[list[str], str]:
    """Return (chat_id_list, env_var_used) for the given SoC.

    Uses priority fallback: SOC-specific CHAT_IDS → generic CHAT_IDS →
    SOC-specific CHAT_ID → generic CHAT_ID. Group IDs (TELEGRAM_*_GROUP_ID)
    are appended as extra targets for backward compatibility.
    """
    key = (soc or "").strip().lower()

    if key == "mtk":
        primary_vars = [
            "TELEGRAM_MTK_CHAT_IDS",
            "TELEGRAM_CHAT_IDS",
            "TELEGRAM_MTK_CHAT_ID",
            "TELEGRAM_CHAT_ID",
        ]
        extra_vars = ["TELEGRAM_MTK_GROUP_ID"]
    elif key == "snapdragon":
        primary_vars = [
            "TELEGRAM_SNAPDRAGON_CHAT_IDS",
            "TELEGRAM_CHAT_IDS",
            "TELEGRAM_SNAPDRAGON_CHAT_ID",
            "TELEGRAM_CHAT_ID",
        ]
        extra_vars = ["TELEGRAM_SNAPDRAGON_GROUP_ID"]
    else:
        primary_vars = [
            "TELEGRAM_CHAT_IDS",
            "TELEGRAM_CHAT_ID",
        ]
        extra_vars = []

    # Use first env var that contains a non-empty value
    primary_ids: list[str] = []
    source_var = ""
    for var in primary_vars:
        raw = os.environ.get(var, "").strip()
        if raw:
            primary_ids = _parse_chat_ids(raw)
            source_var = var
            break

    # Append group IDs (backward compat) if not already present
    seen = set(primary_ids)
    result = list(primary_ids)
    for var in extra_vars:
        raw = os.environ.get(var, "").strip()
        if raw and raw not in seen:
            seen.add(raw)
            result.append(raw)

    return result, source_var


def resolve_telegram_recipients(soc: str | None = None) -> list[str]:
    """Return deduplicated list of chat IDs for the given SoC, in priority order.

    Supports negative group chat IDs. Trims whitespace. Deduplicates.
    Old single-ID secrets (TELEGRAM_CHAT_ID etc.) remain fully supported.
    Never reads or prints TELEGRAM_BOT_TOKEN.
    """
    recipients, _ = _resolve_recipients_with_source(soc)
    return recipients


def _bot_token_for_soc(soc: str) -> str:
    """Return the bot token for the given SoC."""
    key = soc.strip().lower()
    if key == "mtk":
        return _env_first("TELEGRAM_MTK_BOT_TOKEN", "TELEGRAM_BOT_TOKEN")
    if key == "snapdragon":
        return _env_first("TELEGRAM_SNAPDRAGON_BOT_TOKEN", "TELEGRAM_BOT_TOKEN")
    return _env_first("TELEGRAM_BOT_TOKEN")


def _credentials_for_soc(soc: str) -> tuple[str, str]:
    """Return (bot_token, primary_chat_id) — kept for backward compat."""
    token = _bot_token_for_soc(soc)
    recipients = resolve_telegram_recipients(soc)
    chat_id = recipients[0] if recipients else ""
    return token, chat_id


def _display_source(value: str) -> str:
    raw = str(value or "").strip()
    parsed = urlparse(raw)
    if parsed.scheme and parsed.netloc:
        name = Path(parsed.path).name
        return f"{parsed.netloc}/{name}" if name else parsed.netloc
    return Path(raw).name or "(none)"


def _float_env(name: str, default: float) -> float:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        return default


def _default_update_interval() -> float:
    default = 20.0 if os.environ.get("GITHUB_ACTIONS", "").lower() == "true" else 15.0
    stage_raw = os.environ.get("DEADZONE_TELEGRAM_STAGE_UPDATE_INTERVAL_SECONDS", "").strip()
    if stage_raw:
        return _float_env("DEADZONE_TELEGRAM_STAGE_UPDATE_INTERVAL_SECONDS", default)
    return _float_env("DEADZONE_TELEGRAM_UPDATE_INTERVAL_SECONDS", default)


def _parse_error_summary(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in str(text or "").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().lower()
        if key in {"status", "failed stage", "title", "reason", "recommendation", "hint"}:
            fields[key] = value.strip()
    return fields


def _meaningful_hint(value: object) -> str:
    hint = _ascii(value).strip()
    if len(hint) <= 1:
        return ""
    if ":" in hint and hint.lower().split(":", 1)[0] in {"status", "failed stage", "title", "reason", "recommendation", "hint"}:
        return ""
    return hint


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
        self.token = _bot_token_for_soc(soc)
        self._recipients, self._recipient_source = _resolve_recipients_with_source(soc)
        # Primary chat ID — first recipient or empty; kept for backward compat
        self.chat_id = self._recipients[0] if self._recipients else ""
        self.thread_id = _env_first("TELEGRAM_THREAD_ID", "TELEGRAM_MESSAGE_THREAD_ID")
        self.started_at = time.monotonic()
        self._classified_error: dict = {}
        self.events: list[dict[str, str]] = []
        self.warnings: list[str] = []
        self.errors: list[str] = []
        self.status = "not requested"
        self.enabled = False
        self.attempted = False
        # Per-chat message IDs: {chat_id: message_id}
        self._message_ids: dict[str, int] = self._existing_message_ids()
        self._last_edit_at: float = 0.0
        self._last_stage: str = ""
        self._update_interval_seconds = _default_update_interval()
        # Per-run send/edit tracking for debug report
        self._sent_chats: list[str] = []
        self._edited_chats: list[str] = []
        self._failed_chats: list[tuple[str, str]] = []

    # ── Recipient helpers ────────────────────────────────────────────────────

    def _all_recipients(self) -> list[str]:
        """Return all resolved chat IDs. Falls back to self.chat_id for test compat."""
        if self._recipients:
            return list(self._recipients)
        # Fallback: chat_id may have been set directly (e.g. in tests)
        return [self.chat_id] if self.chat_id else []

    # ── Backward-compat message_id property ─────────────────────────────────

    @property
    def message_id(self) -> int | None:
        """Primary chat's message ID (backward compat — use _message_ids for multi-chat)."""
        primary = self.chat_id
        if primary and primary in self._message_ids:
            return self._message_ids[primary]
        if self._message_ids:
            return next(iter(self._message_ids.values()))
        return None

    @message_id.setter
    def message_id(self, value: int | None) -> None:
        primary = self.chat_id
        if value is not None and primary:
            self._message_ids[primary] = int(value)
        elif value is None and primary and primary in self._message_ids:
            del self._message_ids[primary]

    # ── Backward-compat helpers (kept for any callers) ───────────────────────

    def _all_personal_chat_ids(self) -> list[str]:
        return self._all_recipients()

    def _all_broadcast_targets(self) -> list[str]:
        return self._all_recipients()

    # ── Lifecycle ────────────────────────────────────────────────────────────

    def start(self) -> TelegramResult:
        if not self.requested:
            return self.result("not requested")
        recipients = self._all_recipients()
        if not self.token or not recipients:
            self.status = "skipped"
            self.warnings.append("Telegram credentials are missing; status notifications skipped")
            print("[TELEGRAM] Status: skipped; missing TELEGRAM_BOT_TOKEN / chat ID")
            return self.result("skipped")
        self.enabled = True
        self.add_event("build started", "RUN")
        self.attempted = True
        text = self._format("RUNNING")
        any_ok = False
        for chat_id in recipients:
            existing = self._message_ids.get(chat_id)
            if existing is not None:
                response = self._edit_chat(chat_id, existing, text)
            else:
                response = self._send_to(chat_id, text)
            if response.get("ok"):
                any_ok = True
                result_data = response.get("result") or {}
                if isinstance(result_data, dict):
                    msg_id = result_data.get("message_id")
                    if msg_id is not None:
                        self._message_ids[chat_id] = int(msg_id)
            else:
                err = str(response.get("error") or "initial Telegram send failed")
                self.errors.append(f"initial send failed for {_mask_chat_id(chat_id)}: {err}")
                self._failed_chats.append((chat_id, err))
        if any_ok:
            self.status = "running"
            self._last_edit_at = time.monotonic()
            self._save_message_id()
            active = len(self._message_ids)
            print(f"[TELEGRAM] Status: running (recipients={len(recipients)}, active={active})")
            return self.result("running")
        self.status = "failed"
        print("[TELEGRAM] Status: initial send failed for all recipients")
        return self.result("failed")

    def add_event(self, name: str, status: str, detail: str = "") -> TelegramResult:
        if not self.requested:
            return self.result("not requested")
        clean_status = status.upper()
        self.events.append({"name": name, "status": clean_status, "detail": detail})
        if not self.enabled or not self._message_ids:
            return self.result(self.status)
        now = time.monotonic()
        stage_changed = clean_status == "RUN" and name != self._last_stage
        stable_summary_ready = name == "stable_app_policy" and clean_status == "OK"
        if stage_changed:
            self._last_stage = name
        elapsed = now - self._last_edit_at if self._last_edit_at else self._update_interval_seconds
        force = stage_changed or stable_summary_ready
        reason = "stable_app_policy_summary" if stable_summary_ready else ("stage_changed" if stage_changed else "interval")
        min_seconds = max(_TELEGRAM_MIN_UPDATE_SECONDS, float(_TELEGRAM_THROTTLE_SECONDS))
        if not force and elapsed < min_seconds:
            print(f"[TELEGRAM] skipped update: reason=throttle elapsed={elapsed:.0f}s")
            return self.result(self.status)
        if not force and elapsed < self._update_interval_seconds:
            return self.result(self.status)
        if reason == "interval":
            print(f"[TELEGRAM] edit live message: reason=interval stage={name} elapsed={elapsed:.0f}s")
        else:
            print(f"[TELEGRAM] edit live message: reason={reason} stage={name}")
        text = self._format("RUNNING")
        any_ok = False
        for chat_id, msg_id in list(self._message_ids.items()):
            response = self._edit_chat(chat_id, msg_id, text)
            if response.get("ok"):
                any_ok = True
                self._edited_chats.append(chat_id)
            else:
                # Fallback: send a new message so this chat stays updated
                fallback = self._send_to(chat_id, text)
                if fallback.get("ok"):
                    any_ok = True
                    result_data = fallback.get("result") or {}
                    if isinstance(result_data, dict) and result_data.get("message_id"):
                        self._message_ids[chat_id] = int(result_data["message_id"])
                    self._sent_chats.append(chat_id)
                else:
                    err = str(response.get("error") or "Telegram update failed")
                    self.errors.append(f"update failed for {_mask_chat_id(chat_id)}: {err}")
                    self._failed_chats.append((chat_id, err))
        if any_ok:
            self._last_edit_at = time.monotonic()
            self.status = "updated"
            return self.result("updated")
        self.status = "failed"
        print("[TELEGRAM] Status: update failed for all recipients")
        return self.result("failed")

    def finish(
        self,
        final_status: str,
        final_zip: Path | None = None,
        upload_url: str = "",
        failed_stage: str = "",
        error_summary: str = "",
        classified_error: dict | None = None,
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
        self._classified_error = classified_error or {}
        self.events.append({"name": "final status", "status": final_status.upper(), "detail": detail})
        if not self.enabled:
            return self.result(self.status)
        text = self._format(final_status.upper(), final_zip=final_zip, upload_url=upload_url)
        self.attempted = True
        reason = "final_success" if final_status.upper() == "OK" else "final_failure"
        print(f"[TELEGRAM] edit live message: reason={reason}")
        if not self._message_ids:
            self.errors.append("Telegram final update skipped because no live message_id map exists")
            self.status = "failed"
            return self.result("failed")
        any_ok = False
        for chat_id, msg_id in list(self._message_ids.items()):
            response = self._edit_chat(chat_id, msg_id, text)
            if response.get("ok"):
                any_ok = True
                result_data = response.get("result") or {}
                if isinstance(result_data, dict) and result_data.get("message_id") is not None:
                    self._message_ids[chat_id] = int(result_data["message_id"])
                self._edited_chats.append(chat_id)
            else:
                # One chat failed to edit — fall back to sendMessage for it
                fallback = self._send_to(chat_id, text)
                if fallback.get("ok"):
                    any_ok = True
                    result_data = fallback.get("result") or {}
                    if isinstance(result_data, dict) and result_data.get("message_id") is not None:
                        self._message_ids[chat_id] = int(result_data["message_id"])
                    self._sent_chats.append(chat_id)
                else:
                    err = str(response.get("error") or "Telegram final update failed")
                    self.errors.append(f"final update failed for {_mask_chat_id(chat_id)}: {err}")
                    self._failed_chats.append((chat_id, err))
        # Send to any recipients that never got a live message (e.g. added after start)
        for chat_id in self._all_recipients():
            if chat_id not in self._message_ids:
                extra = self._send_to(chat_id, text)
                if extra.get("ok"):
                    any_ok = True
                    result_data = extra.get("result") or {}
                    if isinstance(result_data, dict) and result_data.get("message_id") is not None:
                        self._message_ids[chat_id] = int(result_data["message_id"])
                    self._sent_chats.append(chat_id)
        if any_ok:
            self.status = "completed" if final_status.upper() == "OK" else "failed"
            self._save_message_id()
            print(f"[TELEGRAM] Status: {self.status}")
        else:
            self.status = "failed"
            print("[TELEGRAM] Status: final update failed for all recipients")

        # On failure: send log files as documents to all targets
        if final_status.upper() not in {"OK", "DONE"}:
            self._send_failure_documents()

        return self.result(self.status)

    def _send_failure_documents(self) -> None:
        """Send log files as documents to all targets on build failure."""
        reports_dir = self.workspace.reports
        log_files = [
            reports_dir / "stable_matching_debug_report.txt",
            reports_dir / "stable_package_scan_report.json",
        ]
        build_log = Path("/mnt/dz_data/build.log")
        if build_log.is_file():
            log_files.append(build_log)

        targets = self._all_recipients()
        for log_path in log_files:
            if not log_path.is_file():
                continue
            size = log_path.stat().st_size
            if size > MAX_DOCUMENT_BYTES:
                self.warnings.append(f"Log file too large to send: {log_path.name} ({size} bytes)")
                continue
            caption = f"Build failure log: {log_path.name}"
            for chat_id in targets:
                self._send_document_to(chat_id, log_path, caption)

    def _send_document_to(self, chat_id: str, path: Path, caption: str) -> dict[str, Any]:
        """Send a document to a specific chat ID."""
        fields: dict[str, Any] = {
            "chat_id": chat_id,
            "caption": _ascii(caption)[:1024],
        }
        if self.thread_id:
            try:
                fields["message_thread_id"] = int(self.thread_id)
            except ValueError:
                pass
        return self._post_multipart("sendDocument", fields, "document", path)

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
        style_label = _ascii(self.style) or "Unknown"
        caption_parts = [
            f"{style_label} App Inventory generated",
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
        targets = self._all_recipients()
        for chat_id in targets:
            self._send_document_to(chat_id, inventory_zip, caption)
        self.attempted = True
        self.events.append({"name": "app inventory document", "status": "OK", "detail": inventory_zip.name})
        self.status = "updated"
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

    def write_report(self) -> TelegramResult:
        """Write a debug report about recipient resolution and notification activity."""
        report_path = self.workspace.reports / "telegram_recipients_debug.txt"
        try:
            report_path.parent.mkdir(parents=True, exist_ok=True)
            recipients = self._all_recipients()
            lines = [
                "Telegram Recipients Debug Report",
                "================================",
                f"soc: {_ascii(self.soc)}",
                f"env_source: {self._recipient_source or '(none)'}",
                f"recipient_count: {len(recipients)}",
                f"masked_recipients: {[_mask_chat_id(c) for c in recipients]}",
                f"notifier_mode: {'multi' if len(recipients) > 1 else 'single'}",
                f"message_id_map_exists: {bool(self._message_ids)}",
                f"message_id_map: { {_mask_chat_id(k): v for k, v in self._message_ids.items()} }",
                "",
                "Per-chat notification actions:",
            ]
            for chat_id in recipients:
                masked = _mask_chat_id(chat_id)
                if chat_id in self._message_ids:
                    lines.append(f"  {masked}: tracked (msg_id={self._message_ids[chat_id]})")
                else:
                    lines.append(f"  {masked}: no message_id (not reached by start)")
            if self._edited_chats:
                lines.append(f"editMessageText sent to: {[_mask_chat_id(c) for c in self._edited_chats]}")
            if self._sent_chats:
                lines.append(f"sendMessage sent to: {[_mask_chat_id(c) for c in self._sent_chats]}")
            if self._failed_chats:
                lines.append("Failed recipients:")
                for chat_id, err in self._failed_chats:
                    lines.append(f"  {_mask_chat_id(chat_id)}: {err[:120]}")
            lines.append("")
            lines.append(f"final_status: {self.status}")
            report_path.write_text("\n".join(lines), encoding="utf-8")
        except Exception as exc:
            self.warnings.append(f"Could not write telegram debug report: {exc}")
        return self.result(self.status)

    # ── Persistence ──────────────────────────────────────────────────────────

    def _existing_message_ids(self) -> dict[str, int]:
        """Load per-chat message ID map from disk/env, with backward compat."""
        stored = read_json(self.workspace.meta / "telegram_status.json", {})

        # New format: {"message_ids": {"chat_id": msg_id, ...}}
        if isinstance(stored.get("message_ids"), dict):
            result: dict[str, int] = {}
            for cid, mid in stored["message_ids"].items():
                try:
                    result[str(cid)] = int(mid)
                except (ValueError, TypeError):
                    pass
            if result:
                return result

        # Old format: single message_id from env or JSON
        raw = os.environ.get("DEADZONE_TELEGRAM_MESSAGE_ID", "").strip()
        if not raw:
            raw = str(stored.get("message_id") or "").strip()
        if raw:
            try:
                msg_id = int(raw)
                primary = self.chat_id
                if primary:
                    return {primary: msg_id}
            except ValueError:
                self.warnings.append("DEADZONE_TELEGRAM_MESSAGE_ID is not an integer; sending a new message")
        return {}

    def _save_message_id(self) -> None:
        if not self._message_ids:
            return
        write_json(
            self.workspace.meta / "telegram_status.json",
            {
                "message_ids": self._message_ids,
                "message_id": self.message_id,  # backward compat
                "chat_id": self.chat_id,
                "status": self.status,
            },
        )

    # ── Low-level send helpers ───────────────────────────────────────────────

    def _send_to(self, chat_id: str, text: str) -> dict[str, Any]:
        """Send a new message to a specific chat."""
        payload: dict[str, Any] = {
            "chat_id": chat_id,
            "text": str(text)[:MAX_TEXT_LEN],
            "disable_web_page_preview": True,
        }
        if self.thread_id:
            try:
                payload["message_thread_id"] = int(self.thread_id)
            except ValueError:
                if "Telegram thread id is not an integer; topic support skipped" not in self.warnings:
                    self.warnings.append("Telegram thread id is not an integer; topic support skipped")
        return self._post("sendMessage", payload)

    def _edit_chat(self, chat_id: str, msg_id: int, text: str) -> dict[str, Any]:
        """Edit an existing message for a specific chat. Returns response dict."""
        payload: dict[str, Any] = {
            "chat_id": chat_id,
            "message_id": msg_id,
            "text": str(text)[:MAX_TEXT_LEN],
            "disable_web_page_preview": True,
        }
        if self.thread_id:
            try:
                payload["message_thread_id"] = int(self.thread_id)
            except ValueError:
                pass
        response = self._post("editMessageText", payload)
        if not response.get("ok"):
            self.warnings.append(f"Telegram edit failed for {_mask_chat_id(chat_id)}; will fallback to sendMessage")
        return response

    # ── Kept for backward compat (tests mock _post directly) ────────────────

    def _base_payload(self, text: str) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "chat_id": self.chat_id,
            "text": str(text)[:MAX_TEXT_LEN],
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
        self.warnings.append("Telegram edit failed; live status message was not replaced")
        return response

    def _post(self, method: str, payload: dict[str, Any]) -> dict[str, Any]:
        url = f"https://api.telegram.org/bot{self.token}/{method}"
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
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
        status_upper = build_status.upper()
        is_running = status_upper == "RUNNING"
        is_done = status_upper in {"OK", "DONE"}
        is_failed = not is_running and not is_done

        state_data = read_json(self.workspace.root.parent / "state" / "build_state.json", {})
        counters = state_data.get("counters", {})

        # Collapse events: name -> latest {status, detail}
        collapsed: dict[str, dict[str, str]] = {}
        for event in self.events:
            name = event.get("name", "")
            if name:
                collapsed[name] = {
                    "status": event.get("status", ""),
                    "detail": event.get("detail", ""),
                }

        # Elapsed time
        elapsed_secs = int(max(0, time.monotonic() - self.started_at))
        minutes, seconds = divmod(elapsed_secs, 60)
        elapsed_str = f"{minutes:02d}:{seconds:02d}"

        # Build metadata (prefer live state file, fall back to self)
        style = _ascii(state_data.get("edition") or self.style)
        device = _ascii(state_data.get("device") or self.device or "Detecting...")
        soc = _ascii(state_data.get("soc") or self.soc)
        rom = _ascii(state_data.get("rom_version") or self.rom_source)
        build_id = _ascii(state_data.get("build_id") or "")

        lines: list[str] = []

        # ── HEADER ──────────────────────────────────────────────────────────
        if is_done:
            lines.append("✅ DeadZone Build Completed")
        elif is_failed:
            lines.append("❌ DeadZone Build Failed")
        else:
            lines.append("🔥 DeadZone Factory Live")
        lines.append("")
        if build_id:
            lines.append(f"Build: {build_id}")
        lines.append(f"Style: {style}")
        lines.append(f"Device: {device}")
        lines.append(f"SoC: {soc}")
        lines.append(f"ROM: {rom}")
        lines.append(f"Status: {'RUNNING' if is_running else ('DONE' if is_done else 'FAILED')}")
        lines.append(f"Elapsed: {elapsed_str}")

        # ── CURRENT STAGE BLOCK (running only) ──────────────────────────────
        if is_running:
            current_stage_id = ""
            for sid in _TIMELINE_STAGES:
                if collapsed.get(sid, {}).get("status") == "RUN":
                    current_stage_id = sid
                    break
            if not current_stage_id:
                bs_stage = state_data.get("current_stage", "")
                if bs_stage and collapsed.get(bs_stage, {}).get("status") not in {"OK", "FAIL"}:
                    current_stage_id = bs_stage
            if current_stage_id:
                lines.append("")
                lines.append(f"▶ {_stage_title(current_stage_id)}")

            # Progress bar
            progress = float(state_data.get("progress", 0.0))
            if progress > 0:
                bar_width = 20
                filled = int(min(bar_width, max(0, progress / 100.0 * bar_width)))
                bar = "█" * filled + "░" * (bar_width - filled)
                lines.append(f"Progress: {progress:.0f}% [{bar}]")

            # Current action / last event from live state
            current_action = _ascii(state_data.get("current_action") or "")
            if current_action:
                lines.append(f"Action: {current_action}")
            last_event = _ascii(state_data.get("last_event") or "")
            if last_event:
                lines.append(f"Last event: {last_event}")

        # ── STABLE APP POLICY BLOCK ─────────────────────────────────────────
        policy_report = read_json(self.workspace.reports / "stable_app_policy_report.json", {})
        policy_summary = policy_report.get("summary") if isinstance(policy_report.get("summary"), dict) else {}
        stable_kept = int(policy_summary.get("kept_apps", counters.get("stable_kept_apps", 0)) or 0)
        stable_renamed = int(policy_summary.get("renamed_apps", counters.get("stable_renamed_apps", 0)) or 0)
        stable_missing = int(policy_summary.get("missing_apps", counters.get("stable_missing_apps", 0)) or 0)
        stable_deleted = int(policy_summary.get("deleted_extra_apps", counters.get("stable_deleted_extra_apps", 0)) or 0)
        stable_skipped_delete = int(policy_summary.get("skipped_delete_apps", 0) or 0)
        stable_unknown = int(policy_summary.get("unknown_package_apps", 0) or 0)
        if (policy_report or any([stable_kept, stable_renamed, stable_missing, stable_deleted])) and any([stable_kept, stable_renamed, stable_missing, stable_deleted, stable_skipped_delete, stable_unknown]):
            lines.append("")
            lines.append("Stable App Policy:")
            lines.append(f"✅ Kept: {stable_kept}")
            lines.append(f"🔁 Renamed: {stable_renamed}")
            lines.append(f"⚠️ Missing: {stable_missing}")
            lines.append(f"🧹 Deleted extra: {stable_deleted}")
            lines.append(f"⏭ Skipped delete: {stable_skipped_delete}")
            lines.append(f"❔ Unknown package: {stable_unknown}")

        rebuild_report = read_json(self.workspace.reports / "stable_partition_rebuild_report.json", {})
        rebuild_entries = rebuild_report.get("partitions") if isinstance(rebuild_report.get("partitions"), list) else []
        if rebuild_entries:
            lines.append("")
            if rebuild_report.get("status") == "failed":
                lines.append("❌ Partition Rebuild Failed")
                err = rebuild_report.get("error") if isinstance(rebuild_report.get("error"), dict) else {}
                if err.get("error_type"):
                    lines.append(f"Error type: {_ascii(err.get('error_type'))}")
                if err.get("cause"):
                    lines.append(f"Cause: {_ascii(err.get('cause'))}")
                if err.get("suggested_fix"):
                    lines.append(f"Suggested fix: {_ascii(err.get('suggested_fix'))}")
            else:
                lines.append("Partition Rebuild:")
                for entry in rebuild_entries:
                    if entry.get("status") == "rebuilt":
                        lines.append(f"✅ {entry.get('partition')}.img rebuilt: {entry.get('size_before')} → {entry.get('size_after')}")

        # ── TIMELINE BLOCK (running only) ────────────────────────────────────
        if is_running:
            timeline_lines: list[str] = []
            running_idx = -1
            for i, sid in enumerate(_TIMELINE_STAGES):
                if collapsed.get(sid, {}).get("status") == "RUN":
                    running_idx = i
                    break
            for i, sid in enumerate(_TIMELINE_STAGES):
                info = STAGE_DISPLAY.get(sid)
                if info is None:
                    continue
                col_status = collapsed.get(sid, {}).get("status", "")
                if col_status == "OK":
                    timeline_lines.append(f"✅ {info['done_label']}")
                elif col_status == "RUN":
                    timeline_lines.append(f"🔄 {info['running_label']}")
                elif col_status == "FAIL":
                    timeline_lines.append(f"❌ {info['title']}")
                elif running_idx >= 0 and i > running_idx:
                    timeline_lines.append(f"⏳ {info['title']}")
            if timeline_lines:
                lines.append("")
                lines.append("Timeline:")
                lines.extend(timeline_lines)

        # ── DONE-SPECIFIC BLOCK ─────────────────────────────────────────────
        if is_done:
            if upload_url:
                lines.append("")
                lines.append(f"PixelDrain: {_ascii(upload_url)}")
            lines.append("Reports generated ✅")

        # ── FAILED-SPECIFIC BLOCK ───────────────────────────────────────────
        if is_failed:
            failed_stage = _ascii(self.failed_stage)
            if failed_stage:
                lines.append("")
                lines.append(f"Failed stage: {_stage_title(failed_stage)}")
            parsed = _parse_error_summary(self.error_summary)
            ce = self._classified_error or {}
            error_type = _ascii(ce.get("error_type", "") or "BUILD_FAILED")
            cause = _ascii(ce.get("cause", "") or parsed.get("reason", "") or self.error_summary).strip()
            suggested_fix = _ascii(ce.get("suggested_fix", "") or parsed.get("recommendation", "")).strip()
            suggested_check = _meaningful_hint(ce.get("suggested_check") or parsed.get("hint"))
            if not suggested_check:
                suggested_check = suggested_fix
            if error_type:
                lines.append(f"Error type: {error_type}")
            if cause:
                lines.append(f"Cause: {cause[:200]}")
            if suggested_fix:
                lines.append(f"Suggested fix: {suggested_fix[:200]}")
            if suggested_check:
                lines.append(f"Suggested check: {suggested_check[:200]}")
            if failed_stage == "size_policy":
                size_policy = read_json(self.workspace.meta / "size_policy.json", {})
                if size_policy.get("final_zip_size") is not None:
                    lines.append(f"Final ZIP size: {size_policy.get('final_zip_size')}")
                if size_policy.get("final_zip_max_allowed") or size_policy.get("final_zip_max_bytes"):
                    lines.append(f"Limit: {size_policy.get('final_zip_max_allowed') or size_policy.get('final_zip_max_bytes')}")

        return "\n".join(lines)
