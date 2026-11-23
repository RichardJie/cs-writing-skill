# Specialized Figure Skill Blueprint Template

```yaml
target_figure_class: ""
target_skill_slug: ""
version: ""
domain_scope: ""
intended_paper_slots: []
reader_questions: []
figure_taxonomy_axes: []
figure_type_cards: []
subtype_illustration_atlas:
  required: true
  status: planned
  asset_root: assets/subtype-atlas
  manifest_path: assets/subtype-atlas/manifest.json
  boards_dir: assets/subtype-atlas/boards
  thumbnails_dir: assets/subtype-atlas/thumbnails
  reference_doc_path: references/subtype-illustration-atlas.md
  coverage_angles:
    - reader_question
    - narrative_role
    - logical_gap
    - visual_rhetoric
    - visual_grammar_layout
    - paper_slot
    - density_detail_level
    - visual_communication_art_style
  board_strategy: labeled_composite_boards_with_hierarchical_boards_when_needed
  rendering_route: ChatGPT web Create image through ChatGPT Images 2.0; Codex $imagegen skill first; if unavailable, ChatGPT Images 2.0 API or another approved image-generation API.
  text_turn_display_rule: display relevant saved atlas boards/thumbnails when discussing subtype, layout, visual grammar, density, style, metaphor, modeling pattern, candidate scheme differences, or final content architecture
  required_concept_example_rule: if no saved reference fits an abstract-decision text turn, embed or schedule a non-target concept/modeling example image and record concept_example_required/status/role/trigger_reason
  visual_structure_as_image_rule: if a text turn explains visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture, embed a saved reference or non-target visual-structure concept/modeling image; do not use prose/bullets only
  target_paper_image_isolation_rule: never embed target-paper candidate, second-round variant, draft, final, or revision images in text replies; use IMAGE_ONLY for P5/P6b-IMAGE/P8
  markdown_image_embed_rule: display means actual `![alt](...)` image embeds, not plain path lists
  codex_display_path_rule: resolve package-local atlas paths to absolute filesystem paths before embedding
  chatgpt_sources_display_path_rule: use saved source assets or package-relative Markdown image embeds; record attempted_host_blocked if the host cannot render

workflow:
  production_steps:
    P1: {mode: TEXT_ONLY, purpose: startup_or_material_intake_with_saved_atlas_display}
    P2: {mode: TEXT_ONLY, purpose: figure_need_diagnosis_and_routing_with_required_relevant_reference_or_concept_display}
    P3: {mode: TEXT_ONLY, purpose: reader_effect_and_4_to_6_text_candidates_with_required_abstract_decision_reference_display}
    P4: {mode: TEXT_ONLY, purpose: diverse_first_round_visual_candidate_board_setup, mandatory_after_multi_option_text: true}
    P5: {mode: IMAGE_ONLY, purpose: generate_4_to_6_diverse_first_round_candidate_images_or_schematics}
    P6: {mode: TEXT_ONLY, purpose: record_first_round_batch_review_and_select_current_best_direction}
    P6b: {mode: TEXT_ONLY, purpose: setup_4_to_6_paper_local_best_practice_optimization_axes}
    P6b-IMAGE: {mode: IMAGE_ONLY, purpose: generate_4_to_6_second_round_paper_local_variants}
    P6c: {mode: TEXT_ONLY, purpose: record_second_round_batch_and_lock_final_direction}
    P7: {mode: TEXT_ONLY, purpose: final_image_brief_after_second_round_lock}
    P8: {mode: IMAGE_ONLY, purpose: formal_figure_candidate_or_revision_generation}
    P9: {mode: TEXT_ONLY, purpose: review_caption_legend_body_text_handoff}
  cannot_skip_candidate_image_bridge_unless_user_explicitly_requests_text_only: true
  cannot_skip_second_round_unless_user_explicitly_overrides_and_limitation_recorded: true
  off_recommended_prompt_state_mapping:
    required: true
    applies_to_every_text_reply: true
    execute_valid_user_request_then_map_to_original_step: true
    image_request_in_text_turn_maps_to_text_setup_then_next_image_only: true
    do_not_restart_or_ignore_state_when_prompt_wording_differs: true

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
  rendering_route_for_candidate_images: ChatGPT web Create image through ChatGPT Images 2.0; Codex $imagegen skill first; if unavailable, ChatGPT Images 2.0 API or another approved image-generation API.
  forbidden_generated_visual_outputs: [svg, mermaid, tikz, graphviz, html_css_diagram, canvas_diagram, matplotlib_figure, code_generated_figure]

state_fields:
  - text_candidate_count
  - image_candidate_count
  - candidate_generation_mode
  - candidate_scheme_ids
  - candidate_comparison_focus
  - visual_candidate_board_status
  - visual_board_type
  - visual_board_axis_varied
  - visual_board_fixed_elements
  - candidate_image_batch_id
  - visual_candidate_history
  - selected_visual_candidate
  - visual_candidate_board_skipped_by_user
  - first_round_diversity_goal
  - first_round_varied_axes
  - best_practice_divergence_status
  - best_practice_divergence_axes
  - best_practice_fixed_elements_from_first_round
  - best_practice_local_details_to_vary
  - second_round_candidate_batch_id
  - second_round_candidate_history
  - selected_second_round_candidate
  - subtype_atlas_status
  - subtype_atlas_manifest_path
  - subtype_atlas_boards
  - style_atlas_status
  - style_atlas_manifest_path
  - saved_reference_images_displayed
  - missing_reference_images
  - reference_display_mode
  - saved_reference_markdown_embeds_rendered
  - reference_display_render_status
  - inline_reference_image_role
  - inline_reference_images_displayed
  - concept_example_required
  - concept_example_status
  - concept_example_role
  - concept_example_trigger_reason
  - visual_structure_image_required
  - visual_structure_image_status
  - visual_structure_image_role
  - visual_structure_image_trigger_reason
  - target_paper_images_embedded_in_text_turn
  - target_paper_image_generation_in_current_turn
  - user_request_interpreted_action
  - workflow_step_before_user_request
  - workflow_step_after_user_request
  - state_transition_reason
  - off_recommended_prompt_handling
  - prerequisites_inferred_or_missing
  - live_image_generation_in_current_turn

reference_image_policy:
  optional: true
  multiple_images_allowed: true
  per_image_attribute_preferences: [style, layout, panel_rhythm, information_density, content_detail_level, labels, color_semantics, callout_grammar, negative_reference]

text_image_turn_policy:
  first_reply_mode: STARTUP_PLAN_ONLY_TEXT_ONLY
  no_target_paper_image_generation_on_first_reply: true
  display_saved_atlas_on_first_reply_when_available: true
  markdown_image_embed_required_for_saved_atlas_display: true
  no_target_paper_image_generation_in_text_turn: true
  saved_package_images_allowed_in_text_turn: true
  concept_examples_required_for_abstract_decision_text_turns: true
  visual_structure_images_required_for_structure_text_turns: true
  prose_only_visual_structure_descriptions_allowed: false
  target_paper_images_embedded_in_text_turn_allowed: false
  text_turn_stops_before_target_paper_image_generation: true
  image_turn_has_no_prose_or_state: true
  user_must_confirm_after_text_prompt_before_target_paper_image_generation: true

next_prompt_policy:
  recommended_prompt_prefix: "请使用 **<当前skill名称>**，执行，根据当前状态，下一步执行："
  unknown_next_prompt: "请使用 **<当前skill名称>**，根据当前状态，提供下一步提问建议。"
  after_multi_option_text_first_prompt: "请使用 **<当前skill名称>**，执行，根据当前状态，下一步执行：生成 6 张方向差异尽量大的候选图/示意图供我比较选择。"
  after_p6_first_selection_prompt: "请使用 **<当前skill名称>**，执行，根据当前状态，下一步执行：进入 P6b，从最佳实践和论文局部细节出发，设置 6 个二轮优化变体方向。"
  after_p6b_setup_prompt: "请使用 **<当前skill名称>**，执行，根据当前状态，下一步执行：生成 6 张二轮论文局部优化变体图供我比较选择。"

release_tests:
  - startup_no_image
  - text_candidates_default_6
  - candidate_board_setup_after_text_candidates
  - image_only_diverse_first_round_candidate_board_generation
  - candidate_review_records_image_batch_and_selects_current_best
  - p6_does_not_go_directly_to_p7
  - p6b_best_practice_divergence_setup_after_first_selection
  - p6b_image_only_second_round_generation
  - p6c_records_second_round_batch_and_selects_final_direction
  - no_text_image_same_turn
  - rendering_route_chatgpt_create_image_codex_imagegen_first
  - subtype_style_atlas_manifest_present
  - startup_displays_saved_atlas_without_live_generation
  - startup_displays_saved_atlas_with_markdown_image_embeds
  - abstract_decision_text_turn_displays_reference_or_records_missing_asset
  - style_text_turn_uses_markdown_image_embed_when_asset_exists
  - plain_path_list_is_not_valid_atlas_display
  - required_non_target_concept_example_embedded_or_repair_recorded
  - visual_structure_text_turn_embeds_structure_image_or_records_repair
  - prose_only_visual_structure_description_fails
  - target_paper_candidate_or_final_image_not_embedded_in_text
  - inline_concept_example_does_not_satisfy_candidate_bridge_or_second_round
  - off_recommended_user_request_maps_to_original_workflow_step
  - text_reply_records_before_after_step_and_transition_reason
  - image_request_in_text_turn_maps_to_setup_not_live_generation
```
