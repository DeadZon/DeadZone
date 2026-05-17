# MEZO Engine Log Language

MEZO legacy script logs (`third_party/mezo_core/MEZOBuildRom.py`) are standardized to English.

This applies to all user-facing output: `log()` messages, `RuntimeError` and `ValueError` text,
`print()` calls, interactive prompts, and EROFS diagnostic output.

The change is purely cosmetic — no build behavior was modified except the `mkfs.erofs` binary
resolver (`resolve_mkfs_erofs_binary`), which adds a safe fallback chain so EROFS repack works
on GitHub Actions runners where `bin/Linux/x86_64/mkfs.erofs` does not exist.

Motivation: GitHub Actions workflow logs and Telegram bot notifications are easier to debug
when all messages are in English.
