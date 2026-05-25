"""
Common ROM project-level legacy patches.

Carries exact behavior of MEZOBuildRom.py functions:
  - read_debloat_list(debloat_path)          lines 610-627
  - _safe_collect_dirs(project_dir)          lines 630-646
  - debloat_project(project_dir, debloat_path) lines 649-680
  - resolve_partition_root(project_dir, partition_name) lines 683-691
  - resolve_partition_file(project_dir, partition_name, *parts) lines 694-698
  - clean_system_framework_arch_dirs(project_dir) lines 5594-5618
  - move_product_data_app_to_app(project_dir) lines 5212-5249
  - remove_path_force(path)                  lines 107-130
  - apply_language_overlay(project_dir, mi_incremental) lines 6033-6071

Allowed changes from source:
  - log() -> print()  (log was just print in MEZOBuildRom.py)
  - ROOT_DIR / script_dir references -> _LEGACY_ROOT (module-path fix)
  - imports added
  - report wrapper before/after execution

Not changed:
  - logic, strings, regex, target files, smali paths, conditions, algorithm

CLI:
  # dry-run:
  python -m factory.patch.common_rom.project_legacy \\
      --project "path/to/unpacked_project" \\
      --flavor legend \\
      --mi-version OS3.0.303.0.WNOCNXM

  # execute:
  python -m factory.patch.common_rom.project_legacy \\
      --project "path/to/unpacked_project" \\
      --flavor legend \\
      --mi-version OS3.0.303.0.WNOCNXM \\
      --execute
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import stat
import sys
from pathlib import Path

# _LEGACY_ROOT = third_party/mezo_core (where MEZO_OVERLAY/ lives)
_LEGACY_ROOT = Path(__file__).resolve().parents[3] / "third_party" / "mezo_core"

_REPO_ROOT   = Path(__file__).resolve().parents[3]
_OUTPUT_ROOT = _REPO_ROOT / "output"
_REPORTS_DIR = _OUTPUT_ROOT / "reports"

_LEGEND_FLAVORS = {"legend", "deadzone_legend"}


# ── helpers ───────────────────────────────────────────────────────────────────
# Exact copy of MEZOBuildRom.py:remove_path_force (lines 107-130)
def remove_path_force(path: Path) -> bool:
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


# Exact copy of MEZOBuildRom.py:resolve_partition_root (lines 683-691)
def resolve_partition_root(project_dir: Path, partition_name: str) -> Path | None:
    direct_root = project_dir / partition_name
    nested_root = direct_root / partition_name

    if nested_root.is_dir():
        return nested_root
    if direct_root.is_dir():
        return direct_root
    return None


# Exact copy of MEZOBuildRom.py:resolve_partition_file (lines 694-698)
def resolve_partition_file(project_dir: Path, partition_name: str, *parts: str) -> Path | None:
    partition_root = resolve_partition_root(project_dir, partition_name)
    if partition_root is None:
        return None
    return partition_root.joinpath(*parts)


# ── public legacy functions ────────────────────────────────────────────────────
# Exact copy of MEZOBuildRom.py:read_debloat_list (lines 610-627)
def read_debloat_list(debloat_path: Path) -> list[str]:
    names: list[str] = []

    if not debloat_path.is_file():
        print(f"Debloat file not found: {debloat_path}")
        return names

    try:
        with debloat_path.open("r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                name = line.strip()
                if not name or name.startswith("#"):
                    continue
                names.append(name)
    except Exception as exc:
        print(f"Error reading debloat list: {exc}")

    return names


# Exact copy of MEZOBuildRom.py:_safe_collect_dirs (lines 630-646)
def _safe_collect_dirs(project_dir: Path) -> list[Path]:
    dirs: list[Path] = []

    def _onerror(_: OSError) -> None:
        return

    for root, dirnames, _filenames in os.walk(
        project_dir,
        topdown=True,
        followlinks=False,
        onerror=_onerror,
    ):
        root_path = Path(root)
        for dir_name in dirnames:
            dirs.append(root_path / dir_name)

    return dirs


# Exact copy of MEZOBuildRom.py:debloat_project (lines 649-680)
def debloat_project(project_dir: Path, debloat_path: Path) -> None:
    names = read_debloat_list(debloat_path)
    if not names:
        return

    print("Starting debloat from debloat.txt list...")

    # Thu thap truoc de tranh loi do vua duyet vua xoa.
    all_dirs = _safe_collect_dirs(project_dir)

    for name in names:
        print(f"- Searching and removing directories related to: {name}")
        found_any = False
        needle = name.lower()

        for path in all_dirs:
            try:
                if path.is_dir() and path.name.lower() == needle:
                    found_any = True
                    if remove_path_force(path):
                        print(f"    Removed: {path}")
                    else:
                        print(f"    Warning: could not remove {path}")
            except OSError as exc:
                print(f"    Skipping (inaccessible): {path} ({exc})")
            except Exception as exc:
                print(f"    Error removing {path}: {exc}")

        if not found_any:
            print("    No matching directories found.")

    print("Debloat complete.")


# Exact copy of MEZOBuildRom.py:clean_system_framework_arch_dirs (lines 5594-5618)
def clean_system_framework_arch_dirs(project_dir: Path) -> None:
    system_root = resolve_partition_root(project_dir, "system")
    if system_root is None:
        print("System partition not found; cannot clean framework arch directories.")
        return

    framework_dir = system_root / "framework"
    if not framework_dir.is_dir():
        print(f"Framework directory not found: {framework_dir}")
        return

    removed_any = False
    for dir_name in ("arm", "arm64", "oat"):
        target_dir = framework_dir / dir_name
        if not target_dir.exists():
            continue

        if remove_path_force(target_dir):
            print(f"    Removed framework/{dir_name}")
            removed_any = True
        else:
            print(f"    Warning: could not remove directory {target_dir}")

    if not removed_any:
        print("    No arm/arm64/oat directories in system/framework to remove.")


# Exact copy of MEZOBuildRom.py:move_product_data_app_to_app (lines 5212-5249)
def move_product_data_app_to_app(project_dir: Path) -> None:
    product_root = resolve_partition_root(project_dir, "product")
    if product_root is None:
        print("Product partition not found for data-app to app migration.")
        return

    data_app_dir = product_root / "data-app"
    app_dir = product_root / "app"

    if not data_app_dir.is_dir():
        print(f"Directory to move not found: {data_app_dir}")
        return

    entries = sorted(data_app_dir.iterdir(), key=lambda item: item.name.lower())
    if not entries:
        print("Khong co ung dung nao trong product/data-app de chuyen.")
        return

    app_dir.mkdir(parents=True, exist_ok=True)
    moved_count = 0

    for entry in entries:
        target_entry = app_dir / entry.name
        try:
            if target_entry.exists():
                if remove_path_force(target_entry):
                    print(f"    Da xoa muc trung ten tai dich: {target_entry}")
                else:
                    print(f"    Canh bao: khong xoa duoc muc trung ten tai dich: {target_entry}")
                    continue
            shutil.move(str(entry), str(target_entry))
            print(f"    Da chuyen {entry} -> {target_entry}")
            moved_count += 1
        except Exception as exc:
            print(f"    Loi khi chuyen {entry.name} sang product/app: {exc}")

    if moved_count == 0:
        print("Khong chuyen duoc muc nao tu product/data-app sang product/app.")


# Exact copy of MEZOBuildRom.py:apply_language_overlay (lines 6033-6071)
# Path fix: Path(__file__).parent -> _LEGACY_ROOT (where MEZO_OVERLAY/ lives)
def apply_language_overlay(project_dir: Path, mi_incremental: str) -> None:
    if not mi_incremental or len(mi_incremental) < 3:
        return

    prefix = mi_incremental[:3]
    script_dir = _LEGACY_ROOT
    src_dirs = []

    os_lang_dir = script_dir / "MEZO_OVERLAY" / f"{prefix}_language"
    if os_lang_dir.is_dir():
        src_dirs.append(os_lang_dir)

    common_overlay_dir = script_dir / "MEZO_OVERLAY" / "overlay"
    if common_overlay_dir.is_dir():
        src_dirs.append(common_overlay_dir)

    if not src_dirs:
        return

    dest_dir = resolve_partition_file(project_dir, "vendor", "overlay")
    if dest_dir is None:
        print("Vendor/overlay partition not found for overlay addition.")
        return

    dest_dir.mkdir(parents=True, exist_ok=True)
    print("Them cac goi overlay...")

    for src_dir in src_dirs:
        apk_files = list(src_dir.glob("*.apk"))
        if not apk_files:
            continue

        for apk in apk_files:
            try:
                target = dest_dir / apk.name
                shutil.copy2(apk, target)
                print(f"    Da them: {apk.name}")
            except Exception as exc:
                print(f"    Loi khi copy {apk}: {exc}")


# ── orchestrator ──────────────────────────────────────────────────────────────
def apply_common_project_legacy_patches(
    project_dir: Path,
    root_dir: Path,
    flavor: str,
    execute: bool = False,
    *,
    mi_incremental: str | None = None,
) -> dict:
    """
    Run (or dry-run) all common project-level legacy patches in order.

    Execute order (when execute=True):
      1. debloat_project(project_dir, root_dir / "debloat.txt")
      2. clean_system_framework_arch_dirs(project_dir)
      3. move_product_data_app_to_app(project_dir)
      4. if mi_incremental: apply_language_overlay(project_dir, mi_incremental)
    """
    debloat_path = root_dir / "debloat.txt"
    system_framework = None
    product_data_app = None

    # Determine input state for dry-run checks
    sys_root = resolve_partition_root(project_dir, "system")
    if sys_root is not None:
        fw = sys_root / "framework"
        system_framework = fw if fw.is_dir() else None

    prod_root = resolve_partition_root(project_dir, "product")
    if prod_root is not None:
        da = prod_root / "data-app"
        product_data_app = da if da.is_dir() else None

    overlay_src_exists = False
    if mi_incremental and len(mi_incremental) >= 3:
        prefix = mi_incremental[:3]
        overlay_src_exists = (
            (_LEGACY_ROOT / "MEZO_OVERLAY" / f"{prefix}_language").is_dir()
            or (_LEGACY_ROOT / "MEZO_OVERLAY" / "overlay").is_dir()
        )

    planned: list[str] = [
        "debloat_project",
        "clean_system_framework_arch_dirs",
        "move_product_data_app_to_app",
    ]
    if mi_incremental:
        planned.append("apply_language_overlay")

    warnings: list[str] = []
    errors: list[str] = []
    executed: list[str] = []
    skipped: list[dict] = []

    if not execute:
        # Dry-run checks
        if not debloat_path.is_file():
            warnings.append(f"debloat.txt not found at {debloat_path}")
        if system_framework is None:
            warnings.append("system/framework not found in project")
        if product_data_app is None:
            warnings.append("product/data-app not found in project")
        if mi_incremental and not overlay_src_exists:
            warnings.append(
                f"MEZO_OVERLAY source not found for prefix '{mi_incremental[:3]}'"
            )

        report = {
            "project_dir": str(project_dir),
            "flavor": flavor,
            "mi_incremental": mi_incremental,
            "dry_run": True,
            "functions_planned": planned,
            "functions_executed": [],
            "skipped_functions": skipped,
            "warnings": warnings,
            "errors": errors,
            "status": "DRY_RUN",
        }
        return report

    # Execute
    try:
        print("[common_rom] debloat_project ...")
        debloat_project(project_dir, debloat_path)
        executed.append("debloat_project")
    except Exception as exc:
        errors.append(f"debloat_project: {exc}")

    try:
        print("[common_rom] clean_system_framework_arch_dirs ...")
        clean_system_framework_arch_dirs(project_dir)
        executed.append("clean_system_framework_arch_dirs")
    except Exception as exc:
        errors.append(f"clean_system_framework_arch_dirs: {exc}")

    try:
        print("[common_rom] move_product_data_app_to_app ...")
        move_product_data_app_to_app(project_dir)
        executed.append("move_product_data_app_to_app")
    except Exception as exc:
        errors.append(f"move_product_data_app_to_app: {exc}")

    if mi_incremental:
        try:
            print(f"[common_rom] apply_language_overlay ({mi_incremental}) ...")
            apply_language_overlay(project_dir, mi_incremental)
            executed.append("apply_language_overlay")
        except Exception as exc:
            errors.append(f"apply_language_overlay: {exc}")
    else:
        skipped.append({"function": "apply_language_overlay", "reason": "mi_incremental not provided"})

    status = "FAILED" if errors else "APPLIED"

    report = {
        "project_dir": str(project_dir),
        "flavor": flavor,
        "mi_incremental": mi_incremental,
        "dry_run": False,
        "functions_planned": planned,
        "functions_executed": executed,
        "skipped_functions": skipped,
        "warnings": warnings,
        "errors": errors,
        "status": status,
    }
    return report


# ── report writer ──────────────────────────────────────────────────────────────
def _write_reports(report: dict) -> None:
    from factory.patch.common_rom.common_rom_report import write_common_rom_reports
    write_common_rom_reports(report, _REPORTS_DIR)


# ── CLI ────────────────────────────────────────────────────────────────────────
def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Common ROM project-level legacy patches (DeadZone factory)",
    )
    p.add_argument("--project", required=True, help="Path to unpacked project directory")
    p.add_argument("--flavor", required=True, help="ROM flavor (e.g. legend)")
    p.add_argument("--mi-version", dest="mi_version", default=None,
                   help="mi_incremental string (e.g. OS3.0.303.0.WNOCNXM)")
    p.add_argument("--execute", action="store_true",
                   help="Apply patches (default is dry-run)")
    return p


def _main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    project_dir = Path(args.project).resolve()
    if not project_dir.is_dir():
        print(f"[common_rom] ERROR: project directory not found: {project_dir}", file=sys.stderr)
        return 2

    root_dir = _REPO_ROOT
    mode = "EXECUTE" if args.execute else "DRY-RUN"
    print(f"[common_rom] mode={mode}  flavor={args.flavor}  project={project_dir}")

    report = apply_common_project_legacy_patches(
        project_dir=project_dir,
        root_dir=root_dir,
        mi_incremental=args.mi_version,
        flavor=args.flavor,
        execute=args.execute,
    )

    _write_reports(report)

    print(f"[common_rom] status={report['status']}")
    if report["warnings"]:
        for w in report["warnings"]:
            print(f"[common_rom] WARNING: {w}")
    if report["errors"]:
        for e in report["errors"]:
            print(f"[common_rom] ERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(_main())
