"""
One-time generator: reads Legend/MiuiSystemUI/compare/*.mtcr and
Legend/MiuiSystemUI/add/ then produces clean Python rule files under:
  factory/patch/legend/systemui/smali/          (115 modified classes)
  factory/patch/legend/systemui/smali_added/    (313 added classes)
  factory/patch/legend/systemui/resources/      (layout + arsc + values rules)
  factory/patch/legend/systemui/dex/            (dex payload declarations)
  factory/patch/legend/assets/systemui/         (managed add/ XML assets + dex)

Run once from repo root:
  python -m factory.patch.legend.systemui._generator_from_mtcr
"""
from __future__ import annotations

import re
import json
import shutil
import zipfile
from pathlib import Path
from typing import Optional


REPO_ROOT   = Path(__file__).resolve().parents[4]
MTCR_DIR    = REPO_ROOT / "Legend" / "MiuiSystemUI" / "compare"
ADD_DIR     = REPO_ROOT / "Legend" / "MiuiSystemUI" / "add"
OUT_ROOT    = REPO_ROOT / "factory" / "patch" / "legend" / "systemui"
ASSETS_ROOT = REPO_ROOT / "factory" / "patch" / "legend" / "assets" / "systemui"

TARGET_APK = "MiuiSystemUI.apk"

# Added-class grouping: bg/mods/* → classes4; com/justas/+com/miui/* → classes3; rest → classes2
def _dex_group_for(class_path: str) -> str:
    if class_path.startswith("bg/mods/"):
        return "classes4"
    top2 = "/".join(class_path.split("/")[:3])
    if top2 in ("com/justas/AnimationWeather", "com/miui/charge", "com/miui/systemui"):
        return "classes3"
    return "classes2"


# ---------------------------------------------------------------------------
# Smali helpers
# ---------------------------------------------------------------------------

def _parse_smali_methods(text: str) -> list[tuple[str, str]]:
    """Return [(sig_line, full_body), ...] preserving original text."""
    methods: list[tuple[str, str]] = []
    lines = text.splitlines(keepends=True)
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith(".method "):
            sig = stripped
            j = i + 1
            depth = 1
            while j < len(lines):
                inner = lines[j].strip()
                if inner.startswith(".method "):
                    depth += 1
                if ".end method" in lines[j]:
                    depth -= 1
                    if depth == 0:
                        body = "".join(lines[i : j + 1])
                        methods.append((sig, body))
                        i = j + 1
                        break
                j += 1
            else:
                i += 1
        else:
            i += 1
    return methods


def _parse_smali_fields(text: str) -> list[str]:
    return [l.strip() for l in text.splitlines() if l.strip().startswith(".field ")]


def _extract_class_anchors(text: str, n: int = 5) -> list[str]:
    """Stable class-level type/invoke refs for Tier-3 class matching."""
    anchors: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith(".") or not s:
            continue
        if re.search(r"L[a-zA-Z][a-zA-Z0-9_/]+;", s):
            if "->" in s or "invoke" in s or "sget" in s or "iget" in s:
                anchors.append(s)
        if len(anchors) >= n:
            break
    return anchors


def _extract_method_anchors(body: str, n: int = 3) -> list[str]:
    anchors: list[str] = []
    for line in body.splitlines():
        s = line.strip()
        if "L" in s and ("->" in s or "invoke" in s) and not s.startswith("."):
            anchors.append(s)
        if len(anchors) >= n:
            break
    return anchors


def _method_name(sig: str) -> str:
    m = re.search(r"\s(\S+)\(", sig)
    return m.group(1) if m else "unknown"


def _safe_embed(s: str) -> str:
    """Escape content for embedding in a Python triple-quoted string."""
    return s.replace("\\", "\\\\").replace('"""', '""\\"')


def _class_filename(class_path: str) -> str:
    """Convert class path to a safe Python filename."""
    name = class_path.replace("/", "_").replace("$", "__").replace("-", "_")
    if len(name) > 120:
        # Truncate long names but keep extension
        name = name[:115] + "_etc"
    return name + ".py"


