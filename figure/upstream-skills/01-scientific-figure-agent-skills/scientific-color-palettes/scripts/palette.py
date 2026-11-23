#!/usr/bin/env python3
"""List and export the exact palettes bundled with scientific-color-palettes."""

from __future__ import annotations

import argparse
import json
import sys


PALETTES = {
    "balanced-8": ["#2C6E7E", "#1FAE9D", "#7BC48F", "#F2C14E", "#F28E2B", "#E4572E", "#E63946", "#4D4D4D"],
    "blue-yellow-orange-7": ["#497AB7", "#7EB6D5", "#BDE2ED", "#F0FAD9", "#FEEAA1", "#FCB567", "#F27144"],
    "coral-teal-violet-8": ["#E76F51", "#F4A582", "#CFE8E6", "#7BC7C4", "#4DAAA7", "#6C5B95", "#D9D9D9", "#333333"],
    "orange-blue-6": ["#F26A1D", "#F7B891", "#FFF3E6", "#DCE6F2", "#6EA6D6", "#1E5FA8"],
    "orange-5": ["#EA5514", "#EB6821", "#EC7A2E", "#ED8B3C", "#EE9C4B"],
    "amber-5": ["#F7A049", "#F9BD6F", "#FBD18B", "#FDE4AF", "#FEF2D6"],
    "aqua-5": ["#22B5AF", "#3FC4BF", "#63D1D0", "#95E6E8", "#BFFEF8"],
    "blue-gray-5": ["#E3F8F8", "#CAEEF2", "#A4D2D9", "#80AAB7", "#547A8A"],
    "muted-teal-5": ["#D3F5EF", "#B4E3DE", "#96C8C7", "#6FA1A5", "#4F808A"],
    "blue-5": ["#154778", "#397AAA", "#5FA9D1", "#95D4EE", "#C8EBF6"],
    "green-pink-8": ["#FBE4E6", "#E7A8B3", "#F4C4B8", "#DFF0E6", "#B8CDB0", "#7FB59B", "#538F7B", "#2E5B47"],
    "blue-pink-8": ["#FCE7EC", "#E8B3C6", "#D79AB7", "#D8D4EA", "#D4E4F2", "#9CC6E6", "#5B7FAF", "#0F2B55"],
}


def render(name: str, colors: list[str], output_format: str) -> str:
    if output_format == "hex":
        return " ".join(colors)
    if output_format == "python":
        return f"{name.replace('-', '_')} = {colors!r}"
    if output_format == "r":
        values = ", ".join(f'\"{color}\"' for color in colors)
        return f"{name.replace('-', '_')} <- c({values})"
    if output_format == "css":
        lines = [":root {"]
        lines.extend(f"  --{name}-{i}: {color};" for i, color in enumerate(colors, 1))
        lines.append("}")
        return "\n".join(lines)
    return json.dumps({"name": name, "colors": colors}, ensure_ascii=False, indent=2)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="list bundled palette names")

    get_parser = subparsers.add_parser("get", help="export one exact palette")
    get_parser.add_argument("name", choices=sorted(PALETTES))
    get_parser.add_argument("--format", choices=("hex", "python", "r", "css", "json"), default="hex")
    get_parser.add_argument("--reverse", action="store_true", help="reverse the stored order")

    args = parser.parse_args()
    if args.command == "list":
        for name, colors in PALETTES.items():
            print(f"{name}\t{len(colors)}")
        return 0

    colors = list(PALETTES[args.name])
    if args.reverse:
        colors.reverse()
    print(render(args.name, colors, args.format))
    return 0


if __name__ == "__main__":
    sys.exit(main())
