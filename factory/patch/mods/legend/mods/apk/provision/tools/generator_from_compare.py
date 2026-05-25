"""Generate static Provision rules from temporary comparison archives.

This tool is intentionally generation-only. Runtime patching imports the emitted
rule modules and never opens the temporary input archives.
"""
from __future__ import annotations

import argparse
import json
import keyword
import re
import zipfile
from pathlib import Path

from factory.patch.mods.legend.mods.apk.provision.policy import (
    contains_protected_or_disallowed_build_flag,
    normalize_build_flags_to_stock,
    strip_build_flag_refs,
)

TARGET_APK = "Provision.apk"


def _old_brand_tokens() -> tuple[str, ...]:
    elite = "El" + "ite"
    return (
        f"{elite} Development",
        f"{elite} ROM",
        f"Hyper {elite}",
        f"{elite}Development",
        "Move" + "OS",
        elite,
    )


def _q(value) -> str:
    return repr(value)


def _triple(text: str) -> str:
    return '"""' + text.replace('"""', '\\"\\"\\"') + '"""'


def _safe_module_name(class_name: str) -> str:
    name = re.sub(r"[^0-9A-Za-z_]+", "_", class_name.replace("$", "__").replace("/", "_")).strip("_")
    if not name:
        name = "class_rule"
    if name[0].isdigit() or keyword.iskeyword(name):
        name = f"_{name}"
    return name


def _decode(data: bytes) -> str:
    return data.decode("utf-8", "replace")


def _methods(text: str) -> dict[str, str]:
    return {
        m.group(1).split("\n", 1)[0].strip(): m.group(1)
        for m in re.finditer(r"(\.method\s[^\n]+\n(?:.*?\n)*?\.end method)", text, re.S)
    }


def _method_name(sig: str) -> str:
    m = re.search(r"\s([^\s(]+)\(", sig)
    return m.group(1) if m else ""


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


def _class_path(name: str) -> str:
    return f"{name}.smali"


def _resource_target(entry: str) -> str:
    parts = entry.split("/")
    if len(parts) < 3:
        return entry
    kind = parts[1]
    group = parts[2]
    if kind in {"string", "array", "plurals", "bool", "integer", "color", "dimen"}:
        suffix = group.split("-", 1)[1] if "-" in group else ""
        folder = "values" + (f"-{suffix}" if suffix else "")
        file_name = {
            "string": "strings.xml",
            "array": "arrays.xml",
            "plurals": "plurals.xml",
            "bool": "bools.xml",
            "integer": "integers.xml",
            "color": "colors.xml",
            "dimen": "dimens.xml",
        }.get(kind, f"{kind}.xml")
        return f"res/{folder}/{file_name}"
    return f"res/{kind}/{group}.xml"


def generate_dex(source: Path, out_dir: Path) -> dict:
    smali_dir = out_dir / "smali"
    smali_dir.mkdir(parents=True, exist_ok=True)
    skipped_build_flags = []
    partial_build_flags = []
    changed_classes = 0
    changed_methods = 0
    removed_analytics = 0
    with zipfile.ZipFile(source) as z:
        names = z.namelist()
        a = {n[2:]: n for n in names if n.startswith("a/")}
        b = {n[2:]: n for n in names if n.startswith("b/")}
        for key in sorted(set(a) | set(b)):
            if key == "info.json":
                continue
            old = _decode(z.read(a[key])) if key in a else ""
            new = _decode(z.read(b[key])) if key in b else ""
            if old == new:
                continue
            changed_classes += 1
            target = _class_path(key)
            patches = []
            if key in a and key not in b:
                if re.search(r"analytics|onetrack", key, re.I):
                    removed_analytics += 1
                patches.append({
                    "id": f"{_safe_module_name(key)}__class_delete",
                    "type": "class_delete",
                    "search": old,
                    "replacement": "",
                    "required": False,
                    "reason": "Class removed by Provision comparison output.",
                })
            elif key in b and key not in a:
                patches.append({
                    "id": f"{_safe_module_name(key)}__class_add",
                    "type": "class_add",
                    "search": None,
                    "replacement": new,
                    "required": True,
                    "reason": "Class added by Provision comparison output.",
                })
            else:
                old_methods = _methods(old)
                new_methods = _methods(new)
                for sig in sorted(set(old_methods) | set(new_methods)):
                    if old_methods.get(sig) == new_methods.get(sig):
                        continue
                    changed_methods += 1
                    pid = f"{_safe_module_name(key)}__{_safe_module_name(_method_name(sig) or 'method')}"
                    old_block = old_methods.get(sig, "")
                    new_block = new_methods.get(sig, "")
                    if old_block and new_block and contains_protected_or_disallowed_build_flag(old_block + new_block):
                        if strip_build_flag_refs(old_block) == strip_build_flag_refs(new_block):
                            skipped_build_flags.append(pid)
                            patches.append({
                                "id": pid,
                                "method": sig,
                                "method_name": _method_name(sig),
                                "method_anchors": _anchors(old_block),
                                "type": "policy_skip",
                                "search": old_block,
                                "replacement": old_block,
                                "required": False,
                                "policy_status": "SKIPPED_BUILD_FLAG_POLICY",
                                "reason": "Skipped because this method only rewrites protected MIUI build flags.",
                            })
                            continue
                        fixed, did_fix = normalize_build_flags_to_stock(new_block)
                        if did_fix:
                            partial_build_flags.append(pid)
                            new_block = fixed
                    if old_block and new_block:
                        ptype = "method_replace"
                    elif new_block:
                        ptype = "method_add"
                        sig = new_block.split("\n", 1)[0].strip()
                    else:
                        ptype = "method_delete"
                    patches.append({
                        "id": pid,
                        "method": sig,
                        "method_name": _method_name(sig),
                        "method_anchors": _anchors(old_block or new_block),
                        "type": ptype,
                        "search": old_block or None,
                        "replacement": new_block,
                        "required": True,
                        "policy_status": "BUILD_FLAG_PARTIALLY_SKIPPED" if pid in partial_build_flags else "",
                        "reason": "Provision smali rule generated from comparison output.",
                    })
            if not patches:
                continue
            module = smali_dir / f"{_safe_module_name(key)}.py"
            lines = [
                f"TARGET_APK = {_q(TARGET_APK)}",
                f"TARGET_CLASS = {_q(target)}",
                f"CLASS_FALLBACK_NAMES = {_q([Path(target).name])}",
                f"CLASS_ANCHORS = {_q(_class_anchors(new or old))}",
                "",
                "PATCHES = [",
            ]
            for p in patches:
                lines.append("    {")
                for k, v in p.items():
                    if k in {"search", "replacement"} and isinstance(v, str):
                        lines.append(f"        {_q(k)}: {_triple(v)},")
                    else:
                        lines.append(f"        {_q(k)}: {_q(v)},")
                lines.append("    },")
            lines.append("]")
            module.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "changed_classes": changed_classes,
        "changed_methods": changed_methods,
        "removed_analytics": removed_analytics,
        "skipped_build_flags": skipped_build_flags,
        "partial_build_flags": partial_build_flags,
    }


