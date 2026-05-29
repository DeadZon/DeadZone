from __future__ import annotations

import json
import tarfile
import tempfile
import unittest
import zipfile
from pathlib import Path

from factory.core.detector import (
    ROM_EU,
    ROM_FASTBOOT_TGZ,
    ROM_PAYLOAD,
    ROM_SPLIT_SUPER,
    detect_rom,
)
from factory.core.workspace import create_workspace


class UniversalIntakeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.ws = create_workspace(self.root / "output" / "workspace", clean=True)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_payload_ota_detection(self) -> None:
        rom = self.root / "zircon-ota_full-OS2.0.1.0.VNCMIXM-user-15.zip"
        with zipfile.ZipFile(rom, "w") as zf:
            zf.writestr("payload.bin", b"payload")
            zf.writestr("payload_properties.txt", "POST_BUILD=google/zircon/zircon:15/AP3A/OS2.0.1.0.VNCMIXM:user/release-keys\n")

        info = detect_rom(rom, self.ws, soc="mtk")

        self.assertEqual(info.rom_type, ROM_PAYLOAD)
        self.assertTrue(info.has_payload)

    def test_fastboot_tgz_detection(self) -> None:
        image = self.root / "boot.img"
        image.write_bytes(b"boot")
        rom = self.root / "zircon_images_OS2.0.1.0.VNCMIXM_20260101.0000.00_15.0_global.tgz"
        with tarfile.open(rom, "w:gz") as tf:
            tf.add(image, arcname="images/boot.img")

        info = detect_rom(rom, self.ws, soc="mtk")

        self.assertEqual(info.rom_type, ROM_FASTBOOT_TGZ)

    def test_xiaomi_eu_zip_detection(self) -> None:
        rom = self.root / "xiaomi.eu_multi_zircon_OS2.0.1.0.VNCMIXM_15.zip"
        with zipfile.ZipFile(rom, "w") as zf:
            zf.writestr("META-INF/com/google/android/updater-script", "ui_print('xiaomi.eu');")
            zf.writestr("system.new.dat.br", b"br")

        info = detect_rom(rom, self.ws, soc="snapdragon")

        self.assertEqual(info.rom_type, ROM_EU)

    def test_split_super_detection(self) -> None:
        rom = self.root / "split"
        rom.mkdir()
        (rom / "super.img.0").write_bytes(b"a")
        (rom / "super.img.1").write_bytes(b"b")

        info = detect_rom(rom, self.ws, soc="mtk")

        self.assertEqual(info.rom_type, ROM_SPLIT_SUPER)
        self.assertTrue(info.has_split_super)

    def test_metadata_json_files_created(self) -> None:
        rom = self.root / "zircon-ota_full-OS2.0.1.0.VNCMIXM-user-15.zip"
        with zipfile.ZipFile(rom, "w") as zf:
            zf.writestr("payload.bin", b"payload")

        detect_rom(rom, self.ws, soc="mtk")

        for name in ("rom_info.json", "device_info.json", "super_layout.json", "partition_map.json"):
            path = self.ws.meta / name
            self.assertTrue(path.is_file(), name)
            self.assertIsInstance(json.loads(path.read_text(encoding="utf-8")), dict)


if __name__ == "__main__":
    unittest.main()
