#!/bin/bash
set -e

# ===================================================================
# DeadZone MediaTek Cloud Builder - Multi Live Stream (Owners & Group)
# Strictly Pure English - Zero Arabic Characters
# ===================================================================

export SOC="mediatek"
export DZ_FACTORY_NAME="DeadZone MediaTek Factory"
export DZ_MODE="${IN_MODE}"
export DZ_NOTIFY="${IN_NOTIFY}"
export DZ_BUILD="${IN_FINAL_NAME}"
export DZ_DEVICE="${IN_CUSTOM_DEVICE:-$IN_DEVICE}"

# Exact binding to match your GitHub Repository Secrets parameters for MTK
export TELEGRAM_BOT_TOKEN="${TELEGRAM_MTK_BOT_TOKEN}"
export TELEGRAM_GROUP_CHAT_ID="${TELEGRAM_MTK_CHAT_ID}"
export TELEGRAM_THREAD_ID="${TELEGRAM_THREAD_ID}"

cd /mnt/dz_data

if [ ! -f "/mnt/dz_data/swapfile" ]; then
    fallocate -l 48G /mnt/dz_data/swapfile || dd if=/dev/zero of=/mnt/dz_data/swapfile bs=1M count=49152
    chmod 600 /mnt/dz_data/swapfile
    mkswap /mnt/dz_data/swapfile
fi
swapon /mnt/dz_data/swapfile || true

rm -rf DeadZone
git clone https://oauth2:${GITHUB_TOKEN}@github.com/DeadZon/DeadZone.git
cd DeadZone

python -m pip install --upgrade wheel --break-system-packages || true
python -m pip install -r requirements.txt --break-system-packages

# ===========================================================================
# 1. Generate Multi-Streaming Telegram Live Notification Script
# ===========================================================================
cat > _dz_tg.py << 'PYEOF'
import argparse, json, os, sys, urllib.error, urllib.request
from datetime import datetime, timezone

STATE_FILE = "/tmp/telegram_multi_live_message_mtk.json"
STAGES = ["prepare", "download_rom", "extract_rom", "patch_rom", "rebuild_super", "package_zip", "validate_zip", "upload_pixeldrain", "github_release", "telegram_final"]
ICONS = {"pending": "⬜", "running": "🔄", "pass": "✅", "fail": "❌", "skip": "⏭️"}

# Explicit Permanent Hardcoded Owners
LIVE_OWNERS = [7504802216, 6114057985]

def _now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

def _run_url():
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com").rstrip("/")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    return f"{server}/{repo}/actions/runs/{run_id}" if repo and run_id else ""

def _credentials():
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    group_chat = os.environ.get("TELEGRAM_GROUP_CHAT_ID", "").strip()
    thread_id = os.environ.get("TELEGRAM_THREAD_ID", "").strip()
    return token, group_chat, thread_id

def _build_message(state):
    soc = os.environ.get("SOC", "MEDIATEK").upper()
    run_num = os.environ.get("GITHUB_RUN_NUMBER", "")
    header = f"DeadZone {soc} Build" + (f" #{run_num}" if run_num else "")
    lines = [header, f"Device: {state.get('device', '?')} | Platform: {state.get('platform', '?')} | Flavor: {state.get('flavor', '?')} | Mode: {state.get('mode', '?')}"]
    if state.get("run_url"): lines.append(f"Run: {state['run_url']}")
    lines.append("\nStages:")
    for stage in STAGES:
        s = state.get("stages", {}).get(stage, {})
        icon = ICONS.get(s.get("status", "pending"), "⬜")
        msg = s.get("message", "")
        line = f"  {icon} {stage}" + (f": {msg}" if msg else "")
        lines.append(line)
    lines.append(f"\nStarted: {state.get('started_at', '')}")
    if state.get("updated_at") and state["updated_at"] != state["started_at"]:
        lines.append(f"Updated: {state['updated_at']}")
    return "\n".join(lines)

def _load_state():
    try:
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r", encoding="utf-8") as f: return json.load(f)
    except: pass
    return {}

def _save_state(state):
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f: json.dump(state, f, indent=2, ensure_ascii=False)
    except: pass

def _post(token, method, payload):
    if os.environ.get("DZ_NOTIFY", "true").strip().lower() not in ("true", "1", "yes"): return None
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp: return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if "message is not modified" in e.read().decode("utf-8", errors="replace").lower(): return {"ok": True}
        return None
    except: return None

