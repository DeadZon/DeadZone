"""
payload.bin extraction — self-contained implementation.

Extraction strategy (in priority order):
  1. Internal Python extractor: src.core.payload_extract.extract_partitions_from_payload
     (bundled in third_party/mezo_core, available when its deps are installed)
  2. payload-dumper-go: external binary, looked up in PATH then repo bin/

Partition sizes for super rebuild come from the payload manifest metadata,
NOT from extracted image file sizes.  parse_manifest_partition_sizes() reads
new_partition_info.size for every partition in the manifest.

stdout/stderr from the chosen extractor are captured to the caller-supplied
log_path (output/logs/payload_extract.log) and also echoed to the console.

The _legacy() helper is kept because factory.unpack.super_image (and
factory.unpack.partitions) still delegate fs-extraction work to MEZOBuildRom.
"""
from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Absolute path to mezo_core — used for sys.path injection without CWD reliance.
_MEZO_CORE_DIR = Path(__file__).resolve().parents[2] / "third_party" / "mezo_core"
_REPO_ROOT = Path(__file__).resolve().parents[2]


# ── legacy MEZOBuildRom lazy-import (still needed by super_image + partitions) ─

def _legacy():
    """
    Lazy-import MEZOBuildRom, saving/restoring CWD around the first import.
    Returns the module object (cached by sys.modules on subsequent calls).
    """
    if "MEZOBuildRom" in sys.modules:
        return sys.modules["MEZOBuildRom"]

    saved_cwd = os.getcwd()
    try:
        if str(_MEZO_CORE_DIR) not in sys.path:
            sys.path.insert(0, str(_MEZO_CORE_DIR))
        import MEZOBuildRom as _m  # noqa: PLC0415
        return _m
    finally:
        os.chdir(saved_cwd)


# ── Utilities ─────────────────────────────────────────────────────────────────

