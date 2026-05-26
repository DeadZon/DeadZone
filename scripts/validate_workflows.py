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

# Minimum LF line counts per workflow file (guards against minification/corruption).
MIN_LF_COUNTS: dict[str, int] = {
    "deadzone_mtk.yml":              120,
    "deadzone_snapdragon.yml":       120,
    "deadzone_mtk_fly.yml":          180,
    "deadzone_snapdragon_fly.yml":   180,
    "deploy_fly_builder.yml":         30,
}

# Exactly these inputs must appear in the UI — no more, no less.
REQUIRED_INPUTS = [
    "codename",
    "custom_codename",
    "edition",
    "rom_url",
    "mode",
    "upload_pixeldrain",
    "notify_telegram",
]

# Legacy inputs that must NOT be present in any build workflow.
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

# Placeholder codenames that must not appear anywhere in workflow files.
PLACEHOLDER_CODENAMES = [
    "select_device_codename",
]

# Terms that must NOT appear in GitHub local workflow files.
FLY_FORBIDDEN_IN_LOCAL = [
    "FLY_BUILDER_URL",
    "MTK_FLY_BUILDER_URL",
    "SNAPDRAGON_FLY_BUILDER_URL",
    "BUILDER_TOKEN",
    "/build",
    "flyctl machine run",
]

# Terms that must NOT appear in Fly workflow files.
FACTORY_FORBIDDEN_IN_FLY = [
    "factory.pipeline.orchestrator",
    "python -m factory",
    "run_factory",
    "curl -L",
    "Download source ROM",
]

# Terms that must appear in Fly workflow files (secrets guard + notify).
FLY_REQUIRED_PATTERNS = [
    "notify_dispatch_failure.py",
    "exit 3",
]


