"""
Short plaintext/HTML build message formatters for Telegram notifications.
"""


def _soc_label(soc: str) -> str:
    return "MTK" if soc.lower() == "mtk" else soc.capitalize()


def format_build_start(
    device: str,
    soc: str,
    platform: str,
    flavor: str,
    run_url: str = None,
) -> str:
    lines = [
        f"\U0001f680 DeadZone {_soc_label(soc)} build started",
        f"Device: {device}",
        f"Platform: {platform}",
        f"Flavor: {flavor}",
    ]
    if run_url:
        lines.append(f"Run: {run_url}")
    return "\n".join(lines)


def format_build_failure(
    device: str,
    soc: str,
    platform: str,
    flavor: str,
    run_url: str = None,
    reason: str = None,
) -> str:
    lines = [
        f"❌ DeadZone {_soc_label(soc)} build failed",
        f"Device: {device}",
        f"Platform: {platform}",
        f"Flavor: {flavor}",
    ]
    if run_url:
        lines.append(f"Run: {run_url}")
    if reason:
        lines.append(f"Reason: {reason}")
    lines.append("Diagnostics artifact may be available.")
    return "\n".join(lines)


def format_upload_success(
    device: str,
    soc: str,
    platform: str,
    flavor: str,
    pixeldrain_link: str,
    run_url: str = None,
) -> str:
    lines = [
        f"✅ DeadZone {_soc_label(soc)} ROM uploaded",
        f"Device: {device}",
        f"Platform: {platform}",
        f"Flavor: {flavor}",
        f"PixelDrain: {pixeldrain_link}",
    ]
    if run_url:
        lines.append(f"Run: {run_url}")
    return "\n".join(lines)
