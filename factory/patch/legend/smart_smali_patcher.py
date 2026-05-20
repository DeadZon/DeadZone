"""
Smart smali patcher — multi-tier class/method matching with register/label tolerance.

Architecture
============
Class matching tiers:
  Tier 1 — Exact path         : TARGET_CLASS resolved directly under each smali_root.
  Tier 2 — Basename           : any *.smali whose filename matches CLASS_FALLBACK_NAMES.
  Tier 3 — Class anchors      : any *.smali containing ALL class_anchors (stable verbatim refs).
  Tier 4 — Method-anchor refs : stable class/member refs extracted from method_anchors; any
                                 *.smali containing ALL of them.  Requires exactly 1 hit.

  AMBIGUOUS = FAIL at every tier: > 1 candidate → ClassMatchStatus.AMBIGUOUS, abort.
  If all four tiers fail     → ClassMatchStatus.NOT_FOUND.

Method matching tiers:
  Tier 1 — Exact signature : full ".method …" line matches exactly.
  Tier 2 — Method name     : method name part matches (signature may differ; overloads → AMBIGUOUS).
  Tier 3 — Body anchors    : method body contains all method_anchors.

Smali register / label tolerance:
  Registers v0–v15 / p0–p15 are wildcard-matched ([vp]\\d+).
  Labels :cond_* / :goto_* / :pswitch_* / :sswitch_* are wildcard-matched.
  .line N directives are stripped before comparison.

Stable refs (for Tier 3 CLASS_ANCHORS and Tier 4 method-anchor extraction)
  Good: full class type refs  Lcom/android/server/policy/PhoneWindowManager;
        member refs            ->interceptKeyBeforeQueueing  ->mKeyguardDelegate
        specific invoke refs   Landroid/provider/Settings$System;->getIntForUser
  Bad:  register names v0 p0 p1, label names :cond_0 :goto_a (volatile across ROM versions)

Public API
==========
  find_class(smali_roots, exact_class, fallback_names, class_anchors, method_anchors) -> ClassMatchResult
  find_method(class_text, exact_signature, method_name, method_anchors)               -> MethodMatchResult
  apply_smart_patch(smali_roots, rule, dry_run)                                        -> PatchResult
  normalize_smali_for_match(text)                                                       -> str
  build_register_wildcard_regex(smali_block)                                            -> str
  replace_method_body(class_text, found_block, replacement)                            -> tuple[str, bool]
  insert_method_if_missing(class_text, method_block)                                   -> str
  add_class_if_missing(smali_roots, class_name, class_content)                         -> bool
  extract_anchors_from_block(smali_block, n)                                           -> list[str]
  extract_stable_refs_from_anchors(method_anchors, max_refs)                           -> list[str]
  extract_method_name(signature)                                                         -> str
  parse_smali_methods(content)                                                           -> dict[str, str]
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional


# ── Status enums ───────────────────────────────────────────────────────────────

class ClassMatchStatus(Enum):
    EXACT          = "EXACT"          # Tier 1: exact path under smali_root
    BASENAME       = "BASENAME"       # Tier 2: filename match (or fallback name)
    ANCHOR         = "ANCHOR"         # Tier 3: class_anchors all present
    METHOD_ANCHOR  = "METHOD_ANCHOR"  # Tier 4: stable refs from method_anchors all present
    NOT_FOUND      = "NOT_FOUND"
    AMBIGUOUS      = "AMBIGUOUS"      # > 1 candidate — refused to guess


class MethodMatchStatus(Enum):
    EXACT_SIG  = "EXACT_SIG"   # Tier 1: full .method line
    NAME_ONLY  = "NAME_ONLY"   # Tier 2: name matched, signature differed
    ANCHOR     = "ANCHOR"      # Tier 3: body anchors
    NOT_FOUND  = "NOT_FOUND"
    AMBIGUOUS  = "AMBIGUOUS"


class PatchApplyStatus(Enum):
    PATCHED     = "PATCHED"
    WOULD_PATCH = "WOULD_PATCH"
    EXISTS      = "EXISTS"      # method/class already present (identical)
    SKIPPED     = "SKIPPED"     # non-required and not found
    FAILED      = "FAILED"      # required but not applied


# ── Result dataclasses ─────────────────────────────────────────────────────────

@dataclass
class ClassMatchResult:
    status:     ClassMatchStatus
    path:       Optional[Path]  = None
    strategy:   str             = ""
    candidates: list[Path]      = field(default_factory=list)


@dataclass
class MethodMatchResult:
    status:     MethodMatchStatus
    block:      Optional[str]   = None   # full .method … .end method text
    strategy:   str             = ""
    candidates: list[str]       = field(default_factory=list)


@dataclass
class PatchResult:
    patch_id:        str
    method:          str
    type:            str
    status:          PatchApplyStatus
    required:        bool              = True
    class_match:     ClassMatchStatus  = ClassMatchStatus.NOT_FOUND
    method_match:    MethodMatchStatus = MethodMatchStatus.NOT_FOUND
    class_strategy:  str               = ""
    method_strategy: str               = ""
    message:         str               = ""


# ── Smali normalization ────────────────────────────────────────────────────────

_LINE_DIR_RE = re.compile(r"^\s*\.line\s+\d+\s*$", re.MULTILINE)
_REGISTER_RE = re.compile(r"\b([vp]\d+)\b")
_LABEL_RE    = re.compile(r":(cond|goto|pswitch|sswitch)_[a-z0-9]+\b")

_ANCHOR_OPCODES = frozenset({
    "invoke-virtual", "invoke-interface", "invoke-static", "invoke-direct",
    "invoke-super", "iget-object", "iget", "iput-object", "iput",
    "iget-boolean", "iput-boolean", "iget-wide", "iput-wide",
    "sget-object", "sput-object", "sget", "sput",
    "const-string", "const-class", "new-instance", "filled-new-array",
    "check-cast", "throw", "return-object", "return", "return-void",
    "move-result-object", "move-result",
    "if-eqz", "if-nez", "if-eq", "if-ne", "if-lt", "if-ge", "if-gt", "if-le",
})


# ── Stable-ref extraction (Tier 3 CLASS_ANCHORS / Tier 4 method-anchor refs) ──

# Matches any non-trivial fully-qualified smali class ref: Lcom/foo/Bar;
_STABLE_CLASS_REF_RE = re.compile(
    r"L[a-zA-Z][a-zA-Z0-9_]+(?:/[a-zA-Z$][a-zA-Z0-9_$]*){2,};"
)
# Matches ->methodOrFieldName followed by ( or :  (not a register/label)
_STABLE_MEMBER_REF_RE = re.compile(r"->([a-zA-Z_<][a-zA-Z0-9_<>]*)[\(:]")

# Ubiquitous refs that appear in almost every smali file — useless as anchors
_TRIVIAL_CLASS_REFS = frozenset({
    "Ljava/lang/Object;",
    "Ljava/lang/String;",
    "Ljava/lang/Integer;",
    "Ljava/lang/Boolean;",
    "Ljava/lang/Long;",
    "Ljava/lang/Float;",
    "Ljava/lang/Double;",
    "Ljava/lang/Runnable;",
    "Ljava/lang/Thread;",
    "Ljava/lang/Throwable;",
    "Ljava/lang/Exception;",
    "Ljava/lang/RuntimeException;",
    "Ljava/util/List;",
    "Ljava/util/ArrayList;",
    "Landroid/util/Log;",
    "Landroid/os/Bundle;",
    "Landroid/content/Context;",
    "Landroid/content/Intent;",
})

# Very short member names that appear everywhere
_TRIVIAL_MEMBER_NAMES = frozenset({
    "toString", "hashCode", "equals", "getClass", "notify", "wait",
    "init", "<init>", "<clinit>", "get", "set", "add", "put",
    "run", "call", "execute", "start", "stop",
})


def extract_stable_refs_from_anchors(
    method_anchors: list[str],
    max_refs: int = 8,
) -> list[str]:
    """
    Extract version-stable class/member reference strings from instruction-line anchors.

    Pulls ``L<pkg>/<Class>;`` type refs and ``->memberName`` refs from smali instruction
    lines, discards trivially common ones, and returns the most specific (longest) subset.

    These stable refs survive register renaming and label renaming between ROM versions,
    making them suitable for Tier 4 class-file discovery (content substring search).

    Examples of good output:
      Lcom/android/server/policy/PhoneWindowManager;
      ->interceptKeyBeforeQueueing
      Landroid/provider/Settings$System;
      ->getIntForUser
    """
    candidates: list[tuple[int, str]] = []   # (length, ref)

    for line in method_anchors:
        # Class type refs
        for m in _STABLE_CLASS_REF_RE.finditer(line):
            ref = m.group(0)
            if ref not in _TRIVIAL_CLASS_REFS and len(ref) >= 15:
                candidates.append((len(ref), ref))

        # Member refs  ->name( or ->name:
        for m in _STABLE_MEMBER_REF_RE.finditer(line):
            name = m.group(1)
            ref  = f"->{name}"
            if name not in _TRIVIAL_MEMBER_NAMES and len(name) >= 5:
                candidates.append((len(name), ref))

    # Deduplicate, longest-first (most specific)
    seen:   set[str]  = set()
    result: list[str] = []
    for _, ref in sorted(candidates, key=lambda t: -t[0]):
        if ref not in seen:
            seen.add(ref)
            result.append(ref)
            if len(result) >= max_refs:
                break
    return result


def normalize_smali_for_match(text: str) -> str:
    """Strip .line directives, normalize registers and labels, collapse blank lines."""
    text = _LINE_DIR_RE.sub("", text)
    text = _REGISTER_RE.sub("__REG__", text)
    text = _LABEL_RE.sub(":__LBL__", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_anchors_from_block(smali_block: str, n: int = 6) -> list[str]:
    """
    Return up to *n* 'strong' instruction lines from *smali_block*.

    Strong lines start with a known heavy opcode (invoke-*, iget-*, const-string, …).
    """
    anchors: list[str] = []
    for raw in smali_block.splitlines():
        line = raw.strip()
        if not line or line.startswith(".") or line.startswith("#"):
            continue
        if any(line.startswith(op) for op in _ANCHOR_OPCODES):
            anchors.append(line)
            if len(anchors) >= n:
                break
    return anchors


# ── Method parsing ─────────────────────────────────────────────────────────────

_METHOD_BLOCK_RE = re.compile(
    r"(\.method\s[^\n]+\n(?:.*?\n)*?\.end method)",
    re.DOTALL,
)


def parse_smali_methods(content: str) -> dict[str, str]:
    """Return {signature_line: full_block} for every method in *content*."""
    return {
        block.split("\n", 1)[0].strip(): block
        for block in (m.group(1) for m in _METHOD_BLOCK_RE.finditer(content))
    }


def extract_method_name(signature: str) -> str:
    """
    Given ".method public foo(Ljava/lang/String;)V" → "foo".
    Handles <init> and <clinit>.
    """
    parts = signature.strip().split()
    if not parts:
        return ""
    return parts[-1].split("(")[0]


# ── Register-wildcard regex ────────────────────────────────────────────────────

_PH_REG = "XREGPLACEHOLDERX"
_PH_LBL = "XLBLPLACEHOLDERX"


def build_register_wildcard_regex(smali_block: str) -> str:
    """
    Build a regex pattern from *smali_block* that tolerates:
      - different register names (v0/p0 → [vp]\\d+)
      - different label suffixes (:cond_0 → :(?:cond|goto|pswitch|sswitch)_\\w+)
      - optional .line N directives inserted between instructions

    Returns a raw pattern string suitable for re.compile(..., re.DOTALL).
    """
    block = _LINE_DIR_RE.sub("", smali_block)
    block = _REGISTER_RE.sub(_PH_REG, block)
    block = _LABEL_RE.sub(f":{_PH_LBL}", block)

    escaped = re.escape(block)

    # Restore register placeholder as regex wildcard
    escaped = escaped.replace(re.escape(_PH_REG), r"[vp]\d+")
    # Restore label placeholder
    escaped = escaped.replace(
        re.escape(_PH_LBL),
        r"(?:cond|goto|pswitch|sswitch)_[a-z0-9]+",
    )
    # Allow optional .line N between any two lines
    line_gap = r"\n(?:\s*\.line\s+\d+\s*\n)*"
    escaped = escaped.replace(r"\n", line_gap)
    # Allow flexible horizontal whitespace per line
    escaped = re.sub(r"(?<!\[) {2,}(?!\])", r"\\s+", escaped)

    return escaped


# ── Class finder ───────────────────────────────────────────────────────────────

def find_class(
    smali_roots: list[Path],
    exact_class: str,
    fallback_names: list[str] | None = None,
    class_anchors: list[str] | None = None,
    method_anchors: list[str] | None = None,
) -> ClassMatchResult:
    """
    Locate a smali file using a 4-tier strategy.

    Parameters
    ----------
    smali_roots    : directories to search (smali_classes*, smali_classes2*, …)
    exact_class    : class path as in TARGET_CLASS, e.g. "com/android/server/pm/Foo.smali"
    fallback_names : alternative basenames to try in Tier 2
    class_anchors  : verbatim content strings that must ALL be present for a Tier 3 match
    method_anchors : instruction lines from search block; stable class/member refs extracted
                     from them are used for Tier 4 when Tiers 1-3 all fail

    Tier guarantees
    ---------------
    AMBIGUOUS = FAIL at every tier.  Never patches a random close match.
    Returns ClassMatchStatus.NOT_FOUND only after all four tiers are exhausted.
    """
    if not exact_class.endswith(".smali"):
        exact_class += ".smali"
    exact_class = exact_class.replace("\\", "/")

    # Tier 1 — exact path
    for root in smali_roots:
        candidate = root / exact_class
        if candidate.is_file():
            return ClassMatchResult(
                status=ClassMatchStatus.EXACT,
                path=candidate,
                strategy=f"exact path in {root.name}",
            )

    # Collect all smali files for tiers 2-4
    all_smali: list[Path] = []
    for root in smali_roots:
        all_smali.extend(root.rglob("*.smali"))

    # Tier 2 — basename (TARGET_CLASS filename + fallback names)
    search_basenames: set[str] = {Path(exact_class).name}
    for fb in (fallback_names or []):
        bn = fb if fb.endswith(".smali") else fb + ".smali"
        search_basenames.add(Path(bn).name)

    tier2: list[Path] = [p for p in all_smali if p.name in search_basenames]
    if len(tier2) == 1:
        return ClassMatchResult(
            status=ClassMatchStatus.BASENAME,
            path=tier2[0],
            strategy=f"basename match: {tier2[0].name}",
        )
    if len(tier2) > 1:
        return ClassMatchResult(
            status=ClassMatchStatus.AMBIGUOUS,
            candidates=tier2,
            strategy=f"basename ambiguous: {len(tier2)} files named {sorted(search_basenames)}",
        )

    # Tier 3 — verbatim class_anchors content scan
    if class_anchors:
        tier3: list[Path] = []
        for p in all_smali:
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            if all(a in text for a in class_anchors):
                tier3.append(p)

        if len(tier3) == 1:
            return ClassMatchResult(
                status=ClassMatchStatus.ANCHOR,
                path=tier3[0],
                strategy=f"class-anchor scan: {len(class_anchors)} anchors matched in {tier3[0].name}",
            )
        if len(tier3) > 1:
            return ClassMatchResult(
                status=ClassMatchStatus.AMBIGUOUS,
                candidates=tier3,
                strategy=f"class-anchor ambiguous: {len(tier3)} files match all anchors",
            )
        # Tier 3 found nothing; fall through to Tier 4

    # Tier 4 — stable refs extracted from method_anchors instruction lines
    if method_anchors:
        stable_refs = extract_stable_refs_from_anchors(method_anchors)
        if stable_refs:
            tier4: list[Path] = []
            for p in all_smali:
                try:
                    text = p.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                if all(ref in text for ref in stable_refs):
                    tier4.append(p)

            if len(tier4) == 1:
                return ClassMatchResult(
                    status=ClassMatchStatus.METHOD_ANCHOR,
                    path=tier4[0],
                    strategy=(
                        f"method-anchor ref scan: {len(stable_refs)} refs "
                        f"({', '.join(stable_refs[:3])}) matched in {tier4[0].name}"
                    ),
                )
            if len(tier4) > 1:
                return ClassMatchResult(
                    status=ClassMatchStatus.AMBIGUOUS,
                    candidates=tier4,
                    strategy=(
                        f"method-anchor ref ambiguous: {len(tier4)} files match "
                        f"all {len(stable_refs)} stable refs"
                    ),
                )

    return ClassMatchResult(
        status=ClassMatchStatus.NOT_FOUND,
        strategy="all four tiers exhausted (path, basename, class-anchors, method-anchor-refs)",
    )


# ── Method finder ──────────────────────────────────────────────────────────────

def find_method(
    class_text: str,
    exact_signature: str,
    method_name: str | None = None,
    method_anchors: list[str] | None = None,
) -> MethodMatchResult:
    """
    Locate a method block inside a smali class using a 3-tier strategy.

    Parameters
    ----------
    class_text      : full smali text of the class file
    exact_signature : ".method public foo(…)V"
    method_name     : short name ("foo") used for Tier 2; derived from sig if None
    method_anchors  : instruction lines that must ALL appear in body for Tier 3
    """
    methods = parse_smali_methods(class_text)

    # Tier 1 — exact signature
    sig = exact_signature.strip()
    if sig in methods:
        return MethodMatchResult(
            status=MethodMatchStatus.EXACT_SIG,
            block=methods[sig],
            strategy=f"exact sig: {sig}",
        )

    # Tier 2 — method name
    tgt_name = method_name or extract_method_name(sig)
    if tgt_name:
        by_name = {s: b for s, b in methods.items() if extract_method_name(s) == tgt_name}
        if len(by_name) == 1:
            found_sig, found_block = next(iter(by_name.items()))
            return MethodMatchResult(
                status=MethodMatchStatus.NAME_ONLY,
                block=found_block,
                strategy=f"name match '{tgt_name}' → {found_sig}",
            )
        if len(by_name) > 1:
            return MethodMatchResult(
                status=MethodMatchStatus.AMBIGUOUS,
                candidates=list(by_name.keys()),
                strategy=f"name '{tgt_name}' ambiguous: {len(by_name)} overloads",
            )

    # Tier 3 — body anchors
    if not method_anchors:
        return MethodMatchResult(status=MethodMatchStatus.NOT_FOUND, strategy="no method anchors")

    by_anchor = {s: b for s, b in methods.items() if all(a in b for a in method_anchors)}
    if len(by_anchor) == 1:
        found_sig, found_block = next(iter(by_anchor.items()))
        return MethodMatchResult(
            status=MethodMatchStatus.ANCHOR,
            block=found_block,
            strategy=f"anchor scan ({len(method_anchors)} anchors) → {found_sig}",
        )
    if len(by_anchor) > 1:
        return MethodMatchResult(
            status=MethodMatchStatus.AMBIGUOUS,
            candidates=list(by_anchor.keys()),
            strategy=f"anchor ambiguous: {len(by_anchor)} methods match all anchors",
        )

    return MethodMatchResult(status=MethodMatchStatus.NOT_FOUND, strategy="all tiers exhausted")


# ── Replace / inject helpers ───────────────────────────────────────────────────

def replace_method_body(
    class_text: str,
    found_block: str,
    replacement: str,
) -> tuple[str, bool]:
    """
    Replace *found_block* with *replacement* in *class_text* (literal, first occurrence).

    Returns (new_text, changed).
    """
    if found_block not in class_text:
        return class_text, False
    return class_text.replace(found_block, replacement, 1), True


def insert_method_if_missing(class_text: str, method_block: str) -> str:
    """Append *method_block* before .end class, or at the end of the file."""
    insertion = method_block.rstrip("\n") + "\n"
    if ".end class" in class_text:
        return class_text.replace(".end class", insertion + ".end class", 1)
    if ".end method" in class_text:
        idx = class_text.rfind(".end method") + len(".end method")
        return class_text[:idx] + "\n\n" + insertion + class_text[idx:]
    return class_text.rstrip("\n") + "\n\n" + insertion


def add_class_if_missing(
    smali_roots: list[Path],
    class_name: str,
    class_content: str,
) -> bool:
    """
    Write *class_content* as a new smali file in the last smali root.

    Returns True if written, False if the file already exists.
    """
    existing = find_class(smali_roots, class_name)
    if existing.path is not None:
        return False

    inject_root = smali_roots[-1] if smali_roots else None
    if inject_root is None:
        return False

    if not class_name.endswith(".smali"):
        class_name += ".smali"
    dest = inject_root / class_name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(class_content, encoding="utf-8")
    return True


# ── Main smart patch orchestrator ─────────────────────────────────────────────

def apply_smart_patch(
    smali_roots: list[Path],
    rule: dict,
    dry_run: bool = True,
) -> PatchResult:
    """
    Apply one patch rule dict using multi-tier smart matching.

    Expected rule keys
    ------------------
    id, type, required, replacement         — always required
    method                                  — .method signature line (method_replace / method_add)
    search                                  — a/ block (method_replace; used to derive anchors)
    target_class                            — class path (injected by runner from TARGET_CLASS)
    method_name        (optional)           — short name; derived from 'method' if absent
    method_anchors     (optional)           — derived from 'search' if absent
    class_fallback_names (optional)         — list of alt basenames for Tier 2
    class_anchors      (optional)           — list of lines for Tier 3 class scan
    """
    pid         = rule.get("id", "?")
    method_sig  = rule.get("method", "")
    patch_type  = rule.get("type", "?")
    required    = rule.get("required", True)
    replacement = rule.get("replacement", "")
    search      = rule.get("search", "")

    method_name    = rule.get("method_name") or extract_method_name(method_sig)
    method_anchors = rule.get("method_anchors") or (
        extract_anchors_from_block(search) if search else []
    )
    fallback_names = rule.get("class_fallback_names") or []
    class_anchors  = rule.get("class_anchors") or []
    target_class   = rule.get("target_class", "")

    # ── dex_add ───────────────────────────────────────────────────────────────
    if patch_type == "dex_add":
        return PatchResult(
            patch_id=pid, method="", type=patch_type, required=required,
            status=PatchApplyStatus.SKIPPED,
            message="dex_add is handled in the DEX merge stage",
        )

    # ── class_add ─────────────────────────────────────────────────────────────
    if patch_type == "class_add":
        if dry_run:
            return PatchResult(
                patch_id=pid, method="", type=patch_type, required=required,
                status=PatchApplyStatus.WOULD_PATCH,
                message="dry-run: would add class",
            )
        written = add_class_if_missing(smali_roots, target_class, replacement)
        return PatchResult(
            patch_id=pid, method="", type=patch_type, required=required,
            status=PatchApplyStatus.PATCHED if written else PatchApplyStatus.EXISTS,
            message="class injected" if written else "class already exists",
        )

    # ── smali patches: locate target class (4-tier) ──────────────────────────
    class_result = find_class(
        smali_roots, target_class, fallback_names, class_anchors, method_anchors
    )

    if class_result.status in (ClassMatchStatus.NOT_FOUND, ClassMatchStatus.AMBIGUOUS):
        return PatchResult(
            patch_id=pid, method=method_sig, type=patch_type, required=required,
            status=PatchApplyStatus.FAILED if required else PatchApplyStatus.SKIPPED,
            class_match=class_result.status,
            class_strategy=class_result.strategy,
            message=f"class {class_result.status.value}: {class_result.strategy}",
        )

    try:
        class_text = class_result.path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return PatchResult(
            patch_id=pid, method=method_sig, type=patch_type, required=required,
            status=PatchApplyStatus.FAILED,
            class_match=class_result.status,
            class_strategy=class_result.strategy,
            message=f"read error: {exc}",
        )

    # ── method_replace ────────────────────────────────────────────────────────
    if patch_type == "method_replace":
        method_result = find_method(class_text, method_sig, method_name, method_anchors)

        if method_result.status in (MethodMatchStatus.NOT_FOUND, MethodMatchStatus.AMBIGUOUS):
            return PatchResult(
                patch_id=pid, method=method_sig, type=patch_type, required=required,
                status=PatchApplyStatus.FAILED if required else PatchApplyStatus.SKIPPED,
                class_match=class_result.status,
                class_strategy=class_result.strategy,
                method_match=method_result.status,
                method_strategy=method_result.strategy,
                message=f"method {method_result.status.value}: {method_result.strategy}",
            )

        if dry_run:
            return PatchResult(
                patch_id=pid, method=method_sig, type=patch_type, required=required,
                status=PatchApplyStatus.WOULD_PATCH,
                class_match=class_result.status,
                class_strategy=class_result.strategy,
                method_match=method_result.status,
                method_strategy=method_result.strategy,
                message=f"would replace via {class_result.strategy} / {method_result.strategy}",
            )

        new_text, changed = replace_method_body(class_text, method_result.block, replacement)
        if not changed:
            return PatchResult(
                patch_id=pid, method=method_sig, type=patch_type, required=required,
                status=PatchApplyStatus.FAILED,
                class_match=class_result.status,
                class_strategy=class_result.strategy,
                method_match=method_result.status,
                method_strategy=method_result.strategy,
                message="found block disappeared from class text (internal error)",
            )

        try:
            class_result.path.write_text(new_text, encoding="utf-8")
        except OSError as exc:
            return PatchResult(
                patch_id=pid, method=method_sig, type=patch_type, required=required,
                status=PatchApplyStatus.FAILED,
                class_match=class_result.status,
                class_strategy=class_result.strategy,
                method_match=method_result.status,
                method_strategy=method_result.strategy,
                message=f"write error: {exc}",
            )

        return PatchResult(
            patch_id=pid, method=method_sig, type=patch_type, required=required,
            status=PatchApplyStatus.PATCHED,
            class_match=class_result.status,
            class_strategy=class_result.strategy,
            method_match=method_result.status,
            method_strategy=method_result.strategy,
            message=f"replaced via {class_result.strategy} / {method_result.strategy}",
        )

    # ── method_add ────────────────────────────────────────────────────────────
    if patch_type == "method_add":
        existing_names = {extract_method_name(s) for s in parse_smali_methods(class_text)}
        tgt_name = method_name or extract_method_name(method_sig)

        if tgt_name in existing_names:
            return PatchResult(
                patch_id=pid, method=method_sig, type=patch_type, required=required,
                status=PatchApplyStatus.EXISTS,
                class_match=class_result.status,
                class_strategy=class_result.strategy,
                method_match=MethodMatchStatus.NAME_ONLY,
                message=f"method '{tgt_name}' already present",
            )

        if dry_run:
            return PatchResult(
                patch_id=pid, method=method_sig, type=patch_type, required=required,
                status=PatchApplyStatus.WOULD_PATCH,
                class_match=class_result.status,
                class_strategy=class_result.strategy,
                method_match=MethodMatchStatus.NOT_FOUND,
                message="dry-run: would inject method",
            )

        new_text = insert_method_if_missing(class_text, replacement)
        try:
            class_result.path.write_text(new_text, encoding="utf-8")
        except OSError as exc:
            return PatchResult(
                patch_id=pid, method=method_sig, type=patch_type, required=required,
                status=PatchApplyStatus.FAILED,
                class_match=class_result.status,
                class_strategy=class_result.strategy,
                message=f"write error: {exc}",
            )

        return PatchResult(
            patch_id=pid, method=method_sig, type=patch_type, required=required,
            status=PatchApplyStatus.PATCHED,
            class_match=class_result.status,
            class_strategy=class_result.strategy,
            method_match=MethodMatchStatus.NOT_FOUND,
            message=f"injected via {class_result.strategy}",
        )

    # ── unknown type ──────────────────────────────────────────────────────────
    return PatchResult(
        patch_id=pid, method=method_sig, type=patch_type, required=required,
        status=PatchApplyStatus.FAILED,
        message=f"unknown patch type: {patch_type}",
    )
