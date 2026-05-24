"""Fly builder API server.

POST /build
  {
    "codename": "zircon",
    "edition": "base",
    "rom_url": "...",
    "mode": "execute",
    "upload_pixeldrain": true,
    "notify_telegram": true
  }
  Authorization: Bearer $BUILDER_TOKEN

GET /job/<job_id>
  Returns job status and result.

GET /health
  Returns {"status": "ok"}.

Requires: pip install flask
"""
from __future__ import annotations

import os

try:
    from flask import Flask, jsonify, request
except ImportError:
    raise SystemExit("flask is required: pip install flask")

from server.auth import AuthError, verify_token
from server.job_runner import start_worker
from server.queue import enqueue, get_job

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
    return jsonify({"status": "ok"})


@app.route("/build", methods=["POST"])
def build():
    payload = request.get_json(force=True)
    if not payload or "codename" not in payload:
        return jsonify({"error": "codename is required"}), 400

    job_id = enqueue(payload)
    return jsonify({"job_id": job_id, "status": "queued"}), 202


@app.route("/job/<job_id>")
def job_status(job_id: str):
    job = get_job(job_id)
    if not job:
        return jsonify({"error": "job not found"}), 404
    return jsonify({
        "job_id": job.job_id,
        "status": job.status,
        "result": job.result,
        "error": job.error,
    })


if __name__ == "__main__":
    start_worker()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
