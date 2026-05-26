"""
DeadZone Telegram Build Bot.

Dispatches GitHub Actions workflows for MTK and Snapdragon builds.
Does NOT run local builds, execute shell commands, or invoke subprocesses.

Required env vars:
  TELEGRAM_BOT_TOKEN          — bot token from @BotFather
  GITHUB_TOKEN                — personal access token with workflow scope
  GITHUB_REPO                 — e.g. DeadZon/DeadZone
  TELEGRAM_ALLOWED_USER_IDS   — comma-separated Telegram user IDs
"""

import os
import logging
import urllib.request
import urllib.error
import json
from typing import Optional

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("deadzone.telegram_bot")

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

TELEGRAM_BOT_TOKEN: str = os.environ.get("TELEGRAM_BOT_TOKEN", "")
GITHUB_TOKEN: str = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO: str = os.environ.get("GITHUB_REPO", "DeadZon/DeadZone")
_RAW_ALLOWED: str = os.environ.get("TELEGRAM_ALLOWED_USER_IDS", "")

ALLOWED_USER_IDS: set[int] = set()
for _part in _RAW_ALLOWED.split(","):
    _part = _part.strip()
    if _part.isdigit():
        ALLOWED_USER_IDS.add(int(_part))

ALLOWED_EDITIONS = {"legend"}

WORKFLOWS = {
    "mtk": "deadzone_mtk.yml",
    "snapdragon": "deadzone_snapdragon.yml",
}

GITHUB_ACTIONS_BASE = f"https://github.com/{GITHUB_REPO}/actions/workflows"
TELEGRAM_API_BASE = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

# ---------------------------------------------------------------------------
# Low-level HTTP helpers (stdlib only, no shell)
# ---------------------------------------------------------------------------


def _http_post_json(url: str, payload: dict, headers: dict) -> tuple[int, dict]:
    """POST JSON; returns (status_code, response_dict)."""
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode())
            return resp.status, body
    except urllib.error.HTTPError as exc:
        body = {}
        try:
            body = json.loads(exc.read().decode())
        except Exception:
            pass
        return exc.code, body


def _http_get_json(url: str, headers: dict) -> tuple[int, dict]:
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read().decode())
            return resp.status, body
    except urllib.error.HTTPError as exc:
        body = {}
        try:
            body = json.loads(exc.read().decode())
        except Exception:
            pass
        return exc.code, body


# ---------------------------------------------------------------------------
# Telegram helpers
# ---------------------------------------------------------------------------


def send_message(chat_id: int, text: str) -> None:
    url = f"{TELEGRAM_API_BASE}/sendMessage"
    headers = {"Content-Type": "application/json"}
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    status, body = _http_post_json(url, payload, headers)
    if status != 200:
        log.error("sendMessage failed %s: %s", status, body)


def get_updates(offset: Optional[int] = None) -> list[dict]:
    url = f"{TELEGRAM_API_BASE}/getUpdates?timeout=30"
    if offset is not None:
        url += f"&offset={offset}"
    headers = {}
    status, body = _http_get_json(url, headers)
    if status != 200:
        log.error("getUpdates failed %s: %s", status, body)
        return []
    return body.get("result", [])


# ---------------------------------------------------------------------------
# GitHub dispatch helper
# ---------------------------------------------------------------------------


def dispatch_workflow(workflow_file: str, inputs: dict) -> tuple[bool, str]:
    """
    POST workflow_dispatch to GitHub Actions API.
    Returns (success, message).
    """
    url = (
        f"https://api.github.com/repos/{GITHUB_REPO}"
        f"/actions/workflows/{workflow_file}/dispatches"
    )
    payload = {"ref": "main", "inputs": inputs}
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    status, body = _http_post_json(url, payload, headers)
    if status in (204, 200):
        return True, "dispatched"
    msg = body.get("message", str(body))
    return False, f"GitHub API error {status}: {msg}"


# ---------------------------------------------------------------------------
# Command handlers
# ---------------------------------------------------------------------------


def handle_start(chat_id: int) -> None:
    send_message(
        chat_id,
        "<b>DeadZone Build Bot</b>\n\n"
        "Use /help to see available commands.",
    )


def handle_help(chat_id: int) -> None:
    send_message(
        chat_id,
        "<b>Commands</b>\n\n"
        "/build_mtk &lt;codename&gt; &lt;edition&gt;\n"
        "  Dispatch a MediaTek build on GitHub Actions.\n\n"
        "/build_snapdragon &lt;codename&gt; &lt;edition&gt;\n"
        "  Dispatch a Snapdragon build on GitHub Actions.\n\n"
        "/status\n"
        "  Link to the Actions run list.\n\n"
        "/latest\n"
        "  Link to the latest workflow runs.\n\n"
        "Allowed editions: <code>legend</code>",
    )