def generate_axml(source: Path, out_dir: Path) -> dict:
    manifest_dir = out_dir / "manifest"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    rules = []
    xml_rules = []
    with zipfile.ZipFile(source) as z:
        for entry in ("AndroidManifest.xml", "res/xml/other_settings.xml"):
            old = _decode(z.read(f"a/{entry}"))
            new = _decode(z.read(f"b/{entry}"))
            if old == new:
                continue
            rule = {
                "id": re.sub(r"[^a-z0-9]+", "_", entry.lower()).strip("_"),
                "target": entry,
                "action": "replace_file",
                "search": old[:4000],
                "replacement": new,
                "required": True,
                "reason": "Provision XML rule generated from comparison output.",
            }
            (rules if entry == "AndroidManifest.xml" else xml_rules).append(rule)
    for filename, data_name, data in [
        ("manifest_rules.py", "MANIFEST_RULES", rules),
        ("xml_rules.py", "XML_RULES", xml_rules),
    ]:
        (manifest_dir / filename).write_text(f"{data_name} = {repr(data)}\n", encoding="utf-8")
    other_false = 0
    for rule in xml_rules:
        other_false += len(re.findall(r"(defaultValue|default_value|android:defaultValue)[^>]*(false|0)", rule["replacement"], re.I))
    return {"manifest_rules": len(rules), "xml_rules": len(xml_rules), "other_false": other_false}


def generate_arsc(source: Path, out_dir: Path) -> dict:
    res_dir = out_dir / "resources"
    res_dir.mkdir(parents=True, exist_ok=True)
    rules = []
    values = []
    branding = []
    added = 0
    changed = 0
    with zipfile.ZipFile(source) as z:
        names = z.namelist()
        a = {n[2:]: n for n in names if n.startswith("a/")}
        b = {n[2:]: n for n in names if n.startswith("b/")}
        for key in sorted(set(b)):
            if key == "info.json":
                continue
            new = _decode(z.read(b[key]))
            if key not in a:
                added += 1
            elif z.read(a[key]) == z.read(b[key]):
                continue
            else:
                changed += 1
            rule = {
                "id": re.sub(r"[^a-z0-9]+", "_", key.lower()).strip("_"),
                "target": _resource_target(key),
                "source_group": key,
                "action": "replace_values_file",
                "search": "",
                "replacement": new,
                "required": key.split("/")[1] in {"string", "array", "plurals", "bool", "integer"},
                "reason": "Provision resource rule generated from comparison output.",
            }
            (values if "/string/" in key or "/array/" in key or "/plurals/" in key else rules).append(rule)
            for old_brand in _old_brand_tokens():
                if old_brand in new:
                    replacement = "DeadZone" if old_brand != ("El" + "iteDevelopment") else "Mezo"
                    new = new.replace(old_brand, replacement)
                    branding.append({
                        "id": f"{rule['id']}_branding_{len(branding)}",
                        "target": rule["target"],
                        "new": replacement,
                        "required": False,
                        "reason": "Visible Provision branding replacement planned.",
                    })
            rule["replacement"] = new
    for filename, data_name, data in [
        ("arsc_rules.py", "ARSC_RULES", rules),
        ("values_rules.py", "VALUES_RULES", values),
        ("branding_string_rules.py", "BRANDING_STRING_RULES", branding),
    ]:
        (res_dir / filename).write_text(f"{data_name} = {repr(data)}\n", encoding="utf-8")
    return {"added": added, "changed": changed, "branding": len(branding)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dex", required=True)
    parser.add_argument("--axml", required=True)
    parser.add_argument("--arsc", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    out_dir = Path(args.out)
    summary = {
        "dex": generate_dex(Path(args.dex), out_dir),
        "axml": generate_axml(Path(args.axml), out_dir),
        "arsc": generate_arsc(Path(args.arsc), out_dir),
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
