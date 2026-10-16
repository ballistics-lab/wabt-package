"""Console scripts: each runs the bundled executable of the same name with the command line it was given."""

from __future__ import annotations

import subprocess
import sys
from typing import NoReturn

from . import TOOLS, get_executable


def _exec(name: str, argv: list[str]) -> NoReturn:
    try:
        path = get_executable(name)
    except (KeyError, FileNotFoundError) as exc:
        sys.exit(f"{name}: {exc}")
    sys.exit(subprocess.call([str(path), *argv]))


def main(argv: list[str] | None = None) -> NoReturn:
    """`python -m wabt_package TOOL [ARGS...]`."""
    args = sys.argv[1:] if argv is None else argv
    if not args or args[0] in ("-h", "--help"):
        sys.exit("usage: python -m wabt_package TOOL [ARGS...]\ntools: " + ", ".join(TOOLS))
    _exec(args[0], args[1:])


def spectest_interp() -> NoReturn:
    _exec("spectest-interp", sys.argv[1:])


def wasm_interp() -> NoReturn:
    _exec("wasm-interp", sys.argv[1:])


def wasm_objdump() -> NoReturn:
    _exec("wasm-objdump", sys.argv[1:])


def wasm_stats() -> NoReturn:
    _exec("wasm-stats", sys.argv[1:])


def wasm_strip() -> NoReturn:
    _exec("wasm-strip", sys.argv[1:])


def wasm_validate() -> NoReturn:
    _exec("wasm-validate", sys.argv[1:])


def wasm2c() -> NoReturn:
    _exec("wasm2c", sys.argv[1:])


def wasm2wat() -> NoReturn:
    _exec("wasm2wat", sys.argv[1:])


def wast2json() -> NoReturn:
    _exec("wast2json", sys.argv[1:])


def wat_desugar() -> NoReturn:
    _exec("wat-desugar", sys.argv[1:])


def wat2wasm() -> NoReturn:
    _exec("wat2wasm", sys.argv[1:])
