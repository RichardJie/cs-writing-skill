# 自定义 PPT 风格方案

## 配置层级

本项目把 PPT 生成拆成五层：

| 层级 | 作用 | 示例 |
|---|---|---|
| scenario | 决定页面骨架 | thesis-defense, proposal, midterm |
| theme | 决定视觉风格 | thesis-defense-blue |
| layout | 决定单页信息结构 | technical-route, result-comparison |
| content rules | 决定文字密度和表达方式 | maxBulletsPerSlide: 5 |
| brand tokens | 决定学校和学院视觉 | logo, schoolColor, footer |

## 用户可配置字段

```json
{
  "scenario": "thesis-defense",
  "degree": "master",
  "discipline": "computer-science",
  "tone": "formal",
  "theme": "thesis-defense-blue",
  "durationMinutes": 15,
  "slideCount": 12,
  "language": "zh-CN",
  "schoolName": "某某大学",
  "collegeName": "计算机科学与技术学院",
  "schoolColor": "#1f4e79",
  "logo": "./assets/logo.png",
  "speakerNotes": true,
  "qaBackupSlides": true
}
```

## 场景映射

| 用户需求 | 推荐模板 | 推荐主题 |
|---|---|---|
| 硕士论文最终答辩 | thesis-defense | thesis-defense-blue |
| 本科毕设答辩 | thesis-defense | thesis-defense-minimal |
| 文科论文答辩 | thesis-defense | thesis-defense-serif |
| 开题报告 | thesis-defense | thesis-defense-blue |
| 党建/政策/管理主题 | thesis-defense | thesis-defense-red |

## 扩展新风格

新增一个风格通常需要：

1. 在 `assets/themes/` 增加主题 CSS。
2. 在 `templates/style-presets/` 增加或修改 JSON 配置。
3. 在 `references/themes.md` 说明适用场景。
4. 在 `SKILL.md` 增加推荐规则。

## 学校品牌定制

建议通过 CSS variables 接入学校视觉：

```css
:root {
  --accent: var(--school-color, #1f4e79);
}
```

在页面中保留校徽占位：

```html
<div class="cover-mark">校徽</div>
```

如果用户提供真实校徽，可以替换为：

```html
<img class="school-logo" src="./assets/logo.png" alt="学校校徽">
```
