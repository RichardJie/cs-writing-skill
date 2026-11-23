---
description: Create a usable compiled deck quickly from an existing bundled theme
---

# Quick Mode Workflow

Use Quick Mode when the user explicitly prioritizes speed, asks for a first usable draft, or
accepts reasonable defaults. Treat Quick Mode as a workflow choice, not a complexity tier:
Plain, Rich, and Canvas themes are all eligible.

Skip the separate `content_design_spec.md`, Strategist reference, executor references, new-theme
design, and new image acquisition. Keep source conversion, shared standards, speaker notes,
compilation, mechanical quality checks, validation, and requested exports. Match visual-review
depth to the user's intent.

## 1. Prepare the Source and Project

1. Convert non-Markdown source files with the normal source converter and read the result.
2. For a topic-only request, write a concise source brief from reliable information already in
   scope. Switch to Full Mode when research, citation verification, or current/high-stakes facts
   are required.
3. Initialize the project and import the source files with the commands in `SKILL.md`.

Do not use Quick Mode as permission to author from an unread raw document.

## 2. Select One Existing Theme

1. Honor a named, scaffolded, or already copied theme without offering alternatives.
2. Otherwise read the theme dispatcher and only the tier indexes needed to find a fit. Shortlist
   at most five candidates internally and select one without adding a user decision gate.
3. Prefer Rich or Plain when two themes fit equally well because their normal-flow authoring is
   faster. Select Canvas when its `theme.md` and `demo.typ` already demonstrate the composition
   the content needs; Canvas alone is not a reason to leave Quick Mode.
4. Do not create or materially extend a theme in Quick Mode.
5. Copy the selected theme into the project. Read the copied `theme.md`, `demo.typ`, and
   `${SKILL_DIR}/references/shared-standards.md`. Read `template.typ` only when the public docs
   and demo leave an API/layout question or a compile error points to the implementation.

## 3. Author Directly

Choose a concise narrative, page-count target, and slide order, then write `main.typ` directly.
Do not create a substitute mini design-spec file.

- Favor a plain authoring vocabulary: headings, short paragraphs, lists, `#cols[...] [...]`, and
  a small set of documented theme components. “Plain authoring” does not require a Plain theme.
- Use only component calls and slide patterns documented in `theme.md` or proven by `demo.typ`.
- Prefer Typst content blocks for rendered copy: `#card[Title][Body]`, not
  `#card("Title")[Body]`. Keep strings for paths, URLs, enum/config keys, font names, and values
  that genuinely require string operations.
- Reuse a Canvas theme's demonstrated composer or layout skeleton. Do not invent new page
  geometry; use `place()` only when adapting the same pattern shown by the demo and verify it with
  a compile probe.
- Use relevant user/source images and assets required by the theme. Do not search for or generate
  new images, add optional packages, build new components, or add decorative SVG merely to make
  the draft look busier.
- Add concise, meaningful `#speaker-note[...]` content to every slide.

## 4. Compile, Validate, and Review as Requested

Run:

```bash
python3 ${SKILL_DIR}/scripts/typst_compiler.py <project_path> --all
python3 ${SKILL_DIR}/scripts/typst_quality_checker.py <project_path>
```

Apply the Quick Mode policy in `${SKILL_DIR}/workflows/visual-review.md`. Honor an explicit request
to skip visual review. For an ordinary fast draft with no review preference, inspect the overview
and only suspicious pages. Inspect every slide once when the user requests visual assurance or a
delivery-grade review. Fix defects found in the selected review scope, recompile after source
changes, and avoid discretionary polish rounds.

Validate the delivery without requiring a Strategist specification:

```bash
python3 ${SKILL_DIR}/scripts/validate_project.py <project_path> --mode quick
```

Require the same final PDF, overview, slide PNGs, compile receipt, and requested exports as Full
Mode. If visual review was skipped, state that the deck was compiled and mechanically checked but
not visually reviewed; do not report a visual pass.

## 5. Switch to Full Mode When Needed

Switch to the standard workflow when the task requires a new or materially extended theme, new
image generation/search, substantial research or sourcing, a formal design specification,
complex chart calibration, extensive bespoke Canvas geometry, or long-deck phase resumption.
Do not switch merely because the selected existing theme is Canvas.
