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


def check_min_lines(rel_path: str, min_lines: int) -> list[str]:
    path = REPO_ROOT / rel_path
    if not path.exists():
        fail(f"{rel_path}: file not found")
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(lines) < min_lines:
        fail(f"{rel_path}: only {len(lines)} lines (minimum {min_lines} required — file may be corrupted/minified)")
    else:
        ok(f"{rel_path}: {len(lines)} lines (>= {min_lines})")
    return lines


def check_contains(rel_path: str, text: str, required_patterns: list[str]) -> None:
    for pat in required_patterns:
        if pat not in text:
            fail(f"{rel_path}: missing required pattern: {pat!r}")
        else:
            ok(f"{rel_path}: contains {pat!r}")


def check_forbidden_inputs(rel_path: str, text: str, forbidden_terms: list[str]) -> None:
    """Check that forbidden terms do not appear as YAML workflow input keys."""
    for term in forbidden_terms:
        # Match the term as a YAML key in the inputs section (indented, colon-terminated)
        pattern = rf"^\s{{4,10}}{re.escape(term)}\s*:"
        if re.search(pattern, text, re.MULTILINE):
            fail(f"{rel_path}: forbidden term {term!r} appears as a workflow input key")
        else:
            ok(f"{rel_path}: no forbidden input key {term!r}")


print("\n=== Validate repo text files ===\n")

# ── .dockerignore ─────────────────────────────────────────────────────────────
print("-- .dockerignore --")
di_lines = check_min_lines(".dockerignore", 30)
if di_lines:
    check_contains(".dockerignore", "\n".join(di_lines), [
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
check_min_lines("fly.toml", 10)

# ── docker/Dockerfile.builder ─────────────────────────────────────────────────
print("\n-- docker/Dockerfile.builder --")
check_min_lines("docker/Dockerfile.builder", 10)

# ── deadzone_mtk_fly.yml ─────────────────────────────────────────────────────
print("\n-- .github/workflows/deadzone_mtk_fly.yml --")
mtk_fly_path = ".github/workflows/deadzone_mtk_fly.yml"
mtk_lines = check_min_lines(mtk_fly_path, 50)
if mtk_lines:
    mtk_text = "\n".join(mtk_lines)
    check_forbidden_inputs(mtk_fly_path, mtk_text, [
        "select_device_codename",
        "select_device",
        "custom_device",
        "final_name",
        "flavor",
        "runner_label",
    ])

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\n  Errors: {len(ERRORS)}")

if ERRORS:
    print("\nFAILED — fix the errors above before pushing.\n")
    sys.exit(1)
else:
    print("\nAll checks passed.\n")
    sys.exit(0)
