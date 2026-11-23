# Generated Skill Multi-Candidate Policy

Version: 2.0.5

Every generated figure-making skill must inherit this policy.

```yaml
candidate_policy:
  text_candidates_default: 6
  text_candidates_min: 4
  text_candidates_max: 6
  image_candidates_default: 6
  image_candidates_min: 4
  image_candidates_max: 6
  second_round_image_candidates_default: 6
  second_round_image_candidates_min: 4
  second_round_image_candidates_max: 6
  if_user_says_generate_without_count: default_to_6_images
  single_image_only_when_explicit: true
  always_prompt_for_multi_candidate_images: true
  candidate_image_bridge_required_after_multi_option_text: true
  first_round_purpose: maximize_direction_level_diversity
  first_round_varied_axes: [subtype, layout_grammar, metaphor, density, panel_rhythm, style_family]
  second_round_required_after_p6_first_selection: true
  second_round_purpose: optimize_selected_direction_around_paper_local_details
  second_round_local_axes: [module_relationships, evidence_or_case_anchor, label_economy, panel_transition, color_semantics, callout_placement, reviewer_readability]
  required_bridge_steps:
    - TEXT_ONLY_candidate_board_setup
    - IMAGE_ONLY_candidate_board_generation
    - TEXT_ONLY_candidate_review_and_first_round_selection
    - TEXT_ONLY_best_practice_divergence_setup
    - IMAGE_ONLY_second_round_variant_generation
    - TEXT_ONLY_second_round_review_and_final_direction_lock
  key_visual_decision_default: recommend_6_diverse_first_round_candidates_then_6_paper_local_second_round_variants
  rendering_route_for_candidate_images: ChatGPT web Create image through ChatGPT Images 2.0; Codex $imagegen skill first; if unavailable, ChatGPT Images 2.0 API or another approved image-generation API.
  svg_or_code_visual_candidates_allowed: false
  native_image_generation_required: true
  native_generated_bitmap_exports_allowed: true
  allowed_native_bitmap_output_formats: [png, jpg, jpeg, webp]
  forbidden_generated_visual_outputs: [svg, mermaid, tikz, graphviz, html_css_diagram, canvas_diagram, matplotlib_figure, code_generated_figure]
  saved_reference_images_allowed_in_text_turns: true
  concept_examples_required_for_abstract_decision_text_turns: true
  visual_structure_images_required_in_text_turns: true
  prose_only_visual_structure_descriptions_allowed: false
  target_paper_image_generation_allowed_in_text_turns: false
```

## Required Behavior

