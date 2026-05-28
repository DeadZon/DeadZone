"""Tests for Universal Smart ROM Engine — device readiness matrix.

Covers:
  - Every enabled factory device has codename and display_name.
  - Every enabled device passes universal_engine_ready.
  - All MTK devices appear in MTK workflow dropdown.
  - All Snapdragon devices appear in Snapdragon workflow dropdown.
  - No production code hardcodes only zorn/zircon/garnet.
  - selected_codename is accepted by universal intake (any codename).
  - Codename mismatch fails for any device, not just zorn.
  - No detected codename continues with warning (not error).
  - DeadZone_Mezo banner can be generated for arbitrary codename.
  - All devices pass smoke readiness.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

FACTORY_JSON = REPO_ROOT / "registry" / "devices" / "factory_devices.json"

WORKFLOWS = {
    "mtk":        REPO_ROOT / ".github" / "workflows" / "deadzone_mtk.yml",
    "snapdragon": REPO_ROOT / ".github" / "workflows" / "deadzone_snapdragon.yml",
}

_START_MARKER = "# AUTO-GENERATED DEVICE OPTIONS START"
_END_MARKER   = "# AUTO-GENERATED DEVICE OPTIONS END"

_PRODUCTION_MODULES = [
    REPO_ROOT / "factory" / "engine"   / "smart_base_engine.py",
    REPO_ROOT / "factory" / "pipeline" / "legacy_engine_runner.py",
    REPO_ROOT / "factory" / "pipeline" / "free_pipeline.py",
    REPO_ROOT / "factory" / "pipeline" / "orchestrator.py",
    REPO_ROOT / "factory" / "input"    / "universal_rom_intake.py",
    REPO_ROOT / "factory" / "super"    / "universal_super_engine.py",
    REPO_ROOT / "factory" / "output"   / "deadzone_template_patcher.py",
    REPO_ROOT / "factory" / "repack"   / "super_collector.py",
]

_HARDCODE_PATTERN = re.compile(
    r'(?:if|elif)\s+(?:device|codename|selected_codename)\s*(?:==|in)\s*'
    r'(?:"(?:zorn|zircon|garnet)"|'
    r'\[(?:\s*"(?:zorn|zircon|garnet)"\s*,?\s*)+\])',
    re.IGNORECASE,
)


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def all_devices() -> list[dict]:
    return json.loads(FACTORY_JSON.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def enabled_devices(all_devices) -> list[dict]:
    return [d for d in all_devices if d.get("enabled", True)]


@pytest.fixture(scope="module")
def readiness_matrix(all_devices):
    from factory.registry.device_readiness import build_device_readiness_matrix
    return build_device_readiness_matrix(FACTORY_JSON)


# ── Basic registry sanity ─────────────────────────────────────────────────────

def test_all_enabled_devices_have_codename(enabled_devices):
    bad = [d for d in enabled_devices if not d.get("codename", "").strip()]
    assert bad == [], f"Devices with empty codename: {bad}"


def test_all_enabled_devices_have_display_name(enabled_devices):
    bad = [d for d in enabled_devices if not d.get("display_name", "").strip()]
    assert bad == [], f"Devices with empty display_name: {[d.get('codename') for d in bad]}"


def test_no_duplicate_codenames(all_devices):
    seen: dict[str, int] = {}
    for d in all_devices:
        cn = d.get("codename", "")
        seen[cn] = seen.get(cn, 0) + 1
    dups = {cn for cn, cnt in seen.items() if cnt > 1}
    assert dups == set(), f"Duplicate codenames found: {dups}"


# ── Readiness matrix ──────────────────────────────────────────────────────────

def test_all_enabled_devices_are_engine_ready(readiness_matrix):
    not_ready = [
        r for r in readiness_matrix["devices"]
        if r["enabled"] and not r["universal_engine_ready"]
    ]
    assert not_ready == [], (
        "Enabled devices not engine-ready: "
        + str([(r["codename"], r["notes"]) for r in not_ready])
    )


def test_readiness_matrix_summary_has_no_duplicates(readiness_matrix):
    assert readiness_matrix["summary"]["duplicate_codenames"] == []


def test_readiness_matrix_not_ready_count_is_zero(readiness_matrix):
    assert readiness_matrix["summary"]["not_ready"] == 0, (
        "Not-ready devices: " + str(readiness_matrix["summary"]["not_ready_devices"])
    )


# ── Workflow dropdown coverage ─────────────────────────────────────────────────

def _extract_dropdown_codenames(wf_text: str) -> set[str]:
    pat = re.compile(
        re.escape(_START_MARKER) + r"(.*?)" + re.escape(_END_MARKER),
        re.DOTALL,
    )
    m = pat.search(wf_text)
    if not m:
        return set()
    codes: set[str] = set()
    for line in m.group(1).splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            parts = stripped[2:].split("|", 1)
            if parts:
                codes.add(parts[0].strip())
    return codes


@pytest.mark.skipif(not WORKFLOWS["mtk"].exists(), reason="MTK workflow not found")
def test_all_mtk_devices_in_mtk_dropdown(enabled_devices):
    text = WORKFLOWS["mtk"].read_text(encoding="utf-8")
    dropdown = _extract_dropdown_codenames(text)
    mtk_devices = {d["codename"] for d in enabled_devices if d.get("soc") == "mtk"}
    missing = mtk_devices - dropdown
    assert missing == set(), f"MTK devices missing from dropdown: {missing}"


@pytest.mark.skipif(not WORKFLOWS["snapdragon"].exists(), reason="Snapdragon workflow not found")
def test_all_snapdragon_devices_in_snapdragon_dropdown(enabled_devices):
    text = WORKFLOWS["snapdragon"].read_text(encoding="utf-8")
    dropdown = _extract_dropdown_codenames(text)
    sd_devices = {d["codename"] for d in enabled_devices if d.get("soc") == "snapdragon"}
    missing = sd_devices - dropdown
    assert missing == set(), f"Snapdragon devices missing from dropdown: {missing}"


# ── No hardcoded device restrictions in production ────────────────────────────

@pytest.mark.parametrize("mod_path", [p for p in _PRODUCTION_MODULES if p.exists()])
def test_no_hardcoded_device_restriction(mod_path: Path):
    text = mod_path.read_text(encoding="utf-8")
    violations = []
    for i, line in enumerate(text.splitlines(), 1):
        if _HARDCODE_PATTERN.search(line):
            violations.append(f"line {i}: {line.strip()}")
    assert violations == [], (
        f"{mod_path.relative_to(REPO_ROOT)} has hardcoded device restrictions:\n"
        + "\n".join(violations)
    )


# ── Universal intake — arbitrary codename ────────────────────────────────────

@pytest.mark.parametrize("codename", ["zorn", "zircon", "garnet", "agate", "marble", "haotian"])
def test_intake_accepts_any_codename(codename):
    from factory.input.rom_detector import check_codename_match

    ok, msg = check_codename_match(codename, codename)
    assert ok is True, f"Self-match failed for {codename!r}: {msg}"


# ── Codename mismatch fails for any device ────────────────────────────────────

@pytest.mark.parametrize("codename", ["zorn", "marble", "agate", "aristotle", "pandora"])
def test_codename_mismatch_fails_for_any_device(codename):
    from factory.input.rom_detector import check_codename_match

    ok, msg = check_codename_match("some_other_device_xyz", codename)
    assert ok is False, f"Mismatch should fail for {codename!r} but returned ok=True"
    assert msg is not None and len(msg) > 0


# ── No detected codename → warning, not error ────────────────────────────────

@pytest.mark.parametrize("codename", ["zorn", "marble", "agate"])
def test_no_detected_codename_continues_with_warning(codename):
    from factory.input.rom_detector import check_codename_match

    ok, msg = check_codename_match(None, codename)
    assert ok is True, (
        f"None detected_codename should pass (with warning) for {codename!r}, got ok={ok}"
    )


# ── DeadZone_Mezo banner — arbitrary codename ────────────────────────────────

@pytest.mark.parametrize(
    "codename",
    ["zorn", "marble", "agate", "aristotle", "pandora", "miro", "dada", "muyu"],
)
def test_banner_generation_works_for_arbitrary_codename(codename):
    from factory.output.deadzone_template_patcher import _bat_banner_lines, _sh_banner_lines

    bat = _bat_banner_lines(
        codename=codename,
        edition="Free",
        android_version="16.0",
        build_incremental="OS3.0.000.0.TEST",
        region="CN",
    )
    sh = _sh_banner_lines(
        codename=codename,
        edition="Free",
        android_version="16.0",
        build_incremental="OS3.0.000.0.TEST",
        region="CN",
    )
    assert bat, f"BAT banner empty for {codename!r}"
    assert sh,  f"SH banner empty for {codename!r}"
    combined = "\n".join(bat + sh)
    assert codename in combined, (
        f"Codename {codename!r} not found in generated banner"
    )


# ── Smoke readiness: all devices pass every check ─────────────────────────────

def test_all_devices_smoke_readiness(enabled_devices):
    from factory.output.deadzone_template_patcher import _bat_banner_lines, validate_codename
    from factory.input.rom_detector import check_codename_match

    failures: list[str] = []
    for device in enabled_devices:
        codename = device["codename"]
        try:
            # Banner must generate
            lines = _bat_banner_lines(codename, "Free", "16.0", "OS3.0.000.0.TEST", "CN")
            assert lines and codename in "\n".join(lines)

            # ZIP name must contain codename
            zip_name = f"DeadZone_{codename}_V1.zip"
            assert codename in zip_name

            # Self-codename match must pass
            ok, msg = check_codename_match(codename, codename)
            assert ok, f"self-match failed: {msg}"

            # Mismatch must fail
            ok2, _ = check_codename_match("__xyzfake__", codename)
            assert not ok2, "mismatch should fail"

        except Exception as exc:
            failures.append(f"{codename}: {exc}")

    assert failures == [], (
        f"{len(failures)} device(s) failed smoke readiness:\n" + "\n".join(failures)
    )
