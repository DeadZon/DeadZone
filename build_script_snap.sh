#!/bin/bash
set -e

# ==========================================
# DeadZone Snapdragon Cloud Builder (Fly.io)
# ==========================================

export SOC="snapdragon"
export DZ_FACTORY_NAME="DeadZone Snapdragon Factory"
export DZ_MODE="${IN_MODE}"
export DZ_NOTIFY="${IN_NOTIFY}"
export DZ_BUILD="${IN_FINAL_NAME}"
export DZ_DEVICE="${IN_CUSTOM_DEVICE:-$IN_DEVICE}"

cd /mnt/dz_data

# Create 48GB Swap just to ensure smooth packing/unpacking of huge system images
if [ ! -f "/mnt/dz_data/swapfile" ]; then
    fallocate -l 48G /mnt/dz_data/swapfile || dd if=/dev/zero of=/mnt/dz_data/swapfile bs=1M count=49152
    chmod 600 /mnt/dz_data/swapfile
    mkswap /mnt/dz_data/swapfile
fi
swapon /mnt/dz_data/swapfile || true

# Clone your private/public factory repository securely
rm -rf DeadZone
git clone https://oauth2:${GITHUB_TOKEN}@github.com/DeadZon/DeadZone.git
cd DeadZone

# Install Python requirements
python -m pip install --upgrade pip wheel --break-system-packages
python -m pip install -r requirements.txt --break-system-packages

# ==========================================
# 1. Generate Telegram Live Helper Script
# ==========================================
cat > _dz_tg.py << 'PYEOF'
import json, os, sys, urllib.error, urllib.request

_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
_CHAT = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
_THREAD = os.environ.get("TELEGRAM_THREAD_ID", "").strip()
_NOTIFY = os.environ.get("DZ_NOTIFY", "true").strip().lower()
_FACTORY = os.environ.get("DZ_FACTORY_NAME", "DeadZone Factory")
_MODE = os.environ.get("DZ_MODE", "")

def _usable():
    return _NOTIFY in ("true", "1", "yes") and bool(_TOKEN and _CHAT)

def _post(method, payload):
    url = f"https://api.telegram.org/bot{_TOKEN}/{method}"
    data = json.dumps(payload, ensure_ascii=True).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        if "message is not modified" in body.lower(): return {"ok": True}
        return {"ok": False}
    except Exception:
        return {"ok": False}

def _make_text(status, current="", extra=""):
    build = os.environ.get("FINAL_NAME") or os.environ.get("DZ_BUILD", "")
    device = (os.environ.get("EFFECTIVE_DEVICE") or os.environ.get("DZ_DEVICE", "")).split(" | ")[0].strip()
    mode = os.environ.get("DZ_MODE", _MODE)
    lines = [_FACTORY, f"Build: {build}", f"Device: {device}", f"Mode: {mode}", f"Status: {status}"]
    if current: lines.append(f"Current: {current}")
    if extra: lines.append(extra)
    return "\n".join(lines)

def do_send(text):
    if not _usable(): return
    payload = {"chat_id": _CHAT, "text": text}
    if _THREAD: payload["message_thread_id"] = int(_THREAD)
    resp = _post("sendMessage", payload)
    if resp.get("ok"):
        mid = resp.get("result", {}).get("message_id")
        with open("/tmp/tg_msg_id", "w") as fh: fh.write(str(mid))

def do_edit(text):
    if not _usable(): return
    try:
        with open("/tmp/tg_msg_id", "r") as fh: mid = fh.read().strip()
    except: return
    if not mid: return
    payload = {"chat_id": _CHAT, "message_id": int(mid), "text": text}
    if _THREAD: payload["message_thread_id"] = int(_THREAD)
    _post("editMessageText", payload)

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(0)
    action, status = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "UNKNOWN"
    current = sys.argv[3] if len(sys.argv) > 3 else ""
    extra = sys.argv[4] if len(sys.argv) > 4 else ""
    text = _make_text(status, current, extra)
    if action == "send": do_send(text)
    elif action == "edit": do_edit(text)
