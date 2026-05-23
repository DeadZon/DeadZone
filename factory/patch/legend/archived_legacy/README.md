# archived_legacy — Dead Archive

This directory contains old Legend implementation files that have been
superseded by the modular system under `factory/patch/legend/`.

## Contents

| File | Original purpose |
|------|-----------------|
| `jar_misc_legacy.py` | Early JAR patching helpers, replaced by `mtcr/runner.py` |
| `kaori_legacy.py` | Kaori toolbox early implementation, replaced by `mods/jars/*/kaorios_toolbox_v203/` |
| `signature_bypass_legacy.py` | Signature bypass early implementation, replaced by `mods/jars/*/signature_verification_bypass/` |

## Rules

- **Nothing in this directory is imported or executed by any active code.**
- Do not add `import` or `from` statements referencing these files anywhere outside this directory.
- Do not add new Legend logic here — use `factory/patch/legend/patchers/` or `factory/patch/legend/mods/` instead.
- These files exist only for historical reference. They may be deleted when no longer useful.
