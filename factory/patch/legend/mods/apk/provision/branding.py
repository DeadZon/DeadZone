"""Safe Provision branding replacements."""
from __future__ import annotations

USER_VISIBLE_BRAND = "DeadZone"
INTERNAL_HELPER_BRAND = "Mezo"

VISIBLE_REPLACEMENTS = {
    "Elite Development": USER_VISIBLE_BRAND,
    "Elite ROM": USER_VISIBLE_BRAND,
    "Hyper Elite": USER_VISIBLE_BRAND,
    "EliteDevelopment": INTERNAL_HELPER_BRAND,
    "MoveOS": USER_VISIBLE_BRAND,
    "Elite": USER_VISIBLE_BRAND,
}

UNSAFE_CONTEXT_HINTS = (
    ".class ",
    ".method ",
    ".field ",
    "->",
    "Lmiui/os/Build;",
    "Lcom/",
    "Landroid/",
    "package=",
    "authority",
    "permission",
    "intent.",
    "/",
)


def classify_branding_candidate(text: str) -> str:
    lowered = text.lower()
    if any(hint.lower() in lowered for hint in UNSAFE_CONTEXT_HINTS):
        return "unsafe"
    return "visible"


def apply_visible_branding(text: str) -> tuple[str, list[dict], list[dict]]:
    changes: list[dict] = []
    review: list[dict] = []
    result = text
    for old, new in VISIBLE_REPLACEMENTS.items():
        if old not in result:
            continue
        status = classify_branding_candidate(result)
        if status != "visible":
            review.append({"old": old, "new": new, "status": "REVIEW_REQUIRED_BRANDING_STRING"})
            continue
        count = result.count(old)
        result = result.replace(old, new)
        changes.append({"old": old, "new": new, "count": count, "status": "BRANDING_PATCHED"})
    return result, changes, review

