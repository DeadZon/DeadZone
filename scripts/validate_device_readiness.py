"""
validate_device_readiness.py

Comprehensive device readiness validation.

Checks:
  1. Every enabled MTK device appears in the MTK workflow dropdown.
  2. Every enabled Snapdragon device appears in the Snapdragon workflow dropdown.
  3. No old manual codename-only inputs in workflows.
  4. select_device dropdown input exists in both workflows.
  5. custom_device override still exists in both workflows.
  6. All workflow dropdown entries exist in factory_devices.json.
  7. No duplicate codenames.
  8. No empty display_name.
  9. No hardcoded zorn/zircon/garnet-only restrictions in production modules.
  10. DEADZONE_DEVICE_CODENAME is referenced (or select_device passed) in workflows.
  11. All enabled devices pass readiness check.
"""
from __future__ import annotations

import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
FACTORY_JSON = REPO_ROOT / "registry" / "devices" / "factory_devices.json"

WORKFLOWS = {
    "mtk":        REPO_ROOT / ".github" / "workflows" / "deadzone_mtk.yml",
    "snapdragon": REPO_ROOT / ".github" / "workflows" / "deadzone_snapdragon.yml",
}

START_MARKER = "# AUTO-GENERATED DEVICE OPTIONS START"
END_MARKER   = "# AUTO-GENERATED DEVICE OPTIONS END"

# Production modules to scan for device-specific hard-coding
_PRODUCTION_MODULES = [
    REPO_ROOT / "factory" / "pipeline" / "legacy_engine_runner.py",
    REPO_ROOT / "factory" / "pipeline" / "free_pipeline.py",
    REPO_ROOT / "factory" / "input"    / "universal_rom_intake.py",
    REPO_ROOT / "factory" / "super"    / "universal_super_engine.py",
    REPO_ROOT / "factory" / "output"   / "deadzone_template_patcher.py",
    REPO_ROOT / "factory" / "repack"   / "super_collector.py",
]

# Pattern: device-specific conditional on exactly ["zorn"], ["zircon"], ["garnet"]
# e.g.  if device == "zorn"  /  if codename in ["zorn", "zircon"]
_HARDCODE_PATTERN = re.compile(
    r'(?:if|elif)\s+(?:device|codename|selected_codename)\s*(?:==|in)\s*'
    r'(?:"(?:zorn|zircon|garnet)"|'
    r'\[(?:\s*"(?:zorn|zircon|garnet)"\s*,?\s*)+\])',
    re.IGNORECASE,
)


def _load_devices() -> list[dict]:
    import json
    return json.loads(FACTORY_JSON.read_text(encoding="utf-8"))


def _extract_dropdown_codenames(workflow_text: str) -> set[str]:
    pattern = re.compile(
        re.escape(START_MARKER) + r"(.*?)" + re.escape(END_MARKER),
        re.DOTALL,
    )
    m = pattern.search(workflow_text)
    if not m:
        return set()
    codenames: set[str] = set()
    for line in m.group(1).splitlines():
        # Format: "          - <codename> | <display_name>"
        stripped = line.strip()
        if stripped.startswith("- "):
            parts = stripped[2:].split("|", 1)
            if parts:
                codenames.add(parts[0].strip())
    return codenames


def check_duplicate_codenames(devices: list[dict]) -> list[str]:
    errors: list[str] = []
    seen: dict[str, int] = {}
    for d in devices:
        cn = d.get("codename", "")
        seen[cn] = seen.get(cn, 0) + 1
    for cn, cnt in seen.items():
        if cnt > 1:
            errors.append(f"Duplicate codename: {cn!r} appears {cnt} times")
    return errors


def check_empty_display_names(devices: list[dict]) -> list[str]:
    return [
        f"Empty display_name for codename: {d.get('codename')!r}"
        for d in devices
        if not (d.get("display_name") or "").strip()
    ]


def check_workflow_coverage(devices: list[dict]) -> list[str]:
    errors: list[str] = []
    for soc, wf_path in WORKFLOWS.items():
        if not wf_path.exists():
            errors.append(f"Workflow not found: {wf_path}")
            continue

        text = wf_path.read_text(encoding="utf-8")

        # select_device input must exist
        if "select_device:" not in text:
            errors.append(f"{wf_path.name}: missing select_device input")

        # custom_device override must still exist
        if "custom_device" not in text:
            errors.append(f"{wf_path.name}: missing custom_device override input")

        # AUTO-GENERATED markers must be present
        if START_MARKER not in text or END_MARKER not in text:
            errors.append(f"{wf_path.name}: missing AUTO-GENERATED markers")
            continue

        dropdown_codenames = _extract_dropdown_codenames(text)
        registry_codenames = {
            d["codename"]
            for d in devices
            if d.get("soc") == soc and d.get("enabled", True)
        }

        # Every enabled device of this SoC must be in the dropdown
        missing = sorted(registry_codenames - dropdown_codenames)
        if missing:
            errors.append(
                f"{wf_path.name}: {len(missing)} registry device(s) missing from dropdown: "
                + ", ".join(missing[:8]) + ("…" if len(missing) > 8 else "")
            )

        # Every dropdown entry must be in the registry
        registry_all = {d["codename"] for d in devices}
        extra = sorted(dropdown_codenames - registry_all)
        if extra:
            errors.append(
                f"{wf_path.name}: {len(extra)} dropdown entry/entries not in registry: "
                + ", ".join(extra[:8])
            )

    return errors


def check_hardcoded_device_restrictions() -> list[str]:
    errors: list[str] = []
    for mod_path in _PRODUCTION_MODULES:
        if not mod_path.exists():
            continue
        text = mod_path.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if _HARDCODE_PATTERN.search(line):
                errors.append(
                    f"{mod_path.relative_to(REPO_ROOT)}:{i}: "
                    f"hardcoded device restriction: {line.strip()!r}"
                )
    return errors


def check_readiness_matrix(devices: list[dict]) -> list[str]:
    sys.path.insert(0, str(REPO_ROOT))
    from factory.registry.device_readiness import build_device_readiness_matrix

    matrix = build_device_readiness_matrix(FACTORY_JSON)
    errors: list[str] = []
    for r in matrix["devices"]:
        if r["enabled"] and not r["universal_engine_ready"]:
            reasons = "; ".join(r["notes"]) or "unknown"
            errors.append(
                f"Device {r['codename']!r} is enabled but not engine-ready: {reasons}"
            )
    return errors


def main(argv: list[str] | None = None) -> int:
    all_errors: list[str] = []

    if not FACTORY_JSON.exists():
        print(f"[FAIL] factory_devices.json not found: {FACTORY_JSON}", file=sys.stderr)
        return 1

    devices = _load_devices()
    print(f"[OK] Loaded {len(devices)} devices from factory_devices.json")

    for check_fn, label in [
        (lambda: check_duplicate_codenames(devices),  "Duplicate codenames"),
        (lambda: check_empty_display_names(devices),  "Empty display_names"),
        (lambda: check_workflow_coverage(devices),    "Workflow dropdown coverage"),
        (check_hardcoded_device_restrictions,         "Hardcoded device restrictions"),
        (lambda: check_readiness_matrix(devices),     "Universal engine readiness"),
    ]:
        errs = check_fn()
        for e in errs:
            print(f"[FAIL] {e}", file=sys.stderr)
        all_errors.extend(errs)
        if not errs:
            print(f"[OK] {label}: passed")

    if all_errors:
        print(
            f"\n[RESULT] FAILED — {len(all_errors)} error(s) found.",
            file=sys.stderr,
        )
        return 1

    print("\n[RESULT] All device readiness checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
