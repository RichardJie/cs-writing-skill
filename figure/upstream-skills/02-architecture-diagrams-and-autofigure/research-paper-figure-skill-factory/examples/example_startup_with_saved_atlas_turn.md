# Example Startup With Saved Atlas Turn - v2.0.5

This example is for a generated specialized figure-making skill, not the factory itself.

The first reply remains `STARTUP_PLAN_ONLY (TEXT_ONLY)`: it shows the workflow and saved atlas boards already packaged in the skill. It does not analyze the target paper and does not call Create image, `$imagegen`, or an image API. In Codex, replace package-relative paths with absolute filesystem paths before emitting the image tags.

```markdown
## 当前执行计划

当前处于 S0/P1 startup. 本轮只展示启动计划、已保存的子类型/风格示意图谱和下一步提问建议；不分析目标论文，不生成新图。

## 已保存子类型/风格示意图谱

![Subtype overview](assets/subtype-atlas/boards/subtype-overview.png)
![Visual communication style board](assets/subtype-atlas/boards/style-overview.png)

## 默认推荐

先进入材料 intake 和图类型路由；如果后续涉及风格/布局选择，我会继续贴出相关已保存示意图，并建议生成 6 张候选图供比较。

## 当前状态与产物

- 当前步骤：S0/P1
- 当前回复模式：STARTUP_PLAN_ONLY (TEXT_ONLY)
- saved_reference_images_displayed:
  - assets/subtype-atlas/boards/subtype-overview.png
  - assets/subtype-atlas/boards/style-overview.png
- saved_reference_markdown_embeds_rendered:
  - `![Subtype overview](assets/subtype-atlas/boards/subtype-overview.png)`
  - `![Visual communication style board](assets/subtype-atlas/boards/style-overview.png)`
- reference_display_render_status: rendered
- live_image_generation_in_current_turn: false
- target_paper_image_generation_in_current_turn: false

## 下一步你可以这样问

1. `请使用**<当前skill名称>**，执行，根据当前状态，下一步执行：读取我的论文材料并进行图类型路由。`
2. `请使用**<当前skill名称>**，根据当前状态，提供下一步提问建议。`
```
