"""Legend report action — prints or re-formats the last Legend patch report."""
from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[4]
_DEFAULT_REPORT = _REPO_ROOT / "output" / "reports" / "deadzone_patch_report.txt"


def print_last_report(report_path: Path | None = None) -> None:
    path = Path(report_path) if report_path else _DEFAULT_REPORT
    if not path.is_file():
        print(f"[report_legend] No report found at {path}")
        return
    print(path.read_text(encoding="utf-8", errors="replace"))


def main(argv: list[str] | None = None) -> int:
    import argparse
    p = argparse.ArgumentParser(description="Print last DeadZone Legend patch report")
    p.add_argument("--report", type=Path, default=None)
    args = p.parse_args(argv)
    print_last_report(args.report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
