import sys
import zipfile
from pathlib import Path

FORBIDDEN_PATTERNS = [
    "/home/runner",
    "workspace",
    ".git",
    "logs",
    "build_info",
    "upload_links",
    "sha256sums",
    "output/",
    "assets/cache/",
]

REQUIRED_ENTRIES = [
    "images/boot.img",
    "images/init_boot.img",
    "images/vendor_boot.img",
    "images/vbmeta.img",
    "images/super.img",
    "windows_install_and_format_data.bat",
    "windows_install_upgrade.bat",
    "windows_format_data_only.bat",
]


def validate_public_zip(zip_path: Path) -> bool:
    zip_path = Path(zip_path)
    if not zip_path.exists():
        print(f"[ERROR] ZIP not found: {zip_path}")
        return False

    ok = True
    print(f"[ZIP] Validating: {zip_path.name}")

    with zipfile.ZipFile(zip_path, "r") as zf:
        names = [n.replace("\\", "/") for n in zf.namelist()]

        for name in names:
            for pattern in FORBIDDEN_PATTERNS:
                if pattern in name:
                    print(f"  [FAIL] Forbidden entry '{name}' matches pattern '{pattern}'")
                    ok = False

        names_lower = [n.lower() for n in names]
        for req in REQUIRED_ENTRIES:
            if req.lower() not in names_lower:
                print(f"  [FAIL] Missing required entry: {req}")
                ok = False
            else:
                print(f"  [OK] Found: {req}")

    if ok:
        print(f"\n[PASS] {zip_path.name} passed public ZIP validation.")
    else:
        print(f"\n[FAIL] {zip_path.name} failed public ZIP validation.")
    return ok


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m factory.validators.validate_public_zip <path.zip>")
        sys.exit(1)
    result = validate_public_zip(Path(sys.argv[1]))
    sys.exit(0 if result else 1)
