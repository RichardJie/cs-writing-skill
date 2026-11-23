"""Create a labelled contact sheet from user-provided reference images."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


RASTER_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tif", ".tiff"}


def build_contact_sheet(source: Path, output: Path, columns: int = 3, tile_width: int = 520) -> int:
    files = sorted(p for p in source.iterdir() if p.suffix.lower() in RASTER_EXTENSIONS)
    if not files:
        raise SystemExit("No raster reference images found. Convert SVG/PDF examples to PNG first.")
    columns = max(1, columns)
    label_height = 42
    tile_height = int(tile_width * 0.68)
    rows = math.ceil(len(files) / columns)
    sheet = Image.new("RGB", (columns * tile_width, rows * (tile_height + label_height)), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for index, path in enumerate(files):
        with Image.open(path) as image:
            image = image.convert("RGB")
            image.thumbnail((tile_width - 24, tile_height - 24), Image.Resampling.LANCZOS)
            col, row = index % columns, index // columns
            x0 = col * tile_width + (tile_width - image.width) // 2
            y0 = row * (tile_height + label_height) + (tile_height - image.height) // 2
            sheet.paste(image, (x0, y0))
            label = path.name if len(path.name) <= 64 else path.name[:61] + "..."
            draw.text((col * tile_width + 12, row * (tile_height + label_height) + tile_height + 10), label, fill="black", font=font)
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=92)
    return len(files)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--columns", type=int, default=3)
    args = parser.parse_args()
    count = build_contact_sheet(args.source, args.output, args.columns)
    print(f"Created {args.output} from {count} images")


if __name__ == "__main__":
    main()

