"""Registry validator — verifies device codename and edition exist in registry."""
from __future__ import annotations

import sys
from pathlib import Path

_REGISTRY = Path(__file__).resolve().parents[2] / "registry"

_KNOWN_EDITIONS = {"base", "gaming", "legend", "epic"}


def validate_registry(codename: str | None = None, edition: str | None = None) -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    if edition:
        edition_lc = edition.strip().lower()
        if edition_lc not in _KNOWN_EDITIONS:
            edition_file = _REGISTRY / "editions" / f"{edition_lc}.yml"
            if not edition_file.is_file():
                errors.append(f"Edition '{edition}' not found in registry/editions/")
        else:
            edition_file = _REGISTRY / "editions" / f"{edition_lc}.yml"
            if not edition_file.is_file():
                warnings.append(f"registry/editions/{edition_lc}.yml missing (edition known but file absent)")

    if codename:
        codename_lc = codename.strip().lower()
        found_in_devices = False
        for soc_dir in ["mtk", "snapdragon"]:
            dev_file = _REGISTRY / "devices" / soc_dir / f"{codename_lc}.yml"
            if dev_file.is_file():
                found_in_devices = True
                break

        found_in_groups = False
        if not found_in_devices:
            for gf in [_REGISTRY / "device_groups" / "mtk.yml",
                       _REGISTRY / "device_groups" / "snapdragon.yml"]:
                if not gf.is_file():
                    continue
                try:
                    import yaml
                    group = yaml.safe_load(gf.read_text(encoding="utf-8")) or {}
                except ImportError:
                    group = {}
                for entry in group.get("devices", []):
                    if isinstance(entry, dict) and entry.get("codename", "").lower() == codename_lc:
                        found_in_groups = True
                        break
                if found_in_groups:
                    break

        if not found_in_devices and not found_in_groups:
            errors.append(
                f"Device '{codename}' not found in registry/devices/ or registry/device_groups/"
            )

    passed = not errors
    return {"passed": passed, "errors": errors, "warnings": warnings}


def main(argv: list[str] | None = None) -> int:
    import argparse
    p = argparse.ArgumentParser(description="Validate registry entries")
    p.add_argument("--codename", default=None)
    p.add_argument("--edition", default=None)
    args = p.parse_args(argv)
    result = validate_registry(args.codename, args.edition)
    for e in result["errors"]:
        print(f"[REGISTRY_ERROR] {e}", file=sys.stderr)
    for w in result["warnings"]:
        print(f"[REGISTRY_WARN] {w}")
    if result["passed"]:
        print("[REGISTRY] Validation passed.")
    else:
        print("[REGISTRY] Validation FAILED.", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
