"""
Legend single-home validator.

Scans the repo and fails if it finds active Legend-specific files or
references outside factory/patch/legend/.

Allowed exceptions:
  - registry/flavors/deadzone_legend.yml  (metadata only)
  - .github/workflows/*.yml               (launchers only)
  - docs / README files
  - factory/patch/legend/archived_legacy/ (dead archive, not executed)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[5]

_LEGEND_HOME = _REPO_ROOT / "factory" / "patch" / "legend"

# Patterns that indicate a stray active Legend reference.
_STRAY_PATTERNS: list[re.Pattern] = [
    re.compile(r"factory[/\\]assets[/\\]legend", re.IGNORECASE),
    re.compile(r"flavors[/\\]legend(?!\.yml)", re.IGNORECASE),
    re.compile(r"\bMEZO_LEGEND\b"),
    re.compile(r"Legend[/\\]jar", re.IGNORECASE),
    re.compile(r"third_party[/\\]mezo_core[/\\]MEZO_LEGEND", re.IGNORECASE),
]

# Paths that are explicitly allowed to reference Legend.
_ALLOWED_PREFIXES: tuple[Path, ...] = (
    _LEGEND_HOME / "archived_legacy",
    _REPO_ROOT / "registry" / "flavors",
    _REPO_ROOT / ".github" / "workflows",
)

_ALLOWED_SUFFIXES = (".md", ".txt", ".rst")
_SKIP_DIRS = {".git", "__pycache__", ".mypy_cache", "node_modules", "output"}

# Specific repo-relative file paths exempt from the single-home rule.
# These reference MEZO_LEGEND or legend paths in validator/config context only,
# not as runtime patch logic.
_ALLOWED_REL_PATHS: frozenset[str] = frozenset({
    ".dockerignore",
    "scripts/rewrite_critical_text_files.py",
    # This file defines the patterns it scans for — must exempt itself.
    "factory/patch/mods/legend/actions/validate_legend_home.py",
    # References forbidden legend paths as strings inside validator definitions.
    "factory/validators/mod_structure_validator.py",
})


def _is_exempt(path: Path) -> bool:
    if path.suffix in _ALLOWED_SUFFIXES:
        return True
    try:
        rel = path.relative_to(_REPO_ROOT).as_posix()
        if rel in _ALLOWED_REL_PATHS:
            return True
    except ValueError:
        pass
    for prefix in _ALLOWED_PREFIXES:
        try:
            path.relative_to(prefix)
            return True
        except ValueError:
            pass
    return False


def _scan(repo_root: Path) -> list[dict]:
    """Return list of violation dicts found outside the Legend home."""
    violations: list[dict] = []

    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in _SKIP_DIRS for part in path.parts):
            continue

        # Files inside the Legend home are fine.
        try:
            path.relative_to(_LEGEND_HOME)
            continue
        except ValueError:
            pass

        if _is_exempt(path):
            continue

        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        for pat in _STRAY_PATTERNS:
            for match in pat.finditer(text):
                line_no = text[: match.start()].count("\n") + 1
                violations.append({
                    "file": str(path.relative_to(repo_root)),
                    "line": line_no,
                    "pattern": pat.pattern,
                    "snippet": text[max(0, match.start() - 40): match.end() + 40].strip(),
                })

    return violations


def validate(repo_root: Path | None = None, *, quiet: bool = False) -> dict:
    """
    Run the single-home validation scan.

    Returns
    -------
    dict with keys: passed (bool), violations (list[dict])
    """
    root = Path(repo_root) if repo_root else _REPO_ROOT
    violations = _scan(root)
    passed = len(violations) == 0

    if not quiet:
        if passed:
            print("[validate_legend_home] PASSED — no stray Legend references found")
        else:
            print(f"[validate_legend_home] FAILED — {len(violations)} violation(s) found:")
            for v in violations:
                print(f"  {v['file']}:{v['line']}  pattern={v['pattern']!r}")
                print(f"    {v['snippet']}")

    return {"passed": passed, "violations": violations}


def main(argv: list[str] | None = None) -> int:
    import argparse
    p = argparse.ArgumentParser(description="Validate DeadZone Legend single-home rule")
    p.add_argument("--repo", type=Path, default=None, help="Repo root (default: auto-detect)")
    p.add_argument("--quiet", action="store_true")
    args = p.parse_args(argv)

    result = validate(args.repo, quiet=args.quiet)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
