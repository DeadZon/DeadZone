"""Generate static PowerKeeper rules from a temporary comparison archive.

This tool is generation-only. Runtime patching imports the emitted Python
modules and never opens the temporary extraction input.
"""
from __future__ import annotations

import argparse
import keyword
import re
import zipfile
from pathlib import Path

TARGET_APK = "PowerKeeper.apk"
DEFAULT_INPUTS = (
    Path("app/PowerKeeper/dex.mtcr"),
    Path("Legend/system_ext/priv-app/PowerKeeper/compare/dex.mtcr"),
    Path("Legend/system_ext/app/PowerKeeper/dex.mtcr"),
)
DEFAULT_OUT = Path("factory/patch/legend/powerkeeper")
FLAG_FROM = "Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z"
FLAG_TO = "Lmiui/os/Build;->IS_MIUI:Z"


def _q(value) -> str:
    return repr(value)


def _triple(text: str) -> str:
    return '"""' + text.replace('"""', '\\"\\"\\"') + '"""'


def _decode(data: bytes) -> str:
    return data.decode("utf-8", "replace")


def _safe_module_name(class_name: str) -> str:
    name = re.sub(
        r"[^0-9A-Za-z_]+",
        "_",
        class_name.replace("$", "__").replace("/", "_"),
    ).strip("_")
    if not name:
        name = "class_rule"
    if name[0].isdigit() or keyword.iskeyword(name):
        name = f"_{name}"
    return name


def _methods(text: str) -> dict[str, str]:
    return {
        m.group(1).split("\n", 1)[0].strip(): m.group(1)
        for m in re.finditer(r"(\.method\s[^\n]+\n(?:.*?\n)*?\.end method)", text, re.S)
    }


def _method_name(sig: str) -> str:
    match = re.search(r"\s([^\s(]+)\(", sig)
    return match.group(1) if match else ""


def _anchors(block: str, limit: int = 8) -> list[str]:
    keep = []
    prefixes = (
        "invoke-", "iget", "iput", "sget", "sput", "const-string",
        "new-instance", "check-cast", "return", "if-",
    )
    for raw in block.splitlines():
        line = raw.strip()
        if line and line.startswith(prefixes):
            keep.append(line)
            if len(keep) >= limit:
                break
    return keep


def _class_anchors(text: str) -> list[str]:
    anchors = []
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith(".super ") or line.startswith(".implements ") or " static final " in line:
            anchors.append(line)
        if len(anchors) >= 6:
            break
    return anchors


def _target_class(name: str) -> str:
    return f"{name}.smali"


def _patch_id(class_name: str, method_name: str, suffix: str = "") -> str:
    raw = f"{_safe_module_name(class_name)}__{_safe_module_name(method_name or 'method')}{suffix}"
    return raw[:180]


def _flag_rewrite_count(old_block: str, new_block: str) -> int:
    old_count = old_block.count(FLAG_FROM)
    new_count = new_block.count(FLAG_TO)
    return min(old_count, new_count)


def _resolve_input(explicit: Path | None) -> Path:
    if explicit is not None:
        if not explicit.is_file():
            raise FileNotFoundError(explicit)
        return explicit
    for candidate in DEFAULT_INPUTS:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError("No PowerKeeper comparison archive found in known temporary locations")


