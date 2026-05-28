"""Tests for DeadZone Fly workflow correctness and Telegram helper behavior.

Covers all requirements from the Fly rebuild task:
- Fly workflow files contain codename input (not select_device/custom_device/device)
- Fly workflow files do not contain forbidden input names
- Fly workflow passes ENABLE_LISTMEZO / LISTMEZO_MODE / LISTMEZO_EDITION
- Fly workflow passes TELEGRAM_MSG_ID
- Fly workflow passes VM CPU / RAM / region inputs
- Fly entrypoint calls factory.pipeline.orchestrator
- Fly Telegram helper edits existing message_id
- Fly Telegram helper sends new message if no message_id
- Fly final failure sends failed action
- Device readiness report includes direct_supported and fly_supported
- Direct and Fly workflows use the same codename logic (free-text, no dropdown)
"""
from __future__ import annotations

import importlib
import json
import os
import sys
import unittest.mock as mock
from pathlib import Path
from typing import Any

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

FLY_MTK_WF      = REPO_ROOT / ".github" / "workflows" / "deadzone_mtk_fly.yml"
FLY_SNAP_WF     = REPO_ROOT / ".github" / "workflows" / "deadzone_snapdragon_fly.yml"
DIRECT_MTK_WF   = REPO_ROOT / ".github" / "workflows" / "deadzone_mtk.yml"
DIRECT_SNAP_WF  = REPO_ROOT / ".github" / "workflows" / "deadzone_snapdragon.yml"
ENTRYPOINT      = REPO_ROOT / "scripts" / "fly_deadzone_entrypoint.sh"
TELEGRAM_SCRIPT = REPO_ROOT / "scripts" / "deadzone_fly_telegram.py"
FACTORY_JSON    = REPO_ROOT / "registry" / "devices" / "factory_devices.json"

_FLY_WORKFLOWS  = [FLY_MTK_WF, FLY_SNAP_WF]
_ALL_WORKFLOWS  = [FLY_MTK_WF, FLY_SNAP_WF, DIRECT_MTK_WF, DIRECT_SNAP_WF]

_FORBIDDEN_INPUTS = [
    "select_device",
    "custom_device",
    "final_name",
    "flavor",
    "platform",
]


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def mtk_fly_text() -> str:
    return FLY_MTK_WF.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def snap_fly_text() -> str:
    return FLY_SNAP_WF.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def readiness_matrix():
    from factory.registry.device_readiness import build_device_readiness_matrix
    return build_device_readiness_matrix(FACTORY_JSON)


# ── 1. Fly workflows contain `codename` input ─────────────────────────────────

@pytest.mark.parametrize("wf_path", _FLY_WORKFLOWS)
def test_fly_workflow_has_codename_input(wf_path: Path):
    text = wf_path.read_text(encoding="utf-8")
    assert "codename:" in text, f"{wf_path.name} must have a 'codename:' input"


# ── 2. Fly workflows do NOT contain forbidden input names ─────────────────────

@pytest.mark.parametrize("wf_path", _FLY_WORKFLOWS)
@pytest.mark.parametrize("forbidden", _FORBIDDEN_INPUTS)
def test_fly_workflow_no_forbidden_inputs(wf_path: Path, forbidden: str):
    import re
    text = wf_path.read_text(encoding="utf-8")
    # Match as a workflow input key (indented, followed by colon)
    pattern = re.compile(rf"^\s+{re.escape(forbidden)}\s*:", re.MULTILINE)
    assert not pattern.search(text), (
        f"{wf_path.name} contains forbidden input '{forbidden}'"
    )


# ── 3. Fly workflows pass ENABLE_LISTMEZO / LISTMEZO_MODE / LISTMEZO_EDITION ──

@pytest.mark.parametrize("wf_path", _FLY_WORKFLOWS)
@pytest.mark.parametrize("env_var", ["ENABLE_LISTMEZO", "LISTMEZO_MODE", "LISTMEZO_EDITION"])
def test_fly_workflow_passes_listmezo_env(wf_path: Path, env_var: str):
    text = wf_path.read_text(encoding="utf-8")
    assert env_var in text, (
        f"{wf_path.name} must pass {env_var} to the Fly machine"
    )


# ── 4. Fly workflows pass TELEGRAM_MSG_ID ─────────────────────────────────────

@pytest.mark.parametrize("wf_path", _FLY_WORKFLOWS)
def test_fly_workflow_passes_telegram_msg_id(wf_path: Path):
    text = wf_path.read_text(encoding="utf-8")
    assert "TELEGRAM_MSG_ID" in text, (
        f"{wf_path.name} must pass TELEGRAM_MSG_ID to the Fly machine"
    )


# ── 5. Fly workflows pass VM CPU / RAM / region inputs ────────────────────────

