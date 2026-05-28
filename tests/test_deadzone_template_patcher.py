"""Tests for deadzone_template_patcher and dynamic_flash_commands."""
from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

import pytest

from factory.output.dynamic_flash_commands import (
    bat_flash_lines,
    collect_commands,
    sh_flash_lines,
    skipped_images_report,
)
from factory.output.deadzone_template_patcher import (
    _bat_banner_lines,
    _patch_bat_script,
    _patch_sh_script,
    _replace_between_markers,
    _sh_banner_lines,
    patch_deadzone_template,
    validate_codename,
)

# ── Helpers ───────────────────────────────────────────────────────────────────

def _make_images_dir(tmp_path: Path, names: list[str]) -> Path:
    d = tmp_path / "images"
    d.mkdir()
    for name in names:
        (d / name).write_bytes(b"fake")
    return d


def _deadzone_mezo_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "DeadZone_Mezo"


# ── validate_codename ─────────────────────────────────────────────────────────

def test_codename_match():
    match, err = validate_codename("zorn", "zorn")
    assert match is True
    assert err is None


def test_codename_match_case_insensitive():
    match, err = validate_codename("Zorn", "zorn")
    assert match is True
    assert err is None


def test_codename_mismatch_fails():
    match, err = validate_codename("garnet", "zorn")
    assert match is False
    assert err is not None
    assert "garnet" in err
    assert "zorn" in err


def test_codename_mismatch_force():
    match, err = validate_codename("garnet", "zorn", force=True)
    assert match is False
    assert err is None  # forced — not a hard fail


def test_codename_no_detected():
    match, err = validate_codename("zorn", None)
    assert match is True
    assert err is None


# ── dynamic_flash_commands ────────────────────────────────────────────────────

def test_zorn_images_generate_commands_for_every_packaged_image(tmp_path):
    images = ["boot.img", "vendor_boot.img", "dtbo.img", "vbmeta.img", "super.img"]
    d = _make_images_dir(tmp_path, images)
    cmds = collect_commands(d)
    cmd_images = [img for _, img in cmds]
    for name in images:
        assert name in cmd_images, f"{name} missing from flash commands"


def test_unknown_image_generates_command_dynamically(tmp_path):
    d = _make_images_dir(tmp_path, ["super.img", "random_firmware.img"])
    cmds = collect_commands(d)
    partitions = {p for p, _ in cmds}
    images = {i for _, i in cmds}
    assert "random_firmware.img" in images
    assert "random_firmware_ab" in partitions


def test_no_command_for_super_unsparse(tmp_path):
    d = _make_images_dir(tmp_path, ["super.img", "super.unsparse.img"])
    cmds = collect_commands(d)
    cmd_images = [img for _, img in cmds]
    assert "super.unsparse.img" not in cmd_images


def test_no_command_for_split_super_chunks(tmp_path):
    d = _make_images_dir(tmp_path, ["super.img", "super.img.0", "super.img.1"])
    cmds = collect_commands(d)
    cmd_images = [img for _, img in cmds]
    assert "super.img.0" not in cmd_images
    assert "super.img.1" not in cmd_images


def test_no_command_for_dynamic_partition_when_super_present(tmp_path):
    d = _make_images_dir(tmp_path, ["super.img", "system.img", "vendor.img"])
    cmds = collect_commands(d)
    cmd_images = [img for _, img in cmds]
    assert "system.img" not in cmd_images
    assert "vendor.img" not in cmd_images


def test_super_img_flashes_last(tmp_path):
    d = _make_images_dir(tmp_path, ["boot.img", "dtbo.img", "super.img"])
    cmds = collect_commands(d)
    assert cmds[-1][1] == "super.img"


def test_bat_flash_lines_include_set_active(tmp_path):
    d = _make_images_dir(tmp_path, ["boot.img", "super.img"])
    cmds = collect_commands(d)
    lines = bat_flash_lines(cmds)
    assert lines[0] == "%fastboot% set_active a"
    assert any("boot.img" in l for l in lines)
    assert any("super.img" in l for l in lines)


def test_sh_flash_lines_include_set_active(tmp_path):
    d = _make_images_dir(tmp_path, ["boot.img", "super.img"])
    cmds = collect_commands(d)
    lines = sh_flash_lines(cmds)
    assert lines[0] == "$fastboot set_active a"
    assert any("super.img" in l for l in lines)


