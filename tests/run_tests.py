"""Command-line test runner for the repository.

This script lets you target specific test files or directories.
Use the ``--files`` argument to pass one or more paths, and ``--pattern``
if you need a custom discovery glob. By default, it searches the ``tests``
directory for files matching ``test*.py``.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
import unittest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Discover and run unittests by path.")
    parser.add_argument(
        "-f",
        "--files",
        nargs="*",
        default=None,
        help="One or more test files or directories to run. Defaults to the tests directory.",
    )
    parser.add_argument(
        "-p",
        "--pattern",
        default="test*.py",
        help="Glob pattern used to match test files (default: test*.py).",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase output verbosity for the test runner.",
    )
    return parser.parse_args()


def build_test_suite(paths: list[str] | None, pattern: str) -> tuple[unittest.TestSuite, list[str]]:
    """Create a combined test suite from the provided paths.

    Args:
        paths: List of file or directory paths to search for tests. If ``None``,
            defaults to the ``tests`` directory.
        pattern: Glob pattern used to identify test files when discovering tests.

    Returns:
        A tuple containing the combined :class:`unittest.TestSuite` and a list of
        paths that could not be resolved.
    """
    search_paths = paths or ["tests"]
    loader = unittest.TestLoader()
    suites: list[unittest.TestSuite] = []
    missing: list[str] = []

    for path_str in search_paths:
        path = Path(path_str)
        if not path.exists():
            missing.append(str(path))
            continue

        if path.is_dir():
            suites.append(loader.discover(str(path), pattern=pattern))
        else:
            suites.append(loader.discover(start_dir=str(path.parent), pattern=path.name))

    return unittest.TestSuite(suites), missing


def main() -> int:
    args = parse_args()
    suite, missing = build_test_suite(args.files, args.pattern)

    if missing:
        missing_list = "\n - ".join(["", *missing])
        print(f"Warning: the following paths do not exist and were skipped:{missing_list}", file=sys.stderr)

    runner = unittest.TextTestRunner(verbosity=2 if args.verbose else 1)
    result = runner.run(suite)

    if missing or not result.wasSuccessful():
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
