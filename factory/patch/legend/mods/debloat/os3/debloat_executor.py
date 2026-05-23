"""
Legend OS3 Debloat Executor.

Reads debloat_manifest.yml and applies CN-to-Global debloat/conversion
operations to an unpacked ROM root.

Safety contract:
  - Operates ONLY inside the unpacked ROM root.
  - Never deletes, moves, or renames anything outside the ROM root.
  - Validates every path before touching it.
  - Blocks path traversal (../ patterns and absolute paths outside root).
  - Missing files/folders are skipped — never fatal.
  - Every action is logged to stdout and written to the patch report.
  - dry_run=True  → no file-system changes whatsoever.
  - dry_run=False → execute mode; changes are real and irreversible.

Execution order (matches manifest execution_order section):
  1.  Guard: verify Legend OS3 profile.
  2.  Load manifest.
  3.  Validate ROM root.
  4.  Initialise report writer.
  5-6. Move mi_ext useful content (permissions, messaging, framework, overlay).
  7.  Remove unwanted mi_ext folders.
  8.  Filter product/data-app (remove CN packages).
  9.  Move remaining product/data-app → product/app.
  10. Run rename_paths.
  11. Run remove_paths.
  12. Run remove_packages (product/app, product/priv-app, system/app).
  13. Run clean_patterns (if options enabled).
  14. Run overlay_patches (log WARNING if APKEditor unavailable).
  15. Write final report.

CLI:
  # dry-run (default — nothing is changed):
  python -m factory.patch.legend.mods.debloat.os3.debloat_executor \\
      --project path/to/unpacked_rom \\
      --flavor legend \\
      --os-family OS3

  # execute:
  python -m factory.patch.legend.mods.debloat.os3.debloat_executor \\
      --project path/to/unpacked_rom \\
      --flavor legend \\
      --os-family OS3 \\
      --execute
"""
from __future__ import annotations

import argparse
import fnmatch
import os
import shutil
import stat
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore[assignment]

from factory.patch.legend.mods.debloat.os3.legend_profile import guard as _profile_guard

_MANIFEST_PATH = Path(__file__).with_name("debloat_manifest.yml")
_REPO_ROOT = Path(__file__).resolve().parents[6]
_REPORTS_DIR = _REPO_ROOT / "output" / "reports"


# ── report container ──────────────────────────────────────────────────────────

@dataclass
class _DebloatReport:
    profile_name: str = "legend_os3_debloat"
    rom_root: str = ""
    mode: str = "dry-run"
    timestamp: str = ""
    removed: list[str] = field(default_factory=list)
    moved: list[str] = field(default_factory=list)
    renamed: list[str] = field(default_factory=list)
    patched: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    protected: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


# ── path safety ───────────────────────────────────────────────────────────────

def _resolved_safe(rom_root: Path, rel: str) -> Path | None:
    """Resolve *rel* under *rom_root* and return None if it escapes the root."""
    try:
        target = (rom_root / rel).resolve()
        target.relative_to(rom_root.resolve())
        return target
    except (ValueError, OSError):
        return None


def _is_traversal(rom_root: Path, rel: str) -> bool:
    """Return True when *rel* would escape *rom_root*."""
    return _resolved_safe(rom_root, rel) is None


def _is_absolute_escape(rel: str) -> bool:
    """Return True when *rel* is an absolute path string."""
    p = Path(rel)
    return p.is_absolute()


def _path_is_safe(rom_root: Path, rel: str) -> bool:
    """Return True only when *rel* is safe to use inside *rom_root*."""
    if not rel or _is_absolute_escape(rel):
        return False
    return not _is_traversal(rom_root, rel)


# ── filesystem helpers ────────────────────────────────────────────────────────

def _del_rw(target: str) -> None:
    try:
        os.chmod(target, stat.S_IWRITE)
    except OSError:
        pass
    os.remove(target)


