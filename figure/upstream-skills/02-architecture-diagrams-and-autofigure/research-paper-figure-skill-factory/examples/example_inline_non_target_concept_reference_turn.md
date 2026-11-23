# Example Required Inline Non-Target Concept Reference Turn - v2.0.5

This example shows a generated specialized skill embedding an explanatory concept/modeling image inside a `TEXT_ONLY` reply because an abstract-decision trigger is active. The image is not based on the user's target paper, is not a candidate board, and does not satisfy P5/P6b-IMAGE/P8.

```markdown
## 当前执行计划

当前先解释“层级管线式 framework 图”的建模方式：输入、核心模块、监督信号和输出结果分别占据固定层级。下面这张图只是概念示例，不是你的论文候选图。

![Non-target concept example](assets/subtype-atlas/boards/non-target-pipeline-concept-example.png)

## 默认推荐

继续进入 P4，设置目标论文的 6 张候选图生成参数；下一轮 P5 必须是 `IMAGE_ONLY`。

## 当前状态与产物

- 当前回复模式: TEXT_ONLY
- inline_reference_image_role: concept_example
- concept_example_required: true
- concept_example_status: displayed_saved_reference
- concept_example_role: concept_example
- concept_example_trigger_reason: modeling_pattern
- inline_reference_images_displayed:
  - `![Non-target concept example](assets/subtype-atlas/boards/non-target-pipeline-concept-example.png)`
- target_paper_images_embedded_in_text_turn: false
- target_paper_image_generation_in_current_turn: false
- candidate_image_batch_id: null
- second_round_candidate_batch_id: null
- visual_candidate_board_status: setup_ready
- 说明: 上方图片仅用于解释建模方式，不是目标论文候选图，不可作为方向锁定依据。
```
