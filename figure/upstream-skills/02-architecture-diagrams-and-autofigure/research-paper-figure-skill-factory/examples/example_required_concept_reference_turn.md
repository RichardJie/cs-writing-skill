# Example Required Concept Reference Text Turn - v2.0.5

This example is for P2/P3/P4/P7 or any text turn that explains an abstract visual decision. It must show a saved reference or non-target concept/modeling example image.

```markdown
## 当前执行计划

当前处于 P2：诊断目标论文图需求并比较 subtype。因为本轮要解释 subtype 和布局语法，必须展示一个参考/概念图帮助用户理解。

![Subtype concept reference](assets/subtype-atlas/boards/subtype-routing-concept-example.png)

## Subtype routing

- Option A: pipeline framework, best when the reader needs execution order.
- Option B: module architecture, best when the reader needs component relationships.
- Option C: mechanism intuition, best when the reader needs why the method works.

默认推荐 Option B，因为目标论文的主要理解障碍是模块关系，而不是时间顺序。

## 当前状态与产物

- **当前步骤:** P2
- **当前回复模式:** TEXT_ONLY
- **concept_example_required:** true
- **concept_example_status:** displayed_saved_reference
- **concept_example_role:** concept_example
- **concept_example_trigger_reason:** subtype
- **visual_structure_image_required:** true
- **visual_structure_image_status:** displayed_saved_reference
- **visual_structure_image_role:** concept_example
- **visual_structure_image_trigger_reason:** layout_skeleton
- **inline_reference_image_role:** concept_example
- **inline_reference_images_displayed:** [`![Subtype concept reference](assets/subtype-atlas/boards/subtype-routing-concept-example.png)`]
- **candidate_image_batch_id:** null
- **second_round_candidate_batch_id:** null
- **target_paper_images_embedded_in_text_turn:** false
- **target_paper_image_generation_in_current_turn:** false

## 下一步你可以这样问

1. `请使用 **<当前skill名称>**，执行，根据当前状态，下一步执行：继续 P3，给出 6 个文字候选方案。`
2. `请使用 **<当前skill名称>**，根据当前状态，提供下一步提问建议。`
```
