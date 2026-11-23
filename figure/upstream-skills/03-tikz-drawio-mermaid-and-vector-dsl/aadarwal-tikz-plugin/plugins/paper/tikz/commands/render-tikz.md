---
description: Compile a standalone TikZ file to PDF (and PNG for preview).
argument-hint: "<figure.tex> [--svg] [--keep]"
---

Compile the TikZ file at the path in `$ARGUMENTS` (or the most recent `.tex` file in the cwd if empty), render it, and **visually audit the result**. Flags: `--svg` also emits an SVG; `--keep` skips cleanup.

The file should use `\documentclass{standalone}` so the output crops tightly to the figure. If it doesn't, warn the user that the rendered output will include full page whitespace.

The loop is compile → render → look → fix. Generating without looking reliably ships broken figures; the look step is mandatory, not optional.

## 1. Compile

```
latexmk -pdf -interaction=nonstopmode -halt-on-error <file>
```

Prefer `latexmk` over raw `pdflatex` — it handles multi-pass compilation (pgfplots tables, `intersections`) automatically. If the file uses `\write18` features (e.g., `contour gnuplot`), add `-shell-escape`. If `latexmk` isn't installed, fall back to `pdflatex -interaction=nonstopmode` and note the user should install latexmk for robustness.

**On error**, parse the `.log`: the real errors are lines starting `! `. TikZ errors report wrong line numbers (macro expansion) — read the surrounding context, not just the number. Common causes:

- Missing semicolon at end of `\draw` / `\node` / `\path`.
- Unknown TikZ key (typo, or library not loaded — check `\usetikzlibrary{...}`).
- LaTeX math error inside a label (mismatched `$` or unknown command).
- pgfplots "Dimension too large" — domain too wide or divide-by-zero; restrict `domain=`, raise `samples=`.
- Missing package or library file (`.sty` / `.code.tex` not found) — suggest `tlmgr install <pkg>`.

## 2. Render PNG

```
pdftoppm -r 300 -png <file>.pdf <file>
```

300 DPI — high enough to judge label clearance and line termination.

## 3. READ the PNG and audit it

Open the PNG with the Read tool and check it against the pre-flight checklist (see the tikz-diagrams skill):

- No label collisions — text never overlaps curves, lines, or other labels.
- Arrowheads consistent: one family, one size, throughout.
- Elements that should touch actually touch; dashed reference lines terminate exactly ON the curve — not short, not through.
- Edge labels fit their gaps.
- Nothing clipped by the standalone crop.
- Axes extend slightly past the data (plots).
- No garbled or overlapping text.

## 4. Fix and loop

If the audit finds problems: fix the source, then repeat compile → render → look. Report each iteration in one line ("iter 2: staggered axis labels, dashed line now meets curve"). Cap at ~4 iterations; if issues remain, show the user the final image and list what's still wrong.

## 5. SVG output (`--svg`)

```
pdftocairo -svg <file>.pdf <file>.svg
```

Or, for better text fidelity via the DVI path:

```
dvisvgm --font-format=woff2 --exact-bbox <file>.dvi
```

which needs DVI output — compile with `latex` or `lualatex --output-format=dvi`.

## 6. Report and clean up

Report the output paths (PDF, PNG, SVG if requested) and any log warnings (overfull/underfull boxes, pgfplots compatibility warnings). Then clean intermediates (`.aux`, `.log`, `.fdb_latexmk`, `.fls`) with `latexmk -c` — unless `--keep` was passed or the user asked to keep them.