def _remove_force(path: Path) -> bool:
    """Remove *path* (file or directory tree).  Returns True when gone."""
    if not path.exists() and not path.is_symlink():
        return True
    try:
        if path.is_file() or path.is_symlink():
            _del_rw(str(path))
        else:
            shutil.rmtree(path, onerror=lambda _fn, fp, __: _del_rw(fp))
    except Exception:
        pass
    if path.exists() and os.name == "nt":
        os.system(f'cmd /c rd /s /q "{path}" >nul 2>nul')
    return not path.exists()


def _move(src: Path, dst: Path, *, merge: bool = False) -> bool:
    """Move *src* to *dst*.

    When merge=True and both are directories, copy contents of *src* into
    *dst* without overwriting existing files, then delete *src*.
    """
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    if merge and src.is_dir() and dst.is_dir():
        for item in list(src.iterdir()):
            item_dst = dst / item.name
            if item_dst.exists():
                continue
            shutil.move(str(item), str(item_dst))
        _remove_force(src)
        return True
    if dst.exists():
        _remove_force(dst)
    shutil.move(str(src), str(dst))
    return not src.exists()


# ── protected path check ──────────────────────────────────────────────────────

def _is_protected(rel: str, patterns: list[str]) -> bool:
    norm = rel.replace("\\", "/")
    for pat in patterns:
        if fnmatch.fnmatch(norm, pat.replace("\\", "/")):
            return True
    return False


# ── YAML loader ───────────────────────────────────────────────────────────────

def _load_yaml(path: Path) -> dict:
    if yaml is None:
        raise RuntimeError(
            "PyYAML is not installed.  Run: pip install pyyaml"
        )
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return data if isinstance(data, dict) else {}


# ── main executor class ───────────────────────────────────────────────────────

