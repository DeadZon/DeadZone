"""
MTCR patch pack parser and apply engine.

MTCR format (ZIP archive):
  a/<class_path>   — original smali content (no .smali extension in archive)
  b/<class_path>   — modified / added smali content
  info.json        — optional metadata (JAR paths, tool settings)

Rules:
  Modified = exists in both a/ and b/  → replace existing class in workspace
  Added    = exists only in b/         → inject into workspace

Class names in MTCR use path separators (android/content/res/Resources).
On disk the file name is android/content/res/Resources.smali.
"""
from __future__ import annotations

import hashlib
import zipfile
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional


# ── Status enums ─────────────────────────────────────────────────────────────
class ClassStatus(str, Enum):
    # For modified classes (dry-run / execute)
    WOULD_REPLACE    = "WOULD_REPLACE"
    REPLACED         = "REPLACED"
    SKIPPED_MISSING  = "SKIPPED_MISSING"
    FAILED           = "FAILED"
    # For added classes (dry-run / execute)
    WOULD_ADD        = "WOULD_ADD"
    ADDED            = "ADDED"
    EXISTS_IDENTICAL = "EXISTS_IDENTICAL"
    CONFLICT         = "CONFLICT"


@dataclass
class ClassResult:
    class_name: str           # e.g. android/content/res/Resources
    status: ClassStatus
    target_smali: Optional[Path] = None   # where on disk this class lives/landed
    message: str = ""


# ── MTCR data model ───────────────────────────────────────────────────────────
@dataclass
class MtcrPack:
    """Parsed content of a single .mtcr archive."""
    mtcr_path: Path
    info: dict                          # info.json, or {} if absent

    # class_name → smali text from b/ (covers both modified and added)
    b_content: dict[str, str] = field(default_factory=dict)

    # class names present in a/
    a_classes: set[str] = field(default_factory=set)

    @property
    def modified_classes(self) -> list[str]:
        """Classes that exist in both a/ and b/ — will replace existing."""
        return sorted(self.a_classes & set(self.b_content))

    @property
    def added_classes(self) -> list[str]:
        """Classes that exist only in b/ — will be injected new."""
        return sorted(set(self.b_content) - self.a_classes)


def parse_mtcr(mtcr_path: Path) -> MtcrPack:
    """
    Open *mtcr_path* and extract:
      - a/ entry names (without the 'a/' prefix)
      - b/ entry names + their text content
      - info.json metadata
    """
    import json

    a_classes: set[str] = set()
    b_content: dict[str, str] = {}
    info: dict = {}

    with zipfile.ZipFile(mtcr_path, "r") as zf:
        for entry in zf.namelist():
            if entry == "info.json":
                try:
                    raw = zf.read(entry).decode("utf-8", errors="replace")
                    info = json.loads(raw)
                except Exception:
                    info = {}
                continue

            if entry.startswith("a/") and entry != "a/":
                class_name = entry[2:]   # strip "a/" prefix
                a_classes.add(class_name)
                continue

            if entry.startswith("b/") and entry != "b/":
                class_name = entry[2:]   # strip "b/" prefix
                try:
                    content = zf.read(entry).decode("utf-8", errors="replace")
                    b_content[class_name] = content
                except Exception:
                    pass

    return MtcrPack(
        mtcr_path=mtcr_path,
        info=info,
        a_classes=a_classes,
        b_content=b_content,
    )


# ── Apply logic ───────────────────────────────────────────────────────────────
def _find_class_in_smali_roots(
    smali_roots: list[Path],
    class_name: str,
) -> Optional[Path]:
    """
    Search all smali_classes* directories for class_name.smali.
    Returns the path if found, else None.
    """
    smali_file = class_name + ".smali"
    for root in smali_roots:
        candidate = root / smali_file
        if candidate.is_file():
            return candidate
    return None


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def _choose_inject_root(smali_roots: list[Path], prefer_names: list[str]) -> Optional[Path]:
    """
    Choose a smali root for injecting added classes.

    Strategy:
    1. If any of the *prefer_names* dirs exist (preferred based on where
       modified classes of the same pack landed), use the first matching one.
    2. Otherwise use the last (highest-numbered) smali root.
    3. Fall back to smali_classes2 or smali_classes if that is all we have.
    """
    by_name = {r.name: r for r in smali_roots}
    for name in prefer_names:
        if name in by_name:
            return by_name[name]
    if smali_roots:
        return smali_roots[-1]
    return None


