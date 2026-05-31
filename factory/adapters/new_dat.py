from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from factory.core.workspace import Workspace, write_json


# ── Tool resolution ────────────────────────────────────────────────────────────

def resolve_brotli_tool() -> dict[str, Any]:
    """Return brotli tool availability: Python module first, then CLI fallback."""
    try:
        import brotli  # type: ignore  # noqa: F401
        return {"method": "module", "available": True, "detail": "brotli python module", "error": ""}
    except ImportError:
        pass
    if shutil.which("brotli"):
        return {"method": "cli", "available": True, "detail": "brotli CLI", "error": ""}
    return {
        "method": "none",
        "available": False,
        "detail": "",
        "error": (
            "brotli decompressor not found. "
            "Install the Python brotli module ('pip install brotli') "
            "or place the brotli CLI in PATH."
        ),
    }


def resolve_sdat2img_tool() -> dict[str, Any]:
    """Return sdat2img tool availability: mezo_core first, then CLI fallback."""
    third_party = Path("third_party/mezo_core").resolve()
    if third_party.exists():
        saved = sys.path[:]
        probe = str(third_party)
        try:
            if probe not in sys.path:
                sys.path.insert(0, probe)
            from src.core.utils import Sdat2img  # type: ignore  # noqa: F401
            return {"method": "mezo_core", "available": True, "detail": str(third_party), "error": ""}
        except Exception:
            sys.path = saved
    if shutil.which("sdat2img"):
        return {"method": "cli", "available": True, "detail": "sdat2img CLI", "error": ""}
    return {
        "method": "none",
        "available": False,
        "detail": "",
        "error": (
            "sdat2img not found. "
            "Ensure third_party/mezo_core contains src/core/utils.py with Sdat2img, "
            "or install the sdat2img CLI in PATH."
        ),
    }


# ── Discovery ──────────────────────────────────────────────────────────────────

def detect_new_dat_partitions(
    source_dir: Path,
) -> list[tuple[str, Path, Path | None]]:
    """Find all *.new.dat.br files under *source_dir*.

    Returns (partition_name, br_path, transfer_path_or_None) for each file.
    transfer_path is None when the matching *.transfer.list is absent.
    """
    results: list[tuple[str, Path, Path | None]] = []
    for br in sorted(source_dir.rglob("*.new.dat.br")):
        part = br.name[: -len(".new.dat.br")]
        transfer = br.with_name(f"{part}.transfer.list")
        results.append((part, br, transfer if transfer.is_file() else None))
    return results


def parse_dynamic_partitions_op_list(path: Path) -> list[str]:
    """Parse *path* and return partition names from 'add <part> ...' lines.

    Lines starting with '#' are ignored.  'add_group' lines describe partition
    groups, not partitions, and are skipped.  Returns [] if the file is absent.
    """
    if not path.is_file():
        return []
    partitions: list[str] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("add ") and not line.startswith("add_group"):
            tokens = line.split()
            if len(tokens) >= 2:
                partitions.append(tokens[1])
    return partitions


# ── Conversion helpers ─────────────────────────────────────────────────────────

def _decompress_brotli(br_path: Path, out_path: Path, tool: dict[str, Any]) -> None:
    if not tool["available"]:
        raise RuntimeError(tool["error"])
    if tool["method"] == "module":
        import brotli  # type: ignore
        out_path.write_bytes(brotli.decompress(br_path.read_bytes()))
    else:
        subprocess.run(
            ["brotli", "--decompress", "--output", str(out_path), str(br_path)],
            check=True,
        )


def _run_sdat2img(
    transfer: Path, new_dat: Path, out_img: Path, tool: dict[str, Any]
) -> None:
    if not tool["available"]:
        raise RuntimeError(tool["error"])
    if tool["method"] == "mezo_core":
        third_party = Path("third_party/mezo_core").resolve()
        probe = str(third_party)
        if probe not in sys.path:
            sys.path.insert(0, probe)
        from src.core.utils import Sdat2img  # type: ignore
        Sdat2img(str(transfer), str(new_dat), str(out_img))
    else:
        subprocess.run(
            ["sdat2img", str(transfer), str(new_dat), str(out_img)],
            check=True,
        )


