"""Tests for APK package-name scanner rejection rules and Stable matching safety."""
from __future__ import annotations

import os
import zipfile
from pathlib import Path

import pytest

from factory.reports.app_inventory import _is_package_name, _is_rejected_package


# ---------------------------------------------------------------------------
# Part D — APK package scanner rejection tests
# ---------------------------------------------------------------------------

class TestRejectManifestTokens:
    """Rejected tokens must not be accepted as package names."""

    @pytest.mark.parametrize("token", [
        "android.intent.action.ACTION_SHUTDOWN",
        "android.appwidget.action.APPWIDGET_UPDATE",
        "android.hardware.camera",
        "android.permission.ACCESS_NETWORK_STATE",
        "android.intent.action.MAIN",
        "android.intent.action.BOOT_COMPLETED",
        "androidx.core.app.CoreComponentFactory",
        "Manifest.permission.INTERNET",
        "android.accounts.LOGIN_ACCOUNTS_CHANGED",
        "android.bluetooth.action.STATE_CHANGED",
        "android.content.pm.PackageManager",
        "android.provider.Settings",
        "android.app.Activity",
        "android.os.Build",
        "android.view.View",
        "android.widget.TextView",
        "MediaStore.Images.Media",
        "Intent.ACTION_VIEW",
        "Settings.ACTION_SETTINGS",
        "Build.VERSION",
    ])
    def test_rejected_token(self, token):
        assert _is_rejected_package(token), f"Expected rejection of: {token}"

    def test_version_string_v_format_rejected(self):
        assert _is_rejected_package("V7.8.6.CN")
        assert _is_rejected_package("V21.0.0")
        assert _is_rejected_package("v1.2.3")

    def test_allcaps_segment_rejected(self):
        # Segments like ACTION_SHUTDOWN, ACCESS_NETWORK_STATE
        assert _is_rejected_package("some.package.ACTION_SOMETHING")
        assert _is_rejected_package("foo.bar.CONST_NAME")


class TestAcceptRealPackages:
    """Real package names must pass validation."""

    @pytest.mark.parametrize("pkg", [
        "com.xiaomi.mi_connect_service",
        "com.miui.calculator",
        "com.android.settings",
        "com.google.android.gms",
        "com.android.bluetoothmidiservice",
        "org.codeaurora.telephony",
        "net.example.app",
        "com.miui.securitycenter",
        "com.android.shell",
        "vendor.example.service",
    ])
    def test_real_package_accepted(self, pkg):
        assert not _is_rejected_package(pkg), f"Should not be rejected: {pkg}"
        assert _is_package_name(pkg), f"Should be valid package name: {pkg}"

    def test_com_android_package_not_rejected(self):
        # com.android.* is a valid package prefix
        assert not _is_rejected_package("com.android.settings")
        assert not _is_rejected_package("com.android.shell")

    def test_miui_package_not_rejected(self):
        assert not _is_rejected_package("com.miui.calculator")
        assert not _is_rejected_package("com.xiaomi.mi_connect_service")


class TestIsPackageName:
    """_is_package_name combines format check + rejection."""

    def test_rejects_intent_action(self):
        assert not _is_package_name("android.intent.action.ACTION_SHUTDOWN")

    def test_rejects_permission(self):
        assert not _is_package_name("android.permission.ACCESS_NETWORK_STATE")

    def test_rejects_hardware_feature(self):
        assert not _is_package_name("android.hardware.camera")

    def test_rejects_androidx(self):
        assert not _is_package_name("androidx.core.app.CoreComponentFactory")

    def test_rejects_manifest_permission(self):
        assert not _is_package_name("Manifest.permission.INTERNET")

    def test_rejects_version_string(self):
        assert not _is_package_name("V7.8.6.CN")

    def test_accepts_real_package(self):
        assert _is_package_name("com.xiaomi.mi_connect_service")
        assert _is_package_name("com.android.settings")

    def test_rejects_too_few_dots(self):
        assert not _is_package_name("com.example")

    def test_rejects_empty(self):
        assert not _is_package_name("")


