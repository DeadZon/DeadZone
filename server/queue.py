"""Fly builder — simple in-process job queue.

One build job at a time; queued jobs wait.
"""
from __future__ import annotations

import threading
import uuid
from dataclasses import dataclass, field
from typing import Any, Optional

_lock = threading.Lock()
_jobs: dict[str, "Job"] = {}
_active: Optional[str] = None  # job_id currently running


@dataclass
class Job:
    job_id: str
    payload: dict
    status: str = "queued"          # queued | running | done | failed
    result: Optional[dict] = None
    error: Optional[str] = None
    log: list[str] = field(default_factory=list)


def enqueue(payload: dict) -> str:
    """Add a build job to the queue; return job_id."""
    job_id = str(uuid.uuid4())
    with _lock:
        _jobs[job_id] = Job(job_id=job_id, payload=payload)
    return job_id


def get_job(job_id: str) -> Optional[Job]:
    return _jobs.get(job_id)


def claim_next() -> Optional[Job]:
    """Mark next queued job as running and return it (thread-safe)."""
    global _active
    with _lock:
        if _active:
            return None  # one job at a time
        for job in _jobs.values():
            if job.status == "queued":
                job.status = "running"
                _active = job.job_id
                return job
    return None


def complete_job(job_id: str, result: dict) -> None:
    with _lock:
        global _active
        job = _jobs.get(job_id)
        if job:
            job.status = "done"
            job.result = result
        if _active == job_id:
            _active = None


def fail_job(job_id: str, error: str) -> None:
    with _lock:
        global _active
        job = _jobs.get(job_id)
        if job:
            job.status = "failed"
            job.error = error
        if _active == job_id:
            _active = None
