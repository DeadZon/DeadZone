from __future__ import annotations

import os
import shutil
import stat
from dataclasses import dataclass
from pathlib import Path

from factory.core.workspace import Workspace

REQUIRED_TOOLS = ("lpmake", "lpdump", "lpunpack", "simg2img", "img2simg")
OPTIONAL_TOOLS = ("brotli", "zstd", "file", "debugfs", "dump.erofs", "fsck.erofs", "erofsfuse", "7z", "mount")
HELPER_DIRS = (
    Path("tools/helper"),
    Path("tools/helper/linux"),
    Path("tools/helper/android"),
)
MISSING_LPMAKE_MESSAGE = (
    "lpmake is missing. Install Android dynamic partition tools or place lpmake in tools/helper/linux."
)


@dataclass(frozen=True)
class ToolStatus:
    name: str
    path: Path | None
    source: str
    exists: bool
    executable: bool
    checked: tuple[Path, ...]
    action_needed: str


@dataclass(frozen=True)
class Toolchain:
    tools: dict[str, ToolStatus]
    report_path: Path

    def path(self, name: str) -> Path | None:
        status = self.tools.get(name)
        return status.path if status else None

    def missing_required(self) -> list[str]:
        return [name for name in REQUIRED_TOOLS if self.path(name) is None]


def _repo_path(path: Path) -> Path:
    return path if path.is_absolute() else Path.cwd() / path


def _tool_names(tool: str) -> tuple[str, ...]:
    exe = f"{tool}.exe" if os.name == "nt" else tool
    return (exe, tool) if exe != tool else (tool,)


def _helper_candidates(tool: str) -> list[Path]:
    candidates: list[Path] = []
    for root in HELPER_DIRS:
        for name in _tool_names(tool):
            candidate = _repo_path(root) / name
            if candidate not in candidates:
                candidates.append(candidate)
    return candidates


def _ensure_linux_executable(path: Path) -> bool:
    if os.name != "posix":
        return path.is_file()
    try:
        mode = path.stat().st_mode
    except OSError:
        return False
    if mode & stat.S_IXUSR:
        return True
    try:
        path.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    except OSError:
        return False
    return os.access(path, os.X_OK)


def _resolve_tool(tool: str) -> ToolStatus:
    checked = _helper_candidates(tool)
    for candidate in checked:
        if candidate.is_file():
            executable = _ensure_linux_executable(candidate)
            resolved = candidate.resolve()
            return ToolStatus(
                name=tool,
                path=resolved if executable else None,
                source="helper",
                exists=True,
                executable=executable,
                checked=tuple(checked),
                action_needed="" if executable else f"make {resolved} executable",
            )

    found = shutil.which(tool) or shutil.which(f"{tool}.exe")
    if found:
        path = Path(found).resolve()
        return ToolStatus(
            name=tool,
            path=path,
            source="PATH",
            exists=True,
            executable=os.access(path, os.X_OK) if os.name == "posix" else path.is_file(),
            checked=tuple(checked),
            action_needed="",
        )

    action = f"install {tool} or place it in tools/helper/linux"
    if tool == "lpmake":
        action = MISSING_LPMAKE_MESSAGE
    return ToolStatus(
        name=tool,
        path=None,
        source="missing",
        exists=False,
        executable=False,
        checked=tuple(checked),
        action_needed=action,
    )


def resolve_toolchain(ws: Workspace | None = None) -> Toolchain:
    report_path = (ws.reports if ws else Path("output/workspace/reports")) / "toolchain_report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    names = (*REQUIRED_TOOLS, *OPTIONAL_TOOLS)
    toolchain = Toolchain(
        tools={name: _resolve_tool(name) for name in names},
        report_path=report_path,
    )
    write_toolchain_report(toolchain)
    return toolchain


def write_toolchain_report(toolchain: Toolchain) -> Path:
    missing = [name for name in REQUIRED_TOOLS if toolchain.path(name) is None]
    lines = [
        "DeadZone Toolchain Report",
        "=========================",
        "required tools:",
        *[f"  - {name}" for name in REQUIRED_TOOLS],
        "",
        "optional tools:",
        *[f"  - {name}" for name in OPTIONAL_TOOLS],
        "",
        "helper locations checked:",
        *[f"  - {_repo_path(path)}" for path in HELPER_DIRS],
        "",
        f"PATH: {os.environ.get('PATH', '')}",
        "",
        "resolved tools:",
    ]
    for name in (*REQUIRED_TOOLS, *OPTIONAL_TOOLS):
        status = toolchain.tools[name]
        lines.extend(
            [
                f"  - {name}:",
                f"      path: {status.path or '(missing)'}",
                f"      source: {status.source}",
                f"      exists: {status.exists}",
                f"      executable: {status.executable}",
                f"      action needed: {status.action_needed or '(none)'}",
            ]
        )
    lines += [
        "",
        "missing required tools:",
        *([f"  - {name}" for name in missing] or ["  (none)"]),
        "",
        "candidate files checked:",
    ]
    for name in (*REQUIRED_TOOLS, *OPTIONAL_TOOLS):
        lines.append(f"  - {name}:")
        lines.extend(f"      {candidate}" for candidate in toolchain.tools[name].checked)
    lines.append("")
    toolchain.report_path.write_text("\n".join(lines), encoding="utf-8")
    return toolchain.report_path
