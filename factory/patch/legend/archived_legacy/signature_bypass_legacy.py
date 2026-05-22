"""
Legend-only legacy Signature Verification Bypass patch stage.

Carries the exact behavior of MEZOBuildRom.py functions:
  - disable_signature_verification_a14_15(work_dir)
  - disable_signature_verification_a16(work_dir)

Flavor guard: only runs for legend / deadzone_legend / DeadZone_Legend.
All other flavors exit success with status SKIPPED_NON_LEGEND.

Supported android_major values: 14, 15, 16.
Any other value exits success with status SKIPPED_UNSUPPORTED_ANDROID.

Default mode is dry-run (--execute required to apply patches).

CLI:
  # dry-run (default):
  python -m factory.patch.legend.signature_bypass_legacy \\
      --project "path/to/unpacked_project" \\
      --flavor legend \\
      --android-major 16

  # execute:
  python -m factory.patch.legend.signature_bypass_legacy \\
      --project "path/to/unpacked_project" \\
      --flavor legend \\
      --android-major 16 \\
      --execute

Integration hook (safe to call from jar_patch.py or a central runner):
  from factory.patch.legend.signature_bypass_legacy import apply_legacy_signature_bypass
  apply_legacy_signature_bypass(work_dir, android_major=16, flavor="legend", execute=True)
"""
from __future__ import annotations

import argparse
import re
import sys
import traceback
from pathlib import Path

from factory.patch.common.legacy_signature_report import (
    SigBypassReport,
    write_sig_bypass_reports,
)

_REPO_ROOT   = Path(__file__).resolve().parents[3]
_OUTPUT_ROOT = _REPO_ROOT / "output"
_REPORTS_DIR = _OUTPUT_ROOT / "reports"

_LEGEND_FLAVORS = {"legend", "deadzone_legend"}

_EXPECTED_FOLDERS = [
    "framework_unpacked",
    "services_unpacked",
    "miui_services_unpacked",
]


def _normalise_flavor(flavor: str) -> str:
    return flavor.lower().replace("-", "_")


