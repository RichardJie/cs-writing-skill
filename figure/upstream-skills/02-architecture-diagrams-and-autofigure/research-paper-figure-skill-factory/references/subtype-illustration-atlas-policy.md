# Subtype Illustration Atlas Policy

Version: 2.0.5

Generated specialized figure-making skills must include a saved subtype/style illustration atlas. The atlas exists to make subtype, layout, and visual-style choices visible before the user chooses a direction.

## Required Asset Structure

```text
assets/subtype-atlas/manifest.json
assets/subtype-atlas/boards/
assets/subtype-atlas/thumbnails/
references/subtype-illustration-atlas.md
```

The atlas is package-local and must be included in the generated skill zip. Do not rely on external temporary paths for these assets.

## Required Coverage Angles

Cover every angle that is relevant to the generated figure class. At minimum include:

- reader question;
- narrative role;
- logical gap;
- visual rhetoric;
- visual grammar / layout;
- paper slot;
- density / detail level;
- visual communication art style.

Each supported subtype under each angle needs at least one representative thumbnail or mini-panel. Prefer labeled composite boards. For large taxonomies, use hierarchical boards: one overview board plus per-angle boards.

## Rendering Route

When generating atlas images:

1. ChatGPT web uses **Create image** through **ChatGPT Images 2.0**.
2. Codex uses `$imagegen` first.
3. If `$imagegen` is unavailable in Codex, use ChatGPT Images 2.0 API or another approved image-generation API.

Do not substitute SVG, Mermaid, TikZ, Graphviz, HTML/CSS, canvas, matplotlib, or other code-rendered diagrams for atlas images.

## Manifest Requirements

Every atlas asset entry must record:

- asset id;
- classification angle;
- subtype;
- image path;
- thumbnail path;
- board path;
- generation route;
- build time or build id;
- intended use;
- transferable visual attributes;
- limitations.

## Display Rules

Generated specialized skills must:

- display all available saved subtype/style boards on first startup with actual Markdown image embeds, without target-paper analysis or target-paper image generation;
- display relevant saved boards/thumbnails in later text replies that discuss subtype, layout, visual grammar, density, style, metaphor, modeling pattern, candidate scheme differences, or final content architecture with actual Markdown image embeds;
- display relevant saved boards/thumbnails or non-target visual-structure concept images in later text replies that explain visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture; prose-only structure descriptions are not valid display;
- record missing assets and recommend atlas repair if the relevant board is absent;
- keep target-paper candidate/final/revision image generation in separate `IMAGE_ONLY` turns.
- require non-target concept diagrams or skill-modeling example images in text replies when an abstract-decision trigger has no sufficient saved atlas/reference image; these explanatory references do not satisfy the first-round candidate-image bridge, the P6b-IMAGE second-round variant gate, or P8.

Display means renderable Markdown image syntax such as:

```markdown
![Subtype atlas](assets/subtype-atlas/boards/subtype-overview.png)
```

In Codex desktop, resolve that package-relative path to an absolute filesystem path before embedding, for example:

```markdown
![Subtype atlas](~/.codex/skills/<skill-name>/assets/subtype-atlas/boards/subtype-overview.png)
```

A plain path list, manifest excerpt, or prose statement that an atlas exists is not a valid display. If the host cannot render the saved package image, record `reference_display_render_status: attempted_host_blocked` and list the exact asset paths.

Saved image display in a `TEXT_ONLY` reply is allowed only for already-generated package-local assets. If a required non-target concept/modeling example must be newly generated, the generated skill must either use a host-supported inline non-target image route or record `concept_example_status: generation_pending` / `missing_recorded` plus the repair action. Calling target-paper image generation in that same prose reply is invalid.
