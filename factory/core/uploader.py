from __future__ import annotations

import base64
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

from factory.core.workspace import Workspace


PIXELDRAIN_API_URL = "https://pixeldrain.com/api/file"
PIXELDRAIN_PUBLIC_URL = "https://pixeldrain.com/u"
UPLOAD_ATTEMPTS = 3
UPLOAD_RETRY_DELAY = 25


@dataclass
class UploadResult:
    provider: str = "PixelDrain"
    requested: bool = False
    status: str = "not requested"
    final_zip_path: str = "(none)"
    url: str = ""
    file_id: str = ""
    failure_reason: str = ""
    attempts: int = 0
    report_path: str = ""
    links_path: str = ""
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.status == "uploaded" and bool(self.url)


def _api_key() -> str:
    return os.environ.get("PIXELDRAIN_API_KEY", "").strip()


def _write_upload_reports(ws: Workspace, result: UploadResult) -> UploadResult:
    ws.reports.mkdir(parents=True, exist_ok=True)
    links_path = ws.reports / "upload_links.txt"
    report_path = ws.reports / "upload_report.txt"

    if result.url:
        links_path.write_text(f"{result.url}\n", encoding="utf-8")
    else:
        links_path.write_text("", encoding="utf-8")

    lines = [
        "MEZO / DeadZone Upload Report",
        "=============================",
        f"final ZIP path: {result.final_zip_path}",
        f"upload provider: {result.provider}",
        f"upload status: {result.status}",
        f"returned URL: {result.url or '(none)'}",
        f"failure reason: {result.failure_reason or '(none)'}",
        f"attempts: {result.attempts}",
    ]
    if result.warnings:
        lines.extend(["", "warnings:", *result.warnings])
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    result.links_path = str(links_path)
    result.report_path = str(report_path)
    return result


def write_skipped_upload_report(ws: Workspace, requested: bool, reason: str = "") -> UploadResult:
    result = UploadResult(
        requested=requested,
        status="skipped" if requested else "not requested",
        failure_reason=reason,
    )
    return _write_upload_reports(ws, result)


def _put_file(zip_path: Path, api_key: str) -> tuple[str, str]:
    url = f"{PIXELDRAIN_API_URL}/{urllib.parse.quote(zip_path.name)}"
    with zip_path.open("rb") as fh:
        data = fh.read()
    request = urllib.request.Request(url, data=data, method="PUT")
    request.add_header("Content-Type", "application/octet-stream")
    token = base64.b64encode(f":{api_key}".encode("utf-8")).decode("ascii")
    request.add_header("Authorization", f"Basic {token}")
    try:
        with urllib.request.urlopen(request, timeout=3600) as response:
            body = response.read().decode("utf-8", errors="replace")
            payload = json.loads(body)
            file_id = str(payload.get("id") or "").strip()
            if file_id:
                return file_id, ""
            return "", f"upload response missing id: {body[:200]}"
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return "", f"HTTP {exc.code}: {body[:200]}"
    except Exception as exc:
        return "", str(exc)


def upload_final_zip_to_pixeldrain(zip_path: Path | str | None, ws: Workspace) -> UploadResult:
    zip_file = Path(zip_path) if zip_path else None
    result = UploadResult(requested=True, final_zip_path=str(zip_file or "(none)"))

    if zip_file is None or not zip_file.is_file():
        result.status = "failed"
        result.failure_reason = "final ZIP is missing; PixelDrain upload skipped"
        print(f"[UPLOAD] PixelDrain: {result.failure_reason}", file=sys.stderr)
        return _write_upload_reports(ws, result)
    if zip_file.suffix.lower() != ".zip":
        result.status = "failed"
        result.failure_reason = f"final artifact is not a ZIP: {zip_file}"
        print(f"[UPLOAD] PixelDrain: {result.failure_reason}", file=sys.stderr)
        return _write_upload_reports(ws, result)

    api_key = _api_key()
    if not api_key:
        result.status = "failed"
        result.failure_reason = "PIXELDRAIN_API_KEY is required when --upload-pixeldrain is used"
        print(f"[UPLOAD] PixelDrain: {result.failure_reason}", file=sys.stderr)
        return _write_upload_reports(ws, result)

    size_mib = zip_file.stat().st_size / 1024 / 1024
    print(f"[UPLOAD] PixelDrain: uploading final ZIP {zip_file.name} ({size_mib:.1f} MiB)")
    last_error = ""
    for attempt in range(1, UPLOAD_ATTEMPTS + 1):
        result.attempts = attempt
        print(f"[UPLOAD] PixelDrain: attempt {attempt}/{UPLOAD_ATTEMPTS}")
        file_id, error = _put_file(zip_file, api_key)
        if file_id:
            result.status = "uploaded"
            result.file_id = file_id
            result.url = f"{PIXELDRAIN_PUBLIC_URL}/{file_id}"
            print(f"[UPLOAD] PixelDrain: uploaded {result.url}")
            return _write_upload_reports(ws, result)
        last_error = error or "unknown upload error"
        print(f"[UPLOAD] PixelDrain: attempt failed: {last_error}", file=sys.stderr)
        if attempt < UPLOAD_ATTEMPTS:
            time.sleep(UPLOAD_RETRY_DELAY)

    result.status = "failed"
    result.failure_reason = last_error or "unknown upload error"
    return _write_upload_reports(ws, result)
