# Figure Brief Template

```markdown
## Figure Brief
- Figure thesis:
- Paper slot:
- Reader question:
- Logical gap:
- Narrative role:
- Primary figure type:
- Backup figure type:
- 10-second reader effect:
- 60-second reader understanding:
- Must include:
- Must exclude:
- Visual rhetoric:
- Layout skeleton:
- Layout skeleton display: must be an embedded saved/reference or non-target visual-structure image when discussed; do not rely on prose/bullets only
- Style family:
- Saved atlas/reference images displayed:
- Saved atlas/reference Markdown embeds rendered:
  - `![Atlas label](assets/subtype-atlas/boards/<board>.png)` or Codex absolute filesystem equivalent
- Inline non-target concept/example images displayed:
  - `![Concept example](assets/subtype-atlas/boards/<concept-example>.png)` or Codex absolute filesystem equivalent
- Concept/example requirement:
  - concept_example_required: false / true
  - concept_example_status: not_needed / displayed_saved_reference / generated_inline / generation_pending / missing_recorded
  - concept_example_role: none / saved_atlas / non_target_reference / concept_example
  - concept_example_trigger_reason: none / subtype / layout_grammar / visual_style / density / metaphor / modeling_pattern / candidate_scheme_differences / final_content_architecture
- Visual-structure image requirement:
  - visual_structure_image_required: false / true
  - visual_structure_image_status: not_needed / displayed_saved_reference / generated_inline / generation_pending / missing_recorded
  - visual_structure_image_role: none / saved_atlas / non_target_reference / concept_example
  - visual_structure_image_trigger_reason: none / visual_structure / layout_skeleton / panel_choreography / module_topology / arrow_grammar / candidate_board_structure / second_round_optimization_geometry / final_content_architecture
- Target-paper images embedded in this text brief: false
- Missing atlas/reference/concept images:
- Visual communication art style:
- Label strategy:
- Evidence / case anchor:
- Candidate generation mode: `multi_scheme_multi_image` | `single_scheme_multi_image`
- Text candidate count: default 6, allowed 4-6
- First-round image candidate count: default 6, allowed 4-6
- First-round purpose: maximize direction-level diversity
- First-round varied axes: subtype / layout grammar / metaphor / density / panel rhythm / style family
- Candidate comparison focus:
- First-round candidate map:
  - Candidate A: source scheme / broad variant / comparison purpose
  - Candidate B: source scheme / broad variant / comparison purpose
  - Candidate C: source scheme / broad variant / comparison purpose
  - Candidate D-F: optional source scheme / broad variant / comparison purpose
- Selected first-round visual candidate:
- Best-practice divergence:
  - best_practice_divergence_status: not_started / required_after_first_selection / setup_ready / generated / reviewed / final_locked / overridden_by_user
  - best_practice_divergence_axes: []
  - fixed elements from first-round winner: []
  - paper-local details to vary: module relationships / evidence or case anchor / label economy / panel transition / color semantics / callout placement / reviewer readability
- Second-round image candidate count: default 6, allowed 4-6
- second_round_candidate_batch_id:
- selected_second_round_candidate:
- Final direction source: P6c selected second-round candidate
- Default recommendation:
```

## Turn-Separation Note

This brief is a `TEXT_ONLY` artifact. It may include already-saved package-local atlas/reference images and must include non-target concept/modeling example images when an abstract-decision trigger applies and no sufficient saved reference is available. When visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture is discussed, include a saved/reference or non-target visual-structure image as a real Markdown embed; do not use prose/bullets only and do not only list paths.

After presenting P4 or P6b setup, do not perform target-paper image generation in the same response. Ask the user to confirm the desired count; generate first-round target-paper candidates only in a later P5 `IMAGE_ONLY` response, and generate second-round variants only in a later P6b-IMAGE `IMAGE_ONLY` response. P7 final prompt construction is allowed only after P6c records and locks the second-round direction, unless the user explicitly overrides the second round and the limitation is recorded.
