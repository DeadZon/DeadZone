"""Pure-Python EXT4 image extractor.

Ported from MIO-KITCHEN-SOURCE imgextractor.py (AGPL-3.0).
Adapted for DeadZone Universal Core — no external tool dependencies.
"""
from __future__ import annotations

import logging
import os
import re
import struct
from pathlib import Path
from typing import Any

from factory.core._posix import symlink
from factory.core import _ext4 as ext4


def _get_perm(arg: str) -> str:
    if len(arg) < 9 or len(arg) > 10:
        return ""
    if len(arg) > 8:
        arg = arg[1:]
    o = s = w = g = 0
    perms = {"r": 4, "w": 2, "x": 1}
    for n, sym in enumerate(arg):
        if n == 0 and perms.get(sym):
            o = perms.get(sym)
        elif n == 1 and perms.get(sym):
            o += perms.get(sym)
        elif n == 2:
            if sym == "S":
                s = 4
            elif perms.get(sym):
                o += perms.get(sym)
            elif sym == "s":
                s += 4
                o += 1
        elif n == 3 and perms.get(sym):
            g = perms.get(sym)
        elif n == 4 and perms.get(sym):
            g += perms.get(sym)
        if n == 5:
            if perms.get(sym):
                g += perms.get(sym)
            elif sym == "S":
                s += 2
            elif sym == "s":
                s += 2
                g += 1
        elif n == 6 and perms.get(sym):
            w = perms.get(sym)
        elif n == 7 and perms.get(sym):
            w += perms.get(sym)
        elif n == 8:
            if perms.get(sym):
                w += perms.get(sym)
            elif sym == "T":
                s += 1
            elif sym == "t":
                s += 1
                w += 1
    return f"{s}{o}{g}{w}"


def _scan_dir(root_inode: Any, extract_dir: Path, filename: str, context: list, fs_config: list, space: list, root_path: str = "", error_box: list[int] = None) -> None:
    if error_box is None:
        error_box = [0]
    for entry_name, entry_inode_idx, entry_type in root_inode.open_dir():
        if entry_name in (".", "..") or entry_name.endswith(" (2)"):
            continue
        if error_box[0] >= 200:
            break
        entry_inode = root_inode.volume.get_inode(entry_inode_idx, entry_type)
        entry_inode_path = root_path + "/" + entry_name
        if entry_inode_path[-1:] == "/" and not entry_inode.is_dir:
            error_box[0] += 1
            continue

        mode = _get_perm(entry_inode.mode_str)
        uid = entry_inode.inode.i_uid
        gid = entry_inode.inode.i_gid
        cap = ""
        link_target = ""
        tmp_path = filename + entry_inode_path
        for f, e in entry_inode.xattrs():
            if f == "security.selinux":
                t_p = tmp_path
                for fuk_ in "\\^$.|?*+(){}[]":
                    t_p = t_p.replace(fuk_, f"\\{fuk_}")
                context.append(f"/{t_p} {e.decode('utf8')[:-1]}")
            elif f == "security.capability":
                r = struct.unpack("<5I", e)
                if r[1] > 65535:
                    cap = hex(int(f"{r[3]:04x}{r[1]:04x}", 16))
                else:
                    cap = hex(int(f"{r[3]:04x}{r[2]:04x}{r[1]:04x}", 16))
                cap = f" capabilities={cap}"
        if entry_inode.is_symlink:
            try:
                link_target = entry_inode.open_read().read().decode("utf8")
            except Exception:
                try:
                    link_target_block = int.from_bytes(entry_inode.open_read().read(), "little")
                    link_target = root_inode.volume.read(
                        link_target_block * root_inode.volume.block_size,
                        entry_inode.inode.i_size,
                    ).decode("utf8")
                except Exception:
                    link_target = ""
        if " " in tmp_path[1:]:
            space.append(tmp_path)
            fs_config.append(f"{tmp_path.replace(' ', '_')} {uid} {gid} {mode}{cap} {link_target}")
        else:
            fs_config.append(f"{tmp_path} {uid} {gid} {mode}{cap} {link_target}")

        if entry_inode.is_dir:
            if os.name == "nt" and ":" in entry_inode_path:
                entry_inode_path = entry_inode_path.replace(":", "_")
            dir_target = extract_dir / entry_inode_path.replace(" ", "_").replace('"', "")
            if str(dir_target).endswith(".") and os.name == "nt":
                dir_target = Path(str(dir_target)[:-1])
            dir_target.mkdir(parents=True, exist_ok=True)
            if os.name == "posix" and os.geteuid() == 0 and mode:
                try:
                    os.chmod(dir_target, int(mode, 8))
                    os.chown(dir_target, uid, gid)
                except Exception:
                    pass
            _scan_dir(entry_inode, extract_dir, filename, context, fs_config, space, entry_inode_path, error_box)
        elif entry_inode.is_file:
            file_target = extract_dir / entry_inode_path.replace(" ", "_").replace('"', "")
            file_target.parent.mkdir(parents=True, exist_ok=True)
            try:
                file_target.write_bytes(entry_inode.open_read().read())
            except Exception as exc:
                logging.exception("Ext4Extractor")
            if os.name == "posix" and os.geteuid() == 0 and mode:
                try:
                    os.chmod(file_target, int(mode, 8))
                    os.chown(file_target, uid, gid)
                except Exception:
                    pass
        elif entry_inode.is_symlink:
            target = extract_dir / entry_inode_path.replace(" ", "_")
            try:
                if target.is_symlink() or target.is_file():
                    try:
                        target.unlink()
                    except Exception:
                        pass
                if link_target:
                    symlink(link_target, str(target))
            except Exception:
                try:
                    if link_target and link_target.isprintable():
                        symlink(link_target, str(target))
                except Exception:
                    pass


def extract_ext4_image(image: Path, extract_dir: Path) -> tuple[bool, str]:
    """Extract an EXT4 image to extract_dir using pure Python.

    Returns (success, reason).
    """
    extract_dir.mkdir(parents=True, exist_ok=True)
    filename = image.stem.split("-")[0].split(" ")[0]

    context: list[str] = []
    fs_config: list[str] = []
    space: list[str] = []

    try:
        with image.open("rb") as fh:
            volume = ext4.Volume(fh)
            _scan_dir(volume.root, extract_dir, filename, context, fs_config, space)
    except Exception as exc:
        return False, f"Python EXT4 extractor failed: {exc}"

    if not any(extract_dir.iterdir()):
        return False, "Python EXT4 extractor produced no files"
    return True, "python-ext4"


def get_mount_point(image: Path) -> str:
    """Return the EXT4 volume mount point (e.g. 'system', 'product')."""
    try:
        with image.open("rb") as fh:
            mount = ext4.Volume(fh).get_mount_point
            if mount.startswith("/"):
                mount = mount[1:]
            if "/" in mount:
                parts = mount.split("/")
                mount = parts[-1]
            if any(c in mount for c in (".", "@", "#")):
                mount = ""
            return mount
    except Exception:
        return ""
