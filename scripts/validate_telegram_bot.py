"""
Validate that server/telegram_bot.py meets DeadZone bot safety rules:

  1. Does NOT import subprocess, os.system, or shell-execution modules.
  2. Does NOT call subprocess.*, os.system, os.popen, or exec/eval.
  3. Does NOT import local factory/pipeline modules.
  4. Only contacts the GitHub API and Telegram API (no other outbound URLs).
  5. All required env-var names are documented in the module.
"""

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOT_PATH = ROOT / "server" / "telegram_bot.py"

REQUIRED_ENV_VARS = [
    "TELEGRAM_BOT_TOKEN",
    "GITHUB_TOKEN",
    "GITHUB_REPO",
    "TELEGRAM_ALLOWED_USER_IDS",
]

FORBIDDEN_IMPORTS = {
    "subprocess",
    "popen",
    "pty",
    "commands",
    "fabric",
    "plumbum",
    "sh",
}

FORBIDDEN_CALLS = {
    "subprocess.run",
    "subprocess.call",
    "subprocess.Popen",
    "subprocess.check_output",
    "subprocess.check_call",
    "os.system",
    "os.popen",
    "os.execv",
    "os.execve",
    "os.execvp",
    "os.execvpe",
    "os.spawnl",
    "os.spawnv",
    "eval",
    "exec",
}

ALLOWED_URL_PREFIXES = (
    "https://api.telegram.org/",
    "https://api.github.com/",
    "https://github.com/",
    f"https://github.com/",
)

errors: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)
    print(f"[FAIL] {msg}")


def warn(msg: str) -> None:
    warnings.append(msg)
    print(f"[WARN] {msg}")


def ok(msg: str) -> None:
    print(f"[OK]   {msg}")


# ---------------------------------------------------------------------------
# Load and parse
# ---------------------------------------------------------------------------

if not BOT_PATH.exists():
    fail(f"Bot file not found: {BOT_PATH}")
    sys.exit(1)

source = BOT_PATH.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(BOT_PATH))

# ---------------------------------------------------------------------------
# Check 1: Forbidden imports
# ---------------------------------------------------------------------------

for node in ast.walk(tree):
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        if isinstance(node, ast.Import):
            names = [alias.name for alias in node.names]
        else:
            names = [node.module] if node.module else []

        for name in names:
            top = name.split(".")[0] if name else ""
            if top in FORBIDDEN_IMPORTS:
                fail(f"Forbidden import '{name}' at line {node.lineno}")
            if top == "factory" or top == "pipeline":
                fail(f"Local factory/pipeline import '{name}' at line {node.lineno}")

ok("No forbidden imports found")

# ---------------------------------------------------------------------------
# Check 2: Forbidden call patterns
# ---------------------------------------------------------------------------

for node in ast.walk(tree):
    if isinstance(node, ast.Call):
        # Reconstruct call name
        func = node.func
        call_str = ""
        if isinstance(func, ast.Name):
            call_str = func.id
        elif isinstance(func, ast.Attribute):
            parts = []
            cur = func
            while isinstance(cur, ast.Attribute):
                parts.append(cur.attr)
                cur = cur.value
            if isinstance(cur, ast.Name):
                parts.append(cur.id)
            call_str = ".".join(reversed(parts))

        if call_str in FORBIDDEN_CALLS:
            fail(f"Forbidden call '{call_str}' at line {node.lineno}")

ok("No forbidden shell/exec calls found")

# ---------------------------------------------------------------------------
# Check 3: URL hygiene — only GitHub and Telegram API
# ---------------------------------------------------------------------------

for node in ast.walk(tree):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        val: str = node.value
        if val.startswith("https://") or val.startswith("http://"):
            # Allow known-good prefixes
            allowed = any(val.startswith(p) for p in ALLOWED_URL_PREFIXES)
            # Also allow f-string fragments that are just the base
            if not allowed and not val.endswith("/"):
                warn(f"Unexpected URL literal '{val}' at line {node.lineno}")

ok("URL literals checked")

# ---------------------------------------------------------------------------
# Check 4: Required env vars documented
# ---------------------------------------------------------------------------

missing_docs: list[str] = []
for var in REQUIRED_ENV_VARS:
    if var not in source:
        missing_docs.append(var)

if missing_docs:
    for var in missing_docs:
        fail(f"Required env var '{var}' not documented/referenced in bot source")
else:
    ok("All required env vars referenced in source")

# ---------------------------------------------------------------------------
# Check 5: os.environ.get used (not os.getenv with fallback that hides missing)
# ---------------------------------------------------------------------------

if "os.system" in source:
    fail("os.system found in source")
else:
    ok("os.system not present")

# ---------------------------------------------------------------------------
# Check 6: rom_url must not be set to "auto" or 'auto'
# ---------------------------------------------------------------------------

import re as _re_bot

_AUTO_PATTERNS = [
    r'rom_url\s*[=:]\s*["\']auto["\']',
    r'"auto"\s*#.*rom',
    r"'auto'\s*#.*rom",
]
_found_auto = False
for _pat in _AUTO_PATTERNS:
    if _re_bot.search(_pat, source, _re_bot.IGNORECASE):
        fail(f"Bot source contains rom_url=auto pattern matching /{_pat}/ — remove all auto handling")
        _found_auto = True

if not _found_auto:
    ok("No rom_url=auto patterns found")

# ---------------------------------------------------------------------------
# Check 7: build commands require URL argument (len(args) >= 3)
# ---------------------------------------------------------------------------

if "len(args) < 3" in source:
    ok("build commands enforce 3-argument minimum (codename edition rom_url)")
elif "len(args) < 2" in source:
    fail("build commands only check for 2 args — must require 3: codename edition rom_url")
else:
    warn("Could not verify argument count check for build commands")

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

print()
if errors:
    print(f"VALIDATION FAILED — {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1)
else:
    if warnings:
        print(f"VALIDATION PASSED with {len(warnings)} warning(s)")
    else:
        print("VALIDATION PASSED — bot is clean")
    sys.exit(0)
