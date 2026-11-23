# Prompt Generation and Rendering Policy

Version: 2.0.5

## Prompt Construction Order

1. Figure thesis
2. Paper slot and audience
3. Canvas and layout
4. Panel choreography
5. Required objects, modules, stages, or evidence elements
6. Label strategy
7. Visual rhetoric
8. Style family
9. Saved subtype/style atlas references to display or use
10. Required concept/modeling example display status for abstract decisions
11. Required visual-structure image display status for layout skeleton, panel choreography, module topology, arrow grammar, and content architecture
12. Color semantics
13. Sample/reference-image transfer rules
14. Negative constraints
15. Candidate count and varied axis
16. First-round diversity objective
17. Second-round paper-local best-practice optimization objective

## Builder-Time Atlas Prompt Boundary

During generated-skill construction, create labeled subtype/style atlas images before locking the skill. These are saved reference assets, not user-facing final figures.

Atlas prompts should ask for composite boards with clearly separated mini-panels, visible subtype names, consistent visual language, and enough detail for users to compare subtype/layout/style differences. If many subtypes exist, generate one overview board plus per-angle boards.

Rendering route for atlas assets:

1. ChatGPT web: Create image through ChatGPT Images 2.0.
2. Codex: `$imagegen` first.
3. Codex fallback: ChatGPT Images 2.0 API or another approved image-generation API.

Save the resulting assets under `assets/subtype-atlas/` and record them in `assets/subtype-atlas/manifest.json`. After saving, the next factory `TEXT_ONLY` reply must embed the saved boards with Markdown image syntax. In Codex, resolve package-local paths to absolute filesystem image paths before embedding; in ChatGPT web Sources, attempt saved asset display or package-relative Markdown embeds.

## Candidate-Board Prompt Boundary

Generated skills must distinguish three prompt types:

- **P4 first-round candidate-board brief:** low-commitment visual comparison for establishing the broad direction after text candidates. It should maximize diversity across subtype, layout grammar, metaphor, density, panel rhythm, or style family.
- **P6b second-round optimization brief:** paper-local best-practice divergence around the selected first-round winner. It should keep the chosen direction fixed and vary local module relationships, evidence/case anchors, label economy, panel transitions, color semantics, callout placement, and reviewer-facing readability.
- **P7 final image brief:** formal prompt for the selected direction after P6c has reviewed the second-round image variants and locked the final direction.

Do not use the final image brief as a substitute for either candidate-board step. After 4-6 text candidates, the generated skill must set up and generate/display diverse first-round candidate images before direction selection unless the user explicitly skips image candidates. After P6 selects the current best first-round direction, the generated skill must run P6b/P6b-IMAGE/P6c before P7 unless the user explicitly overrides the second round and the limitation is recorded.

Target-paper candidate-board and second-round variant images are paper-specific outputs. They must not be embedded inside a text reply and must not be mixed with explanation, critique, or state footer text. Use the dedicated P5 and P6b-IMAGE `IMAGE_ONLY` turns.

## Required Concept/Example Image Boundary

Generated skills must include saved atlas/reference images or non-target concept/modeling example images inside `TEXT_ONLY` replies whenever the text turn explains or compares:

- subtype;
- layout grammar;
- visual style;
- density;
- metaphor;
- modeling pattern;
- candidate scheme differences;
- final content architecture.

Pure state synchronization, caption/body text, simple confirmation, and ordinary restatement of an already registered image batch do not require a new concept/example image.

Inline concept/example images must satisfy all of these conditions:

- they are not generated from the user's target paper;
- they are not offered as candidate directions for the user's target paper;
- they are not draft, formal, final, or revision figures;
- they do not use paper-specific modules, data, labels, or claims unless explicitly framed as a generic placeholder;
- they are recorded in state as `non_target_reference` or `concept_example`;
- they do not set `candidate_image_batch_id` or `second_round_candidate_batch_id`.

Inline concept/example images do not satisfy P5, P6b-IMAGE, or P8. If a generated skill wants to turn a concept/example into a target-paper direction, it must still run P4/P5/P6 and then P6b/P6b-IMAGE/P6c.

If a required concept/example image is unavailable, the text turn must record `concept_example_required: true`, `concept_example_status: generation_pending` or `missing_recorded`, `concept_example_role`, `concept_example_trigger_reason`, and the concrete generation/repair action.

## Required Visual-Structure Image Boundary

Generated skills must include a saved atlas/reference image or non-target visual-structure concept/modeling example inside `TEXT_ONLY` replies whenever the reply explains or defines:

- visual structure;
- layout skeleton;
- panel choreography;
- module topology;
- arrow grammar;
- content architecture;
- candidate-board structure;
- second-round optimization geometry;
- final image-brief structure.

Do not use prose, bullets, tables, ASCII diagrams, Mermaid, SVG, or code-rendered sketches as the only representation of the visual structure. Text can name the role, fixed elements, varied axes, and selected image batch/candidate ids, but the structural form itself must be shown as a Markdown image embed when technically possible.

If the only useful preview would be paper-specific, keep it out of the text reply and defer it to P5, P6b-IMAGE, or P8 `IMAGE_ONLY`. The text reply should embed a generic saved reference or non-target structure example and refer to the selected target-paper batch/candidate id instead of redrawing it in prose.

