"""Fly builder API server.

POST /build
  Accepts new and legacy field names:
    codename / device / custom_codename / custom_device
    edition  / mod    / flavor
    rom_url, mode, soc, upload_pixeldrain, notify_telegram
    platform, android_version, mi_version, vbmeta_mode, final_name
  Authorization: Bearer $BUILDER_TOKEN

GET /job/<job_id>      — job status and result
GET /status/<build_id> — live status by build_id
GET /health            — service health
"""
from __future__ import annotations

import datetime
import os
from typing import Any

try:
    from flask import Flask, jsonify, request
except ImportError:
    raise SystemExit("flask is required: pip install flask")

from server.auth import AuthError, verify_token
from server.job_runner import start_worker
from server.queue import enqueue, get_job, get_job_by_build_id

_VERSION = "2.1.0"

_ACCEPTED_INPUTS = [
    "codename", "custom_codename", "device", "custom_device",
    "edition", "mod", "flavor",
    "rom_url", "mode", "soc",
    "upload_pixeldrain", "notify_telegram",
    "platform", "android_version", "mi_version", "vbmeta_mode",
    "final_name", "build_id", "telegram_message_id", "source",
]

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


_REJECTED_CODENAMES = frozenset({
    "select_device_codename",
    "select_device",
    "device",
    "default",
    "none",
    "null",
    "",
})

_LEGACY_FIELD_NAMES = frozenset({
    "device", "custom_device", "flavor", "platform",
    "android_version", "mi_version", "vbmeta_mode",
})