def test_skipped_report_identifies_forbidden(tmp_path):
    d = _make_images_dir(tmp_path, ["super.img", "super.unsparse.img", "lpdump.img"])
    skipped = skipped_images_report(d)
    skipped_names = {e["image"] for e in skipped}
    assert "super.unsparse.img" in skipped_names
    assert "lpdump.img" in skipped_names


def test_no_fastboot_w_in_generated_lines(tmp_path):
    d = _make_images_dir(tmp_path, ["boot.img", "super.img"])
    cmds = collect_commands(d)
    all_lines = bat_flash_lines(cmds) + sh_flash_lines(cmds)
    for line in all_lines:
        assert " -w" not in line, f"fastboot -w found in: {line}"


# ── Banner generation ─────────────────────────────────────────────────────────

def test_bat_banner_contains_developer_mezo():
    lines = _bat_banner_lines("zorn", "Free", "16.0", "OS3.0.303.0.WOKCNXM", "CN")
    banner_text = "\n".join(lines)
    assert "Mezo" in banner_text
    assert "Developer" in banner_text


def test_bat_banner_contains_codename():
    lines = _bat_banner_lines("zorn", "Free", "16.0", "OS3.0.303.0.WOKCNXM", "CN")
    banner_text = "\n".join(lines)
    assert "zorn" in banner_text


def test_sh_banner_contains_developer_mezo():
    lines = _sh_banner_lines("zorn", "Free", "16.0", "OS3.0.303.0.WOKCNXM", "CN")
    banner_text = "\n".join(lines)
    assert "Mezo" in banner_text


def test_sh_banner_contains_codename():
    lines = _sh_banner_lines("zorn", "Free", "16.0", "OS3.0.303.0.WOKCNXM", "CN")
    banner_text = "\n".join(lines)
    assert "zorn" in banner_text


# ── _replace_between_markers ──────────────────────────────────────────────────

def test_replace_between_markers_basic():
    lines = [
        "before",
        ":: DEADZONE_BANNER_START",
        "old content",
        ":: DEADZONE_BANNER_END",
        "after",
    ]
    result, found = _replace_between_markers(
        lines,
        ":: DEADZONE_BANNER_START",
        ":: DEADZONE_BANNER_END",
        ["new line 1", "new line 2"],
    )
    assert found is True
    assert "old content" not in result
    assert "new line 1" in result
    assert "before" in result
    assert "after" in result
    assert result[0] == "before"
    assert result[-1] == "after"


def test_replace_between_markers_not_found():
    lines = ["a", "b", "c"]
    result, found = _replace_between_markers(lines, ":: START", ":: END", ["x"])
    assert found is False
    assert result == lines


# ── Script patching ───────────────────────────────────────────────────────────

def _make_minimal_bat(tmp_path: Path, name: str, with_flash: bool = True) -> Path:
    p = tmp_path / name
    lines = [
        "@echo off",
        "cd %~dp0",
        'if "%device%" neq "zircon" echo Compatible devices: zircon & pause & exit /B 1',
        ":: DEADZONE_BANNER_START",
        ":: DEADZONE_BANNER_END",
        "echo Install start",
    ]
    if with_flash:
        lines += [
            "echo flashing",
            ":: DEADZONE_IMAGE_FLASH_START",
            "%fastboot% set_active a",
            ":: DEADZONE_IMAGE_FLASH_END",
            "echo done",
        ]
    p.write_text("\r\n".join(lines) + "\r\n", encoding="utf-8-sig")
    return p


def _make_minimal_sh(tmp_path: Path, name: str, with_flash: bool = True) -> Path:
    p = tmp_path / name
    lines = [
        "#!/bin/sh",
        'if [ "$device" != "zircon" ]; then echo "Compatible devices: zircon"; exit 1; fi',
        "# DEADZONE_BANNER_START",
        "# DEADZONE_BANNER_END",
        "echo Install start",
    ]
    if with_flash:
        lines += [
            "# DEADZONE_IMAGE_FLASH_START",
            "$fastboot set_active a",
            "# DEADZONE_IMAGE_FLASH_END",
            "echo done",
        ]
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return p


def test_bat_script_codename_replaced(tmp_path):
    p = _make_minimal_bat(tmp_path, "test.bat", with_flash=False)
    banner = ["echo banner"]
    content, warns = _patch_bat_script(p, "zorn", banner, None)
    assert "zorn" in content
    assert "zircon" not in content
    assert not warns