def handle_build(chat_id: int, soc: str, args: list[str]) -> None:
    if len(args) < 2:
        send_message(
            chat_id,
            f"Usage: /build_{soc} &lt;codename&gt; &lt;edition&gt;\n"
            f"Example: /build_{soc} zircon legend",
        )
        return

    codename = args[0].strip().lower()
    edition = args[1].strip().lower()

    if not codename:
        send_message(chat_id, "Error: codename must not be empty.")
        return

    if edition not in ALLOWED_EDITIONS:
        send_message(
            chat_id,
            f"Error: edition <code>{edition}</code> is not allowed.\n"
            f"Allowed: {', '.join(sorted(ALLOWED_EDITIONS))}",
        )
        return

    workflow_file = WORKFLOWS[soc]
    inputs = {
        "codename": codename,
        "custom_codename": "",
        "edition": edition,
        "rom_url": "",
        "mode": "execute",
        "upload_pixeldrain": "true",
        "notify_telegram": "true",
    }

    ok, detail = dispatch_workflow(workflow_file, inputs)
    if ok:
        actions_url = f"{GITHUB_ACTIONS_BASE}/{workflow_file}"
        send_message(
            chat_id,
            "Build queued\n\n"
            f"SOC: <code>{soc}</code>\n"
            f"Codename: <code>{codename}</code>\n"
            f"Edition: <code>{edition}</code>\n"
            f"Workflow: <code>{workflow_file}</code>\n"
            f"<a href=\"{actions_url}\">View on GitHub Actions</a>",
        )
        log.info("Dispatched %s build: codename=%s edition=%s", soc, codename, edition)
    else:
        send_message(chat_id, f"Failed to queue build.\n{detail}")
        log.error("Dispatch failed for %s/%s: %s", soc, codename, detail)


def handle_status(chat_id: int) -> None:
    url = f"https://github.com/{GITHUB_REPO}/actions"
    send_message(chat_id, f"<a href=\"{url}\">GitHub Actions — all runs</a>")


def handle_latest(chat_id: int) -> None:
    mtk_url = f"{GITHUB_ACTIONS_BASE}/{WORKFLOWS['mtk']}"
    sd_url = f"{GITHUB_ACTIONS_BASE}/{WORKFLOWS['snapdragon']}"
    send_message(
        chat_id,
        f"Latest runs:\n"
        f"<a href=\"{mtk_url}\">MTK workflow</a>\n"
        f"<a href=\"{sd_url}\">Snapdragon workflow</a>",
    )


# ---------------------------------------------------------------------------
# Update dispatcher
# ---------------------------------------------------------------------------


def is_authorized(user_id: int) -> bool:
    return bool(ALLOWED_USER_IDS) and user_id in ALLOWED_USER_IDS


def process_update(update: dict) -> None:
    message = update.get("message") or update.get("edited_message")
    if not message:
        return

    chat_id: int = message["chat"]["id"]
    user_id: int = message["from"]["id"]
    text: str = message.get("text", "").strip()

    if not text.startswith("/"):
        return

    if not is_authorized(user_id):
        log.warning("Unauthorized user %s attempted: %s", user_id, text)
        send_message(chat_id, "Unauthorized.")
        return

    parts = text.split()
    command = parts[0].split("@")[0].lower()
    args = parts[1:]

    if command == "/start":
        handle_start(chat_id)
    elif command == "/help":
        handle_help(chat_id)
    elif command == "/build_mtk":
        handle_build(chat_id, "mtk", args)
    elif command == "/build_snapdragon":
        handle_build(chat_id, "snapdragon", args)
    elif command == "/status":
        handle_status(chat_id)
    elif command == "/latest":
        handle_latest(chat_id)
    else:
        send_message(chat_id, f"Unknown command: <code>{command}</code>. Use /help.")


# ---------------------------------------------------------------------------
# Polling loop
# ---------------------------------------------------------------------------


def run_polling() -> None:
    if not TELEGRAM_BOT_TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")
    if not GITHUB_TOKEN:
        raise RuntimeError("GITHUB_TOKEN is not set")
    if not ALLOWED_USER_IDS:
        raise RuntimeError("TELEGRAM_ALLOWED_USER_IDS is not set or empty")

    log.info("DeadZone Telegram bot starting (repo=%s)", GITHUB_REPO)
    log.info("Allowed users: %s", ALLOWED_USER_IDS)

    offset: Optional[int] = None
    while True:
        updates = get_updates(offset)
        for update in updates:
            try:
                process_update(update)
            except Exception as exc:
                log.exception("Error processing update %s: %s", update.get("update_id"), exc)
            offset = update["update_id"] + 1


if __name__ == "__main__":
    run_polling()
