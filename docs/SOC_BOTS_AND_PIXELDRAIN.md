# DeadZone — SoC Bots and PixelDrain Upload

## Bot Design

DeadZone uses **two Telegram bots split by SoC**, not by event type.

| Bot | SoC | Workflow |
|---|---|---|
| DeadZone_Snapdragon | Snapdragon | `deadzone_snapdragon.yml` |
| DeadZone_MTK | MTK | `deadzone_mtk.yml` |

Each bot receives **all** messages for its SoC:
- Build started
- Build failed (with diagnostics link)
- ROM uploaded to PixelDrain (with download link)

There is no separate "release bot" or "build bot". SoC is the only split.

---

## Required GitHub Secrets

Add these secrets to your repository under **Settings → Secrets and variables → Actions**:

| Secret | Used by |
|---|---|
| `TELEGRAM_SNAPDRAGON_BOT_TOKEN` | `deadzone_snapdragon.yml` |
| `TELEGRAM_SNAPDRAGON_CHAT_ID` | `deadzone_snapdragon.yml` |
| `TELEGRAM_MTK_BOT_TOKEN` | `deadzone_mtk.yml` |
| `TELEGRAM_MTK_CHAT_ID` | `deadzone_mtk.yml` |
| `PIXELDRAIN_API_KEY` | Both workflows |

### How to add secrets on GitHub

1. Go to your repository on GitHub.
2. Click **Settings** → **Secrets and variables** → **Actions**.
3. Click **New repository secret**.
4. Enter the secret name (e.g., `TELEGRAM_SNAPDRAGON_BOT_TOKEN`) and value.
5. Click **Add secret**.

### How to get a Telegram bot token

1. Open Telegram and message `@BotFather`.
2. Send `/newbot` and follow the prompts.
3. Copy the token BotFather gives you.

### How to get your Telegram chat ID

1. Add the bot to your channel/group, or start a private chat.
2. Send a message, then call:
   `https://api.telegram.org/bot<TOKEN>/getUpdates`
3. The `chat.id` field is your chat ID.

---

## PixelDrain API Key

- Sign in at [pixeldrain.com](https://pixeldrain.com).
- Go to **Account → API Keys**.
- Create a new key and copy it.
- Add it as the `PIXELDRAIN_API_KEY` GitHub secret.

If no API key is provided, uploads will be anonymous (still work, but unlinked to your account).

---

## What is uploaded to PixelDrain

Only the **final public ROM ZIP** produced by the MEZO build is uploaded.

The uploader excludes:
- Source ROM ZIPs from `_input_roms/`
- Log and diagnostic ZIPs
- Cache folders

The public PixelDrain link is printed to the workflow log and sent to the SoC Telegram bot.

A JSON sidecar is written to `output/reports/pixeldrain_upload.json`:

```json
{
  "success": true,
  "file": "path/to/final.zip",
  "id": "file_id",
  "link": "https://pixeldrain.com/u/file_id"
}
```

---

## Notification behavior

Notifications are **non-blocking by default**. If Telegram is unreachable or secrets are missing, the build continues and a warning is printed.

To make notification failures fail the build, set the `STRICT_NOTIFICATIONS=true` environment variable.

Missing-secret warnings:

```
[TELEGRAM] Missing Snapdragon bot secrets; notification skipped
[TELEGRAM] Missing MTK bot secrets; notification skipped
```

---

## Service modules

| Module | Purpose |
|---|---|
| `factory/services/telegram_notify.py` | `send_snapdragon_message()`, `send_mtk_message()` |
| `factory/services/pixeldrain_upload.py` | `upload_to_pixeldrain()` |
| `factory/reports/build_summary.py` | `format_build_start()`, `format_build_failure()`, `format_upload_success()` |

### CLI usage

```bash
# Test Telegram (requires secrets in environment)
python -m factory.services.telegram_notify snapdragon "test message"
python -m factory.services.telegram_notify mtk "test message"

# Upload a ROM ZIP manually
python -m factory.services.pixeldrain_upload path/to/final_rom.zip

# Via factory CLI
python -m factory.cli upload-pixeldrain --file path/to/final_rom.zip
```

---

## What must NEVER be committed

- Bot tokens (`TELEGRAM_*_BOT_TOKEN`)
- Chat IDs if your channel is private
- PixelDrain API key (`PIXELDRAIN_API_KEY`)
- Source ROM ZIPs
- Output ROM ZIPs
- Log files that may contain secrets

All credentials must come exclusively from GitHub Secrets or local environment variables.
