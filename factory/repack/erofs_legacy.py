"""Legacy-compatible EROFS partition image repack helpers."""
from __future__ import annotations

import os
import platform
import shutil
import stat
import subprocess
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
_LEGACY_ROOT = _REPO_ROOT / "third_party" / "mezo_core"


def _default_root_dir(root_dir: Path | None = None) -> Path:
    return Path(root_dir).resolve() if root_dir is not None else _LEGACY_ROOT.resolve()


def _tool_bin_candidate(root_dir: Path) -> Path:
    return root_dir / "bin" / platform.system() / platform.machine() / "mkfs.erofs"


def _try_existing(path: Path) -> Path | None:
    if not path.exists():
        return None
    if os.name == "posix" and not os.access(str(path), os.X_OK):
        try:
            path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        except Exception:
            pass
    return path


def resolve_mkfs_erofs_binary_legacy(root_dir: Path | None = None) -> Path | None:
    """
    Resolve mkfs.erofs with the same legacy search order.

    The legacy resolver checked the original command, the arch-specific bundled
    tool path, the flat bundled tool path, and then PATH. This wrapper returns
    None instead of an unresolved command so dry-runs can report a missing tool.
    """
    root_dir = _default_root_dir(root_dir)
    original_binary = Path("mkfs.erofs")

    if original_binary.is_absolute():
        if found := _try_existing(original_binary):
            return found

    if found := _try_existing(original_binary):
        return found

    if found := _try_existing(_tool_bin_candidate(root_dir)):
        return found

    if found := _try_existing(root_dir / "bin" / "mkfs.erofs"):
        return found

    which_result = shutil.which("mkfs.erofs")
    if which_result:
        return Path(which_result)

    return None


def build_erofs_commands_legacy(
    partition_name: str,
    partition_root: Path,
    output_img: Path,
    fs_config: Path | None = None,
    file_contexts: Path | None = None,
    extra_args: list[str] | None = None,
) -> list[list[str]]:
    """Build mkfs.erofs commands using the legacy option order."""
    partition_root = Path(partition_root)
    output_img = Path(output_img)
    project_dir = partition_root.parent
    if partition_root.name == partition_name and partition_root.parent.name == partition_name:
        project_dir = partition_root.parent.parent

    fs_config = fs_config or project_dir / "config" / f"{partition_name}_fs_config"
    file_contexts = file_contexts or project_dir / "config" / f"{partition_name}_file_contexts"
    fs_options = project_dir / "config" / f"{partition_name}_fs_options"
    extra_args = extra_args or []

    commands: list[list[str]] = []

    if fs_options.exists():
        try:
            line = ""
            for raw_line in fs_options.read_text(encoding="utf-8").splitlines():
                if raw_line.startswith("mkfs.erofs options:"):
                    line = raw_line.split("mkfs.erofs options:", 1)[1].strip()
                    break

            if line:
                tokens = line.split()
                parsed_opts: list[str] = []
                i = 0
                while i < len(tokens):
                    token = tokens[i]
                    if token.startswith("-z"):
                        parsed_opts.append(token)
                    elif token in {"-T", "-U", "-E"} and i + 1 < len(tokens):
                        parsed_opts.extend([token, tokens[i + 1]])
                        i += 1
                    elif token.startswith("--mount-point="):
                        parsed_opts.append(token)
                    elif token == "--mount-point" and i + 1 < len(tokens):
                        parsed_opts.extend([token, tokens[i + 1]])
                        i += 1
                    i += 1

                commands.append([
                    "mkfs.erofs",
                    *parsed_opts,
                    *extra_args,
                    f"--fs-config-file={fs_config}",
                    f"--file-contexts={file_contexts}",
                    str(output_img),
                    str(partition_root),
                ])
        except Exception:
            pass

    commands.append([
        "mkfs.erofs",
        "-zlz4hc",
        "-T", "0",
        f"--mount-point=/{partition_name}",
        *extra_args,
        f"--fs-config-file={fs_config}",
        f"--file-contexts={file_contexts}",
        str(output_img),
        str(partition_root),
    ])

    commands.append([
        "mkfs.erofs",
        "-zlz4",
        "-T", "0",
        f"--mount-point=/{partition_name}",
        *extra_args,
        f"--fs-config-file={fs_config}",
        f"--file-contexts={file_contexts}",
        str(output_img),
        str(partition_root),
    ])

    unique_commands: list[list[str]] = []
    seen: set[tuple[str, ...]] = set()
    for command in commands:
        key = tuple(command)
        if key not in seen:
            seen.add(key)
            unique_commands.append(command)
    return unique_commands


def _dir_size(path: Path) -> int | None:
    try:
        return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())
    except Exception:
        return None


def _resolve_command(command: list[str], root_dir: Path) -> tuple[list[str], Path | None]:
    resolved_binary = resolve_mkfs_erofs_binary_legacy(root_dir)
    resolved = list(command)
    if resolved_binary is not None:
        resolved[0] = str(resolved_binary)
    return resolved, resolved_binary


