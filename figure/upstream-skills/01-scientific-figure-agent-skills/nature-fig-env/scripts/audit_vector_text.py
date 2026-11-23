"""Audit actual text sizes in exported SVG or PDF figure files."""

from __future__ import annotations

import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path


FONT_SIZE_RE = re.compile(
    r"(?:font-size\s*:|font\s*:)\s*([0-9]*\.?[0-9]+)(?:px|pt)?",
    re.I,
)
PDF_TF_RE = re.compile(rb"/[A-Za-z0-9_.+-]+\s+([0-9]*\.?[0-9]+)\s+Tf\b")


def svg_font_sizes(path: Path) -> tuple[list[float], int]:
    root = ET.parse(path).getroot()
    text_nodes = [node for node in root.iter() if node.tag.rsplit("}", 1)[-1] in {"text", "tspan"}]
    sizes: list[float] = []
    for node in text_nodes:
        candidates = [node.attrib.get("font-size", ""), node.attrib.get("style", "")]
        for value in candidates:
            match = FONT_SIZE_RE.search(value)
            if match:
                sizes.append(float(match.group(1)))
                break
    return sizes, len(text_nodes)


def pdf_font_sizes(path: Path) -> list[float]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("PDF audit requires pypdf; install requirements.txt") from exc
    sizes: list[float] = []
    for page in PdfReader(str(path)).pages:
        contents = page.get_contents()
        if contents is None:
            continue
        data = contents.get_data()
        sizes.extend(float(match.group(1)) for match in PDF_TF_RE.finditer(data))
    return sizes


def audit(path: Path, minimum_pt: float) -> list[str]:
    if not path.exists():
        return [f"missing vector file: {path}"]
    suffix = path.suffix.lower()
    if suffix == ".svg":
        sizes, text_count = svg_font_sizes(path)
        if text_count == 0:
            return ["[FONT-02] SVG contains no editable <text> elements; text may have been converted to paths"]
        if not sizes:
            return ["[FONT-03] could not determine SVG text sizes"]
    elif suffix == ".pdf":
        try:
            sizes = pdf_font_sizes(path)
        except RuntimeError as exc:
            return [f"[FONT-03] {exc}"]
        if not sizes:
            return ["[FONT-02] could not find PDF text-size commands; verify that text remains editable"]
    else:
        return ["[EXPORT-01] input must be an SVG or PDF"]
    smallest = min(sizes)
    if smallest + 1e-9 < minimum_pt:
        return [f"[FONT-01] minimum detected text size is {smallest:.2f} pt, below {minimum_pt:.2f} pt"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("vector", type=Path)
    parser.add_argument("--minimum-pt", type=float, default=13.0)
    args = parser.parse_args()
    issues = audit(args.vector, args.minimum_pt)
    if issues:
        print("VECTOR TEXT AUDIT FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(f"VECTOR TEXT AUDIT PASSED: all detected text is at least {args.minimum_pt:g} pt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