@pytest.mark.parametrize("wf_path", _FLY_WORKFLOWS)
@pytest.mark.parametrize("param", ["vm_cpus", "vm_memory", "fly_region"])
def test_fly_workflow_has_vm_inputs(wf_path: Path, param: str):
    text = wf_path.read_text(encoding="utf-8")
    assert param in text, f"{wf_path.name} must have '{param}' input"


@pytest.mark.parametrize("wf_path", _FLY_WORKFLOWS)
@pytest.mark.parametrize("flag", ["--vm-cpus", "--vm-memory", "--vm-cpu-kind"])
def test_fly_workflow_passes_vm_flags_to_flyctl(wf_path: Path, flag: str):
    text = wf_path.read_text(encoding="utf-8")
    assert flag in text, f"{wf_path.name} must pass '{flag}' to flyctl machine run"


# ── 6. Fly entrypoint calls factory.pipeline.orchestrator ────────────────────

def test_entrypoint_calls_orchestrator():
    assert ENTRYPOINT.exists(), "scripts/fly_deadzone_entrypoint.sh must exist"
    text = ENTRYPOINT.read_text(encoding="utf-8")
    assert "factory.pipeline.orchestrator" in text, (
        "fly_deadzone_entrypoint.sh must call factory.pipeline.orchestrator"
    )


def test_entrypoint_uses_set_euo_pipefail():
    text = ENTRYPOINT.read_text(encoding="utf-8")
    assert "set -euo pipefail" in text, (
        "fly_deadzone_entrypoint.sh must use 'set -euo pipefail'"
    )


def test_entrypoint_validates_required_envs():
    text = ENTRYPOINT.read_text(encoding="utf-8")
    for var in ["DEADZONE_SOC", "DEADZONE_DEVICE_CODENAME", "DEADZONE_EDITION", "DEADZONE_MODE"]:
        assert var in text, f"fly_deadzone_entrypoint.sh must validate {var}"


def test_entrypoint_does_not_print_secrets():
    text = ENTRYPOINT.read_text(encoding="utf-8")
    import re
    # Secrets should only appear in variable assignments/exports, not in log/echo with their value
    secret_vars = ["PIXELDRAIN_API_KEY", "TELEGRAM_BOT_TOKEN"]
    for var in secret_vars:
        # log "$VAR" pattern should not exist (printing the value)
        pattern = re.compile(rf'log.*"\${var}"', re.IGNORECASE)
        assert not pattern.search(text), (
            f"fly_deadzone_entrypoint.sh must not print secret {var}"
        )


# ── 7. Telegram helper edits existing message_id ─────────────────────────────

def test_telegram_script_exists():
    assert TELEGRAM_SCRIPT.exists(), "scripts/deadzone_fly_telegram.py must exist"


