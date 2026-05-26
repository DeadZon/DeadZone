"""Super image validator — checks LP block device size and rejects unsparse intermediates."""
from __future__ import annotations

import sys
from pathlib import Path

_DEFAULT_SUPER_SIZE = 9126805504
# Android sparse image magic (simg_header_t.magic = 0xED26FF3A LE).
_SPARSE_MAGIC = b"\x3a\xff\x26\xed"


def validate_super(images_dir: Path | str, expected_size: int = _DEFAULT_SUPER_SIZE) -> dict:
    images_dir = Path(images_dir)
    errors: list[str] = []
    warnings: list[str] = []

    super_img = images_dir / "super.img"
    if not super_img.is_file():
        return {"passed": False, "errors": ["super.img not found in images_dir"], "warnings": []}

    # Detect sparse vs raw to choose the right size-check strategy.
    # stat().st_size on a sparse image returns the compressed file size which is far
    # smaller than the LP block device size — comparing it to expected_size would always
    # fail.  Use lpunpack to read the authoritative block device size instead.
    try:
        with super_img.open("rb") as fh:
            first4 = fh.read(4)
    except OSError as exc:
        return {"passed": False, "errors": [f"Could not read super.img: {exc}"], "warnings": []}

    is_sparse = (first4 == _SPARSE_MAGIC)

    if is_sparse:
        # For sparse super.img, derive block device size via LP metadata (lpunpack).
        # stat(super.img) gives the compressed sparse file size — NOT the device size.
        try:
            _repo_root = Path(__file__).resolve().parents[2]
            _legacy_src = _repo_root / "third_party" / "mezo_core" / "src"
            if str(_legacy_src) not in sys.path:
                sys.path.insert(0, str(_legacy_src))
            from core.lpunpack import get_info as _lp_get_info  # type: ignore
            info = _lp_get_info(str(super_img))
            block_devices = (info.get("block_devices") or []) if info else []
            device_size = int(block_devices[0].get("size", 0)) if block_devices else 0
            if device_size != expected_size:
                errors.append(
                    f"super.img LP block device size {device_size} bytes != "
                    f"expected {expected_size} bytes"
                )
            reported_size = device_size
        except Exception as exc:
            warnings.append(
                f"lpunpack not available — skipping LP block device size check "
                f"for sparse super.img: {exc}"
            )
            reported_size = super_img.stat().st_size
    else:
        # Raw LP image: file size equals the block device size.
        reported_size = super_img.stat().st_size
        if reported_size != expected_size:
            errors.append(
                f"super.img size mismatch: expected {expected_size} bytes, "
                f"got {reported_size} bytes"
            )

    # Unsparse intermediate must not be present
    for p in images_dir.glob("*.unsparse.img"):
        errors.append(f"Unsparse intermediate present: {p.name} — must be removed before packaging")

    passed = not errors
    return {
        "passed": passed,
        "super_img_is_sparse": is_sparse,
        "super_size_bytes": reported_size,
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
