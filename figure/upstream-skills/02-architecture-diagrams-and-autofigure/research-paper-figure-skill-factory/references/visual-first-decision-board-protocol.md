# Visual-First Decision Board Protocol

Version: 2.0.5

This protocol prevents generated figure-making skills from becoming text-only questionnaires. It also prevents the specific failure where a generated skill proposes 4-6 text candidates and then has no step that actually generates candidate images for selection.

## Core Rule

If a generated skill presents multiple schemes, layouts, styles, metaphors, density levels, figure subtypes, or prompt alternatives, it must move through this sequence:

1. `TEXT_ONLY`: present text options, display relevant saved subtype/style atlas boards or non-target concept/modeling examples with Markdown image embeds when the text explains abstract visual decisions or visual structure, and recommend visual comparison.
2. `TEXT_ONLY`: set up a diverse first-round visual candidate board, embedding a generic structure/reference image instead of prose-only structure description.
3. `IMAGE_ONLY`: generate/display multiple diverse first-round candidate images or schematic candidates.
4. `TEXT_ONLY`: record the image batch and select the strongest current direction.
5. `TEXT_ONLY`: set up P6b best-practice divergence, optimizing the selected direction around paper-local details.
6. `IMAGE_ONLY`: generate/display multiple second-round paper-local variants.
7. `TEXT_ONLY`: record the second-round batch and lock the final visual direction.

Do not let the user lock a target-paper visual direction from text alone unless the user explicitly asks to skip image candidates. Record the skip. Do not let P6 first-round selection move directly to P7/P8 unless the user explicitly overrides the second round and the limitation is recorded. Saved atlas boards and inline non-target concept/modeling example images support understanding, but they do not replace the target-paper first-round candidate-image bridge or the second-round variant generation gate.

## First-Round Visual Candidate Board Setup

The setup turn must state:

- board type: subtype / scheme / layout / style / metaphor / density / prompt;
- candidate count: 4, 5, or 6, default 6;
- varied axis: high-level direction-setting differences such as subtype, layout grammar, metaphor, density, panel rhythm, or style family;
- fixed elements: paper thesis, target slot, required modules, sample-image transfer constraints, and user hard constraints;
- rendering route: ChatGPT web Create image / ChatGPT Images 2.0; Codex `$imagegen` first; API fallback only if unavailable;
- comparison criteria: what the user should choose for;
- saved/concept reference images displayed: package-local atlas boards, thumbnails, or non-target concept/modeling examples shown in the text turn with Markdown image embeds, or missing assets recorded.
- visual-structure image displayed: a saved atlas/reference or non-target structure concept/modeling image for layout skeleton, panel choreography, module topology, or arrow grammar; prose/bullets alone do not count.

The setup turn is text-only and stops before target-paper candidate generation.

## First-Round Image-Only Board Generation

The target-paper first-round board generation turn must be `IMAGE_ONLY`:

- no prose;
- no state footer;
- no captions or analysis;
- 4-6 diverse candidates, normally 6;
- native image generation only.

Allowed route: ChatGPT web Create image through ChatGPT Images 2.0, or Codex `$imagegen` first. If `$imagegen` is unavailable, use ChatGPT Images 2.0 API or another approved image-generation API. PNG/JPG/JPEG/WebP outputs from that route are allowed.

Forbidden: SVG, Mermaid, TikZ, Graphviz, HTML/CSS, canvas, matplotlib, filesystem code drawing, or code-rendered/exported images.

## P6 First-Round Review Turn

The next text turn after the first-round board must:

1. record the image batch as `candidate_image_batch_id`;
2. summarize candidate IDs or positions;
3. recommend the strongest current direction and why;
4. identify first-round risks/edits;
5. set `best_practice_divergence_status: required_after_first_selection`;
6. ask the user to proceed to P6b paper-local optimization or request another diverse first-round board;
7. update state fields;
8. end with standard next prompts.

P6 is not a final lock. It cannot enter P7 unless P6b/P6b-IMAGE/P6c has completed or the user explicitly overrides that gate.

## P6b Paper-Local Best-Practice Divergence Setup

The P6b setup turn must state:

- second-round count: 4, 5, or 6, default 6;
- fixed elements from first-round winner: subtype, main layout grammar, core metaphor, major panel order, or style family;
- varied local axes: module relationships, evidence/case anchor, label economy, panel transition, color semantics, callout placement, reviewer readability;
- comparison criteria: which variant communicates the local mechanism with the least ambiguity and best paper fit;
- required reference display: a saved reference or non-target concept/modeling example image with Markdown image syntax, or missing/repair state.
- required visual-structure display: a saved reference or non-target optimization-structure image with Markdown image syntax; paper-specific previews belong in P6b-IMAGE, not text.

