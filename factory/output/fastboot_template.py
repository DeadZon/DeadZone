from __future__ import annotations

import shutil
import zipfile
from pathlib import Path


REQUIRED_BIN_FILES = [
    "fastboot.exe",
    "AdbWinApi.dll",
    "AdbWinUsbApi.dll",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _find_default_template_dir() -> Path | None:
    root = _repo_root()
    candidates = [
        root / "DeadZone Fastboot Script",
        root / "templates" / "DeadZone Fastboot Script",
        root / "templates" / "fastboot",
    ]
    for candidate in candidates:
        if all((candidate / "bin" / "windows" / name).is_file() for name in REQUIRED_BIN_FILES):
            return candidate
    legacy = root / "third_party" / "mezo_core" / "flash"
    if all((legacy / "META-INF" / "windows" / name).is_file() for name in REQUIRED_BIN_FILES):
        return legacy
    return None


def _zip_member_for(zf: zipfile.ZipFile, wanted: str) -> str | None:
    wanted_path = f"bin/windows/{wanted}".lower()
    legacy_path = f"meta-inf/windows/{wanted}".lower()
    for name in zf.namelist():
        normalized = name.replace("\\", "/").lower()
        if normalized.endswith(wanted_path) or normalized.endswith(legacy_path):
            return name
    return None


def _dir_source_file(template_dir: Path, wanted: str) -> Path | None:
    direct = template_dir / "bin" / "windows" / wanted
    if direct.is_file():
        return direct
    legacy = template_dir / "META-INF" / "windows" / wanted
    if legacy.is_file():
        return legacy
    return None


def prepare_fastboot_template(
    output_dir: Path,
    template_zip: Path | None = None,
    template_dir: Path | None = None,
    execute: bool = False,
) -> dict:
    output_dir = Path(output_dir)
    template_zip = Path(template_zip) if template_zip else None
    template_dir = Path(template_dir) if template_dir else None
    files_copied: list[str] = []
    errors: list[str] = []
    warnings: list[str] = []
    source = None
    source_type = None

    if template_zip and template_zip.is_file():
        source = template_zip
        source_type = "zip"
    else:
        if template_zip:
            warnings.append(f"Template ZIP not found: {template_zip}")
        if not template_dir:
            template_dir = _find_default_template_dir()
        if template_dir and template_dir.is_dir():
            source = template_dir
            source_type = "dir"

    if source is None:
        errors.append("SKIPPED_MISSING_TEMPLATE: no DeadZone fastboot template assets found")
        return {
            "status": "FAILED" if execute else "SKIPPED_MISSING_TEMPLATE",
            "template_source": None,
            "files_copied": files_copied,
            "warnings": warnings,
            "errors": errors,
        }

    missing: list[str] = []
    if source_type == "zip":
        with zipfile.ZipFile(source, "r") as zf:
            members = {name: _zip_member_for(zf, name) for name in REQUIRED_BIN_FILES}
            missing = [name for name, member in members.items() if member is None]
            if execute and not missing:
                target_dir = output_dir / "bin" / "windows"
                target_dir.mkdir(parents=True, exist_ok=True)
                for name, member in members.items():
                    assert member is not None
                    with zf.open(member) as src, (target_dir / name).open("wb") as dst:
                        shutil.copyfileobj(src, dst)
                    files_copied.append(f"bin/windows/{name}")
    else:
        sources = {name: _dir_source_file(source, name) for name in REQUIRED_BIN_FILES}
        missing = [name for name, path in sources.items() if path is None]
        if execute and not missing:
            target_dir = output_dir / "bin" / "windows"
            target_dir.mkdir(parents=True, exist_ok=True)
            for name, src in sources.items():
                assert src is not None
                shutil.copy2(src, target_dir / name)
                files_copied.append(f"bin/windows/{name}")

    if missing:
        errors.append("Missing template assets: " + ", ".join(missing))
        status = "FAILED"
    else:
        if not execute:
            files_copied = [f"bin/windows/{name}" for name in REQUIRED_BIN_FILES]
        if execute:
            (output_dir / "images").mkdir(parents=True, exist_ok=True)
        status = "APPLIED" if execute else "DRY_RUN"

    return {
        "status": status,
        "template_source": str(source),
        "files_copied": files_copied,
        "warnings": warnings,
        "errors": errors,
    }

