"""Rebuild all DeadZone workflow YAML files from fresh valid templates.

Writes each file via Path.write_bytes so the output is guaranteed LF-only,
BOM-free UTF-8 regardless of the host OS line-ending settings.
"""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = REPO_ROOT / ".github" / "workflows"

# ---------------------------------------------------------------------------
# Shared helpers (written inline so each file is self-contained)
# ---------------------------------------------------------------------------

def _w(rel: str, content: str) -> None:
    path = WORKFLOWS / rel
    # Normalise to LF regardless of how this script file is line-ended.
    body = content.replace("\r\n", "\n").replace("\r", "\n")
    path.write_bytes(body.encode("utf-8"))
    lf = body.count("\n")
    print(f"  wrote {rel}  ({lf} LF lines, {len(body)} bytes)")


# ===========================================================================
# 1. deadzone_mtk.yml — GitHub local build, MTK
# ===========================================================================
MTK_LOCAL = """\
name: DeadZone MTK GitHub Build

on:
  workflow_dispatch:
    inputs:
      codename:
        description: "Device codename, e.g. zircon, garnet"
        required: true
        type: string

      custom_codename:
        description: "Optional override codename"
        required: false
        type: string

      edition:
        description: "ROM edition"
        required: true
        type: choice
        default: legend
        options:
          - free
          - gaming
          - legend
          - epic

      rom_url:
        description: "ROM download URL (leave as auto to use device default)"
        required: false
        default: "auto"
        type: string

      mode:
        description: "Build mode"
        required: true
        type: choice
        default: execute
        options:
          - dry_run
          - execute

      upload_pixeldrain:
        description: "Upload final ROM ZIP to PixelDrain"
        required: true
        type: boolean
        default: true

      notify_telegram:
        description: "Send Telegram live updates"
        required: true
        type: boolean
        default: true

jobs:
  build:
    name: "MTK | ${{ inputs.custom_codename || inputs.codename }} | ${{ inputs.edition }} | ${{ inputs.mode }}"
    runs-on: ubuntu-latest
    timeout-minutes: 180

    steps:
      - name: Validate inputs
        run: |
          set -euo pipefail

          CODENAME="${{ inputs.custom_codename }}"
          [ -z "$CODENAME" ] && CODENAME="${{ inputs.codename }}"
          CODENAME="$(echo "$CODENAME" | xargs)"

          if [ -z "$CODENAME" ]; then
            echo "[ERROR] codename is required. Please enter a real codename like zircon or garnet."
            exit 1
          fi

          for BAD in select_device_codename select_device device none null default; do
            if [ "$CODENAME" = "$BAD" ]; then
              echo "[ERROR] Invalid device codename: $CODENAME."
              echo "[ERROR] Please enter a real codename like zircon or garnet."
              exit 1
            fi
          done

          EDITION="${{ inputs.edition }}"
          case "$EDITION" in
            free|gaming|legend|epic) ;;
            *) echo "[ERROR] Invalid edition: $EDITION. Must be one of: free, gaming, legend, epic."; exit 1 ;;
          esac

          MODE="${{ inputs.mode }}"
          case "$MODE" in
            dry_run|execute) ;;
            *) echo "[ERROR] Invalid mode: $MODE. Must be dry_run or execute."; exit 1 ;;
          esac

          ROM_URL="${{ inputs.rom_url }}"
          if [ "$ROM_URL" = "auto" ]; then
            ROM_URL=""
          fi
          if [ "$MODE" = "execute" ]; then
            if [ -z "$ROM_URL" ]; then
              echo "[ERROR] rom_url is required for execute mode."
              exit 1
            fi
            case "$ROM_URL" in
              http://*|https://*) ;;
              *) echo "[ERROR] rom_url must start with http:// or https://"; exit 1 ;;
            esac
          fi

          echo "[OK] codename  = $CODENAME"
          echo "[OK] edition   = $EDITION"
          echo "[OK] mode      = $MODE"
          echo "[OK] rom_url   = $ROM_URL"
          echo "[OK] Inputs validated."

      - name: Normalize inputs
        id: norm
        run: |
          set -euo pipefail

          CODENAME="${{ inputs.custom_codename }}"
          [ -z "$CODENAME" ] && CODENAME="${{ inputs.codename }}"
          CODENAME="$(echo "$CODENAME" | xargs)"

          EDITION="${{ inputs.edition }}"
          case "$EDITION" in
            free) MOD="free" ;;
            gaming) MOD="gaming" ;;
            legend) MOD="legend" ;;
            epic) MOD="epic" ;;
            *) MOD="free" ;;
          esac

          if [ "$MOD" = "free" ]; then
            FINAL_NAME="DeadZone_${CODENAME}_V1"
          else
            FINAL_NAME="DeadZone_${CODENAME}_${MOD}_V1"
          fi

          MODE="${{ inputs.mode }}"
          ROM_URL="${{ inputs.rom_url }}"
          if [ "$ROM_URL" = "auto" ]; then
            ROM_URL=""
          fi
          UPLOAD_PD="${{ inputs.upload_pixeldrain }}"
          NOTIFY_TG="${{ inputs.notify_telegram }}"

          echo "codename=$CODENAME"           >> "$GITHUB_OUTPUT"
          echo "mod=$MOD"                     >> "$GITHUB_OUTPUT"
          echo "final_name=$FINAL_NAME"       >> "$GITHUB_OUTPUT"
          echo "mode=$MODE"                   >> "$GITHUB_OUTPUT"
          echo "rom_url=$ROM_URL"             >> "$GITHUB_OUTPUT"
          echo "upload_pixeldrain=$UPLOAD_PD" >> "$GITHUB_OUTPUT"
          echo "notify_telegram=$NOTIFY_TG"   >> "$GITHUB_OUTPUT"

          echo "[NORM] codename   = $CODENAME"
          echo "[NORM] mod        = $MOD"
          echo "[NORM] final_name = $FINAL_NAME"
          echo "[NORM] mode       = $MODE"
          echo "[NORM] rom_url    = $ROM_URL"

      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install --quiet \\
            requests pyyaml flask cryptography httpx protobuf \\
            pycryptodome toml zstandard brotli

      - name: Download source ROM (execute mode only)
        if: steps.norm.outputs.mode == 'execute'
        id: download
        run: |
          set -euo pipefail
          ROM_URL="${{ steps.norm.outputs.rom_url }}"

          if [ -z "$ROM_URL" ]; then
            echo "[ERROR] rom_url is empty in execute mode."
            exit 1
          fi

          mkdir -p _input_roms

          case "$ROM_URL" in
            *.tgz)    ROM_FILE="_input_roms/source_rom.tgz" ;;
            *.tar.gz) ROM_FILE="_input_roms/source_rom.tar.gz" ;;
            *.zip)    ROM_FILE="_input_roms/source_rom.zip" ;;
            *)        ROM_FILE="_input_roms/source_rom.zip" ;;
          esac

          echo "[DL] Downloading ROM from: $ROM_URL"
          echo "[DL] Saving to: $ROM_FILE"

          curl -L --fail --retry 5 --retry-delay 10 --connect-timeout 30 \\
            -o "$ROM_FILE" "$ROM_URL"

          if [ ! -f "$ROM_FILE" ]; then
            echo "[ERROR] ROM file not found after download."
            exit 1
          fi

          ROM_SIZE=$(stat -c%s "$ROM_FILE" 2>/dev/null || stat -f%z "$ROM_FILE")
          MIN_SIZE=$((100 * 1024 * 1024))
          echo "[DL] ROM size: $ROM_SIZE bytes"
          if [ "$ROM_SIZE" -lt "$MIN_SIZE" ]; then
            echo "[ERROR] ROM file is too small (${ROM_SIZE} bytes < 100MB). Download may have failed."
            exit 1
          fi
          echo "[DL] ROM download validated OK."
          echo "rom_path=$ROM_FILE" >> "$GITHUB_OUTPUT"

      - name: Run factory pipeline (MTK local — execute)
        if: steps.norm.outputs.mode == 'execute'
        env:
          PIXELDRAIN_API_KEY: ${{ secrets.PIXELDRAIN_API_KEY }}
          TELEGRAM_MTK_BOT_TOKEN: ${{ secrets.TELEGRAM_MTK_BOT_TOKEN }}
          TELEGRAM_MTK_CHAT_ID: ${{ secrets.TELEGRAM_MTK_CHAT_ID }}
          TELEGRAM_THREAD_ID: ${{ secrets.TELEGRAM_THREAD_ID }}
        run: |
          set -euo pipefail
          EXTRA_FLAGS=""
          if [ "${{ steps.norm.outputs.upload_pixeldrain }}" = "true" ]; then
            EXTRA_FLAGS="$EXTRA_FLAGS --upload-pixeldrain"
          fi
          if [ "${{ steps.norm.outputs.notify_telegram }}" = "true" ]; then
            EXTRA_FLAGS="$EXTRA_FLAGS --notify-telegram"
          fi

          python -m factory.pipeline.orchestrator \\
            --soc mtk \\
            --codename "${{ steps.norm.outputs.codename }}" \\
            --edition  "${{ steps.norm.outputs.mod }}" \\
            --rom      "${{ steps.download.outputs.rom_path }}" \\
            --rom-url  "${{ steps.norm.outputs.rom_url }}" \\
            --mode     execute \\
            $EXTRA_FLAGS || {
              echo "[FAIL] Factory exited non-zero. Dumping logs:"
              [ -f output/reports/deadzone_patch_report.txt ] && \\
                cat output/reports/deadzone_patch_report.txt || true
              [ -f output/reports/pipeline_report.json ] && \\
                cat output/reports/pipeline_report.json || true
              for LOG in output/logs/*.log; do
                [ -f "$LOG" ] && { echo "=== $LOG ==="; tail -100 "$LOG"; } || true
              done
              exit 1
            }

      - name: Run factory pipeline (MTK local — dry_run)
        if: steps.norm.outputs.mode != 'execute'
        env:
          TELEGRAM_MTK_BOT_TOKEN: ${{ secrets.TELEGRAM_MTK_BOT_TOKEN }}
          TELEGRAM_MTK_CHAT_ID: ${{ secrets.TELEGRAM_MTK_CHAT_ID }}
          TELEGRAM_THREAD_ID: ${{ secrets.TELEGRAM_THREAD_ID }}
        run: |
          set -euo pipefail
          EXTRA_FLAGS=""
          if [ "${{ steps.norm.outputs.notify_telegram }}" = "true" ]; then
            EXTRA_FLAGS="$EXTRA_FLAGS --notify-telegram"
          fi

          python -m factory.pipeline.orchestrator \\
            --soc mtk \\
            --codename "${{ steps.norm.outputs.codename }}" \\
            --edition  "${{ steps.norm.outputs.mod }}" \\
            --rom-url  "${{ steps.norm.outputs.rom_url }}" \\
            --mode     dry_run \\
            $EXTRA_FLAGS || {
              echo "[FAIL] Factory exited non-zero. Dumping logs:"
              [ -f output/reports/deadzone_patch_report.txt ] && \\
                cat output/reports/deadzone_patch_report.txt || true
              [ -f output/reports/pipeline_report.json ] && \\
                cat output/reports/pipeline_report.json || true
              for LOG in output/logs/*.log; do
                [ -f "$LOG" ] && { echo "=== $LOG ==="; tail -100 "$LOG"; } || true
              done
              exit 1
            }

      - name: Upload build reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: build-report-mtk-${{ steps.norm.outputs.codename }}-${{ github.run_number }}
          path: |
            output/reports/**
            output/logs/**
          if-no-files-found: ignore
"""

