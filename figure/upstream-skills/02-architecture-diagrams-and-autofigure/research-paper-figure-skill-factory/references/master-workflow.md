# Master Workflow

Version: 2.0.5

This skill is a two-layer Skill Factory.

- **Skill Builder layer (B1-B9):** build, test, patch, package, and lock a reusable specialized figure-making skill for one research-paper figure class, including a saved subtype/style illustration atlas.
- **Figure Production layer (P1-P9 plus P6b/P6c):** after a generated specialized skill is locked, use it to produce concrete figures for arbitrary target papers of that figure class. The first image round maximizes direction-level diversity; the second round optimizes the selected direction around paper-local details.

## Workflow Table

| Code | Layer | Mode | Name | Output |
|---|---|---|---|---|
| S0 | Startup | STARTUP_PLAN_ONLY (TEXT_ONLY) | Startup confirmation gate | Full plan only |
| B1 | Skill Builder | TEXT_ONLY | Target figure class and skill objective | Figure-class brief |
| B2 | Skill Builder | TEXT_ONLY | Literature goal and corpus plan | Corpus plan and inclusion rules |
| B3 | Skill Builder | TEXT_ONLY | Lawful literature acquisition and local corpus artifact | PDFs/manifests/acquisition report |
| B4 | Skill Builder | TEXT_ONLY | Evidence extraction from corpus | Paper cards, figure/caption inventory, evidence map |
| B5 | Skill Builder | TEXT_ONLY | Evidence-backed taxonomy and atlas coverage plan | Taxonomy, lineage, and atlas coverage |
| B6 | Skill Builder | TEXT_ONLY | Saved subtype/style atlas, Markdown image preview, and specialized skill blueprint | Atlas assets, rendered atlas embeds, workflow, state schema, prompt/style/review rules |
| B7 | Skill Builder | TEXT_ONLY | Generate specialized skill | Skill package files |
| B8 | Skill Builder | TEXT_ONLY | Test and patch specialized skill | Test report and patched files |
| B9 | Skill Builder | TEXT_ONLY | Lock generated skill | Locked slug/version/scope/limitations |
| P1 | Figure Production | TEXT_ONLY | Startup/material intake with saved atlas Markdown image display | Material status + rendered saved atlas references |
| P2 | Figure Production | TEXT_ONLY | Figure need diagnosis and routing with relevant atlas Markdown image display | Subtype candidates + default recommendation + rendered atlas references |
| P3 | Figure Production | TEXT_ONLY | Reader effect and 4-6 text candidate schemes with saved style/layout board embeds when relevant | Text candidates + rendered saved reference boards + required visual-candidate next action |
| P4 | Figure Production | TEXT_ONLY | Visual candidate board setup with embedded generic structure/reference image | Board brief: count, varied axis, fixed content, route, structure image embed |
| P5 | Figure Production | IMAGE_ONLY | Diverse first-round visual candidate board generation | 4-6 diverse image/schematic candidates, normally 6 |
| P6 | Figure Production | TEXT_ONLY | First-round candidate review and current-best selection | Recorded first-round batch + selected current direction + required P6b next action |
| P6b | Figure Production | TEXT_ONLY | Paper-local best-practice divergence setup with embedded generic optimization-structure image | 4-6 optimization axes, normally 6, with fixed elements, local details to vary, and structure image embed |
| P6b-IMAGE | Figure Production | IMAGE_ONLY | Second-round variant generation | 4-6 paper-local variant images, normally 6 |
| P6c | Figure Production | TEXT_ONLY | Second-round review and final direction lock | Recorded second-round batch + final selected/combined direction |
| P7 | Figure Production | TEXT_ONLY | Final image brief construction after P6c | Formal prompt/image brief |
| P8 | Figure Production | IMAGE_ONLY | Formal figure candidate generation | Formal image batch only |
| P9 | Figure Production | TEXT_ONLY | Review and paper text package | Critique, caption, legend, body text, handoff |

## Mandatory Candidate-Image Bridge

The generated production workflow must not stop at text candidates. After any text reply that presents multiple schemes, subtypes, layouts, styles, metaphors, density levels, or prompt alternatives:

1. The first recommended next prompt must ask the user to generate/display multiple diverse candidate images or schematic candidates, normally 6.
2. The next workflow step must be a `TEXT_ONLY` candidate-board setup step unless all setup fields were already confirmed by the user. This first-round setup varies high-level direction axes such as subtype, layout grammar, metaphor, density, panel rhythm, or style family.
3. The following generation step must be `IMAGE_ONLY` and must generate/display 4-6 diverse first-round candidates, normally 6.
4. The next `TEXT_ONLY` step must record the generated image batch and select the strongest current direction.
5. P6b/P6b-IMAGE/P6c must then optimize that selected direction around paper-local details before P7: module relationships, evidence/case anchors, label economy, panel transitions, color semantics, callout placement, and reviewer readability.

