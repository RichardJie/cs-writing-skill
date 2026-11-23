---
name: humanize
description: "Remove AI voice and synthetic slop across prose, academic papers, visuals, and UI. Supports :chinese, :english, :bilingual, :paper-boundaries (press-conference principle), :academic/:rebuttal/:nsfc, :model (:gpt/:claude/:gemini/:deepseek/:qwen/:kimi/:doubao), genres (:blog/:readme/:social/:email/:sop/:script/:fiction), visuals (:image/:mj/:flux/:figure/:ui), and :audit."
---

# Humanize — Multi-Dimensional AI-Voice Removal & Narrative Surgery Suite

One installable skill, five orthogonal axes plus a quantitative 3-Pass audit engine. **Read every matched module in full before rewriting or generating.**

```text
humanize/
├── SKILL.md                                       # Master router, guardrails & chaining rules
├── chinese.md                                     # :chinese — 7-step surgery, 28 CN patterns, anti-translationese
├── english.md                                     # :english — C1-F10 catalog, direct-statement law, zero-dash rule
├── paper-boundaries.md                            # :paper-boundaries — 发布会原则 (Press-Conference Principle)
├── references/
│   ├── methodology-and-audit.md                   # :audit / :rubric — 3-Pass Engine, 100-pt rubric & voice calibration
│   ├── bilingual-tech-writing.md                  # :bilingual — CN-EN CS prose, Pangu spacing, 32 anti-calques
│   ├── model-fingerprints.md                      # :model — GPT / Claude / Gemini / DeepSeek / Qwen / Kimi / Doubao / Llama
│   ├── academic-prose-and-rebuttal.md             # :academic / :rebuttal / :nsfc — papers, OpenReview, NSFC & LaTeX
│   ├── genres-playbook.md                         # :blog / :readme / :social / :email / :sop / :script / :fiction (15 genres)
│   ├── visual-image-de-ai.md                      # :image / :photo / :mj / :flux — optical physics, prompts & halation/grain
│   └── scientific-figures-and-ui-de-ai.md         # :figure / :diagram / :ui — Nature/NeurIPS vectors & anti-slop UI
└── agents/openai.yaml
```

---

## 1. Multi-Dimensional Tag Router (5 Axes + Audit Engine)

Explicit tags win and **compose freely across axes** (e.g., `/humanize :academic :english :claude` or `/humanize :chinese :wechat :deepseek`). Read only the modules triggered by the prompt or auto-detected from the input.

### (a) Axis 1 — Language Tracks

| Tag(s) | Read | Scope & Core Surgery |
|:---|:---|:---|
| `:chinese` (`:zh`, `:cn`) | [chinese.md](chinese.md) | Simplified Chinese prose: 7-Step Surgery (`七步手术法`), 28 Chinese AI patterns, 3-tier互联网黑话/公文套话 blacklist, 余光中 12-symptom anti-translationese, parataxis (`意合流水句`) & burstiness |
| `:english` (`:en`) | [english.md](english.md) | English prose: 31-pattern catalog (`C1–C6`, `L1–L12`, `M1–M3`, `F1–F10`), Direct-Statement Law (hard ban on `not X, but Y`), zero prose em/en-dash ban (`—`/`–`), Tier-1/Tier-2 blacklists, Provost/Williams burstiness & ESL rescue |
| `:bilingual` (`:zh-en`) | [references/bilingual-tech-writing.md](references/bilingual-tech-writing.md) *(pair with [chinese.md](chinese.md))* | CN-EN mixed CS/engineering prose: Pangu spacing (`盘古之白`) + 8 non-space exceptions, official tech casing (`PyTorch`/`vLLM`/`LaTeX`), inline `` `code` `` boundaries, 32-term CS anti-calque dictionary (`vanilla`/`oracle`/`ground truth`), 10 AST fixes killing English-syntax-in-Chinese |

### (b) Axis 2 — Academic Narrative & Scholarly Prose (Incorporating `paper-boundaries`)

