"""GitHub release uploader (stub — not active in current pipeline)."""
from __future__ import annotations

from pathlib import Path


def upload_to_release(zip_path: Path, tag: str, repo: str | None = None) -> dict:
    """Placeholder for GitHub release asset upload."""
    return {
        "status": "NOT_IMPLEMENTED",
        "reason": "GitHub release upload not yet implemented",
    }
