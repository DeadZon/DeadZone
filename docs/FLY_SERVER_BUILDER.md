# Fly Server Builder

GitHub is source control only for the Fly builder path. Do not use GitHub Actions artifacts for ROM ZIPs from Fly builds, and do not commit tokens, chat IDs, API keys, ROM links, or private paths.

Fly.io runs the actual DeadZone ROM factory in a worker container. The repository is copied into `/app` as the source tree, while the large build workspace is `/work` on a Fly volume.

## Create the App and Volume

Create or reuse the app from `fly.toml`:

```sh
fly apps create dz-builder-snap
```

Create the persistent work volume in the same region as the app:

```sh
fly volumes create deadzone_work --app dz-builder-snap --region fra --size 100
```

Deploy the worker image:

```sh
fly deploy --remote-only
```

The default config has no public HTTP service. It starts in `MODE=dry_run` and `KEEP_ALIVE_AFTER_RUN=true` so the Fly machine stays alive after a successful run.

## Secrets

Set secrets with Fly, never in files.

Generic Telegram secrets:

```sh
fly secrets set --app dz-builder-snap TELEGRAM_BOT_TOKEN="..."
fly secrets set --app dz-builder-snap TELEGRAM_CHAT_ID="..."
fly secrets set --app dz-builder-snap TELEGRAM_THREAD_ID="..."
```

SoC-specific Telegram secrets:

```sh
fly secrets set --app dz-builder-snap TELEGRAM_SNAPDRAGON_BOT_TOKEN="..."
fly secrets set --app dz-builder-snap TELEGRAM_SNAPDRAGON_CHAT_ID="..."
fly secrets set --app dz-builder-snap TELEGRAM_SNAPDRAGON_THREAD_ID="..."

fly secrets set --app dz-builder-snap TELEGRAM_MTK_BOT_TOKEN="..."
fly secrets set --app dz-builder-snap TELEGRAM_MTK_CHAT_ID="..."
fly secrets set --app dz-builder-snap TELEGRAM_MTK_THREAD_ID="..."
```

The entrypoint maps SoC-specific Telegram values to `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` when the generic values are not already set.

PixelDrain is only used when `MODE=execute` and `PIXELDRAIN_API_KEY` exists:

```sh
fly secrets set --app dz-builder-snap PIXELDRAIN_API_KEY="..."
```

## Dry Run

The default `fly.toml` environment is a safe dry run:

```sh
fly deploy --remote-only
fly logs --app dz-builder-snap
```

To run a dry run with explicit values:

```sh
fly deploy --remote-only \
  --env SOC=snapdragon \
  --env MODE=dry_run \
  --env NOTIFY_TELEGRAM=false \
  --env DEVICE_CODENAME=garnet \
  --env FINAL_NAME=DeadZone_Test \
  --env PLATFORM=os3_a16 \
  --env FLAVOR=legend \
  --env ANDROID_VERSION=16 \
  --env MI_VERSION=OS3.0.303.0.WNOCNXM \
  --env VBMETA_MODE=3
```

Dry runs do not require Telegram or PixelDrain secrets.

## Execute Build

Use `MODE=execute` and provide either `ROM_URL` or `ROM_PATH`. When `ROM_PATH` is omitted, the worker downloads the ROM into `/work/_input_roms`.

```sh
fly deploy --remote-only \
  --env SOC=snapdragon \
  --env MODE=execute \
  --env ROM_URL="https://example.com/path/to/rom.zip" \
  --env DEVICE_CODENAME=garnet \
  --env FINAL_NAME=DeadZone_Legend_Garnet \
  --env PLATFORM=os3_a16 \
  --env FLAVOR=legend \
  --env ANDROID_VERSION=16 \
  --env MI_VERSION=OS3.0.303.0.WNOCNXM \
  --env VBMETA_MODE=3 \
  --env NOTIFY_TELEGRAM=true
```

The pipeline runs:

```sh
python -m factory.pipeline.legacy_build_orchestrator \
  --rom "$ROM_FILE" \
  --output-dir /work/output \
  --build-name "$FINAL_NAME" \
  --device "$DEVICE" \
  --soc "$SOC" \
  --platform "$PLATFORM" \
  --flavor "$FLAVOR" \
  --android-version "$ANDROID_VERSION" \
  --mi-version "$MI_VERSION" \
  --vbmeta-mode "$VBMETA_MODE" \
  --template-zip /app/third_party/mezo_core/templates/deadzone_fastboot \
  --execute
```

`--telegram` is added only when `NOTIFY_TELEGRAM=true` and Telegram token/chat secrets are available.

## Switch SoC

Snapdragon:

```sh
fly deploy --remote-only --env SOC=snapdragon --env DEVICE_CODENAME=garnet
```

MTK:

```sh
fly deploy --remote-only --env SOC=mtk --env DEVICE_CODENAME=zircon
```

Supported flavor aliases match the GitHub factories:

```text
base -> deadzone
gaming -> deadzone_gaming
epic -> deadzone_epic
legend -> deadzone_legend
```
