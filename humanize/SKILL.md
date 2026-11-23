---
name: humanize
description: "Remove AI voice from prose. Invoke with :chinese for Chinese de-AI-ing (7-step surgery, Chinese patterns) or :english for humanize/English rewrite (pattern catalog, direct-statement rules, em-dash ban). Triggers: humanize, remove AI tells, make it sound natural."
---

# Humanize — Remove AI Voice

One installable skill, two language tracks. **Read the matching file in full before rewriting.**

| Invocation | Read | Use when |
|------------|------|----------|
| `:chinese` or Chinese input | [chinese.md](chinese.md) | Chinese prose, WeChat posts, CN blogs, CN academic polish (not paper-boundaries scope) |
| `:english` or English input / humanize | [english.md](english.md) | English prose, READMEs, essays, LinkedIn, technical docs |
| `:paper-boundaries` | [paper-boundaries.md](paper-boundaries.md) | CS paper narrative boundaries (`发布会原则` / press-conference principle, no self-undermining) |

## Router

1. **Explicit tag wins.** `:chinese` → `chinese.md`; `:english` → `english.md`; `:paper-boundaries` → `paper-boundaries.md`.
2. **No tag:** infer from the text language. Mixed or unclear → ask once, default `:english`.
3. **Embedded mode** (another task calls humanize as a step): run the loop internally; output only the final rewrite unless the user asked for diagnosis.

## Shared guardrails (both tracks)

- **Preserve facts.** No new names, numbers, dates, quotes, or citations. Opinions and stance are voice, not facts.
- **Preserve information, not shape.** Compress dull parts; vary paragraph length; merge or split freely. Information beats mirroring structure.
- **Flag clusters, not isolated tells.** One em dash or one "crucial" is human; stacks of tells are not.
- **Do not rewrite** quoted speech, titles, code, frontmatter, or examples *about* AI patterns.
- **Voice calibration:** if the user supplies a writing sample, match its habits (including punctuation) over these rules.
- **Register match:** encyclopedic, legal, and reference text stay neutral; blog/opinion pieces get personality when appropriate.
- **Do not over-edit.** Specific, messy, dated human detail → leave it alone.

## Output modes

| Mode | Deliver |
|------|---------|
| **Pasted text (default)** | Brief diagnosis bullets → final rewrite → short change summary |
| **File** | Rewrite in place; leave code blocks and frontmatter untouched; summarize changes in chat |
| **Embedded** | Final text only |

## Examples

**`:chinese`** — Input: typical AI Chinese boilerplate (summarize-and-challenges opener).  
→ Apply [chinese.md](chinese.md) 7-step surgery; cut stock transitions and opportunity-challenge cliches; add concrete scene.

**`:english`** — Input: "Additionally, this pivotal initiative underscores our commitment to fostering innovation in today's evolving landscape."  
→ Apply [english.md](english.md); kill AI vocabulary; ban em dashes; state what the initiative *is*.

## Related skills

- **`paper-boundaries`** ([paper-boundaries.md](paper-boundaries.md)) — CS paper *narrative boundaries* (press-conference principle, no self-undermining). Does not strip AI voice; pair with `:english` or `:chinese` on finished prose.
- **`plain`** — Explain hard ideas clearly; orthogonal to de-slopping.

---

## 全网开源去 AI 味 Skill 与实测资料分类索引

本节仅作为全网真实开源去 AI 味 `SKILL.md` 仓库（共 **74** 个去重上游仓库，位于 `upstream-skills/`）与已发表文献/社区实测资料汇编（位于 `curated-guides/`）的分类路由索引；所有上游 Commit SHA、开源协议与外部链接溯源清单统一见 [curated-guides/SOURCES_CATALOG.md](curated-guides/SOURCES_CATALOG.md)。

### 0. 文献与实测资料总目录 (`curated-guides/`)

