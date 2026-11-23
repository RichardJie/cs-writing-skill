#!/usr/bin/env python
"""Extract paper figures/captions and build a Chinese figure-by-figure PPTX draft."""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"Pillow is required: {exc}")

try:
    import pdfplumber
except Exception as exc:  # pragma: no cover
    pdfplumber = None

try:
    from pptx import Presentation
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.enum.text import MSO_AUTO_SIZE, PP_ALIGN
    from pptx.oxml.xmlchemy import OxmlElement
    from pptx.util import Inches, Pt
    from pptx.oxml.ns import qn
except Exception:  # pragma: no cover
    Presentation = None


CAPTION_RE = re.compile(
    r"^\s*((?:Fig(?:ure)?\.?|Supplementary\s+Fig(?:ure)?\.?|Extended\s+Data\s+Fig(?:ure)?\.?)\s*[A-Za-z]?\d+[A-Za-z]?)\b",
    re.IGNORECASE,
)


def fail(message: str) -> None:
    raise SystemExit(message)


def qpath(value: str | Path) -> str:
    return str(Path(value).resolve())


def find_pdftoppm(explicit: str | None = None) -> str:
    if explicit:
        return explicit
    found = shutil.which("pdftoppm") or shutil.which("pdftoppm.cmd")
    if found:
        return found
    fail("pdftoppm was not found on PATH. Use the Codex bundled Poppler path or pass --pdftoppm.")


