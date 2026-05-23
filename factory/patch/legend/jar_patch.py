"""
Legend JAR patch orchestrator + CLI entry point.

Pipeline order (execute mode):
  1.  Guard: exit cleanly if flavor is not a Legend flavor.
  2.  Locate MTCR directory.
  3.  For each JAR rule -- UNPACK PHASE:
        a. Copy JAR from project to workspace.
        b. Unpack JAR + baksmali all DEX files into smali roots.
  4.  For each JAR rule -- PATCH PHASE:
        c. Merge add.dex payload as new smali root (if present).
        d. Apply MTCR exact patches (method/field/block replacement).
  5.  Cross-JAR stages (operate on the shared work_dir smali roots):
        e. Signature bypass (if factory.patch.legend.signature_bypass_legacy present).
        f. JAR misc legacy (if factory.patch.legend.jar_misc_legacy present).
        g. Kaori legacy (if factory.patch.legend.kaori_legacy present).
  6.  For each JAR rule -- REBUILD PHASE:
        h. smali -> DEX (compile each smali root).
        i. DEX -> JAR (repack directory into JAR).
  7.  For each JAR rule -- REPLACE PHASE:
        j. Replace original project JAR with rebuilt JAR (NO backup created).
           Skip replace if rebuild failed or rebuilt JAR is missing/empty.
  8.  Write reports.

Pipeline order (dry-run, default):
  - Check each JAR exists in project.
  - Validate add.dex DEX magic, report WOULD_ADD_CLASS intent.
  - Parse MTCR, report WOULD_APPLY / WOULD_ADD intent.
  - Report WOULD_RUN or SKIPPED_MISSING_MODULE for each optional stage.
  - No files modified.

Backup policy: DISABLED. No .bak files, no output/backups entries.

CLI:
  # dry-run:
  python -m factory.patch.legend.jar_patch \\
      --project "path/to/unpacked_project" \\
      --flavor legend \\
      --android-major 16

  # execute:
  python -m factory.patch.legend.jar_patch \\
      --project "path/to/unpacked_project" \\
      --flavor legend \\
      --android-major 16 \\
      --execute
"""
from __future__ import annotations

import argparse
import shutil
import sys
import time
from pathlib import Path

from factory.patch.common.jar_workspace import (
    copy_jars_to_workspace,
    repack_dir_to_jar,
    repack_smali_to_dex,
    resolve_partition_file,
    restore_rebuilt_jar_no_backup,
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
    LegendJarRule,
    find_mtcr_dir,
    resolve_mtcr_path,
)
from factory.patch.legend.add_dex_rules import find_add_dex_for_jar

_REPO_ROOT    = Path(__file__).resolve().parents[3]
_OUTPUT_ROOT  = _REPO_ROOT / "output"
_REPORTS_DIR  = _OUTPUT_ROOT / "reports"

_LEGEND_FLAVORS = {"legend", "deadzone_legend"}

_LEGEND_HOME = Path(__file__).resolve().parent
# Add-DEX payloads live exclusively in factory/patch/legend/assets/jar/
_ADD_DEX_CANONICAL = _LEGEND_HOME / "assets" / "jar"


def _normalise_flavor(flavor: str) -> str:
    return flavor.lower().replace("-", "_")


def _add_dex_dir() -> Path:
    if not _ADD_DEX_CANONICAL.is_dir():
        print(
            f"[jar_patch] WARNING: DEX asset directory not found: {_ADD_DEX_CANONICAL} "
            "— dex_add payloads will be skipped. "
            "Place required JAR assets in factory/patch/legend/assets/jar/"
        )
    return _ADD_DEX_CANONICAL


def _work_dir(project_dir: Path) -> Path:
    ts = time.strftime("%Y%m%d_%H%M%S")
    return _OUTPUT_ROOT / "work" / f"legend_jar_{ts}"


# -- Optional module loading -
# Each module is optional: if missing, the stage is reported as
# SKIPPED_MISSING_MODULE and the pipeline continues.

