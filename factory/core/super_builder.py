from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from factory.core.detector import DYNAMIC_PARTITIONS, RomInfo
from factory.core.size_policy import SizePolicyError, apply_super_policy, collect_size_policy, load_policy, write_size_policy_report
from factory.core.super_profile import build_super_profile, resolve_image_sources
from factory.core.toolchain import MISSING_LPMAKE_MESSAGE, resolve_toolchain
from factory.core.workspace import Workspace, read_json, write_json

DYNAMIC_IMAGES = {f"{name}.img" for name in DYNAMIC_PARTITIONS}


class PreSuperValidationError(RuntimeError):
    def __init__(self, payload: dict[str, Any]):
        self.payload = payload
        super().__init__(str(payload.get("cause") or payload.get("error_type") or "pre-super validation failed"))


def _metadata_path(ws: Workspace, name: str) -> Path:
    return ws.meta / name


def _load_required_metadata(ws: Workspace) -> dict[str, dict[str, Any]]:
    names = ["rom_info.json", "device_info.json", "super_layout.json", "partition_map.json"]
    missing = [name for name in names if not _metadata_path(ws, name).is_file()]
    if missing:
        raise RuntimeError(f"required super metadata is missing: {', '.join(missing)}")
    return {name: read_json(_metadata_path(ws, name), {}) for name in names}


def _int_value(*values: Any) -> int:
    for value in values:
        try:
            parsed = int(value)
        except (TypeError, ValueError):
            continue
        if parsed > 0:
            return parsed
    return 0


def _is_sparse_image(path: Path) -> bool:
    if not path.is_file() or path.stat().st_size < 4:
        return False
    with path.open("rb") as fh:
        return fh.read(4) == b"\x3a\xff\x26\xed"