def run(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode:
        raise SystemExit(f"Command failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stderr}")


def render_pdf_pages(pdf: Path, pages_dir: Path, dpi: int, pdftoppm: str) -> list[Path]:
    pages_dir.mkdir(parents=True, exist_ok=True)
    prefix = pages_dir / "page"
    run([pdftoppm, "-r", str(dpi), "-png", qpath(pdf), qpath(prefix)])
    pages = sorted(pages_dir.glob("page-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
    if not pages:
        fail("No rendered PDF pages were created.")
    cover = pages_dir.parent / "cover_page_1.png"
    if not cover.exists():
        shutil.copyfile(pages[0], cover)
    return pages


def make_cover_crop(rendered_page: Path, out: Path, top_ratio: float) -> None:
    with Image.open(rendered_page) as im:
        bottom = max(1, min(im.height, int(im.height * top_ratio)))
        im.crop((0, 0, im.width, bottom)).save(out)


def extract_captions_from_text(text: str, max_lines: int) -> list[dict]:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    captions: list[dict] = []
    current: list[str] = []
    current_label = ""
    for line in lines:
        match = CAPTION_RE.match(line)
        if match:
            if current:
                captions.append({"label": current_label, "text": " ".join(current)})
            current = [line]
            current_label = match.group(1).replace("Figure", "Fig.")
            continue
        if current and len(current) < max_lines:
            if CAPTION_RE.match(line):
                captions.append({"label": current_label, "text": " ".join(current)})
                current = [line]
                current_label = CAPTION_RE.match(line).group(1)
            else:
                current.append(line)
    if current:
        captions.append({"label": current_label, "text": " ".join(current)})
    return captions


def image_bbox_points(page, image_obj: dict) -> tuple[float, float, float, float]:
    x0 = float(image_obj.get("x0", 0))
    x1 = float(image_obj.get("x1", 0))
    if "top" in image_obj and "bottom" in image_obj:
        top = float(image_obj["top"])
        bottom = float(image_obj["bottom"])
    else:
        y0 = float(image_obj.get("y0", 0))
        y1 = float(image_obj.get("y1", 0))
        top = float(page.height) - y1
        bottom = float(page.height) - y0
    return x0, top, x1, bottom


def crop_rendered_page(rendered_page: Path, page_width_pt: float, bbox_pt: tuple[float, float, float, float], out: Path, padding_px: int) -> tuple[int, int]:
    with Image.open(rendered_page) as im:
        scale = im.width / page_width_pt
        x0, y0, x1, y1 = bbox_pt
        box = (
            max(0, int(x0 * scale) - padding_px),
            max(0, int(y0 * scale) - padding_px),
            min(im.width, int(math.ceil(x1 * scale)) + padding_px),
            min(im.height, int(math.ceil(y1 * scale)) + padding_px),
        )
        crop = im.crop(box)
        crop.save(out)
        return crop.width, crop.height


def extract_command(args: argparse.Namespace) -> None:
    if pdfplumber is None:
        fail("pdfplumber is required for extraction.")

    pdf = Path(args.pdf).resolve()
    workdir = Path(args.workdir).resolve()
    figures_dir = workdir / "figures"
    pages_dir = workdir / "pages"
    workdir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    pages = render_pdf_pages(pdf, pages_dir, args.dpi, find_pdftoppm(args.pdftoppm))
    cover_crop = workdir / "cover_page_1_top.png"
    make_cover_crop(pages[0], cover_crop, args.cover_crop_ratio)

    figures: list[dict] = []
    pages_meta: list[dict] = []
    figure_index = 1
    with pdfplumber.open(qpath(pdf)) as doc:
        for page_number, page in enumerate(doc.pages, start=1):
            rendered = pages[page_number - 1] if page_number - 1 < len(pages) else None
            text = page.extract_text(x_tolerance=1, y_tolerance=3) or ""
            captions = extract_captions_from_text(text, args.max_caption_lines)
            pages_meta.append(
                {
                    "page": page_number,
                    "rendered_page": qpath(rendered) if rendered else "",
                    "captions": captions,
                }
            )

            candidates: list[tuple[float, dict, tuple[float, float, float, float]]] = []
            for image_obj in page.images:
                bbox = image_bbox_points(page, image_obj)
                width_pt = bbox[2] - bbox[0]
                height_pt = bbox[3] - bbox[1]
                area_ratio = (width_pt * height_pt) / max(1.0, float(page.width) * float(page.height))
                if width_pt < args.min_width_pt or height_pt < args.min_height_pt:
                    continue
                if area_ratio < args.min_area_ratio:
                    continue
                candidates.append((bbox[1] * 10000 + bbox[0], image_obj, bbox))

            candidates.sort(key=lambda item: item[0])
            for local_index, (_, image_obj, bbox) in enumerate(candidates, start=1):
                if not rendered:
                    continue
                out = figures_dir / f"figure_{figure_index:03d}_p{page_number:03d}_i{local_index:02d}.png"
                crop_w, crop_h = crop_rendered_page(rendered, float(page.width), bbox, out, args.padding_px)
                caption = captions[local_index - 1] if local_index - 1 < len(captions) else {}
                figures.append(
                    {
                        "id": f"fig-{figure_index:03d}",
                        "page": page_number,
                        "order": figure_index,
                        "image_path": qpath(out),
                        "bbox_pt": [round(v, 2) for v in bbox],
                        "crop_px": [crop_w, crop_h],
                        "raw_label": caption.get("label", ""),
                        "raw_caption": caption.get("text", ""),
                        "zh_caption": "",
                        "notes": "Review crop, order, and caption before building the final deck.",
                    }
                )
                figure_index += 1

            if not candidates and captions and rendered and args.add_page_placeholders:
                for caption in captions:
                    figures.append(
                        {
                            "id": f"fig-{figure_index:03d}",
                            "page": page_number,
                            "order": figure_index,
                            "image_path": qpath(rendered),
                            "bbox_pt": [],
                            "crop_px": [],
                            "raw_label": caption.get("label", ""),
                            "raw_caption": caption.get("text", ""),
                            "zh_caption": "",
                            "notes": "Placeholder uses the full rendered page because no raster image object was detected. Crop manually.",
                        }
                    )
                    figure_index += 1

    manifest = {
        "source_pdf": qpath(pdf),
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "cover_image": qpath(workdir / "cover_page_1.png"),
        "cover_crop_image": qpath(cover_crop),
        "paper": {
            "title_zh": "",
            "journal_if": "",
            "author_school": "",
        },
        "figures": figures,
        "pages": pages_meta,
        "style": {
            "language": "zh-CN",
            "caption_voice": "Concise Chinese group-meeting explanation; preserve figure labels and technical terms.",
        },
    }
    manifest_path = workdir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {manifest_path}")
    print(f"Extracted {len(figures)} candidate figures. Review manifest.json before build.")


def add_fit_picture(slide, image_path: str, x: float, y: float, w: float, h: float, valign: str = "center"):
    with Image.open(image_path) as im:
        iw, ih = im.size
    scale = min(w / iw, h / ih)
    pic_w = iw * scale
    pic_h = ih * scale
    left = x + (w - pic_w) / 2
    if valign == "top":
        top = y
    elif valign == "bottom":
        top = y + (h - pic_h)
    else:
        top = y + (h - pic_h) / 2
    return slide.shapes.add_picture(image_path, Inches(left), Inches(top), Inches(pic_w), Inches(pic_h))


def set_run_font(run, size: int, bold: bool = False) -> None:
    run.font.bold = bold
    run.font.size = Pt(size)
    run.font.name = "Microsoft YaHei"
    rpr = run._r.get_or_add_rPr()
    for tag in ("latin", "ea", "cs"):
        elem = rpr.find(qn(f"a:{tag}"))
        if elem is None:
            elem = OxmlElement(f"a:{tag}")
            rpr.append(elem)
        elem.set("typeface", "Microsoft YaHei")


def add_text(slide, text: str, x: float, y: float, w: float, h: float, size: int = 18, bold_first_label: bool = True):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    tf.margin_left = Inches(0.05)
    tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.03)
    tf.margin_bottom = Inches(0.03)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    p.line_spacing = 1.05
    label_match = CAPTION_RE.match(text)
    if label_match and bold_first_label:
        label = label_match.group(1)
        rest = text[len(label):].lstrip()
        run = p.add_run()
        run.text = label + " "
        set_run_font(run, size, True)
        run = p.add_run()
        run.text = rest
        set_run_font(run, size)
    else:
        run = p.add_run()
        run.text = text
        set_run_font(run, size)
    return box


def figure_caption_lines(fig: dict) -> list[str]:
    panels = fig.get("zh_panel_captions") or fig.get("panel_captions") or []
    if isinstance(panels, dict):
        panel_lines = [f"{key}: {value}" for key, value in panels.items() if value]
    else:
        panel_lines = [str(item) for item in panels if str(item).strip()]
    if "zh_caption" in fig:
        main = fig.get("zh_caption") or ""
    else:
        main = fig.get("raw_caption") or fig.get("raw_label") or fig.get("id", "")
    if not str(main).strip() and not panel_lines:
        main = fig.get("raw_caption") or fig.get("raw_label") or fig.get("id", "")
    return ([main] if str(main).strip() else []) + panel_lines


def figure_caption_text(fig: dict) -> str:
    return "\n".join(figure_caption_lines(fig))


def add_caption(slide, fig: dict, x: float, y: float, w: float, h: float, size: int) -> None:
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE if fig.get("auto_fit", False) else MSO_AUTO_SIZE.NONE
    tf.margin_left = Inches(0.04)
    tf.margin_right = Inches(0.04)
    tf.margin_top = Inches(0.02)
    tf.margin_bottom = Inches(0.02)

    line_spacing = float(fig.get("line_spacing") or 1.18)
    space_after = float(fig.get("space_after_pt") or 9)
    for idx, line in enumerate(figure_caption_lines(fig)):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.line_spacing = line_spacing
        p.space_after = Pt(space_after if idx < len(figure_caption_lines(fig)) - 1 else 0)

        panel_match = re.match(r"^\s*([A-Z](?:[-–][A-Z])?:)\s*(.*)$", line)
        fig_match = CAPTION_RE.match(line)
        if panel_match:
            label, rest = panel_match.groups()
            run = p.add_run()
            run.text = label + " "
            set_run_font(run, size, True)
            run = p.add_run()
            run.text = rest
            set_run_font(run, size)
        elif fig_match:
            label = fig_match.group(1)
            rest = line[len(label):].lstrip()
            run = p.add_run()
            run.text = label + " "
            set_run_font(run, int(fig.get("figure_label_size") or size), True)
            run = p.add_run()
            run.text = rest
            set_run_font(run, size)
        else:
            run = p.add_run()
            run.text = line
            set_run_font(run, size)


def iter_slide_figures(figures: list[dict]) -> list[dict]:
    expanded: list[dict] = []
    for fig in sorted(figures, key=lambda item: item.get("order", 0)):
        subslides = fig.get("subslides") or []
        if not subslides:
            expanded.append(fig)
            continue
        for idx, sub in enumerate(subslides, start=1):
            entry = dict(fig)
            entry.update(sub)
            entry["id"] = sub.get("id") or f"{fig.get('id', 'fig')}-{idx}"
            entry["order"] = fig.get("order", 0) + idx / 10
            entry.pop("subslides", None)
            expanded.append(entry)
    return sorted(expanded, key=lambda item: item.get("order", 0))


def add_header(slide, title: str = "文献汇报") -> None:
    add_text(slide, title, 0.35, 0.12, 3.8, 0.38, size=16, bold_first_label=False)
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0.72), Inches(13.33), Inches(0.01))
    line.fill.solid()
    line.fill.fore_color.rgb = RGBColor(0, 0, 0)
    line.line.fill.background()


