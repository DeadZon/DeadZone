"""Legacy image collection and payload image movement."""
from __future__ import annotations

import os
import shutil
import stat
from pathlib import Path

# Dynamic partition images — must land in partition_staging_dir, never in output/images.
DYNAMIC_PARTITION_IMAGES: frozenset[str] = frozenset({
    "system.img",
    "product.img",
    "system_ext.img",
    "vendor.img",
    "vendor_dlkm.img",
    "system_dlkm.img",
    "odm.img",
    "odm_dlkm.img",
    "mi_ext.img",
})

# Standalone fastboot images — land directly in output/images.
STANDALONE_IMAGES: frozenset[str] = frozenset({
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "vendor_kernel_boot.img",
    "dtbo.img",
    "vbmeta.img",
    "vbmeta_system.img",
    "vbmeta_vendor.img",
    "logo.img",
    "recovery.img",
    "cust.img",
    "preloader.img",
    "lk.img",
    "persist.img",
    "tee.img",
})

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
    partition_staging_dir: Path | None = None,
    execute: bool = False,
) -> dict:
    """Move payload-extracted files to staging (dynamic) or images (standalone)."""
    project_dir = Path(project_dir)
    images_dir = Path(images_dir)
    partition_staging_dir = Path(partition_staging_dir) if partition_staging_dir is not None else None
    payload_extracted_dir = project_dir / "rom" / "payload_extracted"

    copied_images: list[str] = []
    moved_images: list[str] = []
    dynamic_images_moved_to_staging: list[str] = []
    standalone_images_moved_to_images: list[str] = []
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

    def _base_report() -> dict:
        return {
            "project_dir": str(project_dir),
            "images_dir": str(images_dir),
            "partition_staging_dir": str(partition_staging_dir) if partition_staging_dir else None,
            "required_images": list(REQUIRED_IMAGES),
            "optional_images": list(OPTIONAL_IMAGES),
            "found_images": found_images,
            "missing_required_images": missing_required,
            "payload_entries": [str(entry) for entry in payload_entries],
            "copied_images": copied_images,
            "moved_images": moved_images,
            "dynamic_images_moved_to_staging": dynamic_images_moved_to_staging,
            "standalone_images_moved_to_images": standalone_images_moved_to_images,
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    if not execute:
        print(f"[images] Dry-run: would collect images into: {images_dir}")
        return {"status": "DRY_RUN", **_base_report()}

    try:
        images_dir.mkdir(parents=True, exist_ok=True)
    except Exception as exc:
        errors.append(f"create images directory: {exc}")
        return {"status": "FAILED", **_base_report()}

    if partition_staging_dir is not None:
        try:
            partition_staging_dir.mkdir(parents=True, exist_ok=True)
        except Exception as exc:
            errors.append(f"create partition staging directory: {exc}")
            return {"status": "FAILED", **_base_report()}

    moved_count = 0
    for entry in payload_entries:
        if entry.name in DYNAMIC_PARTITION_IMAGES:
            if partition_staging_dir is None:
                skipped_items.append(f"dynamic image skipped (no staging dir): {entry.name}")
                warnings.append(f"dynamic image skipped — partition_staging_dir not set: {entry.name}")
                continue
            target = partition_staging_dir / entry.name
            try:
                if target.exists() and not remove_path_force(target):
                    warnings.append(f"could not remove duplicate target: {target}")
                    continue
                shutil.move(str(entry), str(target))
                dynamic_images_moved_to_staging.append(entry.name)
                moved_count += 1
                print(f"[images] Moved {entry.name} -> staging {partition_staging_dir}")
            except Exception as exc:
                errors.append(f"move {entry}: {exc}")
        elif entry.name in STANDALONE_IMAGES:
            target = images_dir / entry.name
            try:
                if target.exists() and not remove_path_force(target):
                    warnings.append(f"could not remove duplicate target: {target}")
                    continue
                shutil.move(str(entry), str(target))
                standalone_images_moved_to_images.append(entry.name)
                moved_images.append(str(target))
                moved_count += 1
                print(f"[images] Moved {entry.name} -> images {images_dir}")
            except Exception as exc:
                errors.append(f"move {entry}: {exc}")
        else:
            skipped_items.append(f"payload image not in known sets, skipped: {entry.name}")
            print(f"[images] Skipped unknown payload image: {entry.name}")

    if moved_count > 0:
        try:
            shutil.rmtree(payload_extracted_dir.parent, ignore_errors=True)
            print(f"[images] Moved {moved_count} file(s) from payload_extracted and removed rom directory.")
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
    return {"status": status, **_base_report()}