| 资料汇编文件 | 收录范围与原始来源 |
|:---|:---|
| [curated-guides/SOURCES_CATALOG.md](curated-guides/SOURCES_CATALOG.md) | 74 个开源 GitHub/Gist 仓库（精确 Commit SHA + License）及全部论文 DOI、官方文档与社区实测链接总表 |
| [curated-guides/wikipedia-signs-of-ai-writing.md](curated-guides/wikipedia-signs-of-ai-writing.md) | Wikipedia `WikiProject AI Cleanup` 官方指南（主条目 + `/Style` + `/Markup` 子页，CC BY-SA 4.0 原文归档） |
| [curated-guides/published-stylometry-and-classics.md](curated-guides/published-stylometry-and-classics.md) | Kobak 等 (*Science Advances* 2025)、Liang 等 (ICML 2024 & *Nature Human Behaviour* 2025)、Gray (2024)、Juzek & Ward (COLING 2025) 实证词频表，以及 George Orwell、Paul Graham 经典散文规范 |
| [curated-guides/by-language-chinese-community.md](curated-guides/by-language-chinese-community.md) | 余光中、王力、朱光潜、谢益辉反翻译腔经典文献，W3C `clreq` 标点规范，以及中文社区原版去 AI 味 Prompt 与评测汇编 |
| [curated-guides/by-model-tells-and-prompts.md](curated-guides/by-model-tells-and-prompts.md) | 跨模型指纹实证（ICML 2025 / EQ-Bench / Graphite Research）及 GPT、Claude、Gemini、DeepSeek、Qwen、Kimi、豆包分模型口癖与原版反制 Prompt |
| [curated-guides/by-genre-academic-tech-social.md](curated-guides/by-genre-academic-tech-social.md) | 学术论文、审稿回复（Rebuttal）、技术文档/博客/README、公众号/小红书/LinkedIn 及冷启动邮件学者与从业者指南 |
| [curated-guides/by-visual-image-figure-ui.md](curated-guides/by-visual-image-figure-ui.md) | Midjourney / FLUX / Stable Diffusion 官方写实参数与社区去塑料感实测、期刊 AI 配图政策、前端 UI 反 AI 模板化资料 |

---

### 1. 按语言分类：中英文与双语 (`01-english-and-universal/` · `02-chinese-and-bilingual/`)

