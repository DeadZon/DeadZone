"""
PixelDrain upload service for DeadZone Factory.

Uploads the final public ROM ZIP to PixelDrain using the PIXELDRAIN_API_KEY
environment variable.  Never upload source ROMs from _input_roms.

Returns/prints the public link: https://pixeldrain.com/u/<file_id>

CLI usage:
  python -m factory.services.pixeldrain_upload <path/to/final_rom.zip>
"""

import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

_UPLOAD_URL = "https://pixeldrain.com/api/file"
_FILE_URL = "https://pixeldrain.com/u"


def upload_to_pixeldrain(file_path: str, api_key: str | None = None) -> dict:
    """Upload file_path to PixelDrain. Returns dict with success, file, id, link."""
    path = Path(file_path)
    if not path.exists():
        return {"success": False, "file": str(path), "error": f"File not found: {file_path}"}

    if api_key is None:
        api_key = os.environ.get("PIXELDRAIN_API_KEY", "").strip() or None

    filename = path.name
    url = f"{_UPLOAD_URL}/{filename}"
    size_mib = path.stat().st_size / 1024 / 1024
    print(f"[PIXELDRAIN] Uploading: {filename} ({size_mib:.1f} MiB)")

    with path.open("rb") as fh:
        file_bytes = fh.read()

    req = urllib.request.Request(url, data=file_bytes, method="PUT")
    req.add_header("Content-Type", "application/octet-stream")

    if api_key:
        token = base64.b64encode(f":{api_key}".encode()).decode()
        req.add_header("Authorization", f"Basic {token}")
    else:
        print("[PIXELDRAIN] No API key found — uploading anonymously")

    try:
        with urllib.request.urlopen(req, timeout=3600) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            resp_data = json.loads(body)
            file_id = resp_data.get("id", "")
            link = f"{_FILE_URL}/{file_id}" if file_id else ""
            if file_id:
                print(f"[PIXELDRAIN] Upload successful: {link}")
                return {"success": True, "file": str(path), "id": file_id, "link": link}
            print(f"[PIXELDRAIN] Upload response missing id: {body}", file=sys.stderr)
            return {"success": False, "file": str(path), "id": "", "link": "", "error": body}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        msg = f"HTTP {exc.code}: {body}"
        print(f"[PIXELDRAIN] {msg}", file=sys.stderr)
        return {"success": False, "file": str(path), "id": "", "link": "", "error": msg}
    except Exception as exc:
        print(f"[PIXELDRAIN] Upload failed: {exc}", file=sys.stderr)
        return {"success": False, "file": str(path), "id": "", "link": "", "error": str(exc)}


def write_sidecar(result: dict) -> None:
    out_dir = Path("output") / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    sidecar = out_dir / "pixeldrain_upload.json"
    sidecar.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"[PIXELDRAIN] Sidecar written: {sidecar}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m factory.services.pixeldrain_upload <path/to/final_rom.zip>")
        sys.exit(1)
    _result = upload_to_pixeldrain(sys.argv[1])
    write_sidecar(_result)
    if _result.get("success"):
        print(f"[PIXELDRAIN] Link: {_result['link']}")
        sys.exit(0)
    else:
        print(f"[PIXELDRAIN] Upload failed: {_result.get('error', 'unknown')}", file=sys.stderr)
        sys.exit(1)
