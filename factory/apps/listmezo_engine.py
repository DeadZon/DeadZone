"""ListMezo Normalize Engine — Phase 1.

Normalizes app folder/APK names in a extracted ROM against the ListMezo guide,
reports missing and wrong-location apps, removes true extras, and edits
build.prop.  Defaults to dry_run; execute mode must be explicitly enabled.

Entry point: run_listmezo()
"""
from __future__ import annotations

import json
import os
import re
import shutil
import struct
import subprocess
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# ── Constants ─────────────────────────────────────────────────────────────────

SCOPED_DIRS = [
    "system/app",
    "system/priv-app",
    "product/app",
    "product/priv-app",
    "system_ext/app",
    "system_ext/priv-app",
]

COMPILED_ARTIFACTS = {"oat", "arm", "arm64"}
COMPILED_EXTENSIONS = {".odex", ".vdex", ".art", ".prof", ".dm"}

# All known header aliases → canonical path
_HEADER_ALIASES: dict[str, str] = {
    "system/system/app":        "system/app",
    "system/app":               "system/app",
    "system/ app":              "system/app",
    "system/system/priv-app":   "system/priv-app",
    "system/priv-app":          "system/priv-app",
    "system / priv-app":        "system/priv-app",
    "product/app":              "product/app",
    "product / app":            "product/app",
    "product/priv-app":         "product/priv-app",
    "product / priv-app":       "product/priv-app",
    "system_ext/app":           "system_ext/app",
    "system_ext / app":         "system_ext/app",
    "system_ext/priv-app":      "system_ext/priv-app",
    "system_ext / priv-app":    "system_ext/priv-app",
    "system/system/build.prop": "system/build.prop",
    "system/build.prop":        "system/build.prop",
    "system / build.prop":      "system/build.prop",
}

_BUILDPROP_REPLACE = {
    "ro.build.host": "ro.build.host=xiaomi.deadzone",
    "ro.product.locale": "ro.product.locale=en-GB",
}
_BUILDPROP_REMOVE = {
    "ro.miui.has_security_keyboard=1",
    "ro.miui.support_miui_ime_bottom=1",
}

# ── Data models ───────────────────────────────────────────────────────────────

@dataclass
class GuideEntry:
    location: str           # canonical e.g. "product/priv-app"
    folder: str             # expected folder name
    package: str            # expected package name
    allowed_apks: list[str] = field(default_factory=list)   # extra allowed APK names

@dataclass
class GuideWarning:
    line_no: int
    raw: str
    reason: str

@dataclass
class ParsedGuide:
    entries: list[GuideEntry] = field(default_factory=list)
    buildprop_section: bool = False
    warnings: list[GuideWarning] = field(default_factory=list)

@dataclass
class RomApp:
    package: str
    partition_dir: str      # one of SCOPED_DIRS
    folder_path: Path       # absolute
    folder_name: str
    apk_path: Path
    apk_name: str

# ── Guide parser ──────────────────────────────────────────────────────────────

def _normalize_header(raw: str) -> Optional[str]:
    """Return canonical path if raw is a known header alias, else None."""
    key = re.sub(r"\s+", " ", raw.strip().lower().rstrip("/"))
    return _HEADER_ALIASES.get(key)


def _is_apk_line(s: str) -> bool:
    return s.lower().endswith(".apk")


def _is_valid_package(s: str) -> bool:
    """Loose check: contains a dot, no spaces, doesn't end in .apk."""
    s = s.strip()
    if not s or " " in s or _is_apk_line(s):
        return False
    return "." in s


