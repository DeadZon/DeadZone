"""Sanity check critical repo text files are not minified/corrupted one-liners."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

ERRORS: list[str] = []


def fail(msg: str) -> None:
    ERRORS.append(msg)
    print(f"  [FAIL] {msg}")


def ok(msg: str) -> None:
    print(f"  [ OK ] {msg}")


def check_lf_bytes(rel_path: str, min_lf: int) -> bytes:
    """Read raw bytes, fail if CR exists or LF count is below threshold."""
    path = REPO_ROOT / rel_path
    if not path.exists():
        fail(f"{rel_path}: file not found")
        return b""

    raw = path.read_bytes()

    # Fail on any CR byte (catches both CR-only and CRLF)
    if b"\r" in raw:
        cr_only = raw.count(b"\r") - raw.count(b"\r\n")
        crlf = raw.count(b"\r\n")
        fail(
            f"{rel_path}: contains CR bytes (CRLF={crlf}, CR-only={cr_only}) — "
            f"file must be LF-only. Run: python scripts/fix_lf.py"
        )
    else:
        ok(f"{rel_path}: no CR bytes (LF-only)")

    lf_count = raw.count(b"\n")
    if lf_count < min_lf:
        fail(
            f"{rel_path}: only {lf_count} LF bytes (minimum {min_lf} required) — "
            f"file may be minified/corrupted"
        )
    else:
        ok(f"{rel_path}: {lf_count} LF lines (>= {min_lf})")

    return raw


def check_contains(rel_path: str, raw: bytes, required_patterns: list[str]) -> None:
    text = raw.decode("utf-8", errors="replace")
    for pat in required_patterns:
        if pat not in text:
            fail(f"{rel_path}: missing required pattern: {pat!r}")
        else:
            ok(f"{rel_path}: contains {pat!r}")


def check_forbidden_inputs(rel_path: str, raw: bytes, forbidden_terms: list[str]) -> None:
    """Check that forbidden terms do not appear as YAML workflow input keys."""
    text = raw.decode("utf-8", errors="replace")
    for term in forbidden_terms:
        pattern = rf"^\s{{4,10}}{re.escape(term)}\s*:"
        if re.search(pattern, text, re.MULTILINE):
            fail(f"{rel_path}: forbidden term {term!r} appears as a workflow input key")
        else:
            ok(f"{rel_path}: no forbidden input key {term!r}")


print("\n=== Validate repo text files ===\n")

# ── .dockerignore ─────────────────────────────────────────────────────────────
print("-- .dockerignore --")
di_raw = check_lf_bytes(".dockerignore", min_lf=30)
if di_raw:
    check_contains(".dockerignore", di_raw, [
        "*",
        "!server/**",
        "!factory/**",
        "!third_party/mezo_core/**",
        "third_party/mezo_core/MEZO_APP/**",
        "_input_roms/**",
        "*_unpacked/**",
        "*.img",
        "*.zip",
        "*.apk",
    ])

# ── fly.toml ─────────────────────────────────────────────────────────────────
print("\n-- fly.toml --")
check_lf_bytes("fly.toml", min_lf=10)

# ── docker/Dockerfile.builder ─────────────────────────────────────────────────
print("\n-- docker/Dockerfile.builder --")
check_lf_bytes("docker/Dockerfile.builder", min_lf=10)

# ── deadzone_mtk_fly.yml ─────────────────────────────────────────────────────
print("\n-- .github/workflows/deadzone_mtk_fly.yml --")
mtk_fly_path = ".github/workflows/deadzone_mtk_fly.yml"
mtk_raw = check_lf_bytes(mtk_fly_path, min_lf=50)
if mtk_raw:
    check_forbidden_inputs(mtk_fly_path, mtk_raw, [
        "select_device_codename",
        "select_device",
        "custom_device",
        "final_name",
        "flavor",
        "runner_label",
    ])

# ── validate_repo_text_files.py itself ───────────────────────────────────────
print("\n-- scripts/validate_repo_text_files.py --")
check_lf_bytes("scripts/validate_repo_text_files.py", min_lf=50)

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\n  Errors: {len(ERRORS)}")

if ERRORS:
    print("\nFAILED — fix the errors above before pushing.\n")
    sys.exit(1)
else:
    print("\nAll checks passed.\n")
    sys.exit(0)