def _load(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _workflow_inputs(data: dict) -> set[str]:
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


# ── Check 1b: LF integrity — CR, BOM, minimum line count ─────────────────────
print("\n=== Check 1b: LF integrity (CR=0, BOM=false, minimum lines) ===")
for name in all_wf:
    path = WORKFLOWS_DIR / name
    if not path.exists():
        continue
    raw = path.read_bytes()
    cr_count = raw.count(b"\r")
    bom = raw.startswith(b"\xef\xbb\xbf")
    lf_count = raw.count(b"\n")
    min_lf = MIN_LF_COUNTS.get(name, 0)

    if cr_count > 0:
        fail(f"{name}: contains {cr_count} CR byte(s) — file must be LF-only")
    else:
        ok(f"{name}: no CR bytes")

    if bom:
        fail(f"{name}: starts with UTF-8 BOM — must be BOM-free")
    else:
        ok(f"{name}: no BOM")

    if min_lf > 0 and lf_count < min_lf:
        fail(f"{name}: only {lf_count} LF lines (minimum {min_lf}) — file may be minified/corrupted")
    elif min_lf > 0:
        ok(f"{name}: {lf_count} LF lines (>= {min_lf})")


# ── Check 2: Build workflows have exactly the required inputs (no legacy) ──────
print("\n=== Check 2: Build workflow inputs — required only, no legacy ===")
for name in ALL_BUILD_WORKFLOWS:
    if name not in parsed:
        continue
    inputs = _workflow_inputs(parsed[name])
    required_set = set(REQUIRED_INPUTS)
    missing = [i for i in REQUIRED_INPUTS if i not in inputs]
    extra_legacy = [i for i in LEGACY_INPUTS if i in inputs]

    if missing:
        fail(f"{name}: missing required inputs: {missing}")
    else:
        ok(f"{name}: all {len(REQUIRED_INPUTS)} required inputs present")

    if extra_legacy:
        fail(f"{name}: legacy inputs must be removed from UI: {extra_legacy}")
    else:
        ok(f"{name}: no legacy inputs in UI")


# ── Check 3: No placeholder codename as YAML input default or choice option ────
print("\n=== Check 3: No placeholder codename in YAML input defaults/options ===")
for name in ALL_BUILD_WORKFLOWS:
    if name not in parsed:
        continue
    on_section = parsed[name].get("on") or parsed[name].get(True) or {}
    try:
        inputs_section = on_section["workflow_dispatch"]["inputs"] or {}
    except (KeyError, TypeError):
        inputs_section = {}

    found_placeholders: list[str] = []
    for inp_name, inp_def in inputs_section.items():
        if not isinstance(inp_def, dict):
            continue
        default_val = str(inp_def.get("default", ""))
        options = inp_def.get("options") or []
        for placeholder in PLACEHOLDER_CODENAMES:
            if default_val == placeholder:
                found_placeholders.append(f"{inp_name}.default={placeholder}")
            if placeholder in [str(o) for o in options]:
                found_placeholders.append(f"{inp_name}.options contains {placeholder}")

    if found_placeholders:
        fail(f"{name}: placeholder codename(s) in YAML input definition — must be removed: {found_placeholders}")
    else:
        ok(f"{name}: no placeholder codenames in input defaults/options")


# ── Check 4: GitHub local workflows must NOT reference Fly secrets/endpoints ──
print("\n=== Check 4: GitHub local workflows — no Fly references ===")
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


# ── Check 5: Fly workflows must NOT run factory locally or download ROM ────────
print("\n=== Check 5: Fly workflows — no local factory run or ROM download ===")
for name in FLY_WORKFLOWS:
    if name not in texts:
        continue
    text = texts[name]
    clean = True
    for forbidden in FACTORY_FORBIDDEN_IN_FLY:
        if forbidden in text:
            fail(f"{name}: must not contain '{forbidden}'")
            clean = False
    if clean:
        ok(f"{name}: no local factory execution or ROM download found")


# ── Check 6: Fly workflows must include secrets guard + dispatch notifier ──────
print("\n=== Check 6: Fly workflows — missing-secret Telegram dispatch notification ===")
for name in FLY_WORKFLOWS:
    if name not in texts:
        continue
    text = texts[name]
    all_present = True
    for pattern in FLY_REQUIRED_PATTERNS:
        if pattern not in text:
            fail(f"{name}: missing required pattern '{pattern}' (secrets guard + notify)")
            all_present = False
    if all_present:
        ok(f"{name}: secrets guard and dispatch notifier present")


# ── Check 7: deploy_fly_builder.yml has no ROM/device inputs ──────────────────
print("\n=== Check 7: deploy_fly_builder.yml — no ROM/device inputs ===")
deploy_name = "deploy_fly_builder.yml"
if deploy_name in parsed:
    deploy_inputs = _workflow_inputs(parsed[deploy_name])
    rom_device_inputs = {"rom_url", "device", "codename", "edition", "flavor"}
    found_bad = deploy_inputs & rom_device_inputs
    if found_bad:
        fail(f"{deploy_name}: must not have ROM/device inputs — found: {found_bad}")
    else:
        ok(f"{deploy_name}: no ROM/device inputs")


# ── Check 8: codename input type is string, not choice ────────────────────────
print("\n=== Check 8: codename input type is string (not choice dropdown) ===")
for name in ALL_BUILD_WORKFLOWS:
    if name not in parsed:
        continue
    on_section = parsed[name].get("on") or parsed[name].get(True) or {}
    try:
        inputs_section = on_section["workflow_dispatch"]["inputs"]
        codename_input = inputs_section.get("codename", {})
        input_type = codename_input.get("type", "string")
        if input_type == "choice":
            fail(f"{name}: codename input must be type: string, not type: choice")
        else:
            ok(f"{name}: codename is type: {input_type}")
    except (KeyError, TypeError):
        warn(f"{name}: could not read codename input definition")


# ── Check 9: Telegram secret cross-wiring ─────────────────────────────────────
# MTK workflows must not set TELEGRAM_SNAPDRAGON_* env keys.
# Snapdragon workflows must not set TELEGRAM_MTK_* env keys.
# GitHub workflows must set SoC-specific env keys (not only generic BOT_TOKEN).
print("\n=== Check 9: Telegram bot secret separation ===")

_MTK_FORBIDDEN_SNAP  = ["TELEGRAM_SNAPDRAGON_BOT_TOKEN", "TELEGRAM_SNAPDRAGON_CHAT_ID"]
_SNAP_FORBIDDEN_MTK  = ["TELEGRAM_MTK_BOT_TOKEN", "TELEGRAM_MTK_CHAT_ID"]


def _strip_yaml_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.lstrip()
        if not stripped.startswith("#"):
            lines.append(line)
    return "\n".join(lines)


for name in ["deadzone_mtk.yml", "deadzone_mtk_fly.yml"]:
    if name not in texts:
        continue
    body = _strip_yaml_comments(texts[name])
    clean = True
    for bad in _MTK_FORBIDDEN_SNAP:
        if bad in body:
            fail(f"{name}: must not reference Snapdragon secret '{bad}'")
            clean = False
    if clean:
        ok(f"{name}: no Snapdragon Telegram secret cross-wiring")

for name in ["deadzone_snapdragon.yml", "deadzone_snapdragon_fly.yml"]:
    if name not in texts:
        continue
    body = _strip_yaml_comments(texts[name])
    clean = True
    for bad in _SNAP_FORBIDDEN_MTK:
        if bad in body:
            fail(f"{name}: must not reference MTK secret '{bad}'")
            clean = False
    if clean:
        ok(f"{name}: no MTK Telegram secret cross-wiring")

# GitHub local workflows must use SoC-specific env key names (not only generic remapping)
if "deadzone_mtk.yml" in texts:
    import re as _re
    body = _strip_yaml_comments(texts["deadzone_mtk.yml"])
    if _re.search(r"TELEGRAM_MTK_BOT_TOKEN\s*:", body):
        ok("deadzone_mtk.yml: TELEGRAM_MTK_BOT_TOKEN env key set correctly")
    else:
        fail(
            "deadzone_mtk.yml: must set env key 'TELEGRAM_MTK_BOT_TOKEN:' "
            "(not remap it to TELEGRAM_BOT_TOKEN) so SoC-specific resolver works"
        )

if "deadzone_snapdragon.yml" in texts:
    import re as _re
    body = _strip_yaml_comments(texts["deadzone_snapdragon.yml"])
    if _re.search(r"TELEGRAM_SNAPDRAGON_BOT_TOKEN\s*:", body):
        ok("deadzone_snapdragon.yml: TELEGRAM_SNAPDRAGON_BOT_TOKEN env key set correctly")
    else:
        fail(
            "deadzone_snapdragon.yml: must set env key 'TELEGRAM_SNAPDRAGON_BOT_TOKEN:' "
            "(not remap it to TELEGRAM_BOT_TOKEN) so SoC-specific resolver works"
        )


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
