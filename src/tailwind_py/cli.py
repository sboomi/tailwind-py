import argparse
import platform
from pathlib import Path

from tailwind_py.download import download_tailwind
from tailwind_py.tailwind import Tailwind


def build(args):
    """
    Build the CSS output using Tailwind CSS.
    """
    tw = Tailwind(args.executable)
    if args.minify:
        tw.minify_css(Path(args.input), Path(args.output))
    elif args.watch:
        tw.watch_css(Path(args.input), Path(args.output))
    else:
        raise ValueError("Either --minify or --watch must be specified.")


def main():
    parser = argparse.ArgumentParser(
        prog="tailwindcss",
        description="Tailwind Python CLI - A tool for managing Tailwind CSS in Python projects, without npm",
        epilog="Use 'tailwindcss <command> --help' for more information on a specific command.",
    )
    subparsers = parser.add_subparsers(title="subcommands", help="Available commands")

    dl_parser = subparsers.add_parser(
        "download", help="Downloads the latest version of the TailwindCSS CLI"
    )
    dl_parser.add_argument(
        "--output-dir",
        type=str,
        default=".tailwind",
        help="Directory to download the TailwindCSS CLI executable",
    )
    dl_parser.set_defaults(func=lambda args: download_tailwind(args.output_dir))

    init_parser = subparsers.add_parser(
        "init", help="Initialize `tailwind.config.js` file"
    )
    init_parser.add_argument(
        "--output-dir",
        type=str,
        help="Path to the Tailwind CSS configuration file",
    )
    init_parser.add_argument(
        "-e",
        "--executable",
        type=Path,
        default=Path(".tailwind")
        / ("tailwindcss" + ".exe" if platform.system() == "Windows" else ""),
    )
    init_parser.set_defaults(
        func=lambda args: Tailwind(args.executable).init_config(args.output_dir)
    )

    build_parser = subparsers.add_parser("build", help="Builds the CSS output")
    build_parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="Path to the input CSS file",
    )
    build_parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=True,
        help="Path to the output CSS file",
    )
    build_parser.add_argument(
        "--minify",
        action="store_true",
        help="Minify the output CSS file",
    )
    build_parser.add_argument(
        "--watch",
        action="store_true",
        help="Watch the output CSS file",
    )
    build_parser.add_argument(
        "-e",
        "--executable",
        type=Path,
        default=Path(".tailwind")
        / ("tailwindcss" + ".exe" if platform.system() == "Windows" else ""),
    )
    build_parser.set_defaults(func=build)

    args = parser.parse_args()

    args.func(args)


if __name__ == "__main__":
    main()
