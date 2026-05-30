from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

from factory.core.detector import DYNAMIC_PARTITIONS, RomInfo
from factory.core.toolchain import resolve_toolchain
from factory.core.workspace import Workspace, read_json, write_json


PARTITIONS = ("system", "product", "vendor", "system_ext", "mi_ext", "odm")
ANDROID_SPARSE_MAGIC = b"\x3a\xff\x26\xed"


def _base_partition(path: Path | str) -> str:
    return Path(str(path)).stem.removesuffix("_a").removesuffix("_b")


def _run(command: list[str], log: Path, cwd: Path | None = None) -> tuple[int, str]:
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a", encoding="utf-8") as fh:
        fh.write("$ " + " ".join(command) + "\n")
        try:
            proc = subprocess.run(command, cwd=cwd, stdout=fh, stderr=subprocess.STDOUT, text=True)
        except Exception as exc:
            fh.write(f"ERROR: {exc}\n")
            return 127, str(exc)
        fh.write(f"exit: {proc.returncode}\n\n")
    return proc.returncode, ""


def _count_tree(root: Path) -> tuple[int, int, int]:
    files = 0
    dirs = 0
    total = 0
    if not root.exists():
        return files, dirs, total
    for path in root.rglob("*"):
        if path.is_dir():
            dirs += 1
        elif path.is_file() or path.is_symlink():
            files += 1
            try:
                total += path.stat().st_size
            except OSError:
                continue
    return files, dirs, total


