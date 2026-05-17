import argparse
import sys
from pathlib import Path


def cmd_plan(args):
    from factory.core.build_plan import BuildPlan
    plan = BuildPlan(
        device=args.device,
        soc=args.soc,
        platform=args.platform,
        flavor=args.flavor,
    )
    plan.load()
    plan.print()


def cmd_validate_registry(args):
    from factory.validators.validate_registry import validate_registry
    ok = validate_registry()
    sys.exit(0 if ok else 1)


def cmd_validate_zip(args):
    from factory.validators.validate_public_zip import validate_public_zip
    ok = validate_public_zip(Path(args.zip))
    sys.exit(0 if ok else 1)


def cmd_run_mezo(args):
    rom_path = Path(args.rom)
    print(f"[INFO] Device  : {args.device}")
    print(f"[INFO] SoC     : {args.soc}")
    print(f"[INFO] Platform: {args.platform}")
    print(f"[INFO] Flavor  : {args.flavor}")
    print(f"[INFO] ROM     : {rom_path}")
    if not args.execute:
        print()
        print("[DRY RUN] run-mezo would invoke: third_party/mezo_core/MEZOBuildRom.py")
        print("[DRY RUN] Pass --execute to actually run the build.")
        return
    from factory.engines.mezo_legacy_engine import run_mezo_legacy_engine
    run_mezo_legacy_engine(rom_path)


def main():
    parser = argparse.ArgumentParser(
        prog="factory",
        description="DeadZone ROM Factory CLI",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_plan = sub.add_parser("plan", help="Show build plan without executing")
    p_plan.add_argument("--device", required=True, help="Device codename (e.g. garnet)")
    p_plan.add_argument("--soc", required=True, choices=["snapdragon", "mtk"])
    p_plan.add_argument("--platform", required=True, help="Platform ID (e.g. os3_a16)")
    p_plan.add_argument("--flavor", required=True, help="Flavor ID (e.g. deadzone)")
    p_plan.set_defaults(func=cmd_plan)

    p_val = sub.add_parser("validate-registry", help="Validate all registry YAML files")
    p_val.set_defaults(func=cmd_validate_registry)

    p_zip = sub.add_parser("validate-zip", help="Validate a public ROM ZIP")
    p_zip.add_argument("--zip", required=True, help="Path to the ZIP to validate")
    p_zip.set_defaults(func=cmd_validate_zip)

    p_run = sub.add_parser(
        "run-mezo",
        help="Invoke MEZO legacy engine (dry-run by default; add --execute to actually build)",
    )
    p_run.add_argument("--rom", required=True, help="Path to source ROM ZIP")
    p_run.add_argument("--device", required=True)
    p_run.add_argument("--soc", required=True, choices=["snapdragon", "mtk"])
    p_run.add_argument("--platform", required=True)
    p_run.add_argument("--flavor", required=True)
    p_run.add_argument(
        "--execute",
        action="store_true",
        help="Actually run MEZOBuildRom.py (omit for dry-run)",
    )
    p_run.set_defaults(func=cmd_run_mezo)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
