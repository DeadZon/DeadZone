#!/usr/bin/env python3
import json
import shutil
import sys
import time
import urllib.parse
import zipfile
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "assets_manifest" / "mezo_app_assets.json"
DOWNLOADS = ROOT / "_asset_downloads"

DEFAULT_COMMON = ["thermallevel_to_fps", "system", "product"]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "*/*",
    "Referer": "https://pixeldrain.com/",
}


def log(msg: str) -> None:
    print(msg, flush=True)


def pixeldrain_id_from_url(url: str) -> str | None:
    parsed = urllib.parse.urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]

    if len(parts) >= 2 and parts[0] == "u":
        return parts[1]

    if len(parts) >= 3 and parts[0] == "api" and parts[1] == "file":
        return parts[2]

    return None


def filename_from_response(response: requests.Response, fallback: str) -> str:
    cd = response.headers.get("Content-Disposition", "")
    if "filename=" in cd:
        name = cd.split("filename=", 1)[1].strip().strip('"')
        if name:
            return name

    ctype = response.headers.get("Content-Type", "")
    if "zip" in ctype:
        return fallback + ".zip"

    return fallback + ".bin"


def candidate_urls(info: dict) -> list[str]:
    urls: list[str] = []

    direct = info.get("direct_url")
    page = info.get("page_url")

    if direct:
        urls.append(direct)

        file_id = pixeldrain_id_from_url(direct)
        if file_id:
            urls.append(f"https://pixeldrain.com/api/file/{file_id}?download")
            urls.append(f"https://pixeldrain.com/u/{file_id}")

    if page:
        file_id = pixeldrain_id_from_url(page)
        if file_id:
            urls.append(f"https://pixeldrain.com/api/file/{file_id}")
            urls.append(f"https://pixeldrain.com/api/file/{file_id}?download")
        urls.append(page)

    # de-duplicate, keep order
    clean: list[str] = []
    seen = set()
    for url in urls:
        if url and url not in seen:
            clean.append(url)
            seen.add(url)

    return clean


def download_asset(name: str, info: dict) -> Path:
    DOWNLOADS.mkdir(parents=True, exist_ok=True)

    last_error = None

    for url in candidate_urls(info):
        try:
            log(f"[MEZO_ASSET] Downloading {name}: {url}")

            with requests.get(url, headers=HEADERS, stream=True, timeout=120) as r:
                ctype = r.headers.get("Content-Type", "")
                log(f"[MEZO_ASSET] HTTP {r.status_code} content-type={ctype}")

                if r.status_code == 403:
                    body = ""
                    try:
                        body = r.text[:500]
                    except Exception:
                        pass
                    raise RuntimeError(f"403 Forbidden from {url}\n{body}")

                r.raise_for_status()

                # If page_url returned HTML, skip it because it is not the actual file.
                if "text/html" in ctype.lower():
                    raise RuntimeError(f"Got HTML page, not file: {url}")

                filename = filename_from_response(r, name)
                out = DOWNLOADS / filename

                with out.open("wb") as f:
                    downloaded = 0
                    for chunk in r.iter_content(chunk_size=1024 * 1024):
                        if not chunk:
                            continue
                        f.write(chunk)
                        downloaded += len(chunk)
                        if downloaded % (100 * 1024 * 1024) < 1024 * 1024:
                            log(f"[MEZO_ASSET] {name}: {downloaded / 1024 / 1024:.1f} MiB")

                if out.stat().st_size <= 0:
                    raise RuntimeError(f"Downloaded empty file: {out}")

                log(f"[MEZO_ASSET] Saved: {out} size={out.stat().st_size}")
                return out

        except Exception as exc:
            last_error = exc
            log(f"[MEZO_ASSET] Failed {name} from {url}: {exc}")
            time.sleep(3)

    raise RuntimeError(f"Could not download asset {name}. Last error: {last_error}")


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
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8-sig"))

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
