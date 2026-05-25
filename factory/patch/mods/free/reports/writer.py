"""Free mod report writer."""
from __future__ import annotations
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[5]
_REPORTS_DIR = _REPO_ROOT / "output" / "reports"


def write_mod_report(report: dict) -> None:
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    txt = _REPORTS_DIR / "mod_free_report.txt"
    import json
    jsn = _REPORTS_DIR / "mod_free_report.json"
    txt.write_text(_format_report(report), encoding="utf-8")
    jsn.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")


def _format_report(r: dict) -> str:
    lines = [
        f"Mod: free",
        f"Status: {r.get('final_status', 'UNKNOWN')}",
        f"Applied: {r.get('applied_steps', [])}",
        f"Skipped: {r.get('skipped_steps', [])}",
        f"Warnings: {len(r.get('warnings', []))}",
        f"Errors: {len(r.get('errors', []))}",
    ]
    return "\n".join(lines) + "\n"
