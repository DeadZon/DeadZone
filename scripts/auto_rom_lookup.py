"""
auto_rom_lookup.py

Auto ROM URL resolver for DeadZone Factory.
Currently a stub — returns None for all devices.
Implement real URL discovery here when a firmware mirror source is available.

CLI usage (called by workflow step or tests):
    python scripts/auto_rom_lookup.py --codename zircon --rom-source auto_latest
    python scripts/auto_rom_lookup.py --codename garnet --rom-source manual_url --manual-url https://...

Exits 0 and prints URL on success, exits 1 with error on stderr on failure.
"""

import argparse
import sys


def find_latest_rom_url(codename: str) -> str | None:
    """
    Return the latest available ROM download URL for the given codename.
    Returns None when no URL can be determined automatically.
    """
    # Stub: no automatic source implemented yet.
    return None


def resolve_rom_url(
    codename: str,
    rom_source: str,
    manual_url: str = "",
) -> tuple[str, str]:
    """
    Resolve the final ROM URL given codename and rom_source mode.

    Returns:
        (url, error_message)
        - If url is non-empty: success.
        - If url is empty: error_message describes why.
    """
    if rom_source == "manual_url":
        if not manual_url:
            return "", "rom_url is required when rom_source=manual_url"
        if not (manual_url.startswith("http://") or manual_url.startswith("https://")):
            return "", "rom_url must start with http:// or https://"
        return manual_url, ""

    if rom_source == "auto_latest":
        url = find_latest_rom_url(codename)
        if not url:
            return (
                "",
                "No automatic ROM URL found for this device. Use manual_url mode.",
            )
        return url, ""

    return "", f"Invalid rom_source: {rom_source!r}. Must be auto_latest or manual_url."


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Resolve ROM URL for a device.")
    parser.add_argument("--codename", required=True, help="Device codename")
    parser.add_argument(
        "--rom-source",
        default="auto_latest",
        choices=["auto_latest", "manual_url"],
        help="ROM source mode",
    )
    parser.add_argument("--manual-url", default="", help="URL for manual_url mode")
    args = parser.parse_args(argv)

    url, error = resolve_rom_url(args.codename, args.rom_source, args.manual_url)
    if error:
        print(f"[ERROR] {error}", file=sys.stderr)
        return 1
    print(url)
    return 0


if __name__ == "__main__":
    sys.exit(main())
