from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
import stat
from pathlib import Path

from factory.adapters.common import copy_images
from factory.core.workspace import Workspace, read_json, write_json


MISSING_TOOL_MESSAGE = "payload-dumper-go is missing. Add it to tools/helper or install it in Docker/GitHub runner."


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


def _helper_candidates(tool: str) -> list[Path]:
    exe = f"{tool}.exe" if os.name == "nt" else tool
    system_name = platform.system().lower()
    machine = platform.machine()
    roots = [
        Path("tools/helper"),
        Path("tools/helper/bin"),
        Path("tools/helper/bin") / system_name,
        Path("tools/helper/bin") / system_name / machine,
        Path("tools/helper/bin/linux"),
        Path("tools/helper/bin/windows"),
    ]
    return [root / exe for root in roots] + [root / tool for root in roots if exe != tool]


def _resolve_payload_tool() -> Path | None:
    for candidate in _helper_candidates("payload-dumper-go"):
        if candidate.is_file():
            if os.name == "posix":
                try:
                    candidate.chmod(candidate.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                except OSError:
                    pass
            return candidate.resolve()
    found = shutil.which("payload-dumper-go") or shutil.which("payload-dumper-go.exe")
    return Path(found).resolve() if found else None


def _stage_payload_files(extracted: Path, ws: Workspace) -> Path:
    payloads = sorted(extracted.rglob("payload.bin"))
    if not payloads:
        raise RuntimeError("payload.bin not found")

    payload_dir = ws.extracted / "payload"
    payload_dir.mkdir(parents=True, exist_ok=True)
    staged_payload = payload_dir / "payload.bin"
    if payloads[0].resolve() != staged_payload.resolve():
        shutil.copy2(payloads[0], staged_payload)

    for props in sorted(extracted.rglob("payload_properties.txt")):
        staged_props = payload_dir / "payload_properties.txt"
        if props.resolve() != staged_props.resolve():
            shutil.copy2(props, staged_props)
        break
    return staged_payload


def _dumped_images(ws: Workspace) -> list[Path]:
    return sorted(p for p in ws.images.glob("*.img") if p.is_file() and p.stat().st_size > 0)


def _first_lines(path: Path, count: int = 50) -> list[str]:
    if not path.is_file():
        return []
    return path.read_text(encoding="utf-8", errors="replace").splitlines()[:count]


def _write_payload_report(
    ws: Workspace,
    *,
    tool: Path | None,
    command: list[str],
    exit_code: int | None,
    images: list[Path],
    error: str = "",
) -> Path:
    stderr_path = ws.logs / "payload_dump_stderr.log"
    report_path = ws.reports / "payload_unpack_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    stderr_lines = _first_lines(stderr_path, 50)
    lines = [
        "MEZO / DeadZone Payload Unpack Report",
        "=====================================",
        f"tool path: {tool or '(missing)'}",
        f"command: {' '.join(command) if command else '(not run)'}",
        f"exit code: {exit_code if exit_code is not None else '(not run)'}",
        f"output directory: {ws.images}",
        f"found image count: {len(images)}",
        f"images: {', '.join(p.name for p in images) if images else '(none)'}",
        f"error: {error or '(none)'}",
        "",
        "first 50 lines of stderr:",
        *(stderr_lines or ["(none)"]),
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def _update_payload_metadata(ws: Workspace, images: list[Path], dumped: bool) -> None:
    image_names = [p.name for p in images]
    partition_map = read_json(ws.meta / "partition_map.json", {})
    by_partition = partition_map.get("by_partition") if isinstance(partition_map.get("by_partition"), dict) else {}
    by_partition.update({p.stem.removesuffix("_a").removesuffix("_b"): str(p.relative_to(ws.root)) for p in images})
    partition_map["by_partition"] = dict(sorted(by_partition.items()))
    seen = set(partition_map.get("source_images_seen") or [])
    seen.update(image_names)
    partition_map["source_images_seen"] = sorted(seen)
    write_json(ws.meta / "partition_map.json", partition_map)

    rom_info = read_json(ws.meta / "rom_info.json", {})
    rom_info.update({
        "has_payload": True,
        "payload_dumped": dumped,
        "payload_image_count": len(images),
    })
    write_json(ws.meta / "rom_info.json", rom_info)


def adapt(extracted: Path, ws: Workspace) -> dict:
    payload_bin = _stage_payload_files(extracted, ws)
    sizes = _payload_sizes(payload_bin)
    stdout_path = ws.logs / "payload_dump_stdout.log"
    stderr_path = ws.logs / "payload_dump_stderr.log"
    stdout_path.write_text("", encoding="utf-8")
    stderr_path.write_text("", encoding="utf-8")

    tool = _resolve_payload_tool()
    command: list[str] = []
    exit_code: int | None = None
    if tool is None:
        images = _dumped_images(ws)
        _update_payload_metadata(ws, images, dumped=False)
        _write_payload_report(ws, tool=tool, command=command, exit_code=exit_code, images=images, error=MISSING_TOOL_MESSAGE)
        print("[PAYLOAD] Tool: (missing)")
        print("[PAYLOAD] Command: (not run)")
        print(f"[PAYLOAD] Output: {ws.images}")
        print(f"[PAYLOAD] Images dumped: {len(images)}")
        raise RuntimeError(MISSING_TOOL_MESSAGE)

    command = [str(tool), "-o", str(ws.images), str(payload_bin)]
    print(f"[PAYLOAD] Tool: {tool}")
    print(f"[PAYLOAD] Command: {' '.join(command)}")
    print(f"[PAYLOAD] Output: {ws.images}")
    with stdout_path.open("w", encoding="utf-8") as stdout, stderr_path.open("w", encoding="utf-8") as stderr:
        result = subprocess.run(command, stdout=stdout, stderr=stderr)
    exit_code = result.returncode
    ok = exit_code == 0 and bool(_dumped_images(ws))

    images = _dumped_images(ws)
    _update_payload_metadata(ws, images, dumped=ok)
    _write_payload_report(ws, tool=tool, command=command, exit_code=exit_code, images=images)
    print(f"[PAYLOAD] Images dumped: {len(images)}")
    if not ok:
        _write_payload_report(
            ws,
            tool=tool,
            command=command,
            exit_code=exit_code,
            images=images,
            error="payload-dumper-go ran but produced no images",
        )
        raise RuntimeError(
            f"payload-dumper-go ran but produced no images. See {ws.reports / 'payload_unpack_report.txt'}"
        )
    return {"adapter": "payload", "images": copy_images(ws.images, ws.images), "partition_sizes": sizes}