def _make_patch_id(idx: int, method_name: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9_]", "_", method_name)[:40]
    return f"p{idx:04d}_{safe}"


# ---------------------------------------------------------------------------
# Generate smali/ files for modified classes (115)
# ---------------------------------------------------------------------------

def gen_smali_modified(pack: dict) -> None:
    out_dir = OUT_ROOT / "smali"
    out_dir.mkdir(parents=True, exist_ok=True)

    a_set = set(pack["a"].keys())
    b_set = set(pack["b"].keys())
    modified = sorted(a_set & b_set)

    print(f"[gen] smali/ modified: {len(modified)} classes")
    count = 0

    for class_path in modified:
        a_text = pack["a"][class_path]
        b_text = pack["b"][class_path]

        a_methods = dict(_parse_smali_methods(a_text))
        b_methods_list = _parse_smali_methods(b_text)
        a_fields = set(_parse_smali_fields(a_text))
        b_fields = _parse_smali_fields(b_text)

        patches: list[dict] = []
        idx = 0

        # Changed or added methods
        for sig, b_body in b_methods_list:
            if sig in a_methods:
                a_body = a_methods[sig]
                if a_body.strip() == b_body.strip():
                    continue  # unchanged
                method_anchors = _extract_method_anchors(b_body)
                patches.append({
                    "id": _make_patch_id(idx, _method_name(sig)),
                    "type": "method_replace",
                    "method": sig,
                    "method_name": _method_name(sig),
                    "method_anchors": method_anchors,
                    "search": a_body,
                    "replacement": b_body,
                    "required": True,
                    "reason": "Legend MiuiSystemUI MTCR dex.mtcr modified class",
                })
            else:
                method_anchors = _extract_method_anchors(b_body)
                patches.append({
                    "id": _make_patch_id(idx, _method_name(sig)),
                    "type": "method_add",
                    "method": sig,
                    "method_name": _method_name(sig),
                    "method_anchors": method_anchors,
                    "search": None,
                    "replacement": b_body,
                    "required": False,
                    "reason": "Legend MiuiSystemUI MTCR dex.mtcr added method",
                })
            idx += 1

        # Added fields (in b/ but not in a/)
        for field_line in b_fields:
            if field_line not in a_fields:
                patches.append({
                    "id": _make_patch_id(idx, "field_" + re.sub(r"[^a-zA-Z0-9]", "_", field_line)[:20]),
                    "type": "field_add",
                    "method": field_line,
                    "method_name": "",
                    "method_anchors": [],
                    "search": None,
                    "replacement": field_line,
                    "required": False,
                    "reason": "Legend MiuiSystemUI MTCR dex.mtcr added field",
                })
                idx += 1

        if not patches:
            continue

        class_anchors = _extract_class_anchors(b_text)
        basename = class_path.split("/")[-1] + ".smali"
        fname = _class_filename(class_path)

        lines: list[str] = [
            '"""',
            f"Legend MiuiSystemUI MTCR patch — modified class.",
            f"",
            f"Target APK   : {TARGET_APK}",
            f"Target class : {class_path}.smali",
            f"Patches      : {len(patches)}",
            f'"""',
            "from __future__ import annotations",
            "",
            f"TARGET_APK           = {TARGET_APK!r}",
            f"TARGET_CLASS         = {class_path + '.smali'!r}",
            f"CLASS_FALLBACK_NAMES = {[basename]!r}",
            f"CLASS_ANCHORS        = {class_anchors!r}",
            "",
            "PATCHES = [",
        ]

        for p in patches:
            lines.append("    {")
            lines.append(f"        'id':             {p['id']!r},")
            lines.append(f"        'type':           {p['type']!r},")
            lines.append(f"        'method':         {p['method']!r},")
            lines.append(f"        'method_name':    {p['method_name']!r},")
            lines.append(f"        'method_anchors': {p['method_anchors']!r},")
            if p["search"] is not None:
                lines.append(f"        'search':         {p['search']!r},")
            else:
                lines.append(f"        'search':         None,")
            lines.append(f"        'replacement':    {p['replacement']!r},")
            lines.append(f"        'required':       {p['required']!r},")
            lines.append(f"        'reason':         {p['reason']!r},")
            lines.append("    },")

        lines.append("]")
        lines.append("")

        (out_dir / fname).write_text("\n".join(lines), encoding="utf-8")
        count += 1

    print(f"[gen] smali/ written: {count} files")


