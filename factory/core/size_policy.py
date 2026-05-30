from __future__ import annotations

from pathlib import Path
from typing import Any

from factory.core.workspace import Workspace, read_json, write_json


DEFAULT_SUPER_TARGET_BYTES = 8_500_000_000
DEFAULT_FINAL_ZIP_MAX_BYTES = 4_500_000_000
DEFAULT_SUPER_OUTPUT_FORMAT = "sparse"
DEFAULT_FINAL_ZIP_COMPRESSION = "max"
DEFAULT_SUPER_SIZE_POLICY = "stock_safe"
SUPER_SIZE_POLICIES = ("stock_safe", "compact_if_safe", "force_decimal")
LP_METADATA_OVERHEAD = 4 * 1024 * 1024


class SizePolicyError(RuntimeError):
    pass


def bytes_from_decimal_gb(value: float | str | int, default: int) -> int:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return default
    if parsed <= 0:
        return default
    return int(parsed * 1_000_000_000)


def default_policy(
    super_target_bytes: int = DEFAULT_SUPER_TARGET_BYTES,
    final_zip_max_bytes: int = DEFAULT_FINAL_ZIP_MAX_BYTES,
    allow_oversized_final: bool = False,
    super_size_policy: str = DEFAULT_SUPER_SIZE_POLICY,
) -> dict[str, Any]:
    return {
        "super_target_bytes": int(super_target_bytes),
        "final_zip_max_bytes": int(final_zip_max_bytes),
        "super_output_format": DEFAULT_SUPER_OUTPUT_FORMAT,
        "final_zip_compression": DEFAULT_FINAL_ZIP_COMPRESSION,
        "allow_oversized_final": bool(allow_oversized_final),
        "super_size_policy": _normalize_super_size_policy(super_size_policy),
    }


def load_policy(ws: Workspace) -> dict[str, Any]:
    stored = read_json(ws.meta / "size_policy.json", {})
    policy = default_policy()
    policy.update({key: value for key, value in stored.items() if value not in (None, "")})
    policy["super_target_bytes"] = int(policy.get("super_target_bytes") or DEFAULT_SUPER_TARGET_BYTES)
    policy["final_zip_max_bytes"] = int(policy.get("final_zip_max_bytes") or DEFAULT_FINAL_ZIP_MAX_BYTES)
    policy["super_output_format"] = str(policy.get("super_output_format") or DEFAULT_SUPER_OUTPUT_FORMAT)
    policy["final_zip_compression"] = str(policy.get("final_zip_compression") or DEFAULT_FINAL_ZIP_COMPRESSION)
    policy["allow_oversized_final"] = bool(policy.get("allow_oversized_final", False))
    policy["super_size_policy"] = _normalize_super_size_policy(policy.get("super_size_policy"))
    return policy


def write_policy_config(ws: Workspace, policy: dict[str, Any]) -> None:
    current = read_json(ws.meta / "size_policy.json", {})
    current.update(default_policy())
    current.update(policy)
    write_json(ws.meta / "size_policy.json", current)


def _int_value(*values: Any) -> int:
    for value in values:
        try:
            parsed = int(value)
        except (TypeError, ValueError):
            continue
        if parsed > 0:
            return parsed
    return 0


def _normalize_super_size_policy(value: Any) -> str:
    mode = str(value or DEFAULT_SUPER_SIZE_POLICY).strip().lower()
    return mode if mode in SUPER_SIZE_POLICIES else DEFAULT_SUPER_SIZE_POLICY


def _bool_value(*values: Any) -> bool:
    for value in values:
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in {"1", "true", "yes", "on"}:
                return True
            if normalized in {"0", "false", "no", "off"}:
                return False
    return False


def dynamic_allocation_total(layout: dict[str, Any]) -> int:
    partitions = layout.get("partitions") if isinstance(layout.get("partitions"), dict) else {}
    total = 0
    for entry in partitions.values():
        if isinstance(entry, dict):
            total += _int_value(entry.get("allocation_size"))
    return total


def actual_images_total(layout: dict[str, Any]) -> int:
    partitions = layout.get("partitions") if isinstance(layout.get("partitions"), dict) else {}
    total = 0
    for entry in partitions.values():
        if isinstance(entry, dict):
            total += _int_value(entry.get("image_size"))
    if total:
        return total
    images = layout.get("dynamic_images") if isinstance(layout.get("dynamic_images"), dict) else {}
    for path_value in images.values():
        path = Path(str(path_value))
        if path.is_file():
            total += path.stat().st_size
    return total


