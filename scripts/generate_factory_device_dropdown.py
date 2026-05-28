"""
generate_factory_device_dropdown.py

Reads registry/devices/factory_devices.json, sorts devices alphabetically by
display_name, and rewrites the AUTO-GENERATED DEVICE OPTIONS blocks in both
GitHub Actions workflow files.

Usage:
    python scripts/generate_factory_device_dropdown.py
    python scripts/generate_factory_device_dropdown.py --dry-run
    python scripts/generate_factory_device_dropdown.py --devices-json path/to/factory_devices.json
"""

import argparse
import json
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

DEVICES_JSON = REPO_ROOT / "registry" / "devices" / "factory_devices.json"

WORKFLOWS = {
    "mtk": REPO_ROOT / ".github" / "workflows" / "deadzone_mtk.yml",
    "snapdragon": REPO_ROOT / ".github" / "workflows" / "deadzone_snapdragon.yml",
}

START_MARKER = "# AUTO-GENERATED DEVICE OPTIONS START"
END_MARKER = "# AUTO-GENERATED DEVICE OPTIONS END"

OPTION_INDENT = "          "


def load_devices(json_path: pathlib.Path) -> list[dict]:
    text = json_path.read_text(encoding="utf-8")
    return json.loads(text)


def filter_devices(devices: list[dict], soc: str) -> list[dict]:
    # soc must be an exact match ("mtk" or "snapdragon").
    # Devices with soc="auto" are intentionally excluded from both workflows.
    return [d for d in devices if d.get("soc") == soc and d.get("enabled", True)]


def sort_devices(devices: list[dict]) -> list[dict]:
    return sorted(devices, key=lambda d: d["display_name"].lower())


def make_option_line(device: dict) -> str:
    return f"{OPTION_INDENT}- {device['codename']} | {device['display_name']}"


def build_options_block(devices: list[dict]) -> str:
    lines = [f"{OPTION_INDENT}{START_MARKER}"]
    for device in devices:
        lines.append(make_option_line(device))
    lines.append(f"{OPTION_INDENT}{END_MARKER}")
    return "\n".join(lines)


def rewrite_workflow(workflow_path: pathlib.Path, options_block: str, dry_run: bool = False) -> bool:
    original = workflow_path.read_text(encoding="utf-8")

    pattern = re.compile(
        r"( *" + re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER) + r")",
        re.DOTALL,
    )

    if not pattern.search(original):
        print(f"[WARN] Markers not found in {workflow_path.name} — skipping (codename string input design).")
        return True

    updated = pattern.sub(options_block, original)

    if updated == original:
        print(f"[OK] {workflow_path.name} already up to date.")
        return True

    if dry_run:
        print(f"[DRY-RUN] Would update {workflow_path.name}")
        return True

    workflow_path.write_text(updated, encoding="utf-8")
    print(f"[UPDATED] {workflow_path.name}")
    return True


def parse_select_device(selected: str) -> tuple[str, str]:
    """
    Parse 'codename | Display Name' into (codename, display_name).
    Raises ValueError if the format is invalid.
    """
    if " | " not in selected:
        raise ValueError(
            f"Invalid select_device format: {selected!r}. "
            "Expected: 'codename | Display Name'"
        )
    codename, _, display_name = selected.partition(" | ")
    codename = codename.strip()
    display_name = display_name.strip()
    if not codename:
        raise ValueError(f"Empty codename in select_device: {selected!r}")
    return codename, display_name


_INVALID_CODENAMES = frozenset(
    {"select_device_codename", "select_device", "device", "none", "null", "default"}
)


def resolve_codename(selected: str, custom_device: str = "") -> tuple[str, str]:
    """
    Resolve the final (codename, display_name) from select_device + optional custom_device.
    Raises ValueError for invalid inputs.
    """
    codename, display_name = parse_select_device(selected)
    if custom_device:
        codename = custom_device.strip()
    if codename.lower() in _INVALID_CODENAMES:
        raise ValueError(f"Invalid device codename: {codename!r}")
    return codename, display_name


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Update workflow device dropdowns.")
    parser.add_argument(
        "--devices-json",
        type=pathlib.Path,
        default=DEVICES_JSON,
        help="Path to factory_devices.json",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would change without writing files",
    )
    args = parser.parse_args(argv)

    if not args.devices_json.exists():
        print(f"[ERROR] Devices file not found: {args.devices_json}", file=sys.stderr)
        return 1

    devices = load_devices(args.devices_json)
    print(f"[INFO] Loaded {len(devices)} devices from {args.devices_json.name}")

    ok = True
    for soc, workflow_path in WORKFLOWS.items():
        if not workflow_path.exists():
            print(f"[WARN] Workflow not found: {workflow_path}")
            continue

        filtered = filter_devices(devices, soc)
        sorted_devs = sort_devices(filtered)
        options_block = build_options_block(sorted_devs)

        print(f"[INFO] {soc}: {len(sorted_devs)} devices -> {workflow_path.name}")
        result = rewrite_workflow(workflow_path, options_block, dry_run=args.dry_run)
        if not result:
            ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