# ---------------------------------------------------------------------------
# Generate smali_added/ files for added classes (313)
# ---------------------------------------------------------------------------

def gen_smali_added(pack: dict) -> None:
    a_set = set(pack["a"].keys())
    b_set = set(pack["b"].keys())
    added = sorted(b_set - a_set)

    print(f"[gen] smali_added/: {len(added)} classes")

    groups: dict[str, list[str]] = {}
    for cls in added:
        g = _dex_group_for(cls)
        groups.setdefault(g, []).append(cls)

    for group, classes in groups.items():
        out_dir = OUT_ROOT / "smali_added" / group
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "__init__.py").touch()

    count = 0
    for class_path in added:
        group = _dex_group_for(class_path)
        out_dir = OUT_ROOT / "smali_added" / group
        b_text = pack["b"][class_path]
        basename = class_path.split("/")[-1] + ".smali"
        fname = _class_filename(class_path)

        lines: list[str] = [
            '"""',
            f"Legend MiuiSystemUI MTCR patch — added class.",
            f"",
            f"Target APK   : {TARGET_APK}",
            f"Target class : {class_path}.smali",
            f"DEX group    : {group}",
            f'"""',
            "from __future__ import annotations",
            "",
            f"TARGET_APK           = {TARGET_APK!r}",
            f"TARGET_CLASS         = {class_path + '.smali'!r}",
            f"CLASS_FALLBACK_NAMES = {[basename]!r}",
            f"DEX_GROUP            = {group!r}",
            "",
            "PATCHES = [",
            "    {",
            "        'id':          " + repr("class_add_" + re.sub("/", "_", class_path)[:60]) + ",",
            f"        'type':        'class_add',",
            f"        'method':      '',",
            f"        'method_name': '',",
            f"        'search':      None,",
            f"        'replacement': {b_text!r},",
            f"        'required':    True,",
            f"        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',",
            "    },",
            "]",
            "",
        ]

        (out_dir / fname).write_text("\n".join(lines), encoding="utf-8")
        count += 1

    print(f"[gen] smali_added/ written: {count} files")


# ---------------------------------------------------------------------------
# Generate resources/layout_rules.py (xml.mtcr — 20 layouts)
# ---------------------------------------------------------------------------

def gen_layout_rules(xml_pack: dict) -> None:
    out_dir = OUT_ROOT / "resources"
    out_dir.mkdir(parents=True, exist_ok=True)

    a_set = set(xml_pack["a"].keys())
    b_set = set(xml_pack["b"].keys())
    modified = sorted(a_set & b_set)
    added_only = sorted(b_set - a_set)

    print(f"[gen] layout_rules.py: {len(modified)} modified, {len(added_only)} added layouts")

    lines: list[str] = [
        '"""',
        "Legend MiuiSystemUI layout XML patch rules.",
        "",
        "Extracted from compare/xml.mtcr.",
        "Each entry provides a_text (original) and b_text (modified).",
        "Runner applies text-diff hunks: find a_block in target, replace with b_block.",
        "",
        f"Modified layouts : {len(modified)}",
        f"Added layouts    : {len(added_only)}",
        '"""',
        "from __future__ import annotations",
        "",
        "TARGET_APK = 'MiuiSystemUI.apk'",
        "",
        "# Modified layout rules: {layout_name: {a_text, b_text}}",
        "MODIFIED_LAYOUTS: dict = {",
    ]

    for layout_path in modified:
        layout_name = Path(layout_path).name
        a_text = xml_pack["a"][layout_path]
        b_text = xml_pack["b"][layout_path]
        lines.append(f"    {layout_name!r}: {{")
        lines.append(f"        'path':   {layout_path!r},")
        lines.append(f"        'a_text': {a_text!r},")
        lines.append(f"        'b_text': {b_text!r},")
        lines.append(f"        'required': True,")
        lines.append(f"        'reason': 'Legend MiuiSystemUI MTCR xml.mtcr layout change',")
        lines.append("    },")

    lines.append("}")
    lines.append("")

    lines.append("# Added layout files (only in b/)")
    lines.append("ADDED_LAYOUTS: dict = {")
    for layout_path in added_only:
        layout_name = Path(layout_path).name
        b_text = xml_pack["b"][layout_path]
        lines.append(f"    {layout_name!r}: {{")
        lines.append(f"        'path':    {layout_path!r},")
        lines.append(f"        'content': {b_text!r},")
        lines.append(f"        'required': False,")
        lines.append(f"        'reason': 'Legend MiuiSystemUI MTCR xml.mtcr added layout',")
        lines.append("    },")
    lines.append("}")
    lines.append("")

    (out_dir / "layout_rules.py").write_text("\n".join(lines), encoding="utf-8")
    print(f"[gen] layout_rules.py written")


