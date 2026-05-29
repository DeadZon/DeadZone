from __future__ import annotations

import shutil
from pathlib import Path

from factory.core.workspace import Workspace


def cleanup(ws: Workspace, keep_workspace: bool = True) -> None:
    if not keep_workspace and ws.root.exists():
        shutil.rmtree(ws.root)
    Path("output").mkdir(exist_ok=True)
