"""
add.dex merger — decompile with baksmali, merge smali into the JAR smali tree.

add.dex files contain new helper classes that must be treated exactly like
any other DEX-derived smali: baksmali → smali files → new smali_classesN root.

NEVER insert the .dex file directly into a JAR.

Merge rules:
  Class not yet present   → ADDED_CLASS (copied into new smali root)
  Class already present, identical content → EXISTS_IDENTICAL (skipped)
  Class already present, different content → CONFLICT (not overwritten)
"""
from __future__ import annotations

import hashlib
import shutil
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from factory.patch.common.mtcr_exact_patcher import PatchStatus, MethodPatchResult
from factory.patch.common.smali_tools import decompile_dex, resolve_baksmali, smali_dirs_in


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _next_smali_root_path(smali_roots: list[Path], unpack_dir: Path) -> Path:
    """
    Return the path for the next available smali_classesN directory inside
    *unpack_dir* that does not already exist.

    smali_classes  → if not present
    smali_classes2 → if smali_classes already present
    smali_classes3 → etc.
    """
    existing = {r.name for r in smali_roots}
    if "smali_classes" not in existing:
        return unpack_dir / "smali_classes"
    n = 2
    while f"smali_classes{n}" in existing:
        n += 1
    return unpack_dir / f"smali_classes{n}"


def _find_class_in_roots(smali_roots: list[Path], class_name: str) -> Optional[Path]:
    """Search all smali_classes* dirs for class_name.smali."""
    for root in smali_roots:
        candidate = root / (class_name + ".smali")
        if candidate.is_file():
            return candidate
    return None


# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class AddDexMergeResult:
    dex_path: Path
    target_jar: str
    decompiled: bool = False
    dex_valid: bool = False
    class_count: int = 0
    smali_root: Optional[Path] = None
    class_results: list[MethodPatchResult] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def merged_count(self) -> int:
        return sum(1 for r in self.class_results if r.status == PatchStatus.ADDED_CLASS)

    @property
    def conflict_count(self) -> int:
        return sum(1 for r in self.class_results if r.status == PatchStatus.CONFLICT)


def _is_valid_dex(dex_path: Path) -> bool:
    """Return True if file starts with the DEX magic bytes."""
    try:
        with dex_path.open("rb") as fh:
            return fh.read(4) == b"dex\n"
    except Exception:
        return False


def merge_add_dex(
    dex_path: Path,
    unpack_dir: Path,
    target_jar: str,
    dry_run: bool = True,
) -> AddDexMergeResult:
    """
    Decompile *dex_path* with baksmali and merge the resulting smali classes
    into a new smali_classesN root inside *unpack_dir*.

    In dry-run mode no files are written; the result carries dex_valid and a
    WOULD_ADD_CLASS entry for the dex file as a whole (class enumeration
    requires actually running baksmali, which we skip in dry-run).
    """
    result = AddDexMergeResult(dex_path=dex_path, target_jar=target_jar)

    if not dex_path.is_file():
        result.errors.append(f"add.dex not found: {dex_path}")
        print(f"[add_dex] NOT FOUND: {dex_path.name}")
        return result

    result.dex_valid = _is_valid_dex(dex_path)
    if not result.dex_valid:
        result.errors.append(f"{dex_path.name} is not a valid DEX file")
        print(f"[add_dex] INVALID DEX: {dex_path.name}")
        return result

    print(f"[add_dex] Processing: {dex_path.name} -> {target_jar}")

    # ── Dry-run: report intent without running baksmali ───────────────────────
    if dry_run:
        smali_roots = smali_dirs_in(unpack_dir)
        next_root = _next_smali_root_path(smali_roots, unpack_dir)
        result.class_results.append(MethodPatchResult(
            class_name=f"(all classes in {dex_path.name})",
            status=PatchStatus.WOULD_ADD_CLASS,
            message=f"would decompile and merge into {next_root.name}/",
        ))
        print(f"[add_dex] DRY RUN: would merge {dex_path.name} into {next_root.name}/")
        return result

    # ── Execute: baksmali → temp dir → merge ──────────────────────────────────
    baksmali_jar = resolve_baksmali()
    if baksmali_jar is None:
        result.errors.append("baksmali.jar not found; cannot decompile add.dex")
        return result

    smali_roots = smali_dirs_in(unpack_dir)
    next_root = _next_smali_root_path(smali_roots, unpack_dir)

    with tempfile.TemporaryDirectory() as tmp_str:
        tmp_dir = Path(tmp_str)
        ok, err = decompile_dex(baksmali_jar, dex_path, tmp_dir)
        if not ok:
            result.errors.append(f"baksmali failed: {err}")
            print(f"[add_dex] baksmali FAILED for {dex_path.name}: {err}")
            return result

        result.decompiled = True

        # Collect all .smali files from temp dir
        smali_files = list(tmp_dir.rglob("*.smali"))
        result.class_count = len(smali_files)
        print(f"[add_dex]   Decompiled {len(smali_files)} smali classes from {dex_path.name}")

        if not smali_files:
            result.errors.append("baksmali produced no smali files")
            return result

        # Merge each class
        next_root.mkdir(parents=True, exist_ok=True)
        result.smali_root = next_root

        for smali_path in sorted(smali_files):
            # Derive class_name relative to tmp_dir, without .smali extension
            rel = smali_path.relative_to(tmp_dir)
            class_name = str(rel.with_suffix("")).replace("\\", "/")

            # Check all existing roots (not the new one yet)
            existing = _find_class_in_roots(smali_roots, class_name)
            target_in_new_root = next_root / rel

            if existing is not None:
                # Compare content
                existing_content = existing.read_text(encoding="utf-8", errors="replace")
                new_content = smali_path.read_text(encoding="utf-8", errors="replace")
                if _sha256_file(existing) == hashlib.sha256(
                    new_content.encode("utf-8", errors="replace")
                ).hexdigest():
                    result.class_results.append(MethodPatchResult(
                        class_name=class_name,
                        status=PatchStatus.EXISTS_IDENTICAL,
                        target_smali=existing,
                        message="already present in smali tree, identical",
                    ))
                    print(f"[add_dex]   EXISTS_IDENTICAL: {class_name}")
                else:
                    result.class_results.append(MethodPatchResult(
                        class_name=class_name,
                        status=PatchStatus.CONFLICT,
                        target_smali=existing,
                        message="class exists with different content; not overwritten",
                    ))
                    print(f"[add_dex]   CONFLICT: {class_name}")
                continue

            # Also check if we've already placed it in the new root this session
            if target_in_new_root.is_file():
                result.class_results.append(MethodPatchResult(
                    class_name=class_name,
                    status=PatchStatus.EXISTS_IDENTICAL,
                    target_smali=target_in_new_root,
                    message="placed in new smali root this session",
                ))
                continue

            # Copy into new root
            try:
                target_in_new_root.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(smali_path, target_in_new_root)
                result.class_results.append(MethodPatchResult(
                    class_name=class_name,
                    status=PatchStatus.ADDED_CLASS,
                    target_smali=target_in_new_root,
                    message=f"merged into {next_root.name}/",
                ))
                print(f"[add_dex]   ADDED_CLASS: {class_name} -> {next_root.name}/")
            except Exception as exc:
                result.class_results.append(MethodPatchResult(
                    class_name=class_name,
                    status=PatchStatus.FAILED,
                    message=str(exc),
                ))
                print(f"[add_dex]   FAILED: {class_name}: {exc}")

    print(f"[add_dex]   Merged: {result.merged_count}  Conflicts: {result.conflict_count}")
    return result