# ===========================================================================
# 2. deadzone_snapdragon.yml — GitHub local build, Snapdragon
# ===========================================================================
SNAP_LOCAL = """\
name: DeadZone Snapdragon GitHub Build

on:
  workflow_dispatch:
    inputs:
      codename:
        description: "Device codename, e.g. zircon, garnet"
        required: true
        type: string

      custom_codename:
        description: "Optional override codename"
        required: false
        type: string

      edition:
        description: "ROM edition"
        required: true
        type: choice
        default: legend
        options:
          - free
          - gaming
          - legend
          - epic

      rom_url:
        description: "ROM download URL (leave as auto to use device default)"
        required: false
        default: "auto"
        type: string

      mode:
        description: "Build mode"
        required: true
        type: choice
        default: execute
        options:
          - dry_run
          - execute

      upload_pixeldrain:
        description: "Upload final ROM ZIP to PixelDrain"
        required: true
        type: boolean
        default: true

      notify_telegram:
        description: "Send Telegram live updates"
        required: true
        type: boolean
        default: true

jobs:
  build:
    name: "Snapdragon | ${{ inputs.custom_codename || inputs.codename }} | ${{ inputs.edition }} | ${{ inputs.mode }}"
    runs-on: ubuntu-latest
    timeout-minutes: 180

    steps:
      - name: Validate inputs
        run: |
          set -euo pipefail

          CODENAME="${{ inputs.custom_codename }}"
          [ -z "$CODENAME" ] && CODENAME="${{ inputs.codename }}"
          CODENAME="$(echo "$CODENAME" | xargs)"

          if [ -z "$CODENAME" ]; then
            echo "[ERROR] codename is required. Please enter a real codename like zircon or garnet."
            exit 1
          fi

          for BAD in select_device_codename select_device device none null default; do
            if [ "$CODENAME" = "$BAD" ]; then
              echo "[ERROR] Invalid device codename: $CODENAME."
              echo "[ERROR] Please enter a real codename like zircon or garnet."
              exit 1
            fi
          done

          EDITION="${{ inputs.edition }}"
          case "$EDITION" in
            free|gaming|legend|epic) ;;
            *) echo "[ERROR] Invalid edition: $EDITION. Must be one of: free, gaming, legend, epic."; exit 1 ;;
          esac

          MODE="${{ inputs.mode }}"
          case "$MODE" in
            dry_run|execute) ;;
            *) echo "[ERROR] Invalid mode: $MODE. Must be dry_run or execute."; exit 1 ;;
          esac

          ROM_URL="${{ inputs.rom_url }}"
          if [ "$ROM_URL" = "auto" ]; then
            ROM_URL=""
          fi
          if [ "$MODE" = "execute" ]; then
            if [ -z "$ROM_URL" ]; then
              echo "[ERROR] rom_url is required for execute mode."
              exit 1
            fi
            case "$ROM_URL" in
              http://*|https://*) ;;
              *) echo "[ERROR] rom_url must start with http:// or https://"; exit 1 ;;
            esac
          fi

          echo "[OK] codename  = $CODENAME"
          echo "[OK] edition   = $EDITION"
          echo "[OK] mode      = $MODE"
          echo "[OK] rom_url   = $ROM_URL"
          echo "[OK] Inputs validated."

      - name: Normalize inputs
        id: norm
        run: |
          set -euo pipefail

          CODENAME="${{ inputs.custom_codename }}"
          [ -z "$CODENAME" ] && CODENAME="${{ inputs.codename }}"
          CODENAME="$(echo "$CODENAME" | xargs)"

          EDITION="${{ inputs.edition }}"
          case "$EDITION" in
            free) MOD="free" ;;
            gaming) MOD="gaming" ;;
            legend) MOD="legend" ;;
            epic) MOD="epic" ;;
            *) MOD="free" ;;
          esac

          if [ "$MOD" = "free" ]; then
            FINAL_NAME="DeadZone_${CODENAME}_V1"
          else
            FINAL_NAME="DeadZone_${CODENAME}_${MOD}_V1"
          fi

          MODE="${{ inputs.mode }}"
          ROM_URL="${{ inputs.rom_url }}"
          if [ "$ROM_URL" = "auto" ]; then
            ROM_URL=""
          fi
          UPLOAD_PD="${{ inputs.upload_pixeldrain }}"
          NOTIFY_TG="${{ inputs.notify_telegram }}"

          echo "codename=$CODENAME"           >> "$GITHUB_OUTPUT"
          echo "mod=$MOD"                     >> "$GITHUB_OUTPUT"
          echo "final_name=$FINAL_NAME"       >> "$GITHUB_OUTPUT"
          echo "mode=$MODE"                   >> "$GITHUB_OUTPUT"
          echo "rom_url=$ROM_URL"             >> "$GITHUB_OUTPUT"
          echo "upload_pixeldrain=$UPLOAD_PD" >> "$GITHUB_OUTPUT"
          echo "notify_telegram=$NOTIFY_TG"   >> "$GITHUB_OUTPUT"

          echo "[NORM] codename   = $CODENAME"
          echo "[NORM] mod        = $MOD"
          echo "[NORM] final_name = $FINAL_NAME"
          echo "[NORM] mode       = $MODE"
          echo "[NORM] rom_url    = $ROM_URL"

      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install --quiet \\
            requests pyyaml flask cryptography httpx protobuf \\
            pycryptodome toml zstandard brotli

      - name: Download source ROM (execute mode only)
        if: steps.norm.outputs.mode == 'execute'
        id: download
        run: |
          set -euo pipefail
          ROM_URL="${{ steps.norm.outputs.rom_url }}"

          if [ -z "$ROM_URL" ]; then
            echo "[ERROR] rom_url is empty in execute mode."
            exit 1
          fi

          mkdir -p _input_roms

          case "$ROM_URL" in
            *.tgz)    ROM_FILE="_input_roms/source_rom.tgz" ;;
            *.tar.gz) ROM_FILE="_input_roms/source_rom.tar.gz" ;;
            *.zip)    ROM_FILE="_input_roms/source_rom.zip" ;;
            *)        ROM_FILE="_input_roms/source_rom.zip" ;;
          esac

          echo "[DL] Downloading ROM from: $ROM_URL"
          echo "[DL] Saving to: $ROM_FILE"

          curl -L --fail --retry 5 --retry-delay 10 --connect-timeout 30 \\
            -o "$ROM_FILE" "$ROM_URL"

          if [ ! -f "$ROM_FILE" ]; then
            echo "[ERROR] ROM file not found after download."
            exit 1
          fi

          ROM_SIZE=$(stat -c%s "$ROM_FILE" 2>/dev/null || stat -f%z "$ROM_FILE")
          MIN_SIZE=$((100 * 1024 * 1024))
          echo "[DL] ROM size: $ROM_SIZE bytes"
          if [ "$ROM_SIZE" -lt "$MIN_SIZE" ]; then
            echo "[ERROR] ROM file is too small (${ROM_SIZE} bytes < 100MB). Download may have failed."
            exit 1
          fi
          echo "[DL] ROM download validated OK."
          echo "rom_path=$ROM_FILE" >> "$GITHUB_OUTPUT"

      - name: Run factory pipeline (Snapdragon local — execute)
        if: steps.norm.outputs.mode == 'execute'
        env:
          PIXELDRAIN_API_KEY: ${{ secrets.PIXELDRAIN_API_KEY }}
          TELEGRAM_SNAPDRAGON_BOT_TOKEN: ${{ secrets.TELEGRAM_SNAPDRAGON_BOT_TOKEN }}
          TELEGRAM_SNAPDRAGON_CHAT_ID: ${{ secrets.TELEGRAM_SNAPDRAGON_CHAT_ID }}
          TELEGRAM_THREAD_ID: ${{ secrets.TELEGRAM_THREAD_ID }}
        run: |
          set -euo pipefail
          EXTRA_FLAGS=""
          if [ "${{ steps.norm.outputs.upload_pixeldrain }}" = "true" ]; then
            EXTRA_FLAGS="$EXTRA_FLAGS --upload-pixeldrain"
          fi
          if [ "${{ steps.norm.outputs.notify_telegram }}" = "true" ]; then
            EXTRA_FLAGS="$EXTRA_FLAGS --notify-telegram"
          fi

          python -m factory.pipeline.orchestrator \\
            --soc snapdragon \\
            --codename "${{ steps.norm.outputs.codename }}" \\
            --edition  "${{ steps.norm.outputs.mod }}" \\
            --rom      "${{ steps.download.outputs.rom_path }}" \\
            --rom-url  "${{ steps.norm.outputs.rom_url }}" \\
            --mode     execute \\
            $EXTRA_FLAGS || {
              echo "[FAIL] Factory exited non-zero. Dumping logs:"
              [ -f output/reports/deadzone_patch_report.txt ] && \\
                cat output/reports/deadzone_patch_report.txt || true
              [ -f output/reports/pipeline_report.json ] && \\
                cat output/reports/pipeline_report.json || true
              for LOG in output/logs/*.log; do
                [ -f "$LOG" ] && { echo "=== $LOG ==="; tail -100 "$LOG"; } || true
              done
              exit 1
            }

      - name: Run factory pipeline (Snapdragon local — dry_run)
        if: steps.norm.outputs.mode != 'execute'
        env:
          TELEGRAM_SNAPDRAGON_BOT_TOKEN: ${{ secrets.TELEGRAM_SNAPDRAGON_BOT_TOKEN }}
          TELEGRAM_SNAPDRAGON_CHAT_ID: ${{ secrets.TELEGRAM_SNAPDRAGON_CHAT_ID }}
          TELEGRAM_THREAD_ID: ${{ secrets.TELEGRAM_THREAD_ID }}
        run: |
          set -euo pipefail
          EXTRA_FLAGS=""
          if [ "${{ steps.norm.outputs.notify_telegram }}" = "true" ]; then
            EXTRA_FLAGS="$EXTRA_FLAGS --notify-telegram"
          fi

          python -m factory.pipeline.orchestrator \\
            --soc snapdragon \\
            --codename "${{ steps.norm.outputs.codename }}" \\
            --edition  "${{ steps.norm.outputs.mod }}" \\
            --rom-url  "${{ steps.norm.outputs.rom_url }}" \\
            --mode     dry_run \\
            $EXTRA_FLAGS || {
              echo "[FAIL] Factory exited non-zero. Dumping logs:"
              [ -f output/reports/deadzone_patch_report.txt ] && \\
                cat output/reports/deadzone_patch_report.txt || true
              [ -f output/reports/pipeline_report.json ] && \\
                cat output/reports/pipeline_report.json || true
              for LOG in output/logs/*.log; do
                [ -f "$LOG" ] && { echo "=== $LOG ==="; tail -100 "$LOG"; } || true
              done
              exit 1
            }

      - name: Upload build reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: build-report-snap-${{ steps.norm.outputs.codename }}-${{ github.run_number }}
          path: |
            output/reports/**
            output/logs/**
          if-no-files-found: ignore
"""

