"""Fly builder — simple in-process job queue.

One build job at a time; queued jobs wait.
"""
from __future__ import annotations

import threading
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Optional

_lock = threading.Lock()
_jobs:        dict[str, "Job"] = {}
_by_build_id: dict[str, str]  = {}   # build_id -> job_id
_active: Optional[str] = None        # job_id currently running


@dataclass
class Job:
    job_id:   str
    payload:  dict
    status:   str = "queued"          # queued | running | done | failed
    result:   Optional[dict] = None
    error:    Optional[str]  = None
    log:      list[str] = field(default_factory=list)

    build_id:           Optional[str] = None
    stage:              str            = "QUEUED"
    telegram_message_id: Optional[int] = None
    notifier:           Optional[Any]  = None   # TelegramLiveStatus (in-process)
    started_at:         Optional[str]  = None
    updated_at:         Optional[str]  = None


def _utc_now() -> str:
    import datetime
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def enqueue(
    payload: dict,
    build_id: Optional[str] = None,
    notifier: Optional[Any] = None,
    telegram_message_id: Optional[int] = None,
) -> str:
    """Add a build job to the queue; return job_id."""
    job_id = str(uuid.uuid4())
    now = _utc_now()
    job = Job(
        job_id=job_id,
        payload=payload,
        build_id=build_id,
        notifier=notifier,
        telegram_message_id=telegram_message_id,
        started_at=now,
        updated_at=now,
    )
    with _lock:
        _jobs[job_id] = job
        if build_id:
            _by_build_id[build_id] = job_id
    return job_id


def get_job(job_id: str) -> Optional[Job]:
    return _jobs.get(job_id)


def get_job_by_build_id(build_id: str) -> Optional[Job]:
    job_id = _by_build_id.get(build_id)
    return _jobs.get(job_id) if job_id else None


def claim_next() -> Optional[Job]:
    """Mark next queued job as running and return it (thread-safe)."""
    global _active
    with _lock:
        if _active:
            return None
        for job in _jobs.values():
            if job.status == "queued":
                job.status     = "running"
                job.stage      = "FLY_RECEIVED"
                job.updated_at = _utc_now()
                _active        = job.job_id
                return job
    return None


def update_job_stage(job_id: str, stage: str) -> None:
    with _lock:
        job = _jobs.get(job_id)
        if job:
            job.stage      = stage
            job.updated_at = _utc_now()


def complete_job(job_id: str, result: dict) -> None:
    global _active
    with _lock:
        job = _jobs.get(job_id)
        if job:
            job.status     = "done"
            job.stage      = "DONE"
            job.result     = result
            job.updated_at = _utc_now()
        if _active == job_id:
            _active = None


def fail_job(job_id: str, error: str) -> None:
    global _active
    with _lock:
        job = _jobs.get(job_id)
        if job:
            job.status     = "failed"
            job.stage      = "FAILED"
            job.error      = error
            job.updated_at = _utc_now()
        if _active == job_id:
            _active = None
