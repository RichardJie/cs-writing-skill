# Example Diverse First-Round Visual Candidate Board Round - v2.0.5

This example occurs after a generated specialized skill has presented 4-6 text candidates. The next step is not final prompt generation; it is diverse first-round candidate-board setup.

## P4 TEXT_ONLY Candidate-Board Setup

```markdown
## 当前执行计划

- 当前处于 P4：第一轮视觉候选图板设置（TEXT_ONLY）
- 上一步 P3 已给出 6 个文字候选方案
- 本步目标：设置 6 张方向差异尽量大的候选图/示意图生成规则

![Layout grammar board](assets/subtype-atlas/boards/visual-grammar-layout.png)

## 默认推荐

生成 6 张第一轮候选图。固定论文 thesis、核心模块和必要标签，广泛变化 subtype、布局骨架、metaphor、密度和 panel rhythm，让用户先看图搭方向，而不是只靠文字定稿。

### Candidate-board brief

- board type: layout / scheme / metaphor / density
- candidate count: 6
- varied axis: broad direction-level diversity across layout skeleton, metaphor, density, and panel rhythm
- fixed elements: figure thesis, required modules, exact labels, sample-image hard constraints
- rendering route: ChatGPT web Create image / ChatGPT Images 2.0; Codex `$imagegen` first; fallback ChatGPT Images 2.0 API or approved image API
- compare: reading clarity, contribution prominence, label readability, paper-slot fit

## 当前状态与产物

- **阶段:** Figure Production
- **当前步骤:** P4
- **当前回复模式:** TEXT_ONLY
- **全部步骤与当前位置:** P1(TEXT_ONLY) -> P2(TEXT_ONLY) -> P3(TEXT_ONLY) -> P4(TEXT_ONLY diverse first-round setup) [当前位置] -> P5(IMAGE_ONLY diverse first-round generation) -> P6(TEXT_ONLY first-round review/current-best selection) -> P6b(TEXT_ONLY paper-local best-practice setup) -> P6b-IMAGE(IMAGE_ONLY second-round variants) -> P6c(TEXT_ONLY final direction lock) -> P7(TEXT_ONLY final image brief) -> P8(IMAGE_ONLY formal generation) -> P9(TEXT_ONLY review/final text)
- **text_candidate_count:** 6
- **image_candidate_count:** 6
- **visual_candidate_board_status:** setup_ready
- **first_round_diversity_goal:** direction_level_diversity
- **first_round_varied_axes:** [layout_skeleton, metaphor, density, panel_rhythm]
- **candidate_image_batch_id:** not_created
- **concept_example_required:** true
- **concept_example_status:** displayed_saved_reference
- **concept_example_role:** saved_atlas
- **concept_example_trigger_reason:** layout_grammar
- **visual_structure_image_required:** true
- **visual_structure_image_status:** displayed_saved_reference
- **visual_structure_image_role:** saved_atlas
- **visual_structure_image_trigger_reason:** layout_skeleton
- **saved_reference_markdown_embeds_rendered:** [`![Layout grammar board](assets/subtype-atlas/boards/visual-grammar-layout.png)`]
- **target_paper_images_embedded_in_text_turn:** false
- **本轮新增产物:** candidate-board brief
- **待产物:** P5 IMAGE_ONLY diverse first-round candidate image board

## 下一步你可以这样问
1. `请使用 **<当前skill名称>**，执行，根据当前状态，下一步执行：生成 6 张方向差异尽量大的候选图/示意图供我比较选择。`
2. `请使用 **<当前skill名称>**，根据当前状态，提供下一步提问建议。`
```

## P5 IMAGE_ONLY Candidate Board

P5 must contain only first-round image generation/display. No prose, no state footer, no captions.

## P6 TEXT_ONLY First-Round Candidate Review

The next text turn after P5 must record the image batch, compare candidates, recommend the current best first-round direction, and then trigger P6b. It must not proceed directly to P7.
