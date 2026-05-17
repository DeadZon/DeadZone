"""
Check or regenerate device panel group files against SuperConfig.

Usage:
    python factory/tools/sync_device_panels_from_superconfig.py --check
    python factory/tools/sync_device_panels_from_superconfig.py --generate
"""

import argparse
import sys
from pathlib import Path

# Allow running as a plain script from the repo root as well as with -m
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

try:
    import yaml
except ImportError:
    print("[ERROR] PyYAML not installed. Run: pip install PyYAML", file=sys.stderr)
    sys.exit(1)

from factory.core.paths import MEZO_CORE, REGISTRY_ROOT

SUPERCONFIG_ROOT = MEZO_CORE / "SuperConfig"
DEVICE_GROUPS_DIR = REGISTRY_ROOT / "device_groups"


def _load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def _get_superconfig_codenames() -> set[str]:
    if not SUPERCONFIG_ROOT.exists():
        print(f"[ERROR] SuperConfig not found: {SUPERCONFIG_ROOT}", file=sys.stderr)
        sys.exit(1)
    return {d.name for d in SUPERCONFIG_ROOT.iterdir() if d.is_dir()}


def _get_grouped_codenames() -> dict[str, str]:
    """Return {codename: group_name} for all entries in all device_group files."""
    grouped: dict[str, str] = {}
    for gf in DEVICE_GROUPS_DIR.glob("*.yml"):
        try:
            data = _load_yaml(gf)
        except Exception as e:
            print(f"[WARN] Cannot parse {gf.name}: {e}")
            continue
        for entry in data.get("devices", []):
            c = entry.get("codename")
            if c:
                grouped[c] = gf.stem
    return grouped


def cmd_check() -> bool:
    print("[CHECK] Comparing SuperConfig folders against device panel groups...")
    sc = _get_superconfig_codenames()
    grouped = _get_grouped_codenames()

    ok = True

    # SuperConfig devices not in any group
    ungrouped = sc - set(grouped.keys())
    if ungrouped:
        print(f"\n[FAIL] {len(ungrouped)} SuperConfig device(s) not assigned to any panel:")
        for c in sorted(ungrouped):
            print(f"  - {c}")
        ok = False
    else:
        print(f"  [OK] All {len(sc)} SuperConfig devices are assigned to a panel group")

    # Devices in groups that don't exist in SuperConfig (manual/golden is expected)
    not_in_sc = set(grouped.keys()) - sc
    manual_ok = set()
    for c in not_in_sc:
        # Look up source to distinguish manual entries
        gname = grouped[c]
        gf = DEVICE_GROUPS_DIR / f"{gname}.yml"
        try:
            data = _load_yaml(gf)
            for entry in data.get("devices", []):
                if entry.get("codename") == c and entry.get("source") == "manual":
                    manual_ok.add(c)
                    break
        except Exception:
            pass

    unexpected = not_in_sc - manual_ok
    if manual_ok:
        print(f"  [OK] {len(manual_ok)} manual device(s) not in SuperConfig: {sorted(manual_ok)}")
    if unexpected:
        print(f"\n[WARN] {len(unexpected)} grouped device(s) not in SuperConfig and not marked manual:")
        for c in sorted(unexpected):
            print(f"  - {c} (group: {grouped[c]})")

    # Duplicates
    seen: dict[str, list[str]] = {}
    for gf in DEVICE_GROUPS_DIR.glob("*.yml"):
        try:
            data = _load_yaml(gf)
        except Exception:
            continue
        for entry in data.get("devices", []):
            c = entry.get("codename")
            if c:
                seen.setdefault(c, []).append(gf.stem)
    dupes = {c: groups for c, groups in seen.items() if len(groups) > 1}
    if dupes:
        print(f"\n[FAIL] {len(dupes)} duplicate codename(s) across groups:")
        for c, groups in sorted(dupes.items()):
            print(f"  - {c}: {groups}")
        ok = False
    else:
        print(f"  [OK] No duplicate codenames across groups")

    # Summary
    sd = sum(1 for g in grouped.values() if g == "snapdragon")
    mtk = sum(1 for g in grouped.values() if g == "mtk")
    print(f"\n[SUMMARY]")
    print(f"  SuperConfig devices : {len(sc)}")
    print(f"  Snapdragon panel    : {sd}")
    print(f"  MTK panel           : {mtk}")
    print(f"  Manual (non-SC)     : {len(manual_ok)}")

    if ok:
        print("\n[PASS] All SuperConfig devices are assigned to panels.")
    else:
        print("\n[FAIL] Fix the issues listed above before committing.")
    return ok


def cmd_generate() -> None:
    print("[GENERATE] This mode would regenerate device_groups YAMLs from the canonical mapping.")
    print("[GENERATE] Not implemented in this phase — edit device_groups/*.yml directly.")
    print("[GENERATE] Use --check to verify current state.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync/check device panel groups against SuperConfig."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="Check coverage and report issues")
    group.add_argument("--generate", action="store_true", help="Regenerate group files (not yet implemented)")
    args = parser.parse_args()

    if args.generate:
        cmd_generate()
    else:
        ok = cmd_check()
        sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