> **Mandatory Academic Execution Order:** Always run **narrative & scope surgery in [paper-boundaries.md](paper-boundaries.md) FIRST** before sentence-level de-slopping! Never polish the grammar of a chronological failure diary, an apologetic comparison, or an uncurated experiment dump.

| Tag(s) | Read (In Order) | Scope & Core Surgery |
|:---|:---|:---|
| `:paper-boundaries` | [paper-boundaries.md](paper-boundaries.md) | **发布会原则 (Press-Conference Principle):** 12 core mandates, 7-tier priority waterfall for unfavorable results, CN/EN self-sabotage lexicons, Pareto regime reframing, experiment-as-argument role mapping, reviewer-knife prevention, full story reconstruction |
| `:academic` (`:paper`) | 1. [paper-boundaries.md](paper-boundaries.md)<br>2. [references/academic-prose-and-rebuttal.md](references/academic-prose-and-rebuttal.md)<br>3. Language track ([english.md](english.md) or [chinese.md](chinese.md)) | Peer-reviewed manuscripts & `.tex` files: Kobak/Liang scholarly excess-vocabulary purge (`delve`, `intricate`, `meticulous`, `pivotal`), 5-move Abstract, falsifiable Contribution contracts, 3-move Taxonomic Related Work synthesis (killing `[1] did X, [2] did Y` laundry lists), Method contracts, anti-table-reader Experiments, safe Operating Boundaries, and 8 LaTeX-safe invariants |
| `:rebuttal` | 1. [paper-boundaries.md](paper-boundaries.md)<br>2. [references/academic-prose-and-rebuttal.md](references/academic-prose-and-rebuttal.md) (§3) | OpenReview / ARR / IEEE / 中文顶刊审稿回复: `Direct-Evidence-Diff` micro-structure, zero sycophantic groveling, zero camera-ready IOUs, polite factual misreading correction, compact ablation proofs |
| `:nsfc` (`:grant`) | 1. [paper-boundaries.md](paper-boundaries.md)<br>2. [references/academic-prose-and-rebuttal.md](references/academic-prose-and-rebuttal.md) (§4)<br>3. [chinese.md](chinese.md) | 国自然（NSFC）基金本子与中文学位论文：立项依据「倒三角四段切入法」、拟解决的关键科学问题 vs 工程实现难点剥离、研究方案消灭「形容词空头支票」 |

### (c) Axis 3 — AI Model Fingerprints

