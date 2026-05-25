"""Send a Telegram message when workflow validation fails before Fly/API/factory starts.

Exits 0 always — never fails the workflow due to a Telegram error.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


def _send_telegram(bot_token: str, chat_id: str, text: str) -> bool:
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = json.dumps({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except Exception as exc:
        print(f"[notify] Telegram send failed: {exc}", file=sys.stderr)
        return False


def _resolve_credentials(soc: str) -> tuple[str, str] | None:
    """Return (bot_token, chat_id) from env for the given SoC, or None if missing."""
    soc_upper = soc.upper()

    # SoC-specific keys (highest priority)
    specific_token = os.environ.get(f"TELEGRAM_{soc_upper}_BOT_TOKEN", "")
    specific_chat = os.environ.get(f"TELEGRAM_{soc_upper}_CHAT_ID", "")
    if specific_token and specific_chat:
        return specific_token, specific_chat

    # Generic fallback
    generic_token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    generic_chat = os.environ.get("TELEGRAM_CHAT_ID", "")
    if generic_token and generic_chat:
        return generic_token, generic_chat

    return None


def _build_message(args: argparse.Namespace) -> str:
    soc_display = args.soc.upper() if args.soc else "Unknown"
    lines = [
        "❌ <b>DeadZone Dispatch Failed</b>",
        "",
        "Source: GitHub Actions",
        f"SoC: {soc_display}",
        f"Device: {args.codename or 'unknown'}",
        f"Edition: {args.edition or 'unknown'}",
        f"Mode: {args.mode or 'unknown'}",
        "",
        f"Reason:\n{args.reason or 'Unknown error'}",
    ]

    if args.missing:
        missing_items = [m.strip() for m in args.missing.split(",") if m.strip()]
        if missing_items:
            lines.append("")
            lines.append("Missing:")
            for item in missing_items:
                lines.append(item)

    if args.run_url:
        lines.append("")
        lines.append(f"Run:\n{args.run_url}")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Notify Telegram on dispatch failure")
    parser.add_argument("--soc", default="", help="SoC: mtk or snapdragon")
    parser.add_argument("--codename", default="", help="Device codename")
    parser.add_argument("--edition", default="", help="ROM edition")
    parser.add_argument("--mode", default="", help="Build mode")
    parser.add_argument("--title", default="DeadZone Dispatch Failed", help="Message title")
    parser.add_argument("--reason", default="", help="Failure reason")
    parser.add_argument("--missing", default="", help="Comma-separated list of missing secrets/items")
    parser.add_argument("--run-url", default="", help="GitHub Actions run URL")
    args = parser.parse_args()

    creds = _resolve_credentials(args.soc)
    if creds is None:
        print("[notify] Telegram skipped: missing secrets (TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID or SoC-specific)")
        return 0

    bot_token, chat_id = creds
    message = _build_message(args)

    print(f"[notify] Sending dispatch failure message to Telegram chat {chat_id}")
    ok = _send_telegram(bot_token, chat_id, message)
    if ok:
        print("[notify] Telegram message sent.")
    else:
        print("[notify] Telegram send failed — continuing anyway.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