PYEOF

python _dz_tg.py send STARTING "Preparing runner on 400GB Cloud" || true

# ==========================================
# 2. Fastboot Template & Registry Validation
# ==========================================
python _dz_tg.py edit VALIDATING_TEMPLATE "Checking fastboot template" || true
TEMPLATE="third_party/mezo_core/templates/deadzone_fastboot"
MISSING=0
for f in bin/windows/fastboot.exe bin/windows/AdbWinApi.dll bin/windows/AdbWinUsbApi.dll; do
  if [ ! -f "$TEMPLATE/$f" ]; then MISSING=1; fi
done
if [ "$MISSING" = "1" ]; then
  python _dz_tg.py edit FAILED "Fastboot template files missing" || true
  exit 1
fi

python _dz_tg.py edit VALIDATING_INPUTS "Validating device registry" || true
python -m factory.cli validate-registry

# ==========================================
# 3. Resolve Inputs (Flavor & Device)
# ==========================================
if [ -n "$IN_CUSTOM_DEVICE" ] && [ "$IN_CUSTOM_DEVICE" != "select_device_codename" ]; then
  export EFFECTIVE_DEVICE="$IN_CUSTOM_DEVICE"
else
  export EFFECTIVE_DEVICE="${IN_DEVICE%% | *}"
fi

case "${IN_FLAVOR}" in
  base)   export FLAVOR="deadzone" ;;
  gaming) export FLAVOR="deadzone_gaming" ;;
  epic)   export FLAVOR="deadzone_epic" ;;
  legend) export FLAVOR="deadzone_legend" ;;
  *)      export FLAVOR="${IN_FLAVOR}" ;;
esac
export FINAL_NAME="${IN_FINAL_NAME}"
python _dz_tg.py edit VALIDATING_INPUTS "Inputs resolved: device=$EFFECTIVE_DEVICE" || true

# ==========================================
# 4. Prepare MEZO Core Requirements
# ==========================================
if [ "$DZ_MODE" == "execute" ]; then
  cat > fix_mezo.py <<'PYEOF'
from pathlib import Path
src = Path("third_party/mezo_core/requirements.txt")
dst = Path("third_party/mezo_core/.requirements.ci.txt")
if not src.is_file():
    src.write_text("cryptography>=42.0.0\nhttpx>=0.27.0\nprotobuf>=4.25.0\npycryptodome>=3.19.0\nrequests>=2.31.0\ntoml>=0.10.2\nzstandard>=0.22.0\nbrotli>=1.1.0\n", encoding="utf-8")
lines = src.read_text(encoding="utf-8-sig", errors="ignore").splitlines()
cleaned = [line.strip() for line in lines if line.strip() and not line.strip().startswith("#") and not line.lower().startswith("lzma") and not line.lower().startswith("google")]
if not any(l.lower().startswith("brotli") for l in cleaned): cleaned.append("brotli>=1.1.0")
dst.write_text("\n".join(cleaned) + "\n", encoding="utf-8")
PYEOF
  python fix_mezo.py
  python -m pip install -r third_party/mezo_core/.requirements.ci.txt --break-system-packages
  
  cd third_party/mezo_core
  find bin -type f -exec chmod +x {} \; || true
  python -m py_compile MEZOBuildRom.py
  mkdir -p MEZO_APP/product MEZO_APP/system MEZO_APP/appMod MEZO_APP/OS3_A16 MEZO_APP/OS3_A15 MEZO_APP/OS2_A15 MEZO_APP/OS2_A14 MEZO_APP/OS1_A14
  cd ../..
fi

