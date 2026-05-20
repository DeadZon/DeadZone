# Fly.io Deployment

This repository is configured for a Fly.io worker/builder container. It does not expose a public HTTP service.

## Launch

```sh
fly launch --no-deploy --copy-config
```

## Set Secrets

Set Telegram secrets manually. Do not commit tokens, chat IDs, API keys, or private values to the repository.

```sh
fly secrets set TELEGRAM_SNAPDRAGON_BOT_TOKEN="..."
fly secrets set TELEGRAM_SNAPDRAGON_CHAT_ID="..."
fly secrets set TELEGRAM_MTK_BOT_TOKEN="..."
fly secrets set TELEGRAM_MTK_CHAT_ID="..."
```

## Deploy

```sh
fly deploy --remote-only
```

## Logs

```sh
fly logs
```

## Runtime Mode

The default deployment is safe:

```toml
SOC = "snapdragon"
MODE = "dry_run"
NOTIFY_TELEGRAM = "false"
DEVICE_CODENAME = "garnet"
FINAL_NAME = "DeadZone_Test"
```

For an actual build, set runtime environment values such as `MODE=execute` and provide either `ROM_URL` or `ROM_PATH`. Telegram is optional and only used when `NOTIFY_TELEGRAM=true` and the matching SoC secrets are present.
