"""
Legend JAR mod — framework/signature_verification_bypass

Patches framework.jar smali files to disable APK signature verification.

Target classes (all found by rglob within unpack_dir):
  PackageParser.smali              — collectCertificates, parseBaseApkCommon
  PackageParser$PackageParserException.smali — <init>
  PackageParser$SigningDetails.smali / SigningDetails.smali
                                   — checkCapability, hasAncestorOrSelf
  ApkSignatureSchemeV2Verifier.smali — verifySigner
  ApkSignatureSchemeV3Verifier.smali — verifySigner
  ApkSignatureVerifier.smali       — getMinimumSignatureSchemeVersionForTargetSdk
  ApkSigningBlockUtils.smali       — verifyIntegrityFor1MbChunkBasedAlgorithm
  StrictJarVerifier.smali          — verifyMessageDigest
  StrictJarFile.smali              — <init>
  ParsingPackageUtils.smali (A16+) — parseSharedUser

Config gate: signature_verification_bypass (default: False)
Security sensitive: True
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from factory.patch.legend.mods._shared import find_first

MOD_ID = "signature_verification_bypass"
TARGET_JAR = "framework.jar"
METADATA = {
    "mod_id":             MOD_ID,
    "target_jar":         TARGET_JAR,
    "target_classes": [
        "PackageParser.smali",
        "PackageParser$PackageParserException.smali",
        "PackageParser$SigningDetails.smali",
        "SigningDetails.smali",
        "ApkSignatureSchemeV2Verifier.smali",
        "ApkSignatureSchemeV3Verifier.smali",
        "ApkSignatureVerifier.smali",
        "ApkSigningBlockUtils.smali",
        "StrictJarVerifier.smali",
        "StrictJarFile.smali",
        "ParsingPackageUtils.smali (A16+)",
    ],
    "target_methods": [
        "collectCertificates", "parseBaseApkCommon",
        "checkCapability", "hasAncestorOrSelf",
        "verifySigner", "getMinimumSignatureSchemeVersionForTargetSdk",
        "verifyIntegrityFor1MbChunkBasedAlgorithm",
        "verifyMessageDigest", "<init>", "parseSharedUser",
    ],
    "enabled_by_default": False,
    "security_sensitive": True,
    "report_keys": ["status", "enabled", "patched_classes", "patched_methods",
                    "skipped_missing", "android_major"],
}


def _ow(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def _patch_packageparser(root: Path, android_major: int | None, dry_run: bool) -> tuple[str, list[str]]:
    tgt = find_first(root, "PackageParser.smali")
    if not tgt:
        return "MISSING", []
    lines = tgt.read_text(encoding="utf-8").splitlines(True)
    out, in_collect, in_common, changed = [], False, False, 0
    a16 = android_major == 16
    for line in lines:
        s = line.strip()
        if s.startswith(".method") and "collectCertificates(" in s and s.endswith("Z)V"):
            in_collect = True
        elif in_collect and s.startswith(".end method"):
            in_collect = False
        if in_collect and "if-eqz p2" in s:
            out.append(f"    const/4 {'v1' if a16 else 'p2'}, 0x1\n")
            changed += 1
        if s.startswith(".method") and "parseBaseApkCommon(" in s:
            in_common = True
        elif in_common and s.startswith(".end method"):
            in_common = False
        if in_common and ("if-nez v14" if a16 else "if-nez v5") in s:
            out.append(f"    const/4 {'v14' if a16 else 'v5'}, 0x1\n")
            changed += 1
        out.append(line)
    if changed and not dry_run:
        _ow(tgt, "".join(out))
    return ("PATCHED" if changed else "SKIPPED"), (["PackageParser.smali::collectCertificates", "PackageParser.smali::parseBaseApkCommon"] if changed else [])


def _patch_ppe(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    tgt = find_first(root, "PackageParser$PackageParserException.smali")
    if not tgt:
        return "MISSING", []
    lines = tgt.read_text(encoding="utf-8").splitlines(True)
    out, changed = [], 0
    for line in lines:
        out.append(line)
        if "iput p1, p0, Landroid/content/pm/PackageParser$PackageParserException;->error:I" in line:
            out.append("    const/4 p1, 0x0\n")
            changed += 1
    if changed and not dry_run:
        _ow(tgt, "".join(out))
    return ("PATCHED" if changed else "SKIPPED"), (["PackageParser$PackageParserException.smali::<init>"] if changed else [])


def _patch_signing_details(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    patched: list[str] = []
    for fn in ("PackageParser$SigningDetails.smali", "SigningDetails.smali"):
        tgt = find_first(root, fn)
        if not tgt:
            continue
        txt = orig = tgt.read_text(encoding="utf-8")
        txt = re.sub(
            r"(\.method[^\n]*checkCapability[^\n]*\n)(.*?)(\.end method)",
            r"\1    .registers 3\n    const/4 p0, 0x1\n    return p0\n\3",
            txt, flags=re.DOTALL,
        )
        txt = re.sub(
            r"(\.method[^\n]*hasAncestorOrSelf[^\n]*\n)(.*?)(\.end method)",
            r"\1    .registers 2\n    const/4 p0, 0x1\n    return p0\n\3",
            txt, flags=re.DOTALL,
        )
        if txt != orig:
            if not dry_run:
                _ow(tgt, txt)
            patched.extend([f"{fn}::checkCapability", f"{fn}::hasAncestorOrSelf"])
    return ("PATCHED" if patched else "SKIPPED"), patched


def _patch_v2(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    tgt = find_first(root, "ApkSignatureSchemeV2Verifier.smali")
    if not tgt:
        return "MISSING", []
    lines = tgt.read_text(encoding="utf-8").splitlines(True)
    out, in_m, idxs = [], False, []
    for line in lines:
        s = line.strip()
        if s.startswith(".method") and "verifySigner(Ljava/nio/ByteBuffer;Ljava/util/Map;Ljava/security/cert/CertificateFactory;)" in s:
            in_m = True
        elif in_m and s.startswith(".end method"):
            in_m = False
        if in_m and s == "move-result v0":
            idxs.append(len(out))
        out.append(line)
    if idxs:
        out[idxs[-1]] = "    const/4 v0, 0x1\n"
        if not dry_run:
            _ow(tgt, "".join(out))
        return "PATCHED", ["ApkSignatureSchemeV2Verifier.smali::verifySigner"]
    return "SKIPPED", []


def _patch_v3(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    tgt = find_first(root, "ApkSignatureSchemeV3Verifier.smali")
    if not tgt:
        return "MISSING", []
    lines = tgt.read_text(encoding="utf-8").splitlines(True)
    out, in_m, changed = [], False, False
    for line in lines:
        s = line.strip()
        if s.startswith(".method") and "verifySigner(Ljava/nio/ByteBuffer;Ljava/util/Map;Ljava/security/cert/CertificateFactory;)" in s:
            in_m = True
        elif in_m and s.startswith(".end method"):
            in_m = False
        if in_m and s == "move-result v0":
            k = len(out) - 1
            while k >= 0 and out[k].strip() == "":
                k -= 1
            if k >= 0 and "MessageDigest;->isEqual([B[B)Z" in out[k].strip():
                out.append("    const/4 v0, 0x1\n")
                changed = True
                continue
        out.append(line)
    if changed:
        if not dry_run:
            _ow(tgt, "".join(out))
        return "PATCHED", ["ApkSignatureSchemeV3Verifier.smali::verifySigner"]
    return "SKIPPED", []


def _patch_apk_sig_verifier(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    tgt = find_first(root, "ApkSignatureVerifier.smali")
    if not tgt:
        return "MISSING", []
    lines = tgt.read_text(encoding="utf-8").splitlines(True)
    out, in_m, changed = [], False, False
    for line in lines:
        s = line.strip()
        if s.startswith(".method") and "getMinimumSignatureSchemeVersionForTargetSdk" in s:
            in_m = True
            out.append(line)
            out += ["    .registers 1\n", "    const/4 v0, 0x0\n", "    return v0\n"]
            changed = True
            continue
        elif in_m and s.startswith(".end method"):
            out.append(line); in_m = False; continue
        elif in_m:
            continue
        if "invoke-static {p0, p1, p3}, Landroid/util/apk/ApkSignatureVerifier;->verifyV1Signature(" in s:
            out.append("    const p3, 0x0\n")
            changed = True
        out.append(line)
    if changed:
        if not dry_run:
            _ow(tgt, "".join(out))
        return "PATCHED", ["ApkSignatureVerifier.smali::getMinimumSignatureSchemeVersionForTargetSdk"]
    return "SKIPPED", []


def _patch_signing_block_utils(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    tgt = find_first(root, "ApkSigningBlockUtils.smali")
    if not tgt:
        return "MISSING", []
    lines = tgt.read_text(encoding="utf-8").splitlines(True)
    out, in_m, changed = [], False, False
    for line in lines:
        s = line.strip()
        if s.startswith(".method") and "verifyIntegrityFor1MbChunkBasedAlgorithm" in s:
            in_m = True
        elif in_m and s.startswith(".end method"):
            in_m = False
        if in_m and s == "move-result v7":
            out.append("    const/4 v7, 0x1\n"); changed = True; continue
        out.append(line)
    if changed:
        if not dry_run:
            _ow(tgt, "".join(out))
        return "PATCHED", ["ApkSigningBlockUtils.smali::verifyIntegrityFor1MbChunkBasedAlgorithm"]
    return "SKIPPED", []


def _patch_strict_jar(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    patched: list[str] = []
    v = find_first(root, "StrictJarVerifier.smali")
    if v:
        lines = v.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "verifyMessageDigest" in s:
                in_m = True; out.append(line)
                out += ["    .registers 2\n", "    const/4 v0, 0x1\n", "    return v0\n"]
                changed = True; continue
            if in_m and s.startswith(".end method"):
                out.append(line); in_m = False; continue
            if in_m:
                continue
            out.append(line)
        if changed:
            if not dry_run:
                _ow(v, "".join(out))
            patched.append("StrictJarVerifier.smali::verifyMessageDigest")
    f = find_first(root, "StrictJarFile.smali")
    if f:
        lines = f.read_text(encoding="utf-8").splitlines(True)
        out, in_m = [], False
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "<init>(Ljava/lang/String;Ljava/io/FileDescriptor;ZZ)V" in s:
                in_m = True
            elif in_m and s.startswith(".end method"):
                in_m = False
            if in_m and (s == "if-eqz v6, :cond_56" or s == ":cond_56"):
                continue
            out.append(line)
        if not dry_run:
            _ow(f, "".join(out))
        patched.append("StrictJarFile.smali::<init>")
    return ("PATCHED" if patched else "SKIPPED"), patched


def _patch_parsing_package_utils(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    """Android 16 only."""
    tgt = find_first(root, "ParsingPackageUtils.smali")
    if not tgt:
        return "MISSING", []
    lines = tgt.read_text(encoding="utf-8").splitlines(True)
    out, in_m, in_ps, found, changed = [], False, False, False, False
    for line in lines:
        s = line.strip()
        if s.startswith(".method") and "parseSharedUser" in s:
            in_m = in_ps = True; out.append(line); continue
        if in_m and s.startswith(".end method"):
            in_m = in_ps = False; found = False; out.append(line); continue
        if in_ps and s == "if-eqz v4" and not found:
            found = changed = True
            out.append("    const/4 v4, 0x0\n")
        out.append(line)
    if changed:
        if not dry_run:
            _ow(tgt, "".join(out))
        return "PATCHED", ["ParsingPackageUtils.smali::parseSharedUser"]
    return "SKIPPED", []


def apply(unpack_dir: Path, config: dict, dry_run: bool = True) -> dict[str, Any]:
    enabled      = config.get(MOD_ID, False)
    android_major = config.get("android_major")

    report: dict[str, Any] = {
        "mod_id":          MOD_ID,
        "target_jar":      TARGET_JAR,
        "status":          "UNKNOWN",
        "enabled":         enabled,
        "android_major":   android_major,
        "patched_classes": [],
        "patched_methods": [],
        "skipped_missing": [],
        "warnings":        [],
        "errors":          [],
    }

    if not enabled:
        report["status"] = "SKIPPED_CONFIG_DISABLED"
        return report

    if not unpack_dir.is_dir():
        report["status"] = "FAILED"
        report["errors"].append(f"unpack_dir not found: {unpack_dir}")
        return report

    patched: list[str] = []
    missing: list[str] = []

    for fn, args in [
        (_patch_packageparser, (unpack_dir, android_major, dry_run)),
        (_patch_ppe,           (unpack_dir, dry_run)),
        (_patch_signing_details, (unpack_dir, dry_run)),
        (_patch_v2,            (unpack_dir, dry_run)),
        (_patch_v3,            (unpack_dir, dry_run)),
        (_patch_apk_sig_verifier, (unpack_dir, dry_run)),
        (_patch_signing_block_utils, (unpack_dir, dry_run)),
        (_patch_strict_jar,    (unpack_dir, dry_run)),
    ]:
        try:
            st, methods = fn(*args)
            if st == "MISSING":
                missing.append(fn.__name__.replace("_patch_", ""))
            else:
                patched.extend(methods)
        except Exception as exc:
            report["errors"].append(f"{fn.__name__}: {exc}")

    if android_major == 16:
        try:
            st, methods = _patch_parsing_package_utils(unpack_dir, dry_run)
            if st == "MISSING":
                missing.append("ParsingPackageUtils.smali")
            else:
                patched.extend(methods)
        except Exception as exc:
            report["errors"].append(f"_patch_parsing_package_utils: {exc}")

    report["patched_methods"] = patched
    report["patched_classes"] = list({m.split("::")[0] for m in patched})
    report["skipped_missing"] = missing

    if report["errors"]:
        report["status"] = "FAILED"
    elif dry_run:
        report["status"] = "DRY_RUN"
    elif patched:
        report["status"] = "APPLIED"
    else:
        report["status"] = "SKIPPED"

    return report