def build_command(args: argparse.Namespace) -> None:
    if Presentation is None:
        fail("python-pptx is required for build.")

    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    prs = Presentation(args.reference_pptx) if args.reference_pptx and Path(args.reference_pptx).exists() else Presentation()
    prs.slide_width = Inches(13.333333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # Start from a fresh deck even when a reference was used for dimensions/theme.
    while len(prs.slides) > 0:
        r_id = prs.slides._sldIdLst[0].rId
        prs.part.drop_rel(r_id)
        del prs.slides._sldIdLst[0]

    cover = prs.slides.add_slide(blank)
    paper_meta = manifest.get("paper", {}) if isinstance(manifest.get("paper"), dict) else {}
    title_zh = args.title_zh or paper_meta.get("title_zh") or args.cover_title
    journal_if = args.journal_if or paper_meta.get("journal_if") or ""
    author_school = args.author_school or paper_meta.get("author_school") or ""
    cover_path = manifest.get("cover_crop_image") or manifest.get("cover_image")
    if cover_path and Path(cover_path).exists():
        add_fit_picture(cover, cover_path, 0.25, 0.18, 12.85, 5.25)
    if title_zh:
        add_text(cover, title_zh, 0.65, 5.35, 12.2, 0.92, size=26, bold_first_label=False)
    meta_lines = [line for line in [f"IF {journal_if}" if journal_if else "", author_school] if line]
    if meta_lines:
        add_text(cover, "  |  ".join(meta_lines), 0.7, 6.38, 11.95, 0.48, size=18, bold_first_label=False)

    for fig in iter_slide_figures(manifest.get("figures", [])):
        image_path = fig.get("image_path", "")
        if not image_path or not Path(image_path).exists():
            continue
        slide = prs.slides.add_slide(blank)
        add_header(slide, args.header_title)
        with Image.open(image_path) as im:
            aspect = im.width / max(1, im.height)
        panel_count = len(fig.get("zh_panel_captions") or fig.get("panel_captions") or [])
        caption_size = int(fig.get("caption_size") or min(args.caption_size, 14 if panel_count >= 5 else args.caption_size))
        layout = fig.get("layout", "")
        if layout == "top-bottom":
            add_fit_picture(slide, image_path, 0.45, 0.88, 12.35, 4.25)
            add_caption(slide, fig, 0.65, 5.18, 12.0, 1.9, size=caption_size)
        elif layout != "left-right" and aspect >= 1.75 and panel_count <= 4:
            add_fit_picture(slide, image_path, 0.35, 0.9, 12.65, 4.35)
            add_caption(slide, fig, 0.55, 5.32, 12.25, 1.85, size=caption_size)
        else:
            image_box_w = float(fig.get("image_box_w") or (6.85 if panel_count >= 5 else 7.25))
            image_x = float(fig.get("image_x") or 0.25)
            image_y = float(fig.get("image_y") or 0.88)
            image_box_h = float(fig.get("image_box_h") or 6.32)
            pic = add_fit_picture(
                slide,
                image_path,
                image_x,
                image_y,
                image_box_w,
                image_box_h,
                valign=fig.get("image_valign", "center"),
            )
            pic_right = pic.left / 914400 + pic.width / 914400
            text_x = max(pic_right + 0.25, float(fig.get("min_text_x") or 6.85))
            text_x = min(text_x, float(fig.get("max_text_x") or 9.15))
            text_y = float(fig.get("text_y") or 0.92)
            text_h = float(fig.get("text_h") or 6.25)
            add_caption(slide, fig, text_x, text_y, 13.08 - text_x, text_h, size=caption_size)

    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(qpath(out))
    print(f"Wrote {out}")


def crop_command(args: argparse.Namespace) -> None:
    src = Path(args.image).resolve()
    out = Path(args.out).resolve()
    if len(args.bbox) != 4:
        fail("--bbox must contain four pixel values: x0 y0 x1 y1")
    with Image.open(src) as im:
        crop = im.crop(tuple(args.bbox))
        out.parent.mkdir(parents=True, exist_ok=True)
        crop.save(out)
    print(f"Wrote {out}")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_extract = sub.add_parser("extract", help="Render PDF pages, extract candidate figures, and write manifest.json.")
    p_extract.add_argument("--pdf", required=True)
    p_extract.add_argument("--workdir", required=True)
    p_extract.add_argument("--dpi", type=int, default=220)
    p_extract.add_argument("--pdftoppm")
    p_extract.add_argument("--min-width-pt", type=float, default=110)
    p_extract.add_argument("--min-height-pt", type=float, default=80)
    p_extract.add_argument("--min-area-ratio", type=float, default=0.015)
    p_extract.add_argument("--padding-px", type=int, default=8)
    p_extract.add_argument("--max-caption-lines", type=int, default=8)
    p_extract.add_argument("--cover-crop-ratio", type=float, default=0.32)
    p_extract.add_argument("--add-page-placeholders", action="store_true")
    p_extract.set_defaults(func=extract_command)

    p_build = sub.add_parser("build", help="Build a PPTX draft from a reviewed manifest.json.")
    p_build.add_argument("--manifest", required=True)
    p_build.add_argument("--out", required=True)
    p_build.add_argument("--reference-pptx")
    p_build.add_argument("--header-title", default="文献汇报")
    p_build.add_argument("--cover-title", default="")
    p_build.add_argument("--title-zh", default="")
    p_build.add_argument("--journal-if", default="")
    p_build.add_argument("--author-school", default="")
    p_build.add_argument("--caption-size", type=int, default=16)
    p_build.set_defaults(func=build_command)

    p_crop = sub.add_parser("crop", help="Crop a rendered page image by pixel bbox.")
    p_crop.add_argument("--image", required=True)
    p_crop.add_argument("--bbox", nargs=4, type=int, required=True)
    p_crop.add_argument("--out", required=True)
    p_crop.set_defaults(func=crop_command)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
