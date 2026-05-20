#!/usr/bin/env python3
"""
DeadZone Factory - Telegram multi-channel live build card tailored for Fly.io.
This script runs independently without touching the original project script.
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
    "pending": "⬜",
    "running": "🔄",
    "pass":    "✅",
    "fail":    "❌",
    "skip":    "⏭️",
}

_MAX_LEN = 4000

# ---------------------------------------------------------------------------
# Smart Environment Credentials Hunter
# ---------------------------------------------------------------------------

def _credentials():
    """
    Scans the Fly microVM environment for any available Telegram token or Chat IDs.
    """
    # Hunt for Token (Global -> Snapdragon -> MediaTek)
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    if not token:
        token = os.environ.get("TELEGRAM_SNAPDRAGON_BOT_TOKEN", "").strip()
    if not token:
        token = os.environ.get("TELEGRAM_MTK_BOT_TOKEN", "").strip()

    # Hunt for Group Chat ID (Global -> Snapdragon -> MediaTek)
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not chat_id:
        chat_id = os.environ.get("TELEGRAM_SNAPDRAGON_CHAT_ID", "").strip()
    if not chat_id:
        chat_id = os.environ.get("TELEGRAM_MTK_CHAT_ID", "").strip()

    thread_id = os.environ.get("TELEGRAM_THREAD_ID", "").strip()
    return token, chat_id, thread_id


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


def _build_message(state):
    soc = state.get("soc", "?").upper()
    run_num = os.environ.get("GITHUB_RUN_NUMBER", "")
    header = f"DeadZone {soc} Build" + (f" #{run_num}" if run_num else "")

    lines = [
        header,
        f"Device: {state.get('device', '?')} | Platform: {state.get('platform', '?')} | Flavor: {state.get('flavor', '?')}",
    ]
    url = state.get("run_url", "")
    if url:
        lines.append(f"Run: {url}")
    lines.append("")
    lines.append("Stages:")
    for stage in STAGES:
        s = state.get("stages", {}).get(stage, {})
        icon = ICONS.get(s.get("status", "pending"), "⬜")
        msg = s.get("message", "")
        line = f"  {icon} {stage}"
        if msg:
            line += f": {msg}"
        lines.append(line)
    lines.append("")
    started = state.get("started_at", "")
    updated = state.get("updated_at", "")
    if started:
        lines.append(f"Started: {started}")
    if updated and updated != started:
        lines.append(f"Updated: {updated}")

    text = "\n".join(lines)
    return text[:_MAX_LEN] if len(text) > _MAX_LEN else text


def _load_state():
    try:
        if STATE_FILE.exists():
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except:
        pass
    return {}


def _save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def _post(token, method, payload):
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if "message is not modified" in body.lower():
            return {"ok": True}
        print(f"[LIVE] HTTP {exc.code}: {body}", file=sys.stderr, flush=True)
        return None
    except Exception as exc:
        print(f"[LIVE] Request error: {exc}", file=sys.stderr, flush=True)
        return None


# ---------------------------------------------------------------------------
# Commands Execution
# ---------------------------------------------------------------------------

def cmd_start(args):
    token, chat_id, thread_id = _credentials()
    if not token or not chat_id:
        print("[LIVE] Skipping: Missing critical Telegram configuration.", flush=True)
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
        try: payload["message_thread_id"] = int(thread_id)
        except ValueError: pass

    result = _post(token, "sendMessage", payload)
    if result and result.get("ok") and isinstance(result.get("result"), dict):
        state["message_id"] = result["result"]["message_id"]
        print(f"[LIVE] Live card initiated on Fly (message_id={state['message_id']}).", flush=True)
    else:
        print(f"[LIVE] sendMessage failed: {result}", file=sys.stderr, flush=True)

    _save_state(state)
    return 0


def cmd_update(args):
    token, chat_id, thread_id = _credentials()
    if not token or not chat_id: return 0

    state = _load_state()
    if not state: return 0

    message_id = state.get("message_id")
    if not message_id: return 0
    if args.stage not in STAGES: return 0

    state.setdefault("stages", {})[args.stage] = {
        "status": args.status,
        "message": args.message or "",
    }
    state["updated_at"] = _now_iso()
    _save_state(state)

    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": _build_message(state),
        "disable_web_page_preview": True,
    }
    if thread_id:
        try: payload["message_thread_id"] = int(thread_id)
        except ValueError: pass

    _post(token, "editMessageText", payload)
    return 0


def cmd_final(args):
    token, chat_id, thread_id = _credentials()
    if not token or not chat_id: return 0

    state = _load_state()
    if not state: return 0

    message_id = state.get("message_id")
    stages = state.setdefault("stages", {})
    failed_stage = getattr(args, "failed_stage", None)

    if args.result == "success":
        for s in STAGES:
            if stages.get(s, {}).get("status") in ("pending", "running"):
                stages[s] = {"status": "pass", "message": ""}
        stages["telegram_final"] = {"status": "pass", "message": args.message or "Build completed"}
    else:
        if failed_stage and failed_stage in STAGES:
            stages[failed_stage] = {"status": "fail", "message": args.message or "Failed"}
        else:
            for s in reversed(STAGES):
                if stages.get(s, {}).get("status") == "running":
                    stages[s] = {"status": "fail", "message": args.message or "Failed"}
                    failed_stage = s
                    break
        past_fail = False
        for s in STAGES:
            if s == failed_stage or stages.get(s, {}).get("status") == "fail":
                past_fail = True
                continue
            if past_fail and stages.get(s, {}).get("status") in ("pending", "running"):
                stages[s] = {"status": "skip", "message": ""}
        stages["telegram_final"] = {"status": "fail", "message": args.message or "Build failed"}

    state["updated_at"] = _now_iso()
    _save_state(state)
    text = _build_message(state)

    if message_id:
        payload = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text,
            "disable_web_page_preview": True,
        }
        if thread_id:
            try: payload["message_thread_id"] = int(thread_id)
            except ValueError: pass
        result = _post(token, "editMessageText", payload)
        if result and result.get("ok"):
            return 0

    payload = {"chat_id": chat_id, "text": text, "disable_web_page_preview": True}
    if thread_id:
        try: payload["message_thread_id"] = int(thread_id)
        except ValueError: pass
    _post(token, "sendMessage", payload)
    return 0


# ---------------------------------------------------------------------------
# Main Entry Gate
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="DeadZone Telegram live build card for Fly")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("start")
    p.add_argument("--device", required=True)
    p.add_argument("--soc", required=True)
    p.add_argument("--platform", required=True)
    p.add_argument("--flavor", required=True)

    p = sub.add_parser("update")
    p.add_argument("--stage", required=True)
    p.add_argument("--status", required=True, choices=["pending", "running", "pass", "fail", "skip"])
    p.add_argument("--message", default="")

    p = sub.add_parser("final")
    p.add_argument("--result", required=True, choices=["success", "failure"])
    p.add_argument("--message", default="")
    p.add_argument("--failed-stage", dest="failed_stage", default=None)

    args = parser.parse_args()
    try:
        if args.command == "start": return cmd_start(args)
        if args.command == "update": return cmd_update(args)
        if args.command == "final": return cmd_final(args)
    except Exception as exc:
        print(f"[LIVE] Error bypass: {exc}", file=sys.stderr, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