| 细分方向 | 本仓核心文件与资料汇编 | 完整收录的上游开源 Skill / 规范仓库 |
|:---|:---|:---|
| **英文通用去 AI 味（纯规则 / `SKILL.md`）** | [english.md](english.md) · [wikipedia-signs-of-ai-writing.md](curated-guides/wikipedia-signs-of-ai-writing.md) · [published-stylometry-and-classics.md](curated-guides/published-stylometry-and-classics.md) | [blader/humanizer](upstream-skills/01-english-and-universal/humanizer/SKILL.md) · [hardikpandya/stop-slop](upstream-skills/01-english-and-universal/stop-slop/SKILL.md) · [Anbeeld/WRITING.md](upstream-skills/01-english-and-universal/WRITING.md/README.md) · [petergyang/no-ai-slop](upstream-skills/01-english-and-universal/no-ai-slop/README.md) · [Nanako0129/sepia](upstream-skills/01-english-and-universal/sepia/README.md) · [Dodaios/ste80-humanizer](upstream-skills/01-english-and-universal/ste80-humanizer/SKILL.md) · [gabelul/slopbuster](upstream-skills/01-english-and-universal/slopbuster/SKILL.md) · [nonatofabio/claude-writing-skills](upstream-skills/01-english-and-universal/claude-writing-skills/README.md) · [hannsxpeter/humanizer](upstream-skills/01-english-and-universal/hannsxpeter-humanizer/SKILL.md) |
| **英文检测器、Vale / `.mdc` 规则与评分脚本** | [wikipedia-signs-of-ai-writing.md](curated-guides/wikipedia-signs-of-ai-writing.md) | [conorbronsdon/avoid-ai-writing](upstream-skills/01-english-and-universal/avoid-ai-writing/SKILL.md) · [seyedehsanhadi/sloptrim](upstream-skills/01-english-and-universal/sloptrim/SKILL.md) · [Aboudjem/humanizer-skill](upstream-skills/01-english-and-universal/humanizer-skill/README.md) · [ehmo/slopkit](upstream-skills/01-english-and-universal/slopkit/README.md) · [forjd/better-writing](upstream-skills/01-english-and-universal/better-writing/README.md) · [199-biotechnologies/humanise-text-skill](upstream-skills/01-english-and-universal/humanise-text-skill/SKILL.md) · [bnivanov/omp-writing-skills](upstream-skills/01-english-and-universal/omp-writing-skills/README.md) |
| **简体中文通用去 AI 味与活人感改稿** | [chinese.md](chinese.md) · [by-language-chinese-community.md](curated-guides/by-language-chinese-community.md) | [op7418/Humanizer-zh](upstream-skills/02-chinese-and-bilingual/Humanizer-zh/SKILL.md) · [KKKKhazix/khazix-skills](upstream-skills/02-chinese-and-bilingual/khazix-skills/README.md) · [KKKKhazix/human-writing](upstream-skills/02-chinese-and-bilingual/human-writing/README.md) · [MrGeDiao/shuorenhua](upstream-skills/02-chinese-and-bilingual/shuorenhua/README.md) · [hylarucoder/ai-flavor-remover](upstream-skills/02-chinese-and-bilingual/ai-flavor-remover/README.md) · [orange2ai/renwei-writing](upstream-skills/02-chinese-and-bilingual/renwei-writing/SKILL.md) · [OUBIGFA/De-AI-Prompt-Enhancer](upstream-skills/02-chinese-and-bilingual/De-AI-Prompt-Enhancer-Writer-Booster-SKILL/README.md) · [LifelongLazyLearner/qu-ai-wei](upstream-skills/02-chinese-and-bilingual/qu-ai-wei/SKILL.md) · [Hyacehila/humanizer-zh-next](upstream-skills/02-chinese-and-bilingual/humanizer-zh-next/SKILL.md) · [ai-zixun/humanizer-zh](upstream-skills/02-chinese-and-bilingual/ai-zixun-humanizer-zh/SKILL.md) · [mengke-wang/zh-humanizer-literary](upstream-skills/02-chinese-and-bilingual/zh-humanizer-literary/README.md) · [taxueseek/plainspoken-writing](upstream-skills/02-chinese-and-bilingual/plainspoken-writing/README.md) · [hellogit2021/avoid-ai-writing-cn](upstream-skills/02-chinese-and-bilingual/avoid-ai-writing-cn/README.md) · [Liam0205/skills](upstream-skills/02-chinese-and-bilingual/Liam0205-skills/README.md) |
| **繁體中文（台灣/港澳）去 AI 味** | [by-language-chinese-community.md](curated-guides/by-language-chinese-community.md) | [Raymondhou0917/speak-human-tw](upstream-skills/02-chinese-and-bilingual/speak-human-tw/SKILL.md) · [WenyuChiou/academic-writing-skills](upstream-skills/04-genres-academic-tech-social/academic-writing-skills/README.md) |
| **中英混排、技术文案规范与正式双语语域** | [by-language-chinese-community.md](curated-guides/by-language-chinese-community.md) | [sparanoid/chinese-copywriting-guidelines](upstream-skills/02-chinese-and-bilingual/chinese-copywriting-guidelines/README.md) · [ruanyf/document-style-guide](upstream-skills/02-chinese-and-bilingual/document-style-guide/README.md) · [jiutianxvanyin/humanizer-formal](upstream-skills/02-chinese-and-bilingual/humanizer-formal/SKILL.md) · [dengzhe-hou/research-writing-prompts](upstream-skills/04-genres-academic-tech-social/research-writing-prompts/README.md) |

---

### 2. 按 AI 模型分类：跨模型计量数据与分模型反制 (`03-models-and-stylometry-data/`)

