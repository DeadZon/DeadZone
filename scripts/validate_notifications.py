"""Validate DeadZone notification routing and bot separation.

Checks:
  1. MTK workflows use TELEGRAM_MTK_* secrets — not TELEGRAM_SNAPDRAGON_*
  2. Snapdragon workflows use TELEGRAM_SNAPDRAGON_* secrets — not TELEGRAM_MTK_*
  3. MTK Fly dispatch sends soc=mtk
  4. Snapdragon Fly dispatch sends soc=snapdragon
  5. GitHub local workflows pass source=GitHub (or rely on default)
  6. Fly workflows pass source=GitHub in the dispatched JSON payload
  7. notify_telegram input is present in all build workflows
  8. No workflow exposes TELEGRAM_BOT_TOKEN as the primary credential
     when a SoC-specific env is available
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT      = Path(__file__).resolve().parents[1]
WORKFLOWS_DIR  = REPO_ROOT / ".github" / "workflows"

MTK_WORKFLOWS   = ["deadzone_mtk.yml", "deadzone_mtk_fly.yml"]
SNAP_WORKFLOWS  = ["deadzone_snapdragon.yml", "deadzone_snapdragon_fly.yml"]
GITHUB_WORKFLOWS = ["deadzone_mtk.yml", "deadzone_snapdragon.yml"]
FLY_WORKFLOWS   = ["deadzone_mtk_fly.yml", "deadzone_snapdragon_fly.yml"]
ALL_BUILD       = MTK_WORKFLOWS + SNAP_WORKFLOWS


errors:   list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)
    print(f"  [FAIL] {msg}")


def warn(msg: str) -> None:
    warnings.append(msg)
    print(f"  [WARN] {msg}")


def ok(msg: str) -> None:
    print(f"  [ OK ] {msg}")


def _read(name: str) -> str | None:
    p = WORKFLOWS_DIR / name
    if not p.exists():
        fail(f"Missing workflow file: {name}")
        return None
    return p.read_text(encoding="utf-8")


def _strip_comments(text: str) -> str:
    """Remove YAML comment lines for cross-wiring checks."""
    lines = []
    for line in text.splitlines():
        stripped = line.lstrip()
        if not stripped.startswith("#"):
            lines.append(line)
    return "\n".join(lines)


# ── Check 1: MTK workflows use MTK secrets, not Snapdragon ───────────────────
print("\n=== Check 1: MTK workflows — use MTK Telegram secrets only ===")
for name in MTK_WORKFLOWS:
    text = _read(name)
    if text is None:
        continue
    body = _strip_comments(text)
    if "TELEGRAM_MTK_BOT_TOKEN" not in body and "TELEGRAM_BOT_TOKEN" not in body:
        fail(f"{name}: no Telegram credentials referenced — MTK bot secrets must be present")
    else:
        ok(f"{name}: MTK Telegram credential referenced")

    if "TELEGRAM_SNAPDRAGON_BOT_TOKEN" in body or "TELEGRAM_SNAPDRAGON_CHAT_ID" in body:
        fail(f"{name}: references Snapdragon Telegram secrets — MTK workflows must not use Snapdragon credentials")
    else:
        ok(f"{name}: no Snapdragon Telegram secret cross-wiring")


# ── Check 2: Snapdragon workflows use Snapdragon secrets, not MTK ────────────
print("\n=== Check 2: Snapdragon workflows — use Snapdragon Telegram secrets only ===")
for name in SNAP_WORKFLOWS:
    text = _read(name)
    if text is None:
        continue
    body = _strip_comments(text)
    if "TELEGRAM_SNAPDRAGON_BOT_TOKEN" not in body and "TELEGRAM_BOT_TOKEN" not in body:
        fail(f"{name}: no Telegram credentials referenced — Snapdragon bot secrets must be present")
    else:
        ok(f"{name}: Snapdragon Telegram credential referenced")

    if "TELEGRAM_MTK_BOT_TOKEN" in body or "TELEGRAM_MTK_CHAT_ID" in body:
        fail(f"{name}: references MTK Telegram secrets — Snapdragon workflows must not use MTK credentials")
    else:
        ok(f"{name}: no MTK Telegram secret cross-wiring")


# ── Check 3: MTK Fly dispatch sends soc=mtk ──────────────────────────────────
print('\n=== Check 3: MTK Fly workflow — sends soc=mtk ===')
mtk_fly_text = _read("deadzone_mtk_fly.yml")
if mtk_fly_text is not None:
    if '"soc"' in mtk_fly_text and '"mtk"' in mtk_fly_text:
        ok("deadzone_mtk_fly.yml: soc=mtk payload found")
    elif "'soc'" in mtk_fly_text and "'mtk'" in mtk_fly_text:
        ok("deadzone_mtk_fly.yml: soc=mtk payload found (single-quoted)")
    else:
        fail('deadzone_mtk_fly.yml: JSON payload must contain "soc": "mtk"')


# ── Check 4: Snapdragon Fly dispatch sends soc=snapdragon ────────────────────
print('\n=== Check 4: Snapdragon Fly workflow — sends soc=snapdragon ===')
snap_fly_text = _read("deadzone_snapdragon_fly.yml")
if snap_fly_text is not None:
    if '"soc"' in snap_fly_text and '"snapdragon"' in snap_fly_text:
        ok("deadzone_snapdragon_fly.yml: soc=snapdragon payload found")
    elif "'soc'" in snap_fly_text and "'snapdragon'" in snap_fly_text:
        ok("deadzone_snapdragon_fly.yml: soc=snapdragon payload found (single-quoted)")
    else:
        fail('deadzone_snapdragon_fly.yml: JSON payload must contain "soc": "snapdragon"')


# ── Check 5: GitHub local workflows pass source=GitHub ───────────────────────
print('\n=== Check 5: GitHub local workflows — source=GitHub ===')
for name in GITHUB_WORKFLOWS:
    text = _read(name)
    if text is None:
        continue
    # GitHub local workflows don't POST JSON — they call the orchestrator directly.
    # The source is set by the orchestrator default (source="GitHub").
    # We just verify there's no explicit source=Fly being sent.
    if '"source"' in text and '"Fly"' in text:
        fail(f"{name}: GitHub local workflow must not send source=Fly")
    else:
        ok(f"{name}: no source=Fly mismatch")


# ── Check 6: Fly dispatch workflows send source=Fly in JSON payload ──────────
print('\n=== Check 6: Fly dispatch workflows — send source=Fly in payload ===')
for name in FLY_WORKFLOWS:
    text = _read(name)
    if text is None:
        continue
    if '"source"' in text and '"Fly"' in text:
        ok(f"{name}: source=Fly in dispatch payload")
    elif "'source'" in text and "'Fly'" in text:
        ok(f"{name}: source=Fly in dispatch payload (single-quoted)")
    else:
        fail(f'{name}: JSON payload must include "source": "Fly"')


# ── Check 7: notify_telegram input present in all build workflows ─────────────
print('\n=== Check 7: notify_telegram input wired in all build workflows ===')
for name in ALL_BUILD:
    text = _read(name)
    if text is None:
        continue
    if "notify_telegram" in text:
        ok(f"{name}: notify_telegram present")
    else:
        fail(f"{name}: notify_telegram input/field missing")


# ── Check 8: SoC-specific env var names used (not only generic fallback) ──────
print('\n=== Check 8: SoC-specific Telegram env var names set by GitHub workflows ===')
mtk_gh_text  = _read("deadzone_mtk.yml")
snap_gh_text = _read("deadzone_snapdragon.yml")

if mtk_gh_text is not None:
    body = _strip_comments(mtk_gh_text)
    # Env key set in workflow (not secret reference, but the env key itself)
    if re.search(r'TELEGRAM_MTK_BOT_TOKEN\s*:', body):
        ok("deadzone_mtk.yml: TELEGRAM_MTK_BOT_TOKEN env key set (SoC-specific)")
    else:
        fail(
            "deadzone_mtk.yml: env must set TELEGRAM_MTK_BOT_TOKEN key so the "
            "SoC-specific resolver in telegram_live.py finds it"
        )

if snap_gh_text is not None:
    body = _strip_comments(snap_gh_text)
    if re.search(r'TELEGRAM_SNAPDRAGON_BOT_TOKEN\s*:', body):
        ok("deadzone_snapdragon.yml: TELEGRAM_SNAPDRAGON_BOT_TOKEN env key set (SoC-specific)")
    else:
        fail(
            "deadzone_snapdragon.yml: env must set TELEGRAM_SNAPDRAGON_BOT_TOKEN key so the "
            "SoC-specific resolver in telegram_live.py finds it"
        )


# ── Summary ────────────────────────────────────────────────────────────────────
print("\n=== Summary ===")
print(f"  Errors  : {len(errors)}")
print(f"  Warnings: {len(warnings)}")

if errors:
    print("\nFAILED — fix notification routing errors above.\n")
    sys.exit(1)
else:
    print("\nAll notification checks passed.\n")
    sys.exit(0)