def _append_log(log_path: Path, text: str) -> None:
    """Append *text* to log_path, creating parent dirs as needed."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8", errors="replace") as fh:
        if text and not text.endswith("\n"):
            text += "\n"
        fh.write(text)


def _ensure_mezo_core_on_path() -> None:
    if str(_MEZO_CORE_DIR) not in sys.path:
        sys.path.insert(0, str(_MEZO_CORE_DIR))


# ── Public helpers ────────────────────────────────────────────────────────────

def find_payload_bin(search_roots: list[Path]) -> list[Path]:
    """
    Return all payload.bin files found under the given search roots (unique, sorted).
    """
    seen: set[str] = set()
    found: list[Path] = []
    for root in search_roots:
        if not root.exists():
            continue
        try:
            for p in root.rglob("payload.bin"):
                if p.is_file() and str(p) not in seen:
                    seen.add(str(p))
                    found.append(p)
        except Exception:
            pass
    return found


def parse_manifest_partition_sizes(payload_bin: Path) -> dict[str, int]:
    """
    Parse payload.bin manifest and return {partition_name: size_bytes} from
    new_partition_info.size for each partition entry.

    These are the authoritative original sizes for super rebuild — do NOT use
    extracted image file sizes for this purpose.

    Returns an empty dict when the manifest cannot be parsed (non-fatal).
    """
    _ensure_mezo_core_on_path()
    try:
        from src.core.payload_extract import init_payload_info  # noqa: PLC0415
    except Exception as exc:
        print(f"[payload] Warning: cannot import payload_extract for manifest parsing: {exc}")
        return {}

    try:
        with payload_bin.open("rb") as fh:
            manifest = init_payload_info(fh)
        sizes: dict[str, int] = {}
        for part in manifest.partitions:
            try:
                if part.HasField("new_partition_info") and part.new_partition_info.size > 0:
                    sizes[part.partition_name] = part.new_partition_info.size
            except Exception:
                pass
        return sizes
    except Exception as exc:
        print(f"[payload] Warning: manifest size parsing failed: {exc}")
        return {}


# ── Extraction back-ends ──────────────────────────────────────────────────────

def _try_internal_extractor(
    payload_bin: Path,
    out_dir: Path,
    log_path: Path,
) -> bool:
    """
    Attempt extraction via the bundled Python payload_extract library.
    Captures stdout/stderr into log_path and echoes them to the console.
    Returns True on success.
    """
    _ensure_mezo_core_on_path()
    try:
        from src.core.payload_extract import extract_partitions_from_payload  # noqa: PLC0415
    except Exception as exc:
        msg = f"[payload] Internal extractor unavailable: {exc}"
        print(msg)
        _append_log(log_path, msg)
        return False

    buf = io.StringIO()
    try:
        with payload_bin.open("rb") as fh:
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                extract_partitions_from_payload(
                    reader=fh,
                    partitions_name=[],
                    out_dir=str(out_dir),
                    max_workers=32,
                )
        output = buf.getvalue()
        if output:
            print(output, end="" if output.endswith("\n") else "\n")
            _append_log(log_path, output)
        _append_log(log_path, "[payload] Internal extractor: success.")
        return True
    except Exception as exc:
        output = buf.getvalue()
        if output:
            print(output, end="" if output.endswith("\n") else "\n")
            _append_log(log_path, output)
        msg = f"[payload] Internal extractor failed: {exc}"
        print(msg)
        _append_log(log_path, msg)
        return False


def _try_payload_dumper_go(
    payload_bin: Path,
    out_dir: Path,
    log_path: Path,
) -> bool:
    """
    Attempt extraction via payload-dumper-go (PATH or repo bin/).
    stdout/stderr are written directly to log_path.
    Returns True when the process exits 0.
    """
    dumper_name = "payload-dumper-go"
    dumper_path = shutil.which(dumper_name) or str(_REPO_ROOT / "bin" / dumper_name)
    if not Path(dumper_path).exists():
        msg = f"[payload] payload-dumper-go not found (PATH or bin/); skipping fallback."
        print(msg)
        _append_log(log_path, msg)
        return False

    cmd = [dumper_path, "-output", str(out_dir), str(payload_bin)]
    msg = f"[payload] Running payload-dumper-go: {' '.join(cmd)}"
    print(msg)
    _append_log(log_path, msg)

    log_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with log_path.open("a", encoding="utf-8", errors="replace") as log_fh:
            result = subprocess.run(
                cmd,
                stdout=log_fh,
                stderr=subprocess.STDOUT,
                text=True,
            )
        if result.returncode == 0:
            _append_log(log_path, "[payload] payload-dumper-go: success.")
            return True
        else:
            msg = f"[payload] payload-dumper-go exited with code {result.returncode}."
            print(msg)
            _append_log(log_path, msg)
            return False
    except Exception as exc:
        msg = f"[payload] payload-dumper-go execution error: {exc}"
        print(msg)
        _append_log(log_path, msg)
        return False


# ── Primary extraction entry point ────────────────────────────────────────────

def extract_from_payload(
    payload_bin: Path,
    out_dir: Path,
    log_path: Path,
) -> tuple[bool, dict[str, int]]:
    """
    Extract all partitions from *payload_bin* into *out_dir*.

    Returns ``(success, manifest_sizes)`` where:
    - success: True when at least one .img file was produced in out_dir.
    - manifest_sizes: {partition_name: original_size_bytes} from manifest metadata.
      Use these sizes for super rebuild — not extracted file sizes.

    extractor stdout/stderr are captured to *log_path* and echoed to the console.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    header = f"[payload] === Payload extraction start: {payload_bin} ==="
    print(header)
    _append_log(log_path, header)

    manifest_sizes = parse_manifest_partition_sizes(payload_bin)
    if manifest_sizes:
        size_summary = ", ".join(
            f"{k}={v // (1024 * 1024)}MiB" for k, v in sorted(manifest_sizes.items())
        )
        msg = f"[payload] Manifest partition sizes: {size_summary}"
        print(msg)
        _append_log(log_path, msg)
    else:
        _append_log(log_path, "[payload] Warning: no partition sizes read from manifest.")

    # Try internal extractor first.
    success = _try_internal_extractor(payload_bin, out_dir, log_path)

    if not success:
        _append_log(log_path, "[payload] Falling back to payload-dumper-go …")
        success = _try_payload_dumper_go(payload_bin, out_dir, log_path)

    if success:
        # Verify at least one .img landed in out_dir.
        imgs = list(out_dir.glob("*.img"))
        if not imgs:
            msg = (
                "[payload] Extractor reported success but no .img files found "
                f"in {out_dir}; treating as failure."
            )
            print(msg)
            _append_log(log_path, msg)
            success = False
        else:
            img_names = ", ".join(p.name for p in sorted(imgs))
            msg = f"[payload] Images produced: {img_names}"
            print(msg)
            _append_log(log_path, msg)

    footer = f"[payload] === Extraction {'complete' if success else 'FAILED'} ==="
    print(footer)
    _append_log(log_path, footer)

    return success, manifest_sizes
