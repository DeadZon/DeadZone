#!/usr/bin/env bash
# DeadZone Fly machine entrypoint — OrangeFox-style direct runner.
# Receives all build inputs as env vars from `flyctl machine run --env ...`.
# Calls factory.pipeline.orchestrator exactly as GitHub direct workflows do.
set -euo pipefail

# ── Constants ─────────────────────────────────────────────────────────────────

APP_DIR="/app"
INPUT_DIR="${APP_DIR}/_input_roms"
OUTPUT_DIR="${APP_DIR}/output"
REPORTS_DIR="${OUTPUT_DIR}/reports"
LOGS_DIR="${OUTPUT_DIR}/logs"

TELEGRAM_SCRIPT="${APP_DIR}/scripts/deadzone_fly_telegram.py"

# ── Helpers ───────────────────────────────────────────────────────────────────

log()   { printf '[fly-entrypoint] %s\n' "$*"; }
stage() { printf '\n[fly-entrypoint] ===== %s =====\n' "$*"; }
fail()  {
  stage "FAILED"
  printf '[fly-entrypoint] ERROR: %s\n' "$*" >&2
  _tg_send "failed" "Failed: $*" || true
  exit 1
}

truthy() {
  case "${1:-}" in
    true|TRUE|1|yes|YES|y|Y) return 0 ;;
    *) return 1 ;;
  esac
}

_elapsed() {
  local secs=$(( $(date +%s) - _BUILD_START_TS ))
  printf '%dm %ds' $(( secs / 60 )) $(( secs % 60 ))
}

_tg_send() {
  local action="${1:-update}"
  local detail="${2:-}"
  if [ -f "$TELEGRAM_SCRIPT" ] && truthy "${DEADZONE_NOTIFY_TELEGRAM:-false}"; then
    python3 "$TELEGRAM_SCRIPT" \
      --action "$action" \
      --detail "$detail" \
      --codename "${DEADZONE_DEVICE_CODENAME:-unknown}" \
      --soc "${DEADZONE_SOC:-unknown}" \
      --edition "${DEADZONE_EDITION:-free}" \
      --mode "${DEADZONE_MODE:-dry_run}" \
      --listmezo-mode "${LISTMEZO_MODE:-dry_run}" \
      --elapsed "$(_elapsed)" \
      2>/dev/null || true
  fi
}

# ── Read env inputs ───────────────────────────────────────────────────────────

_BUILD_START_TS=$(date +%s)

DEADZONE_SOC="${DEADZONE_SOC:-}"
DEADZONE_DEVICE_CODENAME="${DEADZONE_DEVICE_CODENAME:-}"
DEADZONE_EDITION="${DEADZONE_EDITION:-free}"
DEADZONE_ROM_SOURCE="${DEADZONE_ROM_SOURCE:-manual_url}"
DEADZONE_ROM_URL="${DEADZONE_ROM_URL:-}"
DEADZONE_MODE="${DEADZONE_MODE:-dry_run}"
DEADZONE_UPLOAD_PIXELDRAIN="${DEADZONE_UPLOAD_PIXELDRAIN:-false}"
DEADZONE_NOTIFY_TELEGRAM="${DEADZONE_NOTIFY_TELEGRAM:-false}"
ENABLE_LISTMEZO="${ENABLE_LISTMEZO:-true}"
LISTMEZO_MODE="${LISTMEZO_MODE:-dry_run}"
LISTMEZO_EDITION="${LISTMEZO_EDITION:-free}"

TELEGRAM_BOT_TOKEN="${TELEGRAM_BOT_TOKEN:-}"
TELEGRAM_CHAT_ID="${TELEGRAM_CHAT_ID:-}"
TELEGRAM_GROUP_ID="${TELEGRAM_GROUP_ID:-}"
TELEGRAM_MSG_ID="${TELEGRAM_MSG_ID:-}"
PIXELDRAIN_API_KEY="${PIXELDRAIN_API_KEY:-}"

GITHUB_RUN_ID="${GITHUB_RUN_ID:-}"
GITHUB_SERVER_URL="${GITHUB_SERVER_URL:-https://github.com}"
GITHUB_REPOSITORY="${GITHUB_REPOSITORY:-}"
GITHUB_ACTOR="${GITHUB_ACTOR:-}"

export PYTHONPATH="${APP_DIR}${PYTHONPATH:+:${PYTHONPATH}}"
export PYTHONUNBUFFERED=1
export ENABLE_LISTMEZO LISTMEZO_MODE LISTMEZO_EDITION
export PIXELDRAIN_API_KEY TELEGRAM_BOT_TOKEN TELEGRAM_CHAT_ID TELEGRAM_GROUP_ID TELEGRAM_MSG_ID

# ── Stage 1: Boot ─────────────────────────────────────────────────────────────

