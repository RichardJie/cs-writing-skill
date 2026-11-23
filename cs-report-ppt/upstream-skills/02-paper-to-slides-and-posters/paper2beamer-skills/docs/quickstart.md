# Quickstart

This is the shortest path from a paper PDF to a reviewed deck workspace.

## 1. Create a workspace

From this repository:

```bash
cp -r workspace-template ../my-topic-workspace
cp -r skills            ../my-topic-workspace/skills
cd ../my-topic-workspace
```

Put source PDFs under `papers/`.

```text
papers/
  foo.pdf
```

## 2. Optional: describe your field

Edit `domain.md` if the agent should calibrate background depth, terminology,
or evaluation expectations to a specific research area.

## 3. Extract and verify figures

Run the deterministic figure pipeline before slide authoring:

```bash
python3 skills/paper-beamer-deck/scripts/figure_extraction/extract_figures.py \
  papers/foo.pdf --out build/figures/foo
```

Open `build/figures/foo/previews/index.html`.
If anything is marked `needs_manual_review`, edit
`build/figures/foo/figure_overrides.example.json`, save it as
`figure_overrides.json`, and rerun extraction with `--overrides`.

Verify successful records:

```bash
python3 skills/paper-beamer-deck/scripts/figure_extraction/verify_figures.py \
  build/figures/foo/figures.json
```

## 4. Ask the agent to build a deck

Use a prompt like:

```text
Read papers/foo.pdf and create a detailed paper-reading Beamer deck.
Use risk-targeted visual QA. Run figure extraction first, consume
build/figures/foo/figures.json, and generate a quality report before finishing.
```

Outputs go under `slides/<paper-short-name>/`.

## 5. Run final checks

After the deck builds:

```bash
python3 skills/paper-beamer-deck/scripts/check_deck_sources.py slides/foo
python3 skills/paper-beamer-deck/scripts/check_visual_qa.py slides/foo
python3 skills/paper-beamer-deck/scripts/generate_quality_report.py slides/foo \
  --figures-json build/figures/foo/figures.json
```

The checks are aids, not replacements for reading the paper and visually
inspecting the final PDF.

## 6. For multi-paper gap analysis

Put multiple PDFs under `papers/` and ask for a research-gap analysis.
The output goes under `analysis/<topic>/`, with a synthesis deck under
`slides/<topic>-gap-analysis/` unless you ask for memo-only mode.
