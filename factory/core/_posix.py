import os

if os.name == "nt":
    from ctypes.wintypes import LPCSTR, DWORD
    from stat import FILE_ATTRIBUTE_SYSTEM
    from ctypes import windll

from logging import exception


def symlink(link_target, target):
    if not os.path.exists(os.path.dirname(target)):
        os.makedirs(os.path.dirname(target), exist_ok=True)
    if os.name == "posix":
        os.symlink(link_target, target)
    elif os.name == "nt":
        with open(target.replace("/", os.sep), "wb") as out:
            out.write(b"!<symlink>" + link_target.encode("utf-16") + b"\x00\x00")
            try:
                windll.kernel32.SetFileAttributesA(LPCSTR(target.encode()), DWORD(FILE_ATTRIBUTE_SYSTEM))
            except Exception:
                exception("Posix")