class LegendOS3DebloatExecutor:
    """Apply the Legend OS3 debloat profile to an unpacked ROM root.

    Parameters
    ----------
    rom_root:
        Absolute path to the unpacked ROM (e.g. ``output/work/project``).
    flavor:
        Build flavor string (e.g. ``"legend"``).
    os_family:
        OS family string (e.g. ``"OS3"`` or ``"HyperOS3"``).
    debloat_profile:
        Profile selector string — must be ``"legend_os3"``.
    execute:
        ``True`` → apply changes; ``False`` → dry-run (default).
    manifest_path:
        Override the manifest YAML path (used in tests).
    """

    def __init__(
        self,
        rom_root: Path,
        flavor: str = "legend",
        os_family: str = "OS3",
        debloat_profile: str = "legend_os3",
        execute: bool = False,
        manifest_path: Path | None = None,
    ) -> None:
        self.rom_root = Path(rom_root).resolve()
        self.flavor = flavor
        self.os_family = os_family
        self.debloat_profile = debloat_profile
        self.execute = execute
        self.manifest_path = manifest_path or _MANIFEST_PATH
        self._manifest: dict[str, Any] = {}
        self._protected_patterns: list[str] = []
        self._report = _DebloatReport(
            rom_root=str(self.rom_root),
            mode="execute" if execute else "dry-run",
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%S"),
        )

    # ── public entry point ────────────────────────────────────────────────────

    def run(self) -> dict:
        """Execute the debloat profile.  Returns a result dict suitable for
        the pipeline orchestrator."""

        # Step 1 — guard
        try:
            _profile_guard(self.flavor, self.os_family, self.debloat_profile)
        except ValueError as exc:
            msg = str(exc)
            print(msg)
            return self._skip(msg)

        print(f"[LEGEND OS3] Running Legend OS3 Debloat Profile "
              f"(mode={self._report.mode})")

        # Step 2 — load manifest
        try:
            self._manifest = _load_yaml(self.manifest_path)
        except Exception as exc:
            return self._fail(f"Failed to load manifest: {exc}")

        # Step 3 — validate ROM root
        if not self.rom_root.is_dir():
            return self._fail(f"ROM root does not exist: {self.rom_root}")

        # Step 4 — build protected patterns index
        self._protected_patterns = [
            entry["pattern"]
            for entry in self._manifest.get("protected_paths", [])
            if isinstance(entry, dict) and "pattern" in entry
        ]

        # Steps 5-6 — move mi_ext useful content first
        self._stage_move_paths()

        # Steps 8-9 — filter product/data-app then move remainder
        self._stage_data_app_filter_and_move()

        # Step 10 — rename_paths
        self._stage_rename_paths()

        # Step 11 — remove_paths
        self._stage_remove_paths()

        # Step 12 — remove_packages
        self._stage_remove_packages()

        # Step 13 — clean_patterns
        self._stage_clean_patterns()

        # Step 14 — overlay_patches
        self._stage_overlay_patches()

        # Step 15 — write report
        self._write_report()

        return self._build_result()

    # ── stage: move_paths ─────────────────────────────────────────────────────

    def _stage_move_paths(self) -> None:
        for entry in self._manifest.get("move_paths", []):
            if not isinstance(entry, dict):
                continue
            src_rel = entry.get("src", "")
            dst_rel = entry.get("dst", "")
            merge = bool(entry.get("merge", False))
            note = entry.get("note", "")

            if not _path_is_safe(self.rom_root, src_rel):
                self._warn(f"BLOCKED path traversal in move src: {src_rel!r}")
                continue
            if not _path_is_safe(self.rom_root, dst_rel):
                self._warn(f"BLOCKED path traversal in move dst: {dst_rel!r}")
                continue
            if _is_protected(src_rel, self._protected_patterns):
                self._protect(src_rel, note)
                continue

            src = _resolved_safe(self.rom_root, src_rel)
            dst = _resolved_safe(self.rom_root, dst_rel)
            if src is None or dst is None:
                continue

            if not src.exists():
                self._skip_path("MOVE", src_rel)
                continue

            label = "MOVE" if self.execute else "DRY-MOVE"
            print(f"[LEGEND OS3][{label}] {src_rel} -> {dst_rel}")
            if self.execute:
                ok = _move(src, dst, merge=merge)
                if ok:
                    self._report.moved.append(f"{src_rel} -> {dst_rel}")
                else:
                    self._warn(f"MOVE FAILED: {src_rel} -> {dst_rel}")
            else:
                self._report.moved.append(f"[DRY] {src_rel} -> {dst_rel}")

    # ── stage: rename_paths ───────────────────────────────────────────────────

    def _stage_rename_paths(self) -> None:
        for entry in self._manifest.get("rename_paths", []):
            if not isinstance(entry, dict):
                continue
            src_rel = entry.get("src", "")
            dst_rel = entry.get("dst", "")
            note = entry.get("note", "")

            if not _path_is_safe(self.rom_root, src_rel):
                self._warn(f"BLOCKED traversal in rename src: {src_rel!r}")
                continue
            if not _path_is_safe(self.rom_root, dst_rel):
                self._warn(f"BLOCKED traversal in rename dst: {dst_rel!r}")
                continue
            if _is_protected(src_rel, self._protected_patterns):
                self._protect(src_rel, note)
                continue

            src = _resolved_safe(self.rom_root, src_rel)
            dst = _resolved_safe(self.rom_root, dst_rel)
            if src is None or dst is None:
                continue

            if not src.exists():
                self._skip_path("RENAME", src_rel)
                continue

            label = "RENAME" if self.execute else "DRY-RENAME"
            print(f"[LEGEND OS3][{label}] {src_rel} -> {dst_rel}")
            if self.execute:
                ok = _move(src, dst, merge=False)
                if ok:
                    self._report.renamed.append(f"{src_rel} -> {dst_rel}")
                else:
                    self._warn(f"RENAME FAILED: {src_rel} -> {dst_rel}")
            else:
                self._report.renamed.append(f"[DRY] {src_rel} -> {dst_rel}")

    # ── stage: remove_paths ───────────────────────────────────────────────────

    def _stage_remove_paths(self) -> None:
        for entry in self._manifest.get("remove_paths", []):
            rel = entry.get("path", "") if isinstance(entry, dict) else str(entry)
            note = entry.get("note", "") if isinstance(entry, dict) else ""
            if not rel:
                continue

            if not _path_is_safe(self.rom_root, rel):
                self._warn(f"BLOCKED traversal in remove: {rel!r}")
                continue
            if _is_protected(rel, self._protected_patterns):
                self._protect(rel, note)
                continue

            target = _resolved_safe(self.rom_root, rel)
            if target is None:
                continue

            if not target.exists():
                self._skip_path("REMOVE", rel)
                continue

            label = "REMOVE" if self.execute else "DRY-REMOVE"
            print(f"[LEGEND OS3][{label}] {rel}")
            if self.execute:
                ok = _remove_force(target)
                if ok:
                    self._report.removed.append(rel)
                else:
                    self._warn(f"REMOVE FAILED: {rel}")
            else:
                self._report.removed.append(f"[DRY] {rel}")

    # ── stage: remove_packages ────────────────────────────────────────────────

    def _stage_remove_packages(self) -> None:
        packages: dict = self._manifest.get("remove_packages", {})
        if not isinstance(packages, dict):
            return
        # product/data-app packages are handled in _stage_data_app_filter_and_move
        skip_partitions = {"product/data-app"}
        for partition_rel, pkg_list in packages.items():
            if partition_rel in skip_partitions:
                continue
            if not isinstance(pkg_list, list):
                continue
            for pkg in pkg_list:
                rel = f"{partition_rel}/{pkg}"
                if not _path_is_safe(self.rom_root, rel):
                    self._warn(f"BLOCKED traversal in package remove: {rel!r}")
                    continue
                if _is_protected(rel, self._protected_patterns):
                    self._protect(rel, "package")
                    continue
                target = _resolved_safe(self.rom_root, rel)
                if target is None:
                    continue
                if not target.exists():
                    self._skip_path("PKG-REMOVE", rel)
                    continue
                label = "REMOVE-PKG" if self.execute else "DRY-REMOVE-PKG"
                print(f"[LEGEND OS3][{label}] {rel}")
                if self.execute:
                    ok = _remove_force(target)
                    if ok:
                        self._report.removed.append(f"[pkg] {rel}")
                    else:
                        self._warn(f"PKG REMOVE FAILED: {rel}")
                else:
                    self._report.removed.append(f"[DRY][pkg] {rel}")

    # ── stage: data-app filter then move ─────────────────────────────────────

    def _stage_data_app_filter_and_move(self) -> None:
        cfg = self._manifest.get("move_data_app_to_app", {})
        if not isinstance(cfg, dict) or not cfg.get("enabled", False):
            self._report.skipped.append("move_data_app_to_app: disabled in manifest")
            return

        src_rel = cfg.get("src", "product/data-app")
        dst_rel = cfg.get("dst", "product/app")

        if not _path_is_safe(self.rom_root, src_rel):
            self._warn(f"BLOCKED traversal in data-app src: {src_rel!r}")
            return
        if not _path_is_safe(self.rom_root, dst_rel):
            self._warn(f"BLOCKED traversal in data-app dst: {dst_rel!r}")
            return

        src_dir = _resolved_safe(self.rom_root, src_rel)
        dst_dir = _resolved_safe(self.rom_root, dst_rel)
        if src_dir is None or dst_dir is None:
            return

        if not src_dir.is_dir():
            self._report.skipped.append(f"DATA-APP SKIP (missing): {src_rel}")
            return

        # Step 8 — filter: remove unwanted CN data-app packages first
        data_app_removes: set[str] = set(
            self._manifest.get("remove_packages", {}).get("product/data-app", [])
        )
        for item in list(src_dir.iterdir()):
            if item.name not in data_app_removes:
                continue
            rel = f"{src_rel}/{item.name}"
            if _is_protected(rel, self._protected_patterns):
                self._protect(rel, "data-app filter")
                continue
            label = "FILTER-DATA-APP" if self.execute else "DRY-FILTER-DATA-APP"
            print(f"[LEGEND OS3][{label}] {rel}")
            if self.execute:
                ok = _remove_force(item)
                if ok:
                    self._report.removed.append(f"[data-app filter] {rel}")
                else:
                    self._warn(f"FILTER FAILED: {rel}")
            else:
                self._report.removed.append(f"[DRY][data-app filter] {rel}")

        # Step 9 — move remaining data-app entries to product/app
        if not src_dir.is_dir():
            return
        if self.execute:
            dst_dir.mkdir(parents=True, exist_ok=True)
        for item in list(src_dir.iterdir()):
            item_dst = dst_dir / item.name
            if item_dst.exists():
                self._report.skipped.append(
                    f"DATA-APP MOVE SKIP (dst exists): {item.name}"
                )
                continue
            label = "MOVE-DATA-APP" if self.execute else "DRY-MOVE-DATA-APP"
            print(f"[LEGEND OS3][{label}] {src_rel}/{item.name} -> {dst_rel}/{item.name}")
            if self.execute:
                shutil.move(str(item), str(item_dst))
                self._report.moved.append(
                    f"[data-app] {src_rel}/{item.name} -> {dst_rel}/{item.name}"
                )
            else:
                self._report.moved.append(
                    f"[DRY][data-app] {src_rel}/{item.name} -> {dst_rel}/{item.name}"
                )

    # ── stage: clean_patterns ─────────────────────────────────────────────────

    def _stage_clean_patterns(self) -> None:
        cp = self._manifest.get("clean_patterns", {})
        if not isinstance(cp, dict):
            return
        options: dict = cp.get("options", {})
        patterns: list = cp.get("patterns", [])

        for entry in patterns:
            if not isinstance(entry, dict):
                continue
            ext = entry.get("ext", "")
            option_key = entry.get("option", "")
            if not options.get(option_key, False):
                self._report.skipped.append(
                    f"CLEAN SKIP (disabled): {ext!r} ({option_key}=false)"
                )
                continue
            for partition in entry.get("partitions", []):
                part_path = _resolved_safe(self.rom_root, str(partition))
                if part_path is None or not part_path.is_dir():
                    continue
                for match in part_path.rglob(ext):
                    if not match.is_file():
                        continue
                    rel = str(match.relative_to(self.rom_root))
                    label = "CLEAN" if self.execute else "DRY-CLEAN"
                    print(f"[LEGEND OS3][{label}] {rel}")
                    if self.execute:
                        ok = _remove_force(match)
                        if ok:
                            self._report.removed.append(f"[clean] {rel}")
                    else:
                        self._report.removed.append(f"[DRY][clean] {rel}")

    # ── stage: overlay_patches ────────────────────────────────────────────────

    def _stage_overlay_patches(self) -> None:
        for entry in self._manifest.get("overlay_patches", []):
            if not isinstance(entry, dict):
                continue
            target_rel = entry.get("target", "")
            resource_name = entry.get("resource_name", "")
            old_value = entry.get("old_value", "")
            new_value = entry.get("new_value", "")
            note = entry.get("note", "")
            msg = (
                f"GestureLineOverlay patch requested "
                f"({resource_name}: {old_value!r} -> {new_value!r}) "
                f"but APK resource patching is not available yet. [{note}]"
            )
            self._warn(msg)

    # ── report writer ─────────────────────────────────────────────────────────

    def _write_report(self) -> None:
        _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        report_path = _REPORTS_DIR / "deadzone_patch_report.txt"

        def _section(title: str, items: list[str]) -> list[str]:
            lines = [f"\n[{title}]"]
            lines += [f"  {x}" for x in items] if items else ["  (none)"]
            return lines

        lines: list[str] = [
            "[LEGEND OS3 PATCH PROFILE]",
            f"  profile   : {self._report.profile_name}",
            f"  rom_root  : {self._report.rom_root}",
            f"  mode      : {self._report.mode}",
            f"  timestamp : {self._report.timestamp}",
        ]
        lines += _section("REMOVED",   self._report.removed)
        lines += _section("MOVED",     self._report.moved)
        lines += _section("RENAMED",   self._report.renamed)
        lines += _section("PATCHED",   self._report.patched)
        lines += _section("SKIPPED",   self._report.skipped)
        lines += _section("PROTECTED", self._report.protected)
        lines += _section("WARNINGS",  self._report.warnings)
        lines += _section("ERRORS",    self._report.errors)

        report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"[LEGEND OS3] Report written: {report_path}")

    # ── result builders ───────────────────────────────────────────────────────

    def _skip(self, reason: str) -> dict:
        return {
            "stage": "legend_os3_debloat",
            "status": "SKIPPED",
            "final_status": "SKIPPED",
            "warnings": [reason],
            "errors": [],
        }

    def _fail(self, reason: str) -> dict:
        self._report.errors.append(reason)
        print(f"[LEGEND OS3][ERROR] {reason}")
        return {
            "stage": "legend_os3_debloat",
            "status": "FAILED",
            "final_status": "FAILED",
            "warnings": list(self._report.warnings),
            "errors": list(self._report.errors),
        }

    def _build_result(self) -> dict:
        has_errors = bool(self._report.errors)
        if has_errors:
            status = "FAILED"
        elif self.execute:
            status = "APPLIED"
        else:
            status = "DRY_RUN"
        return {
            "stage": "legend_os3_debloat",
            "profile": self._report.profile_name,
            "mode": self._report.mode,
            "rom_root": self._report.rom_root,
            "timestamp": self._report.timestamp,
            "removed_count": len(self._report.removed),
            "moved_count": len(self._report.moved),
            "renamed_count": len(self._report.renamed),
            "patched_count": len(self._report.patched),
            "skipped_count": len(self._report.skipped),
            "protected_count": len(self._report.protected),
            "removed": list(self._report.removed),
            "moved": list(self._report.moved),
            "renamed": list(self._report.renamed),
            "patched": list(self._report.patched),
            "skipped": list(self._report.skipped),
            "protected": list(self._report.protected),
            "warnings": list(self._report.warnings),
            "errors": list(self._report.errors),
            "status": status,
            "final_status": status,
            "report_files": {
                "txt": str(_REPORTS_DIR / "deadzone_patch_report.txt"),
            },
        }

    # ── small helpers ─────────────────────────────────────────────────────────

    def _skip_path(self, action: str, rel: str) -> None:
        msg = f"{action} SKIP (missing): {rel}"
        self._report.skipped.append(msg)

    def _protect(self, rel: str, reason: str) -> None:
        msg = f"PROTECTED: {rel}" + (f" — {reason}" if reason else "")
        self._report.protected.append(msg)
        print(f"[LEGEND OS3][PROTECTED] {msg}")

    def _warn(self, msg: str) -> None:
        self._report.warnings.append(msg)
        print(f"[LEGEND OS3][WARN] {msg}")