def parse_guide(guide_path: Path) -> ParsedGuide:
    result = ParsedGuide()
    lines = guide_path.read_text(encoding="utf-8", errors="ignore").splitlines()

    current_location: Optional[str] = None
    in_buildprop = False
    pending: list[tuple[int, str]] = []   # (line_no, stripped_text) for current entry

    def flush_pending():
        nonlocal pending
        if not pending or current_location is None or in_buildprop:
            pending = []
            return
        # Filter out blank lines and noise already stripped
        tokens = [(n, t) for n, t in pending if t]
        pending = []
        if not tokens:
            return

        folder_line_no, folder = tokens[0]

        if len(tokens) < 2:
            result.warnings.append(GuideWarning(folder_line_no, folder, "entry_has_no_package"))
            return

        pkg_line_no, pkg = tokens[1]

        # Validate package
        if not _is_valid_package(pkg):
            result.warnings.append(GuideWarning(
                pkg_line_no,
                f"{folder} / {pkg}",
                f"invalid_package_value: {pkg!r}",
            ))
            return

        # Collect allowed APK lines (tokens[2:])
        allowed: list[str] = []
        for _, tok in tokens[2:]:
            if _is_apk_line(tok):
                allowed.append(tok)
            elif tok.lower() == "or":
                pass   # skip stray "or" tokens
            else:
                result.warnings.append(GuideWarning(0, tok, "unexpected_token_after_package"))

        result.entries.append(GuideEntry(
            location=current_location,
            folder=folder.strip(),
            package=pkg.strip(),
            allowed_apks=allowed,
        ))

    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        i += 1

        # Skip separator lines
        if re.fullmatch(r"[=\-*]+", stripped):
            flush_pending()
            continue

        # Check for header alias
        canonical = _normalize_header(stripped)
        if canonical is not None:
            flush_pending()
            if canonical == "system/build.prop":
                in_buildprop = True
                result.buildprop_section = True
                current_location = canonical
            else:
                in_buildprop = False
                current_location = canonical
            continue

        # Skip "or" lines that appear as standalone header aliases
        if stripped.lower() == "or":
            continue

        # Skip build.prop instruction prose / action lines
        if in_buildprop:
            continue

        # Skip obvious instruction prose (long sentences)
        if len(stripped.split()) > 6 and stripped.endswith((".", ",")):
            continue
        # Skip known instruction fragments from the guide
        if stripped.lower() in (
            "remove",
            "fine package name",
            "file name of apk and package name",
            "fine lines and replace",
            "fine and remove",
            "any other waiting for finish and delate if you not found in guide",
        ):
            continue
        if stripped.startswith("any other"):
            continue

        if not stripped:
            flush_pending()
            continue

        if current_location is None:
            continue

        # Accumulate tokens for current entry
        pending.append((i, stripped))

    flush_pending()
    return result


# ── APK package name extraction ───────────────────────────────────────────────

def _run(*cmd: str) -> Optional[str]:
    try:
        r = subprocess.run(list(cmd), capture_output=True, text=True, timeout=15)
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None


def _extract_package_aapt2(apk: Path) -> Optional[str]:
    out = _run("aapt2", "dump", "badging", str(apk))
    if out:
        m = re.search(r"^package:\s+name='([^']+)'", out, re.MULTILINE)
        if m:
            return m.group(1)
    return None


def _extract_package_aapt(apk: Path) -> Optional[str]:
    out = _run("aapt", "dump", "badging", str(apk))
    if out:
        m = re.search(r"^package:\s+name='([^']+)'", out, re.MULTILINE)
        if m:
            return m.group(1)
    return None


def _extract_package_binary(apk: Path) -> Optional[str]:
    """Fallback: scan binary AndroidManifest.xml string pool for package name."""
    try:
        with zipfile.ZipFile(apk, "r") as zf:
            if "AndroidManifest.xml" not in zf.namelist():
                return None
            data = zf.read("AndroidManifest.xml")
    except Exception:
        return None

    # Binary XML: magic 0x00080003, then chunks.  We look for the string pool
    # (chunk type 0x0001) and extract all UTF-16LE strings, then heuristically
    # pick the package name (first string with 2+ dots, no spaces, length < 80).
    if len(data) < 8:
        return None
    # String pool chunk starts at offset 8 (after file header chunk header)
    # Chunk header: type(2), headerSize(2), chunkSize(4)
    pos = 8
    while pos + 8 < len(data):
        chunk_type, header_sz, chunk_sz = struct.unpack_from("<HHI", data, pos)
        if chunk_sz == 0:
            break
        if chunk_type == 0x0001:   # RES_STRING_POOL_TYPE
            # stringCount at offset 8 from chunk start
            if pos + 28 > len(data):
                break
            string_count, style_count, flags, strings_start, styles_start = struct.unpack_from(
                "<IIIII", data, pos + 8
            )
            utf8_flag = bool(flags & (1 << 8))
            index_start = pos + header_sz
            candidates: list[str] = []
            for si in range(min(string_count, 200)):
                idx_off = index_start + si * 4
                if idx_off + 4 > len(data):
                    break
                (str_off,) = struct.unpack_from("<I", data, idx_off)
                abs_off = pos + strings_start + str_off
                if abs_off + 2 > len(data):
                    continue
                try:
                    if utf8_flag:
                        # UTF-8: first byte = char len, second = byte len
                        char_len = data[abs_off] & 0x7F
                        byte_len = data[abs_off + 1] & 0x7F
                        s = data[abs_off + 2: abs_off + 2 + byte_len].decode("utf-8", errors="ignore")
                    else:
                        (str_len,) = struct.unpack_from("<H", data, abs_off)
                        s = data[abs_off + 2: abs_off + 2 + str_len * 2].decode("utf-16-le", errors="ignore")
                    if s and "." in s and " " not in s and not s.endswith(".apk") and len(s) < 80:
                        candidates.append(s)
                except Exception:
                    continue
            # The package name is typically among the first few strings
            for c in candidates[:10]:
                if c.count(".") >= 1 and re.match(r"^[a-zA-Z][a-zA-Z0-9_.]+$", c):
                    return c
            break
        pos += chunk_sz
    return None


