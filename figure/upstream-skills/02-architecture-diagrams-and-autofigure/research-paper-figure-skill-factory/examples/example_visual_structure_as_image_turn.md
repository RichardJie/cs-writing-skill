# Example Visual-Structure-As-Image Text Turn - v2.0.5

This example shows a generated specialized skill explaining a layout skeleton without relying on prose-only structure description. The embedded image is a non-target reference. It is not a target-paper candidate, not a second-round variant, and does not satisfy P5/P6b-IMAGE/P8.

## Current Plan

Current step: P4 `TEXT_ONLY`. Set up the first-round board and show the layout grammar with a generic structure image before any target-paper image generation.

## Structure Reference

The first round will compare broad direction choices. The target-paper thesis and required labels stay fixed; the candidate images will vary layout grammar, panel rhythm, metaphor, density, and style family.

![Generic layout skeleton reference](assets/subtype-atlas/boards/visual-grammar-layout.png)

This image is a generic layout/reference board. It does not contain target-paper modules or paper-specific claims.

## Board Setup

- candidate count: 6
- first-round purpose: direction-level diversity
- fixed elements: target paper thesis, target slot, required module names, sample-image hard constraints
- varied axes: subtype, layout grammar, metaphor, density, panel rhythm, style family
- next mode: P5 `IMAGE_ONLY`

## State

- **current_step:** P4
- **concept_example_required:** true
- **concept_example_status:** displayed_saved_reference
- **concept_example_role:** saved_atlas
- **concept_example_trigger_reason:** layout_grammar
- **visual_structure_image_required:** true
- **visual_structure_image_status:** displayed_saved_reference
- **visual_structure_image_role:** saved_atlas
- **visual_structure_image_trigger_reason:** layout_skeleton
- **candidate_image_batch_id:** null
- **second_round_candidate_batch_id:** null
- **target_paper_images_embedded_in_text_turn:** false

## Next Prompt

`请使用 **<当前skill名称>**，执行，根据当前状态，下一步执行：生成 6 张方向差异尽量大的第一轮目标论文候选图，供我比较选择。`
