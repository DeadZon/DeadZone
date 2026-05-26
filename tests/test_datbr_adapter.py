"""Tests for factory.unpack.datbr_adapter."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.unpack.datbr_adapter import (
    STATUS_FAILED,
    STATUS_OK,
    STATUS_PARTIAL,
    DatBrPair,
    DatBrResult,
    detect_datbr_pairs,
    find_dynamic_partitions_op_list,
    parse_op_list,
    process_datbr_rom,
    _partition_name_from_br,
)


# ── Helpers ───────────────────────────────────────────────────────────────────

def _dirs(tmp: str):
    base = Path(tmp)
    return base / "rom", base / "work", base / "reports"


def _write(path: Path, content: bytes = b"x") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


def _write_text(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


# ── Partition name extraction ──────────────────────────────────────────────────

def test_partition_name_simple():
    assert _partition_name_from_br(Path("system.new.dat.br")) == "system"


def test_partition_name_vendor():
    assert _partition_name_from_br(Path("vendor.new.dat.br")) == "vendor"


def test_partition_name_odm():
    assert _partition_name_from_br(Path("odm.new.dat.br")) == "odm"


def test_partition_name_mixed_case():
    assert _partition_name_from_br(Path("System.New.Dat.Br")) == "system"


# ── detect_datbr_pairs ────────────────────────────────────────────────────────

def test_detect_pairs_with_matching_transfer_list():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir = Path(tmp) / "rom"
        _write(rom_dir / "system.new.dat.br", b"br")
        _write_text(rom_dir / "system.transfer.list", "4\n100\n0\n0\nnew 2,0,100\n")

        pairs = detect_datbr_pairs(rom_dir)

        assert len(pairs) == 1
        assert pairs[0].partition == "system"
        assert pairs[0].transfer_list is not None
        assert pairs[0].transfer_list.name == "system.transfer.list"


def test_detect_pairs_missing_transfer_list():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir = Path(tmp) / "rom"
        _write(rom_dir / "vendor.new.dat.br", b"br")

        pairs = detect_datbr_pairs(rom_dir)

        assert len(pairs) == 1
        assert pairs[0].partition == "vendor"
        assert pairs[0].transfer_list is None


def test_detect_pairs_multiple_partitions():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir = Path(tmp) / "rom"
        for part in ("system", "vendor", "product", "odm"):
            _write(rom_dir / f"{part}.new.dat.br", b"br")
            _write_text(rom_dir / f"{part}.transfer.list", "4\n10\n0\n0\nnew 2,0,10\n")

        pairs = detect_datbr_pairs(rom_dir)

        assert len(pairs) == 4
        partitions = {p.partition for p in pairs}
        assert partitions == {"system", "vendor", "product", "odm"}
        for pair in pairs:
            assert pair.transfer_list is not None


def test_detect_pairs_empty_dir():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir = Path(tmp) / "rom"
        rom_dir.mkdir()

        pairs = detect_datbr_pairs(rom_dir)

        assert pairs == []


# ── find_dynamic_partitions_op_list ───────────────────────────────────────────

def test_find_op_list_present():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir = Path(tmp) / "rom"
        _write_text(rom_dir / "dynamic_partitions_op_list", "remove_all_groups\n")

        result = find_dynamic_partitions_op_list(rom_dir)

        assert result is not None
        assert result.name == "dynamic_partitions_op_list"


def test_find_op_list_nested():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir = Path(tmp) / "rom"
        _write_text(rom_dir / "META" / "dynamic_partitions_op_list", "remove_all_groups\n")

        result = find_dynamic_partitions_op_list(rom_dir)

        assert result is not None


def test_find_op_list_absent():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir = Path(tmp) / "rom"
        rom_dir.mkdir()

        assert find_dynamic_partitions_op_list(rom_dir) is None


# ── parse_op_list ─────────────────────────────────────────────────────────────

_SAMPLE_OP_LIST = """\
# Remove all existing dynamic partitions and groups before applying full OTA
remove_all_groups
# Add group main_a with maximum size 8388608000
add_group main_a 8388608000
# Add group main_b with maximum size 0
add_group main_b 0
# Add partition system_a to group main_a
add_partition system_a main_a
# Add partition vendor_a to group main_a
add_partition vendor_a main_a
"""


def test_parse_op_list_groups():
    with tempfile.TemporaryDirectory() as tmp:
        p = _write_text(Path(tmp) / "op_list", _SAMPLE_OP_LIST)
        groups, partitions = parse_op_list(p)

        # main_a has size; main_b is 0 so excluded
        assert "main" in groups
        assert groups["main"] == 8388608000


def test_parse_op_list_partitions():
    with tempfile.TemporaryDirectory() as tmp:
        p = _write_text(Path(tmp) / "op_list", _SAMPLE_OP_LIST)
        groups, partitions = parse_op_list(p)

        assert "system_a" in partitions
        assert "vendor_a" in partitions


def test_parse_op_list_ignores_zero_size_groups():
    with tempfile.TemporaryDirectory() as tmp:
        content = "add_group empty_b 0\nadd_group real_a 1000000\n"
        p = _write_text(Path(tmp) / "op_list", content)
        groups, _ = parse_op_list(p)

        assert "empty" not in groups
        assert "real" in groups


def test_parse_op_list_empty_file():
    with tempfile.TemporaryDirectory() as tmp:
        p = _write_text(Path(tmp) / "op_list", "")
        groups, partitions = parse_op_list(p)

        assert groups == {}
        assert partitions == []


# ── process_datbr_rom: fail-fast with no .br files ────────────────────────────

def test_process_no_br_files_fails():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        rom_dir.mkdir()

        result = process_datbr_rom(rom_dir, work_dir, reports_dir)

        assert result.status == STATUS_FAILED
        assert result.error is not None
        assert result.images == {}


# ── process_datbr_rom: report always written ──────────────────────────────────

def test_process_report_always_written():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        rom_dir.mkdir()

        process_datbr_rom(rom_dir, work_dir, reports_dir)

        assert (reports_dir / "datbr_adapter_report.txt").exists()


# ── process_datbr_rom: missing transfer.list is a warning, not a hard failure ─

def test_process_missing_transfer_list_warns():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "system.new.dat.br", b"br_data")
        # intentionally no system.transfer.list

        result = process_datbr_rom(rom_dir, work_dir, reports_dir)

        # Fails because nothing could convert, but warning was recorded
        assert len(result.warnings) >= 1
        assert any("transfer.list" in w.lower() or "system" in w.lower() for w in result.warnings)


# ── process_datbr_rom: op_list sizes propagated ───────────────────────────────

def test_process_op_list_sizes_populated():
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        _write(rom_dir / "system.new.dat.br", b"br")
        _write_text(rom_dir / "dynamic_partitions_op_list",
                    "add_group main_a 9999999999\n")

        result = process_datbr_rom(rom_dir, work_dir, reports_dir)

        assert result.op_list_path is not None
        assert result.original_partition_sizes.get("main") == 9999999999


# ── process_datbr_rom: partial status when some pairs succeed ─────────────────

def test_process_partial_status_on_mixed_results():
    """If one partition has no transfer.list but another fully succeeds (mock),
    status should be PARTIAL or FAILED — never silently OK with missing data."""
    with tempfile.TemporaryDirectory() as tmp:
        rom_dir, work_dir, reports_dir = _dirs(tmp)
        # vendor: has both files but they are not real brotli/sdat data
        _write(rom_dir / "vendor.new.dat.br", b"not_brotli")
        _write_text(rom_dir / "vendor.transfer.list", "4\n1\n0\n0\nnew 2,0,1\n")
        # system: no transfer.list → warning
        _write(rom_dir / "system.new.dat.br", b"br")

        result = process_datbr_rom(rom_dir, work_dir, reports_dir)

        # Both partitions failed (invalid brotli data + missing tl),
        # so overall status must be FAILED not OK.
        assert result.status in (STATUS_FAILED, STATUS_PARTIAL)
        # Warning recorded for system (missing transfer.list)
        assert any("system" in w.lower() for w in result.warnings)


# ── DatBrResult dataclass defaults ───────────────────────────────────────────

def test_datbr_result_defaults():
    r = DatBrResult(status=STATUS_OK, rom_dir=Path("/tmp"))
    assert r.pairs == []
    assert r.images == {}
    assert r.original_partition_sizes == {}
    assert r.warnings == []
    assert r.error is None


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