stage "BOOTING"
log "DeadZone Fly machine entrypoint starting"
log "App directory: ${APP_DIR}"
cd "$APP_DIR"

# ── Stage 2: Create output dirs ───────────────────────────────────────────────

stage "PREPARING_DIRS"
mkdir -p "$INPUT_DIR" "$REPORTS_DIR" "$LOGS_DIR"
log "Input dir  : $INPUT_DIR"
log "Output dir : $OUTPUT_DIR"
log "Reports dir: $REPORTS_DIR"

# ── Stage 3: Print safe inputs (never print secrets) ─────────────────────────

stage "VALIDATING_INPUTS"
log "DEADZONE_SOC              = ${DEADZONE_SOC}"
log "DEADZONE_DEVICE_CODENAME  = ${DEADZONE_DEVICE_CODENAME}"
log "DEADZONE_EDITION          = ${DEADZONE_EDITION}"
log "DEADZONE_ROM_SOURCE       = ${DEADZONE_ROM_SOURCE}"
log "DEADZONE_ROM_URL          = ${DEADZONE_ROM_URL:-(empty)}"
log "DEADZONE_MODE             = ${DEADZONE_MODE}"
log "DEADZONE_UPLOAD_PIXELDRAIN= ${DEADZONE_UPLOAD_PIXELDRAIN}"
log "DEADZONE_NOTIFY_TELEGRAM  = ${DEADZONE_NOTIFY_TELEGRAM}"
log "ENABLE_LISTMEZO           = ${ENABLE_LISTMEZO}"
log "LISTMEZO_MODE             = ${LISTMEZO_MODE}"
log "LISTMEZO_EDITION          = ${LISTMEZO_EDITION}"
log "GITHUB_RUN_ID             = ${GITHUB_RUN_ID:-(not set)}"
log "GITHUB_REPOSITORY         = ${GITHUB_REPOSITORY:-(not set)}"
log "PIXELDRAIN_API_KEY        = ${PIXELDRAIN_API_KEY:+(set)}"
log "TELEGRAM_BOT_TOKEN        = ${TELEGRAM_BOT_TOKEN:+(set)}"
log "TELEGRAM_CHAT_ID          = ${TELEGRAM_CHAT_ID:+(set)}"
log "TELEGRAM_MSG_ID           = ${TELEGRAM_MSG_ID:-(empty — will create new)}"

# Required env validation
[ -z "$DEADZONE_SOC" ]              && fail "DEADZONE_SOC is required (mtk or snapdragon)"
[ -z "$DEADZONE_DEVICE_CODENAME" ]  && fail "DEADZONE_DEVICE_CODENAME is required"
[ -z "$DEADZONE_EDITION" ]          && fail "DEADZONE_EDITION is required"
[ -z "$DEADZONE_MODE" ]             && fail "DEADZONE_MODE is required"

case "$DEADZONE_SOC" in
  mtk|snapdragon) ;;
  *) fail "DEADZONE_SOC must be 'mtk' or 'snapdragon', got: '${DEADZONE_SOC}'" ;;
esac

case "$DEADZONE_EDITION" in
  free|gaming|legend|epic) ;;
  *) fail "DEADZONE_EDITION must be one of: free, gaming, legend, epic — got: '${DEADZONE_EDITION}'" ;;
esac

case "$DEADZONE_MODE" in
  dry_run|execute) ;;
  *) fail "DEADZONE_MODE must be 'dry_run' or 'execute', got: '${DEADZONE_MODE}'" ;;
esac

for BAD in select_device_codename select_device device none null default; do
  if [ "$DEADZONE_DEVICE_CODENAME" = "$BAD" ]; then
    fail "Invalid DEADZONE_DEVICE_CODENAME: '${DEADZONE_DEVICE_CODENAME}'. Enter a real codename."
  fi
done

# Validate ROM URL when needed
if [ "$DEADZONE_MODE" = "execute" ] && [ "${DEADZONE_ROM_SOURCE:-manual_url}" = "manual_url" ]; then
  if [ -z "$DEADZONE_ROM_URL" ]; then
    fail "DEADZONE_ROM_URL is required in execute mode with rom_source=manual_url"
  fi
  case "$DEADZONE_ROM_URL" in
    http://*|https://*) ;;
    *) fail "DEADZONE_ROM_URL must start with http:// or https://" ;;
  esac
fi

log "[OK] All required inputs validated."

# ── Stage 4: Telegram start notification ─────────────────────────────────────

_tg_send "start" "Fly machine booted — validating inputs"

# ── Stage 5: Download ROM (execute mode, manual_url) ─────────────────────────

