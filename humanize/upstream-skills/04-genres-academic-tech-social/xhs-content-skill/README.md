<div align="center">

# 📕 XHS Content Skill

**让 AI Agent 写出能爆的小红书短图文**

不是把长文截一段，是真正按小红书的节奏、钩子、互动逻辑重新设计的生产规范。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skill: Claude Code](https://img.shields.io/badge/Skill-Claude%20Code-8A2BE2)](https://github.com/anthropics/claude-code)
[![Platform: 小红书](https://img.shields.io/badge/Platform-小红书-FF2741)]()
[![Stars](https://img.shields.io/github/stars/cool111111/xhs-content-skill?style=social)](https://github.com/cool111111/xhs-content-skill/stargazers)

</div>

> 让 AI 写小红书最常见的失败：长文逻辑塞进短文，开头铺垫一大段，看到第三行就划走。
> 这个 Skill 解决的是"小红书的节奏不一样"这件事。


## 为什么需要专门的小红书 Skill

公众号长文和小红书短图文是**完全不同的两种生物**：

| 维度 | 公众号长文 | 小红书短图文 |
|------|-----------|-------------|
| 字数 | 4000-8000 | 300-800 |
| 开头 | 叙事铺垫，慢慢进入 | **第一句就要炸**，3 秒决定划不划走 |
| 深度 | 层层剥开 | 聚焦一个点，**讲透就收**，别贪多 |
| 收尾 | 哲思余韵 | **留悬念**，绝不用"你觉得呢" |
| 钩子 | 内容自带钩子 | **标题 + 首句**双钩子，缺一不可 |

通用写作 Prompt 写出来的小红书几乎全是失败品 — 没钩子、没节奏、读起来像简化版长文。

## 核心特性

- 🎯 **选题优先级体系** — KOL 观点 > 开源项目破圈 > 产品发布 > 行业数据（基于实际数据迭代而来）
- 📊 **四维评分** — 钩子力 / 信息密度 / 传播性 / 互动潜力，每篇出稿前自带质量预测
- 🪝 **标题钩子库** — 数字冲击、信息差、争议性、反常识等公式化模板
- 🚫 **反 AI 味底座** — 继承 [Writer Skill](https://github.com/cool111111/writer-skill) 的反套话词库
- 🔁 **反馈迭代闭环** — 预测评分 vs 实际数据对比分析，持续校准选题判断

## Quick Start

```bash
# 1. 安装 Writer Skill 作为风格底座（必需）
git clone https://github.com/cool111111/writer-skill.git \
  ~/.your-agent/skills/writer

# 2. 安装本 Skill
git clone https://github.com/cool111111/xhs-content-skill.git \
  ~/.your-agent/skills/xhs-content
```

然后对 Agent 说："**帮我写 3 篇小红书，话题是 XXX**"，Agent 自动加载这个 Skill。

## 我自己怎么用的

这个 Skill 是我做 AI 内容运营时跑出来的真东西 — 配合一条多 Agent 自动化管线，**每天产出 3-5 条候选小红书帖子**，挑出最好的发出去。

整套管线长这样：

```
Twitter KOL × 3 ──┐
GitHub Trending ──┼──→ 日报汇总 ──→ 选题筛选 ──→ XHS Content Skill ──→ 推飞书审稿 ──→ 发布
AI 新闻 ─────────┘
```

每天 30 分钟全自动跑完，我只负责审稿 + 发布。

## 文件结构

```
xhs-content-skill/
└── SKILL.md   # 主 Skill 入口
```

简单到只有一个文件 — 因为风格底座复用了 Writer Skill 的 references。

## 配套 Skill

- 长文写作 → [Writer Skill](https://github.com/cool111111/writer-skill)
- 找达人 → [find-influencer-skill](https://github.com/cool111111/find-influencer-skill)

## License

MIT — 觉得有用就 **star 一下** ⭐
