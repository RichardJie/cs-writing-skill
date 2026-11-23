---
name: academic-meeting-skills
description: Build Chinese academic meeting and journal-club PowerPoint decks from scientific paper PDFs. Use when the user provides an article PDF and wants the PDF first-page screenshot on slide 1, then each paper figure or figure panel placed in order with Chinese translated/summarized captions near the image, especially for group-meeting PPTX preparation using a provided reference deck style.
---

# Academic Meeting Skills

## Core Workflow

Use this skill for academic meeting paper-PDF-to-PPT tasks where the expected output is a figure-by-figure Chinese deck, not a broad narrative review deck.

1. Confirm the input PDF path and output PPTX path. If the user provides a reference PPTX, use it as the visual reference; otherwise use `assets/reference-style.pptx` if present.
2. Create a scratch directory outside the source PDF folder, for example `<workspace>/work/academic-meeting-skills/<paper-slug>`.
3. Run extraction:

```powershell
& "<python>" "<skill-dir>\scripts\paper_figures_to_ppt.py" extract `
  --pdf "<paper.pdf>" `
  --workdir "<scratch-dir>"
```

4. Open `<scratch-dir>/manifest.json`. Review `figures` in order. Remove irrelevant images such as logos, page decorations, tiny icons, or duplicate crops. If vector figures were not extracted, use the rendered page PNGs under `<scratch-dir>/pages/` and manually crop missing figures.
5. Fill `paper.title_zh`, `paper.journal_if`, and `paper.author_school`. Verify journal IF from a current source because it changes over time. Use the first author's primary university or the corresponding author's university unless the user asks otherwise.
6. Translate each `raw_caption` into both a short figure-level `zh_caption` and panel-level `zh_panel_captions`. Match the reference style: start with `Fig. 2` / `Fig. 3`, then a concise Chinese explanation of what the authors did and what the result means. Add A/B/C/D explanations as separate lines, for example `A: ...`, `B: ...`. Preserve technical terms, units, genes, proteins, methods, and concentrations.
7. For large composite figures with many panels, crop the figure into readable panel groups and add `subslides` in the manifest. Each subslide should point to a cropped image and contain only the relevant panel captions. Increase `caption_size` for these cropped slides.
8. Build a draft deck:

```powershell
& "<python>" "<skill-dir>\scripts\paper_figures_to_ppt.py" build `
  --manifest "<scratch-dir>\manifest.json" `
  --out "<output.pptx>" `
  --reference-pptx "<reference.pptx>"
```

9. Inspect the PPTX. Fix missing figures, wrong order, missing A/B/C/D panel explanations, overlong captions, overlap, or clipped images. Rebuild after editing the manifest.

## Figure And Caption Rules

- Slide 1 must contain only the top citation/title/authors/affiliations screenshot from the PDF first page, not the full first page. Use `cover_crop_image` when available.
- Slide 1 must also show the Chinese paper title, the journal IF, and the authors' school/institution.
- Keep figures in paper order: page order first, then top-to-bottom and left-to-right within the page.
- Put one large figure/panel per slide by default. Combine multiple panels only when they belong together and remain readable.
- Do not squeeze a large multi-panel figure and all panel text into one dense slide. Crop it into logical groups, for example `A/B` on one slide and `C/D/E` on the next, then enlarge the caption font.
- Place Chinese captions close to the relevant figure: below wide figures, to the right of tall figures, or in nearby text boxes for multi-panel slides.
- Prefer a large left-image/right-caption layout for most figures. Use top-image/bottom-caption only for very wide figures. Reduce header height and margins so the image plus caption area fills most of the 16:9 canvas.
- Use Microsoft YaHei for all Chinese and English text in generated decks unless the user asks for a different font.
- Prefer fixed readable caption sizes over automatic text shrinking. Use larger `caption_size`, `line_spacing`, and `space_after_pt` values to fill the page vertically, then shorten text if it overflows.
- Do not translate figure labels inside the image. Only translate/summarize the caption text around the image.
- Do not stop at the first sentence of the original caption. Include the original caption's A/B/C/D panel meanings in `zh_panel_captions` unless the figure has no panel labels.
- Keep captions short enough for a group-meeting presentation. A useful target is one figure-level sentence plus one short line for each panel.
- For long original captions, summarize experimental purpose, condition, readout, and conclusion instead of translating every clause.
- Preserve exact values and symbols: `40 copies ul-1`, `65 C`, `P < 0.05`, gene names, strain names, and assay names.

## Visual Reference

Read `references/style-profile.md` before laying out or manually repairing slides. The bundled `assets/reference-style.pptx` is an example style asset derived from the user's provided deck and can be used as a reference, not as a source of scientific content.

## Script Notes

The script uses local Python packages plus Poppler `pdftoppm` when available. It intentionally creates a manifest for human/Codex review because PDF figure extraction is not perfectly reliable across journals:

- Raster figures usually appear as cropped image files under `<scratch-dir>/figures/`.
- Vector figures may only appear in rendered page screenshots under `<scratch-dir>/pages/`; crop them manually and add them to the manifest.
- Captions are heuristic text extractions. Always review and rewrite `zh_caption` before final PPT generation.

If the automatic extractor misses too much, use the rendered page PNGs as the source of truth and manually create ordered crops, then edit `manifest.json` to point each figure's `image_path` to the crop.
