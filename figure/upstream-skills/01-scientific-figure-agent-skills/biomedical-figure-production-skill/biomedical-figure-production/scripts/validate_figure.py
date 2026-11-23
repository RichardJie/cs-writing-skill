#!/usr/bin/env python3
"""Inspect figure exports and emit a reproducibility-oriented JSON report."""

from __future__ import annotations

import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image


RASTER_EXTENSIONS = {".png", ".tif", ".tiff"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def inspect_raster(path: Path, minimum_dpi: float) -> dict:
    with Image.open(path) as image:
        dpi_value = image.info.get("dpi")
        dpi = None
        if isinstance(dpi_value, tuple) and dpi_value:
            dpi = [round(float(value), 2) for value in dpi_value[:2]]
        warnings: list[str] = []
        if dpi is None:
            warnings.append("DPI metadata is absent; verify physical size manually.")
        elif min(dpi) + 0.5 < minimum_dpi:
            warnings.append(f"DPI is below the requested minimum of {minimum_dpi:g}.")
        if min(image.size) < 600:
            warnings.append("A raster dimension is below 600 pixels; inspect text and line sharpness.")
        return {
            "kind": "raster",
            "format": image.format,
            "mode": image.mode,
            "pixels": list(image.size),
            "dpi": dpi,
            "frames": getattr(image, "n_frames", 1),
            "warnings": warnings,
        }


def inspect_svg(path: Path) -> dict:
    root = ET.parse(path).getroot()
    return {
        "kind": "vector",
        "format": "SVG",
        "width": root.attrib.get("width"),
        "height": root.attrib.get("height"),
        "viewBox": root.attrib.get("viewBox"),
        "warnings": [] if root.attrib.get("viewBox") else ["SVG viewBox is absent."],
    }


def inspect_file(path: Path, minimum_dpi: float) -> dict:
    record = {
        "path": str(path.resolve()),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }
    extension = path.suffix.lower()
    if extension in RASTER_EXTENSIONS:
        record.update(inspect_raster(path, minimum_dpi))
    elif extension == ".svg":
        record.update(inspect_svg(path))
    elif extension == ".pdf":
        record.update(
            {
                "kind": "vector_or_mixed",
                "format": "PDF",
                "warnings": ["Render the PDF and inspect fonts, strokes, and rasterized panels."],
            }
        )
    else:
        record.update({"kind": "unknown", "warnings": ["Unsupported extension."]})
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--minimum-dpi", type=float, default=300.0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    missing = [str(path) for path in args.files if not path.is_file()]
    if missing:
        parser.error("Missing file(s): " + ", ".join(missing))

    report = {
        "minimum_dpi": args.minimum_dpi,
        "files": [inspect_file(path, args.minimum_dpi) for path in args.files],
        "note": "Automated checks do not establish scientific correctness or visual legibility.",
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