# ===========================================================================
# 3. deadzone_mtk_fly.yml — Fly API dispatch, MTK
# ===========================================================================
MTK_FLY = """\
name: DeadZone MTK Fly Build

on:
  workflow_dispatch:
    inputs:
      codename:
        description: "Device codename, e.g. zircon, garnet"
        required: true
        type: string

      custom_codename:
        description: "Optional override codename"
        required: false
        type: string

      edition:
        description: "ROM edition"
        required: true
        type: choice
        default: legend
        options:
          - free
          - gaming
          - legend
          - epic

      rom_url:
        description: "ROM download URL (leave as auto to use device default)"
        required: false
        default: "auto"
        type: string

      mode:
        description: "Build mode"
        required: true
        type: choice
        default: execute
        options:
          - dry_run
          - execute

      upload_pixeldrain:
        description: "Upload final ROM ZIP to PixelDrain"
        required: true
        type: boolean
        default: true

      notify_telegram:
        description: "Send Telegram live updates"
        required: true
        type: boolean
        default: true

jobs:
  trigger-fly:
    name: "MTK Fly | ${{ inputs.custom_codename || inputs.codename }} | ${{ inputs.edition }} | ${{ inputs.mode }}"
    runs-on: ubuntu-latest
    timeout-minutes: 10

    outputs:
      build_id: ${{ steps.post.outputs.build_id }}
      job_id: ${{ steps.post.outputs.job_id }}
      telegram_message_id: ${{ steps.post.outputs.telegram_message_id }}

    steps:
      - name: Validate inputs
        run: |
          set -euo pipefail

          CODENAME="${{ inputs.custom_codename }}"
          [ -z "$CODENAME" ] && CODENAME="${{ inputs.codename }}"
          CODENAME="$(echo "$CODENAME" | xargs)"

          if [ -z "$CODENAME" ]; then
            echo "[ERROR] codename is required. Please enter a real codename like zircon or garnet."
            exit 1
          fi

          for BAD in select_device_codename select_device device none null default; do
            if [ "$CODENAME" = "$BAD" ]; then
              echo "[ERROR] Invalid device codename: $CODENAME."
              echo "[ERROR] Please enter a real codename like zircon or garnet."
              exit 1
            fi
          done

          EDITION="${{ inputs.edition }}"
          case "$EDITION" in
            free|gaming|legend|epic) ;;
            *) echo "[ERROR] Invalid edition: $EDITION. Must be one of: free, gaming, legend, epic."; exit 1 ;;
          esac

          MODE="${{ inputs.mode }}"
          case "$MODE" in
            dry_run|execute) ;;
            *) echo "[ERROR] Invalid mode: $MODE. Must be dry_run or execute."; exit 1 ;;
          esac

          ROM_URL="${{ inputs.rom_url }}"
          if [ "$ROM_URL" = "auto" ]; then
            ROM_URL=""
          fi
          if [ "$MODE" = "execute" ]; then
            if [ -z "$ROM_URL" ]; then
              echo "[ERROR] rom_url is required for execute mode."
              exit 1
            fi
            case "$ROM_URL" in
              http://*|https://*) ;;
              *) echo "[ERROR] rom_url must start with http:// or https://"; exit 1 ;;
            esac
          fi

          echo "[OK] codename  = $CODENAME"
          echo "[OK] edition   = $EDITION"
          echo "[OK] mode      = $MODE"
          echo "[OK] rom_url   = $ROM_URL"
          echo "[OK] Inputs validated."

      - name: Normalize inputs
        id: norm
        run: |
          set -euo pipefail

          CODENAME="${{ inputs.custom_codename }}"
          [ -z "$CODENAME" ] && CODENAME="${{ inputs.codename }}"
          CODENAME="$(echo "$CODENAME" | xargs)"

          EDITION="${{ inputs.edition }}"
          case "$EDITION" in
            free) MOD="free" ;;
            gaming) MOD="gaming" ;;
            legend) MOD="legend" ;;
            epic) MOD="epic" ;;
            *) MOD="free" ;;
          esac

          if [ "$MOD" = "free" ]; then
            FINAL_NAME="DeadZone_${CODENAME}_V1"
          else
            FINAL_NAME="DeadZone_${CODENAME}_${MOD}_V1"
          fi

          MODE="${{ inputs.mode }}"
          ROM_URL="${{ inputs.rom_url }}"
          if [ "$ROM_URL" = "auto" ]; then
            ROM_URL=""
          fi
          UPLOAD_PD="${{ inputs.upload_pixeldrain }}"
          NOTIFY_TG="${{ inputs.notify_telegram }}"
          [ -z "$UPLOAD_PD" ] && UPLOAD_PD="true"
          [ -z "$NOTIFY_TG" ] && NOTIFY_TG="true"

          echo "codename=$CODENAME"           >> "$GITHUB_OUTPUT"
          echo "mod=$MOD"                     >> "$GITHUB_OUTPUT"
          echo "final_name=$FINAL_NAME"       >> "$GITHUB_OUTPUT"
          echo "mode=$MODE"                   >> "$GITHUB_OUTPUT"
          echo "rom_url=$ROM_URL"             >> "$GITHUB_OUTPUT"
          echo "upload_pixeldrain=$UPLOAD_PD" >> "$GITHUB_OUTPUT"
          echo "notify_telegram=$NOTIFY_TG"   >> "$GITHUB_OUTPUT"

          echo "[NORM] codename   = $CODENAME"
          echo "[NORM] mod        = $MOD"
          echo "[NORM] final_name = $FINAL_NAME"
          echo "[NORM] mode       = $MODE"
          echo "[NORM] rom_url    = $ROM_URL"

      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Validate repo text files
        run: |
          set -euo pipefail
          python3 scripts/validate_repo_text_files.py

      - name: Validate Fly secrets and notify on failure
        env:
          MTK_URL: ${{ secrets.MTK_FLY_BUILDER_URL }}
          FALLBACK_URL: ${{ secrets.FLY_BUILDER_URL }}
          BUILDER_TOKEN: ${{ secrets.BUILDER_TOKEN }}
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_MTK_BOT_TOKEN }}
          TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_MTK_CHAT_ID }}
        run: |
          set -euo pipefail
          BUILDER_URL="${MTK_URL:-$FALLBACK_URL}"
          MISSING=""
          [ -z "$BUILDER_URL" ]   && MISSING="${MISSING}MTK_FLY_BUILDER_URL or FLY_BUILDER_URL\\n"
          [ -z "$BUILDER_TOKEN" ] && MISSING="${MISSING}BUILDER_TOKEN\\n"

          if [ -n "$MISSING" ]; then
            echo "[ERROR] Required Fly secrets not set:"
            echo -e "$MISSING"
            echo ""
            echo "========================================================"
            echo "Required GitHub repository secrets:"
            echo ""
            echo "For MTK Fly:"
            echo "  MTK_FLY_BUILDER_URL=https://dz-builder-mtk.fly.dev"
            echo "  or FLY_BUILDER_URL=https://dz-builder-mtk.fly.dev"
            echo "  BUILDER_TOKEN=<same token configured on Fly>"
            echo ""
            echo "Telegram optional but recommended:"
            echo "  TELEGRAM_MTK_BOT_TOKEN"
            echo "  TELEGRAM_MTK_CHAT_ID"
            echo "  or: TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID"
            echo "========================================================"
            echo ""

            python3 scripts/notify_dispatch_failure.py \\
              --soc mtk \\
              --codename "${{ steps.norm.outputs.codename }}" \\
              --edition  "${{ steps.norm.outputs.mod }}" \\
              --mode     "${{ steps.norm.outputs.mode }}" \\
              --title    "DeadZone Fly Dispatch Failed" \\
              --reason   "Missing Fly secrets" \\
              --missing  "$(echo -e "$MISSING" | tr '\\n' ',' | sed 's/,$//')" \\
              --run-url  "$GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID" \\
              || true

            exit 3
          fi

          echo "[OK] Fly secrets verified. URL: $BUILDER_URL"

      - name: Health check Fly builder
        env:
          MTK_URL: ${{ secrets.MTK_FLY_BUILDER_URL }}
          FALLBACK_URL: ${{ secrets.FLY_BUILDER_URL }}
        run: |
          set -euo pipefail
          BUILDER_URL="${MTK_URL:-$FALLBACK_URL}"
          echo "[FLY] Health check: $BUILDER_URL/health"
          if ! curl -fsS \\
               --retry 5 --retry-delay 5 \\
               --connect-timeout 10 --max-time 30 \\
               "$BUILDER_URL/health"; then
            echo ""
            echo "[ERROR] Fly builder health check failed. Deploy or start dz-builder-mtk before dispatch."
            exit 1
          fi
          echo ""
          echo "[OK] Fly builder is healthy."

      - name: POST build job to Fly MTK builder
        id: post
        env:
          MTK_URL: ${{ secrets.MTK_FLY_BUILDER_URL }}
          FALLBACK_URL: ${{ secrets.FLY_BUILDER_URL }}
          BUILDER_TOKEN: ${{ secrets.BUILDER_TOKEN }}
        run: |
          set -euo pipefail
          BUILDER_URL="${MTK_URL:-$FALLBACK_URL}"
          CODENAME="${{ steps.norm.outputs.codename }}"
          MOD="${{ steps.norm.outputs.mod }}"
          MODE="${{ steps.norm.outputs.mode }}"
          ROM_URL="${{ steps.norm.outputs.rom_url }}"
          FINAL_NAME="${{ steps.norm.outputs.final_name }}"
          UPLOAD_PD="${{ steps.norm.outputs.upload_pixeldrain }}"
          NOTIFY_TG="${{ steps.norm.outputs.notify_telegram }}"

          PAYLOAD=$(python3 - <<PYEOF
          import json
          d = {
              "source":            "Fly",
              "soc":               "mtk",
              "codename":          "$CODENAME",
              "edition":           "$MOD",
              "mod":               "$MOD",
              "rom_url":           "$ROM_URL",
              "mode":              "$MODE",
              "final_name":        "$FINAL_NAME",
              "upload_pixeldrain": "$UPLOAD_PD" == "true",
              "notify_telegram":   "$NOTIFY_TG" == "true",
          }
          print(json.dumps(d))
          PYEOF
          )

          echo "[FLY] Posting to $BUILDER_URL/build"
          echo "[FLY] Codename : $CODENAME"
          echo "[FLY] Edition  : $MOD"
          echo "[FLY] Mode     : $MODE"
          echo "[FLY] ROM URL  : $ROM_URL"

          HTTP_CODE=$(curl -sS -w "%{http_code}" \\
            --retry 5 --retry-all-errors --retry-delay 10 \\
            --connect-timeout 20 --max-time 120 \\
            -o response.json \\
            -X POST "$BUILDER_URL/build" \\
            -H "Authorization: Bearer $BUILDER_TOKEN" \\
            -H "Content-Type: application/json" \\
            -d "$PAYLOAD")

          echo "[FLY] HTTP status: $HTTP_CODE"
          echo "[FLY] Response body:"
          cat response.json
          echo ""

          if [ "$HTTP_CODE" -lt 200 ] || [ "$HTTP_CODE" -ge 300 ]; then
            echo "[ERROR] Fly builder returned HTTP $HTTP_CODE — build not accepted."
            exit 3
          fi

          BUILD_ID=$(python3 -c \\
            "import json; d=json.load(open('response.json')); print(d.get('build_id',''))" \\
            2>/dev/null || echo "")
          JOB_ID=$(python3 -c \\
            "import json; d=json.load(open('response.json')); print(d.get('job_id',''))" \\
            2>/dev/null || echo "")
          TG_MSG_ID=$(python3 -c \\
            "import json; d=json.load(open('response.json')); print(d.get('telegram_message_id',''))" \\
            2>/dev/null || echo "")

          echo "[FLY] build_id            : $BUILD_ID"
          echo "[FLY] job_id              : $JOB_ID"
          echo "[FLY] telegram_message_id : $TG_MSG_ID"

          echo "build_id=$BUILD_ID"             >> "$GITHUB_OUTPUT"
          echo "job_id=$JOB_ID"                 >> "$GITHUB_OUTPUT"
          echo "telegram_message_id=$TG_MSG_ID" >> "$GITHUB_OUTPUT"
"""

