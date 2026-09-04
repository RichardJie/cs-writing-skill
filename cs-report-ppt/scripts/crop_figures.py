#!/usr/bin/env python3
r"""
crop_figures.py
High-DPI PDF Figure and Table Extraction Engine using PyMuPDF (fitz) and Pillow.

Features:
- Mode A (Auto): Scans PDF pages for Figure/Table captions, computes union bounding boxes
  of vector drawings and raster images, detects single/dual column layouts.
- Mode B (Manual): Supports --page <INT> and --bbox <x0,y0,x1,y1> in points or [0..1] normalized coordinates.
- 300+ DPI high-resolution rendering.
- Intelligent whitespace margin trimming and aesthetic padding via PIL.
- True aspect ratio calculation (width / height) and JSON metadata emission.

Usage:
    python3 crop_figures.py --pdf paper.pdf --out-dir output/figures/ --auto
    python3 crop_figures.py --pdf paper.pdf --page 2 --bbox "55,370,557,590" --name fig_arch
"""

import os
import sys
import re
import json
import argparse
from typing import List, Dict, Optional, Tuple, Any
import pymupdf
from PIL import Image, ImageOps

CAPTION_REGEX = re.compile(
    r"^\s*(Figure|Fig\.|Table)\s*([0-9]+|[A-Z][0-9]*)\s*[:.]\s*(.*)",
    re.IGNORECASE | re.DOTALL
)


def parse_bbox_string(bbox_str: str, page_width: float, page_height: float) -> pymupdf.Rect:
    """
    Parses bbox string "x0,y0,x1,y1" supporting absolute points or [0..1] normalized floats.
    """
    parts = [p.strip() for p in bbox_str.split(",")]
    if len(parts) != 4:
        raise ValueError(f"Invalid bounding box string: '{bbox_str}'. Expected 4 comma-separated values (x0,y0,x1,y1).")

    coords = [float(p) for p in parts]
    x0, y0, x1, y1 = coords

    # If all coordinates are in range [0, 1], treat as normalized coordinates
    if all(0.0 <= c <= 1.0 for c in coords) and not (x0 == 0 and y0 == 0 and x1 >= 10.0):
        x0 *= page_width
        x1 *= page_width
        y0 *= page_height
        y1 *= page_height

    if x0 >= x1 or y0 >= y1:
        raise ValueError(f"Invalid bounding box dimensions: x0={x0}, y0={y0}, x1={x1}, y1={y1}")

    return pymupdf.Rect(x0, y0, x1, y1)


def trim_whitespace(image: Image.Image, padding: int = 10) -> Image.Image:
    """
    Trims uniform white margin from an image using Pillow and applies aesthetic padding.
    """
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Invert grayscale image to identify non-white pixel envelope
    gray = image.convert("L")
    diff = ImageOps.invert(gray)
    bbox = diff.getbbox()

    if not bbox:
        return image

    w, h = image.size
    x0 = max(0, bbox[0] - padding)
    y0 = max(0, bbox[1] - padding)
    x1 = min(w, bbox[2] + padding)
    y1 = min(h, bbox[3] + padding)

    return image.crop((x0, y0, x1, y1))


def is_header_or_footer_line(rect: pymupdf.Rect, page_height: float, page_width: float) -> bool:
    """Determines if a drawing line is a page header or footer rule."""
    if rect.y0 > page_height - 45.0 or rect.y1 < 45.0:
        return True
    if rect.height < 1.0 and rect.width > page_width * 0.7:
        if rect.y0 > page_height - 50.0 or rect.y0 < 50.0:
            return True
    return False