# Legacy modules are archived — they must never be executed by this runner.
# Imports are intentionally left failing so _HAS_* stays False.
try:
    from factory.patch.legend.archived_legacy.signature_bypass_legacy import (
        apply_legacy_signature_bypass as _apply_sig_bypass,
    )
    _HAS_SIG_BYPASS = False  # archived: do not execute
except ImportError:
    _HAS_SIG_BYPASS = False
    _apply_sig_bypass = None  # type: ignore[assignment]

try:
    from factory.patch.legend.archived_legacy.jar_misc_legacy import (
        apply_legend_jar_misc_legacy_patches as _apply_misc_legacy,
    )
    _HAS_MISC_LEGACY = False  # archived: do not execute
except ImportError:
    _HAS_MISC_LEGACY = False
    _apply_misc_legacy = None  # type: ignore[assignment]

try:
    from factory.patch.legend.archived_legacy.kaori_legacy import (
        apply_kaori_legacy_patch as _apply_kaori,
    )
    _HAS_KAORI = False  # archived: do not execute
except ImportError:
    _HAS_KAORI = False
    _apply_kaori = None  # type: ignore[assignment]


# -- Stage status helpers -

def _dry_stage(module_name: str, available: bool) -> dict:
    """Return a dry-run stage status dict."""
    status = "WOULD_RUN" if available else "SKIPPED_MISSING_MODULE"
    return {
        "module": module_name,
        "status": status,
        "available": available,
        "warnings": [],
        "errors": [],
    }


def _stage_from_report(module_name: str, report: dict) -> dict:
    """Wrap a module's return dict into a stage summary."""
    status = report.get("status", "UNKNOWN")
    if status not in ("APPLIED", "DRY_RUN", "SKIPPED_NON_LEGEND",
                      "SKIPPED_UNSUPPORTED_ANDROID", "FAILED"):
        status = "APPLIED" if not report.get("errors") else "FAILED"
    return {
        "module": module_name,
        "status": status,
        "available": True,
        "warnings": report.get("warnings", []),
        "errors":   report.get("errors", []),
    }


def _stage_from_sig_report(module_name: str, sig_report) -> dict:
    """Convert a SigBypassReport object into a stage summary dict."""
    return {
        "module": module_name,
        "status": getattr(sig_report, "status", "UNKNOWN"),
        "available": True,
        "warnings": getattr(sig_report, "warnings", []),
        "errors":   getattr(sig_report, "errors", []),
    }


