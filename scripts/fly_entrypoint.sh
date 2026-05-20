#!/usr/bin/env bash
set -Eeuo pipefail

log() {
  printf '[fly-entrypoint] %s\n' "$*"
}

fail() {
  printf '[fly-entrypoint] ERROR: %s\n' "$*" >&2
  exit 1
}

normalize_flavor() {
  case "$1" in
    base) printf 'deadzone' ;;
    gaming) printf 'deadzone_gaming' ;;
    epic) printf 'deadzone_epic' ;;
    legend) printf 'deadzone_legend' ;;
    *) printf '%s' "$1" ;;
  esac
}

map_telegram_env() {
  case "$SOC" in
    snapdragon)
      export TELEGRAM_BOT_TOKEN="${TELEGRAM_BOT_TOKEN:-${TELEGRAM_SNAPDRAGON_BOT_TOKEN:-}}"
      export TELEGRAM_CHAT_ID="${TELEGRAM_CHAT_ID:-${TELEGRAM_SNAPDRAGON_CHAT_ID:-}}"
      export TELEGRAM_THREAD_ID="${TELEGRAM_THREAD_ID:-${TELEGRAM_SNAPDRAGON_THREAD_ID:-${TELEGRAM_MESSAGE_THREAD_ID:-}}}"
      ;;
    mtk)
      export TELEGRAM_BOT_TOKEN="${TELEGRAM_BOT_TOKEN:-${TELEGRAM_MTK_BOT_TOKEN:-}}"
      export TELEGRAM_CHAT_ID="${TELEGRAM_CHAT_ID:-${TELEGRAM_MTK_CHAT_ID:-}}"
      export TELEGRAM_THREAD_ID="${TELEGRAM_THREAD_ID:-${TELEGRAM_MTK_THREAD_ID:-${TELEGRAM_MESSAGE_THREAD_ID:-}}}"
      ;;
  esac
}

prepare_rom_from_url() {
  local url="$1"
  local output_dir="_input_roms"
  local filename

  mkdir -p "$output_dir"
  filename="${url%%\?*}"
  filename="${filename##*/}"
  if [ -z "$filename" ] || [ "$filename" = "$url" ]; then
    filename="input_rom.zip"
  fi

  printf '[fly-entrypoint] Downloading ROM from ROM_URL into %s/%s\n' "$output_dir" "$filename" >&2
  curl --fail --location --show-error --progress-bar "$url" --output "${output_dir}/${filename}"
  printf '%s\n' "${output_dir}/${filename}"
}

SOC="${SOC:-snapdragon}"
MODE="${MODE:-dry_run}"
NOTIFY_TELEGRAM="${NOTIFY_TELEGRAM:-false}"
DEVICE_CODENAME="${DEVICE_CODENAME:-garnet}"
FINAL_NAME="${FINAL_NAME:-DeadZone_Test}"
PLATFORM="${PLATFORM:-os3_a16}"
FLAVOR="$(normalize_flavor "${FLAVOR:-deadzone}")"
ANDROID_VERSION="${ANDROID_VERSION:-16}"
MI_VERSION="${MI_VERSION:-OS3.0.303.0.WNOCNXM}"
VBMETA_MODE="${VBMETA_MODE:-3}"
OUTPUT_DIR="${OUTPUT_DIR:-output}"
TEMPLATE_ZIP="${TEMPLATE_ZIP:-third_party/mezo_core/templates/deadzone_fastboot}"

case "$SOC" in
  snapdragon | mtk) ;;
  *) fail "Unknown SOC '${SOC}'. Expected 'snapdragon' or 'mtk'." ;;
esac

case "$MODE" in
  dry_run | execute) ;;
  *) fail "Unknown MODE '${MODE}'. Expected 'dry_run' or 'execute'." ;;
esac

map_telegram_env

log "DeadZone Fly worker starting"
log "SOC=${SOC}"
log "MODE=${MODE}"
log "DEVICE_CODENAME=${DEVICE_CODENAME}"
log "FINAL_NAME=${FINAL_NAME}"
log "PLATFORM=${PLATFORM}"
log "FLAVOR=${FLAVOR}"
log "NOTIFY_TELEGRAM=${NOTIFY_TELEGRAM}"
log "Selected ${SOC} workflow-equivalent pipeline command"

python3 -m factory.cli validate-registry

TELEGRAM_FLAG=()
if [ "$NOTIFY_TELEGRAM" = "true" ] && [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ]; then
  TELEGRAM_FLAG=(--telegram)
  log "Telegram notifications enabled for ${SOC}"
else
  log "Telegram notifications disabled or missing non-required env"
fi

if [ "$MODE" = "dry_run" ]; then
  log "Running existing DeadZone pipeline in dry-run mode"
  exec python3 -m factory.pipeline.legacy_build_orchestrator \
    --output-dir "$OUTPUT_DIR" \
    --build-name "$FINAL_NAME" \
    --device "$DEVICE_CODENAME" \
    --soc "$SOC" \
    --platform "$PLATFORM" \
    --flavor "$FLAVOR" \
    --android-version "$ANDROID_VERSION" \
    --mi-version "$MI_VERSION" \
    --vbmeta-mode "$VBMETA_MODE" \
    --template-zip "$TEMPLATE_ZIP" \
    "${TELEGRAM_FLAG[@]}"
fi

if [ -n "${ROM_PATH:-}" ]; then
  ROM_FILE="$ROM_PATH"
elif [ -n "${ROM_URL:-}" ]; then
  ROM_FILE="$(prepare_rom_from_url "$ROM_URL")"
else
  fail "MODE=execute requires ROM_PATH or ROM_URL. No secrets are required for dry_run."
fi

[ -f "$ROM_FILE" ] || fail "ROM file not found: ${ROM_FILE}"

log "Running existing DeadZone pipeline in execute mode"
exec python3 -m factory.pipeline.legacy_build_orchestrator \
  --rom "$ROM_FILE" \
  --output-dir "$OUTPUT_DIR" \
  --build-name "$FINAL_NAME" \
  --device "$DEVICE_CODENAME" \
  --soc "$SOC" \
  --platform "$PLATFORM" \
  --flavor "$FLAVOR" \
  --android-version "$ANDROID_VERSION" \
  --mi-version "$MI_VERSION" \
  --vbmeta-mode "$VBMETA_MODE" \
  --template-zip "$TEMPLATE_ZIP" \
  --execute \
  "${TELEGRAM_FLAG[@]}"
