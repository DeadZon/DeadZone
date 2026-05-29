from __future__ import annotations

import contextlib
import io
import shutil
import subprocess
import sys
from pathlib import Path

from factory.adapters.common import copy_images
from factory.core.workspace import Workspace


def _payload_sizes(payload_bin: Path) -> dict[str, int]:
    third_party = Path("third_party/mezo_core/src").resolve()
    if third_party.exists() and str(third_party) not in sys.path:
        sys.path.insert(0, str(third_party))
    try:
        from core.payload_extract import init_payload_info  # type: ignore
        with payload_bin.open("rb") as fh:
            manifest = init_payload_info(fh)
        return {
            p.partition_name: int(p.new_partition_info.size)
            for p in manifest.partitions
            if p.HasField("new_partition_info") and p.new_partition_info.size > 0
        }
    except Exception:
        return {}


def adapt(extracted: Path, ws: Workspace) -> dict:
    payloads = list(extracted.rglob("payload.bin"))
    if not payloads:
        raise RuntimeError("payload.bin not found")
    payload_bin = payloads[0]
    sizes = _payload_sizes(payload_bin)
    log_path = ws.logs / "payload_extract.log"
    ok = False

    third_party = Path("third_party/mezo_core/src").resolve()
    if third_party.exists() and str(third_party) not in sys.path:
        sys.path.insert(0, str(third_party))
    try:
        from core.payload_extract import extract_partitions_from_payload  # type: ignore
        buf = io.StringIO()
        with payload_bin.open("rb") as fh, contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            extract_partitions_from_payload(fh, [], str(ws.images), max_workers=32)
        log_path.write_text(buf.getvalue(), encoding="utf-8", errors="replace")
        ok = any(ws.images.glob("*.img"))
    except Exception as exc:
        log_path.write_text(f"Internal payload extractor failed: {exc}\n", encoding="utf-8")

    if not ok and shutil.which("payload-dumper-go"):
        with log_path.open("a", encoding="utf-8") as log:
            result = subprocess.run(["payload-dumper-go", "-output", str(ws.images), str(payload_bin)], stdout=log, stderr=subprocess.STDOUT)
        ok = result.returncode == 0 and any(ws.images.glob("*.img"))

    if not ok:
        raise RuntimeError("payload.bin was extracted but could not be dumped into images")
    return {"adapter": "payload", "images": copy_images(ws.images, ws.images), "partition_sizes": sizes}
