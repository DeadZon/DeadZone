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


def check_lf_bytes(rel_path: str, min_lf: int, min_lines: int = 0) -> bytes:
    """Read raw bytes; fail if CR, BOM, or counts below threshold."""
    path = REPO_ROOT / rel_path
    if not path.exists():
        fail(f"{rel_path}: file not found")
        return b""

    raw = path.read_bytes()

    # BOM check
    if raw.startswith(b"\xef\xbb\xbf"):
        fail(f"{rel_path}: starts with UTF-8 BOM — must be BOM-free")
    else:
        ok(f"{rel_path}: no BOM")

    # CR check
    if b"\r" in raw:
        cr_only = raw.count(b"\r") - raw.count(b"\r\n")
        crlf = raw.count(b"\r\n")
        fail(
            f"{rel_path}: contains CR bytes (CRLF={crlf}, CR-only={cr_only}) — "
            f"file must be LF-only. Run: python scripts/rewrite_critical_text_files.py"
        )
    else:
        ok(f"{rel_path}: no CR bytes (LF-only)")

    # LF count
    lf_count = raw.count(b"\n")
    if lf_count < min_lf:
        fail(
            f"{rel_path}: only {lf_count} LF bytes (minimum {min_lf} required) — "
            f"file may be minified/corrupted"
        )
    else:
        ok(f"{rel_path}: {lf_count} LF lines (>= {min_lf})")

    # Line count via raw split
    if min_lines > 0:
        line_count = len(raw.split(b"\n"))
        if line_count < min_lines:
            fail(
                f"{rel_path}: only {line_count} split-lines (minimum {min_lines} required) — "
                f"file may be corrupted"
            )
        else:
            ok(f"{rel_path}: {line_count} split-lines (>= {min_lines})")

    return raw


def check_exact_lines(rel_path: str, raw: bytes, required_lines: list[str]) -> None:
    """Fail if any required string is not present as an exact line (not just substring)."""
    actual_lines = {line.decode("utf-8", errors="replace") for line in raw.split(b"\n")}
    for pat in required_lines:
        if pat in actual_lines:
            ok(f"{rel_path}: exact line present: {pat!r}")
        else:
            fail(f"{rel_path}: missing exact line: {pat!r}")


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
di_raw = check_lf_bytes(".dockerignore", min_lf=100, min_lines=100)
if di_raw:
    check_exact_lines(".dockerignore", di_raw, [
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

# ── .gitattributes ────────────────────────────────────────────────────────────
print("\n-- .gitattributes --")
check_lf_bytes(".gitattributes", min_lf=15, min_lines=15)

# ── fly.toml ─────────────────────────────────────────────────────────────────
print("\n-- fly.toml --")
check_lf_bytes("fly.toml", min_lf=20, min_lines=20)

# ── docker/Dockerfile.builder ─────────────────────────────────────────────────
print("\n-- docker/Dockerfile.builder --")
check_lf_bytes("docker/Dockerfile.builder", min_lf=20, min_lines=20)

# ── workflow files ────────────────────────────────────────────────────────────
WORKFLOW_CHECKS = [
    (".github/workflows/deadzone_mtk.yml",              120),
    (".github/workflows/deadzone_snapdragon.yml",        120),
    (".github/workflows/deadzone_mtk_fly.yml",           180),
    (".github/workflows/deadzone_snapdragon_fly.yml",    180),
    (".github/workflows/deploy_fly_builder.yml",          30),
]
WORKFLOW_FORBIDDEN_INPUTS = [
    "select_device_codename",
    "select_device",
    "device",
    "custom_device",
    "final_name",
    "platform",
    "flavor",
    "runner_label",
    "VM_CPUS",
    "VM_MEMORY",
]

for wf_path, wf_min_lf in WORKFLOW_CHECKS:
    print(f"\n-- {wf_path} --")
    wf_raw = check_lf_bytes(wf_path, min_lf=wf_min_lf, min_lines=wf_min_lf)
    if wf_raw:
        check_forbidden_inputs(wf_path, wf_raw, WORKFLOW_FORBIDDEN_INPUTS)

# ── validate_repo_text_files.py itself ───────────────────────────────────────
print("\n-- scripts/validate_repo_text_files.py --")
check_lf_bytes("scripts/validate_repo_text_files.py", min_lf=80, min_lines=80)

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\n  Errors: {len(ERRORS)}")

if ERRORS:
    print("\nFAILED — fix the errors above before pushing.\n")
    sys.exit(1)
else:
    print("\nAll checks passed.\n")
    sys.exit(0)
