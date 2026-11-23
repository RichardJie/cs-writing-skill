# Session State Schema

Version: 2.0.5

Use this schema conceptually. The state does not need to be emitted as JSON, but every text reply must preserve these fields in the required current-status/current-output footer.

```yaml
skill: research-paper-figure-skill-factory
version: 2.0.5
mode: TEXT_ONLY | IMAGE_ONLY
current_step:
  code: S0 # S0 | B1-B9 | P1-P6 | P6b | P6b-IMAGE | P6c | P7-P9
  layer: startup | skill_builder | figure_production
  response_mode: TEXT_ONLY | IMAGE_ONLY | STARTUP_PLAN_ONLY_TEXT_ONLY
  user_request_interpreted_action: null
  workflow_step_before_user_request: null
  workflow_step_after_user_request: null
  state_transition_reason: null
  off_recommended_prompt_handling: not_needed | handled_and_mapped | blocked_missing_prerequisites | mapped_to_text_setup_before_image_only
  prerequisites_inferred_or_missing: []
all_steps_and_current_position: ""

builder_layer:
  target_figure_class: null
  target_skill_slug: null
  builder_time_acquisition:
    required: true
    status: not_started | planning | searching | downloading | extracting | completed | blocked | user_supplied_evidence
    local_corpus_root: null
    retrieval_manifest_json: null
    evidence_map_json: null
  local_corpus:
    processing_scope: all_accessible_relevant_pdfs | chunked_resumable | user_approved_pilot_sample | resource_limited_sample | metadata_or_caption_fallback
    candidate_pdf_count: 0
    accessible_pdf_count: 0
    processed_pdf_count: 0
    skipped_pdf_count: 0
    skipped_reasons: []
    ready_for_extraction: false
  extracted_evidence:
    status: not_started | extracting | extracted | partial | caption_only | metadata_only | blocked
    ready_for_taxonomy: false
    evidence_map_json: null
    multi_label_records_count: 0
  evidence_sufficiency:
    level: not_assessed | full_taxonomy | thin_taxonomy | pilot_taxonomy | fallback_taxonomy
  subtype_style_atlas:
    subtype_atlas_status: not_started | planned | generating | generated | packaged | displayed | repair_needed | missing
    subtype_atlas_manifest_path: null
    subtype_atlas_boards: []
    saved_reference_markdown_embeds_rendered: []
    reference_display_render_status: none | rendered | attempted_host_blocked | missing_recorded
    style_atlas_status: not_started | planned | generating | generated | packaged | displayed | repair_needed | missing
    style_atlas_manifest_path: null
    classification_angles: []
    missing_reference_images: []
  generated_skill:
    status: not_started | generated | tested | patched | locked
    slug: null
    version: null
    package_path: null
    lock_grade: none | production_grade | limited | pilot | fallback
    known_limitations: []
    test_results:
      startup_gate: not_started | passed | failed
      state_footer: not_started | passed | failed
      candidate_image_bridge: not_started | passed | failed
      rendering_boundary: not_started | passed | failed
      target_paper_image_isolation: not_started | passed | failed
      required_concept_example_display: not_started | passed | failed
      visual_structure_as_image_display: not_started | passed | failed
      best_practice_second_round: not_started | passed | failed
      inline_non_target_reference_display: not_started | passed | failed
      subtype_style_atlas: not_started | passed | failed
      saved_reference_display: not_started | passed | failed
      off_recommended_prompt_state_mapping: not_started | passed | failed

production_layer:
  active_specialized_skill:
    slug: null
    version: null
    limitations: []
  material_status: not_provided | partial | sufficient
  sample_reference_images:
    status: none | requested | provided | analyzed
    images: []
  text_candidate_count: 0
  image_candidate_count: 0
  candidate_generation_mode: none | multi_scheme_multi_image | single_scheme_multi_image
  candidate_scheme_ids: []
  candidate_comparison_focus: null
  visual_candidate_board_status: not_started | setup_ready | confirmed | generated | reviewed | skipped_by_user
  visual_board_type: subtype | scheme | layout | style | metaphor | density | prompt | final_candidate | null
  visual_board_axis_varied: null
  visual_board_fixed_elements: []
  candidate_image_batch_id: null
  visual_candidate_history: []
  selected_visual_candidate: null
  visual_candidate_board_skipped_by_user: false
  first_round_diversity_goal: direction_level_diversity | not_applicable
  first_round_varied_axes: []
  best_practice_divergence_status: not_started | required_after_first_selection | setup_ready | generated | reviewed | final_locked | overridden_by_user
  best_practice_divergence_axes: []
  best_practice_fixed_elements_from_first_round: []
  best_practice_local_details_to_vary: []
  second_round_candidate_batch_id: null
  second_round_candidate_history: []
  selected_second_round_candidate: null
  saved_reference_images_displayed: []
  saved_reference_markdown_embeds_rendered: []
  missing_reference_images: []
  reference_display_mode: none | startup_atlas | relevant_subtype | relevant_layout | relevant_style | concept_example | missing_recorded
  reference_display_render_status: none | rendered | attempted_host_blocked | missing_recorded
  inline_reference_image_role: none | saved_atlas | non_target_reference | concept_example
  inline_reference_images_displayed: []
  concept_example_required: false
  concept_example_status: not_needed | displayed_saved_reference | generated_inline | generation_pending | missing_recorded
  concept_example_role: none | saved_atlas | non_target_reference | concept_example
  concept_example_trigger_reason: null
  visual_structure_image_required: false
  visual_structure_image_status: not_needed | displayed_saved_reference | generated_inline | generation_pending | missing_recorded
  visual_structure_image_role: none | saved_atlas | non_target_reference | concept_example
  visual_structure_image_trigger_reason: null
  target_paper_images_embedded_in_text_turn: false
  target_paper_image_generation_in_current_turn: false
  live_image_generation_in_current_turn: false
  user_request_interpreted_action: null
  workflow_step_before_user_request: null
  workflow_step_after_user_request: null
  state_transition_reason: null
  off_recommended_prompt_handling: not_needed | handled_and_mapped | blocked_missing_prerequisites | mapped_to_text_setup_before_image_only
  prerequisites_inferred_or_missing: []

deliverables:
  current_turn_outputs: []
  cumulative_outputs: []
  output_paths_or_ids: []
  pending_outputs: []
  previous_image_only_outputs_recorded: not_applicable | recorded | pending_record

navigation:
  recommended_prompt_prefix: "Use the exact Chinese prefix from SKILL.md."
  unknown_next_prompt: "Use the exact Chinese fallback prompt from SKILL.md."
  after_multi_option_text_first_prompt: "Ask to generate/display 6 diverse first-round candidate images or schematic candidates."
  after_p6_first_selection_first_prompt: "Ask to set up P6b best-practice paper-local optimization axes before P7."
  after_p6b_setup_first_prompt: "Ask to generate/display 6 second-round paper-local variant images."
  state_source_default: active_session_history
```