def _ensure_sparse_super(super_img: Path, img2simg: Path | None, warnings: list[str]) -> bool:
    if _is_sparse_image(super_img):
        return True
    if img2simg is None:
        warnings.append("super.img is raw and img2simg is unavailable; final ZIP may exceed size policy")
        return False
    sparse_tmp = super_img.with_suffix(".sparse.tmp")
    proc = subprocess.run(
        [str(img2simg), str(super_img), str(sparse_tmp)],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if proc.returncode != 0 or not sparse_tmp.is_file():
        warnings.append(f"img2simg could not convert raw super.img to sparse; code={proc.returncode}")
        if sparse_tmp.exists():
            sparse_tmp.unlink()
        return False
    sparse_tmp.replace(super_img)
    return _is_sparse_image(super_img)


def _allocation(part: str, image: Path, layout: dict[str, Any], warnings: list[str]) -> int:
    partitions = layout.get("partitions") if isinstance(layout.get("partitions"), dict) else {}
    entry = partitions.get(part) if isinstance(partitions.get(part), dict) else {}
    original_size = _int_value(entry.get("allocation_size"))
    if original_size:
        image_size = image.stat().st_size
        if image_size > original_size:
            raise RuntimeError(f"{part}.img is larger than metadata allocation")
        print(f"[SUPER] Allocation: {part}={original_size} source={entry.get('source')}")
        return original_size
    raise RuntimeError(
        f"allocation metadata not found for {part}.img — "
        "check super_image_input_report.txt and super_profile_report.txt for details"
    )


def _allowed_partition_sizes(layout: dict[str, Any]) -> dict[str, int]:
    result: dict[str, int] = {}
    partitions = layout.get("partitions") if isinstance(layout.get("partitions"), dict) else {}
    for part, entry in partitions.items():
        if isinstance(entry, dict):
            size = _int_value(entry.get("allocation_size"), entry.get("size"), entry.get("partition_size"))
            if size:
                result[str(part)] = size
    for source_key in ("partition_sizes", "allowed_partition_sizes"):
        source = layout.get(source_key)
        if isinstance(source, dict):
            for part, value in source.items():
                size = _int_value(value)
                if size and str(part) not in result:
                    result[str(part)] = size
    return result


def _error_payload(error_type: str, cause: str) -> dict[str, str]:
    if error_type == "SUPER_GROUP_SIZE_EXCEEDED":
        return {
            "error_type": error_type,
            "cause": cause,
            "suggested_fix": "Reduce image sizes or fix EROFS rebuild compression before lpmake",
            "suggested_check": "Check stable_partition_rebuild_report.json and super_profile_report.txt",
        }
    return {
        "error_type": "REBUILT_IMAGE_TOO_LARGE",
        "cause": cause,
        "suggested_fix": "Rebuild EROFS with compression/options matching original, reduce more content, or do not rebuild this partition",
        "suggested_check": "Check stable_partition_rebuild_report.json and super_profile_report.txt",
    }


def _write_super_image_input_report(
    ws: Workspace,
    layout: dict[str, Any],
    dynamic_images: dict[str, Path],
    image_sources: dict[str, str],
    missing_images: list[str],
    lpmake_args: list[str],
    payload_reextraction_skipped: bool,
) -> None:
    codename = (layout.get("device") or {}).get("codename") or "unknown"
    data: dict[str, Any] = {
        "codename": codename,
        "super_config_source": layout.get("superconfig_source") or layout.get("metadata_source"),
        "super_size": layout.get("target_super_size"),
        "group_name": layout.get("dynamic_group_name"),
        "slot_mode": layout.get("slot_mode"),
        "partitions": [],
        "missing_images": missing_images,
        "lpmake_args": lpmake_args,
        "payload_reextraction_skipped": payload_reextraction_skipped,
        "status": "missing_images" if missing_images else "ok",
    }
    for part in layout.get("selected_partitions") or []:
        img = dynamic_images.get(part)
        data["partitions"].append({
            "name": part,
            "image_path": str(img) if img else None,
            "image_source": image_sources.get(part, "missing"),
            "size": img.stat().st_size if img and img.is_file() else 0,
        })
    ws.reports.mkdir(parents=True, exist_ok=True)
    write_json(ws.reports / "super_image_input_report.json", data)
    lines = [
        "DeadZone Super Image Input Report",
        "==================================",
        f"codename               : {codename}",
        f"super_config_source    : {data['super_config_source']}",
        f"super_size             : {data['super_size']}",
        f"group_name             : {data['group_name']}",
        f"slot_mode              : {data['slot_mode']}",
        f"payload_reextraction_skipped: {payload_reextraction_skipped}",
        f"status                 : {data['status']}",
        "",
        "partition images:",
    ]
    for entry in data["partitions"]:
        lines.append(
            f"  {entry['name']}: path={entry['image_path'] or '(missing)'} "
            f"source={entry['image_source']} size={entry['size']}"
        )
    if missing_images:
        lines += ["", "missing images:"]
        lines.extend(f"  - {name}" for name in missing_images)
    if lpmake_args:
        lines += ["", "lpmake command:"]
        lines.append("  " + " ".join(str(a) for a in lpmake_args))
    lines.append("")
    (ws.reports / "super_image_input_report.txt").write_text("\n".join(lines), encoding="utf-8")


def _check_super_image_inputs(
    ws: Workspace,
    layout: dict[str, Any],
    dynamic_images: dict[str, Path],
) -> tuple[dict[str, str], list[str]]:
    """Check that all selected partitions have usable images. Returns (sources, missing)."""
    image_sources = dict(layout.get("image_sources") or {})
    if not image_sources:
        image_sources = resolve_image_sources(ws, dynamic_images)
    selected: list[str] = list(layout.get("selected_partitions") or dynamic_images.keys())
    missing: list[str] = []
    for part in selected:
        img = dynamic_images.get(part)
        if not img or not img.is_file() or img.stat().st_size == 0:
            missing.append(part)
            image_sources[part] = "missing"
    return image_sources, missing


def validate_pre_super_images(ws: Workspace, layout: dict[str, Any] | None = None) -> dict[str, Any]:
    profile = layout or read_json(ws.meta / "super_profile.json", {}) or read_json(ws.meta / "super_layout.json", {})
    dynamic_images = {name: Path(path) for name, path in (profile.get("dynamic_images") or {}).items()}
    selected = list(profile.get("selected_partitions") or dynamic_images.keys())
    allowed = _allowed_partition_sizes(profile)
    rebuild_report = read_json(ws.reports / "stable_partition_rebuild_report.json", {})
    original_sizes: dict[str, int] = {}
    for entry in rebuild_report.get("partitions") or []:
        if isinstance(entry, dict) and entry.get("partition"):
            original_sizes[str(entry["partition"])] = _int_value(entry.get("original_size"), entry.get("size_before"))
    image_sizes: dict[str, int] = {}
    errors: list[dict[str, str]] = []
    group_usage = 0
    for part in selected:
        image = dynamic_images.get(part) or ws.images / f"{part}.img"
        size = image.stat().st_size if image.is_file() else 0
        image_sizes[str(part)] = size
        limit = allowed.get(str(part), 0)
        if limit:
            group_usage += max(size, limit)
            if size > limit:
                before = original_sizes.get(str(part), 0)
                if before:
                    cause = f"{part}.img grew from {before} to {size} and exceeds allowed partition/group size"
                else:
                    cause = f"{part}.img size {size} exceeds allowed partition size {limit}"
                errors.append(_error_payload("REBUILT_IMAGE_TOO_LARGE", cause))
        else:
            group_usage += size
    group_limit = _int_value(profile.get("group_size"))
    if group_limit and group_usage > group_limit:
        errors.append(
            _error_payload(
                "SUPER_GROUP_SIZE_EXCEEDED",
                f"Rebuilt dynamic partition images exceed qti_dynamic_partitions group size ({group_usage} > {group_limit})",
            )
        )
    data = {
        "stage": "pre_super_image_validation",
        "image_sizes": image_sizes,
        "allowed_partition_sizes": allowed,
        "group_usage": group_usage,
        "group_limit": group_limit,
        "status": "failed" if errors else "ok",
        "errors": errors,
    }
    write_json(ws.reports / "pre_super_image_validation_report.json", data)
    lines = [
        "DeadZone Pre-Super Image Validation Report",
        "==========================================",
        f"status: {data['status']}",
        f"group_usage: {group_usage}",
        f"group_limit: {group_limit}",
        "",
        "images:",
    ]
    for part, size in image_sizes.items():
        lines.append(f"  - {part}.img: size={size} allowed={allowed.get(part, 0)}")
    if errors:
        lines += ["", "errors:"]
        lines.extend(f"  - {err['error_type']}: {err['cause']}" for err in errors)
    (ws.reports / "pre_super_image_validation_report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    if errors:
        raise PreSuperValidationError(errors[0])
    return data


def _build_lpmake_command(
    output_super: Path,
    layout: dict[str, Any],
    dynamic_images: dict[str, Path],
    lpmake: Path,
    warnings: list[str],
) -> list[str]:
    target_size = int(layout["target_super_size"])
    if target_size <= 0:
        raise RuntimeError("target super size is missing or invalid")
    group_size = int(layout["group_size"])
    if group_size <= 0 or group_size >= target_size:
        raise RuntimeError("dynamic group size is missing or exceeds target super size")

    command = [
        str(lpmake),
        "--metadata-size", str(layout["metadata_size"]),
        "--super-name", str(layout["block_device_name"]),
        "--metadata-slots", str(layout["metadata_slots"]),
        "--device", f"{layout['block_device_name']}:{target_size}",
    ]
    if layout.get("output_format") == "sparse":
        command.append("--sparse")

    selected = list(layout["selected_partitions"])
    if not selected:
        raise RuntimeError("no dynamic partition images are available to build super.img")

    if layout["virtual_ab"]:
        command += ["--group", f"{layout['group_a_name']}:{group_size}"]
        for part in selected:
            image = dynamic_images[part]
            alloc = _allocation(part, image, layout, warnings)
            command += ["--partition", f"{part}_a:readonly:{alloc}:{layout['group_a_name']}"]
            command += ["--image", f"{part}_a={image}"]
        command += ["--group", f"{layout['group_b_name']}:{group_size}"]
        for part in selected:
            command += ["--partition", f"{part}_b:readonly:0:{layout['group_b_name']}"]
            print(f"[SUPER] VAB zero_b: {part}_b=0")
        command.append("--virtual-ab")
    else:
        command += ["--group", f"{layout['group_a_name']}:{group_size}"]
        for part in selected:
            image = dynamic_images[part]
            alloc = _allocation(part, image, layout, warnings)
            command += ["--partition", f"{part}:readonly:{alloc}:{layout['group_a_name']}"]
            command += ["--image", f"{part}={image}"]

    command += ["--out", str(output_super)]
    return command


def _validate_with_lpdump(super_img: Path, lpdump: Path | None) -> dict[str, Any]:
    if lpdump is None:
        return {"status": "SKIPPED", "reason": "lpdump not available from toolchain", "output": ""}
    if not super_img.is_file():
        return {"status": "FAILED", "reason": f"super.img not found: {super_img}", "output": ""}
    proc = subprocess.run(
        [str(lpdump), str(super_img)],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return {
        "status": "PASSED" if proc.returncode == 0 else "FAILED",
        "reason": "lpdump completed" if proc.returncode == 0 else f"lpdump exited with code {proc.returncode}",
        "output": proc.stdout,
    }


def _write_report(
    ws: Workspace,
    result: dict[str, Any],
    layout: dict[str, Any],
    validation: dict[str, Any],
) -> None:
    command = result.get("lpmake_command") or []
    lines = [
        "DeadZone Super Build Report",
        "===========================",
        f"action: {result.get('action')}",
        f"reason: {result.get('reason')}",
        f"input metadata source: {layout.get('metadata_source')}",
        f"allocation metadata source: {layout.get('allocation_metadata_source')}",
        f"target super size: {layout.get('target_super_size')}",
        f"requested super target bytes: {layout.get('requested_super_target_bytes')}",
        f"selected super size bytes: {layout.get('selected_super_size_bytes')}",
        f"selected super size source: {layout.get('selected_super_size_source')}",
        f"stock super size bytes: {layout.get('stock_super_size_bytes')}",
        f"super policy mode: {layout.get('super_size_policy')}",
        f"super policy reason: {layout.get('super_size_policy_reason')}",
        f"final ZIP max bytes: {layout.get('final_zip_max_bytes')}",
        f"stock super size: {layout.get('stock_super_size')}",
        f"group name: {layout.get('dynamic_group_name')}",
        f"group size: {layout.get('group_size')}",
        f"dynamic allocation total: {layout.get('dynamic_allocation_total')}",
        f"actual images total: {layout.get('actual_images_total')}",
        f"output format: {layout.get('output_format')}",
        f"actual super.img size: {result.get('super_size')}",
        f"super.img sparse: {result.get('super_is_sparse')}",
        f"slot mode: {layout.get('slot_mode')}",
        "",
        "partition list:",
    ]
    for part in layout.get("selected_partitions", []):
        image = layout.get("dynamic_images", {}).get(part, "")
        entry = (layout.get("partitions") or {}).get(part, {})
        size = entry.get("allocation_size")
        source = entry.get("source", "unresolved")
        lines.append(f"  - {part}: image={image} allocation={size} source={source}")
    lines += ["", "_b zero-size entries for VAB:"]
    if layout.get("virtual_ab"):
        for entry in layout.get("vab_zero_b_partitions", []):
            lines.append(f"  - {entry.get('name')}: {entry.get('allocation_size')} group={entry.get('group_name')}")
    else:
        lines.append("  (not VAB)")
    lines += [
        "",
        f"toolchain report: {result.get('toolchain_report') or '(none)'}",
        "",
        "lpmake command:",
        f"  {' '.join(str(token) for token in command)}" if command else "  (none)",
        "",
        f"validation status: {validation.get('status')}",
        f"validation reason: {validation.get('reason')}",
    ]
    if validation.get("output"):
        lines += ["", "lpdump output:"]
        lines.extend(f"  {line}" for line in str(validation["output"]).splitlines())
    warnings = result.get("warnings") or []
    errors = result.get("errors") or []
    lines += ["", "warnings:"]
    lines.extend([f"  - {warning}" for warning in warnings] or ["  (none)"])
    lines += ["", "errors:"]
    lines.extend([f"  - {error}" for error in errors] or ["  (none)"])
    lines.append("")
    (ws.reports / "super_build_report.txt").write_text("\n".join(lines), encoding="utf-8")


def _write_error_summary(ws: Workspace, stage: str, message: str, layout: dict[str, Any] | None = None) -> None:
    title = "Super metadata allocation missing" if "no metadata allocation" in message.lower() else "Super image build failed"
    lines = [
        "DeadZone Error Summary",
        "======================",
        f"stage: {stage}",
        f"title: {title}",
        f"error: {message}",
    ]
    if layout:
        missing = layout.get("missing_metadata") or []
        lines += [
            f"metadata source: {layout.get('metadata_source')}",
            f"safe sources checked: {', '.join(layout.get('metadata_priority') or [])}",
            f"missing metadata: {', '.join(missing) if missing else '(none)'}",
        ]
    lines.append("")
    (ws.reports / "error_summary.txt").write_text("\n".join(lines), encoding="utf-8")


def build_super_image(ws: Workspace, info: RomInfo | None = None, inspection: dict[str, Any] | None = None) -> dict[str, Any]:
    metadata = _load_required_metadata(ws)
    rom_info = metadata["rom_info.json"]
    super_layout = metadata["super_layout.json"]
    layout = build_super_profile(ws, info, inspection)
    policy = load_policy(ws)
    try:
        layout = apply_super_policy(layout, policy)
    except SizePolicyError as exc:
        message = str(exc)
        write_json(ws.meta / "super_layout.json", {**super_layout, **layout})
        policy_data = collect_size_policy(ws, status="FAILED", reason=message)
        write_size_policy_report(ws, policy_data)
        _write_error_summary(ws, "super", message, layout)
        raise RuntimeError(message) from exc
    print(f"[SIZE] Super display target: {layout.get('requested_super_target_bytes')}")
    print(f"[SIZE] Stock-safe super: {layout.get('stock_super_size_bytes')}")
    print(f"[SIZE] Selected super: {layout.get('selected_super_size_bytes')}")
    print(f"[SIZE] Super policy: {layout.get('super_size_policy')}")
    print(f"[SIZE] Final ZIP max: {policy.get('final_zip_max_bytes')}")
    write_json(ws.meta / "super_profile.json", layout)
    dynamic_images = {name: Path(path) for name, path in layout.get("dynamic_images", {}).items()}
    image_sources, missing_images = _check_super_image_inputs(ws, layout, dynamic_images)
    payload_reextraction_skipped = bool(layout.get("payload_reextraction_skipped", True))
    _write_super_image_input_report(
        ws, layout, dynamic_images, image_sources,
        missing_images=[], lpmake_args=[],
        payload_reextraction_skipped=payload_reextraction_skipped,
    )
    if missing_images:
        message = (
            f"SUPER_IMAGE_INPUT_MISSING: partition image missing for super build: "
            f"{', '.join(missing_images)}. "
            f"Check super_image_input_report.txt for details."
        )
        _write_super_image_input_report(
            ws, layout, dynamic_images, image_sources,
            missing_images=missing_images, lpmake_args=[],
            payload_reextraction_skipped=payload_reextraction_skipped,
        )
        _write_error_summary(ws, "super", message, layout)
        raise RuntimeError(message)
    toolchain = resolve_toolchain(ws)
    lpmake = toolchain.path("lpmake")
    lpdump = toolchain.path("lpdump")
    img2simg = toolchain.path("img2simg")
    final_super = ws.images / "super.img"
    needs_rebuild = bool(
        super_layout.get("rebuild_required")
        or super_layout.get("needs_super_rebuild")
        or rom_info.get("super_rebuild_required")
        or rom_info.get("needs_super_rebuild")
        or (inspection or {}).get("needs_super_rebuild")
    )
    reason = ""
    warnings: list[str] = []
    errors: list[str] = []
    command: list[str] = []

    if final_super.is_file() and not needs_rebuild:
        action = "preserved"
        reason = "original super.img is present and no dynamic partition rebuild was requested"
        _ensure_sparse_super(final_super, img2simg, warnings)
        validation = _validate_with_lpdump(final_super, lpdump)
    elif final_super.is_file() and not dynamic_images:
        action = "preserved"
        reason = "super.img is present and no replacement dynamic partition images are available"
        _ensure_sparse_super(final_super, img2simg, warnings)
        validation = _validate_with_lpdump(final_super, lpdump)
    else:
        action = "rebuilt"
        if not dynamic_images:
            raise RuntimeError("cannot rebuild super.img because no dynamic partition images are available")
        if lpmake is None:
            message = f"{MISSING_LPMAKE_MESSAGE} Toolchain report: {toolchain.report_path}"
            result = {
                "status": "FAILED",
                "action": "failed",
                "reason": message,
                "super_img": str(final_super),
                "super_size": final_super.stat().st_size if final_super.is_file() else None,
                "input_metadata_source": layout.get("metadata_source"),
                "allocation_metadata_source": layout.get("allocation_metadata_source"),
                "target_super_size": layout.get("target_super_size"),
                "selected_super_size_bytes": layout.get("selected_super_size_bytes"),
                "selected_super_size_source": layout.get("selected_super_size_source"),
                "stock_super_size_bytes": layout.get("stock_super_size_bytes"),
                "super_size_policy": layout.get("super_size_policy"),
                "super_size_policy_reason": layout.get("super_size_policy_reason"),
                "final_zip_max_bytes": layout.get("final_zip_max_bytes"),
                "group_name": layout.get("dynamic_group_name"),
                "group_size": layout.get("group_size"),
                "slot_mode": layout.get("slot_mode"),
                "partition_list": layout.get("selected_partitions"),
                "vab_zero_size_b_partitions": [f"{p}_b" for p in layout.get("selected_partitions", [])] if layout.get("virtual_ab") else [],
                "lpmake_command": command,
                "tools": {name: str(status.path) if status.path else None for name, status in toolchain.tools.items()},
                "toolchain_report": str(toolchain.report_path),
                "validation": {"status": "FAILED", "reason": MISSING_LPMAKE_MESSAGE, "output": ""},
                "warnings": warnings,
                "errors": [message],
            }
            write_json(ws.meta / "super_build_result.json", result)
            _write_report(ws, result, layout, result["validation"])
            _write_error_summary(ws, "super", message, layout)
            raise RuntimeError(message)
        reason = "dynamic partition content requires a new super.img"
        if not final_super.is_file():
            reason = "no original super.img is available and dynamic partition images exist"
        try:
            validate_pre_super_images(ws, layout)
        except PreSuperValidationError as exc:
            payload = exc.payload
            message = json.dumps(payload, sort_keys=True)
            result = {
                "status": "FAILED",
                "action": "failed",
                "reason": payload.get("cause"),
                "super_img": str(final_super),
                "super_size": final_super.stat().st_size if final_super.is_file() else None,
                "target_super_size": layout.get("target_super_size"),
                "group_name": layout.get("dynamic_group_name"),
                "group_size": layout.get("group_size"),
                "partition_list": layout.get("selected_partitions"),
                "lpmake_command": command,
                "validation": {"status": "FAILED", "reason": payload.get("cause"), "output": ""},
                "warnings": warnings,
                "errors": [payload],
            }
            write_json(ws.meta / "super_build_result.json", result)
            _write_report(ws, result, layout, result["validation"])
            _write_error_summary(ws, "pre_super_image_validation", message, layout)
            raise RuntimeError(message) from exc
        try:
            command = _build_lpmake_command(final_super, layout, dynamic_images, lpmake, warnings)
            _write_super_image_input_report(
                ws, layout, dynamic_images, image_sources,
                missing_images=[], lpmake_args=command,
                payload_reextraction_skipped=payload_reextraction_skipped,
            )
        except RuntimeError as exc:
            message = str(exc)
            errors.append(message)
            result = {
                "status": "FAILED",
                "action": "failed",
                "reason": message,
                "super_img": str(final_super),
                "super_size": final_super.stat().st_size if final_super.is_file() else None,
                "input_metadata_source": layout.get("metadata_source"),
                "allocation_metadata_source": layout.get("allocation_metadata_source"),
                "target_super_size": layout.get("target_super_size"),
                "selected_super_size_bytes": layout.get("selected_super_size_bytes"),
                "selected_super_size_source": layout.get("selected_super_size_source"),
                "stock_super_size_bytes": layout.get("stock_super_size_bytes"),
                "super_size_policy": layout.get("super_size_policy"),
                "super_size_policy_reason": layout.get("super_size_policy_reason"),
                "final_zip_max_bytes": layout.get("final_zip_max_bytes"),
                "group_name": layout.get("dynamic_group_name"),
                "group_size": layout.get("group_size"),
                "slot_mode": layout.get("slot_mode"),
                "partition_list": layout.get("selected_partitions"),
                "vab_zero_size_b_partitions": [entry.get("name") for entry in layout.get("vab_zero_b_partitions", [])],
                "lpmake_command": command,
                "tools": {name: str(status.path) if status.path else None for name, status in toolchain.tools.items()},
                "toolchain_report": str(toolchain.report_path),
                "validation": {"status": "FAILED", "reason": message, "output": ""},
                "warnings": warnings,
                "errors": errors,
            }
            write_json(ws.meta / "super_build_result.json", result)
            _write_report(ws, result, layout, result["validation"])
            _write_error_summary(ws, "super", message, layout)
            raise
        final_super.parent.mkdir(parents=True, exist_ok=True)
        if final_super.exists():
            final_super.unlink()
        log = ws.logs / "lpmake.log"
        with log.open("w", encoding="utf-8") as fh:
            proc = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=fh, stderr=subprocess.STDOUT, text=True)
        if proc.returncode != 0 or not final_super.is_file():
            errors.append(f"lpmake failed with code {proc.returncode}; see {log}")
            validation = {"status": "FAILED", "reason": "lpmake did not produce a valid super.img", "output": ""}
        else:
            _ensure_sparse_super(final_super, img2simg, warnings)
            validation = _validate_with_lpdump(final_super, lpdump)

    super_is_sparse = _is_sparse_image(final_super)
    result = {
        "status": "FAILED" if errors or validation.get("status") == "FAILED" else "OK",
        "action": action,
        "reason": reason,
        "super_img": str(final_super),
        "super_size": final_super.stat().st_size if final_super.is_file() else None,
        "super_is_sparse": super_is_sparse,
        "super_output_format": "sparse" if super_is_sparse else "raw",
        "requested_super_target_bytes": layout.get("requested_super_target_bytes"),
        "selected_super_size_bytes": layout.get("selected_super_size_bytes"),
        "selected_super_size_source": layout.get("selected_super_size_source"),
        "stock_super_size": layout.get("stock_super_size"),
        "stock_super_size_bytes": layout.get("stock_super_size_bytes"),
        "super_size_policy": layout.get("super_size_policy"),
        "super_size_policy_reason": layout.get("super_size_policy_reason"),
        "final_zip_max_bytes": layout.get("final_zip_max_bytes"),
        "dynamic_allocation_total": layout.get("dynamic_allocation_total"),
        "actual_images_total": layout.get("actual_images_total"),
        "input_metadata_source": layout.get("metadata_source"),
        "allocation_metadata_source": layout.get("allocation_metadata_source"),
        "target_super_size": layout.get("target_super_size"),
        "group_name": layout.get("dynamic_group_name"),
        "group_size": layout.get("group_size"),
        "slot_mode": layout.get("slot_mode"),
        "partition_list": layout.get("selected_partitions"),
        "vab_zero_size_b_partitions": [f"{p}_b" for p in layout.get("selected_partitions", [])] if layout.get("virtual_ab") else [],
        "lpmake_command": command,
        "tools": {name: str(status.path) if status.path else None for name, status in toolchain.tools.items()},
        "toolchain_report": str(toolchain.report_path),
        "validation": validation,
        "warnings": warnings,
        "errors": errors,
    }
    write_json(ws.meta / "super_layout.json", {**super_layout, **layout, "lpmake_command": command, "validation": validation})
    write_json(ws.meta / "super_build_result.json", result)
    _write_report(ws, result, layout, validation)
    policy_data = collect_size_policy(ws, status=result["status"], reason="; ".join(errors))
    write_size_policy_report(ws, policy_data)
    if errors:
        _write_error_summary(ws, "super", "; ".join(errors), layout)
        raise RuntimeError("; ".join(errors))
    print(f"[SUPER] {action}")
    print(f"[SUPER] super.img size={result.get('super_size')} sparse={result.get('super_is_sparse')}")
    return result


def build_super(ws: Workspace, info: RomInfo | None = None, inspection: dict[str, Any] | None = None) -> dict[str, Any]:
    return build_super_image(ws, info, inspection)