def test_sh_script_codename_replaced(tmp_path):
    p = _make_minimal_sh(tmp_path, "test.sh", with_flash=False)
    banner = ["echo banner"]
    content, warns = _patch_sh_script(p, "zorn", banner, None)
    assert "zorn" in content
    assert "zircon" not in content
    assert not warns


def test_bat_flash_section_replaced(tmp_path):
    p = _make_minimal_bat(tmp_path, "install.bat")
    cmds = [("boot_ab", "boot.img"), ("super", "super.img")]
    flash = bat_flash_lines(cmds)
    content, warns = _patch_bat_script(p, "zorn", ["echo banner"], flash)
    assert "boot.img" in content
    assert "super.img" in content
    assert "set_active a" in content
    # Original placeholder still gone, replaced by real commands
    assert content.count("set_active a") == 1  # only one from generated lines
    assert not warns


def test_sh_flash_section_replaced(tmp_path):
    p = _make_minimal_sh(tmp_path, "install.sh")
    cmds = [("boot_ab", "boot.img"), ("super", "super.img")]
    flash = sh_flash_lines(cmds)
    content, warns = _patch_sh_script(p, "zorn", ["echo banner"], flash)
    assert "boot.img" in content
    assert "super.img" in content
    assert not warns


def test_script_body_outside_markers_unchanged(tmp_path):
    p = _make_minimal_bat(tmp_path, "install.bat")
    content, _ = _patch_bat_script(p, "zorn", ["echo banner"], bat_flash_lines([]))
    assert "echo Install start" in content
    assert "echo done" in content


def test_format_data_only_has_no_flash_section(tmp_path):
    p = _make_minimal_bat(tmp_path, "format.bat", with_flash=False)
    content, warns = _patch_bat_script(p, "zorn", ["echo banner"], None)
    # Should not warn about missing flash markers since we passed None
    assert not any("flash markers" in w for w in warns)


# ── patch_deadzone_template end-to-end ───────────────────────────────────────

@pytest.fixture()
def template_dir():
    d = _deadzone_mezo_dir()
    if not d.is_dir():
        pytest.skip("DeadZone_Mezo template directory not found")
    return d


def test_patch_dry_run_succeeds(tmp_path, template_dir):
    images_dir = _make_images_dir(tmp_path, [
        "boot.img", "dtbo.img", "vbmeta.img", "vendor_boot.img", "super.img"
    ])
    result = patch_deadzone_template(
        template_dir=template_dir,
        staging_dir=tmp_path / "staging",
        images_dir=images_dir,
        selected_codename="zorn",
        detected_codename="zorn",
        edition="Free",
        android_version="16.0",
        build_incremental="OS3.0.303.0.WOKCNXM",
        region="CN",
        execute=False,
    )
    assert result["status"] == "DRY_RUN"
    assert result["codename_match"] is True
    assert not result["errors"]


def test_patch_execute_applies_all_scripts(tmp_path, template_dir):
    images_dir = _make_images_dir(tmp_path, [
        "boot.img", "dtbo.img", "vbmeta.img", "vendor_boot.img", "super.img"
    ])
    staging = tmp_path / "staging"
    result = patch_deadzone_template(
        template_dir=template_dir,
        staging_dir=staging,
        images_dir=images_dir,
        selected_codename="zorn",
        detected_codename="zorn",
        edition="Free",
        android_version="16.0",
        build_incremental="OS3.0.303.0.WOKCNXM",
        region="CN",
        execute=True,
    )
    assert result["status"] == "APPLIED"
    assert not result["errors"]
    # All 9 scripts should be patched
    assert len(result["scripts_patched"]) == 9


def test_patch_banner_in_all_scripts(tmp_path, template_dir):
    images_dir = _make_images_dir(tmp_path, ["boot.img", "super.img"])
    staging = tmp_path / "staging"
    patch_deadzone_template(
        template_dir=template_dir,
        staging_dir=staging,
        images_dir=images_dir,
        selected_codename="zorn",
        edition="Free",
        android_version="16.0",
        build_incremental="OS3.0.303.0.WOKCNXM",
        region="CN",
        execute=True,
    )
    for script in staging.glob("*.bat"):
        content = script.read_text(encoding="utf-8-sig", errors="replace")
        assert "Mezo" in content, f"Developer: Mezo missing from {script.name}"
        assert "zorn" in content, f"codename missing from {script.name}"
    for script in staging.glob("*.sh"):
        content = script.read_text(encoding="utf-8", errors="replace")
        assert "Mezo" in content, f"Developer: Mezo missing from {script.name}"
        assert "zorn" in content, f"codename missing from {script.name}"