# --
class LegendJarPatcher:
    """
    Orchestrate the Legend JAR patch stage.

    Parameters
    ----------
    project_dir : Path
        Unpacked ROM project directory (output of the unpack stage).
    flavor : str
        Must be a Legend flavor to proceed; any other value exits clean.
    android_major : int | None
        Android major version. Passed to cross-JAR stages. Optional.
    dry_run : bool
        When True nothing is written; reports show WOULD_* intent statuses.
    """

    def __init__(
        self,
        project_dir: Path,
        *,
        flavor: str,
        android_major: int | None = None,
        dry_run: bool = True,
    ) -> None:
        self.project_dir  = project_dir.resolve()
        self.flavor       = _normalise_flavor(flavor)
        self.android_major = android_major
        self.dry_run      = dry_run
        self.work_dir     = _work_dir(self.project_dir)
        # No backup directory -- backup policy is disabled.

    # -- Public entry point -

    def run(self) -> PatchSession:
        mtcr_dir = find_mtcr_dir() or Path("(not found)")
        session = PatchSession(
            flavor=self.flavor,
            dry_run=self.dry_run,
            project_dir=self.project_dir,
            work_dir=self.work_dir,
            patch_dir=mtcr_dir,
            android_major=self.android_major,
        )

        # -- Flavor guard -
        if self.flavor not in _LEGEND_FLAVORS:
            msg = f"Flavor '{self.flavor}' is not a Legend flavor; JAR patch stage skipped."
            session.warnings.append(msg)
            print(f"[legend_jar] SKIPPED -- {msg}")
            write_reports(session, _REPORTS_DIR)
            return session

        mode = "DRY RUN" if self.dry_run else "EXECUTE"
        print(f"[legend_jar] === Legend JAR Patch Stage ({mode}) ===")
        print(f"[legend_jar] Project       : {self.project_dir}")
        print(f"[legend_jar] Work dir      : {self.work_dir}")
        print(f"[legend_jar] Android major : {self.android_major}")
        print(f"[legend_jar] Backup policy : disabled")

        # -- Locate MTCR packs -
        mtcr_dir_real = find_mtcr_dir()
        if mtcr_dir_real is None:
            msg = "MTCR directory not found. Place MTCR packs in factory/patch/legend/assets/jar/."
            session.errors.append(msg)
            print(f"[legend_jar] ERROR: {msg}")
            write_reports(session, _REPORTS_DIR)
            return session

        session.patch_dir = mtcr_dir_real
        print(f"[legend_jar] MTCR dir      : {mtcr_dir_real}")

        add_dex_search = _add_dex_dir()
        print(f"[legend_jar] add.dex dir   : {add_dex_search}")

        if self.dry_run:
            return self._run_dry(session, mtcr_dir_real, add_dex_search)
        return self._run_execute(session, mtcr_dir_real, add_dex_search)

    # -- Dry-run path -

    def _run_dry(
        self,
        session: PatchSession,
        mtcr_dir: Path,
        add_dex_search: Path,
    ) -> PatchSession:
        """Dry-run: report intent for every stage without modifying anything."""
        print("[legend_jar] --- DRY RUN: checking JARs and patches ---")

        for rule in LEGEND_JAR_RULES:
            jr = self._dry_jar(rule, mtcr_dir, add_dex_search, session)
            session.jar_reports.append(jr)

        # Cross-JAR stage status (WOULD_RUN / SKIPPED_MISSING_MODULE)
        session.signature_bypass_stage = _dry_stage(
            "signature_bypass_legacy", _HAS_SIG_BYPASS
        )
        session.jar_misc_legacy_stage = _dry_stage(
            "jar_misc_legacy", _HAS_MISC_LEGACY
        )
        session.kaori_legacy_stage = _dry_stage(
            "kaori_legacy", _HAS_KAORI
        )

        print("[legend_jar]   signature_bypass : " + session.signature_bypass_stage["status"])
        print("[legend_jar]   jar_misc_legacy  : " + session.jar_misc_legacy_stage["status"])
        print("[legend_jar]   kaori_legacy     : " + session.kaori_legacy_stage["status"])
        print("[legend_jar]   rebuild          : SKIPPED_DRY_RUN")
        print("[legend_jar]   replace (no bak) : SKIPPED_DRY_RUN")

        write_reports(session, _REPORTS_DIR)
        print("[legend_jar] === DRY RUN complete ===")
        return session

    def _dry_jar(
        self,
        rule: LegendJarRule,
        mtcr_dir: Path,
        add_dex_search: Path,
        session: PatchSession,
    ) -> JarReport:
        """Dry-run: check one JAR -- locate files, parse MTCR, report intent."""
        jar_partition_path = f"{rule.jar_partition}/{rule.jar_rel_path}"
        jr = JarReport(
            jar_name=rule.jar_name,
            jar_partition_path=jar_partition_path,
            found=False,
        )

        # Locate JAR in project
        parts = rule.jar_rel_path.split("/")
        project_jar = resolve_partition_file(self.project_dir, rule.jar_partition, *parts)
        if project_jar is None or not project_jar.is_file():
            session.warnings.append(f"{rule.jar_name}: not found in project")
            print(f"[legend_jar]   NOT FOUND: {rule.jar_name}")
            return jr
        jr.found = True

        # Locate MTCR pack
        mtcr_path = resolve_mtcr_path(rule, mtcr_dir)
        if mtcr_path is None:
            jr.decompile_errors.append(
                f"MTCR pack {rule.mtcr_filename} not found in {mtcr_dir}"
            )
            session.warnings.append(
                f"{rule.jar_name}: MTCR pack missing ({rule.mtcr_filename})"
            )
            print(f"[legend_jar]   MTCR MISSING: {rule.mtcr_filename}")
            return jr

        print(f"[legend_jar]   Processing (dry): {rule.jar_name} <- {rule.mtcr_filename}")
        pack = parse_mtcr(mtcr_path)
        print(f"[legend_jar]     Modified: {len(pack.modified_classes)}  Added: {len(pack.added_classes)}")

        unpack_dir = unpack_dir_for(self.work_dir, rule.jar_name)
        mr = MtcrPackReport(mtcr_name=rule.mtcr_filename, jar_name=rule.jar_name)

        # add.dex dry-run: validate DEX magic, report WOULD_ADD_CLASS
        add_dex_path = find_add_dex_for_jar(rule.jar_name, add_dex_search)
        if add_dex_path is not None:
            adr = merge_add_dex(add_dex_path, unpack_dir, rule.jar_name, dry_run=True)
            jr.add_dex_reports.append(adr)

        # MTCR dry-run: exact patcher against empty dir -> WOULD_* statuses
        mr.method_results = apply_exact_mtcr(pack, unpack_dir, dry_run=True)
        jr.mtcr_reports.append(mr)
        jr.decompile_ok = True   # nominal -- not actually done in dry-run
        jr.repack_ok = True
        return jr

    # -- Execute path -

    def _run_execute(
        self,
        session: PatchSession,
        mtcr_dir: Path,
        add_dex_search: Path,
    ) -> PatchSession:
        """Execute the full pipeline in order."""
        self.work_dir.mkdir(parents=True, exist_ok=True)

        # Track JARs that completed unpack + patch successfully so we can
        # rebuild and replace them. Maps jar_name -> (JarReport, rule, project_jar).
        ready: dict[str, tuple[JarReport, LegendJarRule, Path]] = {}

        # -- Phase 1+2: Unpack all JARs, then apply per-JAR patches -
        print("[legend_jar] --- Phase: unpack + per-JAR patches ---")
        for rule in LEGEND_JAR_RULES:
            jr, project_jar = self._unpack_and_patch(
                rule, mtcr_dir, add_dex_search, session
            )
            session.jar_reports.append(jr)
            if jr.found and jr.decompile_ok:
                ready[rule.jar_name] = (jr, rule, project_jar)

        # -- Phase 3: Cross-JAR stages -
        print("[legend_jar] --- Phase: cross-JAR stages ---")
        session.signature_bypass_stage = self._exec_sig_bypass(session)
        session.jar_misc_legacy_stage  = self._exec_misc_legacy(session)
        session.kaori_legacy_stage     = self._exec_kaori(session)

        # -- Phase 4+5: Rebuild then replace each JAR -
        print("[legend_jar] --- Phase: rebuild + replace ---")
        for jar_name, (jr, rule, project_jar) in ready.items():
            self._rebuild_and_replace(rule, jr, project_jar, session)

        write_reports(session, _REPORTS_DIR)
        print("[legend_jar] === EXECUTE complete ===")
        return session

    def _unpack_and_patch(
        self,
        rule: LegendJarRule,
        mtcr_dir: Path,
        add_dex_search: Path,
        session: PatchSession,
    ) -> tuple[JarReport, Path | None]:
        """Copy + unpack one JAR, then apply add.dex + MTCR patches."""
        jar_partition_path = f"{rule.jar_partition}/{rule.jar_rel_path}"
        jr = JarReport(
            jar_name=rule.jar_name,
            jar_partition_path=jar_partition_path,
            found=False,
        )

        # Locate JAR
        parts = rule.jar_rel_path.split("/")
        project_jar = resolve_partition_file(self.project_dir, rule.jar_partition, *parts)
        if project_jar is None or not project_jar.is_file():
            jr.found = False
            session.warnings.append(f"{rule.jar_name}: not found in project")
            print(f"[legend_jar]   NOT FOUND: {rule.jar_name}")
            return jr, None
        jr.found = True

        # Locate MTCR pack
        mtcr_path = resolve_mtcr_path(rule, mtcr_dir)
        if mtcr_path is None:
            jr.decompile_errors.append(
                f"MTCR pack {rule.mtcr_filename} not found in {mtcr_dir}"
            )
            session.warnings.append(
                f"{rule.jar_name}: MTCR pack missing ({rule.mtcr_filename})"
            )
            print(f"[legend_jar]   MTCR MISSING: {rule.mtcr_filename}")
            return jr, project_jar

        print(f"[legend_jar]   Processing: {rule.jar_name} <- {rule.mtcr_filename}")
        pack = parse_mtcr(mtcr_path)

        unpack_dir = unpack_dir_for(self.work_dir, rule.jar_name)

        # Step 1: Copy JAR to workspace
        workspace_jar = self.work_dir / rule.jar_name
        if not workspace_jar.exists():
            shutil.copy2(project_jar, workspace_jar)
            print(f"[legend_jar]     Copied {rule.jar_name} to workspace")

        # Step 2: Unpack JAR + baksmali all DEX files
        unpack_result = unpack_jar(workspace_jar, unpack_dir)
        jr.decompile_ok     = len(unpack_result.errors) == 0
        jr.decompile_errors = unpack_result.errors

        if not jr.decompile_ok:
            for e in unpack_result.errors:
                session.errors.append(f"{rule.jar_name} decompile: {e}")
            jr.mtcr_reports.append(
                MtcrPackReport(mtcr_name=rule.mtcr_filename, jar_name=rule.jar_name)
            )
            return jr, project_jar

        # Step 3: Merge add.dex (baksmali -> smali -> new smali_classesN root)
        add_dex_path = find_add_dex_for_jar(rule.jar_name, add_dex_search)
        if add_dex_path is not None:
            print(f"[legend_jar]     add.dex: {add_dex_path.name}")
            adr = merge_add_dex(add_dex_path, unpack_dir, rule.jar_name, dry_run=False)
            jr.add_dex_reports.append(adr)
            if adr.errors:
                for e in adr.errors:
                    session.warnings.append(f"{rule.jar_name} add.dex: {e}")
        else:
            print(f"[legend_jar]     No add.dex for {rule.jar_name}")

        # Step 4: Apply MTCR exact patch
        mr = MtcrPackReport(mtcr_name=rule.mtcr_filename, jar_name=rule.jar_name)
        mr.method_results = apply_exact_mtcr(pack, unpack_dir, dry_run=False)
        jr.mtcr_reports.append(mr)

        return jr, project_jar

    def _rebuild_and_replace(
        self,
        rule: LegendJarRule,
        jr: JarReport,
        project_jar: Path,
        session: PatchSession,
    ) -> None:
        """Rebuild smali->dex->jar, then replace project JAR without backup."""
        unpack_dir  = unpack_dir_for(self.work_dir, rule.jar_name)
        rebuilt_jar = self.work_dir / f"{rule.jar_name}.rebuilt"

        # Step 5: smali -> dex
        dex_results = repack_smali_to_dex(unpack_dir)
        repack_failed = [name for (name, ok, _) in dex_results if not ok]
        if repack_failed:
            for name, ok, err in dex_results:
                if not ok:
                    jr.repack_errors.append(f"{name}: {err}")
                    session.errors.append(f"{rule.jar_name} smali repack {name}: {err}")
            jr.repack_ok = False
            print(f"[legend_jar]   Smali repack FAILED for {rule.jar_name} -- project JAR NOT replaced")
            return
        jr.repack_ok = True

        # Step 6: dex -> jar
        jar_result = repack_dir_to_jar(unpack_dir, rebuilt_jar)
        if not jar_result.success:
            jr.repack_errors.append(jar_result.error)
            session.errors.append(f"{rule.jar_name} jar repack: {jar_result.error}")
            jr.repack_ok = False
            print(f"[legend_jar]   JAR repack FAILED for {rule.jar_name} -- project JAR NOT replaced")
            return

        # Step 7: Replace project JAR (no backup)
        replace_result = restore_rebuilt_jar_no_backup(rebuilt_jar, project_jar)
        jr.restore_ok    = replace_result.success
        jr.restore_error = replace_result.error
        if not replace_result.success:
            session.errors.append(f"{rule.jar_name} replace: {replace_result.error}")
            print(f"[legend_jar]   Replace FAILED for {rule.jar_name}: {replace_result.error}")
        else:
            print(f"[legend_jar]   Replaced {rule.jar_name} in project (no backup)")

    # -- Cross-JAR stage runners -

    def _exec_sig_bypass(self, session: PatchSession) -> dict:
        if not _HAS_SIG_BYPASS:
            print("[legend_jar]   signature_bypass_legacy : SKIPPED_MISSING_MODULE")
            return _dry_stage("signature_bypass_legacy", False)
        print("[legend_jar]   Running signature_bypass_legacy ...")
        try:
            report = _apply_sig_bypass(
                work_dir=self.work_dir,
                android_major=self.android_major,
                flavor=self.flavor,
                execute=True,
            )
            stage = _stage_from_sig_report("signature_bypass_legacy", report)
        except Exception as exc:
            err = f"signature_bypass_legacy raised: {exc}"
            session.errors.append(err)
            stage = {
                "module": "signature_bypass_legacy",
                "status": "FAILED",
                "available": True,
                "warnings": [],
                "errors": [err],
            }
        print(f"[legend_jar]   signature_bypass_legacy : {stage['status']}")
        return stage

    def _exec_misc_legacy(self, session: PatchSession) -> dict:
        if not _HAS_MISC_LEGACY:
            print("[legend_jar]   jar_misc_legacy : SKIPPED_MISSING_MODULE")
            return _dry_stage("jar_misc_legacy", False)
        print("[legend_jar]   Running jar_misc_legacy ...")
        try:
            report = _apply_misc_legacy(
                work_dir=self.work_dir,
                android_major=self.android_major,
                flavor=self.flavor,
                execute=True,
            )
            stage = _stage_from_report("jar_misc_legacy", report)
        except Exception as exc:
            err = f"jar_misc_legacy raised: {exc}"
            session.errors.append(err)
            stage = {
                "module": "jar_misc_legacy",
                "status": "FAILED",
                "available": True,
                "warnings": [],
                "errors": [err],
            }
        print(f"[legend_jar]   jar_misc_legacy : {stage['status']}")
        return stage

    def _exec_kaori(self, session: PatchSession) -> dict:
        if not _HAS_KAORI:
            print("[legend_jar]   kaori_legacy : SKIPPED_MISSING_MODULE")
            return _dry_stage("kaori_legacy", False)
        print("[legend_jar]   Running kaori_legacy ...")
        try:
            report = _apply_kaori(
                work_dir=self.work_dir,
                flavor=self.flavor,
                android_major=self.android_major,
                execute=True,
            )
            stage = _stage_from_report("kaori_legacy", report)
        except Exception as exc:
            err = f"kaori_legacy raised: {exc}"
            session.errors.append(err)
            stage = {
                "module": "kaori_legacy",
                "status": "FAILED",
                "available": True,
                "warnings": [],
                "errors": [err],
            }
        print(f"[legend_jar]   kaori_legacy : {stage['status']}")
        return stage


# -- CLI -
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
        help="Build flavor (legend or deadzone_legend to apply patches; others are skipped)",
    )
    parser.add_argument(
        "--android-major", dest="android_major", type=int, default=None,
        metavar="N",
        help="Android major version (e.g. 14, 15, 16); passed to cross-JAR stages",
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
        print(
            f"[legend_jar] ERROR: project directory not found: {project_dir}",
            file=sys.stderr,
        )
        return 1

    patcher = LegendJarPatcher(
        project_dir,
        flavor=args.flavor,
        android_major=args.android_major,
        dry_run=not args.execute,
    )
    session = patcher.run()
    return 0 if not session.errors else 1


if __name__ == "__main__":
    sys.exit(main())
