# MEZO Tool Resolution

MEZO resolves bundled tools using a safe fallback chain implemented in
`third_party/mezo_core/src/core/utils.py` (`resolve_tool_path`).

## Resolution order

1. Absolute path provided and exists — use it.
2. Relative path provided and exists — use it.
3. Arch-specific bundled path (`bin/<platform>/<machine>/<tool>`) — use if it exists.
4. Flat bundled path (`bin/<tool>`) — use if it exists.
5. System `PATH` via `shutil.which` — use if found.
6. Return arch-specific candidate string so subprocess error is descriptive.

## Why this matters

On GitHub Linux runners, `platform.system()` = `Linux` and `platform.machine()` = `x86_64`,
so the arch path resolves to `bin/Linux/x86_64/<tool>`. Bundled tools such as `lpmake`,
`lpunpack`, `mkfs.erofs`, and `extract.erofs` are stored at `bin/<tool>` (flat, no arch subdir).
Without the fallback chain, every `call()` with `extra_path=True` would try the arch path first
and raise `FileNotFoundError`.

## Diagnostic output

When a tool is found, the resolver prints:

```
[TOOL] lpmake resolved to: .../bin/lpmake
```

When nothing is found, it prints:

```
[TOOL] lpdump not found in bundled paths or PATH; using fallback: .../bin/Linux/x86_64/lpdump
```

If execution still fails with `FileNotFoundError`, `call()` prints full diagnostics:

```
[TOOL ERROR] Failed to execute command
  Command: [...]
  Resolved executable: ...
  PATH: ...
[TOOL DEBUG] arch path: ... exists=False
[TOOL DEBUG] flat bin: ... exists=False
[TOOL DEBUG] PATH which: None
```

## Log language

All MEZO engine logs are standardized to English. See `docs/MEZO_ENGINE_LOG_LANGUAGE.md`.