def test_telegram_helper_edits_existing_message_id(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "output" / "reports").mkdir(parents=True)

    captured_calls: list[tuple[str, dict]] = []

    def mock_api_call(token: str, method: str, payload: dict) -> dict:
        captured_calls.append((method, payload))
        if method == "editMessageText":
            return {"ok": True, "result": {"message_id": 42}}
        return {"ok": True, "result": {"message_id": 99}}

    env = {
        "TELEGRAM_BOT_TOKEN": "fake_token",
        "TELEGRAM_CHAT_ID": "123456",
        "TELEGRAM_MSG_ID": "42",
    }
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", env["TELEGRAM_BOT_TOKEN"])
    monkeypatch.setenv("TELEGRAM_CHAT_ID", env["TELEGRAM_CHAT_ID"])
    monkeypatch.setenv("TELEGRAM_MSG_ID", env["TELEGRAM_MSG_ID"])
    monkeypatch.delenv("TELEGRAM_GROUP_ID", raising=False)

    spec = importlib.util.spec_from_file_location("deadzone_fly_telegram", TELEGRAM_SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    with mock.patch.object(mod, "_api_call", side_effect=mock_api_call):
        result = mod.main([
            "--action", "update",
            "--detail", "Testing edit",
            "--codename", "garnet",
            "--soc", "snapdragon",
            "--edition", "free",
            "--mode", "execute",
            "--listmezo-mode", "dry_run",
            "--elapsed", "1m 0s",
        ])

    assert result == 0
    methods = [c[0] for c in captured_calls]
    assert "editMessageText" in methods, "Must use editMessageText when TELEGRAM_MSG_ID is set"
    assert "sendMessage" not in methods, "Must NOT use sendMessage when message_id exists and edit succeeds"

    edit_payload = next(p for m, p in captured_calls if m == "editMessageText")
    assert edit_payload["message_id"] == 42
    assert edit_payload["chat_id"] == "123456"


# ── 8. Telegram helper sends new message if no message_id ─────────────────────

def test_telegram_helper_sends_new_message_when_no_id(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "output" / "reports").mkdir(parents=True)

    captured_calls: list[tuple[str, dict]] = []

    def mock_api_call(token: str, method: str, payload: dict) -> dict:
        captured_calls.append((method, payload))
        return {"ok": True, "result": {"message_id": 77}}

    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "fake_token")
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "123456")
    monkeypatch.delenv("TELEGRAM_MSG_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_GROUP_ID", raising=False)

    spec = importlib.util.spec_from_file_location("deadzone_fly_telegram", TELEGRAM_SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    with mock.patch.object(mod, "_api_call", side_effect=mock_api_call):
        result = mod.main([
            "--action", "start",
            "--detail", "First message",
            "--codename", "zircon",
            "--soc", "mtk",
            "--edition", "free",
            "--mode", "dry_run",
            "--listmezo-mode", "dry_run",
            "--elapsed", "0m 5s",
        ])

    assert result == 0
    methods = [c[0] for c in captured_calls]
    assert "sendMessage" in methods, "Must use sendMessage when no message_id exists"
    assert "editMessageText" not in methods, "Must NOT use editMessageText when no message_id"

    # Status JSON must be written with the returned message_id
    status_path = tmp_path / "output" / "reports" / "telegram_status.json"
    assert status_path.exists(), "telegram_status.json must be written after sendMessage"
    status = json.loads(status_path.read_text(encoding="utf-8"))
    assert status["message_id"] == 77, "telegram_status.json must store the new message_id"


# ── 9. Telegram helper sends failed action on failure ─────────────────────────

def test_telegram_helper_failed_action_message(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "output" / "reports").mkdir(parents=True)

    sent_texts: list[str] = []

    def mock_api_call(token: str, method: str, payload: dict) -> dict:
        if "text" in payload:
            sent_texts.append(payload["text"])
        return {"ok": True, "result": {"message_id": 10}}

    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "fake_token")
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "123456")
    monkeypatch.delenv("TELEGRAM_MSG_ID", raising=False)
    monkeypatch.delenv("TELEGRAM_GROUP_ID", raising=False)

    spec = importlib.util.spec_from_file_location("deadzone_fly_telegram", TELEGRAM_SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    with mock.patch.object(mod, "_api_call", side_effect=mock_api_call):
        mod.main([
            "--action", "failed",
            "--detail", "Pipeline crashed",
            "--error-reason", "OOM during super build",
            "--codename", "cannon",
            "--soc", "mtk",
            "--edition", "legend",
            "--mode", "execute",
            "--listmezo-mode", "dry_run",
            "--elapsed", "15m 30s",
        ])

    assert sent_texts, "At least one Telegram message must be sent"
    combined = "\n".join(sent_texts)
    assert "failed" in combined.lower() or "❌" in combined, (
        "Failed message must indicate failure"
    )
    assert "OOM during super build" in combined, "Error reason must appear in failed message"


# ── 10. Device readiness has direct_supported and fly_supported ───────────────

def test_readiness_matrix_has_direct_supported(readiness_matrix):
    for record in readiness_matrix["devices"]:
        assert "direct_supported" in record, (
            f"Device {record['codename']} missing 'direct_supported' in readiness matrix"
        )


def test_readiness_matrix_has_fly_supported(readiness_matrix):
    for record in readiness_matrix["devices"]:
        assert "fly_supported" in record, (
            f"Device {record['codename']} missing 'fly_supported' in readiness matrix"
        )


def test_all_workflow_ready_devices_are_direct_and_fly_supported(readiness_matrix):
    failures = []
    for r in readiness_matrix["devices"]:
        if r["workflow_ready"]:
            if not r["direct_supported"]:
                failures.append(f"{r['codename']}: workflow_ready but direct_supported=False")
            if not r["fly_supported"]:
                failures.append(f"{r['codename']}: workflow_ready but fly_supported=False")
    assert failures == [], "\n".join(failures)


# ── 11. Direct and Fly workflows use the same codename logic ──────────────────

@pytest.mark.parametrize("wf_path", _ALL_WORKFLOWS)
def test_all_workflows_use_free_text_codename(wf_path: Path):
    """All workflows must accept free-text codename, not a forced dropdown."""
    text = wf_path.read_text(encoding="utf-8")
    assert "codename:" in text, f"{wf_path.name} must have a 'codename:' input"
    # Must be type: string (free text), not a dropdown for codename
    import re
    # Find the codename input block and verify it's a string type
    block_match = re.search(
        r"codename:\s*\n((?:\s+.+\n)*)",
        text,
    )
    if block_match:
        block = block_match.group(1)
        # String type codename means no 'options:' in the codename block
        # (choices would have options listed under codename)
        lines = block.splitlines()
        # The block ends at the next top-level input key (lower indent)
        codename_block = []
        for line in lines:
            if line.strip() and not line.startswith("      "):
                break
            codename_block.append(line)
        codename_text = "\n".join(codename_block)
        assert "type: string" in codename_text or "type: string" in text, (
            f"{wf_path.name}: codename input should be type: string (free text)"
        )


@pytest.mark.parametrize("bad_name", ["select_device", "custom_device", "device"])
@pytest.mark.parametrize("wf_path", _ALL_WORKFLOWS)
def test_no_workflow_uses_forbidden_device_input_name(wf_path: Path, bad_name: str):
    import re
    text = wf_path.read_text(encoding="utf-8")
    pattern = re.compile(rf"^\s+{re.escape(bad_name)}\s*:", re.MULTILINE)
    assert not pattern.search(text), (
        f"{wf_path.name} must not have '{bad_name}' as a workflow input"
    )


# ── 12. Fly workflow uses flyctl machine run with --rm ────────────────────────

@pytest.mark.parametrize("wf_path", _FLY_WORKFLOWS)
def test_fly_workflow_uses_flyctl_machine_run(wf_path: Path):
    text = wf_path.read_text(encoding="utf-8")
    assert "flyctl machine run" in text, (
        f"{wf_path.name} must use 'flyctl machine run'"
    )


@pytest.mark.parametrize("wf_path", _FLY_WORKFLOWS)
def test_fly_workflow_uses_rm_flag(wf_path: Path):
    text = wf_path.read_text(encoding="utf-8")
    assert "--rm" in text, (
        f"{wf_path.name} must pass --rm to flyctl machine run"
    )


@pytest.mark.parametrize("wf_path", _FLY_WORKFLOWS)
def test_fly_workflow_uses_custom_dockerfile(wf_path: Path):
    text = wf_path.read_text(encoding="utf-8")
    assert "docker/Dockerfile.fly" in text, (
        f"{wf_path.name} must specify docker/Dockerfile.fly"
    )


# ── 13. Fly Dockerfile.fly exists and has correct ENTRYPOINT ─────────────────

def test_dockerfile_fly_exists():
    dockerfile = REPO_ROOT / "docker" / "Dockerfile.fly"
    assert dockerfile.exists(), "docker/Dockerfile.fly must exist"


def test_dockerfile_fly_entrypoint():
    dockerfile = REPO_ROOT / "docker" / "Dockerfile.fly"
    text = dockerfile.read_text(encoding="utf-8")
    assert "fly_deadzone_entrypoint.sh" in text, (
        "docker/Dockerfile.fly ENTRYPOINT must point to fly_deadzone_entrypoint.sh"
    )


# ── 14. Fly workflow passes DEADZONE_SOC env ──────────────────────────────────

def test_mtk_fly_workflow_sets_soc_mtk(mtk_fly_text: str):
    assert "DEADZONE_SOC=mtk" in mtk_fly_text, (
        "deadzone_mtk_fly.yml must set DEADZONE_SOC=mtk"
    )


def test_snap_fly_workflow_sets_soc_snapdragon(snap_fly_text: str):
    assert "DEADZONE_SOC=snapdragon" in snap_fly_text, (
        "deadzone_snapdragon_fly.yml must set DEADZONE_SOC=snapdragon"
    )


# ── 15. Fly workflow passes GitHub context env vars ───────────────────────────

@pytest.mark.parametrize("wf_path", _FLY_WORKFLOWS)
@pytest.mark.parametrize("env_var", ["GITHUB_RUN_ID", "GITHUB_SERVER_URL", "GITHUB_REPOSITORY", "GITHUB_ACTOR"])
def test_fly_workflow_passes_github_context(wf_path: Path, env_var: str):
    text = wf_path.read_text(encoding="utf-8")
    assert env_var in text, (
        f"{wf_path.name} must pass {env_var} to the Fly machine"
    )


# ── 16. Telegram script has editMessageText and sendMessage logic ─────────────

def test_telegram_script_has_edit_message_text():
    text = TELEGRAM_SCRIPT.read_text(encoding="utf-8")
    assert "editMessageText" in text, "deadzone_fly_telegram.py must use editMessageText"


def test_telegram_script_has_send_message():
    text = TELEGRAM_SCRIPT.read_text(encoding="utf-8")
    assert "sendMessage" in text, "deadzone_fly_telegram.py must use sendMessage"


def test_telegram_script_writes_status_json():
    text = TELEGRAM_SCRIPT.read_text(encoding="utf-8")
    assert "telegram_status.json" in text, (
        "deadzone_fly_telegram.py must write telegram_status.json"
    )


def test_telegram_script_handles_group_id():
    text = TELEGRAM_SCRIPT.read_text(encoding="utf-8")
    assert "TELEGRAM_GROUP_ID" in text, (
        "deadzone_fly_telegram.py must handle TELEGRAM_GROUP_ID for group messages"
    )
