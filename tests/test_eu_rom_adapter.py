"""Tests for factory.unpack.eu_rom_adapter."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.unpack.eu_rom_adapter import (
    SOURCE_NEW_DAT_BR,
    SOURCE_PAYLOAD,
    SOURCE_SPLIT_SUPER,
    SOURCE_SUPER_IMG,
    SOURCE_UNKNOWN,
    STATUS_FAILED,
    STATUS_OK,
    inspect_rom_source,
)


# ── Helpers ───────────────────────────────────────────────────────────────────

def _dirs(tmp: str):
    """Return (rom_dir, work_dir, reports_dir) as Paths inside tmp."""
    base = Path(tmp)
    return base / "rom", base / "work", base / "reports"


def _write(path: Path, content: bytes = b"x") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


# ── Report is always written ──────────────────────────────────────────────────

def test_report_always_written():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        rom_dir.mkdir(parents=True)

        inspect_rom_source(rom_dir, work_dir, reports_dir)

        report = reports_dir / "eu_rom_adapter_report.txt"
        assert report.exists(), "Report file must always be written"
        text = report.read_text(encoding="utf-8")
        assert "Final status" in text


# ── Unknown layout ────────────────────────────────────────────────────────────

def test_unknown_layout():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        rom_dir.mkdir(parents=True)
        _write(rom_dir / "random_file.txt", b"data")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_UNKNOWN
        assert info.status == STATUS_OK
        assert info.normalized_path is None


# ── Payload layout ────────────────────────────────────────────────────────────

def test_payload_layout():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "payload.bin", b"payload_data")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_PAYLOAD
        assert info.status == STATUS_OK
        assert info.normalized_path is None
        assert any(f.name == "payload.bin" for f in info.found_files)


# ── new.dat.br layout ─────────────────────────────────────────────────────────

def test_new_dat_br_layout():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "system.new.dat.br", b"br_data")
        _write(rom_dir / "vendor.new.dat.br", b"br_data")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_NEW_DAT_BR
        assert info.status == STATUS_OK
        assert len(info.found_files) == 2


# ── Normal super.img layout ───────────────────────────────────────────────────

def test_super_img_layout():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        sup = _write(rom_dir / "super.img", b"super_data")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SUPER_IMG
        assert info.status == STATUS_OK
        assert info.normalized_path == sup


def test_super_img_under_images_dir():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        sup = _write(rom_dir / "images" / "super.img", b"super_data")
        _write(rom_dir / "super.img", b"other")  # shallower but "images/" preferred

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SUPER_IMG
        assert info.normalized_path == sup


# ── Split-super layout ────────────────────────────────────────────────────────

def test_split_super_merges_correctly():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        # Write three parts with known payloads
        _write(rom_dir / "super.img.0", b"PART0")
        _write(rom_dir / "super.img.1", b"PART1")
        _write(rom_dir / "super.img.2", b"PART2")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SPLIT_SUPER
        assert info.status == STATUS_OK
        assert info.normalized_path is not None
        assert info.normalized_path.exists()
        merged = info.normalized_path.read_bytes()
        assert merged == b"PART0PART1PART2"


def test_split_super_natural_sort():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        # Write parts out of filesystem order to confirm natural sort
        _write(rom_dir / "super.img.2", b"C")
        _write(rom_dir / "super.img.0", b"A")
        _write(rom_dir / "super.img.1", b"B")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.status == STATUS_OK
        assert info.normalized_path.read_bytes() == b"ABC"


def test_split_super_missing_part_fails():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img.0", b"A")
        _write(rom_dir / "super.img.2", b"C")  # part 1 is missing

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SPLIT_SUPER
        assert info.status == STATUS_FAILED
        assert info.error is not None
        # Merged file must not be left behind on failure
        if info.normalized_path:
            assert not info.normalized_path.exists()


def test_split_super_never_overwrites_inputs():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        p0 = _write(rom_dir / "super.img.0", b"ORIGINAL0")
        p1 = _write(rom_dir / "super.img.1", b"ORIGINAL1")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert p0.read_bytes() == b"ORIGINAL0"
        assert p1.read_bytes() == b"ORIGINAL1"
        # Merged output lives in a different directory
        assert info.normalized_path != p0
        assert info.normalized_path != p1


# ── Priority: split_super beats super.img ─────────────────────────────────────

def test_split_super_takes_priority_over_super_img():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img", b"full_super")
        _write(rom_dir / "super.img.0", b"PART0")
        _write(rom_dir / "super.img.1", b"PART1")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SPLIT_SUPER


# ── Report content validation ─────────────────────────────────────────────────

def test_report_contains_required_fields():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img.0", b"A")
        _write(rom_dir / "super.img.1", b"B")

        inspect_rom_source(rom_dir, work_dir, reports_dir)

        text = (reports_dir / "eu_rom_adapter_report.txt").read_text(encoding="utf-8")
        assert "Detected source type" in text
        assert "Original path" in text
        assert "Normalized path" in text
        assert "Files found" in text
        assert "Final status" in text
        assert STATUS_OK in text


def test_failed_report_contains_error():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img.0", b"A")
        _write(rom_dir / "super.img.2", b"C")  # gap → failure

        inspect_rom_source(rom_dir, work_dir, reports_dir)

        text = (reports_dir / "eu_rom_adapter_report.txt").read_text(encoding="utf-8")
        assert STATUS_FAILED in text


# ── Runner ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    passed = failed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except Exception as exc:
            print(f"  FAIL  {t.__name__}: {exc}")
            import traceback
            traceback.print_exc()
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