# ===========================================================================
# 4. deadzone_snapdragon_fly.yml — Fly API dispatch, Snapdragon
# ===========================================================================
SNAP_FLY = """\
name: DeadZone Snapdragon Fly Build

on:
  workflow_dispatch:
    inputs:
      codename:
        description: "Device codename, e.g. zircon, garnet"
        required: true
        type: string

      custom_codename:
        description: "Optional override codename"
        required: false
        type: string

      edition:
        description: "ROM edition"
        required: true
        type: choice
        default: legend
        options:
          - free
          - gaming
          - legend
          - epic

      rom_url:
        description: "ROM download URL (leave as auto to use device default)"
        required: false
        default: "auto"
        type: string

      mode:
        description: "Build mode"
        required: true
        type: choice
        default: execute
        options:
          - dry_run
          - execute

      upload_pixeldrain:
        description: "Upload final ROM ZIP to PixelDrain"
        required: true
        type: boolean
        default: true

      notify_telegram:
        description: "Send Telegram live updates"
        required: true
        type: boolean
        default: true

jobs:
  trigger-fly:
    name: "Snapdragon Fly | ${{ inputs.custom_codename || inputs.codename }} | ${{ inputs.edition }} | ${{ inputs.mode }}"
    runs-on: ubuntu-latest
    timeout-minutes: 10

    outputs:
      build_id: ${{ steps.post.outputs.build_id }}
      job_id: ${{ steps.post.outputs.job_id }}
      telegram_message_id: ${{ steps.post.outputs.telegram_message_id }}

    steps:
      - name: Validate inputs
        run: |
          set -euo pipefail

          CODENAME="${{ inputs.custom_codename }}"
          [ -z "$CODENAME" ] && CODENAME="${{ inputs.codename }}"
          CODENAME="$(echo "$CODENAME" | xargs)"

          if [ -z "$CODENAME" ]; then
            echo "[ERROR] codename is required. Please enter a real codename like zircon or garnet."
            exit 1
          fi

          for BAD in select_device_codename select_device device none null default; do
            if [ "$CODENAME" = "$BAD" ]; then
              echo "[ERROR] Invalid device codename: $CODENAME."
              echo "[ERROR] Please enter a real codename like zircon or garnet."
              exit 1
            fi
          done

          EDITION="${{ inputs.edition }}"
          case "$EDITION" in
            free|gaming|legend|epic) ;;
            *) echo "[ERROR] Invalid edition: $EDITION. Must be one of: free, gaming, legend, epic."; exit 1 ;;
          esac

          MODE="${{ inputs.mode }}"
          case "$MODE" in
            dry_run|execute) ;;
            *) echo "[ERROR] Invalid mode: $MODE. Must be dry_run or execute."; exit 1 ;;
          esac

          ROM_URL="${{ inputs.rom_url }}"
          if [ "$ROM_URL" = "auto" ]; then
            ROM_URL=""
          fi
          if [ "$MODE" = "execute" ]; then
            if [ -z "$ROM_URL" ]; then
              echo "[ERROR] rom_url is required for execute mode."
              exit 1
            fi
            case "$ROM_URL" in
              http://*|https://*) ;;
              *) echo "[ERROR] rom_url must start with http:// or https://"; exit 1 ;;
            esac
          fi

          echo "[OK] codename  = $CODENAME"
          echo "[OK] edition   = $EDITION"
          echo "[OK] mode      = $MODE"
          echo "[OK] rom_url   = $ROM_URL"
          echo "[OK] Inputs validated."

      - name: Normalize inputs
        id: norm
        run: |
          set -euo pipefail

          CODENAME="${{ inputs.custom_codename }}"
          [ -z "$CODENAME" ] && CODENAME="${{ inputs.codename }}"
          CODENAME="$(echo "$CODENAME" | xargs)"

          EDITION="${{ inputs.edition }}"
          case "$EDITION" in
            free) MOD="free" ;;
            gaming) MOD="gaming" ;;
            legend) MOD="legend" ;;
            epic) MOD="epic" ;;
            *) MOD="free" ;;
          esac

          if [ "$MOD" = "free" ]; then
            FINAL_NAME="DeadZone_${CODENAME}_V1"
          else
            FINAL_NAME="DeadZone_${CODENAME}_${MOD}_V1"
          fi

          MODE="${{ inputs.mode }}"
          ROM_URL="${{ inputs.rom_url }}"
          if [ "$ROM_URL" = "auto" ]; then
            ROM_URL=""
          fi
          UPLOAD_PD="${{ inputs.upload_pixeldrain }}"
          NOTIFY_TG="${{ inputs.notify_telegram }}"
          [ -z "$UPLOAD_PD" ] && UPLOAD_PD="true"
          [ -z "$NOTIFY_TG" ] && NOTIFY_TG="true"

          echo "codename=$CODENAME"           >> "$GITHUB_OUTPUT"
          echo "mod=$MOD"                     >> "$GITHUB_OUTPUT"
          echo "final_name=$FINAL_NAME"       >> "$GITHUB_OUTPUT"
          echo "mode=$MODE"                   >> "$GITHUB_OUTPUT"
          echo "rom_url=$ROM_URL"             >> "$GITHUB_OUTPUT"
          echo "upload_pixeldrain=$UPLOAD_PD" >> "$GITHUB_OUTPUT"
          echo "notify_telegram=$NOTIFY_TG"   >> "$GITHUB_OUTPUT"

          echo "[NORM] codename   = $CODENAME"
          echo "[NORM] mod        = $MOD"
          echo "[NORM] final_name = $FINAL_NAME"
          echo "[NORM] mode       = $MODE"
          echo "[NORM] rom_url    = $ROM_URL"

      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Validate repo text files
        run: |
          set -euo pipefail
          python3 scripts/validate_repo_text_files.py

      - name: Validate Fly secrets and notify on failure
        env:
          SNAP_URL: ${{ secrets.SNAPDRAGON_FLY_BUILDER_URL }}
          FALLBACK_URL: ${{ secrets.FLY_BUILDER_URL }}
          BUILDER_TOKEN: ${{ secrets.BUILDER_TOKEN }}
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_SNAPDRAGON_BOT_TOKEN }}
          TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_SNAPDRAGON_CHAT_ID }}
        run: |
          set -euo pipefail
          BUILDER_URL="${SNAP_URL:-$FALLBACK_URL}"
          MISSING=""
          [ -z "$BUILDER_URL" ]   && MISSING="${MISSING}SNAPDRAGON_FLY_BUILDER_URL or FLY_BUILDER_URL\\n"
          [ -z "$BUILDER_TOKEN" ] && MISSING="${MISSING}BUILDER_TOKEN\\n"

          if [ -n "$MISSING" ]; then
            echo "[ERROR] Required Fly secrets not set:"
            echo -e "$MISSING"
            echo ""
            echo "========================================================"
            echo "Required GitHub repository secrets:"
            echo ""
            echo "For Snapdragon Fly:"
            echo "  SNAPDRAGON_FLY_BUILDER_URL=https://dz-builder-snapdragon.fly.dev"
            echo "  or FLY_BUILDER_URL=https://dz-builder-snapdragon.fly.dev"
            echo "  BUILDER_TOKEN=<same token configured on Fly>"
            echo ""
            echo "Telegram optional but recommended:"
            echo "  TELEGRAM_SNAPDRAGON_BOT_TOKEN"
            echo "  TELEGRAM_SNAPDRAGON_CHAT_ID"
            echo "  or: TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID"
            echo "========================================================"
            echo ""

            python3 scripts/notify_dispatch_failure.py \\
              --soc snapdragon \\
              --codename "${{ steps.norm.outputs.codename }}" \\
              --edition  "${{ steps.norm.outputs.mod }}" \\
              --mode     "${{ steps.norm.outputs.mode }}" \\
              --title    "DeadZone Fly Dispatch Failed" \\
              --reason   "Missing Fly secrets" \\
              --missing  "$(echo -e "$MISSING" | tr '\\n' ',' | sed 's/,$//')" \\
              --run-url  "$GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID" \\
              || true

            exit 3
          fi

          echo "[OK] Fly secrets verified. URL: $BUILDER_URL"

      - name: Health check Fly builder
        env:
          SNAP_URL: ${{ secrets.SNAPDRAGON_FLY_BUILDER_URL }}
          FALLBACK_URL: ${{ secrets.FLY_BUILDER_URL }}
        run: |
          set -euo pipefail
          BUILDER_URL="${SNAP_URL:-$FALLBACK_URL}"
          echo "[FLY] Health check: $BUILDER_URL/health"
          if ! curl -fsS \\
               --retry 5 --retry-delay 5 \\
               --connect-timeout 10 --max-time 30 \\
               "$BUILDER_URL/health"; then
            echo ""
            echo "[ERROR] Fly builder health check failed. Deploy or start dz-builder-snap before dispatch."
            exit 1
          fi
          echo ""
          echo "[OK] Fly builder is healthy."

      - name: POST build job to Fly Snapdragon builder
        id: post
        env:
          SNAP_URL: ${{ secrets.SNAPDRAGON_FLY_BUILDER_URL }}
          FALLBACK_URL: ${{ secrets.FLY_BUILDER_URL }}
          BUILDER_TOKEN: ${{ secrets.BUILDER_TOKEN }}
        run: |
          set -euo pipefail
          BUILDER_URL="${SNAP_URL:-$FALLBACK_URL}"
          CODENAME="${{ steps.norm.outputs.codename }}"
          MOD="${{ steps.norm.outputs.mod }}"
          MODE="${{ steps.norm.outputs.mode }}"
          ROM_URL="${{ steps.norm.outputs.rom_url }}"
          FINAL_NAME="${{ steps.norm.outputs.final_name }}"
          UPLOAD_PD="${{ steps.norm.outputs.upload_pixeldrain }}"
          NOTIFY_TG="${{ steps.norm.outputs.notify_telegram }}"

          PAYLOAD=$(python3 - <<PYEOF
          import json
          d = {
              "source":            "Fly",
              "soc":               "snapdragon",
              "codename":          "$CODENAME",
              "edition":           "$MOD",
              "mod":               "$MOD",
              "rom_url":           "$ROM_URL",
              "mode":              "$MODE",
              "final_name":        "$FINAL_NAME",
              "upload_pixeldrain": "$UPLOAD_PD" == "true",
              "notify_telegram":   "$NOTIFY_TG" == "true",
          }
          print(json.dumps(d))
          PYEOF
          )

          echo "[FLY] Posting to $BUILDER_URL/build"
          echo "[FLY] Codename : $CODENAME"
          echo "[FLY] Edition  : $MOD"
          echo "[FLY] Mode     : $MODE"
          echo "[FLY] ROM URL  : $ROM_URL"

          HTTP_CODE=$(curl -sS -w "%{http_code}" \\
            --retry 5 --retry-all-errors --retry-delay 10 \\
            --connect-timeout 20 --max-time 120 \\
            -o response.json \\
            -X POST "$BUILDER_URL/build" \\
            -H "Authorization: Bearer $BUILDER_TOKEN" \\
            -H "Content-Type: application/json" \\
            -d "$PAYLOAD")

          echo "[FLY] HTTP status: $HTTP_CODE"
          echo "[FLY] Response body:"
          cat response.json
          echo ""

          if [ "$HTTP_CODE" -lt 200 ] || [ "$HTTP_CODE" -ge 300 ]; then
            echo "[ERROR] Fly builder returned HTTP $HTTP_CODE — build not accepted."
            exit 3
          fi

          BUILD_ID=$(python3 -c \\
            "import json; d=json.load(open('response.json')); print(d.get('build_id',''))" \\
            2>/dev/null || echo "")
          JOB_ID=$(python3 -c \\
            "import json; d=json.load(open('response.json')); print(d.get('job_id',''))" \\
            2>/dev/null || echo "")
          TG_MSG_ID=$(python3 -c \\
            "import json; d=json.load(open('response.json')); print(d.get('telegram_message_id',''))" \\
            2>/dev/null || echo "")

          echo "[FLY] build_id            : $BUILD_ID"
          echo "[FLY] job_id              : $JOB_ID"
          echo "[FLY] telegram_message_id : $TG_MSG_ID"

          echo "build_id=$BUILD_ID"             >> "$GITHUB_OUTPUT"
          echo "job_id=$JOB_ID"                 >> "$GITHUB_OUTPUT"
          echo "telegram_message_id=$TG_MSG_ID" >> "$GITHUB_OUTPUT"
"""

