<a id="english"></a>

# Reviewer 2 🔪

> **Meet Reviewer 2 before they meet you.**
> **在 Reviewer 2 找上你之前,先让他帮你挑一遍。**

**English** · [中文 ↓](#chinese)

> Point it at your paper draft. It simulates a full peer-review panel — the generous champion, the brutal *Reviewer 2*, and a novelty-hawk Area Chair — predicts the reviews you'll get, and hands you a prioritized, **evidence-grounded** fix list. Every criticism is pinned to a line in *your* draft. No invented flaws.

A [Claude Code](https://claude.com/claude-code) skill for researchers who'd rather get torn apart in private.

---

## The problem

You already know the feeling. You submit. Three months later, **Reviewer 2** writes the words that sink your paper:

> *"The baselines are weak and the improvements are not statistically significant. Reject."*

The brutal part: **most of those wounds were self-inflicted and fixable** — a missing baseline, an un-controlled confound, an overclaim in the abstract, a number with no error bars. You just didn't have a hostile reader before the deadline.

`reviewer-2` **is that hostile reader.** It runs the panel on your draft *now*, while you can still fix things.

## What it does

You give it a draft (`.pdf`, `.tex`, `.md`, an arXiv link, or pasted text). It produces a **red-team report**:

1. **Simulated reviews** from a panel that genuinely disagrees with itself —
   - 🫶 **R1, The Champion** — finds your real contribution (and calibrates what's *actually* strong: where even R1 can't praise, you're weak).
   - 🔪 **R2, The Methodological Skeptic** — the one you're afraid of. Hunts weak baselines, missing ablations, confounds, cherry-picking, overclaiming, single-run "SOTA".
   - 🦅 **R3 / AC, The Novelty Hawk** — *"isn't this just X + Y?"* Demands what's actually new versus recent work.
2. **An Area Chair meta-review** — consensus weaknesses (the deadly ones), split opinions, the 2–3 decisive factors, and a **predicted outcome** (Reject / Borderline / Accept).
3. **A pre-submission fix list** — every weakness, deduped and **sorted by impact × effort**, each one telling you *what to change, where, and whether you can realistically do it before the deadline.*

## Does it actually find real flaws? (a real run)

We pointed it at a **real, recent arXiv preprint** — a reasoning-efficiency benchmark — and let it pick the paper itself. The simulated R2 caught a textbook methodological flaw, pinned to a section:

> 🔪 **R2:** The headline claim is *"models differ wildly in token usage."* But the paper **deliberately selects problems with high token-usage variance** `[§3.1, §4.1]` — so the dramatic difference may be **manufactured by the sampling criterion itself**. That's circular. Needs a control on a random, unbiased sample.

That's not "consider adding more experiments." That's *"your conclusion is baked into your sampling — see §3.1."* — exactly the wound a real Reviewer 2 lands, found in minutes, before submission.

*(We keep the paper anonymous on purpose. This tool is for red-teaming **your own** draft, not dunking on other people's.)*

## Two modes

- **A — Red-team your own draft** before submission → simulated panel + predicted outcome + fix list.
- **B — Review someone else's paper** when you're an assigned reviewer or helping your advisor → a fair, **venue-formatted, submission-ready review** you sign off on.

## Grounded in real standards — rigorous *and* fair

Built on the official reviewer guidelines of **NeurIPS, ICLR, and ACL Rolling Review** — the same dimensions and rating scales real reviewers use. Crucially, every criticism is checked against **ACL's official H1–H17 list of *illegitimate* critiques** — *"not novel" with no citation, "doesn't beat SOTA", "the method is too simple", "the authors should run extra experiment X", "limitations = weaknesses"*… If a complaint is on that list, the tool **drops it or demotes it to a gentle suggestion**. That's the line between a rigorous reviewer and a toxic one — Reviewer 2 with the receipts, not the cheap shots.

And the checklist isn't hand-waved — it's distilled from **2,956 real ICLR 2024 reviews** (public on OpenReview). The data is blunt: *weak novelty, poor positioning, and overclaiming* are what actually sink papers, while *"doesn't beat SOTA"* and *"you should run more experiments"* are common but barely move the score. In other words, **the real data confirms the fairness firewall.** → [methodology & numbers](skills/paper-redteam/references/data/iclr2024-weakness-analysis.md)

## The one rule that makes it trustworthy

**No naked criticism, and no invented flaws.**

- Every weakness is pinned to a location in your draft — `[§4.2]`, `[Table 1]`, `["a short quote"]` — or explicitly flagged `⚠ MISSING` (because a missing baseline *is* a finding, not a hallucination).
- If a dimension has no real problem, it says so. It will **not** manufacture a weakness to look thorough. A confident-but-fake criticism is worse than none.
- It separates 🔴 **substance** (your method/experiments don't hold up — may need new runs) from 🟡 **misread-risk** (you're actually fine, but the writing hands a reviewer the gun) from 🟢 **polish**. These get fixed completely differently, and conflating them is how you waste your last week before a deadline.

## Why not just ask ChatGPT "review my paper"?

| | Generic "review my paper" | **Reviewer 2** |
|---|:---:|:---:|
| Multiple reviewers who *disagree* | — | ✅ |
| Every criticism pinned to a location in your draft | sometimes | ✅ |
| Refuses to invent flaws when none exist | — | ✅ |
| Separates "real flaw" from "will be misread" | — | ✅ |
| Predicts the **decisive** factors, not a wall of nits | — | ✅ |
| A prioritized fix list sorted by impact × effort | — | ✅ |
| Honest about "can you fix this before the deadline?" | — | ✅ |

It's a structured workflow with a schema and an evidence contract — not a one-shot prompt.

## Install

**As a plugin (recommended):**
```bash
# Point Claude Code at this repo as a plugin source, then enable it
/plugin
```

**Or manually** — copy the skill into your skills directory:
```bash
cp -r skills/paper-redteam ~/.claude/skills/
```

## Usage

```
> Red-team my draft before I submit: ~/papers/adaprompt/main.tex
```
You'll get a report at `redteam/<paper-slug>.md`: simulated reviews → AC meta-review → a prioritized fix list.

Tell it where you're submitting to sharpen the panel:
```
> Red-team this for NeurIPS, and add a reproducibility-stickler reviewer.
```

See [`examples/example-redteam.md`](./examples/example-redteam.md) for a full sample report (on a fictional paper).

## Honest limitations

- **It's a simulation, not a verdict.** Predicted scores reflect *which guns your current draft walks into* — not what real reviewers, sampled on a real day in a real competition, will actually do. It lowers your reject risk; it does not promise acceptance.
- **It won't fabricate experiments.** When the fix is "run an ablation," it tells you *what* to run and *why* — it never invents results.
- **It doesn't rewrite your paper.** It produces a diagnosis. Acting on it is your call.

## Roadmap

- **v1 (now):** Two modes (red-team your own draft / review others' papers), grounded in NeurIPS/ICLR/ACL guidelines + the H1–H17 fairness firewall. ✅
- **v2:** **Rebuttal Copilot** — feed in the *real* reviews you got back; get a point-by-point response grounded in your paper that never promises experiments you didn't run.
- **v2:** Venue packs (CVPR / ACL / journal) that swap in the right review priorities.
- **v2:** A "defended draft" diff — show which fixes you applied and which guns are now spiked.

## Acknowledgments

Architecture and the evidence-grounded, output-is-an-artifact discipline are studied from [academic-research-skills](https://github.com/imbad0202/academic-research-skills) (structured artifacts / contract patterns) and [nature-skills](https://github.com/Yuan1z0825/nature-skills) (no-claim-without-evidence, modular references). We borrow their *patterns*, not their code. Sibling skill: [paper-method-bridge](https://github.com/xf686/paper-method-bridge).

## License

[MIT](./LICENSE) — free forever.

<br>

---
---

<br>

<a id="chinese"></a>

# Reviewer 2 🔪(中文)

> **在 Reviewer 2 找上你之前,先让他帮你挑一遍。**

[↑ English](#english) · **中文**

> 把论文草稿丢进来,它模拟一个完整的审稿小组——温和的拥护者、暴躁的 *Reviewer 2*、卡 novelty 的 area chair——预测你会拿到的评审,并给你一份按优先级排序、**证据绑死**的修补清单。每条批评都钉在*你草稿*的具体某一行,绝不脑补不存在的毛病。

一个给研究者的 [Claude Code](https://claude.com/claude-code) 技能(skill)——**宁可先在私下被撕碎**。

---

## 它解决什么

那种感觉你太熟了。投出去,三个月后,**Reviewer 2** 写下那句毙掉你论文的话:

> *"baseline 偏弱,提升不显著。Reject。"*

最扎心的是:**这些伤多半是自己造成、且本可修补的**——少比了一个 baseline、没控住一个混淆变量、摘要里吹大了、某个数字没有误差棒。你只是在 deadline 前,**缺一个怀着敌意的读者**。

`reviewer-2` **就是那个敌意读者。** 它趁你还能改的时候,*现在*就把审稿小组放到你草稿上跑一遍。

## 它干什么

你给一份草稿(`.pdf` / `.tex` / `.md` / arXiv 链接 / 直接粘文本),它产出一份 **red-team 报告**:

1. **模拟评审**——一个会真·内部分歧的小组:
   - 🫶 **R1 拥护者** —— 找出你真正的贡献(顺带校准"什么是真强":连 R1 都夸不出口的地方,就是真弱)。
   - 🔪 **R2 方法怀疑论者** —— 你最怕的那个。专挑弱 baseline、缺失 ablation、混淆变量、樱桃挑选、过度承诺、单次跑就敢叫 SOTA。
   - 🦅 **R3 / AC 新意鹰派** —— *"这不就是 X+Y 吗?"* 逼问相对最近工作到底新在哪。
2. **AC 综合评审** —— 共识 weakness(最致命的)、分歧点、真正左右结局的 2–3 条、外加一个**预测结局**(Reject / Borderline / Accept)。
3. **投稿前修补清单** —— 所有 weakness 去重后,**按"影响 × 成本"排序**,每条告诉你:改什么、改哪、以及*deadline 前到底赶不赶得上*。

## 它真能挑出真毛病吗?(一次真实运行)

我们让它自己去 arXiv 挑了一篇**真实、近期的预印本**(一个推理效率 benchmark),跑了一遍。模拟出来的 R2 抓到一个教科书级的方法漏洞,并钉死了出处:

> 🔪 **R2:** 头条卖点是*"模型间 token 消耗差异巨大"*。但这篇**刻意筛选了"token 用量高方差"的题目** `[§3.1, §4.1]`——所以这个"巨大差异"很可能是**选题准则自己制造出来的**。这是循环论证,需要在随机/无偏抽样上做对照。

这不是"建议多补点实验",而是*"你的结论被你的采样写进去了——看 §3.1"*——正是真·Reviewer 2 一剑封喉的地方,在投稿前几分钟就被挖出来。

*(我们故意隐去论文名。这工具是帮你挑**自己**的稿,不是公开处刑别人的。)*

## 两种模式

- **A — 审自己的稿(红队):** 投稿前 → 模拟审稿小组 + 预测结局 + 修补清单。
- **B — 审别人的稿:** 你被指派当审稿人、或帮导师审稿时 → 产出一份**按会议官方表格式、公正、可直接提交**的评审(你过目签字后交)。

## 基于真实标准 —— 既严谨,又公正

建立在 **NeurIPS、ICLR、ACL Rolling Review 官方审稿人指南**之上——用的是真实审稿人同款的评审维度和评分量表。更关键的是:每条批评都要过 **ACL 官方的 H1–H17"不正当批评"黑名单**——*"不够新颖却不给引用""没超过 SOTA""方法太简单""作者应该再做个实验 X""有局限=有缺陷"*……只要命中黑名单,工具就**删掉它、或降级为温和建议**。这就是**严谨审稿人**和**键盘喷子**的分水岭——Reviewer 2 该有理有据,而不是耍嘴皮子。

而且那份"必查清单"不是拍脑袋——它**蒸馏自 2956 份 ICLR 2024 真实评审**(OpenReview 公开数据)。数据很直白:真正毙掉论文的是 *novelty 不足、定位没摆好、过度承诺*;而 *"没超 SOTA""你该多做点实验"* 虽然天天有人喊,却几乎不影响打分。换句话说,**真实数据反过来印证了那道公正性防火墙。** → [方法与数据](skills/paper-redteam/references/data/iclr2024-weakness-analysis.md)

## 让它可信的那一条铁律

**没有裸批评,也绝不编造毛病。**

- 每条 weakness 都钉到草稿里的具体位置——`[§4.2]`、`[表1]`、`["原文短引"]`——或显式标 `⚠ MISSING`(因为"少了个 baseline"是一条 finding,不是幻觉)。
- 某个维度上真没问题,就直说。它**不会**为了显得周全硬挑一条出来。一个自信却假的批评,比没有更糟。
- 它把 🔴 **实质问题**(方法/实验真站不住,可能要补实验)、🟡 **会被误读**(你其实没错,但写法把枪递给了审稿人)、🟢 **打磨**分开。三者修法天差地别,**混为一谈正是你白白浪费 deadline 前最后一周的元凶。**

## 为什么不直接问 ChatGPT "帮我审一下论文"?

| | 泛泛的"帮我审论文" | **Reviewer 2** |
|---|:---:|:---:|
| 多个会*互相不买账*的审稿人 | — | ✅ |
| 每条批评都钉到你草稿的具体位置 | 有时 | ✅ |
| 无实质问题时拒绝硬编一条 | — | ✅ |
| 区分"真缺陷"和"会被误读" | — | ✅ |
| 预测**决定性**因素,而非甩你一墙的鸡毛 | — | ✅ |
| 一张按"影响×成本"排序的修补清单 | — | ✅ |
| 诚实标注"这条 deadline 前赶得上吗" | — | ✅ |

它是一套带 schema 和证据契约的**结构化工作流**,不是一次性 prompt。

## 安装

**作为插件(推荐):**
```bash
# 把 Claude Code 指向本仓库作为插件源,然后启用
/plugin
```

**或手动** —— 把技能拷进你的 skills 目录:
```bash
cp -r skills/paper-redteam ~/.claude/skills/
```

## 用法

```
> 投稿前帮我 red-team 这份草稿:~/papers/adaprompt/main.tex
```
你会在 `redteam/<paper-slug>.md` 拿到报告:模拟评审 → AC 综合 → 优先级修补清单。

告诉它投哪,审稿会更准:
```
> 按 NeurIPS 标准 red-team,再加一个专盯可复现性的审稿人。
```

完整样例见 [`examples/example-redteam.md`](./examples/example-redteam.md)(跑在一篇虚构论文上)。

## 诚实的局限

- **是模拟,不是判决。** 预测分数反映的是"你当前草稿会撞上哪些枪",不是真实审稿人在真实竞争里当天会怎么打。它降低被毙风险,但**不承诺录用**。
- **绝不编实验。** 当修补建议是"补个 ablation",它只告诉你*补什么、为什么*,**绝不替你编结果**。
- **不替你改论文。** 它产出诊断;改不改、怎么改,你说了算。

## 路线图

- **v1(现在):** 两种模式(审自己 / 审别人),基于 NeurIPS/ICLR/ACL 官方指南 + H1–H17 公正性防火墙。✅
- **v2:** **Rebuttal Copilot** —— 把你*真正*收到的评审喂进去,生成逐条、绑定到你论文、**绝不乱承诺没做过的实验**的回复。
- **v2:** venue 包(CVPR / ACL / 期刊),自动切换对应的评审重点。
- **v2:** "已设防草稿"diff —— 显示你改了哪些、哪些枪已经被堵上。

## 致谢

架构与"证据绑死 / 输出即成品"的纪律,研究自 [academic-research-skills](https://github.com/imbad0202/academic-research-skills)(结构化产物 / 契约模式)与 [nature-skills](https://github.com/Yuan1z0825/nature-skills)(无证据不立论、模块化 references)。我们借鉴其*模式*,而非代码。姊妹技能:[paper-method-bridge](https://github.com/xf686/paper-method-bridge)。

## 许可

[MIT](./LICENSE) —— 永久免费。