# ---------------------------------------------------------------------------
# Generate resources/arsc_rules.py (arsc.mtcr — 20 modified + 140 added)
# ---------------------------------------------------------------------------

def gen_arsc_rules(arsc_pack: dict) -> None:
    out_dir = OUT_ROOT / "resources"
    out_dir.mkdir(parents=True, exist_ok=True)

    a_set = set(arsc_pack["a"].keys())
    b_set = set(arsc_pack["b"].keys())
    modified = sorted(a_set & b_set)
    added_only = sorted(b_set - a_set)

    print(f"[gen] arsc_rules.py: {len(modified)} modified, {len(added_only)} added groups")

    lines: list[str] = [
        '"""',
        "Legend MiuiSystemUI arsc resource patch rules.",
        "",
        "Extracted from compare/arsc.mtcr.",
        "Each entry provides a_text (original XML) and b_text (modified XML).",
        "Runner merges resource values into the decompiled APK res/values*/ dirs.",
        "",
        f"Modified groups : {len(modified)}",
        f"Added groups    : {len(added_only)}",
        '"""',
        "from __future__ import annotations",
        "",
        "TARGET_APK = 'MiuiSystemUI.apk'",
        "",
        "# Modified resource groups: apply only when target matches a_text",
        "MODIFIED_GROUPS: dict = {",
    ]

    for entry_path in modified:
        a_text = arsc_pack["a"][entry_path]
        b_text = arsc_pack["b"][entry_path]
        lines.append(f"    {entry_path!r}: {{")
        lines.append(f"        'a_text': {a_text!r},")
        lines.append(f"        'b_text': {b_text!r},")
        lines.append(f"        'required': True,")
        lines.append(f"        'reason': 'Legend MiuiSystemUI MTCR arsc.mtcr modified group',")
        lines.append("    },")

    lines.append("}")
    lines.append("")
    lines.append("# Added resource groups: merge into target if not present")
    lines.append("ADDED_GROUPS: dict = {")

    for entry_path in added_only:
        b_text = arsc_pack["b"][entry_path]
        lines.append(f"    {entry_path!r}: {{")
        lines.append(f"        'b_text': {b_text!r},")
        lines.append(f"        'required': False,")
        lines.append(f"        'reason': 'Legend MiuiSystemUI MTCR arsc.mtcr added group',")
        lines.append("    },")

    lines.append("}")
    lines.append("")

    (out_dir / "arsc_rules.py").write_text("\n".join(lines), encoding="utf-8")
    print(f"[gen] arsc_rules.py written")


# ---------------------------------------------------------------------------
# Copy add/ resource XMLs to factory/assets/ and generate values_rules.py
# ---------------------------------------------------------------------------