def test_patch_flash_commands_reference_only_existing_images(tmp_path, template_dir):
    images_dir = _make_images_dir(tmp_path, ["boot.img", "dtbo.img", "super.img"])
    staging = tmp_path / "staging"
    patch_deadzone_template(
        template_dir=template_dir,
        staging_dir=staging,
        images_dir=images_dir,
        selected_codename="zorn",
        edition="Free",
        android_version="16.0",
        build_incremental="OS3.0.303.0.WOKCNXM",
        region="CN",
        execute=True,
    )
    for script in staging.glob("*install*.bat"):
        content = script.read_text(encoding="utf-8-sig", errors="replace")
        for line in content.splitlines():
            if "flash" in line and "images\\" in line:
                img = line.split("images\\")[-1].strip()
                assert (images_dir / img).is_file(), (
                    f"{script.name}: references {img} which is not in images_dir"
                )


def test_codename_mismatch_fails_without_force(tmp_path, template_dir):
    images_dir = _make_images_dir(tmp_path, ["super.img"])
    result = patch_deadzone_template(
        template_dir=template_dir,
        staging_dir=tmp_path / "staging",
        images_dir=images_dir,
        selected_codename="garnet",
        detected_codename="zorn",
        execute=False,
    )
    assert result["status"] == "FAILED"
    assert any("mismatch" in e.lower() or "garnet" in e for e in result["errors"])


def test_codename_match_passes(tmp_path, template_dir):
    images_dir = _make_images_dir(tmp_path, ["super.img"])
    result = patch_deadzone_template(
        template_dir=template_dir,
        staging_dir=tmp_path / "staging",
        images_dir=images_dir,
        selected_codename="zorn",
        detected_codename="zorn",
        execute=False,
    )
    assert result["codename_match"] is True
    assert not any("mismatch" in e.lower() for e in result["errors"])


def test_staging_has_deadzone_mezo_structure(tmp_path, template_dir):
    images_dir = _make_images_dir(tmp_path, ["boot.img", "super.img"])
    staging = tmp_path / "staging"
    patch_deadzone_template(
        template_dir=template_dir,
        staging_dir=staging,
        images_dir=images_dir,
        selected_codename="zorn",
        edition="Free",
        android_version="16.0",
        build_incremental="OS3.0.303.0.WOKCNXM",
        region="CN",
        execute=True,
    )
    assert (staging / "bin" / "windows" / "fastboot.exe").is_file()
    assert (staging / "bin" / "linux" / "fastboot").is_file()
    assert (staging / "bin" / "macos" / "fastboot").is_file()
    assert (staging / "windows_install_and_format_data.bat").is_file()
    assert (staging / "linux_install_and_format_data.sh").is_file()
    assert (staging / "macos_install_and_format_data.sh").is_file()


def test_no_super_unsparse_in_flash_commands(tmp_path, template_dir):
    images_dir = _make_images_dir(tmp_path, ["super.img", "super.unsparse.img", "boot.img"])
    result = patch_deadzone_template(
        template_dir=template_dir,
        staging_dir=tmp_path / "staging",
        images_dir=images_dir,
        selected_codename="zorn",
        edition="Free",
        android_version="16.0",
        build_incremental="OS3.0.303.0.WOKCNXM",
        region="CN",
        execute=False,
    )
    cmd_images = [c["image"] for c in result["flash_commands"]]
    assert "super.unsparse.img" not in cmd_images


def test_report_written(tmp_path, template_dir):
    images_dir = _make_images_dir(tmp_path, ["boot.img", "super.img"])
    reports_dir = tmp_path / "reports"
    patch_deadzone_template(
        template_dir=template_dir,
        staging_dir=tmp_path / "staging",
        images_dir=images_dir,
        selected_codename="zorn",
        detected_codename="zorn",
        edition="Free",
        android_version="16.0",
        build_incremental="OS3.0.303.0.WOKCNXM",
        region="CN",
        execute=False,
        reports_dir=reports_dir,
    )
    report = reports_dir / "dynamic_flash_script_report.txt"
    assert report.is_file()
    text = report.read_text(encoding="utf-8")
    assert "zorn" in text
    assert "DeadZone_Mezo" in text
    assert "flash method changed : false" in text.lower()