# ── public convenience function ───────────────────────────────────────────────

def apply_legend_os3_debloat(
    project_dir: Path,
    flavor: str = "legend",
    os_family: str = "OS3",
    debloat_profile: str = "legend_os3",
    execute: bool = False,
) -> dict:
    """Entry point for the pipeline orchestrator.

    Returns a dict with ``final_status`` in
    ``{"APPLIED", "DRY_RUN", "SKIPPED", "FAILED"}``.
    """
    executor = LegendOS3DebloatExecutor(
        rom_root=project_dir,
        flavor=flavor,
        os_family=os_family,
        debloat_profile=debloat_profile,
        execute=execute,
    )
    return executor.run()


# ── CLI ───────────────────────────────────────────────────────────────────────

def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Legend OS3 debloat executor — CN-to-Global ROM conversion"
    )
    p.add_argument("--project", type=Path, required=True,
                   help="Path to the unpacked ROM root")
    p.add_argument("--flavor", default="legend",
                   help="Build flavor (default: legend)")
    p.add_argument("--os-family", dest="os_family", default="OS3",
                   help="OS family (default: OS3)")
    p.add_argument("--debloat-profile", dest="debloat_profile",
                   default="legend_os3",
                   help="Debloat profile key (default: legend_os3)")
    p.add_argument("--execute", action="store_true",
                   help="Apply changes (default: dry-run)")
    return p


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    result = apply_legend_os3_debloat(
        project_dir=args.project,
        flavor=args.flavor,
        os_family=args.os_family,
        debloat_profile=args.debloat_profile,
        execute=args.execute,
    )
    status = result.get("final_status", "FAILED")
    print(f"[LEGEND OS3] final_status={status}")
    return 0 if status in {"APPLIED", "DRY_RUN", "SKIPPED"} else 1


if __name__ == "__main__":
    sys.exit(main())