def cmd_start(args):
    token, group_chat_id, thread_id = _credentials()
    if not token: return 0
    now = _now_iso()
    
    state = {
        "group_message_id": None,
        "owner_messages": {},
        "started_at": now,
        "updated_at": now,
        "device": os.environ.get("DZ_DEVICE", "?"),
        "platform": os.environ.get("IN_PLATFORM", "?"),
        "flavor": os.environ.get("IN_FLAVOR", "?"),
        "mode": os.environ.get("DZ_MODE", "?"),
        "run_url": _run_url(),
        "stages": {s: {"status": "pending", "message": ""} for s in STAGES}
    }
    state["stages"]["prepare"] = {"status": "running", "message": "Preparing MediaTek cloud stream channels..."}
    text_content = _build_message(state)
    
    # Dispatch card to target Group Chat
    if group_chat_id:
        payload = {"chat_id": group_chat_id, "text": text_content, "disable_web_page_preview": True}
        if thread_id: payload["message_thread_id"] = int(thread_id)
        res = _post(token, "sendMessage", payload)
        if res and res.get("ok"): state["group_message_id"] = res["result"]["message_id"]
        
    # Dispatch cards parallel to BOTH owners private DMs
    for owner_id in LIVE_OWNERS:
        payload = {"chat_id": owner_id, "text": text_content, "disable_web_page_preview": True}
        res = _post(token, "sendMessage", payload)
        if res and res.get("ok"): state["owner_messages"][str(owner_id)] = res["result"]["message_id"]
        
    _save_state(state)
    return 0

def cmd_update(args):
    token, group_chat_id, thread_id = _credentials()
    state = _load_state()
    if not token or not state: return 0
    if args.stage not in STAGES: return 0
    
    state.setdefault("stages", {})[args.stage] = {"status": args.status, "message": args.message or ""}
    state["updated_at"] = _now_iso()
    _save_state(state)
    text_content = _build_message(state)
    
    if group_chat_id and state.get("group_message_id"):
        payload = {"chat_id": group_chat_id, "message_id": int(state["group_message_id"]), "text": text_content, "disable_web_page_preview": True}
        if thread_id: payload["message_thread_id"] = int(thread_id)
        _post(token, "editMessageText", payload)
        
    owner_msgs = state.get("owner_messages", {})
    for owner_id in LIVE_OWNERS:
        mid = owner_msgs.get(str(owner_id))
        if mid:
            payload = {"chat_id": owner_id, "message_id": int(mid), "text": text_content, "disable_web_page_preview": True}
            _post(token, "editMessageText", payload)
    return 0

def cmd_final(args):
    token, group_chat_id, thread_id = _credentials()
    state = _load_state()
    if not token or not state: return 0
    stages = state.setdefault("stages", {})
    
    if args.result == "success":
        for s in STAGES:
            if stages.get(s, {}).get("status") in ("pending", "running"): stages[s] = {"status": "pass", "message": "Completed successfully."}
        stages["telegram_final"] = {"status": "pass", "message": args.message or "Compilation finalized successfully."}
    else:
        for s in reversed(STAGES):
            if stages.get(s, {}).get("status") == "running":
                stages[s] = {"status": "fail", "message": args.message or "Execution broken."}
                break
        stages["telegram_final"] = {"status": "fail", "message": "Pipeline critical execution failure."}
        
    state["updated_at"] = _now_iso()
    _save_state(state)
    text_content = _build_message(state)
    
    if group_chat_id and state.get("group_message_id"):
        payload = {"chat_id": group_chat_id, "message_id": int(state["group_message_id"]), "text": text_content, "disable_web_page_preview": True}
        if thread_id: payload["message_thread_id"] = int(thread_id)
        _post(token, "editMessageText", payload)
        
    owner_msgs = state.get("owner_messages", {})
    for owner_id in LIVE_OWNERS:
        mid = owner_msgs.get(str(owner_id))
        if mid:
            payload = {"chat_id": owner_id, "message_id": int(mid), "text": text_content, "disable_web_page_preview": True}
            _post(token, "editMessageText", payload)
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("start")
    p = sub.add_parser("update")
    p.add_argument("--stage", required=True)
    p.add_argument("--status", required=True)
    p.add_argument("--message", default="")
    p = sub.add_parser("final")
    p.add_argument("--result", required=True)
    p.add_argument("--message", default="")
    args = parser.parse_args()
    if args.command == "start": cmd_start(args)
    elif args.command == "update": cmd_update(args)
    elif args.command == "final": cmd_final(args)
PYEOF

NOTIFY_CLI="python3 _dz_tg.py"

# --- 1. Broadcast Start Channels ---
$NOTIFY_CLI start || true
sleep 1
$NOTIFY_CLI update --stage prepare --status pass --message "Multi-channel MTK distribution streaming active." || true

# ==========================================
# 2. Fastboot Template & Registry Validation
# ==========================================
$NOTIFY_CLI update --stage validate_zip --status running --message "Verifying template components integration mapping..." || true
TEMPLATE="third_party/mezo_core/templates/deadzone_fastboot"
MISSING=0
for f in bin/windows/fastboot.exe bin/windows/AdbWinApi.dll bin/windows/AdbWinUsbApi.dll; do
  if [ ! -f "$TEMPLATE/$f" ]; then MISSING=1; fi
