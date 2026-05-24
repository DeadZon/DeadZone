"""Workspace cleanup — removes intermediate files after a build."""
from __future__ import annotations

import shutil
from pathlib import Path


def cleanup(
    output_dir: Path | str,
    keep_final_zip: bool = True,
) -> dict:
    """Remove build intermediates; optionally remove the final ZIP."""
    output_dir = Path(output_dir)
    removed: list[str] = []
    errors: list[str] = []

    def _rm(path: Path) -> None:
        if not path.exists():
            return
        try:
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            removed.append(str(path))
        except Exception as exc:
            errors.append(f"remove {path}: {exc}")

    # Remove unpacked ROM work dirs
    for pattern in ["*_unpacked", "super_partitions"]:
        for p in output_dir.rglob(pattern):
            if p.is_dir():
                _rm(p)

    # Remove work and tmp dirs
    _rm(output_dir / "work")
    _rm(output_dir / "tmp")

    # Remove super.unsparse.img if present
    for p in output_dir.rglob("*.unsparse.img"):
        _rm(p)

    # Remove images/ after packaging (they are in the ZIP)
    _rm(output_dir / "images")

    # Optionally remove final ZIP (after PixelDrain upload)
    if not keep_final_zip:
        final_dir = output_dir / "final"
        if final_dir.is_dir():
            for zp in final_dir.glob("*.zip"):
                _rm(zp)

    return {
        "status": "APPLIED",
        "removed": removed,
        "errors": errors,
    }
