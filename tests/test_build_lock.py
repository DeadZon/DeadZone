from __future__ import annotations

import os
import tempfile
from pathlib import Path

from factory.core.build_lock import (
    BuildAlreadyRunningError,
    BuildLock,
    _safe_filename,
    make_lock_key,
)


def _tmp() -> Path:
    return Path(tempfile.mkdtemp())


def test_acquire_creates_lock_file():
    output_dir = _tmp()
    lock = BuildLock(output_dir, "test_build")
    lock.acquire()
    assert lock.lock_file.is_file()
    lock.release()


def test_release_removes_lock_file():
    output_dir = _tmp()
    lock = BuildLock(output_dir, "test_build")
    lock.acquire()
    lock.release()
    assert not lock.lock_file.exists()


def test_lock_file_contains_pid():
    output_dir = _tmp()
    lock = BuildLock(output_dir, "mypid_test")
    lock.acquire()
    content = lock.lock_file.read_text(encoding="utf-8")
    assert str(os.getpid()) in content
    lock.release()


def test_double_acquire_raises():
    output_dir = _tmp()
    lock1 = BuildLock(output_dir, "duplicate_build")
    lock2 = BuildLock(output_dir, "duplicate_build")
    lock1.acquire()
    try:
        raised = False
        try:
            lock2.acquire()
        except BuildAlreadyRunningError:
            raised = True
        assert raised, "Expected BuildAlreadyRunningError"
    finally:
        lock1.release()


def test_stale_lock_is_replaced():
    output_dir = _tmp()
    locks_dir = output_dir / "state" / "locks"
    locks_dir.mkdir(parents=True, exist_ok=True)
    lock = BuildLock(output_dir, "stale_build")
    lock.lock_file.write_text("99999 stale_build\n", encoding="utf-8")
    lock.acquire()
    content = lock.lock_file.read_text(encoding="utf-8")
    assert str(os.getpid()) in content
    lock.release()


def test_context_manager_releases_on_exit():
    output_dir = _tmp()
    lock = BuildLock(output_dir, "ctx_test")
    with lock:
        assert lock.lock_file.is_file()
    assert not lock.lock_file.exists()


def test_context_manager_releases_on_exception():
    output_dir = _tmp()
    lock = BuildLock(output_dir, "exc_test")
    try:
        with lock:
            raise ValueError("simulated failure")
    except ValueError:
        pass
    assert not lock.lock_file.exists()


def test_different_keys_dont_conflict():
    output_dir = _tmp()
    lock1 = BuildLock(output_dir, "build_a")
    lock2 = BuildLock(output_dir, "build_b")
    lock1.acquire()
    lock2.acquire()
    assert lock1.lock_file.is_file()
    assert lock2.lock_file.is_file()
    lock1.release()
    lock2.release()


def test_make_lock_key_format():
    key = make_lock_key("mtk", "stable", "lisa", "OS1.0.5.0.TKAMIXM")
    assert "mtk" in key
    assert "stable" in key
    assert "lisa" in key


def test_make_lock_key_normalizes_case():
    k1 = make_lock_key("MTK", "Stable", "Lisa", "OS1.0.5")
    k2 = make_lock_key("mtk", "stable", "lisa", "os1.0.5")
    assert k1 == k2


def test_safe_filename_ascii():
    result = _safe_filename("mtk_stable_lisa_os1.0.5")
    assert "/" not in result
    assert " " not in result


def test_safe_filename_long_key_truncated():
    long_key = "a" * 200
    result = _safe_filename(long_key)
    assert len(result) <= 130
