"""Tests for ROM format detection in the unpack stage.

Verifies that eu_rom_adapter.inspect_rom_source() + UnpackPipeline correctly
identify which adapter path to take for each ROM layout:
  - payload.bin            → SOURCE_PAYLOAD
  - images/super.img       → SOURCE_SUPER_IMG (preferred images/ variant)
  - super.img.0/1/2        → SOURCE_SPLIT_SUPER
  - *.new.dat.br           → SOURCE_NEW_DAT_BR
  - nothing recognised     → SOURCE_UNKNOWN
  - cust.img.* alongside   → cust_img_path populated (best-effort)
  - dynamic_partitions_op_list present → original_partition_sizes populated
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.unpack.eu_rom_adapter import (
    SOURCE_NEW_DAT_BR,
    SOURCE_PAYLOAD,
    SOURCE_SPLIT_SUPER,
    SOURCE_SUPER_IMG,
    SOURCE_SUPER_IMG_ZST,
    SOURCE_UNKNOWN,
    STATUS_FAILED,
    STATUS_OK,
    inspect_rom_source,
)


# ── Helpers ───────────────────────────────────────────────────────────────────

def _dirs(tmp: str):
    base = Path(tmp)
    return base / "rom", base / "work", base / "reports"


def _write(path: Path, content: bytes = b"x") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


def _text(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


# ── Single-signal detection ───────────────────────────────────────────────────

def test_detect_payload():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "payload.bin")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_PAYLOAD
        assert info.status == STATUS_OK


def test_detect_super_img_flat():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        sup = _write(rom_dir / "super.img", b"super")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SUPER_IMG
        assert info.normalized_path == sup


def test_detect_super_img_under_images_dir():
    """images/super.img must be preferred over a root-level super.img."""
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        img_sup = _write(rom_dir / "images" / "super.img", b"images_super")
        _write(rom_dir / "super.img", b"root_super")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SUPER_IMG
        assert info.normalized_path == img_sup


def test_detect_split_super():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img.0", b"A")
        _write(rom_dir / "super.img.1", b"B")
        _write(rom_dir / "super.img.2", b"C")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SPLIT_SUPER
        assert info.status == STATUS_OK
        assert info.normalized_path is not None
        assert info.normalized_path.read_bytes() == b"ABC"


def test_detect_new_dat_br():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "system.new.dat.br", b"br")
        _write(rom_dir / "vendor.new.dat.br", b"br")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_NEW_DAT_BR
        assert info.status == STATUS_OK


def test_detect_unknown():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "readme.txt", b"nothing here")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_UNKNOWN
        assert info.status == STATUS_OK


# ── Priority ordering ─────────────────────────────────────────────────────────

def test_split_super_beats_payload_and_new_dat_br():
    """split_super has highest priority when present alongside other signals."""
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "payload.bin")
        _write(rom_dir / "system.new.dat.br", b"br")
        _write(rom_dir / "super.img.0", b"A")
        _write(rom_dir / "super.img.1", b"B")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SPLIT_SUPER


def test_super_img_beats_payload():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img", b"super")
        _write(rom_dir / "payload.bin")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SUPER_IMG


def test_payload_beats_new_dat_br():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "payload.bin")
        _write(rom_dir / "system.new.dat.br", b"br")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_PAYLOAD


# ── cust.img.* merge alongside split super ───────────────────────────────────

def test_cust_parts_merged_alongside_split_super():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img.0", b"S0")
        _write(rom_dir / "super.img.1", b"S1")
        _write(rom_dir / "cust.img.0", b"C0")
        _write(rom_dir / "cust.img.1", b"C1")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SPLIT_SUPER
        assert info.cust_img_path is not None
        assert info.cust_img_path.exists()
        assert info.cust_img_path.read_bytes() == b"C0C1"


def test_cust_parts_merged_alongside_super_img():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img", b"super_data")
        _write(rom_dir / "cust.img.0", b"X0")
        _write(rom_dir / "cust.img.1", b"X1")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SUPER_IMG
        assert info.cust_img_path is not None
        assert info.cust_img_path.read_bytes() == b"X0X1"


def test_cust_absent_means_none():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img", b"super")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.cust_img_path is None


# ── dynamic_partitions_op_list → original_partition_sizes ────────────────────

def test_op_list_sizes_populated_with_split_super():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img.0", b"A")
        _write(rom_dir / "super.img.1", b"B")
        _text(rom_dir / "dynamic_partitions_op_list",
              "add_group main_a 8000000000\nadd_group main_b 0\n")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert "main" in info.original_partition_sizes
        assert info.original_partition_sizes["main"] == 8000000000


def test_op_list_absent_means_empty_sizes():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img", b"super")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.original_partition_sizes == {}


def test_op_list_zero_size_group_excluded():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img", b"super")
        _text(rom_dir / "dynamic_partitions_op_list", "add_group placeholder_b 0\n")

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.original_partition_sizes == {}


# ── Report is always written ──────────────────────────────────────────────────

def test_report_written_for_every_layout():
    layouts = [
        {"payload.bin": b"payload"},
        {"super.img": b"super"},
        {"super.img.0": b"A", "super.img.1": b"B"},
        {"system.new.dat.br": b"br"},
        {"random.txt": b"data"},
    ]
    for files in layouts:
        with tempfile.TemporaryDirectory() as tmp:
            rom_dir, work_dir, reports_dir = _dirs(tmp)
            for name, content in files.items():
                _write(rom_dir / name, content)
            inspect_rom_source(rom_dir, work_dir, reports_dir)
            assert (reports_dir / "eu_rom_adapter_report.txt").exists(), (
                f"Report missing for layout {list(files)}"
            )


# ── Split-super failure propagates correctly ──────────────────────────────────

def test_split_super_gap_yields_failed_status():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "super.img.0", b"A")
        _write(rom_dir / "super.img.2", b"C")  # part 1 missing

        info = inspect_rom_source(rom_dir, work_dir, reports_dir)

        assert info.source_type == SOURCE_SPLIT_SUPER
        assert info.status == STATUS_FAILED


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
            import traceback
            print(f"  FAIL  {t.__name__}: {exc}")
            traceback.print_exc()
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