# ===========================================================================
# 5. deploy_fly_builder.yml — deploy Fly builder app
# ===========================================================================
DEPLOY_FLY = """\
name: Deploy DeadZone Fly Builder

on:
  workflow_dispatch:
    inputs:
      target_app:
        description: "Fly app to deploy"
        required: true
        type: choice
        default: dz-builder-mtk
        options:
          - dz-builder-mtk
          - dz-builder-snap

  push:
    branches:
      - main
    paths:
      - "server/**"
      - "factory/**"
      - "docker/Dockerfile.builder"
      - "fly.toml"
      - "requirements.txt"

jobs:
  deploy:
    name: "Deploy ${{ inputs.target_app || 'dz-builder-mtk' }} to Fly.io"
    runs-on: ubuntu-latest
    timeout-minutes: 30

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup flyctl
        uses: superfly/flyctl-actions/setup-flyctl@master

      - name: Deploy to Fly
        run: |
          set -euo pipefail
          APP="${{ inputs.target_app || 'dz-builder-mtk' }}"
          echo "[DEPLOY] Deploying app: $APP"
          flyctl deploy --app "$APP" --remote-only
        env:
          FLY_API_TOKEN: ${{ secrets.FLY_API_TOKEN }}
"""

# ---------------------------------------------------------------------------
# Write all files
# ---------------------------------------------------------------------------
FILES = [
    ("deadzone_mtk.yml",            MTK_LOCAL),
    ("deadzone_snapdragon.yml",      SNAP_LOCAL),
    ("deadzone_mtk_fly.yml",         MTK_FLY),
    ("deadzone_snapdragon_fly.yml",  SNAP_FLY),
    ("deploy_fly_builder.yml",       DEPLOY_FLY),
]

print("Rebuilding workflow files...")
for name, content in FILES:
    _w(name, content)

print("\nDone. All workflow files rebuilt with fresh LF-only YAML content.")