def _normalize_payload(payload: dict) -> tuple[dict, str | None]:
    """Normalize legacy + new fields into canonical form.

    Returns (normalized_dict, error_string_or_None).
    Legacy fields are accepted internally but logged as warnings.
    """
    # ── Legacy field detection ────────────────────────────────────────────────
    used_legacy = [f for f in _LEGACY_FIELD_NAMES if payload.get(f)]
    if used_legacy:
        app.logger.warning("Legacy fields in request payload: %s — update caller to use canonical fields", used_legacy)

    # ── CODENAME ──────────────────────────────────────────────────────────────
    codename = (
        payload.get("custom_codename")
        or payload.get("custom_device")
        or payload.get("codename")
        or payload.get("device")
        or ""
    ).strip().lower()
    if codename in _REJECTED_CODENAMES:
        return {}, f"codename is required (got: {codename!r})"
    codename = (
        payload.get("custom_codename")
        or payload.get("custom_device")
        or payload.get("codename")
        or payload.get("device")
        or ""
    ).strip()

    # ── MOD / EDITION ─────────────────────────────────────────────────────────
    raw = (
        payload.get("edition")
        or payload.get("mod")
        or payload.get("flavor")
        or "free"
    ).strip().lower()
    _mod_map = {
        "base": "free",
        "deadzone": "free",
        "free": "free",
        "deadzone_legend": "legend",
        "legend": "legend",
        "gaming": "gaming",
        "epic": "epic",
    }
    mod = _mod_map.get(raw, "free")

    # ── FINAL NAME ────────────────────────────────────────────────────────────
    final_name = payload.get("final_name", "").strip()
    if not final_name:
        if mod == "free":
            final_name = f"DeadZone_{codename}_V1"
        else:
            final_name = f"DeadZone_{codename}_{mod}_V1"

    # ── MODE ─────────────────────────────────────────────────────────────────
    mode = payload.get("mode", "execute").strip().lower()
    if mode not in ("execute", "dry_run"):
        mode = "execute"

    # ── ROM URL ───────────────────────────────────────────────────────────────
    rom_url = payload.get("rom_url", "").strip()
    if mode == "execute" and not rom_url:
        return {}, "rom_url is required for execute mode"

    # ── OTHER FIELDS ──────────────────────────────────────────────────────────
    vbmeta = str(payload.get("vbmeta_mode") or "3").strip()

    normalized = {
        "codename":         codename,
        "edition":          mod,
        "mod":              mod,
        "final_name":       final_name,
        "rom_url":          rom_url,
        "mode":             mode,
        "soc":              payload.get("soc", "").strip(),
        "platform":         payload.get("platform", "").strip(),
        "android_version":  str(payload.get("android_version") or "").strip(),
        "mi_version":       str(payload.get("mi_version") or "").strip(),
        "vbmeta_mode":      vbmeta,
        "upload_pixeldrain": bool(payload.get("upload_pixeldrain", False)),
        "notify_telegram":   bool(payload.get("notify_telegram", False)),
        "source":           payload.get("source", "Fly"),
        "build_id":         payload.get("build_id"),
        "telegram_message_id": payload.get("telegram_message_id"),
    }
    return normalized, None


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
    raw = request.get_json(force=True) or {}

    normalized, error = _normalize_payload(raw)

    # If notify is requested, set up Telegram immediately so failures also update it
    notifier = None
    telegram_message_id: int | None = None
    build_id: str | None = None

    if not error:
        codename = normalized["codename"]
        mod      = normalized["mod"]
        mode     = normalized["mode"]
        soc      = normalized["soc"]

        build_id = normalized.get("build_id") or None
        if not build_id:
            try:
                from factory.notify.telegram_live import generate_build_id
                build_id = generate_build_id(soc, codename)
            except Exception:
                ts = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
                build_id = f"DZ-{(soc or 'unk').lower()}-{codename}-{ts}"

        if normalized["notify_telegram"]:
            try:
                from factory.notify.telegram_live import TelegramLiveStatus
                existing_msg_id = normalized.get("telegram_message_id")
                if existing_msg_id is not None:
                    try:
                        existing_msg_id = int(existing_msg_id)
                    except (ValueError, TypeError):
                        existing_msg_id = None

                notifier = TelegramLiveStatus(
                    build_id=build_id,
                    soc=soc,
                    codename=codename,
                    mod=mod,
                    mode=mode,
                    rom_url=normalized["rom_url"],
                    upload_pixeldrain=normalized["upload_pixeldrain"],
                    source=normalized["source"],
                    enabled=True,
                    telegram_message_id=existing_msg_id,
                )
                notifier.start()
                notifier.update_stage("FLY_RECEIVED", "Build request received by Fly")
                telegram_message_id = notifier.message_id
            except Exception as exc:
                app.logger.warning("Telegram setup failed: %s", exc)
                notifier = None
    else:
        # Validation failed — try to send a Telegram FAILED update if requested
        if raw.get("notify_telegram"):
            try:
                from factory.notify.telegram_live import TelegramLiveStatus
                soc_raw = raw.get("soc", "")
                cn_raw = (
                    raw.get("custom_codename")
                    or raw.get("custom_device")
                    or raw.get("codename")
                    or raw.get("device")
                    or "unknown"
                )
                tmp_id = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
                tmp_build_id = f"DZ-{soc_raw or 'unk'}-{cn_raw}-{tmp_id}"
                n = TelegramLiveStatus(
                    build_id=tmp_build_id,
                    soc=soc_raw,
                    codename=cn_raw,
                    mod="",
                    mode=raw.get("mode", "execute"),
                    rom_url=raw.get("rom_url"),
                    upload_pixeldrain=False,
                    source=raw.get("source", "Fly"),
                    enabled=True,
                )
                n.start()
                n.update_stage("FAILED", f"Validation error: {error}")
                n.finish(success=False, error=error)
            except Exception:
                pass

        return jsonify({
            "accepted": False,
            "error": error,
            "accepted_inputs": _ACCEPTED_INPUTS,
        }), 400

    normalized["build_id"] = build_id

    job_id = enqueue(
        normalized,
        build_id=build_id,
        notifier=notifier,
        telegram_message_id=telegram_message_id,
    )

    return jsonify({
        "accepted":            True,
        "job_id":              job_id,
        "build_id":            build_id,
        "status":              "queued",
        "telegram_message_id": telegram_message_id,
    }), 202


@app.route("/job/<job_id>")
def job_status(job_id: str):
    job = get_job(job_id)
    if not job:
        return jsonify({"error": "job not found"}), 404
    return jsonify({
        "job_id":              job.job_id,
        "build_id":            job.build_id,
        "status":              job.status,
        "stage":               job.stage,
        "telegram_message_id": job.telegram_message_id,
        "started_at":          job.started_at,
        "updated_at":          job.updated_at,
        "result":              job.result,
        "error":               job.error,
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
        "build_id":            job.build_id,
        "status":              job.status,
        "stage":               snap.get("stage") or job.stage,
        "action":              snap.get("action"),
        "elapsed":             snap.get("elapsed"),
        "telegram_message_id": job.telegram_message_id,
        "started_at":          job.started_at,
        "updated_at":          job.updated_at,
    })


if __name__ == "__main__":
    start_worker()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
