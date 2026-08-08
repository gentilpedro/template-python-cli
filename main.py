"""Entry point. Keep this thin: parse args, delegate to app/."""
from __future__ import annotations

import argparse

from app.logger import log
from app.use_cases.say_hello import say_hello


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="template-python-cli")
    parser.add_argument("--hello", metavar="NAME", help="Print a greeting for NAME")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.hello:
        print(say_hello(args.hello))
        return

    log.info("No command given, showing help.")
    parser.print_help()


if __name__ == "__main__":
    main()