| 模型 / 研究类别 | 实证文献与社区资料汇编 | 上游开源词表、语料研究与反制 Skill 仓库 |
|:---|:---|:---|
| **跨模型词汇超额分布与 Slop 计量数据集** | [published-stylometry-and-classics.md](curated-guides/published-stylometry-and-classics.md) · [by-model-tells-and-prompts.md](curated-guides/by-model-tells-and-prompts.md)（Part I：ICML 2025 `arXiv:2502.12150`、EQ-Bench 23 模型榜单、Graphite Research 10 模型对照） | [sam-paech/slop-forensics](upstream-skills/03-models-and-stylometry-data/slop-forensics/README.md) · [sam-paech/antislop-sampler](upstream-skills/03-models-and-stylometry-data/antislop-sampler/README.md) · [berenslab/llm-excess-vocab](upstream-skills/03-models-and-stylometry-data/berenslab-llm-excess-vocab/README.md) · [Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers](upstream-skills/03-models-and-stylometry-data/Weixin-Liang-Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers/readme.md) · [tjuzek/delve](upstream-skills/03-models-and-stylometry-data/tjuzek-delve/README.md) · [larashero3-dotcom/lieflat-less-ai-tone](upstream-skills/03-models-and-stylometry-data/lieflat-less-ai-tone/SKILL.md) |
| **OpenAI（GPT-3.5 / GPT-4o / o3 / GPT-5+）** | [by-model-tells-and-prompts.md](curated-guides/by-model-tells-and-prompts.md)（Part II：ChatGPT Custom Instructions、Sabrina Ramonov、Ruben Hassid） | [haidrrrry/humanize-ai-writing](upstream-skills/03-models-and-stylometry-data/haidrrrry-humanize-ai-writing/README.md) · [sam-paech/antislop-sampler](upstream-skills/03-models-and-stylometry-data/antislop-sampler/README.md) |
| **Anthropic（Claude 3.5 Sonnet → Opus 5.5）** | [by-model-tells-and-prompts.md](curated-guides/by-model-tells-and-prompts.md)（Part III：`claudisms.ai` CC0 词表、Graphite Opus 5.5 更新、`tropes.fyi`） | [ossa-ma/writing-whip](upstream-skills/03-models-and-stylometry-data/ossa-ma-writing-whip/writing-whip-SKILL.md) · [MrGeDiao/shuorenhua](upstream-skills/02-chinese-and-bilingual/shuorenhua/README.md) |
| **Google（Gemini 1.5 Pro → 2.5 Pro / 3.1 Pro & Gemma）** | [by-model-tells-and-prompts.md](curated-guides/by-model-tells-and-prompts.md)（Part IV）· [wikipedia-signs-of-ai-writing.md](curated-guides/wikipedia-signs-of-ai-writing.md)（Gemini `WP:STARTSPAN` 标记特征） | [hylarucoder/ai-flavor-remover](upstream-skills/02-chinese-and-bilingual/ai-flavor-remover/README.md) · [larashero3-dotcom/lieflat-less-ai-tone](upstream-skills/03-models-and-stylometry-data/lieflat-less-ai-tone/SKILL.md) |
| **国产模型（DeepSeek / Qwen 通义千问 / Kimi / 豆包）** | [by-model-tells-and-prompts.md](curated-guides/by-model-tells-and-prompts.md)（Part V：DeepSeek 物理/文学口癖词、豆包体密集“最”字、88 万篇语料与多模型横评） | [larashero3-dotcom/lieflat-less-ai-tone](upstream-skills/03-models-and-stylometry-data/lieflat-less-ai-tone/SKILL.md) · [LifelongLazyLearner/qu-ai-wei](upstream-skills/02-chinese-and-bilingual/qu-ai-wei/SKILL.md) · [hellogit2021/avoid-ai-writing-cn](upstream-skills/02-chinese-and-bilingual/avoid-ai-writing-cn/README.md) · [MrGeDiao/shuorenhua](upstream-skills/02-chinese-and-bilingual/shuorenhua/README.md) |

---

### 3. 按文字形式与体裁分类 (`04-genres-academic-tech-social/`)

