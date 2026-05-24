"""PixelDrain upload — uploads final ROM ZIP and returns public link."""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

_API_BASE = "https://pixeldrain.com/api"
_MAX_RETRIES = 3
_RETRY_DELAY = 25


def upload(zip_path: str | Path, output_dir: Path | None = None) -> dict:
    """Upload zip_path to PixelDrain. Returns status dict with link."""
    zip_path = Path(zip_path)
    api_key = os.environ.get("PIXELDRAIN_API_KEY", "").strip()

    if not api_key:
        return {"status": "SKIPPED", "reason": "PIXELDRAIN_API_KEY not set"}
    if not zip_path.is_file():
        return {"status": "FAILED", "error": f"File not found: {zip_path}"}

    size_bytes = zip_path.stat().st_size
    size_mib = round(size_bytes / (1024 * 1024), 1)
    print(f"[pixeldrain] Uploading: {zip_path.name} ({size_mib} MiB)")

    last_error = ""
    for attempt in range(1, _MAX_RETRIES + 1):
        print(f"[pixeldrain] Attempt {attempt}/{_MAX_RETRIES}")
        try:
            file_id, err = _do_upload(zip_path, api_key)
        except Exception as exc:
            err = str(exc)
            file_id = None

        if file_id:
            link = f"https://pixeldrain.com/u/{file_id}"
            print(f"[pixeldrain] Uploaded OK: {link}")
            result = {
                "status": "UPLOADED",
                "link": link,
                "file_id": file_id,
                "file_name": zip_path.name,
                "size_bytes": size_bytes,
                "size_mib": size_mib,
                "attempts": attempt,
            }
            _write_sidecar(result, output_dir)
            return result

        last_error = err or "unknown error"
        print(f"[pixeldrain] Attempt {attempt} failed: {last_error}", file=sys.stderr)
        if attempt < _MAX_RETRIES:
            time.sleep(_RETRY_DELAY)

    result = {
        "status": "FAILED",
        "error": last_error,
        "attempts": _MAX_RETRIES,
        "file_name": zip_path.name,
    }
    _write_sidecar(result, output_dir)
    return result


def _do_upload(zip_path: Path, api_key: str) -> tuple[str | None, str | None]:
    url = f"{_API_BASE}/file/{zip_path.name}"
    with zip_path.open("rb") as fh:
        data = fh.read()
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Content-Type", "application/octet-stream")
    import base64
    token = base64.b64encode(f":{api_key}".encode()).decode()
    req.add_header("Authorization", f"Basic {token}")
    try:
        with urllib.request.urlopen(req, timeout=1800) as resp:
            body = json.loads(resp.read().decode())
            return body.get("id"), None
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        return None, f"HTTP {exc.code}: {body[:200]}"
    except Exception as exc:
        return None, str(exc)


def _write_sidecar(result: dict, output_dir: Path | None) -> None:
    if output_dir is None:
        return
    reports_dir = Path(output_dir) / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    sidecar = reports_dir / "pixeldrain_upload.json"
    sidecar.write_text(json.dumps(result, indent=2), encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m factory.upload.pixeldrain <zip_path>")
        sys.exit(1)
    r = upload(sys.argv[1])
    print(json.dumps(r, indent=2))
    sys.exit(0 if r.get("status") == "UPLOADED" else 1)
