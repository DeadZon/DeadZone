"""DeadZone Fly Telegram notification helper.

Behavior (matches OrangeFox-Action-Builder pattern):
- If TELEGRAM_MSG_ID env is set: uses editMessageText to update existing message.
- If TELEGRAM_MSG_ID is not set: sends a new message via sendMessage and writes
  the returned message_id to output/reports/telegram_status.json.
- TELEGRAM_GROUP_ID: only used for group_success / group_failed final messages.
- All private messages update the same single message — no duplicates.

Usage:
  python3 scripts/deadzone_fly_telegram.py \
    --action start|update|failed|group_success \
    --detail "Stage description" \
    --codename garnet \
    --soc snapdragon \
    --edition free \
    --mode execute \
    --listmezo-mode dry_run \
    --elapsed "2m 30s"
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

# ── Progress bar ──────────────────────────────────────────────────────────────

_STAGES = [
    ("queued",               0),
    ("booting",              5),
    ("validating",          10),
    ("downloading",         20),
    ("unpacking",           30),
    ("listmezo",            45),
    ("repacking",           60),
    ("super",               70),
    ("packaging",           80),
    ("uploading",           90),
    ("done",               100),
    ("failed",             100),
]

_STAGE_LABELS = {
    "queued":       "Queued",
    "booting":      "Booting Fly machine",
    "validating":   "Validating inputs",
    "downloading":  "Downloading ROM",
    "unpacking":    "Unpacking ROM",
    "listmezo":     "Running ListMezo",
    "repacking":    "Repacking partitions",
    "super":        "Rebuilding super.img",
    "packaging":    "Packaging fastboot ZIP",
    "uploading":    "Uploading to PixelDrain",
    "done":         "Build complete",
    "failed":       "Build failed",
    "update":       "In progress",
    "start":        "Booting Fly machine",
    "group_success":"Build complete",
    "group_failed": "Build failed",
}

_STAGE_PROGRESS = dict(_STAGES)


def _progress_bar(pct: int, width: int = 10) -> str:
    filled = round(width * pct / 100)
    return "[" + "█" * filled + "░" * (width - filled) + "]"


def _stage_pct(action: str) -> int:
    return _STAGE_PROGRESS.get(action, 50)


# ── Message formatting ────────────────────────────────────────────────────────

def _build_message(
    action: str,
    detail: str,
    codename: str,
    soc: str,
    edition: str,
    mode: str,
    listmezo_mode: str,
    elapsed: str,
    pixeldrain_url: str = "",
    github_run_url: str = "",
    zip_size: str = "",
    error_reason: str = "",
) -> str:
    pct = _stage_pct(action)
    bar = _progress_bar(pct)
    status_label = _STAGE_LABELS.get(action, detail or action)
    if detail and action not in ("done", "failed", "group_success", "group_failed"):
        status_label = detail

    lm_display = listmezo_mode if listmezo_mode else "off"

    lines = [
        "🔧 <b>DeadZone Fly Build</b>",
        "",
        f"📱 Device: <code>{codename}</code>",
        f"⚙️  SoC: <code>{soc}</code>",
        f"🎮 Edition: <code>{edition}</code>",
        f"🔄 Mode: <code>{mode}</code>",
        f"📋 ListMezo: <code>{lm_display}</code>",
        "",
        f"📊 Status: <b>{status_label}</b>",
        f"📈 Progress: {bar} {pct}%",
        f"⏱️  Elapsed: {elapsed}",
    ]

    if action in ("done", "group_success") or pct == 100 and action != "failed":
        lines.append("")
        lines.append("✅ <b>Build succeeded!</b>")
        if pixeldrain_url:
            lines.append(f"📥 Download: {pixeldrain_url}")
        if github_run_url:
            lines.append(f"🔗 Run: {github_run_url}")
        if zip_size:
            lines.append(f"📦 ZIP size: {zip_size}")

    elif action in ("failed", "group_failed"):
        lines.append("")
        lines.append("❌ <b>Build failed!</b>")
        if error_reason:
            lines.append(f"💬 Reason: {error_reason[:200]}")
        if github_run_url:
            lines.append(f"🔗 Logs: {github_run_url}")
        lines.append("📁 Artifacts: check GitHub Actions run for full logs.")

    return "\n".join(lines)


# ── Telegram API ──────────────────────────────────────────────────────────────

def _api_call(token: str, method: str, payload: dict) -> dict:
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {"ok": False, "error_code": exc.code, "description": body}
    except Exception as exc:
        return {"ok": False, "description": str(exc)}


def _send_message(token: str, chat_id: str, text: str, parse_mode: str = "HTML") -> dict:
    return _api_call(token, "sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True,
    })


def _edit_message(token: str, chat_id: str, message_id: int, text: str, parse_mode: str = "HTML") -> dict:
    return _api_call(token, "editMessageText", {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True,
    })


# ── Status JSON ───────────────────────────────────────────────────────────────

_STATUS_PATH = Path("output/reports/telegram_status.json")


def _load_status() -> dict:
    if _STATUS_PATH.exists():
        try:
            return json.loads(_STATUS_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _save_status(data: dict) -> None:
    _STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    _STATUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


# ── Main ──────────────────────────────────────────────────────────────────────

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="DeadZone Fly Telegram notifier")
    p.add_argument("--action",        default="update")
    p.add_argument("--detail",        default="")
    p.add_argument("--codename",      default="unknown")
    p.add_argument("--soc",           default="unknown")
    p.add_argument("--edition",       default="free")
    p.add_argument("--mode",          default="dry_run")
    p.add_argument("--listmezo-mode", dest="listmezo_mode", default="dry_run")
    p.add_argument("--elapsed",       default="0m 0s")
    p.add_argument("--pixeldrain-url",dest="pixeldrain_url", default="")
    p.add_argument("--zip-size",      dest="zip_size", default="")
    p.add_argument("--error-reason",  dest="error_reason", default="")
    args = p.parse_args(argv)

    token   = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    group_id = os.environ.get("TELEGRAM_GROUP_ID", "")
    msg_id_env = os.environ.get("TELEGRAM_MSG_ID", "").strip()

    github_run_url = ""
    run_id  = os.environ.get("GITHUB_RUN_ID", "")
    server  = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    repo    = os.environ.get("GITHUB_REPOSITORY", "")
    if run_id and repo:
        github_run_url = f"{server}/{repo}/actions/runs/{run_id}"

    if not token or not chat_id:
        print("[tg] TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set — skipping.", file=sys.stderr)
        return 0

    # Group-only actions
    if args.action in ("group_success", "group_failed"):
        if not group_id:
            return 0
        text = _build_message(
            action=args.action,
            detail=args.detail,
            codename=args.codename,
            soc=args.soc,
            edition=args.edition,
            mode=args.mode,
            listmezo_mode=args.listmezo_mode,
            elapsed=args.elapsed,
            pixeldrain_url=args.pixeldrain_url,
            github_run_url=github_run_url,
            zip_size=args.zip_size,
            error_reason=args.error_reason,
        )
        resp = _send_message(token, group_id, text)
        if not resp.get("ok"):
            print(f"[tg] Group message failed: {resp}", file=sys.stderr)
        return 0

    # Private message: edit existing or send new
    status = _load_status()

    # Resolve message_id: env var takes priority, then saved status
    message_id: int | None = None
    if msg_id_env and msg_id_env.isdigit():
        message_id = int(msg_id_env)
    elif status.get("message_id"):
        try:
            message_id = int(status["message_id"])
        except (ValueError, TypeError):
            message_id = None

    text = _build_message(
        action=args.action,
        detail=args.detail,
        codename=args.codename,
        soc=args.soc,
        edition=args.edition,
        mode=args.mode,
        listmezo_mode=args.listmezo_mode,
        elapsed=args.elapsed,
        pixeldrain_url=args.pixeldrain_url,
        github_run_url=github_run_url,
        zip_size=args.zip_size,
        error_reason=args.error_reason,
    )

    if message_id is not None:
        # Edit existing message
        resp = _edit_message(token, chat_id, message_id, text)
        if resp.get("ok"):
            print(f"[tg] Edited message {message_id}")
            status["message_id"] = message_id
            status["last_action"] = args.action
            status["last_update_time"] = time.time()
            _save_status(status)
            return 0

        err_desc = resp.get("description", "")
        # "message is not modified" is not an error
        if "not modified" in err_desc.lower():
            return 0

        print(f"[tg] editMessageText failed ({resp.get('error_code')}): {err_desc}", file=sys.stderr)
        print(f"[tg] Falling back to sendMessage", file=sys.stderr)

    # Send new message
    resp = _send_message(token, chat_id, text)
    if resp.get("ok"):
        new_id = resp["result"]["message_id"]
        print(f"[tg] Sent new message {new_id}")
        status["message_id"] = new_id
        status["last_action"] = args.action
        status["first_send_time"] = time.time()
        status["last_update_time"] = time.time()
        if args.action in ("done", "failed"):
            status["final_status"] = args.action
        _save_status(status)
        # Print message_id to stdout so callers can capture it
        print(new_id)
        return 0

    print(f"[tg] sendMessage failed: {resp}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
