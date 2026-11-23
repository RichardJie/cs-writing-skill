---
name: biomedical-figure-production
description: Create, redraw, audit, and package publication-ready biomedical figures, including statistical plots, bioinformatics visualizations, multi-panel layouts, mechanism schematics, graphical abstracts, and hybrid data-plus-illustration figures. Use when a user asks for 科研绘图、医学论文插图、机制图、示意图、图形摘要、CNS/Nature/Cell-style figures, Python/R/Origin plotting, PNG/TIFF/SVG/PDF export, figure legends, statistical annotation, image integrity review, or reproducible figure source packages.
---

# Biomedical Figure Production

Produce figures as evidence-bearing research artifacts. Keep observed data, computed results, visual interpretation, and illustrative hypotheses visibly distinct. Deliver editable sources, reproducible code, publication exports, and a concise audit record.

## Select the workflow

Classify the request before drawing:

1. **Data-driven plot** — tables, matrices, survival data, omics results, statistical summaries. Read `references/routing.md`, then the selected Python or R workflow.
2. **Illustration or mechanism schematic** — cells, tissues, pathways, study designs, graphical abstracts. Read `references/illustration-workflow.md` and `references/evidence-integrity.md`.
3. **Hybrid figure** — measured panels plus illustrative or mechanistic panels. Run both workflows and keep the layers separable.
4. **Audit or export only** — inspect an existing figure, repair layout, or produce journal formats. Read `references/export-qa.md` and use `scripts/validate_figure.py`.

Do not force a plotting backend when the user has already supplied code or named one. If a new data-driven figure could reasonably use either language and the choice materially affects the deliverable, ask whether to use Python or R. Otherwise infer the backend from the source files and installed environment.

## Establish the figure contract

Before implementation, determine or safely infer:

- the single scientific claim each panel supports;
- the provenance and unit of every data field;
- the distinction among measured, associated, inferred, validated, and hypothetical content;
- target journal, final dimensions, color mode, minimum resolution, and required formats;
- accessibility constraints, including color-vision-safe encoding and legible grayscale reproduction;
- whether individual observations, uncertainty intervals, multiplicity handling, and sample-size labels are required.

Use `assets/figure-brief-template.md` when the brief is incomplete. Record final assets with `assets/figure-manifest-template.yaml`.

## Build data-driven figures

1. Preserve raw inputs and create a tidy analysis table without overwriting the source.
2. Define the estimand, comparison, missing-data rule, transformation, and statistical test before rendering significance marks.
3. Prefer effect sizes and confidence intervals to isolated P values. Show individual observations where defensible.
4. Use the isolated Python stack described in `references/python-workflow.md`, or R as described in `references/r-workflow.md`.
5. When installed and applicable, use `$cnsplots` for its supported biomedical chart types. Treat its automatic statistical choices as proposals that still require verification.
6. When installed and applicable, use `$clinical-biostatistics-review` to audit tests, models, denominators, censoring, multiplicity, confidence intervals, and figure-text consistency.
7. For Origin/OriginPro specifications or template compatibility, use `$origin-figure-template` after the analysis is fixed.

Never reconstruct exact values from a low-resolution figure if source data exist. If digitization is unavoidable, label the values as digitized estimates and retain the extraction record.

## Build illustration-style figures

1. Draft an evidence map before a visual composition. Assign an evidence class to each arrow, node, cell state, and anatomical relationship.
2. Use deterministic vector shapes and editable text for labels, arrows, scales, legends, panel letters, and any quantitative element.
3. Use `$imagegen` only for non-quantitative bitmap components or an illustration draft when it materially improves the figure. Inspect supplied reference images first.
4. Keep generated components on separate layers or as separate source files. Do not use generative output as microscopy, histology, anatomy, molecular structure, or experimental evidence.
5. Encode causal strength in line style and legend: direct perturbation, spatial or cohort association, computational inference, cross-tumour extrapolation, and hypothesis must not look equivalent.
6. Add an explicit boundary statement when a schematic contains hypotheses or cross-model extrapolations.

Follow `references/illustration-workflow.md` for the full composition and disclosure procedure.

## Assemble and export

Keep panel construction separate from final assembly. Use a reproducible layout script or a documented Origin template. Avoid manual resizing that changes relative font, stroke, marker, or scale-bar dimensions.

Default package unless the journal specifies otherwise:

- editable vector master: SVG or PDF;
- review preview: PNG at 150–300 ppi;
- submission raster: lossless TIFF, normally 300 ppi for continuous tone and 600 ppi for line art or mixed figures;
- source code and a minimal input-data manifest;
- figure legend, abbreviations, statistical note, and provenance note;
- environment record and SHA-256 manifest.

Read `references/export-qa.md`. Run `scripts/validate_figure.py` on every final PNG/TIFF/SVG/PDF. Render or reopen the exported artifacts and visually inspect them at both full page and 100% scale.

## Apply integrity gates

Stop and disclose the limitation instead of polishing a misleading figure when:

- the plotted numbers cannot be traced to source data or a documented computation;
- sample units, denominators, biological replicates, or censoring rules are unknown;
- a P value or confidence interval cannot be reproduced;
- generated imagery could be mistaken for experimental evidence;
- an arrow presents association or computational inference as proven causality;
- selective cropping, smoothing, contrast, outlier removal, or axis truncation changes the scientific interpretation.

Read `references/evidence-integrity.md` for the audit checklist.

## Verify the environment

Run `scripts/check_environment.py` before a complex job. Use `scripts/setup_python.ps1` and `scripts/setup_r.R` only when the required environment is absent. Keep project-specific environments outside the skill directory and never commit raw patient data or credentials.

## Report completion

State:

- what was created or changed;
- which data and statistical assumptions were used;
- which elements are measured, inferred, or illustrative;
- which formats and editable sources were produced;
- which checks passed and which limitations remain.

