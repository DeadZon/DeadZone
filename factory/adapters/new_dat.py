from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from factory.core.workspace import Workspace


def _part_name(path: Path) -> str:
    return path.name[: -len(".new.dat.br")]


def _convert(transfer: Path, new_dat: Path, out_img: Path) -> None:
    third_party = Path("third_party/mezo_core").resolve()
    if third_party.exists() and str(third_party) not in sys.path:
        sys.path.insert(0, str(third_party))
    try:
        from src.core.utils import Sdat2img  # type: ignore
        Sdat2img(str(transfer), str(new_dat), str(out_img))
        return
    except Exception:
        if not shutil.which("sdat2img"):
            raise
    subprocess.run(["sdat2img", str(transfer), str(new_dat), str(out_img)], check=True)


def adapt(extracted: Path, ws: Workspace) -> dict:
    converted: list[str] = []
    for br in sorted(extracted.rglob("*.new.dat.br")):
        part = _part_name(br)
        transfer = br.with_name(f"{part}.transfer.list")
        if not transfer.is_file():
            raise RuntimeError(f"missing transfer list for {br.name}")
        new_dat = ws.partitions / f"{part}.new.dat"
        out_img = ws.images / f"{part}.img"
        try:
            import brotli  # type: ignore
            new_dat.write_bytes(brotli.decompress(br.read_bytes()))
        except Exception:
            if not shutil.which("brotli"):
                raise
            subprocess.run(["brotli", "--decompress", "--output", str(new_dat), str(br)], check=True)
        _convert(transfer, new_dat, out_img)
        converted.append(out_img.name)
    if not converted:
        raise RuntimeError("no *.new.dat.br files found")
    return {"adapter": "new_dat", "images": converted}
