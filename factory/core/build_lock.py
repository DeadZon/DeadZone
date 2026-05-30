from __future__ import annotations

import hashlib
import os
from pathlib import Path


class BuildAlreadyRunningError(RuntimeError):
    pass


class BuildLock:
    def __init__(self, output_dir: Path, key: str) -> None:
        self.locks_dir = output_dir / "state" / "locks"
        self.key = key
        self.lock_file = self.locks_dir / f"{_safe_filename(key)}.lock"
        self._acquired = False

    def acquire(self) -> None:
        self.locks_dir.mkdir(parents=True, exist_ok=True)
        if self.lock_file.exists():
            try:
                content = self.lock_file.read_text(encoding="utf-8").strip()
                parts = content.split(None, 1)
                pid = int(parts[0]) if parts else -1
                if _pid_exists(pid):
                    raise BuildAlreadyRunningError(
                        f"Build '{self.key}' is already running (PID {pid}). "
                        f"Lock file: {self.lock_file}. "
                        "If the previous run crashed, remove the lock file manually."
                    )
                print(f"[BUILD LOCK] Removing stale lock for '{self.key}' (PID {pid} is not running)")
                self.lock_file.unlink(missing_ok=True)
            except BuildAlreadyRunningError:
                raise
            except Exception as exc:
                print(f"[BUILD LOCK] Warning: could not read existing lock ({exc}); removing it")
                try:
                    self.lock_file.unlink(missing_ok=True)
                except Exception:
                    pass
        self.lock_file.write_text(f"{os.getpid()} {self.key}\n", encoding="utf-8")
        self._acquired = True
        print(f"[BUILD LOCK] Acquired: {self.key}")

    def release(self) -> None:
        if not self._acquired:
            return
        try:
            self.lock_file.unlink(missing_ok=True)
        except Exception as exc:
            print(f"[BUILD LOCK] Warning: failed to release lock '{self.key}': {exc}")
        self._acquired = False
        print(f"[BUILD LOCK] Released: {self.key}")

    def __enter__(self) -> "BuildLock":
        self.acquire()
        return self

    def __exit__(self, *_: object) -> None:
        self.release()


def make_lock_key(soc: str, style: str, codename: str, build: str) -> str:
    parts = [
        soc.strip().lower() or "unknown",
        style.strip().lower() or "unknown",
        codename.strip().lower() or "unknown",
        build.strip().lower() or "unknown",
    ]
    return "_".join(p.replace("/", "-").replace(" ", "-") for p in parts)


def _safe_filename(key: str) -> str:
    safe = "".join(c if (c.isalnum() or c in "-_.") else "_" for c in key)
    if len(safe) > 120:
        digest = hashlib.md5(key.encode("utf-8")).hexdigest()[:8]
        safe = safe[:110] + "_" + digest
    return safe or "unnamed"


def _pid_exists(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except Exception:
        return False