def apply_super_policy(layout: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    requested = int(policy.get("super_target_bytes") or DEFAULT_SUPER_TARGET_BYTES)
    mode = _normalize_super_size_policy(policy.get("super_size_policy"))
    stock_size = _int_value(layout.get("target_super_size"), layout.get("super_size"))
    stock_size = stock_size or requested
    allocation = dynamic_allocation_total(layout)
    compact_allowed = _bool_value(
        layout.get("allow_super_compaction"),
        layout.get("allow_compact_super"),
        layout.get("compact_super_safe"),
    )
    compact_group_limit = max(1, requested - LP_METADATA_OVERHEAD)
    compact_fits = allocation <= requested and allocation <= compact_group_limit

    if mode == "force_decimal":
        if stock_size > requested:
            raise SizePolicyError(f"Device stock super requires {stock_size} bytes, requested target is {requested} bytes.")
        selected = requested
        selected_source = "force_decimal"
        selection_reason = "force_decimal selected requested display target because stock metadata does not require a larger device"
    elif mode == "compact_if_safe" and stock_size > requested and compact_allowed and compact_fits:
        selected = requested
        selected_source = "compact_if_safe"
        selection_reason = "compact_if_safe selected requested display target because allocation fits and profile allows compacting"
    elif mode == "compact_if_safe" and stock_size <= requested:
        selected = requested
        selected_source = "requested_decimal"
        selection_reason = "compact_if_safe selected requested display target because stock metadata fits within it"
    elif mode == "compact_if_safe":
        selected = stock_size
        selected_source = "stock_safe"
        selection_reason = "compact_if_safe selected stock-safe size because profile does not allow safe compacting or allocation does not fit"
    else:
        selected = max(requested, stock_size)
        selected_source = "stock_safe" if stock_size > requested else "requested_decimal"
        if stock_size > requested:
            selection_reason = "stock_safe selected device stock metadata size because it is larger than the requested display target"
        else:
            selection_reason = "stock_safe selected requested display target because stock metadata fits within it"

    if allocation > selected:
        raise SizePolicyError(f"Cannot build selected super because dynamic partition allocation requires {allocation} bytes.")
    group_limit = max(1, selected - LP_METADATA_OVERHEAD)
    if allocation > group_limit:
        raise SizePolicyError(f"Cannot build selected super because dynamic partition allocation requires {allocation} bytes.")

    updated = dict(layout)
    updated["requested_super_target_bytes"] = requested
    updated["stock_super_size"] = stock_size
    updated["stock_super_size_bytes"] = stock_size
    updated["selected_super_size_bytes"] = selected
    updated["selected_super_size_source"] = selected_source
    updated["super_size_policy"] = mode
    updated["super_size_policy_reason"] = selection_reason
    updated["final_zip_max_bytes"] = int(policy.get("final_zip_max_bytes") or DEFAULT_FINAL_ZIP_MAX_BYTES)
    updated["target_super_size"] = selected
    updated["super_size"] = selected
    updated["output_format"] = DEFAULT_SUPER_OUTPUT_FORMAT
    updated["super_output_format"] = DEFAULT_SUPER_OUTPUT_FORMAT
    updated["dynamic_allocation_total"] = allocation
    updated["actual_images_total"] = actual_images_total(layout)
    current_group = _int_value(layout.get("group_size"))
    updated["group_size"] = min(current_group, group_limit) if current_group else group_limit
    if updated["group_size"] < allocation:
        updated["group_size"] = group_limit
    return updated


def _zip_totals(zip_path: Path | None) -> tuple[int, int, float]:
    if not zip_path or not zip_path.is_file():
        return 0, 0, 0.0
    import zipfile

    compressed = zip_path.stat().st_size
    with zipfile.ZipFile(zip_path) as zf:
        uncompressed = sum(item.file_size for item in zf.infolist())
    ratio = (compressed / uncompressed) if uncompressed else 0.0
    return compressed, uncompressed, ratio


def collect_size_policy(
    ws: Workspace,
    final_zip: Path | None = None,
    status: str = "PENDING",
    reason: str = "",
) -> dict[str, Any]:
    policy = load_policy(ws)
    super_layout = read_json(ws.meta / "super_layout.json", {})
    super_result = read_json(ws.meta / "super_build_result.json", {})
    final_meta = read_json(ws.meta / "final_zip.json", {})
    if final_zip is None and final_meta.get("zip"):
        final_zip = Path(str(final_meta["zip"]))

    final_size, final_uncompressed, ratio = _zip_totals(final_zip)
    requested = int(policy["super_target_bytes"])
    max_allowed = int(policy["final_zip_max_bytes"])
    allocation = _int_value(super_layout.get("dynamic_allocation_total"), dynamic_allocation_total(super_layout))
    images_total = _int_value(super_layout.get("actual_images_total"), actual_images_total(super_layout))
    sparse_size = _int_value(super_result.get("super_size"))
    selected_super_size = _int_value(super_layout.get("selected_super_size_bytes"), super_layout.get("target_super_size"))
    stock_super_size = _int_value(super_layout.get("stock_super_size_bytes"), super_layout.get("stock_super_size"), super_layout.get("target_super_size"))
    passed = final_size <= max_allowed if final_size else False
    if status == "FAILED":
        passed = False
    recommendation = "Enable size-reduction/debloat style to reach 4.5GB" if not passed else "Current package meets the 4.5GB policy"
    if not reason and final_size and not passed:
        reason = f"Final ZIP is {final_size} bytes, max allowed is {max_allowed} bytes"

    return {
        **policy,
        "requested_super_target_bytes": requested,
        "selected_super_size_bytes": selected_super_size,
        "selected_super_size_source": super_layout.get("selected_super_size_source") or "",
        "stock_super_size_bytes": stock_super_size,
        "super_size_policy": _normalize_super_size_policy(policy.get("super_size_policy")),
        "super_size_policy_reason": super_layout.get("super_size_policy_reason") or "",
        "actual_super_device_size": stock_super_size,
        "group_size": _int_value(super_layout.get("group_size")),
        "dynamic_allocation_total": allocation,
        "actual_images_total": images_total,
        "estimated_minimum_possible_final_zip_size": final_size or images_total,
        "sparse_super_size": sparse_size,
        "super_is_sparse": bool(super_result.get("super_is_sparse")),
        "final_zip": str(final_zip) if final_zip else "",
        "final_zip_size": final_size,
        "final_zip_uncompressed_size": final_uncompressed,
        "final_zip_max_bytes": max_allowed,
        "final_zip_max_allowed": max_allowed,
        "compression_ratio": ratio,
        "pass": passed,
        "status": "PASSED" if passed else status,
        "reason": reason,
        "pass_fail_reason": reason or ("Final ZIP passes 4.5GB policy" if passed else "Final ZIP has not been generated yet"),
        "recommendation": recommendation,
    }


def write_size_policy_report(ws: Workspace, data: dict[str, Any]) -> None:
    write_json(ws.meta / "size_policy.json", data)
    lines = [
        "DeadZone Size Policy Report",
        "===========================",
        f"requested super target bytes: {data.get('requested_super_target_bytes')}",
        f"selected super size bytes: {data.get('selected_super_size_bytes')}",
        f"selected super size source: {data.get('selected_super_size_source')}",
        f"stock super size bytes: {data.get('stock_super_size_bytes')}",
        f"super policy mode: {data.get('super_size_policy')}",
        f"super policy reason: {data.get('super_size_policy_reason') or '(none)'}",
        f"actual super device size: {data.get('actual_super_device_size')}",
        f"group size: {data.get('group_size')}",
        f"dynamic allocation total: {data.get('dynamic_allocation_total')}",
        f"actual images total: {data.get('actual_images_total')}",
        f"estimated minimum possible final ZIP size: {data.get('estimated_minimum_possible_final_zip_size')}",
        f"sparse super size: {data.get('sparse_super_size')}",
        f"super is sparse: {data.get('super_is_sparse')}",
        f"final ZIP size: {data.get('final_zip_size')}",
        f"final ZIP max bytes: {data.get('final_zip_max_bytes')}",
        f"final ZIP max allowed: {data.get('final_zip_max_allowed')}",
        f"compression ratio: {float(data.get('compression_ratio') or 0.0):.6f}",
        f"pass/fail: {'PASS' if data.get('pass') else 'FAIL'}",
        f"reason: {data.get('reason') or '(none)'}",
        f"pass/fail reason: {data.get('pass_fail_reason') or '(none)'}",
        f"recommendation: {data.get('recommendation')}",
        "",
    ]
    ws.reports.mkdir(parents=True, exist_ok=True)
    (ws.reports / "size_policy_report.txt").write_text("\n".join(lines), encoding="utf-8")


def enforce_final_zip_policy(ws: Workspace, final_zip: Path, allow_oversized_final: bool | None = None) -> dict[str, Any]:
    policy = load_policy(ws)
    if allow_oversized_final is not None:
        policy["allow_oversized_final"] = bool(allow_oversized_final)
    final_size = final_zip.stat().st_size if final_zip.is_file() else 0
    max_allowed = int(policy["final_zip_max_bytes"])
    passed = final_size <= max_allowed
    reason = ""
    status = "PASSED"
    if not passed:
        reason = f"Final ZIP is {final_size} bytes, max allowed is {max_allowed} bytes"
        status = "OVERSIZED_ALLOWED" if policy.get("allow_oversized_final") else "FAILED"
    data = collect_size_policy(ws, final_zip, status=status, reason=reason)
    data["pass"] = passed or bool(policy.get("allow_oversized_final"))
    data["status"] = "PASSED" if passed else status
    if not passed:
        data["reason"] = reason
        data["recommendation"] = "Enable size-reduction/debloat style to reach 4.5GB"
    write_size_policy_report(ws, data)
    print(f"[SIZE] Super display target: {data.get('requested_super_target_bytes')}")
    print(f"[SIZE] Stock-safe super: {data.get('stock_super_size_bytes')}")
    print(f"[SIZE] Selected super: {data.get('selected_super_size_bytes')}")
    print(f"[SIZE] Super policy: {data.get('super_size_policy')}")
    print(f"[SIZE] Final ZIP max: {data.get('final_zip_max_allowed')}")
    print(f"[SIZE] Dynamic allocation: {data.get('dynamic_allocation_total')}")
    print(f"[SIZE] Sparse super: {data.get('sparse_super_size')}")
    print(f"[SIZE] Final ZIP: {data.get('final_zip_size')}")
    print(f"[SIZE] Policy: {data.get('status')}")
    if not passed and not policy.get("allow_oversized_final"):
        raise SizePolicyError(reason)
    return data
