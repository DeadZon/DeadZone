"""Validate the legend mod structure."""
from __future__ import annotations

from pathlib import Path

_MOD_ROOT = Path(__file__).resolve().parents[1]


def validate(quiet: bool = False) -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    required = [
        "manifest.yml",
        "runner.py",
        "profiles",
        "patchers",
        "assets",
        "reports",
    ]
    for item in required:
        if not (_MOD_ROOT / item).exists():
            errors.append(f"missing: {item}")

    if not quiet:
        for e in errors:
            print(f"[validate_legend] ERROR: {e}")
        for w in warnings:
            print(f"[validate_legend] WARN: {w}")

    return {
        "mod": "legend",
        "passed": not bool(errors),
        "errors": errors,
        "warnings": warnings,
    }


if __name__ == "__main__":
    import sys
    r = validate()
    sys.exit(0 if r["passed"] else 1)
