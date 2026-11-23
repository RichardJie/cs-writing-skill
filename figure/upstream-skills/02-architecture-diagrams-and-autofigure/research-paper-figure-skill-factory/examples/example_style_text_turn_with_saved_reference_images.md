# Example Style Text Turn With Required Saved Reference Images - v2.0.5

This example shows a generated specialized skill discussing style in `TEXT_ONLY` while displaying already-saved atlas images. It does not perform target-paper image generation. In Codex, replace package-relative paths with absolute filesystem paths before emitting the image tags.

```markdown
## 当前执行计划

当前处于 P3/P4 之间：已提出文本方案，正在准备风格/布局视觉候选板。本轮只说明风格选择并展示已保存参考图，不生成目标论文候选图。

## 风格选择

我建议先比较 6 个视觉传达风格方向：formal architecture schematic、clean editorial flat、minimal line-art schematic、premium scientific illustration、isometric soft 3D、mini-evidence infographic。

相关已保存风格图：

![Style board](assets/subtype-atlas/boards/style-overview.png)
![Layout grammar board](assets/subtype-atlas/boards/visual-grammar-layout.png)

## 默认推荐

默认选择 formal architecture schematic，因为它适合方法框架图，能保留模块、数据流和创新点位置。下一步不要只从文字里定风格；建议生成 6 张候选图/示意图比较。

## 当前状态与产物

- 当前步骤：P4
- 当前回复模式：TEXT_ONLY
- saved_reference_images_displayed:
  - assets/subtype-atlas/boards/style-overview.png
  - assets/subtype-atlas/boards/visual-grammar-layout.png
- saved_reference_markdown_embeds_rendered:
  - `![Style board](assets/subtype-atlas/boards/style-overview.png)`
  - `![Layout grammar board](assets/subtype-atlas/boards/visual-grammar-layout.png)`
- reference_display_render_status: rendered
- concept_example_required: true
- concept_example_status: displayed_saved_reference
- concept_example_role: saved_atlas
- concept_example_trigger_reason: visual_style
- missing_reference_images: []
- live_image_generation_in_current_turn: false
- target_paper_image_generation_in_current_turn: false

## 下一步你可以这样问

1. `请使用**<当前skill名称>**，执行，根据当前状态，下一步执行：生成 6 张候选图/示意图供我比较选择。`
2. `请使用**<当前skill名称>**，根据当前状态，提供下一步提问建议。`
```
