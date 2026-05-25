"""Fly builder — background job runner.

Picks jobs off the queue and runs the factory pipeline.
Runs in a daemon thread started by builder_api.py on startup.
"""
from __future__ import annotations

import threading
import time
import traceback

from server.queue import claim_next, complete_job, fail_job, update_job_stage


def _run_job(job) -> None:
    payload  = job.payload
    notifier = job.notifier    # TelegramLiveStatus or None

    def _stage(stage: str, action: str) -> None:
        update_job_stage(job.job_id, stage)
        if notifier is not None:
            try:
                notifier.update_stage(stage, action)
            except Exception:
                pass

    try:
        _stage("VALIDATING_REQUEST", "Validating build request")

        from factory.pipeline.orchestrator import run_factory

        _stage("RESOLVING_DEVICE", "Resolving device metadata")

        result = run_factory(
            codename=payload["codename"],
            edition=payload.get("edition", "base"),
            rom_url=payload.get("rom_url"),
            mode=payload.get("mode", "execute"),
            soc=payload.get("soc"),
            upload_pixeldrain=bool(payload.get("upload_pixeldrain", True)),
            notify_telegram=False,   # notifier is passed directly below
            notifier=notifier,
        )

        final_status = result.get("final_status", "APPLIED")
        success = final_status in {"DRY_RUN", "APPLIED"}

        if notifier is not None:
            try:
                notifier.finish(
                    success=success,
                    final_zip=result.get("final_zip"),
                    pixeldrain_link=result.get("pixeldrain_link"),
                    error="; ".join(result.get("errors") or []) or None,
                )
            except Exception:
                pass

        complete_job(job.job_id, result)

    except Exception as exc:
        tb = traceback.format_exc()
        short_err = f"{type(exc).__name__}: {exc}"
        update_job_stage(job.job_id, "FAILED")

        if notifier is not None:
            try:
                notifier.finish(success=False, error=short_err)
            except Exception:
                pass

        fail_job(job.job_id, f"{short_err}\n{tb}")


def _worker_loop() -> None:
    while True:
        job = claim_next()
        if job:
            _run_job(job)
        else:
            time.sleep(2)


def start_worker() -> threading.Thread:
    t = threading.Thread(target=_worker_loop, daemon=True, name="factory-worker")
    t.start()
    return t
