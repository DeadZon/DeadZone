from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
MEZO_CORE = ROOT / "third_party" / "mezo_core"
MEZO_SCRIPT = MEZO_CORE / "MEZOBuildRom.py"


def run_mezo_legacy_engine(
    rom_path: Path,
    device: str | None = None,
    soc: str | None = None,
    platform: str | None = None,
    flavor: str | None = None,
) -> None:
    rom_path = Path(rom_path).resolve()

    if not rom_path.is_file():
        raise FileNotFoundError(f"ROM not found: {rom_path}")
    if not MEZO_SCRIPT.is_file():
        raise FileNotFoundError(f"MEZO engine missing: {MEZO_SCRIPT}")

    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    env["DEADZONE_FACTORY"] = "1"
    if device:
        env["DEADZONE_DEVICE_CODENAME"] = device
    if soc:
        env["DEADZONE_SOC"] = soc
    if platform:
        env["DEADZONE_PLATFORM"] = platform
    if flavor:
        env["DEADZONE_FLAVOR"] = flavor

    print(f"[ENGINE] Starting MEZO legacy engine")
    print(f"[ENGINE] Script : {MEZO_SCRIPT}")
    print(f"[ENGINE] ROM    : {rom_path}")
    print(f"[ENGINE] CWD    : {MEZO_CORE}")
    if device:
        print(f"[ENGINE] Device : {device} (DEADZONE_DEVICE_CODENAME)")

    result = subprocess.run(
        [sys.executable, str(MEZO_SCRIPT), str(rom_path)],
        cwd=str(MEZO_CORE),
        env=env,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"MEZOBuildRom.py exited with code {result.returncode}"
        )

    print("[ENGINE] MEZO build completed successfully.")