def extract_package_name(apk: Path) -> Optional[str]:
    """Try aapt2, aapt, then binary fallback. Return None if all fail."""
    return (
        _extract_package_aapt2(apk)
        or _extract_package_aapt(apk)
        or _extract_package_binary(apk)
    )


# ── ROM scanner ───────────────────────────────────────────────────────────────

def scan_rom(rom_root: Path) -> tuple[dict[str, RomApp], list[dict]]:
    """
    Walk scoped directories in the extracted ROM.

    Returns:
        index: package_name -> RomApp  (first found if duplicate)
        unknown: list of dicts for APKs whose package could not be determined
    """
    index: dict[str, RomApp] = {}
    unknown: list[dict] = []

    for rel_dir in SCOPED_DIRS:
        scan_root = rom_root / rel_dir
        if not scan_root.is_dir():
            continue
        # Each immediate subdirectory is an app folder
        for app_folder in sorted(scan_root.iterdir()):
            if not app_folder.is_dir():
                continue
            # Find APKs directly inside the folder (not in oat/ etc.)
            apks = [f for f in app_folder.iterdir() if f.suffix.lower() == ".apk"]
            if not apks:
                continue
            apk = apks[0]   # primary APK
            pkg = extract_package_name(apk)
            if pkg is None:
                unknown.append({
                    "path": str(apk.relative_to(rom_root)),
                    "reason": "failed_to_extract_package_name",
                    "action": "kept",
                })
                continue
            if pkg not in index:
                index[pkg] = RomApp(
                    package=pkg,
                    partition_dir=rel_dir,
                    folder_path=app_folder,
                    folder_name=app_folder.name,
                    apk_path=apk,
                    apk_name=apk.name,
                )

    return index, unknown


# ── Compiled artifact removal ─────────────────────────────────────────────────

def _remove_compiled(folder: Path, dry_run: bool) -> list[str]:
    removed: list[str] = []
    if not folder.is_dir():
        return removed
    for item in folder.iterdir():
        if item.is_dir() and item.name in COMPILED_ARTIFACTS:
            removed.append(str(item))
            if not dry_run:
                shutil.rmtree(item, ignore_errors=True)
        elif item.is_file() and item.suffix.lower() in COMPILED_EXTENSIONS:
            removed.append(str(item))
            if not dry_run:
                item.unlink(missing_ok=True)
    return removed


# ── Matching + action engine ──────────────────────────────────────────────────

@dataclass
class MatchResult:
    found_ok: list[dict] = field(default_factory=list)
    renamed: list[dict] = field(default_factory=list)
    missing: list[dict] = field(default_factory=list)
    wrong_location: list[dict] = field(default_factory=list)
    extras: list[dict] = field(default_factory=list)
    conflicts: list[dict] = field(default_factory=list)