| Tag(s) | Read | Target Generator Signatures Purged |
|:---|:---|:---|
| `:model` (auto-triage) | [references/model-fingerprints.md](references/model-fingerprints.md) | 6-axis Rapid Model-ID Triage Matrix (`Sun et al.` / `EQ-Bench Slop Forensics`) + Adversarial Cross-Family Scrubbing Protocol (stopping editor LLMs from swapping GPT slop for Claude slop) |
| `:gpt` | [references/model-fingerprints.md](references/model-fingerprints.md) (Part II) | **OpenAI family:** GPT-4o (`not just X—it's Y`, em-dash chains, `, underscoring...`), GPT-4.5 (frictionless magazine symmetry), o1/o3 (parenthetical spec overload), GPT-5 (upfront scope/rubric throat-clearing) |
| `:claude` | [references/model-fingerprints.md](references/model-fingerprints.md) (Part III) | **Anthropic Claude 3.5/3.7/4 Sonnet & Opus:** Faux-candor whispers (*"Here's the thing:"*, *"And honestly?"*), therapy/essay verbs (*unpack, sit with, worth naming, load-bearing*), *genuinely / quietly*, staccato 1-line paragraphs, fragment-colon reveals, 中文温和随笔反思腔 |
| `:gemini` | [references/model-fingerprints.md](references/model-fingerprints.md) (Part IV) | **Google Gemini 2.5/3/4:** Compulsive `1. **Bold Label:**` echo lists, textbook slide-advance signposting (*"Here is a breakdown"*), unsolicited everyday waiter/library analogies, 中文科普讲义腔 |
| `:deepseek` | [references/model-fingerprints.md](references/model-fingerprints.md) (Part V.1) | **DeepSeek-R1/V3:** `<think>` / `Wait,` CoT dialectic leakage, 公众号宏大叙事与金句拔高（*硅基荒原、确定的锚点、静悄悄的革命*）, 对仗四字小标题癖, 四字成语飞镖, `——` 电击转折 |
| `:qwen` | [references/model-fingerprints.md](references/model-fingerprints.md) (Part V.2) | **Qwen (通义千问):** 大厂高管周报黑话（*颗粒度、拆解、抓手、闭环、水位、打法*）+ 体制内公文对称套话（*既要…又要…还要…*） |
| `:kimi` | [references/model-fingerprints.md](references/model-fingerprints.md) (Part V.3) | **Kimi (月之暗面):** 知乎高赞读书笔记腔（*先说结论、不妨换个角度*）+ 段落连接词泛滥（*首先/其次/再者/综上所述*）+ 长文锋芒磨平 |
| `:doubao` | [references/model-fingerprints.md](references/model-fingerprints.md) (Part V.4) | **Doubao (豆包):** 高情绪价值客服捧场（*问得太到位了！*）+ 小红书网感模板（*宝子们/狠狠拿捏*）+ Emoji 与感叹号通胀 |
| `:llama` / `:mistral` | [references/model-fingerprints.md](references/model-fingerprints.md) (Part VI) | **Open-Weights:** Llama 3–4 assistant chat bookends, 4-sentence block monotony & `Furthermore/Moreover` glue; Mistral consulting-deck bulletization & stiff Romance cognates (*ameliorate, vis-à-vis*); `R1-Distill` chimeras |

### (d) Axis 4 — Genre & Format Playbooks

| Tag(s) | Read | Genre Register & Structural Rules |
|:---|:---|:---|
| `:blog` / `:readme` / `:postmortem` | [references/genres-playbook.md](references/genres-playbook.md) (§1–§2) | **Engineering:** Crime-scene tech blog openers with real logs/diffs; 10-second utilitarian GitHub READMEs (code in top 25 lines, zero `🚀 Blazingly Fast` fluff, explicit Non-Goals); blameless timestamped incident RCAs with ticketed fixes |
| `:social` / `:wechat` / `:xhs` / `:zhihu` / `:x` / `:linkedin` / `:substack` | [references/genres-playbook.md](references/genres-playbook.md) (§1, §3) | **Creator Platforms:** 微信公众号（极小切口、砸碎四字对仗标题、冷收尾）；小红书（前提先行 + 真实毛边槽点、去排队 Emoji）；知乎（首行拆台 + 利益链机制拆解）；X（首行硬指标）；LinkedIn（禁一行一句 Broetry 与假鸡汤寓言）；Substack（去 Claude 随笔腔） |
| `:email` / `:sop` / `:resume` / `:prd` | [references/genres-playbook.md](references/genres-playbook.md) (§1, §4) | **Career & Product:** `<=120w` BLUF work & PhD cold emails (mechanism hook, zero *"hope this finds you well"*); Grad SOPs (open on research tension, zero childhood origin stories); metric-dense XYZ Resumes; deterministic PRDs with failure matrices & kill criteria |
| `:script` / `:fiction` | [references/genres-playbook.md](references/genres-playbook.md) (§1, §5) | **Spoken & Creative:** Ear-first Bilibili/YouTube/Podcast scripts (`<=15w` / `<=18字` 气口切分, zero `former/latter` or nested clauses); subtextual Creative Fiction (physical object staging over emotion labels, banning *ozone / shivers / Elara* clichés & moralizing endings) |

### (e) Axis 5 — Visual, Image Generation, Scientific Figures & UI De-AI