# ─────────────────────────────────────────────────────────────────────────────
# Exact copy of MEZOBuildRom.disable_signature_verification_a14_15
# Only change: log() -> print() (log was print in the original)
# ─────────────────────────────────────────────────────────────────────────────
def disable_signature_verification_a14_15(work_dir: Path) -> None:
    """Disable Signature Verification by modifying various framework and service files"""

    print("\n🔏 Đang xử lý Disable Signature Verification (smali-only)...")

    def p(*a): print(" ".join(str(x) for x in a))
    def overwrite(path: Path, text: str) -> None:
        path.write_text(text, encoding="utf-8")

    def find_one(root: Path, filename: str) -> Path | None:
        for pth in root.rglob(filename):
            return pth
        return None

    def patch_packageparser(smali_root: Path) -> None:
        tgt = find_one(smali_root, "PackageParser.smali")
        if not tgt:
            p(f"  ⚠️ Không thấy PackageParser.smali trong {smali_root}")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_collect, in_common, changed = [], False, False, 0
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "collectCertificates(" in s and s.endswith("Z)V"):
                in_collect = True
            elif in_collect and s.startswith(".end method"):
                in_collect = False
            if in_collect and "if-eqz p2" in s:
                out.append("    const/4 p2, 0x1\n"); changed += 1
            if s.startswith(".method") and "parseBaseApkCommon(" in s:
                in_common = True
            elif in_common and s.startswith(".end method"):
                in_common = False
            if in_common and "if-nez v5" in s:
                out.append("    const/4 v5, 0x1\n"); changed += 1
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ PackageParser.smali patched:", changed, "spot(s)")
        else:
            p("  ℹ️ PackageParser.smali không cần thay đổi")
        tgt2 = find_one(smali_root, "PackageParser$PackageParserException.smali")
        if tgt2:
            lines = tgt2.read_text(encoding="utf-8").splitlines(True)
            out, changed2 = [], 0
            for line in lines:
                out.append(line)
                if "iput p1, p0, Landroid/content/pm/PackageParser$PackageParserException;->error:I" in line:
                    out.append("    const/4 p1, 0x0\n")
                    changed2 += 1
            if changed2:
                overwrite(tgt2, "".join(out))
                p("  ✅ PackageParser$PackageParserException.smali patched")
        for fn in ("PackageParser$SigningDetails.smali", "SigningDetails.smali"):
            tgt3 = find_one(smali_root, fn)
            if not tgt3:
                continue
            txt = tgt3.read_text(encoding="utf-8")
            orig = txt
            txt = re.sub(
                r"(\.method[^\n]*checkCapability[^\n]*\n)(.*?)(\.end method)",
                r"\1    .registers 3\n    const/4 p0, 0x1\n    return p0\n\3",
                txt, flags=re.DOTALL
            )
            txt = re.sub(
                r"(\.method[^\n]*hasAncestorOrSelf[^\n]*\n)(.*?)(\.end method)",
                r"\1    .registers 2\n    const/4 p0, 0x1\n    return p0\n\3",
                txt, flags=re.DOTALL
            )
            if txt != orig:
                overwrite(tgt3, txt)
                p(f"  ✅ {fn} patched (capability/ancestor -> true)")

    def patch_v2_verifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureSchemeV2Verifier.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSignatureSchemeV2Verifier.smali")
            return
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
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureSchemeV2Verifier.smali patched (v0=1)")

    def patch_v3_verifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureSchemeV3Verifier.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSignatureSchemeV3Verifier.smali")
            return
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
                if k >= 0 and out[k].strip() == "invoke-static {v12, v6}, Ljava/security/MessageDigest;->isEqual([B[B)Z":
                    out.append("    const/4 v0, 0x1\n")
                    changed = True
                    continue
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureSchemeV3Verifier.smali patched (v0=1 sau isEqual)")

    def patch_apksignatureverifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureVerifier.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSignatureVerifier.smali")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "getMinimumSignatureSchemeVersionForTargetSdk" in s:
                in_m = True
                out.append(line)
                out.append("    .registers 1\n")
                out.append("    const/4 v0, 0x0\n")
                out.append("    return v0\n")
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
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureVerifier.smali patched (minScheme=0, p3=0)")

    def patch_apksigningblockutils(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSigningBlockUtils.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSigningBlockUtils.smali")
            return
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
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSigningBlockUtils.smali patched (v7=1)")

    def patch_strictjar(smali_root: Path) -> None:
        v = find_one(smali_root, "StrictJarVerifier.smali")
        if v:
            lines = v.read_text(encoding="utf-8").splitlines(True)
            out, in_m, changed = [], False, False
            for line in lines:
                s = line.strip()
                if s.startswith(".method") and "verifyMessageDigest" in s:
                    in_m = True
                    out.append(line)
                    out.append("    .registers 2\n")
                    out.append("    const/4 v0, 0x1\n")
                    out.append("    return v0\n")
                    changed = True
                    continue
                if in_m and s.startswith(".end method"):
                    out.append(line); in_m = False; continue
                if in_m:
                    continue
                out.append(line)
            if changed:
                overwrite(v, "".join(out))
                p("  ✅ StrictJarVerifier.smali patched (verifyMessageDigest -> true)")
        f = find_one(smali_root, "StrictJarFile.smali")
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
            overwrite(f, "".join(out))
            p("  ✅ StrictJarFile.smali patched (<init> drop fail branch)")

    def patch_services(smali_root: Path) -> None:
        f1 = find_one(smali_root, "PackageManagerServiceUtils.smali")
        if f1:
            lines = f1.read_text(encoding="utf-8").splitlines(True)
            out, in_m, changed = [], False, False
            for ln in lines:
                s = ln.strip()
                if s.startswith(".method") and "checkDowngrade" in s:
                    in_m = True; out.append(ln)
                    out.append("    .locals 0\n    return-void\n"); changed = True; continue
                if in_m and s.startswith(".end method"):
                    out.append(ln); in_m = False; continue
                if in_m:
                    continue
                out.append(ln)
            if changed: overwrite(f1, "".join(out)); p("  ✅ PackageManagerServiceUtils.checkDowngrade() -> return-void")
        f2 = find_one(smali_root, "KeySetManagerService.smali")
        if f2:
            lines = f2.read_text(encoding="utf-8").splitlines(True)
            out, in_m, changed = [], False, False
            for ln in lines:
                s = ln.strip()
                if s.startswith(".method") and "shouldCheckUpgradeKeySetLocked" in s:
                    in_m = True; out.append(ln)
                    out.append("    .locals 1\n    const/4 v0, 0x0\n    return v0\n"); changed = True; continue
                if in_m and s.startswith(".end method"):
                    out.append(ln); in_m = False; continue
                if in_m: continue
                out.append(ln)
            if changed: overwrite(f2, "".join(out)); p("  ✅ KeySetManagerService.shouldCheckUpgradeKeySetLocked() -> false")
        f3 = find_one(smali_root, "InstallPackageHelper.smali")
        if f3:
            lines = f3.read_text(encoding="utf-8").splitlines(True)
            out, changed = [], 0
            i = 0
            while i < len(lines):
                ln = lines[i]; s = ln.strip()
                if "if-eqz v12" in s:
                    j = i + 1
                    while j < len(lines) and lines[j].strip() == "":
                        j += 1
                    if j < len(lines) and lines[j].strip() == "invoke-interface {v7}, Lcom/android/server/pm/pkg/AndroidPackage;->isLeavingSharedUser()Z":
                        out.append("    const/4 v12, 0x1\n"); changed += 1
                out.append(ln); i += 1
            if changed:
                overwrite(f3, "".join(out)); p("  ✅ InstallPackageHelper: force v12=1 trước isLeavingSharedUser()")
        f4 = find_one(smali_root, "ReconcilePackageUtils.smali")
        if f4:
            txt = f4.read_text(encoding="utf-8")
            new = txt.replace("const/4 v0, 0x0", "const/4 v0, 0x1", 1)
            if new != txt:
                overwrite(f4, new); p("  ✅ ReconcilePackageUtils: v0 -> 1 (flip đầu tiên)")

    def patch_miui_pms_impl(smali_root: Path) -> None:
        f = find_one(smali_root, "PackageManagerServiceImpl.smali")
        if not f:
            p("  ⚠️ Không thấy PackageManagerServiceImpl.smali (miui)")
            return
        lines = f.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        current = ""
        for ln in lines:
            s = ln.strip()
            if s.startswith(".method") and "verifyIsolationViolation" in s:
                in_m = True; current = "vii"; out.append(ln)
                out.append("    .registers 3\n    return-void\n"); changed = True; continue
            if s.startswith(".method") and "canBeUpdate(" in s:
                in_m = True; current = "cbu"; out.append(ln)
                out.append("    .registers 2\n    return-void\n"); changed = True; continue
            if in_m and s.startswith(".end method"):
                out.append(ln); in_m = False; current = ""; continue
            if in_m: continue
            out.append(ln)
        if changed:
            overwrite(f, "".join(out))
            p("  ✅ PackageManagerServiceImpl.smali (miui) patched (2 method -> return-void)")

    fw = work_dir / "framework_unpacked"
    sv = work_dir / "services_unpacked"
    mi = work_dir / "miui_services_unpacked"

    fw_smali = [
        fw / "smali_classes",
        fw / "smali_classes4",
        fw / "smali_classes5",
    ]
    sv_smali = [sv / "smali_classes2", sv / "smali_classes", sv / "smali_classes3"]
    mi_smali = [mi / "smali_classes"]

    p("\n📁 Patching framework_unpacked/smali_classes ...")
    if fw_smali[0].exists():
        patch_packageparser(fw_smali[0])
    else:
        p("  ⚠️ Thiếu thư mục:", fw_smali[0])

    p("\n📁 Patching framework_unpacked/smali_classes4 ...")
    if fw_smali[1].exists():
        patch_v2_verifier(fw_smali[1])
        patch_v3_verifier(fw_smali[1])
        patch_apksignatureverifier(fw_smali[1])
        patch_apksigningblockutils(fw_smali[1])
        patch_strictjar(fw_smali[1])
    else:
        p("  ⚠️ Thiếu thư mục:", fw_smali[1])

    if fw_smali[2].exists():
        p("\n📁 Kiểm tra framework_unpacked/smali_classes5 (nếu có file liên quan)...")
    else:
        p("  ℹ️ Bỏ qua smali_classes5 (không có)")

    p("\n📁 Patching services_unpacked ...")
    any_sv = False
    for d in sv_smali:
        if d.exists():
            patch_services(d); any_sv = True
    if not any_sv:
        p("  ⚠️ Thiếu toàn bộ thư mục smali trong services_unpacked")

    p("\n📁 Patching miui_services_unpacked/smali_classes ...")
    if mi_smali[0].exists():
        patch_miui_pms_impl(mi_smali[0])
    else:
        p("  ⚠️ Thiếu thư mục:", mi_smali[0])

    print("\n🎉 Hoàn tất Disable Signature Verification (smali-only).")


# ─────────────────────────────────────────────────────────────────────────────
# Exact copy of MEZOBuildRom.disable_signature_verification_a16
# Only change: log() -> print()
# ─────────────────────────────────────────────────────────────────────────────
def disable_signature_verification_a16(work_dir: Path) -> None:
    """Disable Signature Verification (Android 16 / a16.py logic): smali-only patches."""

    print("\n🔏 Đang xử lý Disable Signature Verification A16 (smali-only)...")

    def p(*a):
        print(" ".join(str(x) for x in a))

    def overwrite(path: Path, text: str) -> None:
        path.write_text(text, encoding="utf-8")

    def find_one(root: Path, filename: str) -> Path | None:
        for pth in root.rglob(filename):
            return pth
        return None

    def patch_packageparser(smali_root: Path) -> None:
        tgt = find_one(smali_root, "PackageParser.smali")
        if not tgt:
            p(f"  ⚠️ Không thấy PackageParser.smali trong {smali_root}")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_collect, in_common, changed = [], False, False, 0
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "collectCertificates(" in s and s.endswith("Z)V"):
                in_collect = True
            elif in_collect and s.startswith(".end method"):
                in_collect = False
            if in_collect and "if-eqz p2" in s:
                out.append("    const/4 v1, 0x1\n")
                changed += 1
            if s.startswith(".method") and "parseBaseApkCommon(" in s:
                in_common = True
            elif in_common and s.startswith(".end method"):
                in_common = False
            if in_common and "if-nez v14" in s:
                out.append("    const/4 v14, 0x1\n")
                changed += 1
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ PackageParser.smali patched")
        else:
            p("  ℹ️ PackageParser.smali không cần thay đổi")
        tgt2 = find_one(smali_root, "PackageParser$PackageParserException.smali")
        if tgt2:
            lines = tgt2.read_text(encoding="utf-8").splitlines(True)
            out, changed2 = [], 0
            for line in lines:
                out.append(line)
                if "iput p1, p0, Landroid/content/pm/PackageParser$PackageParserException;->error:I" in line:
                    out.append("    const/4 p1, 0x0\n")
                    changed2 += 1
            if changed2:
                overwrite(tgt2, "".join(out))
                p("  ✅ PackageParser$PackageParserException.smali patched")
        for fn in ("PackageParser$SigningDetails.smali", "SigningDetails.smali"):
            tgt3 = find_one(smali_root, fn)
            if not tgt3:
                continue
            txt = tgt3.read_text(encoding="utf-8")
            orig = txt
            txt = re.sub(
                r"(\.method[^\n]*checkCapability[^\n]*\n)(.*?)(\.end method)",
                r"\1    .registers 3\n    const/4 p0, 0x1\n    return p0\n\3",
                txt,
                flags=re.DOTALL,
            )
            txt = re.sub(
                r"(\.method[^\n]*hasAncestorOrSelf[^\n]*\n)(.*?)(\.end method)",
                r"\1    .registers 2\n    const/4 p0, 0x1\n    return p0\n\3",
                txt,
                flags=re.DOTALL,
            )
            if txt != orig:
                overwrite(tgt3, txt)
                p(f"  ✅ {fn} patched")

    def patch_v2_verifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureSchemeV2Verifier.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSignatureSchemeV2Verifier.smali")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, idxs = [], False, []
        for line in lines:
            s = line.strip()
            if (
                s.startswith(".method")
                and "verifySigner(Ljava/nio/ByteBuffer;Ljava/util/Map;Ljava/security/cert/CertificateFactory;)" in s
            ):
                in_m = True
            elif in_m and s.startswith(".end method"):
                in_m = False
            if in_m and s == "move-result v0":
                idxs.append(len(out))
            out.append(line)
        if idxs:
            out[idxs[-1]] = "    const/4 v0, 0x1\n"
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureSchemeV2Verifier.smali patched")

    def patch_v3_verifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureSchemeV3Verifier.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSignatureSchemeV3Verifier.smali")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for line in lines:
            s = line.strip()
            if (
                s.startswith(".method")
                and "verifySigner(Ljava/nio/ByteBuffer;Ljava/util/Map;Ljava/security/cert/CertificateFactory;)" in s
            ):
                in_m = True
            elif in_m and s.startswith(".end method"):
                in_m = False
            if in_m and s == "move-result v0":
                k = len(out) - 1
                while k >= 0 and out[k].strip() == "":
                    k -= 1
                if (
                    k >= 0
                    and out[k].strip()
                    == "invoke-static {v9, v3}, Ljava/security/MessageDigest;->isEqual([B[B)Z"
                ):
                    out.append("    const/4 v0, 0x1\n")
                    changed = True
                    continue
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureSchemeV3Verifier.smali patched")

    def patch_apksignatureverifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureVerifier.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSignatureVerifier.smali")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "getMinimumSignatureSchemeVersionForTargetSdk" in s:
                in_m = True
                out.append(line)
                out.append("    .registers 1\n")
                out.append("    const/4 v0, 0x0\n")
                out.append("    return v0\n")
                changed = True
                continue
            elif in_m and s.startswith(".end method"):
                out.append(line)
                in_m = False
                continue
            elif in_m:
                continue
            if "invoke-static {p0, p1, p3}, Landroid/util/apk/ApkSignatureVerifier;->verifyV1Signature(" in s:
                out.append("    const p3, 0x0\n")
                changed = True
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureVerifier.smali patched")

    def patch_apksigningblockutils(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSigningBlockUtils.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSigningBlockUtils.smali")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "verifyIntegrityFor1MbChunkBasedAlgorithm" in s:
                in_m = True
            elif in_m and s.startswith(".end method"):
                in_m = False
            if in_m and s == "move-result v7":
                out.append("    const/4 v7, 0x1\n")
                changed = True
                continue
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSigningBlockUtils.smali patched")

    def patch_strictjar(smali_root: Path) -> None:
        v = find_one(smali_root, "StrictJarVerifier.smali")
        if v:
            lines = v.read_text(encoding="utf-8").splitlines(True)
            out, in_m, changed = [], False, False
            for line in lines:
                s = line.strip()
                if s.startswith(".method") and "verifyMessageDigest" in s:
                    in_m = True
                    out.append(line)
                    out.append("    .registers 2\n")
                    out.append("    const/4 v0, 0x1\n")
                    out.append("    return v0\n")
                    changed = True
                    continue
                if in_m and s.startswith(".end method"):
                    out.append(line)
                    in_m = False
                    continue
                if in_m:
                    continue
                out.append(line)
            if changed:
                overwrite(v, "".join(out))
                p("  ✅ StrictJarVerifier.smali patched")
        f = find_one(smali_root, "StrictJarFile.smali")
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
            overwrite(f, "".join(out))
            p("  ✅ StrictJarFile.smali patched")

        parsing_file = find_one(smali_root, "ParsingPackageUtils.smali")
        if parsing_file:
            lines = parsing_file.read_text(encoding="utf-8").splitlines(True)
            out, in_method, in_parseSharedUser, found_if_eqz, changed = [], False, False, False, False
            for line in lines:
                s = line.strip()
                if s.startswith(".method") and "parseSharedUser" in s:
                    in_method = True
                    in_parseSharedUser = True
                    out.append(line)
                    continue
                if in_method and s.startswith(".end method"):
                    in_method = False
                    in_parseSharedUser = False
                    found_if_eqz = False
                    out.append(line)
                    continue
                if in_parseSharedUser and s == "if-eqz v4" and not found_if_eqz:
                    found_if_eqz = True
                    changed = True
                    out.append("    const/4 v4, 0x0\n")
                    out.append(line)
                    continue
                out.append(line)
            if changed:
                overwrite(parsing_file, "".join(out))
                p("  ✅ ParsingPackageUtils.smali patched")

    def patch_services(smali_root: Path) -> None:
        f1 = find_one(smali_root, "PackageManagerServiceUtils.smali")
        if f1:
            lines = f1.read_text(encoding="utf-8").splitlines(True)
            out, in_m, changed = [], False, False
            for ln in lines:
                s = ln.strip()
                if s.startswith(".method") and "checkDowngrade" in s:
                    in_m = True
                    out.append(ln)
                    out.append("    .locals 0\n    return-void\n")
                    changed = True
                    continue
                if in_m and s.startswith(".end method"):
                    out.append(ln)
                    in_m = False
                    continue
                if in_m:
                    continue
                out.append(ln)
            if changed:
                overwrite(f1, "".join(out))
                p("  ✅ PackageManagerServiceUtils.smali patched")
        f2 = find_one(smali_root, "KeySetManagerService.smali")
        if f2:
            lines = f2.read_text(encoding="utf-8").splitlines(True)
            out, in_m, changed = [], False, False
            for ln in lines:
                s = ln.strip()
                if s.startswith(".method") and "shouldCheckUpgradeKeySetLocked" in s:
                    in_m = True
                    out.append(ln)
                    out.append("    .locals 1\n    const/4 v0, 0x0\n    return v0\n")
                    changed = True
                    continue
                if in_m and s.startswith(".end method"):
                    out.append(ln)
                    in_m = False
                    continue
                if in_m:
                    continue
                out.append(ln)
            if changed:
                overwrite(f2, "".join(out))
                p("  ✅ KeySetManagerService.smali patched")
        f3 = find_one(smali_root, "InstallPackageHelper.smali")
        if f3:
            lines = f3.read_text(encoding="utf-8").splitlines(True)
            out, changed = [], 0
            i = 0
            while i < len(lines):
                ln = lines[i]
                s = ln.strip()
                if "if-eqz v12" in s:
                    j = i + 1
                    while j < len(lines) and lines[j].strip() == "":
                        j += 1
                    if (
                        j < len(lines)
                        and lines[j].strip()
                        == "invoke-interface {p1}, Lcom/android/server/pm/pkg/AndroidPackage;->isLeavingSharedUser()Z"
                    ):
                        out.append("    const/4 v0, 0x1\n")
                        changed += 1
                out.append(ln)
                i += 1
            if changed:
                overwrite(f3, "".join(out))
                p("  ✅ InstallPackageHelper")
        f4 = find_one(smali_root, "ReconcilePackageUtils.smali")
        if f4:
            txt = f4.read_text(encoding="utf-8")
            new = txt.replace("const/4 v0, 0x0", "const/4 v0, 0x1", 1)
            if new != txt:
                overwrite(f4, new)
                p("  ✅ ReconcilePackageUtils.smali patched")

    def patch_miui_pms_impl(smali_root: Path) -> None:
        f = find_one(smali_root, "PackageManagerServiceImpl.smali")
        if not f:
            p("  ⚠️ Không thấy PackageManagerServiceImpl.smali (miui)")
            return
        lines = f.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for ln in lines:
            s = ln.strip()
            if s.startswith(".method") and "verifyIsolationViolation" in s:
                in_m = True
                out.append(ln)
                out.append("    .registers 3\n    return-void\n")
                changed = True
                continue
            if s.startswith(".method") and "canBeUpdate(" in s:
                in_m = True
                out.append(ln)
                out.append("    .registers 2\n    return-void\n")
                changed = True
                continue
            if in_m and s.startswith(".end method"):
                out.append(ln)
                in_m = False
                continue
            if in_m:
                continue
            out.append(ln)
        if changed:
            overwrite(f, "".join(out))
            p("  ✅ PackageManagerServiceImpl.smali patched")

    fw = work_dir / "framework_unpacked"
    sv = work_dir / "services_unpacked"
    mi = work_dir / "miui_services_unpacked"

    fw_smali = [
        fw / "smali_classes",
        fw / "smali_classes4",
        fw / "smali_classes5",
    ]
    sv_smali = [sv / "smali_classes2", sv / "smali_classes", sv / "smali_classes3"]
    mi_smali = [mi / "smali_classes"]

    p("\n📁 Patching framework_unpacked/smali_classes ...")
    if fw_smali[0].exists():
        patch_packageparser(fw_smali[0])
    else:
        p("  ⚠️ Thiếu thư mục:", fw_smali[0])

    p("\n📁 Patching framework_unpacked/smali_classes4 ...")
    if fw_smali[1].exists():
        patch_v2_verifier(fw_smali[1])
        patch_v3_verifier(fw_smali[1])
        patch_apksignatureverifier(fw_smali[1])
        patch_apksigningblockutils(fw_smali[1])
        patch_strictjar(fw_smali[1])
    else:
        p("  ⚠️ Thiếu thư mục:", fw_smali[1])

    if fw_smali[2].exists():
        p("\n📁 Kiểm tra framework_unpacked/smali_classes5 (nếu có file liên quan)...")
    else:
        p("  ℹ️ Bỏ qua smali_classes5 (không có)")

    p("\n📁 Patching services_unpacked ...")
    any_sv = False
    for d in sv_smali:
        if d.exists():
            patch_services(d)
            any_sv = True
    if not any_sv:
        p("  ⚠️ Thiếu toàn bộ thư mục smali trong services_unpacked")

    p("\n📁 Patching miui_services_unpacked/smali_classes ...")
    if mi_smali[0].exists():
        patch_miui_pms_impl(mi_smali[0])
    else:
        p("  ⚠️ Thiếu thư mục:", mi_smali[0])

    print("\n🎉 Hoàn tất Disable Signature Verification A16 (smali-only).")


# ─────────────────────────────────────────────────────────────────────────────
# Integration hook — safe to call from a central jar runner
# ─────────────────────────────────────────────────────────────────────────────
def apply_legacy_signature_bypass(
    work_dir: Path,
    android_major: int,
    flavor: str,
    execute: bool,
) -> SigBypassReport:
    """
    Central integration hook.

    Returns a SigBypassReport (report is NOT written to disk from here;
    caller may use write_sig_bypass_reports() if desired).

    This function does not rebuild/repack — the caller's jar runner is
    responsible for that step.
    """
    patcher = LegendSigBypassPatcher(
        project_dir=work_dir,  # work_dir doubles as the project context
        work_dir=work_dir,
        flavor=flavor,
        android_major=android_major,
        dry_run=not execute,
    )
    return patcher.run(write_report=False)


# ─────────────────────────────────────────────────────────────────────────────
# Patcher class
# ─────────────────────────────────────────────────────────────────────────────
class LegendSigBypassPatcher:
    def __init__(
        self,
        project_dir: Path,
        work_dir: Path,
        flavor: str,
        android_major: int,
        dry_run: bool = True,
    ) -> None:
        self.project_dir  = project_dir
        self.work_dir     = work_dir
        self.flavor       = flavor
        self.android_major = android_major
        self.dry_run      = dry_run

    def run(self, write_report: bool = True) -> SigBypassReport:
        norm = _normalise_flavor(self.flavor)
        mode = "DRY RUN" if self.dry_run else "EXECUTE"

        print(f"\n[sig_bypass] === Legend Signature Bypass ({mode}) ===")
        print(f"[sig_bypass] Flavor       : {self.flavor}")
        print(f"[sig_bypass] Android major: {self.android_major}")
        print(f"[sig_bypass] Work dir     : {self.work_dir}")

        report = SigBypassReport(
            flavor=self.flavor,
            android_major=self.android_major,
            project_path=str(self.project_dir),
            work_dir=str(self.work_dir),
            selected_function="",
            status="",
        )

        # ── Flavor guard ──────────────────────────────────────────────────────
        if norm not in _LEGEND_FLAVORS:
            msg = f"Flavor '{self.flavor}' is not a Legend flavor; signature bypass stage skipped."
            report.status = "SKIPPED_NON_LEGEND"
            report.selected_function = "(none)"
            report.warnings.append(msg)
            print(f"[sig_bypass] SKIPPED — {msg}")
            if write_report:
                write_sig_bypass_reports(report, _REPORTS_DIR)
            return report

        # ── Android version guard ─────────────────────────────────────────────
        if self.android_major not in (14, 15, 16):
            msg = f"Android major {self.android_major} is not supported (14/15/16); skipping."
            report.status = "SKIPPED_UNSUPPORTED_ANDROID"
            report.selected_function = "(none)"
            report.warnings.append(msg)
            print(f"[sig_bypass] SKIPPED — {msg}")
            if write_report:
                write_sig_bypass_reports(report, _REPORTS_DIR)
            return report

        # ── Select function ───────────────────────────────────────────────────
        if self.android_major in (14, 15):
            report.selected_function = "disable_signature_verification_a14_15"
        else:
            report.selected_function = "disable_signature_verification_a16"

        print(f"[sig_bypass] Function     : {report.selected_function}")

        # ── Check expected workspace folders ──────────────────────────────────
        expected = [self.work_dir / d for d in _EXPECTED_FOLDERS]
        report.folders_checked = [str(p) for p in expected]
        for p in expected:
            if p.exists():
                report.folders_present.append(str(p))
            else:
                report.folders_missing.append(str(p))
                report.warnings.append(f"Expected folder missing: {p}")

        if report.folders_missing:
            print(f"[sig_bypass] Missing workspace folders: {len(report.folders_missing)}")
            for m in report.folders_missing:
                print(f"[sig_bypass]   MISSING: {m}")

        # ── Dry-run: report intent, touch nothing ─────────────────────────────
        if self.dry_run:
            report.status = "DRY_RUN"
            print(f"[sig_bypass] DRY RUN — would call {report.selected_function}(work_dir)")
            print(f"[sig_bypass] No files modified.")
            if write_report:
                write_sig_bypass_reports(report, _REPORTS_DIR)
            return report

        # ── Execute ───────────────────────────────────────────────────────────
        try:
            if self.android_major in (14, 15):
                disable_signature_verification_a14_15(self.work_dir)
            else:
                disable_signature_verification_a16(self.work_dir)
            report.status = "APPLIED"
            print(f"[sig_bypass] APPLIED — {report.selected_function} completed.")
        except Exception as exc:
            tb = traceback.format_exc()
            report.status = "FAILED"
            report.errors.append(str(exc))
            report.errors.append(tb)
            print(f"[sig_bypass] FAILED: {exc}")

        if write_report:
            write_sig_bypass_reports(report, _REPORTS_DIR)
        return report


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────
def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m factory.patch.legend.signature_bypass_legacy",
        description="DeadZone Legend — legacy Signature Verification Bypass patch stage",
    )
    parser.add_argument(
        "--project", required=True, metavar="PATH",
        help="Path to unpacked ROM project directory (also used as work_dir base)",
    )
    parser.add_argument(
        "--flavor", required=True, metavar="FLAVOR",
        help="Build flavor (must be legend/deadzone_legend; others are skipped)",
    )
    parser.add_argument(
        "--android-major", required=True, type=int, metavar="N",
        help="Android major version (14, 15, or 16)",
    )
    parser.add_argument(
        "--execute", action="store_true",
        help="Actually apply patches (omit for dry-run)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    project_dir = Path(args.project).expanduser().resolve()

    if not project_dir.exists():
        print(f"[sig_bypass] ERROR: project directory not found: {project_dir}", file=sys.stderr)
        return 1

    patcher = LegendSigBypassPatcher(
        project_dir=project_dir,
        work_dir=project_dir,
        flavor=args.flavor,
        android_major=args.android_major,
        dry_run=not args.execute,
    )
    report = patcher.run(write_report=True)
    return 0 if report.status != "FAILED" else 1


if __name__ == "__main__":
    sys.exit(main())