1. In candidate-scheme steps, provide 4-6 text candidates, normally 6.
2. After presenting text candidates, do not make "choose one from text" the primary next action. The first/recommended next prompt must ask to generate/display candidate images or schematic candidates, normally 6.
3. Add a dedicated `TEXT_ONLY` candidate-board setup step. It must state candidate count, varied axis, fixed elements, rendering route, comparison criteria, and any saved atlas/reference images displayed with Markdown image embeds or missing. The first round should maximize high-level diversity to establish direction.
4. Add a dedicated `IMAGE_ONLY` first-round candidate-board generation step. It must generate/display 4-6 diverse candidate images or schematic candidates, normally 6, with no prose or state footer.
5. Add a dedicated `TEXT_ONLY` first-round candidate-review step. It must record the previous image batch, compare candidates, and select the current best direction. It must not proceed directly to P7.
6. Add a mandatory `TEXT_ONLY` P6b best-practice divergence setup step after P6. It must propose 4-6 paper-local optimization axes, normally 6, and state fixed elements from the first-round winner plus local details to vary.
7. Add a mandatory `IMAGE_ONLY` P6b-IMAGE second-round generation step. It must generate/display 4-6 paper-local variants, normally 6, with a new `second_round_candidate_batch_id`.
8. Add a mandatory `TEXT_ONLY` P6c second-round review step. It must record the second-round batch, compare variants, and lock `selected_second_round_candidate` before P7.
9. If the user says only "continue / draw / generate" after a text-candidate, board-setup, or P6b setup step, default to 6 target-paper images for the relevant round.
10. Generate one image only when the user explicitly asks for one and the workflow gate allows it.
11. Map each first-round image candidate to a scheme, layout, style, metaphor, density, or prompt variant; map each second-round image to a paper-local optimization axis.
12. Track `text_candidate_count`, `image_candidate_count`, `candidate_generation_mode`, `candidate_scheme_ids`, `candidate_comparison_focus`, `visual_candidate_board_status`, `candidate_image_batch_id`, `selected_visual_candidate`, `best_practice_divergence_status`, `best_practice_divergence_axes`, `second_round_candidate_batch_id`, and `selected_second_round_candidate`.
13. Support optional sample/reference images with per-image attribute preferences.
14. If the text turn discusses subtype, layout, visual grammar, density, style, metaphor, modeling pattern, candidate scheme differences, or final content architecture, display the relevant saved atlas board/thumbnail or non-target concept/modeling example with Markdown image embeds when available; if missing, record `concept_example_required`, `concept_example_status`, `concept_example_role`, and `concept_example_trigger_reason` plus the repair action. Plain path lists do not count as display.
15. If the text turn discusses visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture, display the relevant saved atlas/reference image or non-target visual-structure concept/modeling example with Markdown image embeds when available. Do not use prose/bullets/ASCII/Mermaid/SVG/code-rendered sketches as the only structure representation. If missing, record `visual_structure_image_required`, `visual_structure_image_status`, `visual_structure_image_role`, and `visual_structure_image_trigger_reason` plus the repair action.
16. Non-target concept diagrams, visual-structure examples, or skill-modeling example images must be recorded as `non_target_reference` or `concept_example` and must not set `candidate_image_batch_id` or `second_round_candidate_batch_id`.
17. Forbid target-paper candidate images, draft figures, final figures, and revisions inside text replies. Those must use the dedicated `IMAGE_ONLY` bridge steps.

## Required Chinese Reminder

Generated skills must include a reminder equivalent to:

> 以上是默认的 4-6 个文字候选方案，通常 6 个。  
> 下一步不要只从文字方案里定稿；建议先生成 **6 张方向差异尽量大的候选图/示意图**，用于搭建方向。  
> 第一轮选出当前最佳方向后，还不能直接进入最终 prompt；我会再从论文局部细节和最佳实践角度设置 **6 个二轮优化变体**，围绕模块关系、证据/案例锚点、标签经济性、面板过渡、颜色语义、callout 位置和审稿人可读性进行局部优化。  
> ChatGPT 网页版会使用 **Create image** 并通过 **ChatGPT Images 2.0** 生图；Codex 会优先使用 **$imagegen skill**，如果不可用，再使用 ChatGPT Images 2.0 API 或其他批准的图像生成 API。候选图可以输出 PNG/JPEG/WebP 等位图结果，但不会使用 SVG、Mermaid、TikZ、Graphviz、HTML/CSS、canvas、matplotlib 或代码绘图替代。

## Lock/Test Requirement

Fail the generated skill lock if any of these are missing:

- default text candidate count = 6;
- default first-round image candidate count = 6;
- default second-round image candidate count = 6;
- dedicated candidate-board setup step after text candidates;
- dedicated `IMAGE_ONLY` first-round candidate-board generation step;
- dedicated first-round candidate-review/current-best selection step after image generation;
- P6b best-practice paper-local divergence setup after P6 first-round selection;
- P6b-IMAGE `IMAGE_ONLY` second-round variant generation step with `second_round_candidate_batch_id`;
- P6c second-round review/final direction selection before P7;
- next prompts after multi-option text ask for multiple candidate images or schematic candidates;
- rendering route uses ChatGPT web Create image / ChatGPT Images 2.0 and Codex `$imagegen` first;
- forbidden code/vector fallback list;
- state fields for candidate counts, visual board status, image batch ID, selected candidate, `best_practice_divergence_axes`, `second_round_candidate_batch_id`, and `selected_second_round_candidate`;
- saved subtype/style atlas Markdown image embed behavior in multi-option subtype/layout/style turns;
- required concept/modeling example display or recorded repair action for abstract visual decisions;
- required visual-structure image display or recorded repair action for layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture;
- inline concept/example images are never counted as candidate-board images;
- target-paper candidate/final images are never embedded in prose replies.
