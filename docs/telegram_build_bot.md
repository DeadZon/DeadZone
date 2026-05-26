# DeadZone Telegram Build Bot

Dispatches GitHub Actions workflows for MTK and Snapdragon ROM builds.
The bot **never runs builds locally** — it only calls the GitHub API.

## Files

| File | Purpose |
|------|---------|
| `server/telegram_bot.py` | Bot implementation (polling loop + command handlers) |
| `scripts/validate_telegram_bot.py` | Safety validator — run in CI before deploying |

## Required environment variables

| Variable | Description |
|----------|-------------|
| `TELEGRAM_BOT_TOKEN` | Bot token from @BotFather |
| `GITHUB_TOKEN` | Personal access token with `workflow` scope |
| `GITHUB_REPO` | Repository in `owner/repo` form, e.g. `DeadZon/DeadZone` |
| `TELEGRAM_ALLOWED_USER_IDS` | Comma-separated list of allowed Telegram user IDs |

## Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message |
| `/help` | List all commands |
| `/build_mtk <codename> <edition> <rom_url>` | Dispatch `deadzone_mtk.yml` workflow |
| `/build_snapdragon <codename> <edition> <rom_url>` | Dispatch `deadzone_snapdragon.yml` workflow |
| `/status` | Link to all GitHub Actions runs |
| `/latest` | Links to latest runs per workflow |

ROM URL is **required** — paste the direct ZIP or TGZ download link.
Example: `/build_mtk zircon legend https://example.com/rom.zip`

## Allowed editions

Only `legend` is accepted. Sending any other edition is rejected with an error message.

## Workflow inputs dispatched

```json
{
  "codename":         "<device codename>",
  "custom_codename":  "",
  "edition":          "legend",
  "rom_url":          "<direct ROM URL — required>",
  "mode":             "execute",
  "upload_pixeldrain": "true",
  "notify_telegram":   "true"
}
```

`rom_url` must start with `http://` or `https://`. The value `auto` is rejected.

## Security model

- Every incoming command is checked against `TELEGRAM_ALLOWED_USER_IDS`.
- Unknown users receive `Unauthorized.` and the command is dropped.
- The bot uses only Python stdlib (`urllib`, `json`, `ast`, `os`).
- No subprocess, shell, or exec calls are present anywhere.
- `scripts/validate_telegram_bot.py` enforces these rules via AST analysis.

## Running locally

```bash
export TELEGRAM_BOT_TOKEN="..."
export GITHUB_TOKEN="ghp_..."
export GITHUB_REPO="DeadZon/DeadZone"
export TELEGRAM_ALLOWED_USER_IDS="123456789"

python server/telegram_bot.py
```

## Validation

```bash
python -m compileall server scripts
python scripts/validate_telegram_bot.py
```

## Deployment notes

- The bot uses long-polling (`getUpdates?timeout=30`). No webhook is required.
- Runs as a single process; restart on exit with `systemd` or Docker.
- Do **not** share `GITHUB_TOKEN` or `TELEGRAM_BOT_TOKEN` in logs.
