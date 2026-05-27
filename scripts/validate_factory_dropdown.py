"""
validate_factory_dropdown.py

Validates factory_devices.json and GitHub Actions workflow files for correctness.

Checks:
  1. factory_devices.json is valid JSON
  2. No duplicate codenames
  3. No empty display_name fields
  4. Every workflow contains AUTO-GENERATED markers
  5. Workflows contain select_device input
  6. Workflows do not contain old required codename/select_device_codename inputs
  7. Generated dropdown options match what is in each workflow
  8. Python scripts in scripts/ compile without syntax errors
"""

from __future__ import annotations

import json
import pathlib
import py_compile
import re
import sys
import tempfile

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

FACTORY_JSON = REPO_ROOT / "registry" / "devices" / "factory_devices.json"

WORKFLOWS = {
    "mtk": REPO_ROOT / ".github" / "workflows" / "deadzone_mtk.yml",
    "snapdragon": REPO_ROOT / ".github" / "workflows" / "deadzone_snapdragon.yml",
}

START_MARKER = "# AUTO-GENERATED DEVICE OPTIONS START"
END_MARKER = "# AUTO-GENERATED DEVICE OPTIONS END"
OPTION_INDENT = "          "

_OLD_INPUTS = {"codename:", "select_device_codename:"}


def _load_devices() -> list[dict]:
    if not FACTORY_JSON.exists():
        raise FileNotFoundError(f"factory_devices.json not found: {FACTORY_JSON}")
    return json.loads(FACTORY_JSON.read_text(encoding="utf-8"))


def _filter_devices(devices: list[dict], soc: str) -> list[dict]:
    return [d for d in devices if d.get("soc") == soc and d.get("enabled", True)]


def _sort_devices(devices: list[dict]) -> list[dict]:
    return sorted(devices, key=lambda d: d["display_name"].lower())


def _make_option(device: dict) -> str:
    return f"{OPTION_INDENT}- {device['codename']} | {device['display_name']}"


def _extract_generated_block(text: str) -> list[str] | None:
    pattern = re.compile(
        re.escape(START_MARKER) + r"(.*?)" + re.escape(END_MARKER),
        re.DOTALL,
    )
    m = pattern.search(text)
    if not m:
        return None
    lines = [ln.strip() for ln in m.group(1).splitlines() if ln.strip()]
    return lines


def check_factory_json(devices: list[dict]) -> list[str]:
    errors: list[str] = []

    codenames = [d.get("codename", "") for d in devices]
    seen: set[str] = set()
    for cn in codenames:
        if cn in seen:
            errors.append(f"Duplicate codename: {cn!r}")
        seen.add(cn)

    for d in devices:
        if not d.get("display_name", "").strip():
            errors.append(f"Empty display_name for codename: {d.get('codename')!r}")

    return errors


def check_workflow(soc: str, path: pathlib.Path, devices: list[dict]) -> list[str]:
    errors: list[str] = []

    if not path.exists():
        errors.append(f"Workflow not found: {path}")
        return errors

    text = path.read_text(encoding="utf-8")

    if START_MARKER not in text or END_MARKER not in text:
        errors.append(f"{path.name}: missing AUTO-GENERATED markers")

    if "select_device:" not in text:
        errors.append(f"{path.name}: missing select_device input")

    for old in _OLD_INPUTS:
        # Check for old required inputs (not inside comments)
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            if old in stripped and "required: true" in text:
                # Only flag if it looks like a top-level input definition
                if re.match(r"\s{4,8}" + re.escape(old), line):
                    errors.append(
                        f"{path.name}: found old input {old!r} — should be removed"
                    )
                    break

    # Verify dropdown options match registry
    filtered = _filter_devices(devices, soc)
    sorted_devs = _sort_devices(filtered)
    expected_options = [_make_option(d).strip() for d in sorted_devs]

    actual_options = _extract_generated_block(text)
    if actual_options is None:
        errors.append(f"{path.name}: could not extract AUTO-GENERATED block")
    else:
        if actual_options != expected_options:
            exp_set = set(expected_options)
            act_set = set(actual_options)
            missing = sorted(exp_set - act_set)
            extra = sorted(act_set - exp_set)
            if missing:
                errors.append(
                    f"{path.name}: {len(missing)} registry devices missing from dropdown: "
                    + ", ".join(missing[:5]) + ("..." if len(missing) > 5 else "")
                )
            if extra:
                errors.append(
                    f"{path.name}: {len(extra)} dropdown entries not in registry: "
                    + ", ".join(extra[:5]) + ("..." if len(extra) > 5 else "")
                )

    return errors


def check_python_scripts() -> list[str]:
    errors: list[str] = []
    scripts_dir = REPO_ROOT / "scripts"
    for py_file in sorted(scripts_dir.glob("*.py")):
        try:
            py_compile.compile(str(py_file), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(f"Syntax error in {py_file.name}: {exc}")
    return errors


def main(argv: list[str] | None = None) -> int:
    all_errors: list[str] = []

    # 1. Load and validate factory_devices.json
    try:
        devices = _load_devices()
        print(f"[OK] Loaded {len(devices)} devices from factory_devices.json")
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1

    json_errors = check_factory_json(devices)
    for e in json_errors:
        print(f"[FAIL] {e}", file=sys.stderr)
    all_errors.extend(json_errors)

    # 2. Validate each workflow
    for soc, path in WORKFLOWS.items():
        wf_errors = check_workflow(soc, path, devices)
        for e in wf_errors:
            print(f"[FAIL] {e}", file=sys.stderr)
        all_errors.extend(wf_errors)
        if not wf_errors:
            filtered = _filter_devices(devices, soc)
            print(f"[OK] {path.name}: {len(filtered)} {soc} devices, dropdown matches registry")

    # 3. Compile all scripts
    script_errors = check_python_scripts()
    for e in script_errors:
        print(f"[FAIL] {e}", file=sys.stderr)
    all_errors.extend(script_errors)
    if not script_errors:
        print("[OK] All scripts//*.py files compile successfully")

    if all_errors:
        print(f"\n[RESULT] FAILED — {len(all_errors)} error(s) found.", file=sys.stderr)
        return 1

    print(f"\n[RESULT] All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