def generate(source: Path, out_dir: Path) -> dict:
    smali_dir = out_dir / "smali"
    smali_dir.mkdir(parents=True, exist_ok=True)
    for stale in smali_dir.glob("*.py"):
        if stale.name != "__init__.py":
            stale.unlink()
    (smali_dir / "__init__.py").write_text("", encoding="utf-8")

    changed_classes = 0
    changed_methods = 0
    flag_rewrites = 0
    lock_detected = False
    gms_detected = False
    classes: list[str] = []
    methods: list[dict] = []
    modules: list[str] = []

    with zipfile.ZipFile(source) as archive:
        names = archive.namelist()
        old_entries = {n[2:]: n for n in names if n.startswith("a/")}
        new_entries = {n[2:]: n for n in names if n.startswith("b/")}

        for key in sorted((set(old_entries) | set(new_entries)) - {"info.json"}):
            old = _decode(archive.read(old_entries[key])) if key in old_entries else ""
            new = _decode(archive.read(new_entries[key])) if key in new_entries else ""
            if old == new:
                continue

            patches = []
            target = _target_class(key)
            changed_classes += 1
            classes.append(target)

            if key in old_entries and key not in new_entries:
                patches.append({
                    "id": _patch_id(key, "class_delete"),
                    "method": "",
                    "method_name": "",
                    "method_anchors": [],
                    "type": "class_delete",
                    "search": old,
                    "replacement": "",
                    "required": False,
                    "flag_rewrite_count": 0,
                    "reason": "Class removed by PowerKeeper comparison output.",
                })
            elif key in new_entries and key not in old_entries:
                patches.append({
                    "id": _patch_id(key, "class_add"),
                    "method": "",
                    "method_name": "",
                    "method_anchors": [],
                    "type": "class_add",
                    "search": None,
                    "replacement": new,
                    "required": True,
                    "flag_rewrite_count": 0,
                    "reason": "Class added by PowerKeeper comparison output.",
                })
            else:
                old_methods = _methods(old)
                new_methods = _methods(new)
                for sig in sorted(set(old_methods) | set(new_methods)):
                    old_block = old_methods.get(sig, "")
                    new_block = new_methods.get(sig, "")
                    if old_block == new_block:
                        continue
                    changed_methods += 1
                    name = _method_name(sig)
                    if not old_block and new_block:
                        patch_type = "method_add"
                        sig = new_block.split("\n", 1)[0].strip()
                        name = _method_name(sig)
                    elif old_block and not new_block:
                        patch_type = "method_delete"
                    else:
                        patch_type = "method_replace"

                    rewrite_count = _flag_rewrite_count(old_block, new_block)
                    flag_rewrites += rewrite_count
                    combined = f"{old_block}\n{new_block}"
                    if "lock_max_fps_mezo" in combined or "SettingsMezoHelper" in combined:
                        lock_detected = True
                    if (
                        key == "com/miui/powerkeeper/utils/GmsObserver"
                        and name == "isGmsControlEnabled"
                        and re.search(r"const/4\s+p?\d*,\s+0x0[\s\S]*return\s+p?\d*", new_block)
                    ):
                        gms_detected = True

                    patches.append({
                        "id": _patch_id(key, name),
                        "method": sig,
                        "method_name": name,
                        "method_anchors": _anchors(old_block or new_block),
                        "type": patch_type,
                        "search": old_block or None,
                        "replacement": new_block,
                        "required": True,
                        "flag_rewrite_count": rewrite_count,
                        "reason": "PowerKeeper smali rule generated from comparison output.",
                    })
                    methods.append({"class": target, "method": sig})

            module_name = f"{_safe_module_name(key)}.py"
            modules.append(module_name)
            lines = [
                f"TARGET_APK = {_q(TARGET_APK)}",
                f"TARGET_CLASS = {_q(target)}",
                f"CLASS_FALLBACK_NAMES = {_q([Path(target).name])}",
                f"CLASS_ANCHORS = {_q(_class_anchors(new or old))}",
                "",
                "PATCHES = [",
            ]
            for patch in patches:
                lines.append("    {")
                for patch_key, value in patch.items():
                    if patch_key in {"search", "replacement"} and isinstance(value, str):
                        lines.append(f"        {_q(patch_key)}: {_triple(value)},")
                    else:
                        lines.append(f"        {_q(patch_key)}: {_q(value)},")
                lines.append("    },")
            lines.append("]")
            (smali_dir / module_name).write_text("\n".join(lines) + "\n", encoding="utf-8")

    return {
        "changed_classes": changed_classes,
        "changed_methods": changed_methods,
        "classes": classes,
        "methods": methods,
        "build_flag_rewrite_count": flag_rewrites,
        "lock_max_fps_mezo_detected": lock_detected,
        "gms_force_false_detected": gms_detected,
        "modules": modules,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Legend PowerKeeper patch rules")
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    source = _resolve_input(args.input)
    inventory = generate(source, args.out_dir)
    print("changed classes count:", inventory["changed_classes"])
    print("changed methods count:", inventory["changed_methods"])
    print("classes list:")
    for item in inventory["classes"]:
        print(" -", item)
    print("methods list:")
    for item in inventory["methods"]:
        print(f" - {item['class']} :: {item['method']}")
    print("build flag rewrite count:", inventory["build_flag_rewrite_count"])
    print("lock_max_fps_mezo patch detected:", "yes" if inventory["lock_max_fps_mezo_detected"] else "no")
    print("GmsObserver force false patch detected:", "yes" if inventory["gms_force_false_detected"] else "no")
    print("proposed Python module per changed class:")
    for class_name, module in zip(inventory["classes"], inventory["modules"]):
        print(f" - {class_name} -> {args.out_dir / 'smali' / module}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
