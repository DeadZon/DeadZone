#!/usr/bin/env python3
import json
import os
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "assets_manifest" / "mezo_app_assets.json"
DOWNLOADS = ROOT / "_asset_downloads"

DEFAULT_COMMON = ["thermallevel_to_fps", "system", "product"]

def log(msg: str) -> None:
    print(msg, flush=True)

def filename_from_headers(response, fallback: str) -> str:
    cd = response.headers.get("Content-Disposition", "")
    if "filename=" in cd:
        name = cd.split("filename=", 1)[1].strip().strip('"')
        if name:
            return name
    ctype = response.headers.get("Content-Type", "")
    if "zip" in ctype:
        return fallback + ".zip"
    return fallback + ".bin"

def download_asset(name: str, info: dict) -> Path:
    DOWNLOADS.mkdir(parents=True, exist_ok=True)
    url = info["direct_url"]
    log(f"[MEZO_ASSET] Downloading {name}: {url}")

    req = urllib.request.Request(url, headers={"User-Agent": "DeadZoneFactory/1.0"})
    with urllib.request.urlopen(req, timeout=900) as response:
        filename = filename_from_headers(response, name)
        out = DOWNLOADS / filename
        with out.open("wb") as f:
            shutil.copyfileobj(response, f)

    log(f"[MEZO_ASSET] Saved: {out}")
    return out

def extract_or_copy(file_path: Path, extract_to: Path) -> None:
    extract_to.mkdir(parents=True, exist_ok=True)

    lower = file_path.name.lower()
    if lower.endswith(".zip"):
        log(f"[MEZO_ASSET] Extracting ZIP -> {extract_to}")
        with zipfile.ZipFile(file_path, "r") as z:
            z.extractall(extract_to)
        return

    if lower.endswith((".tar", ".tar.gz", ".tgz")):
        log(f"[MEZO_ASSET] Extracting TAR -> {extract_to}")
        shutil.unpack_archive(str(file_path), str(extract_to))
        return

    target = extract_to / file_path.name
    log(f"[MEZO_ASSET] Copying file -> {target}")
    shutil.copy2(file_path, target)

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python tools_scripts/download_mezo_assets.py OS3_A16")
        print("Allowed: OS3_A16, OS3_A15, OS2_A15, OS2_A14, OS1_A14")
        return 2

    target_os = sys.argv[1].strip()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    if target_os not in manifest:
        raise SystemExit(f"Unknown asset key: {target_os}")

    keys = [*DEFAULT_COMMON, target_os]

    for key in keys:
        info = manifest[key]
        downloaded = download_asset(key, info)
        extract_to = ROOT / info["extract_to"]
        extract_or_copy(downloaded, extract_to)

    log("[MEZO_ASSET] Done.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
