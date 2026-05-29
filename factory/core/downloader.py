from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlparse
from urllib.request import urlretrieve

from factory.core.workspace import Workspace


def _source_name(source: str) -> str:
    parsed = urlparse(source)
    if parsed.scheme and parsed.netloc:
        return Path(unquote(parsed.path)).name or "source_rom"
    return Path(source).name or "source_rom"


def download_rom(rom_url: str, ws: Workspace) -> Path:
    target = ws.input / _source_name(rom_url)
    parsed = urlparse(rom_url)
    if parsed.scheme in {"http", "https"}:
        print(f"[DOWNLOAD] {rom_url}")
        if shutil.which("curl"):
            subprocess.run(["curl", "-L", "--fail", "-o", str(target), rom_url], check=True)
        else:
            urlretrieve(rom_url, target)
    else:
        src = Path(rom_url).expanduser().resolve()
        if src.is_dir():
            target = ws.input / src.name
            shutil.copytree(src, target, dirs_exist_ok=True)
        else:
            shutil.copy2(src, target)
    print(f"[INPUT] {target}")
    return target