def _safe_rename_folder(
    rom_app: RomApp,
    entry: GuideEntry,
    dry_run: bool,
    conflicts: list[dict],
) -> Optional[dict]:
    """Rename folder (and primary APK) to match guide. Returns renamed dict or None on conflict."""
    old_folder = rom_app.folder_path
    new_folder = old_folder.parent / entry.folder

    # Determine new APK name
    if entry.allowed_apks:
        # Keep existing APK name if it's in the allowed list; else rename to folder.apk
        if rom_app.apk_name in entry.allowed_apks:
            new_apk_name = rom_app.apk_name
        else:
            new_apk_name = f"{entry.folder}.apk"
    else:
        new_apk_name = f"{entry.folder}.apk"

    # Check for conflict at target
    if new_folder.exists() and new_folder != old_folder:
        # Check if target contains the same package
        target_apks = [f for f in new_folder.iterdir() if f.suffix.lower() == ".apk"] if new_folder.is_dir() else []
        if target_apks:
            target_pkg = extract_package_name(target_apks[0])
            if target_pkg != entry.package:
                conflicts.append({
                    "package": entry.package,
                    "old_folder": rom_app.folder_name,
                    "new_folder": entry.folder,
                    "conflict_with_package": target_pkg,
                    "path": str(new_folder),
                    "action": "kept_original_conflict",
                })
                return None

    rec = {
        "package": entry.package,
        "old_folder": rom_app.folder_name,
        "new_folder": entry.folder,
        "old_apk": rom_app.apk_name,
        "new_apk": new_apk_name,
        "path": str((old_folder.parent / entry.folder).relative_to(old_folder.parent.parent.parent)),
    }

    if not dry_run:
        # Rename APK inside folder first
        old_apk = rom_app.folder_path / rom_app.apk_name
        new_apk_path = rom_app.folder_path / new_apk_name
        if old_apk.exists() and old_apk != new_apk_path:
            old_apk.rename(new_apk_path)
        # Rename folder
        if old_folder != new_folder:
            old_folder.rename(new_folder)

    return rec


def run_matching(
    guide: ParsedGuide,
    rom_index: dict[str, RomApp],
    rom_root: Path,
    dry_run: bool,
) -> MatchResult:
    result = MatchResult()

    # Build set of all guide packages for extras detection
    guide_packages: set[str] = {e.package for e in guide.entries}

    # Track which ROM apps were claimed by the guide
    claimed: set[str] = set()

    for entry in guide.entries:
        pkg = entry.package
        rom_app = rom_index.get(pkg)

        if rom_app is None:
            result.missing.append({
                "location": entry.location,
                "folder": entry.folder,
                "package": pkg,
                "expected_apk": f"{entry.folder}.apk",
                "reason": "package_not_found",
            })
            continue

        claimed.add(pkg)

        # Check if in correct location
        if rom_app.partition_dir != entry.location:
            result.wrong_location.append({
                "package": pkg,
                "current_path": str(rom_app.folder_path.relative_to(rom_root)),
                "expected_path": f"{entry.location}/{entry.folder}",
                "action": "kept_not_moved_phase_1",
            })
            continue

        # Remove compiled artifacts
        _remove_compiled(rom_app.folder_path, dry_run)

        folder_ok = rom_app.folder_name == entry.folder
        # APK name check
        if entry.allowed_apks:
            apk_ok = rom_app.apk_name in entry.allowed_apks
        else:
            apk_ok = rom_app.apk_name == f"{entry.folder}.apk"

        if folder_ok and apk_ok:
            result.found_ok.append({
                "package": pkg,
                "path": str(rom_app.folder_path.relative_to(rom_root)),
                "apk": rom_app.apk_name,
            })
        else:
            rec = _safe_rename_folder(rom_app, entry, dry_run, result.conflicts)
            if rec is not None:
                result.renamed.append(rec)
            else:
                # Conflict — still count as found (not missing, not extra)
                pass

    # Extras: ROM apps in scoped dirs whose package is not in guide
    for pkg, rom_app in rom_index.items():
        if pkg in claimed:
            continue
        if pkg in guide_packages:
            # In guide but wrong location — already reported above
            continue
        # True extra
        rec = {
            "path": str(rom_app.folder_path.relative_to(rom_root)),
            "apk": rom_app.apk_name,
            "package": pkg,
            "reason": "package_not_in_ListMezo_guide",
        }
        result.extras.append(rec)
        if not dry_run:
            shutil.rmtree(rom_app.folder_path, ignore_errors=True)

    return result


# ── Build.prop editor ─────────────────────────────────────────────────────────

