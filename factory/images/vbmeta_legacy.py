"""Legacy vbmeta patch wrapper."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

from factory.images.image_collector_legacy import remove_path_force

_REPO_ROOT = Path(__file__).resolve().parents[2]
_LEGACY_ROOT = _REPO_ROOT / "third_party" / "mezo_core"


def apply_vbmeta_legacy_patch(
    images_dir: Path,
    vbmeta_mode: str | int | None = None,
    execute: bool = False,
) -> dict:
    """Patch vbmeta.img using the exact legacy avbtool command and flags."""
    images_dir = Path(images_dir)
    vbmeta_img = images_dir / "vbmeta.img"
    avbtool_path = _LEGACY_ROOT / "vbmeta" / "avbtool.py"
    avb_key_path = _LEGACY_ROOT / "vbmeta" / "testkey_rsa2048.pem"
    vbmeta_tmp = images_dir / "vbmeta_patched.img"
    openssl_bin_dir = _LEGACY_ROOT / "bin" / "openssl"
    openssl_exe = openssl_bin_dir / "openssl.exe"

    vbmeta_files_found = [
        str(path) for path in sorted(images_dir.glob("vbmeta*.img"))
    ] if images_dir.is_dir() else []

    patched_files: list[str] = []
    skipped_items: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    if not images_dir.is_dir():
        skipped_items.append(f"images directory not found: {images_dir}")
    if not vbmeta_img.is_file():
        skipped_items.append(f"vbmeta.img not found in images: {images_dir}")
    if not avbtool_path.is_file():
        errors.append(f"avbtool not found: {avbtool_path}")
    if not avb_key_path.is_file():
        errors.append(f"AVB key not found: {avb_key_path}")
    if not openssl_exe.is_file():
        errors.append(f"openssl.exe not found in: {openssl_bin_dir}")

    selected_mode = str(vbmeta_mode) if vbmeta_mode is not None else None
    if selected_mode not in (None, "", "3"):
        warnings.append(
            f"vbmeta_mode '{selected_mode}' recorded only; legacy patch command is unchanged"
        )

    would_patch = images_dir.is_dir() and vbmeta_img.is_file() and not errors

    if not execute:
        print(f"[images] Dry-run: vbmeta files found: {len(vbmeta_files_found)}")
        return {
            "status": "DRY_RUN",
            "images_dir": str(images_dir),
            "vbmeta_mode": selected_mode,
            "vbmeta_files_found": vbmeta_files_found,
            "would_patch": would_patch,
            "patched_vbmeta_files": patched_files,
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    if skipped_items or errors:
        return {
            "status": "FAILED" if errors else "APPLIED",
            "images_dir": str(images_dir),
            "vbmeta_mode": selected_mode,
            "vbmeta_files_found": vbmeta_files_found,
            "would_patch": False,
            "patched_vbmeta_files": patched_files,
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    print("[images] Patching vbmeta.img with legacy avbtool command.")
    try:
        if vbmeta_tmp.exists():
            remove_path_force(vbmeta_tmp)

        before_size = vbmeta_img.stat().st_size
        cmd = [
            sys.executable,
            str(avbtool_path),
            "make_vbmeta_image",
            "--output",
            str(vbmeta_tmp),
            "--algorithm",
            "SHA256_RSA2048",
            "--key",
            str(avb_key_path),
            "--include_descriptors_from_image",
            str(vbmeta_img),
            "--padding_size",
            "4096",
            "--set_hashtree_disabled_flag",
        ]
        env = os.environ.copy()
        env["PATH"] = str(openssl_bin_dir) + os.pathsep + env.get("PATH", "")
        subprocess.run(cmd, check=True, cwd=str(_LEGACY_ROOT / "vbmeta"), env=env)
        shutil.move(str(vbmeta_tmp), str(vbmeta_img))
        after_size = vbmeta_img.stat().st_size
        patched_files.append(str(vbmeta_img))
        print(f"[images] vbmeta patched: {vbmeta_img.name}")
        status = "APPLIED"
    except subprocess.CalledProcessError as exc:
        before_size = None
        after_size = None
        errors.append(f"vbmeta patch exit code {exc.returncode}")
        status = "FAILED"
    except Exception as exc:
        before_size = None
        after_size = None
        errors.append(f"vbmeta patch: {exc}")
        status = "FAILED"
    finally:
        if vbmeta_tmp.exists():
            remove_path_force(vbmeta_tmp)

    return {
        "status": status,
        "images_dir": str(images_dir),
        "vbmeta_mode": selected_mode,
        "vbmeta_files_found": vbmeta_files_found,
        "would_patch": False,
        "patched_vbmeta_files": patched_files,
        "skipped_items": skipped_items,
        "warnings": warnings,
        "errors": errors,
        "before_size": before_size,
        "after_size": after_size,
    }