# ── Report writers ─────────────────────────────────────────────────────────────

def _build_report_data(
    source_dir: Path,
    brotli_info: dict[str, Any],
    sdat2img_info: dict[str, Any],
    op_list_path: Path | None,
    op_list_parts: list[str],
    detected_names: list[str],
    partition_records: list[dict[str, Any]],
    converted_count: int,
    skipped_count: int,
    failed_count: int,
) -> dict[str, Any]:
    def _tool_label(info: dict[str, Any]) -> str:
        return f"{info['method']} ({info['detail']})" if info["available"] else "missing"

    return {
        "source_dir": str(source_dir),
        "brotli_tool": _tool_label(brotli_info),
        "sdat2img_tool": _tool_label(sdat2img_info),
        "op_list_path": str(op_list_path) if op_list_path else None,
        "op_list_partitions": op_list_parts,
        "detected_partitions": detected_names,
        "partitions": partition_records,
        "converted_count": converted_count,
        "skipped_count": skipped_count,
        "failed_count": failed_count,
    }


def _write_reports(ws: Workspace, report_data: dict[str, Any]) -> tuple[Path, Path]:
    txt_path = ws.reports / "new_dat_adapter_report.txt"
    json_path = ws.meta / "new_dat_adapter.json"
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    entries: list[dict[str, Any]] = report_data.get("partitions", [])
    lines = [
        "DeadZone new_dat Adapter Report",
        "================================",
        f"source_dir       : {report_data.get('source_dir', '(unknown)')}",
        f"brotli_tool      : {report_data.get('brotli_tool', '(unknown)')}",
        f"sdat2img_tool    : {report_data.get('sdat2img_tool', '(unknown)')}",
        f"op_list_path     : {report_data.get('op_list_path') or '(not found)'}",
        f"op_list_parts    : {', '.join(report_data.get('op_list_partitions', [])) or '(none)'}",
        f"detected_parts   : {', '.join(report_data.get('detected_partitions', [])) or '(none)'}",
        "",
        "partition results:",
    ]
    for e in entries:
        size_line = (
            f"      out_size     : {e['out_size_bytes']} bytes"
            if e["out_size_bytes"] is not None
            else "      out_size     : (n/a)"
        )
        lines += [
            f"  [{e['status']}] {e['partition']}",
            f"      br_path      : {e['br_path']}",
            f"      transfer     : {e['transfer_path'] or '(missing)'}",
            f"      tmp_new_dat  : {e['tmp_new_dat'] or '(n/a)'}",
            f"      out_img      : {e['out_img'] or '(n/a)'}",
            size_line,
            f"      reason       : {e['reason'] or '(none)'}",
        ]
    lines += [
        "",
        f"converted : {report_data.get('converted_count', 0)}",
        f"skipped   : {report_data.get('skipped_count', 0)}",
        f"failed    : {report_data.get('failed_count', 0)}",
        "",
    ]
    txt_path.write_text("\n".join(lines), encoding="utf-8")
    write_json(json_path, report_data)
    return txt_path, json_path


# ── Main adapter ───────────────────────────────────────────────────────────────