| 文字体裁 / 场景 | 本仓核心文件与资料汇编 | 完整收录的上游开源体裁 Skill 仓库 |
|:---|:---|:---|
| **学术论文、基金本子、AIGC 降重与发布会原则** | [paper-boundaries.md](paper-boundaries.md)（`发布会原则`）· [by-genre-academic-tech-social.md](curated-guides/by-genre-academic-tech-social.md)（Part 1：Simon Peyton Jones、Mensh & Kording、Lipton & Steinhardt、Widom） | [AIScientists-Dev/academic-humanizer](upstream-skills/04-genres-academic-tech-social/academic-humanizer/SKILL.md) · [WenyuChiou/academic-writing-skills](upstream-skills/04-genres-academic-tech-social/academic-writing-skills/README.md) · [YuanZHAO321/Scientific-Writing-zh](upstream-skills/04-genres-academic-tech-social/Scientific-Writing-zh/SKILL.md) · [zczjyq/de-AIGC-skill](upstream-skills/04-genres-academic-tech-social/de-AIGC-skill/SKILL.md) · [Orchestra-Research/AI-Research-SKILLs](upstream-skills/04-genres-academic-tech-social/AI-Research-SKILLs-paper-writing/README.md) · [zLanqing/codex-claude-academic-skills](upstream-skills/04-genres-academic-tech-social/codex-claude-academic-skills/README.md) · [dengzhe-hou/research-writing-prompts](upstream-skills/04-genres-academic-tech-social/research-writing-prompts/README.md) · [redbaronyyyyy-eng/humanizer-zh-academic](upstream-skills/02-chinese-and-bilingual/humanizer-zh-academic/SKILL.md) · [cangtianhuang/humanizer-academic-zh](upstream-skills/02-chinese-and-bilingual/humanizer-academic-zh/SKILL.md) |
| **同行评审审稿与 Rebuttal 回复** | [by-genre-academic-tech-social.md](curated-guides/by-genre-academic-tech-social.md)（Durand、Zeller、Maarten Sap、魏秀参） | [MLNLP-World/Paper-Rebuttal-Tips](upstream-skills/04-genres-academic-tech-social/Paper-Rebuttal-Tips/README.md) · [yuangao-tum/rebuttal-skills](upstream-skills/04-genres-academic-tech-social/rebuttal-skills/README.md) · [xf686/Meet-Reviewer-2](upstream-skills/04-genres-academic-tech-social/Meet-Reviewer-2/README.md) |
| **技术博客、设计文档与 GitHub README** | [by-genre-academic-tech-social.md](curated-guides/by-genre-academic-tech-social.md)（Part 2：Google Dev Style Guide、Diátaxis、Eugene Yan、Julia Evans） | [anthropics/skills (`doc-coauthoring`)](upstream-skills/05-visual-image-figure-and-ui/anthropics-skills/skills/doc-coauthoring/SKILL.md) · [cursor/plugins (`pstack` technical-writing)](upstream-skills/04-genres-academic-tech-social/cursor-pstack-technical-writing/README.md) · [Omer-Dahan/readme-skill](upstream-skills/04-genres-academic-tech-social/readme-skill/README.md) · [RichardLitt/standard-readme](upstream-skills/04-genres-academic-tech-social/standard-readme/README.md) |
| **公众号、小红书、知乎与 LinkedIn 社媒写作** | [by-genre-academic-tech-social.md](curated-guides/by-genre-academic-tech-social.md)（Part 3：少数派、人人都是产品经理、Melanie Goodman LinkedIn 指南） | [imraywang/wewrite](upstream-skills/04-genres-academic-tech-social/wewrite/README.md) · [guzhezao/xhs-content-skill](upstream-skills/04-genres-academic-tech-social/xhs-content-skill/SKILL.md) · [meikis/remove-ai-flavor-writing-skill](upstream-skills/04-genres-academic-tech-social/remove-ai-flavor-writing-skill/SKILL.md) · [KKKKhazix/human-writing](upstream-skills/02-chinese-and-bilingual/human-writing/README.md) · [coreyhaines31/marketingskills](upstream-skills/04-genres-academic-tech-social/marketingskills-copy-social-email/README.md) |
| **冷启动邮件、内部沟通与中文公文** | [by-genre-academic-tech-social.md](curated-guides/by-genre-academic-tech-social.md)（BuiltForB2B Cold Email、Matt Might 学术邮件指南） | [Liuxiangjian-ai/official-document-skill](upstream-skills/04-genres-academic-tech-social/official-document-skill/SKILL.md) · [anthropics/skills (`internal-comms`)](upstream-skills/05-visual-image-figure-and-ui/anthropics-skills/skills/internal-comms/SKILL.md) · [coreyhaines31/marketingskills (`cold-email`)](upstream-skills/04-genres-academic-tech-social/marketingskills-copy-social-email/skills/cold-email/SKILL.md) · [jiutianxvanyin/humanizer-formal](upstream-skills/02-chinese-and-bilingual/humanizer-formal/SKILL.md) |

