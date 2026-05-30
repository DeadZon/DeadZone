#!/bin/bash
set -e

echo "=========================================="
echo "  DeadZone MTK Builder (Fly.io)"
echo "  Device: ${DEVICE_CODENAME}"
echo "  Style:  ${STYLE}"
echo "  SoC:    MediaTek"
echo "=========================================="

# ── Telegram group forwarder ─────────────────────────────────────────────────
# The Python TelegramStatus handles personal chat with live edits.
# This function forwards final/key messages to the group chat.
send_group() {
    if [ -z "${TELEGRAM_MTK_GROUP_ID}" ] || [ -z "${TELEGRAM_MTK_BOT_TOKEN}" ]; then
        return 0
    fi
    curl -s --fail \
      -X POST "https://api.telegram.org/bot${TELEGRAM_MTK_BOT_TOKEN}/sendMessage" \
      -d chat_id="${TELEGRAM_MTK_GROUP_ID}" \
      -d text="$1" \
      -d parse_mode="Markdown" \
      -d disable_web_page_preview=true > /dev/null 2>&1 || true
}

# ── Swap file (48GB) ─────────────────────────────────────────────────────────
echo "[SETUP] Creating 48GB swap file..."
cd /mnt/dz_data

if [ -f "/mnt/dz_data/swapfile" ]; then
    SWAP_SIZE=$(stat -c%s "/mnt/dz_data/swapfile" 2>/dev/null || echo 0)
    if [ "$SWAP_SIZE" -ne 51539607552 ]; then
        swapoff /mnt/dz_data/swapfile || true
        rm -f /mnt/dz_data/swapfile
    fi
fi

if [ ! -f "/mnt/dz_data/swapfile" ]; then
    fallocate -l 48G /mnt/dz_data/swapfile || dd if=/dev/zero of=/mnt/dz_data/swapfile bs=1M count=49152
    chmod 600 /mnt/dz_data/swapfile
    mkswap /mnt/dz_data/swapfile
fi
swapon /mnt/dz_data/swapfile || true
echo "[SETUP] Swap ready."

# ── Git config ───────────────────────────────────────────────────────────────
git config --global user.name "DeadZone-Builder"
git config --global user.email "deadzone@builder.fly"

# ── Clone DeadZone repo ──────────────────────────────────────────────────────
echo "[SETUP] Cloning DeadZone repository..."
mkdir -p /mnt/dz_data/build
cd /mnt/dz_data/build

if [ ! -d "DeadZone-main/.git" ]; then
    rm -rf DeadZone-main
    git clone https://github.com/${GITHUB_REPOSITORY}.git --depth 1 temp_repo
    mv temp_repo/DeadZone-main . 2>/dev/null || mv temp_repo/* . 2>/dev/null || true
    rm -rf temp_repo
fi

cd DeadZone-main

# ── Install Python deps ──────────────────────────────────────────────────────
echo "[SETUP] Installing Python dependencies..."
pip3 install -r requirements.txt 2>/dev/null || true

# ── Build DeadZone ───────────────────────────────────────────────────────────
# Python TelegramStatus sends live updates (personal chat + group via TELEGRAM_GROUP_ID)
echo "[BUILD] Starting DeadZone build..."
echo ""

send_group "🔥 *DeadZone MTK Build Started*
📱 **Device:** \`${DEVICE_CODENAME}\`
🎨 **Style:** \`${STYLE}\`
🎮 **SoC:** \`MediaTek\`
📦 **Mode:** \`${MODE}\`

⏳ Building on Fly.io..."

BUILD_START=$(date +%s)

set +e

ARGS=(
    --rom-url "$ROM_URL"
    --style "$STYLE"
    --soc mtk
    --mode "$MODE"
    --device-codename "$DEVICE_CODENAME"
)

if [ "$DEVICE_CODENAME" = "custom" ] && [ -n "$CUSTOM_CODENAME" ]; then
    ARGS+=(--custom-codename "$CUSTOM_CODENAME")
fi

if [ "$UPLOAD_PIXELDRAIN" = "true" ]; then
    ARGS+=(--upload-pixeldrain)
fi

# Enable Telegram notifications — Python handles personal chat live updates
ARGS+=(--notify-telegram)

if [ "$ALLOW_OVERSIZED" = "true" ]; then
    ARGS+=(--allow-oversized-final)
fi

python3 -m factory.deadzone "${ARGS[@]}"
EXIT_CODE=$?

BUILD_END=$(date +%s)
BUILD_DIFF=$((BUILD_END - BUILD_START))

echo ""
echo "=========================================="
if [ $EXIT_CODE -eq 0 ]; then
    echo "  BUILD COMPLETED SUCCESSFULLY"
    echo "  Time: $(($BUILD_DIFF / 60))m $(($BUILD_DIFF % 60))s"
    FINAL_ZIP=$(find output/final -name "*.zip" -type f 2>/dev/null | head -1)
    if [ -n "$FINAL_ZIP" ]; then
        echo "  Output: $FINAL_ZIP"
    fi

    send_group "🎉 *DeadZone MTK Build Completed!*
⏱️ Build Time: $(($BUILD_DIFF / 60)) mins and $(($BUILD_DIFF % 60)) secs.

📱 **Device:** \`${DEVICE_CODENAME}\`
🎨 **Style:** \`${STYLE}\`
🎮 **SoC:** \`MediaTek\`
📦 **Mode:** \`${MODE}\`"
else
    echo "  BUILD FAILED"
    echo "  Time: $(($BUILD_DIFF / 60))m $(($BUILD_DIFF % 60))s"

    send_group "❌ *DeadZone MTK Build Failed!*
⏱️ Time: $(($BUILD_DIFF / 60))m $(($BUILD_DIFF % 60))s

📱 **Device:** \`${DEVICE_CODENAME}\`
🎨 **Style:** \`${STYLE}\`

Check personal chat for detailed logs."
fi
echo "=========================================="

exit $EXIT_CODE
