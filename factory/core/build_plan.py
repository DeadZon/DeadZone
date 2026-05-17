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

_SUPERCONFIG_DEFAULT = {
    "flash_profile": "superconfig",
    "vbmeta_policy": "binary_flags_3",
    "required_images": REQUIRED_IMAGES,
}


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
        self._device_lite = False  # True when loaded from device_groups, not registry YAML

    def _load_yaml(self, path: Path) -> dict:
        if not path.exists():
            raise FileNotFoundError(f"Registry file not found: {path}")
        with path.open() as f:
            return yaml.safe_load(f)

    def _load_from_device_group(self) -> dict:
        """Fallback: build a synthetic device config from the device_groups YAML."""
        group_yml = REGISTRY_ROOT / "device_groups" / f"{self.soc}.yml"
        if not group_yml.exists():
            raise FileNotFoundError(
                f"No registry device file and no device_groups/{self.soc}.yml found. "
                f"Cannot resolve device '{self.device}'."
            )
        data = self._load_yaml(group_yml)
        for entry in data.get("devices", []):
            if entry.get("codename") == self.device:
                return {
                    "codename": self.device,
                    "brand": "",
                    "model": entry.get("name", self.device),
                    "soc": data.get("soc", self.soc),
                    "flash_profile": _SUPERCONFIG_DEFAULT["flash_profile"],
                    "vbmeta_policy": _SUPERCONFIG_DEFAULT["vbmeta_policy"],
                    "required_images": list(_SUPERCONFIG_DEFAULT["required_images"]),
                    "_source": entry.get("source", "superconfig"),
                    "_superconfig_path": entry.get("source_path"),
                }
        raise FileNotFoundError(
            f"Device '{self.device}' not found in registry/devices/{self.soc}/ "
            f"or device_groups/{self.soc}.yml."
        )

    def load(self) -> None:
        device_yml = REGISTRY_ROOT / "devices" / self.soc / f"{self.device}.yml"
        if device_yml.exists():
            self._device_cfg = self._load_yaml(device_yml)
            self._device_lite = False
        else:
            self._device_cfg = self._load_from_device_group()
            self._device_lite = True

        self._soc_cfg = self._load_yaml(REGISTRY_ROOT / "soc" / f"{self.soc}.yml")
        self._platform_cfg = self._load_yaml(
            REGISTRY_ROOT / "platforms" / f"{self.platform}.yml"
        )
        self._flavor_cfg = self._load_yaml(
            REGISTRY_ROOT / "flavors" / f"{self.flavor}.yml"
        )

    def print(self) -> None:
        print("=" * 60)
        print("DeadZone Factory -- Build Plan")
        if self._device_lite:
            src_path = self._device_cfg.get("_superconfig_path", "unknown")
            print(f"  [SOURCE] SuperConfig: {src_path}")
        print("=" * 60)
        brand = self._device_cfg.get("brand", "")
        model = self._device_cfg.get("model", "")
        display = f"{brand} {model}".strip() if (brand or model) else self.device
        print(f"  Device   : {self.device} ({display})")
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