def apply_mtcr(
    pack: MtcrPack,
    unpack_dir: Path,
    dry_run: bool = True,
) -> list[ClassResult]:
    """
    Apply the patch pack to the decompiled JAR workspace at *unpack_dir*.

    In dry-run mode no files are written; statuses are WOULD_REPLACE / WOULD_ADD.
    In execute mode statuses are REPLACED / ADDED / SKIPPED_MISSING / CONFLICT /
    EXISTS_IDENTICAL / FAILED.
    """
    from factory.patch.common.smali_tools import smali_dirs_in

    smali_roots = smali_dirs_in(unpack_dir)
    results: list[ClassResult] = []

    # Track where modified classes landed so we can prefer the same root for adds.
    modified_root_names: list[str] = []

    # ── Modified classes ──────────────────────────────────────────────────────
    for class_name in pack.modified_classes:
        existing = _find_class_in_smali_roots(smali_roots, class_name)
        if existing is None:
            results.append(ClassResult(
                class_name=class_name,
                status=ClassStatus.SKIPPED_MISSING,
                message="class not found in any smali_classes* directory",
            ))
            print(f"[mtcr] SKIPPED_MISSING: {class_name}")
            continue

        if dry_run:
            results.append(ClassResult(
                class_name=class_name,
                status=ClassStatus.WOULD_REPLACE,
                target_smali=existing,
            ))
            print(f"[mtcr] WOULD_REPLACE: {class_name} in {existing.parent.name}/")
            modified_root_names.append(existing.parent.name)
            continue

        # Execute: overwrite
        new_content = pack.b_content[class_name]
        try:
            existing.write_text(new_content, encoding="utf-8")
            results.append(ClassResult(
                class_name=class_name,
                status=ClassStatus.REPLACED,
                target_smali=existing,
            ))
            print(f"[mtcr] REPLACED: {class_name} in {existing.parent.name}/")
            modified_root_names.append(existing.parent.name)
        except Exception as exc:
            results.append(ClassResult(
                class_name=class_name,
                status=ClassStatus.FAILED,
                target_smali=existing,
                message=str(exc),
            ))
            print(f"[mtcr] FAILED: {class_name}: {exc}")

    # ── Added classes ─────────────────────────────────────────────────────────
    inject_root = _choose_inject_root(smali_roots, modified_root_names)

    for class_name in pack.added_classes:
        # Check all smali roots for pre-existing copy first.
        existing = _find_class_in_smali_roots(smali_roots, class_name)
        new_content = pack.b_content[class_name]

        if existing is not None:
            existing_content = existing.read_text(encoding="utf-8", errors="replace")
            if _sha256(existing_content) == _sha256(new_content):
                results.append(ClassResult(
                    class_name=class_name,
                    status=ClassStatus.EXISTS_IDENTICAL,
                    target_smali=existing,
                    message="already present, content identical",
                ))
                print(f"[mtcr] EXISTS_IDENTICAL: {class_name}")
            else:
                results.append(ClassResult(
                    class_name=class_name,
                    status=ClassStatus.CONFLICT,
                    target_smali=existing,
                    message="already present with different content; not overwritten",
                ))
                print(f"[mtcr] CONFLICT: {class_name} in {existing.parent.name}/")
            continue

        if inject_root is None:
            results.append(ClassResult(
                class_name=class_name,
                status=ClassStatus.FAILED,
                message="no smali_classes* directory found to inject into",
            ))
            continue

        target_smali = inject_root / (class_name + ".smali")

        if dry_run:
            results.append(ClassResult(
                class_name=class_name,
                status=ClassStatus.WOULD_ADD,
                target_smali=target_smali,
                message=f"would inject into {inject_root.name}/",
            ))
            print(f"[mtcr] WOULD_ADD: {class_name} -> {inject_root.name}/")
            continue

        # Execute: inject
        try:
            target_smali.parent.mkdir(parents=True, exist_ok=True)
            target_smali.write_text(new_content, encoding="utf-8")
            results.append(ClassResult(
                class_name=class_name,
                status=ClassStatus.ADDED,
                target_smali=target_smali,
                message=f"injected into {inject_root.name}/",
            ))
            print(f"[mtcr] ADDED: {class_name} -> {inject_root.name}/")
        except Exception as exc:
            results.append(ClassResult(
                class_name=class_name,
                status=ClassStatus.FAILED,
                target_smali=target_smali,
                message=str(exc),
            ))
            print(f"[mtcr] FAILED adding {class_name}: {exc}")

    return results
