"""Final ZIP package validator.

Checks:
- Required tools present (fastboot.exe, AdbWinApi.dll, AdbWinUsbApi.dll)
- images/ directory present
- No forbidden files (super.unsparse.img, build_info.txt, sha256sums.txt, source code)
- No dynamic standalone images when super.img exists
"""
from __future__ import annotations

import zipfile
from pathlib import Path

_REQUIRED_TOOLS = [
    "bin/windows/fastboot.exe",
    "bin/windows/AdbWinApi.dll",
    "bin/windows/AdbWinUsbApi.dll",
]

_FORBIDDEN_NAMES = {
    "sha256sums.txt",
    "build_info.txt",
}

_FORBIDDEN_SUFFIXES = (
    ".unsparse.img",
    ".py",
    ".sh",
)

_DYNAMIC_PARTITIONS = frozenset({
    "system", "product", "system_ext", "vendor", "odm", "mi_ext",
    "system_dlkm", "vendor_dlkm",
})


def validate_package(zip_path: Path | str) -> dict:
    zip_path = Path(zip_path)
    errors: list[str] = []
    warnings: list[str] = []

    if not zip_path.is_file():
        return {"passed": False, "errors": [f"ZIP not found: {zip_path}"], "warnings": []}

    with zipfile.ZipFile(zip_path, "r") as zf:
        names = zf.namelist()

    names_set = set(names)

    # Required tools
    for tool in _REQUIRED_TOOLS:
        if tool not in names_set:
            errors.append(f"Required tool missing from ZIP: {tool}")

    # images/ directory
    if not any(n.startswith("images/") for n in names):
        errors.append("images/ directory not found in ZIP")

    # Forbidden files
    for n in names:
        base = Path(n).name
        if base in _FORBIDDEN_NAMES:
            errors.append(f"Forbidden file in ZIP: {n}")
        if any(n.endswith(suf) for suf in _FORBIDDEN_SUFFIXES):
            errors.append(f"Forbidden file type in ZIP: {n}")

    # If super.img exists, dynamic standalone images must NOT be present
    has_super = "images/super.img" in names_set
    if has_super:
        for n in names:
            if not n.startswith("images/"):
                continue
            stem = Path(n).stem.lower()
            if stem in _DYNAMIC_PARTITIONS:
                errors.append(
                    f"Dynamic standalone image present alongside super.img: {n}"
                )

    passed = not errors
    return {"passed": passed, "errors": errors, "warnings": warnings, "zip": str(zip_path)}


if __name__ == "__main__":
    import json, sys
    if len(sys.argv) < 2:
        print("Usage: python -m factory.validators.package_validator <zip>")
        sys.exit(1)
    r = validate_package(sys.argv[1])
    print(json.dumps(r, indent=2))
    sys.exit(0 if r["passed"] else 1)
