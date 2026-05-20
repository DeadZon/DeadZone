#!/usr/bin/env bash
set -Eeuo pipefail

APP_DIR="/app"
WORK_DIR="/work"
INPUT_DIR="${WORK_DIR}/_input_roms"
OUTPUT_DIR="${WORK_DIR}/output"
TEMPLATE_ZIP="${TEMPLATE_ZIP:-${APP_DIR}/third_party/mezo_core/templates/deadzone_fastboot}"

log() {
  printf '[fly-entrypoint] %s\n' "$*"
}

stage() {
  log "===== $* ====="
}

fail() {
  stage "FAILED"
  printf '[fly-entrypoint] ERROR: %s\n' "$*" >&2
  exit 1
}

on_error() {
  local exit_code=$?
  stage "FAILED"
  log "Worker failed with exit code ${exit_code}"
  exit "$exit_code"
}
trap on_error ERR

truthy() {
  case "${1:-}" in
    true | TRUE | 1 | yes | YES | y | Y) return 0 ;;
    *) return 1 ;;
  esac
}

normalize_flavor() {
  case "${1:-}" in
    base) printf 'deadzone' ;;
    gaming) printf 'deadzone_gaming' ;;
    epic) printf 'deadzone_epic' ;;
    legend) printf 'deadzone_legend' ;;
    deadzone | deadzone_gaming | deadzone_epic | deadzone_legend) printf '%s' "$1" ;;
    *) printf '%s' "${1:-}" ;;
  esac
}

resolve_device() {
  if [ -n "${CUSTOM_DEVICE:-}" ] && [ "${CUSTOM_DEVICE}" != "select_device_codename" ]; then
    printf '%s' "$CUSTOM_DEVICE"
    return
  fi

  printf '%s' "${DEVICE_CODENAME%% | *}"
}

map_telegram_env() {
  case "$SOC" in
    snapdragon)
      export TELEGRAM_BOT_TOKEN="${TELEGRAM_BOT_TOKEN:-${TELEGRAM_SNAPDRAGON_BOT_TOKEN:-}}"
      export TELEGRAM_CHAT_ID="${TELEGRAM_CHAT_ID:-${TELEGRAM_SNAPDRAGON_CHAT_ID:-}}"
      export TELEGRAM_THREAD_ID="${TELEGRAM_THREAD_ID:-${TELEGRAM_SNAPDRAGON_THREAD_ID:-}}"
      ;;
    mtk)
      export TELEGRAM_BOT_TOKEN="${TELEGRAM_BOT_TOKEN:-${TELEGRAM_MTK_BOT_TOKEN:-}}"
      export TELEGRAM_CHAT_ID="${TELEGRAM_CHAT_ID:-${TELEGRAM_MTK_CHAT_ID:-}}"
      export TELEGRAM_THREAD_ID="${TELEGRAM_THREAD_ID:-${TELEGRAM_MTK_THREAD_ID:-}}"
      ;;
  esac
}

download_rom() {
  local url="$1"
  local filename
  local output_path

  mkdir -p "$INPUT_DIR"
  filename="${url%%\?*}"
  filename="${filename##*/}"
  if [ -z "$filename" ] || [ "$filename" = "$url" ]; then
    filename="input_rom.zip"
  fi

  output_path="${INPUT_DIR}/${filename}"
  printf '[fly-entrypoint] Downloading ROM from ROM_URL\n' >&2
  printf '[fly-entrypoint] Saving ROM to %s\n' "$output_path" >&2
  curl --fail --location --show-error --progress-bar \
    --user-agent "DeadZoneFlyFactory/1.0" \
    "$url" \
    --output "$output_path"
  printf '%s' "$output_path"
}

cleanup_output() {
  stage "CLEANING_OUTPUT"
  log "Removing transient ROM input and staging directories"
  rm -rf "${INPUT_DIR:?}/"* 2>/dev/null || true
  rm -rf "${OUTPUT_DIR}/tmp" "${OUTPUT_DIR}/work" 2>/dev/null || true
  find "${OUTPUT_DIR}" -maxdepth 3 -name '*_unpacked' -type d -exec rm -rf {} + 2>/dev/null || true
}

maybe_keep_alive() {
  if truthy "${KEEP_ALIVE_AFTER_RUN:-false}"; then
    log "KEEP_ALIVE_AFTER_RUN=true; keeping Fly machine alive"
    tail -f /dev/null
  fi
}

find_final_zip() {
  find "${OUTPUT_DIR}/final" -maxdepth 1 -name '*.zip' -type f 2>/dev/null | head -n 1
}

upload_pixeldrain_if_allowed() {
  local final_zip

  if [ "$MODE" != "execute" ]; then
    log "PixelDrain upload skipped: MODE=${MODE}"
    return 0
  fi

  if [ -z "${PIXELDRAIN_API_KEY:-}" ]; then
    log "PixelDrain upload skipped: PIXELDRAIN_API_KEY is not set"
    return 0
  fi

  final_zip="$(find_final_zip)"
  if [ -z "$final_zip" ]; then
    fail "PixelDrain upload requested, but no final ZIP exists in ${OUTPUT_DIR}/final"
  fi

  log "Uploading final ROM ZIP to PixelDrain: ${final_zip}"
  (
    cd "$WORK_DIR"
    python3 -m factory.services.pixeldrain_upload "$final_zip"
  )

  if [ -f "${OUTPUT_DIR}/reports/pixeldrain_upload.json" ]; then
    log "PixelDrain sidecar written to ${OUTPUT_DIR}/reports/pixeldrain_upload.json"
  fi
  find "${OUTPUT_DIR}/final" -maxdepth 1 -name '*.zip' -type f -delete 2>/dev/null || true
  log "Removed local final ZIP after successful PixelDrain upload"
}

