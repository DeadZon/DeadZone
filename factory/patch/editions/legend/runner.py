"""Legend edition runner — delegates to factory.patch.legend.runner (canonical location).

This module is the editions-system entry point for the Legend edition.
The actual implementation lives in factory.patch.legend.runner and is kept
there until a full migration is complete.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any


def run_edition(
    root: Path | str,
    output_dir: Path | str | None = None,
    context: dict[str, Any] | None = None,
) -> dict:
    """Apply Legend patches — delegates to factory.patch.legend.runner.run_legend."""
    from factory.patch.legend.runner import run_legend

    result = run_legend(root=root, output_dir=output_dir, context=context)
    # Normalise key for editions system
    if "edition" not in result:
        result["edition"] = "legend"
    return result