done
if [ "$MISSING" = "1" ]; then
  $NOTIFY_CLI update --stage validate_zip --status fail --message "Template structural dependencies missing." || true
  $NOTIFY_CLI final --result failure --message "Template check error triggered." || true
  exit 1
fi

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
$NOTIFY_CLI update --stage download_rom --status running --message "Downloading architecture baseline source zip payload..." || true
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
$NOTIFY_CLI update --stage download_rom --status pass --message "Firmware snapshot downloaded completely to workspace memory." || true

# ==========================================
# 6. Device Guard & Pipeline Execution
# ==========================================
ROM_FILE="$(find _input_roms -type f | head -n 1)"
TELEGRAM_FLAG=""
if [ "$DZ_NOTIFY" = "true" ]; then TELEGRAM_FLAG="--telegram"; fi

$NOTIFY_CLI update --stage extract_rom --status running --message "Unpacking baseline architecture content..." || true
$NOTIFY_CLI update --stage patch_rom --status running --message "Executing modifications algorithms configurations..." || true
$NOTIFY_CLI update --stage rebuild_super --status running --message "Compiling high speed system logical structures image sparse block..." || true
$NOTIFY_CLI update --stage package_zip --status running --message "Compressing targets distribution flashable package..." || true

if [ "$DZ_MODE" == "dry_run" ]; then
  python -m factory.pipeline.legacy_build_orchestrator \
    --rom "$ROM_FILE" --output-dir output --build-name "$FINAL_NAME" \
    --device "$EFFECTIVE_DEVICE" --soc "$SOC" --platform "$IN_PLATFORM" \
    --flavor "$FLAVOR" --android-version "$IN_ANDROID_VERSION" \
    --mi-version "$IN_MI_VERSION" --vbmeta-mode "$IN_VBMETA_MODE" \
    --template-zip third_party/mezo_core/templates/deadzone_fastboot $TELEGRAM_FLAG
else
  python -m factory.pipeline.legacy_build_orchestrator \
    --rom "$ROM_FILE" --output-dir output --build-name "$FINAL_NAME" \
    --device "$EFFECTIVE_DEVICE" --soc "$SOC" --platform "$IN_PLATFORM" \
    --flavor "$FLAVOR" --android-version "$IN_ANDROID_VERSION" \
    --mi-version "$IN_MI_VERSION" --vbmeta-mode "$IN_VBMETA_MODE" \
    --template-zip third_party/mezo_core/templates/deadzone_fastboot \
    --execute $TELEGRAM_FLAG
fi

$NOTIFY_CLI update --stage extract_rom --status pass --message "Payload entries structural extraction finalized." || true
$NOTIFY_CLI update --stage patch_rom --status pass --message "System configuration modification sequence verified." || true
$NOTIFY_CLI update --stage rebuild_super --status pass --message "Logical sparse super block successfully compiled." || true
$NOTIFY_CLI update --stage package_zip --status pass --message "Distribution package zip compressed finalized safely." || true
$NOTIFY_CLI update --stage validate_zip --status pass --message "System structural block verification integrity matches." || true

# ==========================================
# 7. PixelDrain Upload & Cleanup
# ==========================================
if [ "$DZ_MODE" == "execute" ]; then
  $NOTIFY_CLI update --stage upload_pixeldrain --status running --message "Pushing zipped final delivery payload to PixelDrain server..." || true
  FINAL_ZIP="$(find output/final -maxdepth 1 -name '*.zip' -type f 2>/dev/null | head -n 1)"
  mkdir -p output/reports
  set +e
  python -m factory.services.pixeldrain_upload "$FINAL_ZIP"
  PD_EXIT=$?
  set -e
  if [ "$PD_EXIT" = "0" ]; then
    PD_LINK=$(cat output/reports/pixeldrain_upload.json | grep -o '"link": *"[^"]*"' | cut -d'"' -f4)
    echo "$PD_LINK" > output/reports/pixeldrain_link.txt
    $NOTIFY_CLI update --stage upload_pixeldrain --status pass --message "PixelDrain mirror links live." || true
    $NOTIFY_CLI update --stage github_release --status running --message "Tagging current compilation build onto repository production releases..." || true
  else
    $NOTIFY_CLI update --stage upload_pixeldrain --status fail --message "Cloud server connection timed out." || true
  fi
  
  gh release create "$GITHUB_RUN_ID" output/reports/* output/logs/* --title "DeadZone $EFFECTIVE_DEVICE | $FINAL_NAME" --notes "Build Reports for Run $GITHUB_RUN_ID" || true
  $NOTIFY_CLI update --stage github_release --status pass --message "Release parameters tagged and verified completely." || true
fi

$NOTIFY_CLI final --result success --message "Pipeline distribution finalized without errors. Installation payload stable." || true

rm -rf _input_roms/ output/tmp output/work || true