---

### 4. 按生图、科研配图与 UI 视觉去 AI 味分类 (`05-visual-image-figure-and-ui/`)

| 视觉领域 | 实测文档与政策汇编 | 完整收录的上游开源视觉 / 图表 / UI Skill 仓库 |
|:---|:---|:---|
| **AI 生图光学写实与去塑料感（Midjourney / FLUX / SD / GPT Image）** | [by-visual-image-figure-ui.md](curated-guides/by-visual-image-figure-ui.md)（Part I：Midjourney `--style raw`、BFL FLUX Raw、相机文件名特征与社区去蜡像工作流） | [black-forest-labs/skills](upstream-skills/05-visual-image-figure-and-ui/black-forest-labs-skills/README.md) · [smixs/visual-skills](upstream-skills/05-visual-image-figure-and-ui/visual-skills/README.md) · [keng1304/awesome-ai-visual-realism-prompts](upstream-skills/05-visual-image-figure-and-ui/awesome-ai-visual-realism-prompts/README.md) · [willwulfken/MidJourney-Styles-and-Keywords-Reference](upstream-skills/05-visual-image-figure-and-ui/MidJourney-Styles-and-Keywords-Reference/README.md) |
| **科研论文配图合规、审稿避坑与十条准则** | [by-visual-image-figure-ui.md](curated-guides/by-visual-image-figure-ui.md)（Part II：Nature Portfolio AI 配图禁令、Elisabeth Bik 案例、Rougier 等 *PLOS Comp Biol* 2014） | [Haojae/scipilot-figure-skill](upstream-skills/05-visual-image-figure-and-ui/scipilot-figure-skill/SKILL.md) · [BAIKEMARK/happy-figure-skill](upstream-skills/05-visual-image-figure-and-ui/happy-figure-skill/SKILL.md) · [nrokh/ScientificFigures](upstream-skills/05-visual-image-figure-and-ui/ScientificFigures/README.md) · [rougier/ten-rules](upstream-skills/05-visual-image-figure-and-ui/ten-rules/README.rst) |
| **前端网页与产品界面反 AI 模板化（UI Anti-Slop）** | [by-visual-image-figure-ui.md](curated-guides/by-visual-image-figure-ui.md)（Part III：Ken Imoto 三大 UI Slop 模式、Volpe 与 HN 反紫渐变/三卡片讨论） | [anthropics/skills (`frontend-design` / `canvas-design` / `brand-guidelines` / `theme-factory`)](upstream-skills/05-visual-image-figure-and-ui/anthropics-skills/README.md) · [Nutlope/hallmark](upstream-skills/05-visual-image-figure-and-ui/hallmark/README.md) · [Ferousco-dev/anti-slop-design](upstream-skills/05-visual-image-figure-and-ui/anti-slop-design/README.md) · [h3nryprod01/design-taste](upstream-skills/05-visual-image-figure-and-ui/design-taste/SKILL.md) |