def repack_erofs_legacy(
    partition_name: str,
    partition_root: Path,
    output_img: Path,
    root_dir: Path | None = None,
    execute: bool = False,
) -> dict:
    """Plan or execute a legacy-compatible mkfs.erofs repack."""
    root_dir = _default_root_dir(root_dir)
    partition_root = Path(partition_root).resolve()
    output_img = Path(output_img).resolve()
    project_dir = partition_root.parent
    if partition_root.name == partition_name and partition_root.parent.name == partition_name:
        project_dir = partition_root.parent.parent

    fs_config = project_dir / "config" / f"{partition_name}_fs_config"
    file_contexts = project_dir / "config" / f"{partition_name}_file_contexts"
    commands = build_erofs_commands_legacy(
        partition_name=partition_name,
        partition_root=partition_root,
        output_img=output_img,
        fs_config=fs_config,
        file_contexts=file_contexts,
    )

    warnings: list[str] = []
    errors: list[str] = []
    commands_executed: list[list[str]] = []
    images_created: list[str] = []
    skipped_items: list[dict] = []

    mkfs_path = resolve_mkfs_erofs_binary_legacy(root_dir)
    resolved_commands = []
    for command in commands:
        resolved, _ = _resolve_command(command, root_dir)
        resolved_commands.append(resolved)

    inputs = {
        "partition_root": str(partition_root),
        "partition_root_exists": partition_root.is_dir(),
        "partition_root_bytes": _dir_size(partition_root) if partition_root.is_dir() else None,
        "fs_config": str(fs_config),
        "fs_config_exists": fs_config.exists(),
        "fs_config_bytes": fs_config.stat().st_size if fs_config.exists() else None,
        "file_contexts": str(file_contexts),
        "file_contexts_exists": file_contexts.exists(),
        "file_contexts_bytes": file_contexts.stat().st_size if file_contexts.exists() else None,
    }

    if not partition_root.is_dir():
        errors.append(f"Partition directory is missing: {partition_root}")
    if not fs_config.exists() or fs_config.stat().st_size == 0:
        errors.append(f"fs_config is missing or empty: {fs_config}")
    if not file_contexts.exists() or file_contexts.stat().st_size == 0:
        errors.append(f"file_contexts is missing or empty: {file_contexts}")
    if mkfs_path is None:
        errors.append("mkfs.erofs was not found by the legacy resolver")

    if output_img.exists():
        warnings.append(f"Existing image will be overwritten by legacy repack: {output_img}")

    if not execute:
        return {
            "partition": partition_name,
            "dry_run": True,
            "status": "DRY_RUN" if not errors else "FAILED",
            "mkfs_erofs_path": str(mkfs_path) if mkfs_path else None,
            "inputs": inputs,
            "output_img": str(output_img),
            "commands_planned": resolved_commands,
            "commands_executed": commands_executed,
            "images_created": images_created,
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    if errors:
        skipped_items.append({"partition": partition_name, "reason": "preflight failed"})
        return {
            "partition": partition_name,
            "dry_run": False,
            "status": "FAILED",
            "mkfs_erofs_path": str(mkfs_path) if mkfs_path else None,
            "inputs": inputs,
            "output_img": str(output_img),
            "commands_planned": resolved_commands,
            "commands_executed": commands_executed,
            "images_created": images_created,
            "skipped_items": skipped_items,
            "warnings": warnings,
            "errors": errors,
        }

    output_img.parent.mkdir(parents=True, exist_ok=True)
    if output_img.exists():
        output_img.unlink()

    log_dir = project_dir / "logs" / "mkfs_erofs"
    log_dir.mkdir(parents=True, exist_ok=True)
    last_error: int | str | None = None

    for index, command in enumerate(commands, start=1):
        resolved_cmd, resolved_binary = _resolve_command(command, root_dir)
        commands_executed.append(resolved_cmd)
        try:
            result = subprocess.run(
                resolved_cmd,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name != "posix" else 0,
            )
            ret = result.returncode
            combined_output = result.stdout.decode("utf-8", errors="replace")
        except FileNotFoundError as exc:
            ret = 2
            combined_output = f"[FileNotFoundError] {exc}\n"

        log_file = log_dir / f"{partition_name}_attempt_{index}.log"
        log_file.write_text(
            "\n".join([
                f"partition          : {partition_name}",
                f"attempt            : {index}",
                f"original_binary    : {command[0]}",
                f"resolved_binary    : {resolved_binary}",
                f"resolved_binary_exists: {Path(resolved_cmd[0]).exists()}",
                f"which_mkfs_erofs   : {shutil.which('mkfs.erofs') or 'not found'}",
                f"PATH               : {os.environ.get('PATH', '')}",
                f"command            : {' '.join(resolved_cmd)}",
                f"return_code        : {ret}",
                f"output_img         : {output_img}",
                "",
                "--- stdout+stderr ---",
                combined_output,
            ]),
            encoding="utf-8",
            newline="\n",
        )

        if ret == 0 and output_img.exists() and output_img.stat().st_size > 0:
            images_created.append(str(output_img))
            return {
                "partition": partition_name,
                "dry_run": False,
                "status": "APPLIED",
                "mkfs_erofs_path": str(mkfs_path) if mkfs_path else None,
                "inputs": inputs,
                "output_img": str(output_img),
                "commands_planned": resolved_commands,
                "commands_executed": commands_executed,
                "images_created": images_created,
                "skipped_items": skipped_items,
                "warnings": warnings,
                "errors": errors,
            }

        last_error = ret
        if output_img.exists():
            output_img.unlink()

    errors.append(f"EROFS repack failed for {partition_name} with return code {last_error}")
    return {
        "partition": partition_name,
        "dry_run": False,
        "status": "FAILED",
        "mkfs_erofs_path": str(mkfs_path) if mkfs_path else None,
        "inputs": inputs,
        "output_img": str(output_img),
        "commands_planned": resolved_commands,
        "commands_executed": commands_executed,
        "images_created": images_created,
        "skipped_items": skipped_items,
        "warnings": warnings,
        "errors": errors,
    }