def gen_values_rules() -> None:
    src_dir = ADD_DIR / "com.android.systemui"
    if not src_dir.is_dir():
        print(f"[gen] WARNING: add/com.android.systemui not found: {src_dir}")
        return

    assets_res_dir = ASSETS_ROOT / "resources" / "com.android.systemui"
    assets_res_dir.mkdir(parents=True, exist_ok=True)

    # Copy all resource XMLs to assets
    total = 0
    type_counts: dict[str, int] = {}
    for type_dir in sorted(src_dir.iterdir()):
        if not type_dir.is_dir():
            continue
        dst_type_dir = assets_res_dir / type_dir.name
        dst_type_dir.mkdir(parents=True, exist_ok=True)
        for xml_file in sorted(type_dir.glob("*.xml")):
            shutil.copy2(xml_file, dst_type_dir / xml_file.name)
            type_counts[type_dir.name] = type_counts.get(type_dir.name, 0) + 1
            total += 1

    print(f"[gen] Copied {total} add/ XMLs to factory/patch/legend/assets/systemui/resources/")
    for t, c in sorted(type_counts.items()):
        print(f"        {t}: {c} files")

    # Generate values_rules.py that declares the managed asset path
    out_dir = OUT_ROOT / "resources"
    out_dir.mkdir(parents=True, exist_ok=True)

    lines: list[str] = [
        '"""',
        "Legend MiuiSystemUI add/ resource values rules.",
        "",
        "Points to managed factory assets at:",
        "  factory/patch/legend/assets/systemui/resources/com.android.systemui/",
        "",
        "Runner merges all XML files from this asset path into the decompiled APK",
        "using the same logic as the original apply_add_resources().",
        "",
        f"Total XML files : {total}",
    ]
    for t, c in sorted(type_counts.items()):
        lines.append(f"  {t:<12}: {c}")
    lines += [
        '"""',
        "from __future__ import annotations",
        "from pathlib import Path",
        "",
        "TARGET_APK = 'MiuiSystemUI.apk'",
        "",
        "_HERE = Path(__file__).resolve().parent",
        "_REPO_ROOT = _HERE.parents[4]",
        "",
        "# Managed asset root — do NOT read from Legend/ at runtime",
        "ASSETS_ROOT = _REPO_ROOT / 'factory' / 'patch' / 'legend' / 'assets' / 'systemui' / 'resources'",
        "ADD_RESOURCES_SRC = ASSETS_ROOT / 'com.android.systemui'",
        "",
        f"RESOURCE_TYPES = {sorted(type_counts.keys())!r}",
        "",
        f"RESOURCE_FILE_COUNTS = {type_counts!r}",
        "",
        "REQUIRED = True",
        "REASON   = 'Legend MiuiSystemUI managed resource additions'",
        "",
    ]

    (out_dir / "values_rules.py").write_text("\n".join(lines), encoding="utf-8")
    print(f"[gen] values_rules.py written")


# ---------------------------------------------------------------------------
# Copy classes*.dex to factory/assets/ and generate dex/add_dex_payloads.py
# ---------------------------------------------------------------------------