| Tag(s) | Read | Visual / Interface De-Slopping Scope |
|:---|:---|:---|
| `:image` / `:photo` / `:mj` / `:flux` (`:sdxl`, `:gpt-image`, `:imagen`, `:ideogram`, `:recraft`) | [references/visual-image-de-ai.md](references/visual-image-de-ai.md) | **生图与摄影去 AI 味:** Diagnose `V1–V12` (plastic waxy skin, MJ teal-orange HDR, GPT `4000K` yellow sepia filter, dead-center symmetry, sterile rooms, stock gaze, `f/1.2` bokeh abuse); purge poison tokens (`8k`, `hyperrealistic`, `masterpiece`); camera/lens/film/entropy prompts; model workflows (`--style raw`, Flux Raw / `guidance 2.0–2.5`, GPT-Image `5600K` override); Lightroom/PS/Resolve + Python `Pillow`/`NumPy` red-channel halation & midtone grain |
| `:figure` / `:diagram` | [references/scientific-figures-and-ui-de-ai.md](references/scientific-figures-and-ui-de-ai.md) (Part I) *(pair with [paper-boundaries.md](paper-boundaries.md))* | **科研配图与顶会架构图:** Publisher AI rules (*Science*/*Nature*/*Cell*/*NeurIPS*), purge `SF1–SF10` (glowing sci-fi brains, neon isometric 3D cubes, raster gibberish), exact 1:1 mm column widths, `Arial 6–8pt` + LaTeX math parity, Okabe-Ito & Two-Tone HEX tokens, copy-paste `matplotlib` (`pdf.fonttype=42`) & `TikZ` vector templates |
| `:ui` | [references/scientific-figures-and-ui-de-ai.md](references/scientific-figures-and-ui-de-ai.md) (Part II) | **前端与 Vibe-Coding UI 去 AI 味:** Purge `UI1–UI12` (indigo-purple gradient virus, `✨` pill-badge hero, uniform 3-col icon cards, unconfigured `Inter`, fake `"Sarah Chen"` copy, missing states); 5 intentional human design archetypes, `tabular-nums` CSS, `DESIGN.md` guardrail block, React+Tailwind refactor, 5-state completeness audit |

### (f) Engine & Quantitative Scoring Audit

| Tag(s) | Read | Engine & Audit Scope |
|:---|:---|:---|
| `:audit` / `:rubric` | [references/methodology-and-audit.md](references/methodology-and-audit.md) | **3-Pass Humanization Engine & 100-Point Rubric:** Perplexity/UID/burstiness ($CV_L$) mechanics, Step 0 Information-Epistemic Ledger, Pass 1 (Macro-Structure) -> Pass 2 (Lexical/Syntactic) -> Pass 3 (Burstiness & Read-Aloud), 5 Hard-Fail Gates (`G1–G5`), 6D 100-Point Rubric (`D1–D6`), 8-Axis Voice DNA Calibration, and 12 Anti-Overcorrection Guardrails (`AG-01`–`AG-12`) |

---

## 2. Smart Auto-Detection & Multi-Module Chaining

### When No Explicit Tag Is Given (Auto-Detection Protocol)

1. **Modality first:**
   - Image-generation prompt, camera/photo critique, or Midjourney/Flux/GPT-Image request -> [references/visual-image-de-ai.md](references/visual-image-de-ai.md).
   - Academic Figure 1, architecture diagram, `matplotlib`/`TikZ` plot -> [references/scientific-figures-and-ui-de-ai.md](references/scientific-figures-and-ui-de-ai.md) (Part I) + [paper-boundaries.md](paper-boundaries.md).
   - HTML/CSS/React/Tailwind component, landing page, or `DESIGN.md` -> [references/scientific-figures-and-ui-de-ai.md](references/scientific-figures-and-ui-de-ai.md) (Part II).
2. **Academic vs. Non-Academic prose:**
   - Research paper, `.tex` draft, abstract, experiment analysis, OpenReview rebuttal, or NSFC grant -> [paper-boundaries.md](paper-boundaries.md) **first**, then [references/academic-prose-and-rebuttal.md](references/academic-prose-and-rebuttal.md), plus the matching language track.
   - Recognizable genre (README, postmortem, 公众号, 小红书, 知乎, LinkedIn, X, Substack, cold email, SOP, resume, PRD, spoken script, fiction) -> [references/genres-playbook.md](references/genres-playbook.md) plus the matching language track.
3. **Language track selection:**
   - Chinese prose with English code/CS terms -> [chinese.md](chinese.md) + [references/bilingual-tech-writing.md](references/bilingual-tech-writing.md).
   - Pure Chinese prose -> [chinese.md](chinese.md).
   - English prose -> [english.md](english.md).
   - Genuinely ambiguous input -> ask once; default to [english.md](english.md).
4. **Generator fingerprint overlay:** If the user names the generator or the text exhibits strong model-specific tells (e.g., Claude *"Here's the thing"*, Gemini `1. **Label:**` lists, DeepSeek 对仗金句), also consult [references/model-fingerprints.md](references/model-fingerprints.md).

### Canonical Multi-Module Chaining Recipes

| Task | Exact Module Chain (Read & Apply in Sequence) |
|:---|:---|
| **CS / STEM Paper (EN)** | [paper-boundaries.md](paper-boundaries.md) → [references/academic-prose-and-rebuttal.md](references/academic-prose-and-rebuttal.md) → [english.md](english.md) *(+ [references/model-fingerprints.md](references/model-fingerprints.md) if LLM-drafted)* |
| **中文论文 / 国自然 (NSFC)** | [paper-boundaries.md](paper-boundaries.md) → [references/academic-prose-and-rebuttal.md](references/academic-prose-and-rebuttal.md) (§4) → [chinese.md](chinese.md) → [references/bilingual-tech-writing.md](references/bilingual-tech-writing.md) |
| **Conference Rebuttal** | [paper-boundaries.md](paper-boundaries.md) → [references/academic-prose-and-rebuttal.md](references/academic-prose-and-rebuttal.md) (§3) → [english.md](english.md) |
| **CN Tech Blog / README** | [references/genres-playbook.md](references/genres-playbook.md) (§2) → [chinese.md](chinese.md) → [references/bilingual-tech-writing.md](references/bilingual-tech-writing.md) |
| **公众号 / 知乎 / 小红书** | [references/genres-playbook.md](references/genres-playbook.md) (§3) → [chinese.md](chinese.md) → [references/model-fingerprints.md](references/model-fingerprints.md) (Part V) |
| **Full Audit / High-Stakes Edit** | Append [references/methodology-and-audit.md](references/methodology-and-audit.md) (§3–§4) to enforce the 3-Pass Engine and `>=80/100` gate check |

---

## 3. Shared Guardrails & Constraint Precedence (All Tracks)

When rules pull in opposite directions, resolve strictly top-down (`P1` -> `P5`):

1. **`P1` Sacred-Span Immunity:** Never alter verbatim quotations, citations (`\cite{}`, `[12]`), inline code, fenced code blocks, CLI flags, file paths, URLs, YAML frontmatter, mathematical formulas, or pedagogical anti-pattern examples *about* AI writing.
2. **`P2` Factual & Epistemic Conservation (`信息与确定度守恒`):** Preserve every supported fact, entity, number, date, negation, and actor. **Never invent metrics, outages, prices, or personal anecdotes** to sound concrete (use `[TODO: exact metric]` if needed). Never upgrade epistemic certainty (`may` stays `may`; correlation never becomes causation).
3. **`P3` User Voice Calibration Override:** When the user provides an authentic writing sample, match its cadence, contraction rate, quotation style, and punctuation habits (including em dashes) over default bans—without importing facts from the sample.
4. **`P4` Genre & Register Lock:** Match target register before stylistic surgery. Academic papers, RFCs, postmortems, and legal clauses stay formal and precise (zero slang, zero contractions in formal papers); blogs, columns, and creator posts earn first-person edge and rhythm swings.
5. **`P5` Cluster-First De-Slopping & No-Op Preservation:** Purge Class I tells (`not X, but Y`, chatbot wrappers, Tier-1 slop like `delve`/`tapestry`/`赋能`/`底层逻辑`) on sight. Fix Class II/III signals when clustered. Leave specific, messy, lived-in human prose alone—over-polishing human drafts *creates* AI voice, and swapping corporate slop for 1-line LinkedIn broetry (`Honestly? Let that sink in.`) is strictly banned.

---

## 4. Output Modes

| Mode | Trigger | Deliverable |
|:---|:---|:---|
| **Pasted text (default)** | User pastes text in chat | Brief diagnosis bullets (top clustered tells + optional `:audit` score) → final humanized text → concise change summary |
| **File** | User names file(s) on disk | Rewrite file in place leaving code blocks, math, citations, and frontmatter intact; summarize structural changes in chat |
| **Embedded** | Called as an internal step by another skill/pipeline | Run passes silently; output **only** the final rewritten text/prompt/code with zero commentary |
| **Visual / UI** | `:image`, `:figure`, or `:ui` task | Visual tell diagnosis → optical/vector/UI specification or production-ready prompt/code → post-processing or state checklist |

---

## 5. Crisp Examples Across Axes

- **`:chinese`** — Input: *"在数字化转型的浪潮中，企业必须认识到数据隐私保护的重要性。这不仅是合规的要求，更是建立用户信任的基石。"*  
  → Apply [chinese.md](chinese.md): cut grand-narrative opener and `不仅…更是…` pivot → *"别跟我提「数字化转型」这种大词。用户发现聊天记录被拿去做广告，信任当场崩。合规是后话；先把数据加密做扎实。"*
- **`:english`** — Input: *"Additionally, this pivotal initiative underscores our commitment to fostering innovation in today's evolving landscape—it's not just about technology, but about culture."*  
  → Apply [english.md](english.md): kill Tier-1 vocabulary, em dash, and negation pivot → *"The initiative funds two internal tools and a weekly demo slot. Team culture shapes how those tools get used; the budget line is explicit in Appendix B."*
- **`:paper-boundaries` + `:academic`** — Input: *"Initially, we tried full attention at 64k tokens, which unfortunately failed due to OOM. Regrettably, our SparseBlock lags behind FlashAttention-2 by 0.4 PPL on 2k sequences..."*  
  → Apply [paper-boundaries.md](paper-boundaries.md) + [references/academic-prose-and-rebuttal.md](references/academic-prose-and-rebuttal.md): strip failure-diary chronology and self-sabotage; lead with the 64k regime win → *"Exact attention runs out of memory at 64k tokens, whereas SparseBlock completes the pass within budget and accelerates long-context execution. On short 2k sequences, block-sparse pruning trades 0.4 perplexity points against exact FlashAttention-2 to enable this scaling."*
- **`:image :mj`** — Input: *"Handsome Asian engineer in high-tech lab, confident smile, cinematic lighting, bokeh, photorealistic, 8k, masterpiece."*  
  → Apply [references/visual-image-de-ai.md](references/visual-image-de-ai.md): purge poison buzzwords, anchor lens physics & entropy (`50mm f/2.8`, `4500K` lab fluorescents, oscilloscope bench clutter, off-camera gaze, `--style raw --s 45`).

---

## Related Skills in Pack

- **`plain`** (`../plain/SKILL.md` when installed in pack) — Pedagogical explanation technique: locate exact misconception and walk through one small domain-native numerical example with zero skipped steps. Orthogonal to prose de-slopping.
- **`cs-report-ppt`** (`../cs-report-ppt/SKILL.md` when installed in pack) — Multi-scenario, multi-disciplinary academic slide deck generator with native OMML math and Vision-in-the-Loop QA.
