---
name: seaslides-typst-slides-skill
description: >
  AI-driven presentation generation system using Touying/Typst. Converts source documents
  (PDF/DOCX/URL/Markdown) into high-quality Typst slides through either a multi-role Full Mode
  workflow or direct existing-theme Quick Mode authoring, and exports to PDF/PNG/PPTX. Use this
  skill whenever the user
  wants to create slides, make a presentation, build a deck, convert a PDF/document to slides,
  turn notes into a presentation, or anything involving Typst/Touying slide generation.
  Trigger phrases include: "create slides", "make presentation", "generate slides",
  "convert to slides", "turn into a deck", "keynote", "PPT", "slide deck",
  "生成PPT", "做幻灯片", "制作演示文稿", "用Typst做演示", "做个汇报", "转成幻灯片",
  or mentions "seaslides-typst-slides-skill". Even if the user does not explicitly say "slides" or
  "presentation", use this skill when the intent is clearly to create visual presentation
  materials from source content.
---

# SeaSlides Typst Slides Skill

Convert source material into a compiled Touying/Typst presentation with review depth matched to
the user's intent.

**Full pipeline**: `Source -> Project -> Theme -> Strategist -> [Images] -> Executor -> Compile -> Review -> Export`

**Quick pipeline**: `Source -> Project -> Existing Theme -> Author -> Compile -> [Review] -> Export`

## Contents