def gen_dex_payloads() -> None:
    dex_assets_dir = ASSETS_ROOT / "dex"
    dex_assets_dir.mkdir(parents=True, exist_ok=True)

    payloads: list[dict] = []
    for dex_name in ("classes2.dex", "classes3.dex", "classes4.dex"):
        src = ADD_DIR / dex_name
        if src.is_file():
            shutil.copy2(src, dex_assets_dir / dex_name)
            size = src.stat().st_size
            payloads.append({"name": dex_name, "size": size})
            print(f"[gen] Copied {dex_name} ({size} bytes) -> factory/patch/legend/assets/systemui/dex/")
        else:
            print(f"[gen] WARNING: {dex_name} not found in add/")

    out_dir = OUT_ROOT / "dex"
    out_dir.mkdir(parents=True, exist_ok=True)

    lines: list[str] = [
        '"""',
        "Legend MiuiSystemUI DEX payload rules.",
        "",
        "Declares managed factory assets for classes2.dex, classes3.dex, classes4.dex.",
        "These dex files contain added classes that are merged into the APK as new",
        "smali_classesN roots during build.",
        "",
        "Runtime behavior:",
        "  1. Detect existing smali roots in the decompiled APK workspace.",
        "  2. For each payload, decode dex → smali using baksmali.",
        "  3. Place decoded smali into the next available smali_classesN root.",
        "  4. APKEditor rebuild auto-generates classesN.dex from each smali root.",
        "",
        "Do NOT copy raw .dex files into the APK manually.",
        '"""',
        "from __future__ import annotations",
        "from pathlib import Path",
        "",
        "TARGET_APK = 'MiuiSystemUI.apk'",
        "",
        "_HERE = Path(__file__).resolve().parent",
        "_REPO_ROOT = _HERE.parents[5]",
        "",
        "ASSETS_DEX_DIR = _REPO_ROOT / 'factory' / 'assets' / 'legend' / 'systemui' / 'dex'",
        "",
        "DEX_PAYLOADS = [",
    ]

    for p in payloads:
        smali_group = p["name"].replace(".dex", "")  # e.g. classes2
        lines += [
            "    {",
            f"        'name':        {p['name']!r},",
            f"        'asset_path':  ASSETS_DEX_DIR / {p['name']!r},",
            f"        'smali_group': {smali_group!r},",
            f"        'size_bytes':  {p['size']},",
            f"        'required':    True,",
            f"        'reason':      'Legend MiuiSystemUI managed dex payload',",
            "    },",
        ]

    lines += [
        "]",
        "",
        "# These packages are introduced by the dex payloads.",
        "# Used for reporting and validation.",
        "PAYLOAD_PACKAGE_GROUPS = {",
        "    'classes2': ['com/android/systemui'],",
        "    'classes3': ['com/justas', 'com/miui/charge', 'com/miui/systemui'],",
        "    'classes4': ['bg/mods'],",
        "}",
        "",
    ]

    (out_dir / "add_dex_payloads.py").write_text("\n".join(lines), encoding="utf-8")
    print(f"[gen] add_dex_payloads.py written")


# ---------------------------------------------------------------------------
# Read MTCR packs
# ---------------------------------------------------------------------------

def _read_mtcr(path: Path) -> dict:
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        a: dict[str, str] = {}
        b: dict[str, str] = {}
        for name in names:
            if name == "info.json":
                continue
            if name.startswith("a/"):
                a[name[2:]] = z.read(name).decode("utf-8", errors="replace")
            elif name.startswith("b/"):
                b[name[2:]] = z.read(name).decode("utf-8", errors="replace")
    return {"a": a, "b": b}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("Legend MiuiSystemUI rule generator")
    print("=" * 60)

    dex_mtcr  = MTCR_DIR / "dex.mtcr"
    xml_mtcr  = MTCR_DIR / "xml.mtcr"
    arsc_mtcr = MTCR_DIR / "arsc.mtcr"

    print(f"Reading dex.mtcr  ...")
    dex_pack  = _read_mtcr(dex_mtcr)
    print(f"Reading xml.mtcr  ...")
    xml_pack  = _read_mtcr(xml_mtcr)
    print(f"Reading arsc.mtcr ...")
    arsc_pack = _read_mtcr(arsc_mtcr)

    gen_smali_modified(dex_pack)
    gen_smali_added(dex_pack)
    gen_layout_rules(xml_pack)
    gen_arsc_rules(arsc_pack)
    gen_values_rules()
    gen_dex_payloads()

    print("")
    print("=" * 60)
    print("Generation complete.")
    print(f"smali/         -> {OUT_ROOT / 'smali'}")
    print(f"smali_added/   -> {OUT_ROOT / 'smali_added'}")
    print(f"resources/     -> {OUT_ROOT / 'resources'}")
    print(f"dex/           -> {OUT_ROOT / 'dex'}")
    print(f"assets/        -> {ASSETS_ROOT}")
    print("=" * 60)


if __name__ == "__main__":
    main()
