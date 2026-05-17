# DeadZone Upload Policy

## Upload targets

| `upload_target` | Behaviour |
|---|---|
| `pixeldrain` (default) | Final ROM ZIP is uploaded to PixelDrain; public link is sent to the SoC Telegram bot |
| `none` | No upload happens; SoC bot is notified that the build succeeded but upload was skipped |

PixelDrain is the **only** public release channel. GitHub Actions artifacts are **not** a release mechanism.

---

## GitHub Actions artifact uploads (disabled by default)

The `upload_debug_artifacts` workflow input (default: `false`) controls whether build outputs
and EROFS diagnostic logs are stored as GitHub Actions artifacts.

| `upload_debug_artifacts` | GitHub artifacts stored? |
|---|---|
| `false` (default) | No — nothing is stored on GitHub |
| `true` | Yes — outputs + EROFS logs are stored for 7–14 days |

Enable `upload_debug_artifacts=true` **only** when debugging a build failure.
Never leave it enabled for production builds.

---

## Device / ROM URL must match

The workflow validates the selected device against the downloaded ROM filename before starting MEZO.

If the ROM filename contains a known codename that does not match the selected device, the build is **aborted** before MEZO starts:

```
[DEVICE GUARD] Selected device : amethyst
[DEVICE GUARD] ROM filename    : garnet-ota-os3.2.zip
[DEVICE GUARD] Detected ROM device: garnet
[DEVICE GUARD] Refusing to build mismatched ROM.
```

The relevant SoC Telegram bot receives a mismatch alert.

If no codename can be detected from the ROM filename (e.g. generic filename), a warning is printed and the build continues. Detection is filename-based only — no content inspection.

---

## What is uploaded to PixelDrain

Only the **final public ROM ZIP** produced by MEZO (`DeadZone_*.zip`).

Never uploaded:
- Source ROM from `_input_roms/`
- Log or diagnostic ZIPs
- Cache files
- Any file from `MEZO_APP/` or `_asset_downloads/`

The public link is:
- Printed to the workflow log
- Sent to the SoC Telegram bot
- Written to `output/reports/pixeldrain_upload.json`

---

## What must never be committed

- ROM ZIPs (source or output)
- Telegram bot tokens or chat IDs
- PixelDrain API key
- Log files that may contain secrets

All credentials come exclusively from GitHub Secrets.
