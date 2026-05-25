"""Fly builder API server.

POST /build
  {
    "codename":           "zircon",
    "edition":            "base",
    "rom_url":            "...",
    "mode":               "execute",
    "soc":                "mtk",
    "upload_pixeldrain":  true,
    "notify_telegram":    true,
    "build_id":           "DZ-mtk-zircon-...",   # optional — generated if absent
    "telegram_message_id": 12345                  # optional — reuse GitHub message
  }
  Authorization: Bearer $BUILDER_TOKEN

GET /job/<job_id>
  Returns job status and result.

GET /status/<build_id>
  Returns live status by build_id.

GET /health
  Returns service health and version.

Requires: pip install flask
"""
from __future__ import annotations

import datetime
import os

try:
    from flask import Flask, jsonify, request
except ImportError:
    raise SystemExit("flask is required: pip install flask")

from server.auth import AuthError, verify_token
from server.job_runner import start_worker
from server.queue import enqueue, get_job, get_job_by_build_id

_VERSION = "2.0.0"

app = Flask(__name__)


@app.before_request
def _auth():
    if request.path in ("/health",):
        return
    if not verify_token(request.headers.get("Authorization")):
        raise AuthError()


@app.errorhandler(AuthError)
def _handle_auth(exc):
    return jsonify({"error": exc.message}), 401


@app.route("/health")
def health():
    return jsonify({
        "ok":      True,
        "service": "deadzone-builder",
        "version": _VERSION,
        "time":    datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    })


@app.route("/build", methods=["POST"])
def build():
    payload = request.get_json(force=True)
    if not payload or "codename" not in payload:
        return jsonify({"error": "codename is required"}), 400

    codename = payload["codename"]
    soc      = payload.get("soc", "")
    edition  = payload.get("edition", "base")
    mode     = payload.get("mode", "execute")

    # Generate or reuse build_id
    build_id = payload.get("build_id") or None
    if not build_id:
        try:
            from factory.notify.telegram_live import generate_build_id
            build_id = generate_build_id(soc, codename)
        except Exception:
            import datetime, uuid
            ts = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
            build_id = f"DZ-{(soc or 'unk').lower()}-{codename}-{ts}"

    notify = bool(payload.get("notify_telegram", False))
    notifier = None
    telegram_message_id: int | None = None

    if notify:
        try:
            from factory.notify.telegram_live import TelegramLiveStatus
            existing_msg_id = payload.get("telegram_message_id")
            if existing_msg_id is not None:
                try:
                    existing_msg_id = int(existing_msg_id)
                except (ValueError, TypeError):
                    existing_msg_id = None

            notifier = TelegramLiveStatus(
                build_id=build_id,
                soc=soc,
                codename=codename,
                mod=edition,
                mode=mode,
                rom_url=payload.get("rom_url"),
                upload_pixeldrain=bool(payload.get("upload_pixeldrain", False)),
                source=payload.get("source", "Fly"),
                enabled=True,
                telegram_message_id=existing_msg_id,
            )
            start_result = notifier.start()
            notifier.update_stage("FLY_RECEIVED", "Build request received by Fly")
            telegram_message_id = notifier.message_id
        except Exception as exc:
            app.logger.warning("Telegram setup failed: %s", exc)
            notifier = None

    job_id = enqueue(
        payload,
        build_id=build_id,
        notifier=notifier,
        telegram_message_id=telegram_message_id,
    )

    return jsonify({
        "accepted":           True,
        "job_id":             job_id,
        "build_id":           build_id,
        "status":             "queued",
        "telegram_message_id": telegram_message_id,
    }), 202


@app.route("/job/<job_id>")
def job_status(job_id: str):
    job = get_job(job_id)
    if not job:
        return jsonify({"error": "job not found"}), 404
    return jsonify({
        "job_id":             job.job_id,
        "build_id":           job.build_id,
        "status":             job.status,
        "stage":              job.stage,
        "telegram_message_id": job.telegram_message_id,
        "started_at":         job.started_at,
        "updated_at":         job.updated_at,
        "result":             job.result,
        "error":              job.error,
    })


@app.route("/status/<build_id>")
def build_status(build_id: str):
    job = get_job_by_build_id(build_id)
    if not job:
        return jsonify({"error": "build not found"}), 404

    snap = {}
    if job.notifier is not None:
        try:
            snap = job.notifier.snapshot()
        except Exception:
            pass

    return jsonify({
        "build_id":           job.build_id,
        "status":             job.status,
        "stage":              snap.get("stage") or job.stage,
        "action":             snap.get("action"),
        "elapsed":            snap.get("elapsed"),
        "telegram_message_id": job.telegram_message_id,
        "started_at":         job.started_at,
        "updated_at":         job.updated_at,
    })


if __name__ == "__main__":
    start_worker()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