SOC="${SOC:-snapdragon}"
MODE="${MODE:-dry_run}"
ROM_URL="${ROM_URL:-}"
ROM_PATH="${ROM_PATH:-}"
DEVICE_CODENAME="${DEVICE_CODENAME:-}"
CUSTOM_DEVICE="${CUSTOM_DEVICE:-}"
FINAL_NAME="${FINAL_NAME:-}"
PLATFORM="${PLATFORM:-}"
FLAVOR="$(normalize_flavor "${FLAVOR:-}")"
ANDROID_VERSION="${ANDROID_VERSION:-}"
MI_VERSION="${MI_VERSION:-}"
VBMETA_MODE="${VBMETA_MODE:-}"
NOTIFY_TELEGRAM="${NOTIFY_TELEGRAM:-false}"
KEEP_ALIVE_AFTER_RUN="${KEEP_ALIVE_AFTER_RUN:-false}"

stage "STARTING"
log "DeadZone Fly builder starting"
log "Source directory: ${APP_DIR}"
log "Work directory: ${WORK_DIR}"

export PYTHONPATH="${APP_DIR}${PYTHONPATH:+:${PYTHONPATH}}"
cd "$APP_DIR"
mkdir -p "$INPUT_DIR" "$OUTPUT_DIR"

stage "VALIDATING_INPUTS"
case "$SOC" in
  snapdragon | mtk) ;;
  *) fail "SOC must be 'snapdragon' or 'mtk' (got '${SOC}')" ;;
esac

case "$MODE" in
  dry_run | execute) ;;
  *) fail "MODE must be 'dry_run' or 'execute' (got '${MODE}')" ;;
esac

EFFECTIVE_DEVICE="$(resolve_device)"
if [ -z "$EFFECTIVE_DEVICE" ] || [ "$EFFECTIVE_DEVICE" = "select_device_codename" ]; then
  fail "DEVICE_CODENAME or CUSTOM_DEVICE must be set"
fi

[ -n "$FINAL_NAME" ] || fail "FINAL_NAME must be set"
[ -n "$PLATFORM" ] || fail "PLATFORM must be set"
[ -n "$FLAVOR" ] || fail "FLAVOR must be set"
[ -n "$ANDROID_VERSION" ] || fail "ANDROID_VERSION must be set"
[ -n "$MI_VERSION" ] || fail "MI_VERSION must be set"
[ -n "$VBMETA_MODE" ] || fail "VBMETA_MODE must be set"
[ -d "$TEMPLATE_ZIP" ] || fail "Fastboot template directory not found: ${TEMPLATE_ZIP}"

if [ "$MODE" = "execute" ] && [ -z "$ROM_URL" ] && [ -z "$ROM_PATH" ]; then
  fail "MODE=execute requires ROM_URL or ROM_PATH"
fi

map_telegram_env

log "SOC=${SOC}"
log "MODE=${MODE}"
log "DEVICE=${EFFECTIVE_DEVICE}"
log "FINAL_NAME=${FINAL_NAME}"
log "PLATFORM=${PLATFORM}"
log "FLAVOR=${FLAVOR}"
log "ANDROID_VERSION=${ANDROID_VERSION}"
log "MI_VERSION=${MI_VERSION}"
log "VBMETA_MODE=${VBMETA_MODE}"
log "NOTIFY_TELEGRAM=${NOTIFY_TELEGRAM}"

python3 -m factory.cli validate-registry

ROM_FILE=""
if [ -n "$ROM_PATH" ]; then
  ROM_FILE="$ROM_PATH"
  stage "DOWNLOADING_ROM"
  log "ROM_PATH provided; download skipped: ${ROM_FILE}"
elif [ -n "$ROM_URL" ]; then
  stage "DOWNLOADING_ROM"
  ROM_FILE="$(download_rom "$ROM_URL")"
else
  stage "DOWNLOADING_ROM"
  log "No ROM_URL or ROM_PATH provided; dry_run will run without --rom"
fi

if [ -n "$ROM_FILE" ] && [ ! -f "$ROM_FILE" ]; then
  fail "ROM file not found: ${ROM_FILE}"
fi

TELEGRAM_FLAG=()
if truthy "$NOTIFY_TELEGRAM" && [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ]; then
  TELEGRAM_FLAG=(--telegram)
  log "Telegram enabled"
else
  log "Telegram disabled or missing token/chat ID"
fi

PIPELINE_CMD=(
  python3 -m factory.pipeline.legacy_build_orchestrator
  --output-dir "$OUTPUT_DIR"
  --build-name "$FINAL_NAME"
  --device "$EFFECTIVE_DEVICE"
  --soc "$SOC"
  --platform "$PLATFORM"
  --flavor "$FLAVOR"
  --android-version "$ANDROID_VERSION"
  --mi-version "$MI_VERSION"
  --vbmeta-mode "$VBMETA_MODE"
  --template-zip "$TEMPLATE_ZIP"
)

if [ -n "$ROM_FILE" ]; then
  PIPELINE_CMD+=(--rom "$ROM_FILE")
fi

if [ "$MODE" = "execute" ]; then
  PIPELINE_CMD+=(--execute)
fi

PIPELINE_CMD+=("${TELEGRAM_FLAG[@]}")

stage "RUNNING_PIPELINE"
log "Running legacy build orchestrator"
"${PIPELINE_CMD[@]}"

upload_pixeldrain_if_allowed
cleanup_output

stage "FINISHED"
log "DeadZone Fly builder completed successfully"
maybe_keep_alive