ROM_PATH=""
if [ "$DEADZONE_MODE" = "execute" ] && [ -n "$DEADZONE_ROM_URL" ]; then
  stage "DOWNLOADING_ROM"
  _tg_send "update" "Downloading source ROM"

  case "$DEADZONE_ROM_URL" in
    *.tgz)    ROM_FILE="${INPUT_DIR}/source_rom.tgz" ;;
    *.tar.gz) ROM_FILE="${INPUT_DIR}/source_rom.tar.gz" ;;
    *.zip)    ROM_FILE="${INPUT_DIR}/source_rom.zip" ;;
    *)        ROM_FILE="${INPUT_DIR}/source_rom.zip" ;;
  esac

  log "Downloading ROM from: ${DEADZONE_ROM_URL}"
  log "Saving to: ${ROM_FILE}"

  curl -L --fail --retry 5 --retry-delay 10 --connect-timeout 30 \
    --user-agent "DeadZoneFlyFactory/1.0" \
    -o "$ROM_FILE" "$DEADZONE_ROM_URL"

  if [ ! -f "$ROM_FILE" ]; then
    fail "ROM file not found after download: ${ROM_FILE}"
  fi

  ROM_SIZE=$(stat -c%s "$ROM_FILE" 2>/dev/null || stat -f%z "$ROM_FILE" 2>/dev/null || echo 0)
  MIN_SIZE=$(( 100 * 1024 * 1024 ))
  log "ROM size: ${ROM_SIZE} bytes"
  if [ "$ROM_SIZE" -lt "$MIN_SIZE" ]; then
    fail "ROM file too small (${ROM_SIZE} bytes < 100MB). Download may have failed."
  fi

  log "[OK] ROM download validated."
  ROM_PATH="$ROM_FILE"
  _tg_send "update" "ROM downloaded ($(( ROM_SIZE / 1024 / 1024 ))MB)"
fi

# ── Stage 6: Run factory pipeline (same orchestrator as GitHub direct) ────────

stage "RUNNING_PIPELINE"
_tg_send "update" "Launching DeadZone factory pipeline"

ORCHESTRATOR_ARGS=(
  python3 -m factory.pipeline.orchestrator
  --soc    "$DEADZONE_SOC"
  --codename "$DEADZONE_DEVICE_CODENAME"
  --edition  "$DEADZONE_EDITION"
  --mode     "$DEADZONE_MODE"
)

if [ -n "$DEADZONE_ROM_URL" ]; then
  ORCHESTRATOR_ARGS+=(--rom-url "$DEADZONE_ROM_URL")
fi

if [ -n "$ROM_PATH" ]; then
  ORCHESTRATOR_ARGS+=(--rom "$ROM_PATH")
fi

if truthy "$DEADZONE_UPLOAD_PIXELDRAIN"; then
  ORCHESTRATOR_ARGS+=(--upload-pixeldrain)
fi

if truthy "$DEADZONE_NOTIFY_TELEGRAM"; then
  ORCHESTRATOR_ARGS+=(--notify-telegram)
fi

log "Orchestrator command: ${ORCHESTRATOR_ARGS[*]}"

PIPELINE_EXIT=0
"${ORCHESTRATOR_ARGS[@]}" || PIPELINE_EXIT=$?

# ── Stage 7: Check result and send final Telegram message ─────────────────────

stage "FINALIZING"

if [ "$PIPELINE_EXIT" -ne 0 ]; then
  log "[FAIL] Pipeline exited with code ${PIPELINE_EXIT}"

  # Dump recent logs for GitHub Actions output
  for LOG in "${LOGS_DIR}"/*.log; do
    [ -f "$LOG" ] && { echo "=== $(basename "$LOG") ==="; tail -50 "$LOG"; } || true
  done
  if [ -f "${REPORTS_DIR}/pipeline_report.json" ]; then
    echo "=== pipeline_report.json ==="
    cat "${REPORTS_DIR}/pipeline_report.json" || true
  fi

  _tg_send "failed" "Pipeline exited with code ${PIPELINE_EXIT}. Check GitHub logs."
  exit "$PIPELINE_EXIT"
fi

log "[OK] Pipeline completed successfully."

# Send final group notification if GROUP_ID configured
if [ -n "$TELEGRAM_GROUP_ID" ] && truthy "$DEADZONE_NOTIFY_TELEGRAM"; then
  python3 "$TELEGRAM_SCRIPT" \
    --action "group_success" \
    --detail "Build complete" \
    --codename "$DEADZONE_DEVICE_CODENAME" \
    --soc "$DEADZONE_SOC" \
    --edition "$DEADZONE_EDITION" \
    --mode "$DEADZONE_MODE" \
    --listmezo-mode "$LISTMEZO_MODE" \
    --elapsed "$(_elapsed)" \
    2>/dev/null || true
fi

stage "DONE"
log "DeadZone Fly build finished successfully. Elapsed: $(_elapsed)"
exit 0