def find_figure_bounds_for_caption(page: pymupdf.Page, cap_rect: pymupdf.Rect, cap_type: str) -> Optional[pymupdf.Rect]:
    """
    Finds the visual bounding box associated with a detected caption using vertical clustering.
    """
    page_width = page.rect.width
    page_height = page.rect.height

    drawings = page.get_drawings()
    candidate_rects: List[pymupdf.Rect] = []

    # Detect if caption spans across columns
    is_spanning = (cap_rect.width > page_width * 0.45) or (cap_rect.x0 < page_width * 0.25 and cap_rect.x1 > page_width * 0.75)

    if cap_type == "figure":
        # Figure graphics are typically located above the caption (within 450 pt)
        y_min = max(45.0, cap_rect.y0 - 450.0)
        y_max = cap_rect.y0 + 5.0

        # Collect candidate drawing rects
        valid_drawings = []
        for d in drawings:
            r = d["rect"]
            if is_header_or_footer_line(r, page_height, page_width):
                continue
            if r.height <= 0.5 and r.width <= 10.0:
                continue
            if r.y0 >= y_min and r.y1 <= y_max:
                if is_spanning or (r.x1 >= cap_rect.x0 - 25.0 and r.x0 <= cap_rect.x1 + 25.0):
                    valid_drawings.append(r)

        # Sort by y1 descending (closest to caption first)
        valid_drawings.sort(key=lambda r: r.y1, reverse=True)

        if valid_drawings:
            cluster = [valid_drawings[0]]
            curr_top = valid_drawings[0].y0
            for r in valid_drawings[1:]:
                # If r is within current cluster vertical span or close above it (gap <= 30 pt)
                if r.y1 >= curr_top - 30.0 or r.y0 >= curr_top:
                    cluster.append(r)
                    curr_top = min(curr_top, r.y0)
                elif curr_top - r.y1 > 30.0:
                    # Check if there is text in between
                    break
            candidate_rects.extend(cluster)

    elif cap_type == "table":
        # Table data can be below caption (if caption is top) or above caption (if caption is bottom)
        # Check both regions with expanded vertical horizon (up to 450 pt)
        # 1. Region below caption
        y_min_below = cap_rect.y1 - 5.0
        y_max_below = min(page_height - 45.0, cap_rect.y1 + 450.0)
        # 2. Region above caption
        y_min_above = max(45.0, cap_rect.y0 - 450.0)
        y_max_above = cap_rect.y0 + 5.0

        valid_drawings_below = []
        valid_drawings_above = []

        for d in drawings:
            r = d["rect"]
            if is_header_or_footer_line(r, page_height, page_width):
                continue
            if r.height <= 0.5 and r.width <= 10.0:
                continue
            if is_spanning or (r.x1 >= cap_rect.x0 - 25.0 and r.x0 <= cap_rect.x1 + 25.0):
                if r.y0 >= y_min_below and r.y1 <= y_max_below:
                    valid_drawings_below.append(r)
                elif r.y0 >= y_min_above and r.y1 <= y_max_above:
                    valid_drawings_above.append(r)

        if valid_drawings_below:
            valid_drawings_below.sort(key=lambda r: r.y0)
            cluster = [valid_drawings_below[0]]
            curr_bot = valid_drawings_below[0].y1
            for r in valid_drawings_below[1:]:
                if r.y0 <= curr_bot + 250.0 or r.y1 <= curr_bot:
                    cluster.append(r)
                    curr_bot = max(curr_bot, r.y1)
            candidate_rects.extend(cluster)
        elif valid_drawings_above:
            valid_drawings_above.sort(key=lambda r: r.y1, reverse=True)
            cluster = [valid_drawings_above[0]]
            curr_top = valid_drawings_above[0].y0
            for r in valid_drawings_above[1:]:
                if r.y1 >= curr_top - 250.0 or r.y0 >= curr_top:
                    cluster.append(r)
                    curr_top = min(curr_top, r.y0)
            candidate_rects.extend(cluster)

    # Check raster images on page
    image_list = page.get_images(full=True)
    for img_info in image_list:
        xref = img_info[0]
        for img_rect in page.get_image_rects(xref):
            if is_header_or_footer_line(img_rect, page_height, page_width):
                continue
            if cap_type == "figure" and img_rect.y0 >= max(45.0, cap_rect.y0 - 450.0) and img_rect.y1 <= cap_rect.y0 + 5.0:
                candidate_rects.append(img_rect)
            elif cap_type == "table" and (
                (img_rect.y0 >= cap_rect.y1 - 5.0 and img_rect.y1 <= cap_rect.y1 + 450.0) or
                (img_rect.y0 >= cap_rect.y0 - 450.0 and img_rect.y1 <= cap_rect.y0 + 5.0)
            ):
                candidate_rects.append(img_rect)

    if not candidate_rects:
        # Fallback: estimate region above caption for figure or below caption for table
        if cap_type == "figure":
            h = min(200.0, cap_rect.y0 - 50.0)
            if h > 20.0:
                return pymupdf.Rect(cap_rect.x0, cap_rect.y0 - h, cap_rect.x1, cap_rect.y0)
        return None

    # Compute union bounding box using explicit coordinate extrema
    x0 = min(r.x0 for r in candidate_rects)
    y0 = min(r.y0 for r in candidate_rects)
    x1 = max(r.x1 for r in candidate_rects)
    y1 = max(r.y1 for r in candidate_rects)
    union_rect = pymupdf.Rect(x0, y0, x1, y1)

    # For tables, also check text blocks inside the table region to include table text
    if cap_type == "table":
        blocks = page.get_text("blocks")
        table_blocks = []
        for b in blocks:
            b_rect = pymupdf.Rect(b[0], b[1], b[2], b[3])
            if (b_rect.y0 >= union_rect.y0 - 15 and b_rect.y1 <= union_rect.y1 + 15 and
                b_rect.x0 >= union_rect.x0 - 15 and b_rect.x1 <= union_rect.x1 + 15):
                table_blocks.append(b_rect)
        if table_blocks:
            ux0 = min(union_rect.x0, min(b.x0 for b in table_blocks))
            uy0 = min(union_rect.y0, min(b.y0 for b in table_blocks))
            ux1 = max(union_rect.x1, max(b.x1 for b in table_blocks))
            uy1 = max(union_rect.y1, max(b.y1 for b in table_blocks))
            union_rect = pymupdf.Rect(ux0, uy0, ux1, uy1)

    return union_rect


