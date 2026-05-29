from __future__ import annotations

import shutil
from pathlib import Path

from factory.core.workspace import Workspace, write_json


def cleanup(ws: Workspace, keep_workspace: bool = True) -> dict:
    removed: list[str] = []
    kept: list[str] = []
    errors: list[str] = []

    preserve_names = {
        "final_zip_report.txt",
        "super_build_report.txt",
        "device_registry_report.txt",
        "super_profile_report.txt",
        "build_report.txt",
        "orchestration_report.txt",
    }

    def _remove(path: Path) -> None:
        if not path.exists():
            return
        try:
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            removed.append(str(path))
        except Exception as exc:
            errors.append(f"{path}: {exc}")

    if keep_workspace:
        status = "SKIPPED"
        kept.append(str(ws.root))
    else:
        status = "OK"
        for path in [ws.input, ws.extracted, ws.partitions, ws.final / "stage"]:
            _remove(path)
        for report_name in sorted(preserve_names):
            report = ws.reports / report_name
            if report.exists():
                kept.append(str(report))
        for path in [ws.final, ws.reports, ws.logs, ws.meta, ws.images]:
            if path.exists():
                kept.append(str(path))
    Path("output").mkdir(exist_ok=True)
    result = {"status": "FAILED" if errors else status, "removed": removed, "kept": kept, "errors": errors}
    write_json(ws.meta / "cleanup_result.json", result)
    return result
