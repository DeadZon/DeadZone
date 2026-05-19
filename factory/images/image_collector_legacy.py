"""Legacy image collection and payload image movement."""
from __future__ import annotations

import os
import shutil
import stat
from pathlib import Path

LEGACY_IMAGE_NAMES: tuple[str, ...] = (
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "vendor_kernel_boot.img",
    "recovery.img",
    "dtbo.img",
    "vbmeta.img",
    "vbmeta_system.img",
    "vbmeta_vendor.img",
    "super.img",
    "super_empty.img",
    "cust.img",
    "preloader.img",
    "lk.img",
    "logo.img",
    "persist.img",
    "tee.img",
)

REQUIRED_IMAGES: tuple[str, ...] = (
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "vbmeta.img",
    "super.img",
)

OPTIONAL_IMAGES: tuple[str, ...] = tuple(
    name for name in LEGACY_IMAGE_NAMES if name not in REQUIRED_IMAGES
)


def remove_path_force(path: Path) -> bool:
    """Remove a file or directory using the legacy force-delete behavior."""
    if not path.exists():
        return True

    def del_rw(target: str) -> None:
        try:
            os.chmod(target, stat.S_IWRITE)
        except OSError:
            pass
        os.remove(target)

    try:
        if path.is_file():
            del_rw(str(path))
        else:
            shutil.rmtree(path, onerror=lambda _, fn, __: del_rw(fn))
    except Exception:
        pass

    if path.exists() and os.name == "nt":
        os.system(f'cmd /c rd /s /q "{path}" >nul 2>nul')

    return not path.exists()


def _candidate_roots(project_dir: Path, images_dir: Path) -> list[Path]:
    roots = [
        project_dir,
        project_dir / "rom",
        project_dir / "rom" / "images",
        project_dir / "images",
    ]
    seen: set[str] = set()
    result: list[Path] = []
    for root in roots:
        key = str(root.resolve()) if root.exists() else str(root)
        if key in seen:
            continue
        seen.add(key)
        if root.is_dir() and root != images_dir:
            result.append(root)
    return result


def _find_image_sources(project_dir: Path, images_dir: Path) -> dict[str, Path]:
    found: dict[str, Path] = {}
    names = {name.lower() for name in LEGACY_IMAGE_NAMES}
    for root in _candidate_roots(project_dir, images_dir):
        try:
            for entry in sorted(root.iterdir(), key=lambda item: item.name.lower()):
                if entry.is_file() and entry.name.lower() in names:
                    found.setdefault(entry.name.lower(), entry)
        except Exception:
            continue
    return found


def collect_required_images_legacy(
    project_dir: Path,
    images_dir: Path,
    execute: bool = False,
) -> dict:
    """Move payload-extracted files and copy legacy standalone images."""
    project_dir = Path(project_dir)
    images_dir = Path(images_dir)
    payload_extracted_dir = project_dir / "rom" / "payload_extracted"

    copied_images: list[str] = []
    moved_images: list[str] = []
    found_images: list[str] = []
    missing_required: list[str] = []
    skipped_items: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    sources = _find_image_sources(project_dir, images_dir)
    found_images = sorted({path.name for path in sources.values()})

    for required in REQUIRED_IMAGES:
        if required.lower() not in sources and not (images_dir / required).is_file():
            missing_required.append(required)
            warnings.append(f"required image missing: {required}")

    payload_entries: list[Path] = []
    if payload_extracted_dir.is_dir():
        try:
            payload_entries = sorted(
                [entry for entry in payload_extracted_dir.iterdir() if entry.is_file()],
                key=lambda item: item.name.lower(),
            )
        except Exception as exc:
            errors.append(f"payload_extracted scan: {exc}")
    else:
        skipped_items.append(f"payload_extracted not found: {payload_extracted_dir}")

    if not execute:
        print(f"[images] Dry-run: would collect images into: {images_dir}")
        return {
            "status": "DRY_RUN",
            "project_dir": str(project_dir),
            "images_dir": str(images_dir),
            "required_images": list(REQUIRED_IMAGES),
            "optional_images": list(OPTIONAL_IMAGES),
            "found_images": found_images,
            "missing_required_images": missing_required,
            "payload_entries": [str(entry) for entry in payload_entries],
            "copied_images": copied_images,
            "moved_images": moved_images,
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    try:
        images_dir.mkdir(parents=True, exist_ok=True)
    except Exception as exc:
        errors.append(f"create images directory: {exc}")
        return {
            "status": "FAILED",
            "project_dir": str(project_dir),
            "images_dir": str(images_dir),
            "required_images": list(REQUIRED_IMAGES),
            "optional_images": list(OPTIONAL_IMAGES),
            "found_images": found_images,
            "missing_required_images": missing_required,
            "payload_entries": [str(entry) for entry in payload_entries],
            "copied_images": copied_images,
            "moved_images": moved_images,
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    moved_count = 0
    for entry in payload_entries:
        target = images_dir / entry.name
        try:
            if target.exists() and not remove_path_force(target):
                warnings.append(f"could not remove duplicate target: {target}")
                continue
            shutil.move(str(entry), str(target))
            moved_images.append(str(target))
            moved_count += 1
            print(f"[images] Moved {entry.name} -> {images_dir}")
        except Exception as exc:
            errors.append(f"move {entry}: {exc}")

    if moved_count > 0:
        try:
            shutil.rmtree(payload_extracted_dir.parent, ignore_errors=True)
            print(
                f"[images] Moved {moved_count} file(s) from payload_extracted to images and removed rom directory."
            )
        except Exception as exc:
            warnings.append(f"could not remove rom directory: {exc}")
    elif payload_extracted_dir.is_dir():
        print("[images] No files to move from payload_extracted.")

    sources = _find_image_sources(project_dir, images_dir)
    for image_name, src in sorted(sources.items()):
        target = images_dir / src.name
        if target.exists():
            skipped_items.append(f"already present: {target}")
            continue
        try:
            shutil.copy2(src, target)
            copied_images.append(str(target))
            print(f"[images] Copied {src.name} -> {images_dir}")
        except Exception as exc:
            errors.append(f"copy {src}: {exc}")

    status = "FAILED" if errors else "APPLIED"
    return {
        "status": status,
        "project_dir": str(project_dir),
        "images_dir": str(images_dir),
        "required_images": list(REQUIRED_IMAGES),
        "optional_images": list(OPTIONAL_IMAGES),
        "found_images": found_images,
        "missing_required_images": missing_required,
        "payload_entries": [str(entry) for entry in payload_entries],
        "copied_images": copied_images,
        "moved_images": moved_images,
        "skipped_items": skipped_items,
        "warnings": warnings,
        "errors": errors,
    }

