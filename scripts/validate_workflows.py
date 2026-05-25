"""Validate DeadZone workflow YAML files for correctness and safety."""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("pyyaml is required: pip install pyyaml")

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS_DIR = REPO_ROOT / ".github" / "workflows"

GITHUB_LOCAL_WORKFLOWS = [
    "deadzone_mtk.yml",
    "deadzone_snapdragon.yml",
]

FLY_WORKFLOWS = [
    "deadzone_mtk_fly.yml",
    "deadzone_snapdragon_fly.yml",
]

ALL_BUILD_WORKFLOWS = GITHUB_LOCAL_WORKFLOWS + FLY_WORKFLOWS

LEGACY_INPUTS = [
    "device",
    "custom_device",
    "final_name",
    "platform",
    "flavor",
    "android_version",
    "mi_version",
    "vbmeta_mode",
    "runner_label",
    "VM_CPUS",
    "VM_MEMORY",
]

NEW_INPUTS = [
    "codename",
    "custom_codename",
    "edition",
    "rom_url",
    "mode",
    "upload_pixeldrain",
    "notify_telegram",
]

FLY_FORBIDDEN_IN_LOCAL = [
    "FLY_BUILDER_URL",
    "MTK_FLY_BUILDER_URL",
    "SNAPDRAGON_FLY_BUILDER_URL",
    "BUILDER_TOKEN",
    "/build",
    "flyctl machine run",
]

FACTORY_FORBIDDEN_IN_FLY = [
    "factory.pipeline.orchestrator",
    "python -m factory",
    "run_factory",
]


def _load(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _workflow_inputs(data: dict) -> set[str]:
    # PyYAML parses 'on' as boolean True
    on_section = data.get("on") or data.get(True) or {}
    try:
        return set(on_section["workflow_dispatch"]["inputs"].keys())
    except (KeyError, TypeError):
        return set()


def _workflow_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


errors: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)
    print(f"  [FAIL] {msg}")


def warn(msg: str) -> None:
    warnings.append(msg)
    print(f"  [WARN] {msg}")


def ok(msg: str) -> None:
    print(f"  [ OK ] {msg}")


# ── Check 1: all workflow files exist and parse ────────────────────────────────
print("\n=== Check 1: YAML parse ===")
all_wf = ALL_BUILD_WORKFLOWS + ["deploy_fly_builder.yml"]
parsed: dict[str, dict] = {}
texts: dict[str, str] = {}

for name in all_wf:
    path = WORKFLOWS_DIR / name
    if not path.exists():
        fail(f"Missing workflow file: {name}")
        continue
    try:
        data = _load(path)
        parsed[name] = data
        texts[name] = _workflow_text(path)
        ok(f"Parsed OK: {name}")
    except Exception as exc:
        fail(f"YAML parse error in {name}: {exc}")


# ── Check 2: GitHub local workflows must NOT reference Fly secrets/endpoints ──
print("\n=== Check 2: GitHub local workflows — no Fly references ===")
for name in GITHUB_LOCAL_WORKFLOWS:
    if name not in texts:
        continue
    text = texts[name]
    clean = True
    for forbidden in FLY_FORBIDDEN_IN_LOCAL:
        if forbidden in text:
            fail(f"{name}: must not reference '{forbidden}'")
            clean = False
    if clean:
        ok(f"{name}: no Fly references found")


# ── Check 3: Fly workflows must NOT run factory locally ────────────────────────
print("\n=== Check 3: Fly workflows — must not run factory locally ===")
for name in FLY_WORKFLOWS:
    if name not in texts:
        continue
    text = texts[name]
    clean = True
    for forbidden in FACTORY_FORBIDDEN_IN_FLY:
        if forbidden in text:
            fail(f"{name}: must not run factory locally — found '{forbidden}'")
            clean = False
    if clean:
        ok(f"{name}: no local factory execution found")


# ── Check 4: All build workflows accept legacy inputs ─────────────────────────
print("\n=== Check 4: Legacy inputs present in all build workflows ===")
for name in ALL_BUILD_WORKFLOWS:
    if name not in parsed:
        continue
    inputs = _workflow_inputs(parsed[name])
    missing = [i for i in LEGACY_INPUTS if i not in inputs]
    if missing:
        fail(f"{name}: missing legacy inputs: {missing}")
    else:
        ok(f"{name}: all {len(LEGACY_INPUTS)} legacy inputs present")


# ── Check 5: All build workflows accept new inputs ────────────────────────────
print("\n=== Check 5: New inputs present in all build workflows ===")
for name in ALL_BUILD_WORKFLOWS:
    if name not in parsed:
        continue
    inputs = _workflow_inputs(parsed[name])
    missing = [i for i in NEW_INPUTS if i not in inputs]
    if missing:
        fail(f"{name}: missing new inputs: {missing}")
    else:
        ok(f"{name}: all {len(NEW_INPUTS)} new inputs present")


# ── Check 6: deploy_fly_builder.yml has no ROM/device inputs ──────────────────
print("\n=== Check 6: deploy_fly_builder.yml — no ROM/device inputs ===")
deploy_name = "deploy_fly_builder.yml"
if deploy_name in parsed:
    deploy_inputs = _workflow_inputs(parsed[deploy_name])
    rom_device_inputs = {"rom_url", "device", "codename", "edition", "flavor"}
    found = deploy_inputs & rom_device_inputs
    if found:
        fail(f"{deploy_name}: must not have ROM/device inputs — found: {found}")
    else:
        ok(f"{deploy_name}: no ROM/device inputs")


# ── Summary ────────────────────────────────────────────────────────────────────
print("\n=== Summary ===")
print(f"  Errors  : {len(errors)}")
print(f"  Warnings: {len(warnings)}")

if errors:
    print("\nFAILED — fix the errors above before pushing.\n")
    sys.exit(1)
else:
    print("\nAll checks passed.\n")
    sys.exit(0)
