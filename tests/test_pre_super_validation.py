from __future__ import annotations

import pytest

from factory.core.super_builder import PreSuperValidationError, validate_pre_super_images
from factory.core.workspace import create_workspace, write_json


def _layout(ws, group_size=10_000):
    image = ws.images / "vendor.img"
    return {
        "dynamic_images": {"vendor": str(image)},
        "selected_partitions": ["vendor"],
        "partitions": {"vendor": {"allocation_size": 4_000}},
        "group_size": group_size,
    }


def test_image_bigger_than_allowed_partition_fails_before_lpmake(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(b"x" * 5_000)
    write_json(
        ws.reports / "stable_partition_rebuild_report.json",
        {"partitions": [{"partition": "vendor", "original_size": 2_000}]},
    )

    with pytest.raises(PreSuperValidationError) as exc:
        validate_pre_super_images(ws, _layout(ws))

    assert exc.value.payload["error_type"] == "REBUILT_IMAGE_TOO_LARGE"
    assert "vendor.img grew from 2000 to 5000" in exc.value.payload["cause"]


def test_total_group_usage_bigger_than_group_size_fails_before_lpmake(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(b"x" * 3_000)

    with pytest.raises(PreSuperValidationError) as exc:
        validate_pre_super_images(ws, _layout(ws, group_size=3_500))

    assert exc.value.payload["error_type"] == "SUPER_GROUP_SIZE_EXCEEDED"


def test_validation_pass_allows_lpmake(tmp_path):
    ws = create_workspace(tmp_path / "workspace")
    (ws.images / "vendor.img").write_bytes(b"x" * 3_000)

    result = validate_pre_super_images(ws, _layout(ws, group_size=8_000))

    assert result["status"] == "ok"
    assert result["errors"] == []
    assert (ws.reports / "pre_super_image_validation_report.json").is_file()