- [Hard Contract](#hard-contract)
- [Mode Routing](#mode-routing)
- [Scenario Routing](#scenario-routing)
- [Resource Map](#resource-map)
- [Full Mode Workflow](#full-mode-workflow)
- [Editing an Existing Deck](#editing-an-existing-deck)
- [Dependencies](#dependencies)

## Hard Contract

1. Run the selected mode's phases serially. Complete each gate before entering the next phase.
2. Ask for required user decisions at blocking gates. In unattended mode, decide them and continue.
3. Convert PDF, DOCX, PPTX, spreadsheet, and web sources to Markdown before planning slides.
4. Keep content and theme concerns separate. In Plain/Rich mode, do not add ad hoc visual styling to `main.typ`.
5. For project-owned and custom themes, import Touying exactly as
   `#import "@preview/touying:0.7.4": *`. A third-party Universe theme may own
   an older transitive Touying version; use that package's documented API and
   never add a conflicting direct import or edit the package cache.
6. Compile, run mechanical quality checks, and validate before delivery. Match visual-review depth
   to the user's request; when the user explicitly opts out, skip visual inspection and disclose
   that the output was not visually reviewed.
7. Treat a project without `output/slides.pdf` and `output/overview.png` as incomplete.
8. Add `#speaker-note[...]` to every slide.
9. In Quick Mode, omit the separate design spec and role references only as defined in
   `${SKILL_DIR}/workflows/quick-mode.md`; rules 3-8 still apply.
10. At startup and each phase transition, briefly tell the user the mode, current phase, and action
    in their language. Also update on blockers or after about one minute of silence; do not narrate
    individual commands.
11. Reuse an existing editor or user workspace in place. Never run project initialization inside it,
    and pass its active workspace-relative Typst entry to every compile, audit, and validation step.

Use `${SKILL_DIR}/references/shared-standards.md` as the canonical Typst/Touying contract and anti-pattern reference.

## Mode Routing

Use Quick Mode when the user explicitly prioritizes speed, requests a first usable draft, or
accepts reasonable defaults. Follow `${SKILL_DIR}/workflows/quick-mode.md`.

Use Full Mode for the standard pipeline, or when the task needs a new/materially extended theme,
new image acquisition, substantial research or sourcing, a formal design specification, complex
chart calibration, or long-deck phase resumption.

Quick Mode is a workflow choice, while Plain, Rich, and Canvas are theme complexity tiers. Prefer
Rich or Plain when they fit equally well and are faster to author. Canvas remains eligible when
the selected existing theme's `theme.md` and `demo.typ` already expose a clear, compilable path.
Honor a named, scaffolded, or existing theme in either mode.

In Quick Mode, infer visual-review depth without adding a decision gate: honor an explicit opt-out,
use targeted review for an ordinary fast draft, and inspect every page when the user requests
visual assurance or delivery-grade review.

## Scenario Routing

Route special outputs before entering the standard slide pipeline:

| Intent | Read and follow |
|---|---|
| Academic or conference poster | `${SKILL_DIR}/references/scenarios/poster.md` |
| CV or resume | `${SKILL_DIR}/references/scenarios/cv.md` |
| Social cover, article header, or thumbnail | `${SKILL_DIR}/references/scenarios/social-cover.md` |
| Standard presentation or deck | Continue below |

Match the user's language. Use English section headings in `content_design_spec.md`; write field values in the user's language when appropriate.

For 25+ slide Rich/Canvas decks, use `${SKILL_DIR}/workflows/resume-execute.md` to split planning and execution across sessions.

## Resource Map

Load references only when entering the relevant phase.

### Workflow Routing

| Task | Resource |
|---|---|
| Full creation workflow | `${SKILL_DIR}/workflows/create-presentation.md` |
| Quick creation workflow | `${SKILL_DIR}/workflows/quick-mode.md` |
| Theme selection | `${SKILL_DIR}/workflows/select-theme.md` |
| New theme creation | `${SKILL_DIR}/workflows/create-template.md` |
| Topic-only research | `${SKILL_DIR}/workflows/topic-research.md` |
| Long-deck resumption | `${SKILL_DIR}/workflows/resume-execute.md` |
| Chart calibration | `${SKILL_DIR}/workflows/verify-charts.md` |
| Visual review | `${SKILL_DIR}/workflows/visual-review.md` |
| Audio narration | `${SKILL_DIR}/workflows/generate-audio.md` |

### Reference Authority

Treat each row as the single authority for that concern. Load the detailed file only when the current phase needs it.

| Concern | Authoritative resource | Read when |
|---|---|---|
| Typst/Touying syntax, TCS, layout safety, and hard rules | `${SKILL_DIR}/references/shared-standards.md` | Planning or authoring any Typst output |
| Advanced tables, math, icons, SVG, shadows, and source-image recipes | `${SKILL_DIR}/references/shared-standards-extended.md` | A core-standard link points here or an advanced feature is needed |
| Visual direction, composition, rhythm, and aesthetic anti-patterns | `${SKILL_DIR}/references/design-guide.md` | Establishing visual direction or doing high-craft theme/Canvas work |
| Content strategy and `content_design_spec.md` | `${SKILL_DIR}/references/strategist.md` | Strategist phase |
| Full Mode executor workflow shared by all presentation styles | `${SKILL_DIR}/references/executors/base.md` | Before loading exactly one style executor |
| Theme files, public component APIs, demos, and theme quality gates | `${SKILL_DIR}/references/template-designer.md` | Creating or materially extending a theme |
| Image acquisition dispatch | `${SKILL_DIR}/references/image-base.md` | The design spec requests new images |
| AI image generation and rendering styles | `${SKILL_DIR}/references/image-generator.md` and `${SKILL_DIR}/references/image-renderings/_index.md` | `image-base.md` selects the AI path |
| Licensed web image search and attribution | `${SKILL_DIR}/references/image-searcher.md` | `image-base.md` selects the web path |
| Image placement vocabulary | `${SKILL_DIR}/references/image-layout-patterns.md` | Planning or implementing image-heavy pages |
| Rendered visual review | `${SKILL_DIR}/references/visual-review.md` | The selected review policy requires rendered inspection |
| Visual issue ownership and correction routing | `${SKILL_DIR}/references/artifact-ownership.md` | A defect has been confirmed |

Rendering-style details live in `${SKILL_DIR}/references/image-renderings/<anchor>.md`; use the rendering index to select one anchor before loading its file. The optional controlled comparison gallery is documented in `${SKILL_DIR}/references/ai-image-comparison/README.md` and indexed in `${SKILL_DIR}/references/ai-image-comparison/_index.md`.

### Executor Style Routing

Apply this routing only in Full Mode. Read executor base plus exactly one matching style file.
Complexity tier and executor style are separate decisions; Canvas uses the Canvas executor instead
of also loading a non-Canvas style file. Quick Mode does not load executor references.

| Presentation intent | Style resource |
|---|---|
| Product, training, proposal, marketing, or general-purpose deck | `${SKILL_DIR}/references/executors/general.md` |
| Business review, performance report, or data-heavy consulting deck | `${SKILL_DIR}/references/executors/consultant.md` |
| Board, investment, or MBB-style executive recommendation | `${SKILL_DIR}/references/executors/consultant-top.md` |
| Conference talk, thesis defense, seminar, or research presentation | `${SKILL_DIR}/references/executors/academic.md` |
| Editorial, Swiss, festival, or bespoke page-level composition | `${SKILL_DIR}/references/executors/canvas.md` |

Academic posters remain a scenario workflow and do not use the academic slide executor.

### Resource Hubs and Catalogs

| Need | Human-readable hub | Machine-readable or direct resource |
|---|---|---|
| Script discovery and operational documentation | `${SKILL_DIR}/scripts/README.md` | `${SKILL_DIR}/scripts/docs/` |
| Template resource discovery | `${SKILL_DIR}/templates/README.md` | Per-category indexes below |
| Theme selection | `${SKILL_DIR}/templates/themes/README.md` | `${SKILL_DIR}/templates/themes/<tier>/index.json` |
| Typst packages | `${SKILL_DIR}/templates/packages/README.md` | `${SKILL_DIR}/templates/packages/index.json` |
| Charts and diagrams | `${SKILL_DIR}/templates/charts/README.md` | `${SKILL_DIR}/templates/charts/index.json` |
| Icons and symbols | `${SKILL_DIR}/templates/icons/README.md` | `${SKILL_DIR}/templates/icons/index.json` |
| Content planning schema | — | `${SKILL_DIR}/templates/content_design_spec_reference.md` |
| Theme design schema | — | `${SKILL_DIR}/templates/theme_design_spec_reference.md` |
| Theme API summary schema | — | `${SKILL_DIR}/templates/theme_reference.md` |

Do not enumerate individual themes, charts, packages, or icons in this file. Use their catalogs so the SKILL remains stable as bundled resources evolve.

## Full Mode Workflow

Use the steps below for Full Mode. Quick Mode follows its standalone workflow; reuse the compile,
quality, validation, and export commands below while applying Quick Mode's own review policy.

### Step 1: Process Sources

**Gate**: Source material or a topic is available.

If only a topic is provided, follow `${SKILL_DIR}/workflows/topic-research.md` or generate a source brief before continuing.

| Input | Command |
|---|---|
| PDF | `python3 ${SKILL_DIR}/scripts/source_to_md/pdf_to_md.py <file> --images filtered` |
| DOCX / EPUB / HTML / LaTeX / RST | `python3 ${SKILL_DIR}/scripts/source_to_md/doc_to_md.py <file>` |
| PPTX / PPSX | `python3 ${SKILL_DIR}/scripts/source_to_md/ppt_to_md.py <file>` |
| Excel | `python3 ${SKILL_DIR}/scripts/source_to_md/excel_to_md.py <file>` |
| Web page | `python3 ${SKILL_DIR}/scripts/source_to_md/web_to_md.py <url>` |
| Markdown / text | Read directly |

Do not proceed with only an unread raw document when a converter is available.

### Step 2: Resolve the Workspace

**Gate**: Readable source content exists.

When the user or host editor already provides a workspace, attach it in place:

```bash
python3 ${SKILL_DIR}/scripts/project_manager.py workspace <workspace_path> \
  --entry <workspace-relative-entry.typ> --prepare
```

This creates only missing `assets/`, `output/`, and `sources/` support directories. It does not
create a child project, README, or replacement entry. Keep the returned entry path and pass it as
`--entry` below. If a host such as Tylina supplies workspace and main-file state through a trusted
tool, use that state instead of guessing a filename.

Only initialize a new standalone project when no workspace exists:

```bash
python3 ${SKILL_DIR}/scripts/project_manager.py init <project_name>
python3 ${SKILL_DIR}/scripts/project_manager.py import-sources <project_path> <source_files...> --copy
```

Use `--exact-name` only when a deterministic, date-free directory name is needed (for example, a reproducible benchmark); normal projects retain the dated suffix.

Use `--move` only when the user explicitly requests moving source files. Copy extracted source images into `<project_path>/assets/` and import the converted Markdown.

### Step 3: Select or Create a Theme

**Gate**: Project directory exists.

Follow `${SKILL_DIR}/workflows/select-theme.md`.

1. Use a user-named theme directly.
2. Otherwise inspect the theme dispatch and relevant catalog, then match theme metadata to content, audience, and delivery setting.
3. Use Plain when the user asks for restrained/minimal output. Use Rich as the dependable default.
4. Use Canvas only when bespoke composition materially helps and the executor can correctly handle Typst content/code modes, theme APIs, and a compile probe. Fall back to Rich on uncertainty.
5. Create a new theme only when the library does not fit the content and the task has enough time for implementation plus visual review.

After selection:

```bash
python3 ${SKILL_DIR}/scripts/project_manager.py copy-theme <project_path> <name>
```

Read the copied `theme.md` and `demo.typ`. For Canvas work, also read `template.typ`. Use their documented APIs and structural patterns; do not imitate decorative details mechanically when they do not serve the content.

### Step 4: Produce the Content Design Spec

**Gate**: Theme is selected and understood.

Read:

```text
${SKILL_DIR}/references/strategist.md
${SKILL_DIR}/references/shared-standards.md
```

Present the nine decisions as one bundle and wait, unless unattended mode is active:

1. Page format
2. Page-count range
3. Target audience
4. Style objective
5. Complexity level
6. Color scheme
7. Typography plan
8. Image approach
9. Third-party packages

Choose packages from `${SKILL_DIR}/templates/packages/index.json`. Common choices include mitex for LaTeX math, lilaq for standard charts, gribouille for layered Grammar-of-Graphics plots, codly for optional code styling, lovelace for pseudocode, cheq for checklists, and merman for Mermaid diagrams.

If user images exist, run:

```bash
python3 ${SKILL_DIR}/scripts/analyze_images.py <project_path>/assets
```

Write `<project_path>/content_design_spec.md` from the provided template. Include project settings, a specific theme, packages, narrative, per-slide outline, image decisions, colors, and typography. Record why intentionally excluded assets are not used.

### Step 5: Acquire Images When Needed

**Gate**: The design spec requests AI-generated or searched images.

Read `${SKILL_DIR}/references/image-base.md`, then the selected image workflow.

```bash
python3 ${SKILL_DIR}/scripts/image_gen.py --check-available
```

Generate an asset manifest or prompt file, create/search the images, and verify that required files exist in `assets/`. Skip this phase when the design spec does not need new images.

### Step 6: Author the Presentation

**Gate**: Design spec and required assets are ready.

Read executor base, exactly one style executor, shared standards, and Canvas guidance only when Canvas is selected.

Before writing `main.typ`, reread the copied `theme.md`, `demo.typ`, and `content_design_spec.md`.

Author with these constraints:

- Use theme components and layouts where they express the content clearly; repeated comparison pages may deliberately share a layout.
- Prefer Typst content blocks for rendered component arguments: write `#card[Title][Body]` (or `#card(accent: palette.accent)[Title][Body]`) instead of passing user-facing copy as `"Title"`. Keep strings for genuinely string-valued data such as paths, URLs, enum/config keys, font names, and values that require string operations.
- Use `#cols[...] [...]` for ordinary multi-column composition. Use another theme-specific composer only when its `theme.md` explicitly requires it.
- At caller level, compose complete components directly in natural flow. Do not add a fixed `v()` or wrap adjacent components in `stack()` merely for routine separation; reserve `stack(spacing:)` for elements that form one deliberate visual group.
- Keep ad hoc `rgb()` and `block(fill:)` styling out of Plain/Rich `main.typ`; extend `template.typ` when a reusable visual pattern is missing.
- Use every relevant or user-required asset. Do not insert irrelevant images merely because they exist; record exclusions in the design spec.
- Count title, divider, hero, focus, and appendix pages within the requested range.
- Keep source/debug text, TODOs, unresolved component calls, and diagnostics out of rendered slides.
- Add meaningful speaker notes to every slide.

Treat layout variety, component variety, and rhythm as content-dependent design heuristics rather than numeric quotas. Prefer a coherent repeated structure over arbitrary variation when the narrative calls for comparison or sequence.

### Step 7: Compile, Review, Validate, and Export

**Gate**: `template.typ` and `main.typ` exist.

Run each sub-step in order and rerun compilation after any source change.

#### 7.1 Compile

```bash
python3 ${SKILL_DIR}/scripts/typst_compiler.py <project_path> --all --entry <entry.typ>
```

Require `output/slides.pdf`, per-slide PNGs, `output/overview.png`, and the
coherent `output/compile-manifest.json` receipt written only after the full
`--all` sequence succeeds. On failure, diagnose and retry up to five times.

#### 7.2 Run Mechanical Quality Checks

```bash
python3 ${SKILL_DIR}/scripts/typst_quality_checker.py <project_path> --entry <entry.typ>
```

The default gate fails on `blocker` diagnostics. Treat compilation errors,
missing output/resources, content overflow, layout non-convergence, and an
explicit expected-page mismatch as blocking. `review` diagnostics such as font
fallback and unclassified compiler warnings require source and rendered
inspection; they are not automatic visual failures. Touying's flow-only
`EMPTY_SLIDE` signal is advisory because placement-based pages trigger it even
when visibly populated. Inspect the relevant PNG when visual review is active; if the user opted
out, disclose the unresolved advisory rather than claiming a visual pass. Use
`--expected-pages N` when page intent is known and `--json <receipt.json>` when a machine-readable
audit receipt is needed.

#### 7.3 Perform Visual Review When Selected

Apply the selected scope from `${SKILL_DIR}/workflows/visual-review.md`: inspect the overview and
every slide for `full`, inspect only overview/checker-flagged pages for `targeted`, or skip rendered
inspection for `none`. When inspection is active, use `${SKILL_DIR}/references/visual-review.md`,
fix confirmed defects, and recompile after source changes for up to three iterations.

Evaluate theme fidelity and visual variety in context. Do not redesign a clear repeated sequence solely to satisfy a fixed layout count.

For `none`, state at delivery that the deck was compiled and mechanically checked but not visually
reviewed. Always report review scope separately from result.

#### 7.4 Validate

```bash
python3 ${SKILL_DIR}/scripts/validate_project.py <project_path> --entry <entry.typ>
# Quick Mode only:
python3 ${SKILL_DIR}/scripts/validate_project.py <project_path> --mode quick --entry <entry.typ>
```

Fix reported errors before completion.

#### 7.5 Export

PDF is already available at `output/slides.pdf`. After the selected review policy completes or is
explicitly skipped, export PPTX when requested:

```bash
python3 ${SKILL_DIR}/scripts/typst_compiler.py <project_path> --format pptx
```

### Step 8: Generate Audio When Requested

Follow `${SKILL_DIR}/workflows/generate-audio.md` only after the slide output is stable.

## Editing an Existing Deck

1. Locate and read `main.typ`, `template.typ`, the theme documentation, and the current rendered output.
2. Edit `main.typ` for content or `template.typ` for reusable style changes.
3. Recompile, apply the selected visual-review policy, validate, and re-export.
4. Re-run planning only when the requested change alters narrative, theme, or deck structure.

## Dependencies

```bash
pip install -r ${SKILL_DIR}/requirements.txt
```

When `uv` is available, prefer an isolated environment owned by the calling application or user.
Do not install into the system Python or modify shell startup files. A host-managed runtime should
invoke these scripts through its stable tool interface rather than asking the Agent to locate or
install `uv` itself.

Use `typst watch <project_path>/main.typ` for local preview, but still run the project compiler and validation pipeline before delivery.
