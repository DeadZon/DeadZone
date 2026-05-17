"""
Telegram notification service for DeadZone Factory.

Per-SoC bots:
  DeadZone_Snapdragon  ->  TELEGRAM_SNAPDRAGON_BOT_TOKEN / TELEGRAM_SNAPDRAGON_CHAT_ID
  DeadZone_MTK         ->  TELEGRAM_MTK_BOT_TOKEN        / TELEGRAM_MTK_CHAT_ID

Set STRICT_NOTIFICATIONS=true to make failures exit non-zero.

CLI usage:
  python -m factory.services.telegram_notify snapdragon "message"
  python -m factory.services.telegram_notify mtk "message"
"""

import json
import os
import sys
import urllib.error
import urllib.request


def send_telegram_message(token: str, chat_id: str, text: str) -> bool:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
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
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            data = json.loads(body)
            if data.get("ok"):
                return True
            print(f"[TELEGRAM] API error: {body}", file=sys.stderr)
            return _maybe_strict_fail()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"[TELEGRAM] HTTP {exc.code}: {body}", file=sys.stderr)
    except Exception as exc:
        print(f"[TELEGRAM] Request failed: {exc}", file=sys.stderr)
    return _maybe_strict_fail()


def _maybe_strict_fail() -> bool:
    if os.environ.get("STRICT_NOTIFICATIONS", "").lower() == "true":
        sys.exit(1)
    return False


def send_snapdragon_message(text: str) -> bool:
    token = os.environ.get("TELEGRAM_SNAPDRAGON_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_SNAPDRAGON_CHAT_ID", "").strip()
    if not token or not chat_id:
        print("[TELEGRAM] Missing Snapdragon bot secrets; notification skipped")
        return False
    return send_telegram_message(token, chat_id, text)


def send_mtk_message(text: str) -> bool:
    token = os.environ.get("TELEGRAM_MTK_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_MTK_CHAT_ID", "").strip()
    if not token or not chat_id:
        print("[TELEGRAM] Missing MTK bot secrets; notification skipped")
        return False
    return send_telegram_message(token, chat_id, text)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python -m factory.services.telegram_notify <snapdragon|mtk> <message>")
        sys.exit(1)
    _soc = sys.argv[1].lower()
    _msg = sys.argv[2]
    if _soc == "snapdragon":
        _ok = send_snapdragon_message(_msg)
    elif _soc == "mtk":
        _ok = send_mtk_message(_msg)
    else:
        print(f"[TELEGRAM] Unknown SoC '{_soc}'. Use 'snapdragon' or 'mtk'.")
        sys.exit(1)
    sys.exit(0 if _ok else 1)
