from __future__ import annotations

from factory.core.error_classifier import classify_error, classify_from_context


def test_classify_missing_rom():
    result = classify_error("HTTP 404: not found", "download")
    assert result["error_type"] == "MISSING_ROM"
    assert result["stage"] == "download"
    assert result["suggested_fix"]


def test_classify_payload_unpack():
    result = classify_error("payload.bin extraction failed: bad magic", "unpack")
    assert result["error_type"] == "PAYLOAD_UNPACK_FAILED"


def test_classify_image_mount():
    result = classify_error("could not extract partition image from erofs", "image_extraction")
    assert result["error_type"] == "IMAGE_MOUNT_FAILED"


def test_classify_app_scan():
    result = classify_error("apk scan failed on system/app", "app_inventory")
    assert result["error_type"] == "APP_SCAN_FAILED"


def test_classify_patch_failed():
    result = classify_error("apply_style failed for legend patch", "style")
    assert result["error_type"] == "PATCH_FAILED"


def test_classify_super_info_missing():
    result = classify_error("no metadata allocation found in super profile", "super_profile")
    assert result["error_type"] == "SUPER_INFO_MISSING"


def test_classify_lpmake_failed():
    result = classify_error("lpmake returned exit code 1", "super")
    assert result["error_type"] == "LPMAKE_FAILED"


def test_classify_vbmeta():
    result = classify_error("vbmeta patch verification failed", "final_zip")
    assert result["error_type"] == "VBMETA_PATCH_FAILED"


def test_classify_size_policy():
    result = classify_error("Final ZIP size policy failed: exceeds 4.5GB", "size_policy")
    assert result["error_type"] == "FASTBOOT_VALIDATION_FAILED"


def test_classify_zip_validation():
    result = classify_error("zip build failed at final_zip assembly", "final_zip")
    assert result["error_type"] in {"ZIP_VALIDATION_FAILED", "VBMETA_PATCH_FAILED"}


def test_classify_pixeldrain():
    result = classify_error("pixeldrain upload failed: unauthorized", "upload")
    assert result["error_type"] == "PIXELDRAIN_UPLOAD_FAILED"


def test_classify_telegram():
    result = classify_error("telegram API error: bad token", "telegram")
    assert result["error_type"] == "TELEGRAM_FAILED"


def test_classify_unknown_returns_build_failed():
    result = classify_error("something totally unexpected happened", "mystery_stage")
    assert result["error_type"] == "BUILD_FAILED"
    assert result["stage"] == "mystery_stage"


def test_classify_empty_error():
    result = classify_error("", "")
    assert result["error_type"] == "BUILD_FAILED"
    assert isinstance(result["suggested_fix"], str)


def test_classify_result_has_all_fields():
    result = classify_error("lpmake failed", "super")
    required = {"error_type", "stage", "cause", "suggested_fix", "raw_error"}
    assert required <= result.keys()


def test_classify_from_context():
    class FakeCtx:
        failed_stage = "upload"
        failure_error = "pixeldrain upload failed: 403"

    result = classify_from_context(FakeCtx())
    assert result["error_type"] == "PIXELDRAIN_UPLOAD_FAILED"
    assert result["stage"] == "upload"


def test_classify_from_context_empty():
    class EmptyCtx:
        pass

    result = classify_from_context(EmptyCtx())
    assert "error_type" in result
