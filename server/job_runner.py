"""Fly builder — background job runner.

Picks jobs off the queue and runs the factory pipeline.
Runs in a daemon thread started by builder_api.py on startup.
"""
from __future__ import annotations

import os
import threading
import time
import traceback
from pathlib import Path

from server.queue import claim_next, complete_job, fail_job, update_job_stage

_WORK_ROOT = Path(os.environ.get("DZ_WORK_DIR", "/mnt/dz_data/work"))
_MIN_ROM_BYTES = 100 * 1024 * 1024  # 100 MB


def _fly_stop_self() -> None:
    """Ask Fly to stop this machine after the job is done.

    Uses the Fly internal machine API so the machine shuts itself down
    cleanly instead of being force-killed by the autostop heuristic
    while a build is still running.
    """
    machine_id = os.environ.get("FLY_MACHINE_ID", "")
    app_name   = os.environ.get("FLY_APP_NAME", "")
    if not machine_id or not app_name:
        print("[job_runner] FLY_MACHINE_ID / FLY_APP_NAME not set — skipping self-stop")
        return
    try:
        import urllib.request as _ur
        import json as _json
        url = f"http://_api.internal:4280/v1/apps/{app_name}/machines/{machine_id}/stop"
        req = _ur.Request(url, method="POST",
                          data=b"{}",
                          headers={"Content-Type": "application/json"})
        with _ur.urlopen(req, timeout=10):
            pass
        print(f"[job_runner] Sent self-stop to Fly machine {machine_id}")
    except Exception as exc:
        print(f"[job_runner] Self-stop failed (non-fatal): {exc}")


def _download_rom(rom_url: str, build_id: str) -> Path:
    """Download ROM to local work directory; return path."""
    import urllib.request

    work_dir = _WORK_ROOT / build_id
    work_dir.mkdir(parents=True, exist_ok=True)

    ext = ".zip"
    lower = rom_url.lower().split("?")[0]
    if lower.endswith(".tgz"):
        ext = ".tgz"
    elif lower.endswith(".tar.gz"):
        ext = ".tar.gz"

    dest = work_dir / f"source_rom{ext}"

    # Use requests if available for better reliability; fall back to urllib
    try:
        import requests
        with requests.get(rom_url, stream=True, timeout=600) as r:
            r.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size=8 * 1024 * 1024):
                    f.write(chunk)
    except ImportError:
        urllib.request.urlretrieve(rom_url, dest)

    size = dest.stat().st_size
    if size < _MIN_ROM_BYTES:
        raise RuntimeError(
            f"Downloaded ROM is too small ({size} bytes < 100MB). "
            f"URL may be invalid: {rom_url}"
        )
    return dest


def _run_job(job) -> None:
    payload  = job.payload
    notifier = job.notifier

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

        codename = payload["codename"]
        edition  = payload.get("edition") or payload.get("mod") or "free"
        rom_url  = payload.get("rom_url", "")
        mode     = payload.get("mode", "execute")
        soc      = payload.get("soc", "")
        build_id = job.build_id

        _stage("RESOLVING_DEVICE", "Resolving device metadata")

        rom_path: Path | None = None

        if mode == "execute":
            if not rom_url:
                raise ValueError("rom_url is required for execute mode but was not provided")

            _stage("DOWNLOADING_ROM", "Downloading source ROM to Fly worker")
            rom_path = _download_rom(rom_url, build_id)
            _stage("ROM_DOWNLOADED", f"ROM downloaded ({rom_path.stat().st_size // (1024*1024)} MB)")

        result = run_factory(
            codename=codename,
            edition=edition,
            rom_url=rom_url or None,
            rom_path=rom_path,
            mode=mode,
            soc=soc,
            platform=payload.get("platform") or None,
            android_version=payload.get("android_version") or None,
            mi_incremental=payload.get("mi_version") or None,
            vbmeta_mode=payload.get("vbmeta_mode") or None,
            upload_pixeldrain=bool(payload.get("upload_pixeldrain", True)),
            notify_telegram=False,
            notifier=notifier,
        )

        final_status = result.get("final_status", "APPLIED")
        success = final_status in {"DRY_RUN", "APPLIED"}

        if not success:
            errors = result.get("errors") or []
            print(f"[job_runner] FAILED — errors: {errors}")

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
        print(f"[job_runner] Exception: {short_err}")
        print(tb)
        update_job_stage(job.job_id, "FAILED")

        if notifier is not None:
            try:
                notifier.finish(success=False, error=short_err)
            except Exception:
                pass

        fail_job(job.job_id, f"{short_err}\n{tb}")

    finally:
        # Let Fly stop this machine cleanly now that the job is done.
        # This replaces the autostop heuristic which was killing the machine
        # mid-build because it saw no incoming HTTP traffic.
        _fly_stop_self()


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
