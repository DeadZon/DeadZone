from pathlib import Path
import yaml

from factory.core.paths import REGISTRY_ROOT

REQUIRED_IMAGES = [
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "vbmeta.img",
    "super.img",
]


class BuildPlan:
    def __init__(self, device: str, soc: str, platform: str, flavor: str):
        self.device = device
        self.soc = soc
        self.platform = platform
        self.flavor = flavor
        self._device_cfg = None
        self._soc_cfg = None
        self._platform_cfg = None
        self._flavor_cfg = None

    def _load_yaml(self, path: Path) -> dict:
        if not path.exists():
            raise FileNotFoundError(f"Registry file not found: {path}")
        with path.open() as f:
            return yaml.safe_load(f)

    def load(self) -> None:
        self._device_cfg = self._load_yaml(
            REGISTRY_ROOT / "devices" / self.soc / f"{self.device}.yml"
        )
        self._soc_cfg = self._load_yaml(REGISTRY_ROOT / "soc" / f"{self.soc}.yml")
        self._platform_cfg = self._load_yaml(
            REGISTRY_ROOT / "platforms" / f"{self.platform}.yml"
        )
        self._flavor_cfg = self._load_yaml(
            REGISTRY_ROOT / "flavors" / f"{self.flavor}.yml"
        )

    def print(self) -> None:
        print("=" * 60)
        print("DeadZone Factory — Build Plan")
        print("=" * 60)
        brand = self._device_cfg.get("brand", "")
        model = self._device_cfg.get("model", "")
        print(f"  Device   : {self.device} ({brand} {model})")
        print(f"  SoC      : {self.soc} ({self._soc_cfg.get('name', '')})")
        print(f"  Platform : {self.platform} ({self._platform_cfg.get('name', '')})")
        print(f"  Flavor   : {self.flavor} ({self._flavor_cfg.get('name', '')})")
        print("-" * 60)
        engine_name = self._soc_cfg.get("engine", {}).get("name", "mezo_legacy_engine")
        print(f"  Engine   : {engine_name}")
        print(f"  Flash    : {self._device_cfg.get('flash_profile', '')}")
        print(f"  VBMeta   : {self._device_cfg.get('vbmeta_policy', '')}")
        print(f"  Super FS : {self._platform_cfg.get('super', {}).get('filesystem', '')}")
        print("-" * 60)
        req = self._device_cfg.get("required_images", [])
        print(f"  Required images: {', '.join(req)}")
        feats = self._flavor_cfg.get("features", {})
        if feats:
            feat_list = [k for k, v in feats.items() if v and v is not False]
            print(f"  Flavor features: {', '.join(feat_list)}")
        print("=" * 60)
        print("[PLAN] No build executed. Use run-mezo --execute to start build.")