# ==========================================
# 5. Download ROM
# ==========================================
python _dz_tg.py edit DOWNLOADING_ROM "Downloading ROM to 400GB SSD" || true
mkdir -p _input_roms
cat > down_rom.py << 'PYEOF'
import urllib.parse, urllib.request, os
from pathlib import Path
url = os.environ.get("IN_ROM_URL")
parsed_name = Path(urllib.parse.urlparse(url).path).name
name = urllib.parse.unquote(parsed_name) if parsed_name else "input_rom.zip"
out = Path("_input_roms") / name
req = urllib.request.Request(url, headers={"User-Agent": "DeadZoneFactory/1.0"})
with urllib.request.urlopen(req, timeout=1800) as resp:
    with out.open("wb") as f:
        while True:
            chunk = resp.read(1024 * 1024)
            if not chunk: break
            f.write(chunk)
PYEOF
python down_rom.py
python _dz_tg.py edit ROM_DOWNLOADED "ROM download complete" || true

# ==========================================
# 6. Device Guard & Pipeline Execution
# ==========================================
ROM_FILE="$(find _input_roms -type f | head -n 1)"
TELEGRAM_FLAG=""
if [ "$DZ_NOTIFY" = "true" ]; then TELEGRAM_FLAG="--telegram"; fi

if [ "$DZ_MODE" == "dry_run" ]; then
  python _dz_tg.py edit RUNNING_PIPELINE "Running dry-run pipeline" || true
  python -m factory.pipeline.legacy_build_orchestrator \
    --rom "$ROM_FILE" --output-dir output --build-name "$FINAL_NAME" \
    --device "$EFFECTIVE_DEVICE" --soc "$SOC" --platform "$IN_PLATFORM" \
    --flavor "$FLAVOR" --android-version "$IN_ANDROID_VERSION" \
    --mi-version "$IN_MI_VERSION" --vbmeta-mode "$IN_VBMETA_MODE" \
    --template-zip third_party/mezo_core/templates/deadzone_fastboot $TELEGRAM_FLAG
else
  python _dz_tg.py edit RUNNING_PIPELINE "Running execute pipeline" || true
  python -m factory.pipeline.legacy_build_orchestrator \
    --rom "$ROM_FILE" --output-dir output --build-name "$FINAL_NAME" \
    --device "$EFFECTIVE_DEVICE" --soc "$SOC" --platform "$IN_PLATFORM" \
    --flavor "$FLAVOR" --android-version "$IN_ANDROID_VERSION" \
    --mi-version "$IN_MI_VERSION" --vbmeta-mode "$IN_VBMETA_MODE" \
    --template-zip third_party/mezo_core/templates/deadzone_fastboot \
    --execute $TELEGRAM_FLAG
fi

# ==========================================
# 7. PixelDrain Upload & Cleanup
# ==========================================
if [ "$DZ_MODE" == "execute" ]; then
  python _dz_tg.py edit UPLOADING_PIXELDRAIN "Uploading to PixelDrain" || true
  FINAL_ZIP="$(find output/final -maxdepth 1 -name '*.zip' -type f 2>/dev/null | head -n 1)"
  mkdir -p output/reports
  set +e
  python -m factory.services.pixeldrain_upload "$FINAL_ZIP"
  PD_EXIT=$?
  set -e
  if [ "$PD_EXIT" = "0" ]; then
    PD_LINK=$(cat output/reports/pixeldrain_upload.json | grep -o '"link": *"[^"]*"' | cut -d'"' -f4)
    echo "$PD_LINK" > output/reports/pixeldrain_link.txt
    python _dz_tg.py edit DONE "Done. PixelDrain: $PD_LINK" || true
  else
    python _dz_tg.py edit BUILD_OK "Build succeeded, but PixelDrain upload failed" || true
  fi
  
  # Upload reports as GitHub Release Artifacts instead of GH Actions generic artifacts
  gh release create "$GITHUB_RUN_ID" output/reports/* output/logs/* --title "DeadZone $EFFECTIVE_DEVICE | $FINAL_NAME" --notes "Build Reports for Run $GITHUB_RUN_ID" || true
fi

# Heavy cleanup to maintain the 400GB space for next builds
rm -rf _input_roms/ output/tmp output/work || true