The P6b setup turn is `TEXT_ONLY` and stops before second-round generation.

## P6b-IMAGE Second-Round Generation

The second-round generation turn must be `IMAGE_ONLY`:

- no prose;
- no state footer;
- no captions or analysis;
- 4-6 variants, normally 6;
- native image generation only;
- a new `second_round_candidate_batch_id`, not the first-round `candidate_image_batch_id` and not a concept/example image id.

## P6c Second-Round Review Turn

The P6c text turn must:

1. record `second_round_candidate_batch_id`;
2. compare second-round variants by the paper-local axes;
3. select or combine the final direction;
4. set `selected_second_round_candidate`;
5. set `best_practice_divergence_status: final_locked`;
6. make P7 final prompt construction the next allowed step.

## Required Concept/Example Display

Text turns that explain or compare subtype, layout grammar, visual style, density, metaphor, modeling pattern, candidate scheme differences, or final content architecture must display a relevant saved atlas/reference image or non-target concept/modeling example with Markdown image syntax. If unavailable, record `concept_example_required`, `concept_example_status`, `concept_example_role`, `concept_example_trigger_reason`, and the repair action.

Pure state synchronization, caption/body text, simple confirmation, and ordinary restatement of a registered image batch do not require a new concept/example image.

## Required Visual-Structure Display

Text turns that explain visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture must display a relevant saved atlas/reference image or non-target visual-structure concept/modeling example with Markdown image syntax. Prose, bullets, ASCII, Mermaid, SVG, or code-rendered sketches do not count as the structure display. If unavailable, record `visual_structure_image_required`, `visual_structure_image_status`, `visual_structure_image_role`, `visual_structure_image_trigger_reason`, and the repair action.

## State Fields

Generated skills must track:

```yaml
visual_candidate_board_status: not_started | setup_ready | confirmed | generated | reviewed | skipped_by_user
visual_board_type: subtype | scheme | layout | style | metaphor | density | prompt | final_candidate
visual_board_candidate_count: 6
visual_board_axis_varied: ""
visual_board_fixed_elements: []
candidate_image_batch_id: ""
visual_candidate_history: []
selected_visual_candidate: null
visual_candidate_board_skipped_by_user: false
first_round_diversity_goal: direction_level_diversity
first_round_varied_axes: []
best_practice_divergence_status: not_started | required_after_first_selection | setup_ready | generated | reviewed | final_locked | overridden_by_user
best_practice_divergence_axes: []
best_practice_fixed_elements_from_first_round: []
best_practice_local_details_to_vary: []
second_round_candidate_batch_id: ""
second_round_candidate_history: []
selected_second_round_candidate: null
inline_reference_image_role: none | saved_atlas | non_target_reference | concept_example
inline_reference_images_displayed: []
concept_example_required: false
concept_example_status: not_needed | displayed_saved_reference | generated_inline | generation_pending | missing_recorded
concept_example_role: none | saved_atlas | non_target_reference | concept_example
concept_example_trigger_reason: ""
visual_structure_image_required: false
visual_structure_image_status: not_needed | displayed_saved_reference | generated_inline | generation_pending | missing_recorded
visual_structure_image_role: none | saved_atlas | non_target_reference | concept_example
visual_structure_image_trigger_reason: ""
```

## Required Next Prompt Pattern

After a multi-option text reply, the first next prompt must be equivalent to:

`请使用 **<当前skill名称>**，执行，根据当前状态，下一步执行：生成 6 张方向差异尽量大的候选图/示意图供我比较选择。`

After P6 first-round selection, the first next prompt must be equivalent to:

`请使用 **<当前skill名称>**，执行，根据当前状态，下一步执行：进入 P6b，从最佳实践和论文局部细节出发，设置 6 个二轮优化变体方向。`

After P6b setup, the first next prompt must be equivalent to:

`请使用 **<当前skill名称>**，执行，根据当前状态，下一步执行：生成 6 张二轮论文局部优化变体图供我比较选择。`

The fallback prompt remains:

`请使用 **<当前skill名称>**，根据当前状态，提供下一步提问建议。`

## Startup Boundary

Never generate a visual decision board in the first/startup reply. If the first message requests candidate images, record it as pending and show startup text only.