def extract_figure(
    page: pymupdf.Page,
    bbox: pymupdf.Rect,
    output_path: str,
    dpi: int = 300,
    trim: bool = True,
    padding: int = 10,
    img_format: str = "png"
) -> Dict[str, Any]:
    """
    Renders a clipped bounding box at high DPI, trims margins, and writes to disk.
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    # Render high-resolution pixmap
    pix = page.get_pixmap(dpi=dpi, clip=bbox, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

    if trim:
        img = trim_whitespace(img, padding=padding)

    img.save(output_path, format=img_format.upper())

    w_px, h_px = img.size
    aspect_ratio = round(w_px / max(1, h_px), 4)

    return {
        "width_px": w_px,
        "height_px": h_px,
        "aspect_ratio": aspect_ratio,
        "dpi": dpi,
        "bbox_pt": [round(bbox.x0, 2), round(bbox.y0, 2), round(bbox.x1, 2), round(bbox.y1, 2)]
    }


def auto_detect_figures(doc: pymupdf.Document) -> List[Dict[str, Any]]:
    """
    Scans entire document for Figure and Table captions and associated graphics.
    """
    detected = []

    for page_idx in range(len(doc)):
        page = doc[page_idx]
        blocks = page.get_text("blocks")

        for b in blocks:
            text = b[4].strip()
            first_line = text.splitlines()[0] if text else ""
            match = CAPTION_REGEX.match(first_line)

            if match:
                prefix = match.group(1).lower()
                num = match.group(2)
                cap_type = "table" if "table" in prefix else "figure"
                full_caption = " ".join(text.splitlines())
                cap_rect = pymupdf.Rect(b[0], b[1], b[2], b[3])

                fig_rect = find_figure_bounds_for_caption(page, cap_rect, cap_type)
                if fig_rect is not None and fig_rect.width > 20 and fig_rect.height > 20:
                    detected.append({
                        "id": f"{cap_type}_{num}",
                        "type": cap_type,
                        "number": num,
                        "page": page_idx + 1,
                        "caption": full_caption,
                        "bbox": fig_rect,
                        "is_vector": len(page.get_drawings()) > 0
                    })

    # Deduplicate entries with same ID
    unique_detected = []
    seen_ids = set()
    for item in detected:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            unique_detected.append(item)

    return unique_detected


def main():
    parser = argparse.ArgumentParser(
        description="High-DPI PDF Figure & Table Extraction Engine."
    )
    parser.add_argument("--pdf", type=str, required=True, help="Path to input academic paper PDF")
    parser.add_argument("--out-dir", type=str, default="output/figures/", help="Directory to save extracted images")
    parser.add_argument("--auto", action="store_true", help="Auto-detect figures and tables via captions")
    parser.add_argument("--page", type=int, help="Page number for manual extraction (1-indexed)")
    parser.add_argument("--bbox", type=str, help="Bounding box coordinates x0,y0,x1,y1 in pt or [0..1] normalized floats")
    parser.add_argument("--name", type=str, help="Output image filename prefix (e.g. 'figure_1')")
    parser.add_argument("--dpi", type=int, default=300, help="Rendering resolution in DPI (default: 300)")
    parser.add_argument("--padding", type=int, default=10, help="Padding pixels after whitespace trimming (default: 10)")
    parser.add_argument("--no-trim", action="store_true", help="Disable automatic whitespace trimming")
    parser.add_argument("--json-meta", type=str, help="Path to output metadata JSON (default: <out-dir>/figures_metadata.json)")
    parser.add_argument("--format", type=str, default="png", choices=["png", "jpg", "jpeg"], help="Output image format")
    parser.add_argument("--verbose", action="store_true", help="Print detailed diagnostic messages")

    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"Error: PDF file not found: {args.pdf}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(args.out_dir, exist_ok=True)
    meta_path = args.json_meta or os.path.join(args.out_dir, "figures_metadata.json")

    try:
        doc = pymupdf.open(args.pdf)
    except Exception as e:
        print(f"Error opening PDF: {e}", file=sys.stderr)
        sys.exit(1)

    extracted_records = []

    # Mode A: Auto-Detection
    if args.auto:
        items = auto_detect_figures(doc)
        if not items:
            print(f"Warning: No figures or tables detected in {args.pdf}")
            # Write empty schema
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump({"figures": []}, f, indent=2)
            sys.exit(2)

        for item in items:
            p_num = item["page"]
            page = doc[p_num - 1]
            out_name = f"{item['id']}.{args.format}"
            out_path = os.path.join(args.out_dir, out_name)

            if args.verbose:
                print(f"Extracting {item['id']} on page {p_num} at {item['bbox']} -> {out_path}")

            info = extract_figure(
                page=page,
                bbox=item["bbox"],
                output_path=out_path,
                dpi=args.dpi,
                trim=not args.no_trim,
                padding=args.padding,
                img_format=args.format
            )

            record = {
                "id": item["id"],
                "type": item["type"],
                "number": item["number"],
                "page": p_num,
                "caption": item["caption"],
                "file_path": os.path.relpath(out_path, start=os.getcwd()),
                "bbox_pt": info["bbox_pt"],
                "width_px": info["width_px"],
                "height_px": info["height_px"],
                "aspect_ratio": info["aspect_ratio"],
                "dpi": info["dpi"],
                "is_vector": item["is_vector"]
            }
            extracted_records.append(record)

    # Mode B: Manual Extraction
    elif args.page is not None and args.bbox:
        if args.page < 1 or args.page > len(doc):
            print(f"Error: Page {args.page} is out of range (1..{len(doc)})", file=sys.stderr)
            sys.exit(1)

        page = doc[args.page - 1]
        try:
            bbox_rect = parse_bbox_string(args.bbox, page.rect.width, page.rect.height)
        except Exception as e:
            print(f"Error parsing bounding box: {e}", file=sys.stderr)
            sys.exit(1)

        name_prefix = args.name or f"figure_p{args.page}"
        out_name = f"{name_prefix}.{args.format}"
        out_path = os.path.join(args.out_dir, out_name)

        if args.verbose:
            print(f"Extracting manual region on page {args.page} at {bbox_rect} -> {out_path}")

        info = extract_figure(
            page=page,
            bbox=bbox_rect,
            output_path=out_path,
            dpi=args.dpi,
            trim=not args.no_trim,
            padding=args.padding,
            img_format=args.format
        )

        record = {
            "id": name_prefix,
            "type": "figure",
            "number": "1",
            "page": args.page,
            "caption": f"Extracted figure from page {args.page}",
            "file_path": os.path.relpath(out_path, start=os.getcwd()),
            "bbox_pt": info["bbox_pt"],
            "width_px": info["width_px"],
            "height_px": info["height_px"],
            "aspect_ratio": info["aspect_ratio"],
            "dpi": info["dpi"],
            "is_vector": len(page.get_drawings()) > 0
        }
        extracted_records.append(record)

    else:
        print("Error: Must specify either --auto or both --page and --bbox.", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

    # Emit metadata JSON
    meta_payload = {"figures": extracted_records}
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta_payload, f, indent=2)

    print(f"Successfully extracted {len(extracted_records)} figures to {args.out_dir}")
    print(f"Metadata written to {meta_path}")
    sys.exit(0)


if __name__ == "__main__":
    main()