def apply_buildprop(rom_root: Path, dry_run: bool) -> list[str]:
    """Apply build.prop changes. Returns list of change descriptions."""
    changes: list[str] = []
    bp_path = rom_root / "system" / "build.prop"
    if not bp_path.is_file():
        changes.append("SKIP: system/build.prop not found")
        return changes

    original = bp_path.read_text(encoding="utf-8", errors="ignore")
    lines = original.splitlines(keepends=True)
    new_lines: list[str] = []
    replaced_keys: set[str] = set()
    added_keys: set[str] = set()

    for line in lines:
        stripped = line.rstrip("\n\r")
        # Check remove list
        if stripped in _BUILDPROP_REMOVE:
            changes.append(f"REMOVED: {stripped}")
            continue
        # Check replace list
        key = stripped.split("=", 1)[0].strip() if "=" in stripped else None
        if key and key in _BUILDPROP_REPLACE:
            new_val = _BUILDPROP_REPLACE[key]
            if stripped != new_val:
                changes.append(f"REPLACED: {stripped!r} -> {new_val!r}")
            else:
                changes.append(f"ALREADY_OK: {stripped}")
            new_lines.append(new_val + "\n")
            replaced_keys.add(key)
            continue
        new_lines.append(line if line.endswith("\n") else line + "\n")

    # Add missing keys
    for key, new_val in _BUILDPROP_REPLACE.items():
        if key not in replaced_keys:
            new_lines.append(new_val + "\n")
            added_keys.add(key)
            changes.append(f"ADDED: {new_val!r}")

    if not dry_run:
        bp_path.write_text("".join(new_lines), encoding="utf-8")

    return changes


# ── Report writers ────────────────────────────────────────────────────────────

