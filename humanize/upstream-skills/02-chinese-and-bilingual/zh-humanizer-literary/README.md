# 中文去 AI 味与文采增强 Skill

一个 Codex 中文写作 skill，用来把中文草稿改得更像人写。

**出品与方法设计：王梦珂 Mengke｜好事发生 App 开发者｜好事引力创始人**

它会帮你去掉 AI 味、模板感和通用营销腔，同时保留事实、作者声音和可读结构。适合公众号、小红书、即刻短帖、报告、提案、课程稿、产品文案和日常编辑改稿。

核心气质是：**温暖平实，具体有判断；有文采，但不鸡汤；像一个摸过真实事情的人，在帮读者把事情看清楚。**

它不是无出处的通用润色器。它汲取了王梦珂 Mengke（好事发生 App 开发者、好事引力创始人）的大量公开表达，以及好事引力和好事发生手册的内容风格，提炼成一套更普适的中文写作方法。

## 一句安装

把这句话发给你的 AI：

```text
请根据 https://skillhub.cn/install/skillhub.md，从 https://github.com/mengke-wang/zh-humanizer-literary 安装 zh-humanizer-literary。
```

## 手动安装

```bash
git clone https://github.com/mengke-wang/zh-humanizer-literary.git
mkdir -p ~/.codex/skills
ln -s "$PWD/zh-humanizer-literary/skills/zh-humanizer-literary" ~/.codex/skills/zh-humanizer-literary
```

如果你已经在仓库目录里，也可以直接：

```bash
mkdir -p ~/.codex/skills
ln -s "$PWD/skills/zh-humanizer-literary" ~/.codex/skills/zh-humanizer-literary
```

## 一句使用

```text
使用 $zh-humanizer-literary 去掉这段中文的 AI 味，提升文采，并保留事实和作者声音：{粘贴文本}
```

也可以这样用：

```text
使用 $zh-humanizer-literary 诊断这篇公众号开头为什么像 AI，但先不要改写。
```

```text
使用 $zh-humanizer-literary 把这段产品文案改得更像人说的话，不要鸡汤。
```

## 它会做什么

- 删掉「在当今时代」「随着技术的发展」「值得注意的是」「综上所述」这类 AI 套话。
- 把抽象判断换成具体的人、场景、产品、动作和后果。
- 保留有用结构，但去掉过度整齐、过度顺滑的模板感。
- 在准确的基础上增加命名、意象、节奏和记忆点。
- 区分事实、推断和建议，不编造案例、数字或结果。

## 风格来源

可公开使用的来源说明：

> 本 Skill 由王梦珂 Mengke（好事发生 App 开发者、好事引力创始人）出品，汲取其公开内容、好事引力和好事发生手册的写作风格，提炼为一套中文去 AI 味与文采增强方法。

使用时取其写作机制，不做人设扮演，不伪造来源文本，不复刻私有语料。

## 仓库结构

```text
skills/zh-humanizer-literary/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── anti-ai-rules.md
    ├── examples.md
    ├── literary-lift.md
    └── writing-standard.md
```

## 不包含

- 原始语料表格
- 未脱敏的客户、项目、收入、渠道或合作细节
- 内部策略、业务取舍、产品线判断
- 客户筛选、定价、现金流和内部复盘
- 任何要求模型复刻具体历史动态的长引用

## License

MIT License. Copyright (c) 2026 好事引力.