Skipping the first-round bridge is allowed only when the user explicitly says to stay text-only or skip image candidates. Record that as `visual_candidate_board_skipped_by_user: true`. Skipping the P6b/P6c second round is a nonstandard user override; record it as a limitation, and do not let default production-grade examples skip it.

## Required Abstract-Decision Concept Examples

When a text turn explains or compares subtype, layout grammar, visual style, density, metaphor, modeling pattern, candidate scheme differences, or final content architecture, it must embed a saved atlas/reference image or a non-target `concept_example` / `non_target_reference` image with Markdown image syntax. Pure state sync, caption/body text, simple confirmations, and ordinary restatements of an already registered image batch do not require a new concept/example image.

If no suitable image exists, the turn must record `concept_example_required: true`, `concept_example_status: generation_pending` or `missing_recorded`, `concept_example_role`, `concept_example_trigger_reason`, and the repair action. Concept/modeling examples never set `candidate_image_batch_id` or `second_round_candidate_batch_id`.

## Required Visual-Structure Image Display

When a text turn explains or defines visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, final image-brief structure, or content architecture, it must embed a saved atlas/reference image or non-target visual-structure `concept_example` / `non_target_reference` image with Markdown image syntax.

Do not let generated skills describe visual structure with prose, bullets, ASCII diagrams, Mermaid, SVG, or code-rendered sketches only. Text can state the role, fixed elements, varied axes, and selected batch/candidate ids, but the structure form must be shown as an embedded image when technically possible.

If the useful preview would contain target-paper-specific modules, claims, data, or final labels, do not embed it in text. Defer the paper-specific preview to P5, P6b-IMAGE, or P8 `IMAGE_ONLY`, and use only a generic structure/reference image in the text reply. Record `visual_structure_image_required`, `visual_structure_image_status`, `visual_structure_image_role`, and `visual_structure_image_trigger_reason`.

## Saved Subtype/Style Atlas Requirement

Generated specialized skills must include a package-local saved illustration atlas:

```text
assets/subtype-atlas/manifest.json
assets/subtype-atlas/boards/
assets/subtype-atlas/thumbnails/
references/subtype-illustration-atlas.md
```

The atlas must cover reader question, narrative role, logical gap, visual rhetoric, visual grammar/layout, paper slot, density/detail level, and visual communication art style. Prefer labeled composite boards and hierarchical boards when there are many subtypes.

The first/startup reply of a generated specialized skill must show all available saved atlas boards with Markdown image embeds when they exist, while remaining startup-only and without target-paper image generation. Later text replies that discuss subtype, layout, visual grammar, density, or visual communication art style must display the relevant saved atlas board/thumbnail with Markdown image embeds when available or record the missing asset and suggest atlas repair. Plain path lists do not count as display.

After B6 creates and saves atlas assets, the factory's next text reply must also embed the newly saved atlas boards. In Codex desktop, local image embeds must use absolute filesystem paths resolved from the generated skill root; in ChatGPT web Sources, use the saved source asset or package-relative image embeds and record host-blocked rendering if necessary.

## Startup Table Requirement

The startup reply must show S0, B1-B9, P1-P6, P6b, P6b-IMAGE, P6c, and P7-P9 as separate rows. Every row must label `TEXT_ONLY`, `STARTUP_PLAN_ONLY (TEXT_ONLY)`, or `IMAGE_ONLY`. The startup reply is a plan only and must not analyze the target paper or generate target-paper images.

## Builder Gate Chain

Use this gate chain for production-grade generated skills:

- B3 complete for B4: `local_corpus.ready_for_extraction: true`
- B4 complete for B5: `extracted_evidence.ready_for_taxonomy: true`
- B5 complete for B6-B7: `evidence_lineage.evidence_lineage_complete: true`

If many local PDFs are available, process all accessible relevant PDFs as far as feasible and record candidate/accessible/processed/skipped counts and skipped reasons. Small samples are limited/pilot evidence unless the user accepts the limitation.

## Rendering Boundary

P5, P6b-IMAGE, and P8 are `IMAGE_ONLY`. They must contain only target-paper generated images/artifacts. Do not prepend a plan or append explanation. P4, P6, P6b, P6c, P7, and P9 are `TEXT_ONLY` and must not perform target-paper image generation in the same response. Text replies must embed already-saved package-local atlas/reference images or non-target concept/modeling examples when abstract-decision or visual-structure triggers apply. These explanatory images must be recorded as `non_target_reference` or `concept_example`, and are not candidate boards, second-round batches, or final figures.

ChatGPT web uses Create image through ChatGPT Images 2.0. Codex uses `$imagegen` first; if unavailable, use ChatGPT Images 2.0 API or another approved image-generation API. Do not substitute SVG, Mermaid, TikZ, Graphviz, HTML/CSS, canvas, matplotlib, or code-rendered images.