def _write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def write_reports(
    report_dir: Path,
    guide_path: Path,
    rom_root: Path,
    mode: str,
    guide: ParsedGuide,
    match: MatchResult,
    unknown: list[dict],
    buildprop_changes: list[str],
) -> None:
    report_dir.mkdir(parents=True, exist_ok=True)

    _write_json(report_dir / "missing_apps.json", match.missing)
    _write_json(report_dir / "removed_extras.json", match.extras)
    _write_json(report_dir / "wrong_location.json", match.wrong_location)
    _write_json(report_dir / "renamed_apps.json", match.renamed)
    _write_json(report_dir / "unknown_apks.json", unknown)

    guide_warn_data = [
        {"line_no": w.line_no, "raw": w.raw, "reason": w.reason}
        for w in guide.warnings
    ]
    _write_json(report_dir / "guide_warnings.json", guide_warn_data)

    # Main text report
    lines: list[str] = [
        "[LISTMEZO FREE REPORT]",
        f"Guide path: {guide_path}",
        f"Mode: {mode}",
        f"ROM root: {rom_root}",
        "",
        "[SUMMARY]",
        f"Total guide apps: {len(guide.entries)}",
        f"Found OK: {len(match.found_ok)}",
        f"Renamed: {len(match.renamed)}",
        f"Missing: {len(match.missing)}",
        f"Wrong location: {len(match.wrong_location)}",
        f"Removed extras: {len(match.extras)}",
        f"Unknown APKs: {len(unknown)}",
        f"Conflicts: {len(match.conflicts)}",
        "",
        "[FOUND_OK]",
    ]
    for r in match.found_ok:
        lines.append(f"  {r['package']}  {r['path']}/{r['apk']}")

    lines += ["", "[RENAMED]"]
    for r in match.renamed:
        lines.append(f"  {r['package']}  {r['old_folder']} -> {r['new_folder']}  APK: {r['old_apk']} -> {r['new_apk']}")

    lines += ["", "[MISSING]"]
    for r in match.missing:
        lines.append(f"  {r['package']}  expected: {r['location']}/{r['folder']}/{r['expected_apk']}")

    lines += ["", "[WRONG_LOCATION]"]
    for r in match.wrong_location:
        lines.append(f"  {r['package']}  current: {r['current_path']}  expected: {r['expected_path']}")

    lines += ["", "[REMOVED_EXTRAS]"]
    for r in match.extras:
        lines.append(f"  {r['package']}  {r['path']}")

    lines += ["", "[UNKNOWN]"]
    for r in unknown:
        lines.append(f"  {r['path']}  ({r['reason']})")

    lines += ["", "[CONFLICTS]"]
    for r in match.conflicts:
        lines.append(f"  {r['package']}  {r.get('old_folder')} -> {r.get('new_folder')} CONFLICT with {r.get('conflict_with_package')}")

    lines += ["", "[BUILD_PROP_CHANGES]"]
    for c in buildprop_changes:
        lines.append(f"  {c}")

    (report_dir / "listmezo_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ── Main entry ────────────────────────────────────────────────────────────────

def run_listmezo(
    rom_root: Path | str,
    edition: str = "free",
    mode: str = "dry_run",
    output_dir: Optional[Path | str] = None,
    listmezo_root: Optional[Path | str] = None,
) -> dict:
    """
    Run the ListMezo Normalize Engine.

    Args:
        rom_root:      Path to the extracted ROM root (contains system/, product/, etc.)
        edition:       Edition name — only "free" is active in phase 1.
        mode:          "dry_run" (default) or "execute".
        output_dir:    Base output directory; reports land in <output_dir>/reports/listmezo/<edition>/.
        listmezo_root: Root of the ListMezo guide directory (default: repo_root/ListMezo/).

    Returns dict with keys: edition, mode, status, summary, report_dir, errors.
    """
    from factory.core.paths import REPO_ROOT

    rom_root = Path(rom_root).resolve()
    dry_run = mode != "execute"

    if listmezo_root is None:
        listmezo_root = REPO_ROOT / "ListMezo"
    listmezo_root = Path(listmezo_root).resolve()

    guide_path = listmezo_root / edition / "apps.list"

    # Resolve output report directory
    if output_dir is None:
        output_dir = REPO_ROOT / "output"
    report_dir = Path(output_dir) / "reports" / "listmezo" / edition

    errors: list[str] = []

    # Check edition support
    if not guide_path.is_file():
        msg = f"No ListMezo guide for edition '{edition}' at {guide_path} — skipping."
        print(f"[ListMezo] {msg}")
        return {
            "edition": edition,
            "mode": mode,
            "status": "SKIPPED",
            "reason": msg,
            "errors": [],
        }

    print(f"[ListMezo] edition={edition} mode={mode} guide={guide_path}")

    # Parse guide
    guide = parse_guide(guide_path)
    print(f"[ListMezo] Guide entries: {len(guide.entries)}  Warnings: {len(guide.warnings)}")

    # Scan ROM
    rom_index, unknown = scan_rom(rom_root)
    print(f"[ListMezo] ROM apps found: {len(rom_index)}  Unknown: {len(unknown)}")

    # Match + act
    match = run_matching(guide, rom_index, rom_root, dry_run)

    # Build.prop
    buildprop_changes = apply_buildprop(rom_root, dry_run)

    # Reports (always written)
    write_reports(report_dir, guide_path, rom_root, mode, guide, match, unknown, buildprop_changes)

    summary = {
        "total_guide_apps": len(guide.entries),
        "found_ok": len(match.found_ok),
        "renamed": len(match.renamed),
        "missing": len(match.missing),
        "wrong_location": len(match.wrong_location),
        "removed_extras": len(match.extras),
        "unknown_apks": len(unknown),
        "conflicts": len(match.conflicts),
        "guide_warnings": len(guide.warnings),
        "buildprop_changes": len(buildprop_changes),
    }

    print(f"[ListMezo] Summary: {summary}")
    print(f"[ListMezo] Reports written to: {report_dir}")

    return {
        "edition": edition,
        "mode": mode,
        "status": "DRY_RUN" if dry_run else "EXECUTED",
        "summary": summary,
        "report_dir": str(report_dir),
        "errors": errors,
    }


# ── CLI shim ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    from factory.core.paths import REPO_ROOT

    ap = argparse.ArgumentParser(description="ListMezo Normalize Engine")
    ap.add_argument("rom_root", help="Path to extracted ROM root")
    ap.add_argument("--edition", default="free")
    ap.add_argument("--mode", choices=["dry_run", "execute"], default="dry_run")
    ap.add_argument("--output-dir", default=None)
    args = ap.parse_args()

    result = run_listmezo(
        rom_root=args.rom_root,
        edition=args.edition,
        mode=args.mode,
        output_dir=args.output_dir,
    )
    print(json.dumps(result, indent=2))
