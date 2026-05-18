#!/usr/bin/env python3
"""
DeadZone Factory - Telegram live build card.

One message per build, edited in-place as stages progress.

CLI:
  python scripts/telegram_live_notify.py start \
    --device zircon --soc mtk --platform os3_a16 --flavor deadzone

  python scripts/telegram_live_notify.py update \
    --stage rebuild_super --status running --message "Rebuilding sparse VAB super.img"

  python scripts/telegram_live_notify.py update \
    --stage rebuild_super --status pass --message "super.img rebuilt successfully"

  python scripts/telegram_live_notify.py final --result success --message "Build completed"
  python scripts/telegram_live_notify.py final --result failure \
    --failed-stage rebuild_super --message "super.img rebuild failed"

Environment variables (required):
  TELEGRAM_BOT_TOKEN
  TELEGRAM_CHAT_ID

Environment variables (optional):
  TELEGRAM_THREAD_ID     message thread / forum topic ID
  GITHUB_SERVER_URL      used to build run link
  GITHUB_REPOSITORY      used to build run link
  GITHUB_RUN_ID          used to build run link
  GITHUB_RUN_NUMBER      shown in card header

State file:
  output/runtime/telegram_live_message.json
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

STATE_FILE = Path("output/runtime/telegram_live_message.json")

STAGES = [
    "prepare",
    "download_rom",
    "extract_rom",
    "patch_rom",
    "rebuild_super",
    "package_zip",
    "validate_zip",
    "upload_pixeldrain",
    "github_release",
    "telegram_final",
]

ICONS = {
    "pending": "⬜",   # ⬜
    "running": "\U0001f504",  # 🔄
    "pass":    "✅",   # ✅
    "fail":    "❌",   # ❌
    "skip":    "⏭️",  # ⏭️
}

_MAX_LEN = 4000  # Telegram cap is 4096; leave margin


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def _run_url():
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com").rstrip("/")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    if repo and run_id:
        return f"{server}/{repo}/actions/runs/{run_id}"
    return ""


def _credentials():
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    thread_id = os.environ.get("TELEGRAM_THREAD_ID", "").strip()
    return token, chat_id, thread_id


def _build_message(state):
    soc = state.get("soc", "?").upper()
    run_num = os.environ.get("GITHUB_RUN_NUMBER", "")
    header = "DeadZone {} Build".format(soc) + (" #{}".format(run_num) if run_num else "")

    lines = [
        header,
        "Device: {} | Platform: {} | Flavor: {}".format(
            state.get("device", "?"),
            state.get("platform", "?"),
            state.get("flavor", "?"),
        ),
    ]
    url = state.get("run_url", "")
    if url:
        lines.append("Run: {}".format(url))
    lines.append("")
    lines.append("Stages:")
    for stage in STAGES:
        s = state.get("stages", {}).get(stage, {})
        icon = ICONS.get(s.get("status", "pending"), "⬜")
        msg = s.get("message", "")
        line = "  {} {}".format(icon, stage)
        if msg:
            line += ": {}".format(msg)
        lines.append(line)
    lines.append("")
    started = state.get("started_at", "")
    updated = state.get("updated_at", "")
    if started:
        lines.append("Started: {}".format(started))
    if updated and updated != started:
        lines.append("Updated: {}".format(updated))

    text = "\n".join(lines)
    return text[:_MAX_LEN] if len(text) > _MAX_LEN else text


def _load_state():
    try:
        if STATE_FILE.exists():
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        pass
    return {}


def _save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def _post(token, method, payload):
    url = "https://api.telegram.org/bot{}/{}".format(token, method)
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if "message is not modified" in body.lower():
            print("[LIVE] Message not modified — skipping.", flush=True)
            return {"ok": True}
        print("[LIVE] HTTP {}: {}".format(exc.code, body), file=sys.stderr, flush=True)
        return None
    except Exception as exc:
        print("[LIVE] Request error: {}".format(exc), file=sys.stderr, flush=True)
        return None


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_start(args):
    token, chat_id, thread_id = _credentials()
    if not token or not chat_id:
        print("[LIVE] Missing TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID — skipped.", flush=True)
        return 0

    now = _now_iso()
    state = {
        "chat_id": chat_id,
        "message_id": None,
        "started_at": now,
        "updated_at": now,
        "device": args.device,
        "soc": args.soc,
        "platform": args.platform,
        "flavor": args.flavor,
        "run_url": _run_url(),
        "stages": {s: {"status": "pending", "message": ""} for s in STAGES},
    }
    state["stages"]["prepare"] = {"status": "pass", "message": ""}

    payload = {
        "chat_id": chat_id,
        "text": _build_message(state),
        "disable_web_page_preview": True,
    }
    if thread_id:
        try:
            payload["message_thread_id"] = int(thread_id)
        except ValueError:
            pass

    result = _post(token, "sendMessage", payload)
    if result and result.get("ok") and isinstance(result.get("result"), dict):
        state["message_id"] = result["result"]["message_id"]
        print("[LIVE] Live card started (message_id={}).".format(state["message_id"]), flush=True)
    else:
        print("[LIVE] sendMessage failed: {}".format(result), file=sys.stderr, flush=True)

    _save_state(state)
    return 0


def cmd_update(args):
    token, chat_id, _ = _credentials()
    if not token or not chat_id:
        print("[LIVE] Missing credentials — skipped.", flush=True)
        return 0

    state = _load_state()
    if not state:
        print("[LIVE] No state file — skipping update.", flush=True)
        return 0

    message_id = state.get("message_id")
    if not message_id:
        print("[LIVE] No message_id in state — skipping edit.", flush=True)
        return 0

    if args.stage not in STAGES:
        print("[LIVE] Unknown stage '{}' — skipping.".format(args.stage), flush=True)
        return 0

    state.setdefault("stages", {})[args.stage] = {
        "status": args.status,
        "message": args.message or "",
    }
    state["updated_at"] = _now_iso()
    _save_state(state)

    result = _post(token, "editMessageText", {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": _build_message(state),
        "disable_web_page_preview": True,
    })
    if result and result.get("ok"):
        print("[LIVE] Stage {}={}.".format(args.stage, args.status), flush=True)
    else:
        print("[LIVE] editMessageText failed: {}".format(result), file=sys.stderr, flush=True)
    return 0


def cmd_final(args):
    token, chat_id, thread_id = _credentials()
    if not token or not chat_id:
        print("[LIVE] Missing credentials — skipped.", flush=True)
        return 0

    state = _load_state()
    if not state:
        print("[LIVE] No state file — skipping final.", flush=True)
        return 0

    message_id = state.get("message_id")
    stages = state.setdefault("stages", {})
    failed_stage = getattr(args, "failed_stage", None)

    if args.result == "success":
        for s in STAGES:
            if stages.get(s, {}).get("status") in ("pending", "running"):
                stages[s] = {"status": "pass", "message": ""}
        stages["telegram_final"] = {
            "status": "pass",
            "message": args.message or "Build completed",
        }
    else:
        if failed_stage and failed_stage in STAGES:
            stages[failed_stage] = {
                "status": "fail",
                "message": args.message or "Failed",
            }
        else:
            # Find last running stage and mark it fail
            for s in reversed(STAGES):
                if stages.get(s, {}).get("status") == "running":
                    stages[s] = {"status": "fail", "message": args.message or "Failed"}
                    failed_stage = s
                    break
        # Skip stages that come after the failed one
        past_fail = False
        for s in STAGES:
            if s == failed_stage or stages.get(s, {}).get("status") == "fail":
                past_fail = True
                continue
            if past_fail and stages.get(s, {}).get("status") in ("pending", "running"):
                stages[s] = {"status": "skip", "message": ""}
        stages["telegram_final"] = {
            "status": "fail",
            "message": args.message or "Build failed",
        }

    state["updated_at"] = _now_iso()
    _save_state(state)
    text = _build_message(state)

    if message_id:
        result = _post(token, "editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text,
            "disable_web_page_preview": True,
        })
        if result and result.get("ok"):
            print("[LIVE] Final card updated ({}).".format(args.result), flush=True)
            return 0
        print("[LIVE] editMessageText failed — falling back to sendMessage.", file=sys.stderr, flush=True)

    # Fallback: send a new message (only if edit failed or no message_id)
    payload = {
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": True,
    }
    if thread_id:
        try:
            payload["message_thread_id"] = int(thread_id)
        except ValueError:
            pass
    _post(token, "sendMessage", payload)
    print("[LIVE] Final card sent ({}).".format(args.result), flush=True)
    return 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="DeadZone Telegram live build card",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("start", help="Send the initial build card")
    p.add_argument("--device", required=True, help="Device codename")
    p.add_argument("--soc", required=True, help="SoC (mtk / snapdragon)")
    p.add_argument("--platform", required=True, help="ROM platform (e.g. os3_a16)")
    p.add_argument("--flavor", required=True, help="DeadZone flavor")

    p = sub.add_parser("update", help="Edit a stage in the live card")
    p.add_argument("--stage", required=True, help="Stage name")
    p.add_argument(
        "--status", required=True,
        choices=["pending", "running", "pass", "fail", "skip"],
    )
    p.add_argument("--message", default="", help="Short stage message")

    p = sub.add_parser("final", help="Edit card with final build result")
    p.add_argument("--result", required=True, choices=["success", "failure"])
    p.add_argument("--message", default="", help="Final summary message")
    p.add_argument("--failed-stage", dest="failed_stage", default=None,
                   help="Stage that caused the failure")

    args = parser.parse_args()
    try:
        if args.command == "start":
            return cmd_start(args)
        if args.command == "update":
            return cmd_update(args)
        if args.command == "final":
            return cmd_final(args)
    except Exception as exc:
        print("[LIVE] Unexpected error: {}".format(exc), file=sys.stderr, flush=True)
    return 0  # never fail the build


if __name__ == "__main__":
    sys.exit(main())