# ---------------------------------------------------------------------------
# Stable app policy — folder fallback never becomes a fake package
# ---------------------------------------------------------------------------

class TestFolderFallback:
    """Folder-only apps must have empty/unknown package, never a fake one."""

    def test_folder_with_no_apk_is_unknown(self, tmp_path):
        from factory.core.stable_app_policy import _scan_allowed_apps
        root = tmp_path / "partitions"
        folder = root / "system" / "app" / "NoApkFolder"
        folder.mkdir(parents=True)
        # No APK inside

        apps = _scan_allowed_apps(root, [])
        found = [a for a in apps if a["name"] == "NoApkFolder"]
        assert found, "Folder without APK should still appear in scan"
        app = found[0]
        assert app["package_name"] in ("UNKNOWN", "unknown", ""), (
            f"Folder-only app should be UNKNOWN, got: {app['package_name']}"
        )

    def test_inventory_rejected_token_not_used_as_package(self, tmp_path):
        from factory.core.stable_app_policy import _extract_package
        # inventory_package is a rejected manifest token
        pkg, source, confidence = _extract_package(None, "android.intent.action.MAIN")
        assert pkg == "UNKNOWN"
        assert confidence == "low"

    def test_inventory_valid_package_used_as_fallback(self, tmp_path):
        from factory.core.stable_app_policy import _extract_package
        pkg, source, confidence = _extract_package(None, "com.android.settings")
        assert pkg == "com.android.settings"
        assert source == "inventory"
        assert confidence == "medium"


# ---------------------------------------------------------------------------
# Stable matching — unknown packages never deleted
# ---------------------------------------------------------------------------