def adapt(source_dir: Path, ws: Workspace) -> dict[str, Any]:
    """Convert all *.new.dat.br files in *source_dir* to partition images.

    Improvements over the original:
    - Resolves brotli and sdat2img tools explicitly with actionable error messages.
    - Parses dynamic_partitions_op_list if present; reports skipped optional parts.
    - Decompresses into ws.partitions/_new_dat_tmp — never touches the source ROM.
    - Writes ws.reports/new_dat_adapter_report.txt and ws.meta/new_dat_adapter.json.
    - Crashes only on: found .br with no transfer.list, or conversion failure.
    - Optional partitions absent from the ROM folder are silently skipped.

    Raises RuntimeError with a descriptive message on hard failures.
    Returns {"adapter", "images", "report_path", "meta_path"}.
    """
    source_dir = Path(source_dir)
    brotli_info = resolve_brotli_tool()
    sdat2img_info = resolve_sdat2img_tool()

    tmp_dir = ws.partitions / "_new_dat_tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    ws.images.mkdir(parents=True, exist_ok=True)

    op_list_candidates = list(source_dir.rglob("dynamic_partitions_op_list"))
    op_list_path: Path | None = op_list_candidates[0] if op_list_candidates else None
    op_list_parts = parse_dynamic_partitions_op_list(op_list_path) if op_list_path else []

    detected = detect_new_dat_partitions(source_dir)
    detected_names = [p for p, _, _ in detected]

    if not detected:
        raise RuntimeError(
            f"no *.new.dat.br files found under {source_dir}. "
            "Expected an Android new-dat ROM folder."
        )

    if not brotli_info["available"]:
        raise RuntimeError(brotli_info["error"])
    if not sdat2img_info["available"]:
        raise RuntimeError(sdat2img_info["error"])

    partition_records: list[dict[str, Any]] = []
    converted_images: list[str] = []
    converted_count = skipped_count = failed_count = 0

    for part, br_path, transfer_path in detected:
        record: dict[str, Any] = {
            "partition": part,
            "br_path": str(br_path),
            "transfer_path": str(transfer_path) if transfer_path else None,
            "tmp_new_dat": None,
            "out_img": None,
            "out_size_bytes": None,
            "status": "PENDING",
            "reason": "",
        }

        if transfer_path is None:
            record["status"] = "FAILED"
            record["reason"] = f"missing transfer.list for {br_path.name}"
            failed_count += 1
            partition_records.append(record)
            _write_reports(ws, _build_report_data(
                source_dir, brotli_info, sdat2img_info,
                op_list_path, op_list_parts, detected_names,
                partition_records, converted_count, skipped_count, failed_count,
            ))
            raise RuntimeError(
                f"missing transfer list for {br_path.name}. "
                "Every *.new.dat.br must have a matching *.transfer.list in the same directory."
            )

        tmp_new_dat = tmp_dir / f"{part}.new.dat"
        out_img = ws.images / f"{part}.img"
        record["tmp_new_dat"] = str(tmp_new_dat)
        record["out_img"] = str(out_img)

        try:
            _decompress_brotli(br_path, tmp_new_dat, brotli_info)
            _run_sdat2img(transfer_path, tmp_new_dat, out_img, sdat2img_info)
            record["out_size_bytes"] = out_img.stat().st_size if out_img.is_file() else 0
            record["status"] = "CONVERTED"
            converted_images.append(out_img.name)
            converted_count += 1
        except Exception as exc:
            record["status"] = "FAILED"
            record["reason"] = str(exc)
            failed_count += 1
            partition_records.append(record)
            _write_reports(ws, _build_report_data(
                source_dir, brotli_info, sdat2img_info,
                op_list_path, op_list_parts, detected_names,
                partition_records, converted_count, skipped_count, failed_count,
            ))
            raise RuntimeError(f"conversion failed for partition '{part}': {exc}") from exc

        partition_records.append(record)

    br_names = {p for p, _, _ in detected}
    for op_part in op_list_parts:
        if op_part not in br_names:
            partition_records.append({
                "partition": op_part,
                "br_path": "(not found)",
                "transfer_path": None,
                "tmp_new_dat": None,
                "out_img": None,
                "out_size_bytes": None,
                "status": "SKIPPED",
                "reason": "listed in op_list but no .new.dat.br found — optional partition absent",
            })
            skipped_count += 1

    report_data = _build_report_data(
        source_dir, brotli_info, sdat2img_info,
        op_list_path, op_list_parts, detected_names,
        partition_records, converted_count, skipped_count, failed_count,
    )
    txt_path, json_path = _write_reports(ws, report_data)

    return {
        "adapter": "new_dat",
        "images": converted_images,
        "report_path": str(txt_path),
        "meta_path": str(json_path),
    }
