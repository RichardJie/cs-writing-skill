# Research Paper Figure Skill Factory

Version: 2.0.5

This guide is a two-layer Skill Factory:

1. Build a specialized figure-making skill for a chosen paper-figure class from lawful source acquisition, full-feasible local PDF coverage, structured figure/caption evidence, taxonomy, saved subtype/style atlases, and skill-package testing.
2. Use that generated specialized skill to design, generate, review, and integrate concrete figures for arbitrary target papers of that class.

## Core Rules

- First trigger only shows the plan; no analysis or target-paper image generation.
- B1-B9 are the Skill Builder layer.
- P1-P6/P6b/P6b-IMAGE/P6c/P7-P9 are the generated Figure Production layer.
- Generated specialized skills must include saved subtype/style illustration atlases in their packages.
- Generated specialized skills must display available saved atlas boards on startup and relevant saved atlas boards in later style/layout/subtype text turns with Markdown image embeds, not plain path lists.
- Text turns that explain or compare subtype, layout grammar, visual style, density, metaphor, modeling pattern, candidate scheme differences, or final content architecture must display a saved reference or non-target concept/modeling example image, or record missing status and repair action.
- Text turns must not describe visual structure, layout skeleton, panel choreography, module topology, arrow grammar, or content architecture with prose or bullets only; they must embed a saved reference or non-target visual-structure concept/modeling image when technically possible.
- Generated specialized skills must mark every step as `TEXT_ONLY` or `IMAGE_ONLY`.
- Target-paper candidate/final image generation must never be combined with prose.
- ChatGPT web uses Create image through ChatGPT Images 2.0.
- Codex uses `$imagegen` first; if unavailable, use ChatGPT Images 2.0 API or another approved image-generation API.
- SVG, Mermaid, TikZ, Graphviz, HTML/CSS, canvas, matplotlib, and code-rendered images are forbidden as visual outputs or fallbacks.
- Full-feasible local corpus coverage is required before production-grade generated skill locking when many relevant PDFs exist.

## v2.0.5 Visual Structure Images, Concept Examples, And Two-Round Selection

Generated figure-making skills must prebuild and package a saved atlas:

- `assets/subtype-atlas/manifest.json`
- `assets/subtype-atlas/boards/`
- `assets/subtype-atlas/thumbnails/`
- `references/subtype-illustration-atlas.md`

The first generated-skill startup reply displays available saved boards with Markdown image embeds without target-paper image generation. Later abstract-decision text replies must also display saved references or non-target concept/modeling examples with Markdown image embeds. If the reply explains visual structure, the structure itself must be shown as an embedded image; text can name axes and constraints, but it cannot be the only representation of the structure. These references never count as target-paper candidate images.

The visual selection workflow is now explicitly two-round:

1. First round: P4/P5 generate 4-6 diverse candidate images, normally 6, to establish the broad direction.
2. P6: compare the first-round batch and select the current best direction.
3. Second round: P6b/P6b-IMAGE generate 4-6 paper-local best-practice variants, normally 6, around the selected direction.
4. P6c: compare second-round variants and lock the final direction.
5. P7 can build the final prompt only after P6c, unless the user explicitly overrides the second round and the limitation is recorded.