def _detect_format(image: Path, file_tool: Path | None) -> tuple[str, str]:
    try:
        with image.open("rb") as fh:
            header = fh.read(4096)
    except OSError as exc:
        return "unknown", str(exc)
    if header.startswith(ANDROID_SPARSE_MAGIC):
        return "android_sparse", "android sparse magic"
    if header[0x438:0x43A] == b"\x53\xef":
        return "raw_ext4", "ext filesystem magic"
    if b"EROFS" in header[:2048] or header[1024:1028] == b"EroS":
        return "raw_erofs", "erofs magic"
    if file_tool:
        proc = subprocess.run([str(file_tool), "-b", str(image)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        output = proc.stdout.strip()
        lowered = output.lower()
        if "android sparse" in lowered:
            return "android_sparse", output
        if "ext" in lowered and "filesystem" in lowered:
            return "raw_ext4", output
        if "erofs" in lowered:
            return "raw_erofs", output
        return "unknown", output
    return "unknown", "no file tool and no known magic matched"


def _image_candidates(ws: Workspace, inspection: dict[str, Any]) -> dict[str, Path]:
    found: dict[str, Path] = {}
    partition_map = inspection.get("partition_map") if isinstance(inspection.get("partition_map"), dict) else {}
    for name, rel in partition_map.items():
        base = _base_partition(name)
        if base in DYNAMIC_PARTITIONS:
            path = ws.root / str(rel)
            if path.is_file():
                found[base] = path
    for image in sorted(ws.images.glob("*.img")):
        base = _base_partition(image)
        if base in DYNAMIC_PARTITIONS:
            found.setdefault(base, image)
    return found


def _extract_super_if_needed(ws: Workspace, images: dict[str, Path], toolchain: Any) -> dict[str, Any]:
    wanted = set(PARTITIONS)
    if wanted & set(images):
        return {"status": "skipped", "reason": "partition images already present"}
    super_img = ws.images / "super.img"
    if not super_img.is_file():
        return {"status": "skipped", "reason": "super.img not present"}
    lpunpack = toolchain.path("lpunpack")
    if not lpunpack:
        return {"status": "skipped", "reason": "lpunpack not available"}
    log = ws.logs / "image_extraction_lpunpack.log"
    code, error = _run([str(lpunpack), str(super_img), str(ws.images)], log)
    return {
        "status": "extracted" if code == 0 else "failed",
        "reason": error if error else ("" if code == 0 else f"lpunpack exited {code}"),
        "tool": str(lpunpack),
        "log": str(log),
    }


def _sparse_to_raw(image: Path, partition: str, ws: Workspace, simg2img: Path, log: Path) -> tuple[Path | None, str]:
    raw = ws.partitions / f".{partition}.raw.img"
    code, error = _run([str(simg2img), str(image), str(raw)], log)
    if code == 0 and raw.is_file():
        return raw, ""
    return None, error or f"simg2img exited {code}"


def _extract_ext4(image: Path, target: Path, toolchain: Any, log: Path) -> tuple[str, str, str]:
    debugfs = toolchain.path("debugfs")
    if debugfs:
        target.mkdir(parents=True, exist_ok=True)
        code, error = _run([str(debugfs), "-R", f"rdump / {target}", str(image)], log)
        if code == 0 and any(target.iterdir()):
            return "extracted", "debugfs rdump", str(debugfs)
        if error:
            return "failed", f"debugfs failed: {error}", str(debugfs)

    mount = toolchain.path("mount")
    if mount and hasattr(os, "geteuid") and os.geteuid() == 0:
        mount_dir = target.parent / f".{target.name}_mount"
        mount_dir.mkdir(parents=True, exist_ok=True)
        target.mkdir(parents=True, exist_ok=True)
        code, error = _run([str(mount), "-o", "ro,loop", str(image), str(mount_dir)], log)
        if code == 0:
            try:
                shutil.copytree(mount_dir, target, dirs_exist_ok=True, symlinks=True)
                return "extracted", "read-only loop mount", str(mount)
            finally:
                _run(["umount", str(mount_dir)], log)
        return "failed", error or f"mount exited {code}", str(mount)

    if debugfs:
        return "failed", "debugfs rdump did not produce files", str(debugfs)
    return "failed", "no EXT4 extraction method available", ""


def _extract_erofs(image: Path, target: Path, toolchain: Any, log: Path) -> tuple[str, str, str]:
    dump = toolchain.path("dump.erofs")
    if dump:
        target.mkdir(parents=True, exist_ok=True)
        attempts = [
            [str(dump), "--extract=/", f"--path={target}", str(image)],
            [str(dump), "-x", "-C", str(target), str(image)],
        ]
        for command in attempts:
            code, _error = _run(command, log)
            if code == 0 and any(target.iterdir()):
                return "extracted", "dump.erofs extract", str(dump)
        listing = target.parent / f"{target.name}_erofs_listing.txt"
        with listing.open("w", encoding="utf-8") as out:
            proc = subprocess.run([str(dump), str(image)], stdout=out, stderr=subprocess.STDOUT, text=True)
        with log.open("a", encoding="utf-8") as fh:
            fh.write(f"$ {dump} {image} > {listing}\nexit: {proc.returncode}\n\n")
        if listing.is_file() and listing.stat().st_size > 0:
            return "listed_only", f"extraction failed; listing written to {listing}", str(dump)
    fsck = toolchain.path("fsck.erofs")
    if fsck:
        listing = target.parent / f"{target.name}_erofs_fsck.txt"
        with listing.open("w", encoding="utf-8") as out:
            proc = subprocess.run([str(fsck), "--extract", str(target), str(image)], stdout=out, stderr=subprocess.STDOUT, text=True)
        with log.open("a", encoding="utf-8") as fh:
            fh.write(f"$ {fsck} --extract {target} {image}\nexit: {proc.returncode}\n\n")
        if target.exists() and any(target.iterdir()):
            return "extracted", "fsck.erofs extract", str(fsck)
        if listing.is_file() and listing.stat().st_size > 0:
            return "listed_only", f"fsck.erofs did not extract; output written to {listing}", str(fsck)
    fuse = toolchain.path("erofsfuse")
    if fuse:
        return "failed", "erofsfuse is available but FUSE mounting is not attempted in non-interactive CI", str(fuse)
    return "failed", "no EROFS extraction or listing method available", ""


def _extract_7z(image: Path, target: Path, toolchain: Any, log: Path) -> tuple[str, str, str]:
    seven = toolchain.path("7z")
    if not seven:
        return "failed", "7z not available", ""
    target.mkdir(parents=True, exist_ok=True)
    code, error = _run([str(seven), "x", f"-o{target}", str(image), "-y"], log)
    if code == 0 and any(target.iterdir()):
        return "extracted", "7z extract", str(seven)
    return "failed", error or f"7z exited {code}", str(seven)


def _entry(partition: str, image: Path | None, fmt: str, method: str, tool: str, target: Path, status: str, reason: str = "") -> dict[str, Any]:
    files, dirs, total = _count_tree(target)
    return {
        "partition": partition,
        "source_image": str(image or ""),
        "detected_format": fmt,
        "extraction_method": method,
        "tool_path": tool,
        "extracted_path": str(target),
        "status": status,
        "file_count": files,
        "directory_count": dirs,
        "total_extracted_bytes": total,
        "failure_reason": reason,
    }


def _write_report(ws: Workspace, data: dict[str, Any]) -> None:
    lines = [
        "DeadZone Image Extraction Report",
        "================================",
        f"status: {data.get('status')}",
        f"partitions: {len(data.get('partitions') or [])}",
        "",
        "super extraction:",
    ]
    super_data = data.get("super_extraction") if isinstance(data.get("super_extraction"), dict) else {}
    for key in ("status", "reason", "tool", "log"):
        lines.append(f"  {key}: {super_data.get(key) or '(none)'}")
    lines += ["", "partition results:"]
    for item in data.get("partitions") or []:
        lines.extend([
            f"- partition: {item.get('partition')}",
            f"  source image: {item.get('source_image') or '(none)'}",
            f"  format: {item.get('detected_format')}",
            f"  method: {item.get('extraction_method') or '(none)'}",
            f"  tool: {item.get('tool_path') or '(none)'}",
            f"  extracted path: {item.get('extracted_path')}",
            f"  status: {item.get('status')}",
            f"  files: {item.get('file_count')}",
            f"  directories: {item.get('directory_count')}",
            f"  bytes: {item.get('total_extracted_bytes')}",
            f"  failure reason: {item.get('failure_reason') or '(none)'}",
        ])
    ws.reports.mkdir(parents=True, exist_ok=True)
    (ws.reports / "image_extraction_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    write_json(ws.meta / "image_extraction.json", data)


def extract_partition_images(ws: Workspace, info: RomInfo, inspection: dict[str, Any]) -> dict[str, Any]:
    toolchain = resolve_toolchain(ws)
    images = _image_candidates(ws, inspection)
    super_result = _extract_super_if_needed(ws, images, toolchain)
    if super_result.get("status") == "extracted":
        images = _image_candidates(ws, read_json(ws.meta / "inspection.json", inspection))
        images.update({p.stem.removesuffix("_a").removesuffix("_b"): p for p in ws.images.glob("*.img") if _base_partition(p) in DYNAMIC_PARTITIONS})

    results: list[dict[str, Any]] = []
    for partition in PARTITIONS:
        image = images.get(partition)
        target = ws.partitions / partition
        log = ws.logs / f"image_extraction_{partition}.log"
        if not image or not image.is_file():
            item = _entry(partition, image, "missing", "", "", target, "skipped", "partition image not found")
            results.append(item)
            print(f"[IMAGE EXTRACTION] Partition: {partition}")
            print("[IMAGE EXTRACTION] Format: missing")
            print("[IMAGE EXTRACTION] Method: skipped")
            continue
        fmt, detail = _detect_format(image, toolchain.path("file"))
        source = image
        if fmt == "android_sparse":
            simg2img = toolchain.path("simg2img")
            if not simg2img:
                item = _entry(partition, image, fmt, "simg2img", "", target, "failed", "simg2img not available")
                results.append(item)
                continue
            raw, error = _sparse_to_raw(image, partition, ws, simg2img, log)
            if not raw:
                item = _entry(partition, image, fmt, "simg2img", str(simg2img), target, "failed", error)
                results.append(item)
                continue
            source = raw
            fmt, detail = _detect_format(source, toolchain.path("file"))

        if fmt == "raw_ext4":
            status, method_or_reason, tool = _extract_ext4(source, target, toolchain, log)
            method = method_or_reason if status == "extracted" else "ext4 extraction"
            reason = "" if status == "extracted" else method_or_reason
        elif fmt == "raw_erofs":
            status, method_or_reason, tool = _extract_erofs(source, target, toolchain, log)
            method = method_or_reason if status == "extracted" else "erofs extraction/listing"
            reason = "" if status == "extracted" else method_or_reason
        else:
            status, reason, tool = _extract_7z(source, target, toolchain, log)
            method = "7z fallback"
            if status != "extracted" and not reason:
                reason = detail
        item = _entry(partition, image, fmt, method, tool, target, status, reason)
        results.append(item)
        print(f"[IMAGE EXTRACTION] Partition: {partition}")
        print(f"[IMAGE EXTRACTION] Format: {fmt}")
        print(f"[IMAGE EXTRACTION] Method: {method}")

    extracted = sum(1 for item in results if item["status"] == "extracted")
    listed = sum(1 for item in results if item["status"] == "listed_only")
    failed = sum(1 for item in results if item["status"] == "failed")
    data = {
        "feature": "Stable App Inventory",
        "status": "ok" if extracted or listed else "no_extractable_partitions",
        "rom": {
            "codename": getattr(info, "codename", "unknown"),
            "android_version": getattr(info, "android_version", "unknown"),
            "build": getattr(info, "build", "unknown"),
        },
        "summary": {"extracted": extracted, "listed_only": listed, "failed": failed, "skipped": sum(1 for item in results if item["status"] == "skipped")},
        "super_extraction": super_result,
        "partitions": results,
    }
    _write_report(ws, data)
    return data
