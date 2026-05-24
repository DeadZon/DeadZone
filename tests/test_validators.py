"""Tests for factory validators."""
import sys
import tempfile
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.validators.registry_validator import validate_registry
from factory.validators.package_validator import validate_package
from factory.validators.super_validator import validate_super
from factory.validators.script_validator import validate_script


# ── Registry ──────────────────────────────────────────────────────────────────

def test_validate_known_edition_base():
    r = validate_registry(edition="base")
    assert r["passed"], r["errors"]


def test_validate_known_edition_legend():
    r = validate_registry(edition="legend")
    assert r["passed"], r["errors"]


def test_validate_unknown_edition():
    r = validate_registry(edition="phantom_edition_xyz")
    assert not r["passed"]


def test_validate_known_codename_zircon():
    r = validate_registry(codename="zircon")
    assert r["passed"], r["errors"]


def test_validate_known_codename_garnet():
    r = validate_registry(codename="garnet")
    assert r["passed"], r["errors"]


def test_validate_unknown_codename():
    r = validate_registry(codename="doesnotexist_xyz_999")
    assert not r["passed"]


# ── Package validator ─────────────────────────────────────────────────────────

def _make_zip(path: Path, names: list[str]) -> None:
    with zipfile.ZipFile(path, "w") as zf:
        for n in names:
            zf.writestr(n, b"dummy")


def test_package_validator_valid():
    with tempfile.TemporaryDirectory() as d:
        zp = Path(d) / "test.zip"
        _make_zip(zp, [
            "bin/windows/fastboot.exe",
            "bin/windows/AdbWinApi.dll",
            "bin/windows/AdbWinUsbApi.dll",
            "images/boot.img",
            "images/super.img",
            "windows_install_upgrade.bat",
        ])
        r = validate_package(zp)
        assert r["passed"], r["errors"]


def test_package_validator_missing_tool():
    with tempfile.TemporaryDirectory() as d:
        zp = Path(d) / "test.zip"
        _make_zip(zp, [
            "bin/windows/fastboot.exe",
            # AdbWinApi.dll missing
            "bin/windows/AdbWinUsbApi.dll",
            "images/super.img",
        ])
        r = validate_package(zp)
        assert not r["passed"]
        assert any("AdbWinApi" in e for e in r["errors"])


def test_package_validator_forbidden_sha256():
    with tempfile.TemporaryDirectory() as d:
        zp = Path(d) / "test.zip"
        _make_zip(zp, [
            "bin/windows/fastboot.exe",
            "bin/windows/AdbWinApi.dll",
            "bin/windows/AdbWinUsbApi.dll",
            "images/super.img",
            "sha256sums.txt",
        ])
        r = validate_package(zp)
        assert not r["passed"]


def test_package_validator_no_unsparse():
    with tempfile.TemporaryDirectory() as d:
        zp = Path(d) / "test.zip"
        _make_zip(zp, [
            "bin/windows/fastboot.exe",
            "bin/windows/AdbWinApi.dll",
            "bin/windows/AdbWinUsbApi.dll",
            "images/super.img",
            "images/system.unsparse.img",
        ])
        r = validate_package(zp)
        assert not r["passed"]


# ── Super validator ───────────────────────────────────────────────────────────

def test_super_validator_correct_size():
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        sup = dp / "super.img"
        sup.write_bytes(b"\x00" * 100)
        r = validate_super(dp, expected_size=100)
        assert r["passed"], r["errors"]


def test_super_validator_wrong_size():
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        sup = dp / "super.img"
        sup.write_bytes(b"\x00" * 50)
        r = validate_super(dp, expected_size=9126805504)
        assert not r["passed"]


def test_super_validator_missing():
    with tempfile.TemporaryDirectory() as d:
        r = validate_super(Path(d))
        assert not r["passed"]


def test_super_validator_rejects_unsparse():
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        (dp / "super.img").write_bytes(b"\x00" * 100)
        (dp / "system.unsparse.img").touch()
        r = validate_super(dp, expected_size=100)
        assert not r["passed"]


# ── Script validator ──────────────────────────────────────────────────────────

def test_script_validator_clean():
    with tempfile.TemporaryDirectory() as d:
        sp = Path(d) / "install.bat"
        sp.write_text(
            "@echo off\necho Device : zircon\ncall fastboot flash boot_ab images\\boot.img\n",
            encoding="ascii",
        )
        r = validate_script(sp)
        assert r["passed"], r["errors"]


def test_script_validator_forbidden_wipe():
    with tempfile.TemporaryDirectory() as d:
        sp = Path(d) / "bad.bat"
        sp.write_text("@echo off\nfastboot -w\n", encoding="ascii")
        r = validate_script(sp)
        assert not r["passed"]


def test_script_validator_forbidden_tee1():
    with tempfile.TemporaryDirectory() as d:
        sp = Path(d) / "bad.bat"
        sp.write_text("fastboot flash tee1 images\\tee.img\n", encoding="ascii")
        r = validate_script(sp)
        assert not r["passed"]


def test_script_validator_unknown_in_header():
    with tempfile.TemporaryDirectory() as d:
        sp = Path(d) / "bad.bat"
        sp.write_text("echo Device : unknown\n", encoding="ascii")
        r = validate_script(sp)
        assert not r["passed"]


# ── Build patcher — unknown partition ─────────────────────────────────────────

def test_build_patcher_unknown_partition_fails():
    import tempfile, shutil
    from factory.patch.editions._build_patcher import apply_build_package
    with tempfile.TemporaryDirectory() as build_dir, tempfile.TemporaryDirectory() as root:
        bd = Path(build_dir)
        (bd / "system").mkdir()
        (bd / "bad_unknown_part").mkdir()  # not allowed
        r = apply_build_package(
            root=Path(root),
            build_dir=bd,
            build_url=None,
            edition="gaming",
            execute=False,
        )
        assert r["status"] == "FAILED"
        assert "bad_unknown_part" in str(r.get("unknown_partitions", []))


def test_build_patcher_skipped_when_missing():
    from factory.patch.editions._build_patcher import apply_build_package
    with tempfile.TemporaryDirectory() as root:
        r = apply_build_package(
            root=Path(root),
            build_dir=None,
            build_url=None,
            edition="gaming",
            execute=False,
        )
        assert r["status"] == "SKIPPED_TEMPORARY"


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
