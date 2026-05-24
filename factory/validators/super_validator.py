"""Super image validator — checks size and rejects unsparse intermediates."""
from __future__ import annotations

from pathlib import Path

_DEFAULT_SUPER_SIZE = 9126805504


def validate_super(images_dir: Path | str, expected_size: int = _DEFAULT_SUPER_SIZE) -> dict:
    images_dir = Path(images_dir)
    errors: list[str] = []
    warnings: list[str] = []

    super_img = images_dir / "super.img"
    if not super_img.is_file():
        return {"passed": False, "errors": ["super.img not found in images_dir"], "warnings": []}

    actual_size = super_img.stat().st_size
    if actual_size != expected_size:
        errors.append(
            f"super.img size mismatch: expected {expected_size} bytes, got {actual_size} bytes"
        )

    # Unsparse intermediate must not be present
    for p in images_dir.glob("*.unsparse.img"):
        errors.append(f"Unsparse intermediate present: {p.name} — must be removed before packaging")

    passed = not errors
    return {
        "passed": passed,
        "super_size_bytes": actual_size,
        "expected_size_bytes": expected_size,
        "errors": errors,
        "warnings": warnings,
    }


if __name__ == "__main__":
    import json, sys
    images = sys.argv[1] if len(sys.argv) > 1 else "output/images"
    r = validate_super(images)
    print(json.dumps(r, indent=2))
    sys.exit(0 if r["passed"] else 1)