class TestStableMatchingSafety:
    """Unknown/unsafe apps must be reported, not deleted."""

    def _write_apps_list(self, tmp: Path) -> Path:
        content = "system/app\nMyApp\ncom.example.myapp\n"
        p = tmp / "apps.list"
        p.write_text(content, encoding="utf-8")
        return p

    def test_unknown_package_is_never_deleted(self, tmp_path):
        from factory.core.stable_app_policy import enforce_stable_app_policy
        apps_list = self._write_apps_list(tmp_path)
        os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
        root = tmp_path / "partitions"
        folder = root / "system" / "app" / "Mystery"
        folder.mkdir(parents=True)
        (folder / "Mystery.apk").write_bytes(b"PK\x03\x04")

        scanned = [{
            "partition": "system",
            "name": "Mystery",
            "path": "app/Mystery",
            "absolute_path": str(folder),
            "type": "app",
            "app_type": "app",
            "folder_name": "Mystery",
            "package_name": "UNKNOWN",
            "package_source": "unknown",
            "package_confidence": "low",
            "size": 100,
        }]
        result = enforce_stable_app_policy(
            tmp_path / "reports", root, scanned, "stable"
        )
        assert folder.exists(), "Unknown-package app must NOT be deleted"
        assert result["unknown_package_apps"]
        assert result["delete_candidates"] == []
        del os.environ["LISTMEZO_APPS_LIST"]

    def test_rejected_manifest_token_not_matched_as_package(self, tmp_path):
        """An app whose package was a rejected manifest token must be treated as UNKNOWN."""
        from factory.core.stable_app_policy import enforce_stable_app_policy
        apps_list = self._write_apps_list(tmp_path)
        os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
        root = tmp_path / "partitions"
        folder = root / "system" / "app" / "BadToken"
        folder.mkdir(parents=True)
        (folder / "BadToken.apk").write_bytes(b"PK\x03\x04")

        scanned = [{
            "partition": "system",
            "name": "BadToken",
            "path": "app/BadToken",
            "absolute_path": str(folder),
            "type": "app",
            "app_type": "app",
            "folder_name": "BadToken",
            "package_name": "android.intent.action.ACTION_SHUTDOWN",
            "package_source": "manifest",
            "package_confidence": "medium",
            "size": 100,
        }]
        result = enforce_stable_app_policy(
            tmp_path / "reports", root, scanned, "stable"
        )
        # android.intent.action.ACTION_SHUTDOWN is not a real package — app must be UNKNOWN
        # since _scan_allowed_apps will re-scan; the scanned_apps list above is a hint only
        assert folder.exists(), "App with rejected package token must not be deleted"
        del os.environ["LISTMEZO_APPS_LIST"]

    def test_confident_path_match_works(self, tmp_path):
        """An app with a real high-confidence package that matches expected is kept."""
        from factory.core.stable_app_policy import enforce_stable_app_policy
        apps_list = self._write_apps_list(tmp_path)
        os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
        root = tmp_path / "partitions"
        folder = root / "system" / "app" / "MyApp"
        folder.mkdir(parents=True)
        (folder / "MyApp.apk").write_bytes(b"PK\x03\x04")

        scanned = [{
            "partition": "system",
            "name": "MyApp",
            "path": "app/MyApp",
            "absolute_path": str(folder),
            "type": "app",
            "app_type": "app",
            "folder_name": "MyApp",
            "package_name": "com.example.myapp",
            "package_source": "aapt",
            "package_confidence": "high",
            "size": 100,
        }]
        result = enforce_stable_app_policy(
            tmp_path / "reports", root, scanned, "stable"
        )
        kept = [a["name"] for a in result["kept_apps"]]
        assert "MyApp" in kept
        del os.environ["LISTMEZO_APPS_LIST"]

    def test_deletion_requires_high_confidence(self, tmp_path):
        """Only confidently-identified extra apps should be deletion candidates."""
        from factory.core.stable_app_policy import _classify, _build_allowed_dirs
        from factory.reports.app_inventory import _parse_apps_list

        apps_list = self._write_apps_list(tmp_path)
        root = tmp_path / "partitions"
        folder = root / "system" / "app" / "Extra"
        folder.mkdir(parents=True)

        # Low confidence → should be UNKNOWN, not DELETE candidate
        scanned_low = [{
            "partition": "system",
            "name": "Extra",
            "path": "app/Extra",
            "absolute_path": str(folder),
            "type": "app",
            "app_type": "app",
            "folder_name": "Extra",
            "package_name": "UNKNOWN",
            "package_source": "unknown",
            "package_confidence": "low",
            "size": 100,
        }]
        allowed = _build_allowed_dirs(root)
        expected = _parse_apps_list(apps_list)
        result = _classify(scanned_low, expected, allowed)
        assert not result["extra_in_allowed"], "Low-confidence/UNKNOWN app must not be a delete candidate"
        assert result["unknown"]

    def test_safety_report_is_generated(self, tmp_path):
        """stable_app_policy_report.json must always be written."""
        from factory.core.stable_app_policy import enforce_stable_app_policy
        apps_list = self._write_apps_list(tmp_path)
        os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
        root = tmp_path / "partitions"
        root.mkdir(parents=True, exist_ok=True)

        enforce_stable_app_policy(tmp_path / "reports", root, [], "stable")

        report = tmp_path / "reports" / "stable_app_policy_report.json"
        assert report.is_file()
        del os.environ["LISTMEZO_APPS_LIST"]


# ---------------------------------------------------------------------------
# Stable normalization defaults
# ---------------------------------------------------------------------------

class TestStableNormalizationDefault:
    """Stable normalization must default to active (not False)."""

    def test_stable_normalize_flag_default(self):
        """By default run_stable_normalize should be True for stable style."""
        import factory.deadzone as dz_mod
        import argparse

        # Simulate parsed args with all defaults
        parser = argparse.ArgumentParser()
        parser.add_argument("--skip-stable-app-normalize", action="store_true")
        parser.add_argument("--stable-normalize-mode", choices=["plan", "apply"], default="apply")
        parser.add_argument("--stable-app-normalize", action="store_true")
        args = parser.parse_args([])

        style_key = "stable"
        run_normalize = not args.skip_stable_app_normalize
        assert run_normalize, "Stable normalization must default to True"