If a required visual-structure image is unavailable, record `visual_structure_image_required: true`, `visual_structure_image_status: generation_pending` or `missing_recorded`, `visual_structure_image_role`, `visual_structure_image_trigger_reason`, and the concrete generation/repair action. Production lock fails until a saved/reference/concept structure image is embedded or a host-rendering block is explicitly recorded.

## First-Round Candidate-Board Setup Template

```text
Board purpose:
Generate diverse target-paper candidate images or schematic candidates for choosing the broad figure direction, not a final figure.

Candidate count:
<4/5/6; default 6>

Hold fixed:
<paper thesis, target slot, required modules, exact labels, sample-image transfer rules, any user-provided hard constraints>

Vary broadly:
<subtype / layout grammar / metaphor / density / panel rhythm / style family>

Compare:
<which direction best explains the method and gives reviewers a stable first impression>

Required reference display:
<Markdown embed for saved atlas/reference or non-target concept/example image, or missing/repair state>

Required visual-structure display:
<Markdown embed for saved atlas/reference or non-target structure concept image; do not provide only a prose/bullet layout description>

Rendering route:
ChatGPT web: Create image through ChatGPT Images 2.0.
Codex: $imagegen first; if unavailable, ChatGPT Images 2.0 API or another approved image-generation API.
```

The setup turn is `TEXT_ONLY` and must stop before generation.

## Second-Round Optimization Setup Template

```text
Second-round purpose:
Optimize the selected first-round direction around paper-local details and best practices before final prompt construction.

Second-round count:
<4/5/6; default 6>

Keep fixed from first-round winner:
<subtype, layout grammar, core metaphor, major panel order, style family>

Vary locally:
<module relationships / evidence or case anchor / label economy / panel transition / color semantics / callout placement / reviewer readability>

Compare:
<which variant communicates the paper's local mechanism with the least ambiguity and best reviewer-facing clarity>

Required reference display:
<Markdown embed for saved atlas/reference or non-target concept/modeling example image, or missing/repair state>

Required visual-structure display:
<Markdown embed for saved atlas/reference or non-target structure concept image; paper-specific second-round previews belong only in P6b-IMAGE>

Rendering route:
ChatGPT web: Create image through ChatGPT Images 2.0.
Codex: $imagegen first; if unavailable, ChatGPT Images 2.0 API or another approved image-generation API.
```

The P6b setup turn is `TEXT_ONLY` and must stop before P6b-IMAGE generation.

## Final Image Brief Template

```text
Create a publication-ready scientific figure for a research paper.

Goal / figure thesis:
<one sentence>

Paper slot and audience:
<introduction / method / results / appendix / rebuttal / slides>

Canvas and layout:
<aspect ratio, panel count, reading order>

Final direction source:
<P6c selected_second_round_candidate and what it keeps from first-round winner>

Required visual-structure display in this TEXT_ONLY reply:
<Markdown embed for saved atlas/reference or non-target structure concept image when explaining final architecture; otherwise refer to selected_second_round_candidate instead of restating its structure in prose>

Panel content:
Panel A: ...
Panel B: ...
Panel C: ...

Labels:
Use only these exact short labels: <list>.

Sample-image transfer:
<per-image attributes to borrow, or none>

Style and color semantics:
<style family, palette role, what each color means>

Candidate variation:
Generate <4/5/6> formal candidates, usually 6. Vary only <minor rendering or polish axis>.

Avoid:
long paragraphs, unreadable labels, fake metrics, logos, watermarks, decorative clutter, SVG/Mermaid/TikZ/Graphviz/code-rendered diagram instructions.
```

## Rendering Route

Target-paper candidate boards, second-round variants, draft candidates, final visuals, and revisions must use native image generation:

1. ChatGPT web: Create image through ChatGPT Images 2.0.
2. Codex: `$imagegen` first.
3. Codex fallback: ChatGPT Images 2.0 API or another approved image-generation API.

Allowed bitmap outputs from that route: PNG, JPG, JPEG, WebP.

Forbidden target-paper visual outputs/fallbacks: SVG, Mermaid, TikZ, Graphviz, HTML/CSS diagrams, canvas diagrams, matplotlib/code-generated figures, filesystem image exports produced by local code or scripts.

If image generation is unavailable, stop and provide a prompt handoff. Do not substitute code-rendered figures.

## Turn-Level Separation

- P4, P6b, and P7 are `TEXT_ONLY`; they may prepare prompts but must not perform target-paper image generation.
- TEXT_ONLY turns must display already-saved package-local atlas/reference images or non-target concept/example images when an abstract-decision trigger applies, and must embed them with Markdown image syntax when they are available.
- TEXT_ONLY turns must display saved reference or non-target visual-structure images when visual structure/layout skeleton/panel choreography/module topology/arrow grammar/content architecture is discussed; prose-only structure descriptions are not valid.
- P5, P6b-IMAGE, and P8 are `IMAGE_ONLY`; they must contain target-paper image generation only.
- The next text reply after P5, P6b-IMAGE, or P8 must record the image batch in state.
- The first/startup reply must never perform target-paper image generation; generated specialized skills must display available saved atlas boards on startup with Markdown image embeds.
