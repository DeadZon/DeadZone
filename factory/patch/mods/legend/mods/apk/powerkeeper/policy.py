"""PowerKeeper-specific patch policy."""
from __future__ import annotations

APPLY_FULL_POWERKEEPER_MTCR = True
APPLY_BUILD_FLAG_REWRITES = True

POWERKEEPER_ALLOWED_FLAG_REWRITES = [
    {
        "from": "Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z",
        "to": "Lmiui/os/Build;->IS_MIUI:Z",
    },
]
