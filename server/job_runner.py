"""Fly builder — background job runner.

Picks jobs off the queue and runs the factory pipeline.
Runs in a daemon thread started by builder_api.py on startup.
"""
from __future__ import annotations

import threading
import time

from server.queue import claim_next, complete_job, fail_job


def _run_job(job) -> None:
    payload = job.payload
    try:
        from factory.pipeline.orchestrator import run_factory
        result = run_factory(
            codename=payload["codename"],
            edition=payload.get("edition", "base"),
            rom_url=payload.get("rom_url"),
            mode=payload.get("mode", "execute"),
            upload_pixeldrain=bool(payload.get("upload_pixeldrain", True)),
            notify_telegram=bool(payload.get("notify_telegram", False)),
        )
        complete_job(job.job_id, result)
    except Exception as exc:
        fail_job(job.job_id, str(exc))


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
