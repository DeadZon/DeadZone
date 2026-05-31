"""
Cross-platform fake command-line tools for tests.

Production code resolves tools with ``shutil.which()`` and invokes them via
``subprocess.run([tool, ...])``.  POSIX shell scripts (``#!/bin/sh``) cannot run
on Windows, which is why the original fake-``mkfs.erofs`` tests failed there.

These helpers emit a tiny Python implementation plus a platform-appropriate
launcher that ``shutil.which`` can find under the given directory:

* POSIX  → an executable ``mkfs.erofs`` shell wrapper.
* Windows → a ``mkfs.erofs.bat`` wrapper (``.BAT`` is in the default PATHEXT, so
  ``shutil.which("mkfs.erofs")`` resolves it).

Both forward to the same Python implementation invoked with the current
interpreter, so behaviour is identical on every platform.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

_IMPL_TEMPLATE = '''\
import sys

args = sys.argv[1:]
if args and args[0] == "--help":
    sys.stdout.write("available compressors: lz4 lz4hc\\n")
    sys.exit(0)

# mkfs.erofs forms used by production:
#   mkfs.erofs -z <comp> <out_img> <tree>
#   mkfs.erofs <out_img> <tree>
out = args[2] if (len(args) >= 3 and args[0] == "-z") else (args[0] if args else "")

FAIL = {fail!r}
CONTENT = {content!r}
SIZE = {size!r}

if FAIL or not out:
    sys.exit(1)

data = CONTENT if CONTENT is not None else (b"\\x00" * SIZE)
with open(out, "wb") as fh:
    fh.write(data)
sys.exit(0)
'''


def _render_impl(*, size: int, content: bytes | None, fail: bool) -> str:
    return _IMPL_TEMPLATE.format(size=size, content=content, fail=fail)


def _install_launcher(helper_dir: Path, tool_name: str, impl: Path) -> Path:
    interpreter = sys.executable
    if os.name == "nt":
        launcher = helper_dir / f"{tool_name}.bat"
        launcher.write_text(
            f'@echo off\r\n"{interpreter}" "{impl}" %*\r\n',
            encoding="utf-8",
        )
    else:
        launcher = helper_dir / tool_name
        launcher.write_text(
            f'#!/bin/sh\nexec "{interpreter}" "{impl}" "$@"\n',
            encoding="utf-8",
        )
        launcher.chmod(0o755)
    return launcher


def write_fake_mkfs_erofs(
    helper_dir: Path,
    *,
    size: int = 7,
    content: bytes | None = b"rebuilt",
    fail: bool = False,
) -> Path:
    """Create a cross-platform fake ``mkfs.erofs`` under *helper_dir*.

    * ``content`` (bytes) — exact bytes written to the output image.
    * ``size`` — used only when ``content`` is None: writes that many zero bytes
      (handy for exercising size-growth validation).
    * ``fail`` — the tool exits non-zero without producing output.

    Returns the launcher path.  Add *helper_dir* to ``PATH`` so the toolchain
    resolves it.
    """
    helper_dir.mkdir(parents=True, exist_ok=True)
    impl = helper_dir / "_mkfs_erofs_impl.py"
    impl.write_text(_render_impl(size=size, content=content, fail=fail), encoding="utf-8")
    return _install_launcher(helper_dir, "mkfs.erofs", impl)
