"""Tests for image-driven flash script generation."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.output.flash_scripts import (
    _collect_flash_commands,
    _image_to_partition,
    generate_windows_flash_scripts,
)


def test_image_to_partition_super():
    assert _image_to_partition("super.img") == "super"


def test_image_to_partition_boot():
    assert _image_to_partition("boot.img") == "boot_ab"


def test_image_to_partition_init_boot():
    assert _image_to_partition("init_boot.img") == "init_boot_ab"


def test_image_to_partition_vendor_boot():
    assert _image_to_partition("vendor_boot.img") == "vendor_boot_ab"


def test_image_to_partition_vbmeta():
    assert _image_to_partition("vbmeta.img") == "vbmeta_ab"


def test_image_to_partition_vbmeta_system():
    assert _image_to_partition("vbmeta_system.img") == "vbmeta_system_ab"


def test_image_to_partition_lk():
    assert _image_to_partition("lk.img") == "lk_ab"


def test_image_to_partition_tee():
    assert _image_to_partition("tee.img") == "tee_ab"


def test_image_to_partition_scp():
    assert _image_to_partition("scp.img") == "scp_ab"


def test_image_to_partition_dtbo():
    assert _image_to_partition("dtbo.img") == "dtbo_ab"


def test_collect_flash_commands_super_last():
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        for name in ["boot.img", "super.img", "vbmeta.img"]:
            (dp / name).touch()
        commands = _collect_flash_commands(dp)
        partitions = [p for p, _ in commands]
        images = [i for _, i in commands]
        assert images[-1] == "super.img", f"super.img must be last, got {images}"
        assert "super" in partitions


def test_collect_excludes_unsparse():
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        (dp / "boot.img").touch()
        (dp / "system.unsparse.img").touch()
        (dp / "super.img").touch()
        commands = _collect_flash_commands(dp)
        images = [i for _, i in commands]
        assert "system.unsparse.img" not in images


def test_collect_only_present_images():
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        (dp / "boot.img").touch()
        (dp / "dtbo.img").touch()
        (dp / "super.img").touch()
        commands = _collect_flash_commands(dp)
        images = set(i for _, i in commands)
        assert images == {"boot.img", "dtbo.img", "super.img"}


def test_generate_scripts_dry_run():
    with tempfile.TemporaryDirectory() as staging, tempfile.TemporaryDirectory() as imgs:
        ip = Path(imgs)
        for name in ["boot.img", "vbmeta.img", "super.img"]:
            (ip / name).touch()
        result = generate_windows_flash_scripts(
            staging_dir=Path(staging),
            images_dir=ip,
            device="zircon",
            edition="legend",
            device_model="Redmi Note 13 Pro+",
            android_version="16",
            build_incremental="OS3.0.303.0.WNOCNXM",
            execute=False,
        )
        assert result["status"] == "DRY_RUN"
        assert len(result["scripts_generated"]) == 3
        assert result["flash_command_count"] == 3


def test_generate_scripts_missing_metadata():
    with tempfile.TemporaryDirectory() as staging, tempfile.TemporaryDirectory() as imgs:
        ip = Path(imgs)
        (ip / "boot.img").touch()
        result = generate_windows_flash_scripts(
            staging_dir=Path(staging),
            images_dir=ip,
            device="zircon",
            edition="legend",
            device_model=None,  # missing — should fail metadata
            android_version=None,
            build_incremental=None,
            execute=False,
        )
        assert result["status"] == "FAILED"


def test_generate_scripts_execute():
    with tempfile.TemporaryDirectory() as staging, tempfile.TemporaryDirectory() as imgs:
        ip = Path(imgs)
        sp = Path(staging)
        for name in ["boot.img", "vbmeta.img", "super.img"]:
            (ip / name).touch()
        result = generate_windows_flash_scripts(
            staging_dir=sp,
            images_dir=ip,
            device="zircon",
            edition="base",
            device_model="Redmi Note 13 Pro+",
            android_version="16",
            build_incremental="OS3.0.303.0.WNOCNXM",
            execute=True,
        )
        assert result["status"] == "APPLIED"
        for script in result["scripts_generated"]:
            assert (sp / script).is_file()


def test_no_hardcoded_bad_targets():
    """Generated scripts must not contain forbidden targets."""
    with tempfile.TemporaryDirectory() as staging, tempfile.TemporaryDirectory() as imgs:
        ip = Path(imgs)
        sp = Path(staging)
        for name in ["boot.img", "lk.img", "tee.img", "scp.img", "super.img"]:
            (ip / name).touch()
        generate_windows_flash_scripts(
            staging_dir=sp,
            images_dir=ip,
            device="zircon",
            edition="legend",
            device_model="Redmi Note 13 Pro+",
            android_version="16",
            build_incremental="OS3.0.303.0.WNOCNXM",
            execute=True,
        )
        forbidden = ["lk1", "bootloader2", "tee1", "tee2", "scp1", "scp2", "fastboot -w"]
        for script_path in sp.glob("*.bat"):
            text = script_path.read_text(encoding="ascii", errors="replace").lower()
            for bad in forbidden:
                assert bad.lower() not in text, f"{bad!r} found in {script_path.name}"


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_") and callable(v)]
    passed = failed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except Exception as exc:
            print(f"  FAIL  {t.__name__}: {exc}")
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
