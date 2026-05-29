# DeadZone

DeadZone is a single universal ROM builder.

```bash
python3 -m factory.deadzone \
  --rom-url "$ROM_URL" \
  --style "$STYLE" \
  --soc "$SOC"
```

Supported styles: `Stable`, `Legend`, `Gaming`, `EPiC`.

Both MTK and Snapdragon builds use the same engine. The workflow-selected SoC only chooses profile rules and required firmware images.
