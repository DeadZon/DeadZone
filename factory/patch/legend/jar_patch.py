"""
Legend JAR patch orchestrator + CLI entry point.

Flow (execute mode):
  1. Guard: exit cleanly if flavor is not 'legend'.
  2. Locate MTCR directory.
  3. For each JAR rule:
     a. Copy JAR from project to workspace.
     b. Unpack JAR + baksmali all DEX files.
     c. Merge add.dex (if present) into new smali_classesN root.
     d. Apply MTCR patch pack (exact method/field block replacement / inject added classes).
     e. smali → DEX (repack_smali_to_dex).
     f. DEX → JAR (repack_dir_to_jar).
     g. Backup original JAR + restore rebuilt JAR to project.
  4. Write reports.

Flow (dry-run, default):
  - Steps 1–2 same.
  - For each JAR: locate jar, validate add.dex, parse MTCR, report intent.
  - No files modified.

CLI:
  python -m factory.patch.legend.jar_patch \\
      --project "path/to/unpacked_project" \\
      --flavor legend \\
      --execute          # omit for dry-run
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from factory.patch.common.jar_workspace import (
    backup_and_restore_jar,
    copy_jars_to_workspace,
    repack_dir_to_jar,
    repack_smali_to_dex,
    resolve_partition_file,
    unpack_dir_for,
    unpack_jar,
)
from factory.patch.common.mtcr_patch import parse_mtcr
from factory.patch.common.mtcr_exact_patcher import apply_exact_mtcr
from factory.patch.common.add_dex_merger import merge_add_dex
from factory.patch.common.patch_report import (
    JarReport,
    MtcrPackReport,
    PatchSession,
    write_reports,
)
from factory.patch.legend.jar_rules import (
    LEGEND_JAR_RULES,
    find_mtcr_dir,
    resolve_mtcr_path,
)
from factory.patch.legend.add_dex_rules import find_add_dex_for_jar

_REPO_ROOT    = Path(__file__).resolve().parents[3]
_OUTPUT_ROOT  = _REPO_ROOT / "output"
_REPORTS_DIR  = _OUTPUT_ROOT / "reports"
_LEGEND_FLAVOR = "legend"

# Canonical add.dex search dir (canonical first, fallback second)
_ADD_DEX_CANONICAL = _REPO_ROOT / "third_party" / "mezo_core" / "MEZO_LEGEND" / "jar"
_ADD_DEX_FALLBACK  = _REPO_ROOT / "Legend" / "jar"


def _add_dex_dir() -> Path:
    """Return directory to search for add.dex files."""
    if _ADD_DEX_CANONICAL.is_dir():
        return _ADD_DEX_CANONICAL
    return _ADD_DEX_FALLBACK


def _work_dir(project_dir: Path) -> Path:
    ts = time.strftime("%Y%m%d_%H%M%S")
    return _OUTPUT_ROOT / "work" / f"legend_jar_{ts}"


# ─────────────────────────────────────────────────────────────────────────────
class LegendJarPatcher:
    """
    Orchestrate the Legend JAR patch stage.

    Parameters
    ----------
    project_dir : Path
        The unpacked ROM project directory (output of the unpack stage).
    flavor : str
        Must be 'legend' to proceed; any other value exits clean with SKIPPED.
    dry_run : bool
        When True nothing is written; reports show WOULD_* intent statuses.
    """

    def __init__(
        self,
        project_dir: Path,
        *,
        flavor: str,
        dry_run: bool = True,
    ) -> None:
        self.project_dir = project_dir.resolve()
        self.flavor = flavor.lower()
        self.dry_run = dry_run
        self.work_dir = _work_dir(self.project_dir)
        self.backup_dir = self.work_dir / "backups"

    def run(self) -> PatchSession:
        # ── Guard: Legend-only ────────────────────────────────────────────────
        mtcr_dir = find_mtcr_dir() or Path("(not found)")
        session = PatchSession(
            flavor=self.flavor,
            dry_run=self.dry_run,
            project_dir=self.project_dir,
            work_dir=self.work_dir,
            patch_dir=mtcr_dir,
        )

        if self.flavor != _LEGEND_FLAVOR:
            msg = f"Flavor '{self.flavor}' is not 'legend'; JAR patch stage skipped."
            session.warnings.append(msg)
            print(f"[legend_jar] SKIPPED — {msg}")
            write_reports(session, _REPORTS_DIR)
            return session

        print(f"\n[legend_jar] ═══ Legend JAR Patch Stage ({'DRY RUN' if self.dry_run else 'EXECUTE'}) ═══")
        print(f"[legend_jar] Project  : {self.project_dir}")
        print(f"[legend_jar] Work dir : {self.work_dir}")

        # ── Locate MTCR packs ─────────────────────────────────────────────────
        mtcr_dir_real = find_mtcr_dir()
        if mtcr_dir_real is None:
            msg = "MTCR directory not found. Check Legend/jar/ or third_party/mezo_core/MEZO_LEGEND/jar/."
            session.errors.append(msg)
            print(f"[legend_jar] ERROR: {msg}")
            write_reports(session, _REPORTS_DIR)
            return session

        session.patch_dir = mtcr_dir_real
        print(f"[legend_jar] MTCR dir : {mtcr_dir_real}")

        add_dex_search = _add_dex_dir()
        print(f"[legend_jar] add.dex  : {add_dex_search}")

        # ── Create workspace ──────────────────────────────────────────────────
        if not self.dry_run:
            self.work_dir.mkdir(parents=True, exist_ok=True)
            self.backup_dir.mkdir(parents=True, exist_ok=True)

        # ── Process each JAR rule ─────────────────────────────────────────────
        for rule in LEGEND_JAR_RULES:
            jr = self._process_jar(rule, mtcr_dir_real, add_dex_search, session)
            session.jar_reports.append(jr)

        write_reports(session, _REPORTS_DIR)
        mode = "DRY RUN" if self.dry_run else "EXECUTE"
        print(f"[legend_jar] ═══ Legend JAR Patch complete [{mode}] ═══\n")
        return session

    def _process_jar(
        self,
        rule,
        mtcr_dir: Path,
        add_dex_search: Path,
        session: PatchSession,
    ) -> JarReport:
        jar_partition_path = f"{rule.jar_partition}/{rule.jar_rel_path}"
        jr = JarReport(
            jar_name=rule.jar_name,
            jar_partition_path=jar_partition_path,
            found=False,
        )

        # ── Locate JAR in project ─────────────────────────────────────────────
        parts = rule.jar_rel_path.split("/")
        project_jar = resolve_partition_file(self.project_dir, rule.jar_partition, *parts)
        if project_jar is None or not project_jar.is_file():
            jr.found = False
            session.warnings.append(f"{rule.jar_name}: not found in project")
            print(f"[legend_jar] NOT FOUND: {rule.jar_name}")
            return jr
        jr.found = True

        # ── Locate MTCR pack ──────────────────────────────────────────────────
        mtcr_path = resolve_mtcr_path(rule, mtcr_dir)
        if mtcr_path is None:
            jr.decompile_ok = False
            jr.decompile_errors.append(f"MTCR pack {rule.mtcr_filename} not found in {mtcr_dir}")
            session.warnings.append(f"{rule.jar_name}: MTCR pack missing ({rule.mtcr_filename})")
            print(f"[legend_jar] MTCR MISSING: {rule.mtcr_filename}")
            return jr

        # ── Parse MTCR ────────────────────────────────────────────────────────
        print(f"[legend_jar] Processing: {rule.jar_name} <- {rule.mtcr_filename}")
        pack = parse_mtcr(mtcr_path)
        print(f"[legend_jar]   Modified: {len(pack.modified_classes)}  Added: {len(pack.added_classes)}")

        unpack_dir = unpack_dir_for(self.work_dir, rule.jar_name)
        mr = MtcrPackReport(mtcr_name=rule.mtcr_filename, jar_name=rule.jar_name)

        # ── Dry-run: report intent without touching files ──────────────────────
        if self.dry_run:
            # add.dex dry-run: validate DEX magic, report WOULD_ADD_CLASS
            add_dex_path = find_add_dex_for_jar(rule.jar_name, add_dex_search)
            if add_dex_path is not None:
                adr = merge_add_dex(add_dex_path, unpack_dir, rule.jar_name, dry_run=True)
                jr.add_dex_reports.append(adr)

            # MTCR dry-run: exact patcher against empty dir → WOULD_* statuses
            mr.method_results = apply_exact_mtcr(pack, unpack_dir, dry_run=True)
            jr.mtcr_reports.append(mr)
            jr.decompile_ok = True   # not actually done; mark nominal for report
            jr.repack_ok = True
            return jr

        # ── Execute: copy → unpack → add.dex → apply → repack → restore ──────

        # Step 1: Copy JAR to workspace
        workspace_jar = self.work_dir / rule.jar_name
        if not workspace_jar.exists():
            import shutil
            shutil.copy2(project_jar, workspace_jar)
            print(f"[legend_jar]   Copied {rule.jar_name} to workspace")

        # Step 2: Unpack JAR + baksmali all DEX files
        unpack_result = unpack_jar(workspace_jar, unpack_dir)
        jr.decompile_ok = len(unpack_result.errors) == 0
        jr.decompile_errors = unpack_result.errors

        if not jr.decompile_ok:
            for e in unpack_result.errors:
                session.errors.append(f"{rule.jar_name} decompile: {e}")
            jr.mtcr_reports.append(mr)
            return jr

        # Step 3: Merge add.dex (baksmali → smali → new smali_classesN root)
        add_dex_path = find_add_dex_for_jar(rule.jar_name, add_dex_search)
        if add_dex_path is not None:
            print(f"[legend_jar]   add.dex: {add_dex_path.name}")
            adr = merge_add_dex(add_dex_path, unpack_dir, rule.jar_name, dry_run=False)
            jr.add_dex_reports.append(adr)
            if adr.errors:
                for e in adr.errors:
                    session.warnings.append(f"{rule.jar_name} add.dex: {e}")
        else:
            print(f"[legend_jar]   No add.dex for {rule.jar_name}")

        # Step 4: Apply MTCR patch (exact method/field block replacement)
        mr.method_results = apply_exact_mtcr(pack, unpack_dir, dry_run=False)
        jr.mtcr_reports.append(mr)

        # Step 5: smali → dex
        dex_results = repack_smali_to_dex(unpack_dir)
        repack_failed = [name for (name, ok, _) in dex_results if not ok]
        if repack_failed:
            for name, ok, err in dex_results:
                if not ok:
                    jr.repack_errors.append(f"{name}: {err}")
                    session.errors.append(f"{rule.jar_name} smali repack {name}: {err}")
            jr.repack_ok = False
            return jr
        jr.repack_ok = True

        # Step 6: dex → jar
        rebuilt_jar = self.work_dir / f"{rule.jar_name}.rebuilt"
        jar_result = repack_dir_to_jar(unpack_dir, rebuilt_jar)
        if not jar_result.success:
            jr.repack_errors.append(jar_result.error)
            session.errors.append(f"{rule.jar_name} jar repack: {jar_result.error}")
            jr.repack_ok = False
            return jr

        # Step 7: backup original + restore rebuilt
        restore_result = backup_and_restore_jar(
            rebuilt_jar=rebuilt_jar,
            project_jar=project_jar,
            backup_dir=self.backup_dir,
        )
        jr.restore_ok    = restore_result.success
        jr.backup_path   = restore_result.backup_path
        jr.restore_error = restore_result.error
        if not restore_result.success:
            session.errors.append(f"{rule.jar_name} restore: {restore_result.error}")

        return jr


# ── CLI ───────────────────────────────────────────────────────────────────────
def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m factory.patch.legend.jar_patch",
        description="DeadZone Legend JAR patch stage",
    )
    parser.add_argument(
        "--project", required=True, metavar="PATH",
        help="Path to unpacked ROM project directory",
    )
    parser.add_argument(
        "--flavor", required=True, metavar="FLAVOR",
        help="Build flavor (must be 'legend' to apply patches; others are skipped)",
    )
    parser.add_argument(
        "--execute", action="store_true",
        help="Actually apply patches (omit for dry-run)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    project_dir = Path(args.project).expanduser().resolve()

    if not project_dir.exists():
        print(f"[legend_jar] ERROR: project directory not found: {project_dir}", file=sys.stderr)
        return 1

    patcher = LegendJarPatcher(
        project_dir,
        flavor=args.flavor,
        dry_run=not args.execute,
    )
    session = patcher.run()
    return 0 if not session.errors else 1


if __name__ == "__main__":
    sys.exit(main())
