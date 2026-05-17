from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_ROOT = REPO_ROOT / "registry"
MEZO_CORE = REPO_ROOT / "third_party" / "mezo_core"
MEZO_SCRIPT = MEZO_CORE / "MEZOBuildRom.py"
