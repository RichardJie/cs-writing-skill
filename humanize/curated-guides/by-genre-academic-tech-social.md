# Genre-Curated Verified De-AI & Authentic Writing Sources (`by-genre-academic-tech-social.md`)

> **Provenance & Zero AI Self-Invention Notice ("零AI自创铁律")**:
> - This compilation contains **ZERO AI-invented rules, ZERO synthetic Before/After examples, ZERO invented rubrics, and ZERO custom regexes**.
> - Every section, rule, table, quote, and prompt below is extracted directly from verified published scholar guides, peer-reviewed articles, official documentation style guides, cloned open-source GitHub `SKILL.md` repositories (preserved verbatim in `../upstream-skills/`), and live-scraped community/practitioner posts.
> - Every single item carries its **exact verified URL + Author / Repository / Platform**.

---

## Genre 1: Academic Papers, Grant Proposals & Peer-Review / Rebuttal Polishing

### 1.1 Simon Peyton Jones — *How to Write a Great Research Paper: Seven Simple Suggestions*
- **Author / Affiliation**: Simon Peyton Jones (Microsoft Research, Cambridge / Engineering Fellow, Epic Games)
- **Platform / Venue**: Official Author Page, Microsoft Research Academic Program, & *2017 Imperial College Computing Student Workshop (ICCSW 2017)*, OASIcs Vol. 60 (CC-BY 3.0)
- **Verified URLs**:
  - `https://simon.peytonjones.org/great-research-paper/`
  - `https://www.cis.upenn.edu/~sweirich/icfp-plmw15/slides/peyton-jones.pdf` (52-slide deck verified via OCR)
  - `https://drops.dagstuhl.de/entities/document/10.4230/OASIcs.ICCSW.2017.1` (DOI: `10.4230/OASIcs.ICCSW.2017.1`)

#### Verbatim Core Thesis & Seven Guidelines (Slides 1–46)
1. **#1 Don't wait: write** (Slides 2–5):
   - Reject `"Idea -> Do research -> Write paper"` in favor of `"Idea -> Write paper -> Do research"`.
   - *"Writing papers is a primary mechanism for **doing** research (not just for **reporting** it)."*
   - *"Forces us to be clear, focused; Crystallises what we don't understand; Opens the way to dialogue with others: reality check, critique, and collaboration."*
2. **#2 Identify your key idea** (Slides 6–11):
   - *"Your goal: to convey a useful and re-usable idea. You want to infect the mind of your reader with your idea, like a virus."*
   - *"Your paper should have just one 'ping': one clear, sharp idea. You may not know exactly what the ping is when you start writing; but you must know when you finish. If you have lots of ideas, write lots of papers."*
   - *"Make certain that the reader is in no doubt what the idea is. Be 100% explicit: 'The main idea of this paper is....'"*
3. **#3 Tell a story** (Slides 12–16):
   - **Whiteboard narrative flow**: *"Imagine you are explaining at a whiteboard: Here is a problem -> It's an interesting problem -> It's an unsolved problem -> Here is my idea -> My idea works (details, data) -> Here's how my idea compares to other people's approaches."*
   - **Conference paper readership funnel** (Slide 14):
     - Title (`1000 readers`) -> Abstract (`4 sentences, 100 readers`) -> Introduction (`1 page, 100 readers`) -> The problem (`1 page, 10 readers`) -> My idea (`2 pages, 10 readers`) -> The details (`5 pages, 3 readers`) -> Related work (`1-2 pages, 10 readers`) -> Conclusions and further work (`0.5 pages`).
   - **Kent Beck's Four-Sentence Abstract** (Slide 15):
     1. *"State the problem"*
     2. *"Say why it's an interesting problem"*
     3. *"Say what your solution achieves"*
     4. *"Say what follows from your solution"*
4. **#4 Nail your contributions to the mast** (Slides 17–26):
   - **The 1-page Introduction**: *"1. Describe the problem. 2. State your contributions ...and that is all. ONE PAGE! Use an example to introduce the problem."*
   - **"Molehills not mountains" (Author's verbatim opener contrast, Slide 21)**:
     - **Yawn**: *"Computer programs often have bugs. It is very important to eliminate these bugs [1,2]. Many researchers have tried [3,4,5,6]. It really is very important."*
     - **Cool!**: *"Consider this program, which has an interesting bug. \<brief description\>. We will show an automatic technique for identifying and removing such bugs."*
   - **Contributions should be refutable — Author's Verbatim NO/YES Table (Slide 24)**:

     | NO! (Unrefutable / Vague) | YES! (Refutable & Forward-Referenced) |
     |---|---|
     | *"We describe the WizWoz system. It is really cool."* | *"We give the syntax and semantics of a language that supports concurrent processes (Section 3). Its innovative features are..."* |
     | *"We study its properties"* | *"We prove that the type system is sound, and that type checking is decidable (Section 4)"* |
     | *"We have used WizWoz in practice"* | *"We have built a GUI toolkit in WizWoz, and used it to implement a text editor (Section 5). The result is half the length of the Java version."* |

   - **Ban boilerplate roadmap paragraphs (Slide 26)**:
     - **Not**: *"The rest of this paper is structured as follows. Section 2 introduces the problem. Section 3 ... Finally, Section 8 concludes."*
     - **Instead**: *"Use forward references from the narrative in the introduction. The introduction (including the contributions) should survey the whole paper, and therefore forward reference every important part."*
5. **#5 Related work: later** (Slides 27–33):
   - Do not place Related Work between the reader and your idea (Slide 29: *"Problem 1: the reader knows nothing about the problem yet; so your (highly compressed) description of various technical tradeoffs is absolutely incomprehensible. Problem 2: describing alternative approaches gets between the reader and your idea."*).
   - **Credit is not like money** (Slides 31–33): *"Fallacy: To make my work look good, I have to make other people's work look bad. The truth: Giving credit to others does not diminish the credit you get from your paper. Warmly acknowledge people who have helped you. Be generous to the competition. Acknowledge weaknesses in your approach. Failing to give credit to others can kill your paper."*
6. **#6 Put your readers first** (Slides 34–40):
   - *"Explain it as if you were speaking to someone using a whiteboard. Conveying the intuition is primary, not secondary. Introduce the problem, and your idea, using EXAMPLES and only then present the general case."*
   - *"Do not recapitulate your personal journey of discovery. This route may be soaked with your blood, but that is not interesting to the reader. Instead, choose the most direct route to the idea."*
7. **#7 Listen to your readers & reviewers** (Slides 41–45):
   - *"Get your paper read by as many friendly guinea pigs as possible... Explain carefully what you want ('I got lost here' is much more important than 'Jarva is mis-spelt')."*
   - *"Treat every review like gold dust. Be (truly) grateful for criticism as well as praise... Read every criticism as a positive suggestion for something you could explain more clearly. DO NOT respond 'you stupid person, I meant X'. Fix the paper so that X is apparent even to the stupidest reader."*

#### Verbatim Language & Style Tables (Slides 51–52)
- **Use the active voice** (*"The passive voice is 'respectable' but it DEADENS your paper. Avoid it at all costs."*):

  | NO | YES |
  |---|---|
  | *"It can be seen that..."* | *"We can see that..."* (`"We"` = you and the reader) |
  | *"34 tests were run"* | *"We ran 34 tests"* (`"We"` = the authors) |
  | *"These properties were thought desirable"* | *"We wanted to retain these properties"* |
  | *"It might be thought that this would be a type error"* | *"You might think this would be a type error"* (`"You"` = the reader) |

- **Use simple, direct language**:

  | NO | YES |
  |---|---|
  | *"The object under study was displaced horizontally"* | *"The ball moved sideways"* |
  | *"On an annual basis"* | *"Yearly"* |
  | *"Endeavour to ascertain"* | *"Find out"* |
  | *"It could be considered that the speed of storage reclamation left something to be desired"* | *"The garbage collector was really slow"* |

---

### 1.2 Brett Mensh & Konrad Kording (2017) — *Ten Simple Rules for Structuring Papers*
- **Authors / Affiliations**: Brett Mensh (HHMI Janelia Research Campus / Optimize Science) & Konrad Kording (University of Pennsylvania / Northwestern University)
- **Journal**: *PLOS Computational Biology* 13(9): e1005619 (Published September 28, 2017; CC-BY Open Access)
- **Verified URL**: `https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619` (DOI: `10.1371/journal.pcbi.1005619`)

#### Verbatim Ten Rules & Multi-Scale Structural Mechanics
1. **Rule 1: Focus your paper on a central contribution, which you communicate in the title**
   - *"Focus on a single message; papers that simultaneously focus on multiple contributions tend to be less convincing about each and are therefore less memorable."*
2. **Rule 2: Write for flesh-and-blood human beings who do not know your work**
   - *"Because you are the world's leading expert at exactly what you are doing, you are also the world's least qualified person to judge your writing from the perspective of the naïve reader... Define technical terms clearly... Avoid abbreviations and acronyms so that readers do not have to go back to earlier sections to identify them... Do your best to minimize the number of loose threads that the reader has to keep in mind at any one time."*
3. **Rule 3: Stick to the context-content-conclusion (C-C-C) scheme**
   - *"This structure reduces the chance that the reader will wonder 'Why was I told that?' (if the context is missing) or 'So what?' (if the conclusion is missing)."*
   - **Multi-scale application**: *"At the whole-paper scale, the introduction sets the context, the results are the content, and the discussion brings home the conclusion. Applying C-C-C at the paragraph scale, the first sentence defines the topic or context, the body hosts the novel content put forth for the reader's consideration, and the last sentence provides the conclusion to be remembered."*
   - **Ban chronological lab-diary structure**: *"They do not care about the chronological path by which you reached a result; they just care about the ultimate claim and the logic supporting it."*
4. **Rule 4: Optimize your logical flow by avoiding zig-zag and using parallelism**
   - **Avoiding zig-zag**: *"Only the central idea of the paper should be touched upon multiple times. Otherwise, each subject should be covered in only one place in order to minimize the number of subject changes."*
   - **Using parallelism & banning synonym-cycling ("elegant variation")**: *"Across consecutive paragraphs or sentences, parallel messages should be communicated with parallel form... There is nothing wrong with using the same word multiple times in a sentence or paragraph. Resist the temptation to use a different word to refer to the same concept—doing so makes readers wonder if the second word has a slightly different meaning."*
5. **Rule 5: Tell a complete story in the abstract**
   - Broad-narrow-broad C-C-C arc: **Context** (orient broader field -> narrow to specific gap in literature and why it matters) -> **Content** (*"Here we"* novel method + executive summary of results) -> **Conclusion** (interpret results to answer the gap question + broader significance).
6. **Rule 6: Communicate why the paper matters in the introduction**
   - Progressive gap funnel (field gap -> subfield gap -> specific untested gap) where each paragraph moves from *"knowns"* to the critical *"unknown"*, ending with a final summary paragraph of how the paper fills that gap. *"The introduction should not contain a broad literature review beyond the motivation of the paper."*
7. **Rule 7: Deliver the results as a sequence of statements, supported by figures, that connect logically to support the central contribution**
   - Convert logical steps into **declarative subsection headers** and **conclusion-stating figure titles**. Each results paragraph opens with the question tested, presents data/logic in the middle, and closes with a sentence answering that question.
8. **Rule 8: Discuss how the gap was filled, the limitations of the interpretation, and the relevance to the field**
   - First paragraph summarizes key findings and meaning; middle paragraphs evaluate strengths/limitations linked to literature; final paragraph explains how the contribution moves the field forward.
9. **Rule 9: Allocate time where it matters: Title, abstract, figures, and outlining**
   - *"Write one informal sentence for each planned paragraph... scrutinize at the outline stage in order to reduce wasting time on wordsmithing paragraphs that don't end up fitting within the overall story."*
10. **Rule 10: Get feedback to reduce, reuse, and recycle the story**
    - *"In many cases, trashing entire paragraphs and rewriting is a faster way to produce good text than incremental editing... Non-specific feedback and unenthusiastic reviews often imply that the reviewers did not 'get' the big picture story line."*

---

### 1.3 Zachary C. Lipton & Jacob Steinhardt (2018) — *Troubling Trends in Machine Learning Scholarship*
- **Authors / Affiliations**: Zachary C. Lipton (Carnegie Mellon University) & Jacob Steinhardt (UC Berkeley / Stanford)
- **Venue**: *ICML 2018: The Debates* / *Communications of the ACM* / arXiv:1807.03341
- **Verified URLs**:
  - `https://arxiv.org/abs/1807.03341` (DOI: `10.48550/arXiv.1807.03341`)
  - `https://www.approximatelycorrect.com/2018/07/10/troubling-trends-in-machine-learning-scholarship/index.html`

#### Four Documented Scholarly Pathologies & Verbatim Remedies
1. **Conflating Explanation and Speculation (§3.1)**:
   - Offering unvalidated intuitions in the authoritative guise of technical explanations (e.g., citing *"internal covariate shift"* as established fact without defining a divergence metric).
   - **Positive exemplar cited by authors**: Quarantine informal intuitions explicitly inside a designated `"Motivation"` section (as Srivastava et al. did for dropout) or explicitly qualify unvalidated heuristics (as Bengio 2012 did).
2. **Failure to Identify the Sources of Empirical Gains (§3.2)**:
   - Bundling multiple architectural tweaks without ablation studies when gains actually stem from hyperparameter tuning or stronger baselines (citing Melis et al. on vanilla LSTMs).
   - **Author recommendation (§5.1)**: Ask *"what worked?"* and *"why?"* rather than just *"how well?"*, backed by **error analysis, ablation studies, and robustness checks**.
3. **Mathiness (§3.3)**:
   - Quoting Paul Romer [64]: *"Like mathematical theory, mathiness uses a mixture of words and symbols, but instead of making tight links, it leaves ample room for slippage between statements in natural language versus formal language."*
   - Manifestations: (a) spurious theorems inserted *"to bulldoze rather than to clarify"*, (b) claims that are neither clearly formal nor clearly informal, and (c) dubious passing invocations of broad theorems (e.g., No Free Lunch).
   - **Verbatim Diagnostic Test (§5.1)**: *"When writing, we recommend asking the following question: **Would I rely on this explanation for making predictions or for getting a system to work?** This can be a good test of whether a theorem is being included to please reviewers or to convey actual insight."*
4. **Misuse of Language (§3.4)**:
   - **Suggestive / Anthropomorphic Definitions (§3.4.1)**: Coining technical terms with colloquial human connotations (*"reading comprehension"*, *"curiosity"*, *"fear"*, *"thought vectors"*, *"consciousness prior"*, unqualified *"dermatologist-level"* claims on i.i.d. test sets).
   - **Overloading Technical Terminology (§3.4.2)**: Reusing established mathematical terms imprecisely or contradictorily (e.g., calling transpose convolution *"deconvolution"*, calling conditional discriminative structured predictors *"generative models"*, or redefining *"covariate shift"*).
   - **Suitcase Words (§3.4.3, after Marvin Minsky 2007)**: Packing disjoint meanings into undefined umbrella words (*"interpretability"*, *"generalization"*, *"bias"*, *"intelligence"*) inside technical claims.

---

### 1.4 Jennifer Widom (Stanford InfoLab) — *Tips for Writing Technical Papers*
- **Author / Affiliation**: Prof. Jennifer Widom (Stanford University, Computer Science)
- **Platform**: Stanford InfoLab Technical Writing Notes
- **Verified URL**: `https://cs.stanford.edu/people/widom/paper-writing.html`

#### Verbatim Structural & Micro-Prose Rules
- **Stanford InfoLab Five-Point Introduction Structure** (5 paragraphs answering 5 questions + bulleted `"Summary of Contributions"` with section pointers):
  1. *"What is the problem?"*
  2. *"Why is it interesting and important?"*
  3. *"Why is it hard? (E.g., why do naive approaches fail?)"*
  4. *"Why hasn't it been solved before? (Or, what's wrong with previous proposed solutions? How does mine differ?)"*
  5. *"What are the key components of my approach and results? Also include any specific limitations."*
- **Body Guideline #1**: *"A clear new important technical contribution should have been articulated by the time the reader finishes page 3 (i.e., a quarter of the way through the paper)."*
- **Body Guideline #2**: *"Every section of the paper should tell a story. (Don't, however, fall into the common trap of telling the entire story of how you arrived at your results. Just tell the story of the results themselves.)"*
- **Abstract & Conclusions Non-Repetition**: *"The material in the abstract should not be repeated later word for word in the paper... Under no circumstances should the [Conclusions] paragraph simply repeat material from the Abstract or Introduction."*
- **Grammar & Small-Scale Pet Peeves**:
  - **Define variables/terms once**: *"Just like a program, all 'variables' (terminology and notation) in the paper should be defined before being used, and should be defined only once."*
  - **Ban vague `"etc."`**: *"Do not use 'etc.' unless the remaining items are completely obvious. Acceptable: `We shall number the phases 1, 3, 5, 7, etc.` Unacceptable: `We measure performance factors such as volatility, scalability, etc.`"*
  - **Ban `"for various reasons"`**: *"Never say 'for various reasons'... Tell the reader the reasons!"*
  - **Ban nonreferential `"this"` / `"that"` / `"these"` / `"it"` (Jeff Ullman's rule)**: *"Requiring explicit identification of what 'this' refers to enforces clarity of writing."*

---

### 1.5 Verified Open-Source Academic De-AI Skills (`../upstream-skills/`)
1. **`AIScientists-Dev/academic-humanizer`** (`5,909★`, MIT, commit `94b88b23703bed7df507acae7d6d5876209a0cdf`)
   - **Verified URL**: `https://github.com/AIScientists-Dev/academic-humanizer` | **Local Verbatim Copy**: `../upstream-skills/04-genres-academic-tech-social/academic-humanizer/SKILL.md`
   - **Verbatim Core Principle (`SKILL.md` L31–34)**: *"Academic writing already has a correct human voice: neutral, precise, third-person plural ('we'), every claim tied to its evidence. The job is to (1) strip the AI tells without casualizing, and (2) enforce the discipline a general humanizer misses: **every claim earns its number, figure, or citation, and no verb is stronger than its evidence.**"*
   - **Documented Academic AI-Tell Layers (`SKILL.md` Layer 2)**:
     - `2.1 Over-claiming verbs`: *demonstrate, prove, establish, confirm, guarantee; "significantly" with no test/number* -> replace with exact point gain, table reference, and $p$-value.
     - `2.2 Significance hype`: *paves the way for, a crucial/pivotal step toward, has the potential to revolutionize, opens new avenues, sheds light on, of paramount importance, bridges the gap*.
     - `2.3 Empty intensifiers`: *extensive/comprehensive/thorough experiments, a wide range of, numerous, various* -> name the exact datasets (`ImageNet, CIFAR-100, and iNaturalist`).
     - `2.4 Novelty padding`: *"novel" used more than once per section; "to the best of our knowledge"; "for the first time"*.
     - `2.5 Formulaic openers`: *"In recent years, X has attracted increasing attention"; "With the rapid development of..."; "Despite recent advances,..."*.
     - `2.6 Connective overuse`: Starting consecutive sentences with *Moreover / Furthermore / Additionally / In particular*.
     - `2.7 Contribution-list cliches`: Generic *"(1) a novel method; (2) extensive experiments; (3) strong results"* instead of specific metric/ablation numbers.
     - `2.8 Citation dumping`: *"Many methods exist [3, 7, 9, 12, 15]"* instead of naming the closest prior method and exact contrast.
2. **`zczjyq/de-AIGC-skill`** (`34★`, commit `8bf27b8db57e54fd7f1c1bc5d698480e935fc193`)
   - **Verified URL**: `https://github.com/zczjyq/de-AIGC-skill` | **Local Verbatim Copy**: `../upstream-skills/04-genres-academic-tech-social/de-AIGC-skill/SKILL.md`
   - **Documented Chinese Thesis De-AIGC Rules (`SKILL.md` L44–102)**:
     - **保量润色原则 (Length-Preserving Polish)**: Readable Chinese character count must stay **$\ge 92\%$** of the original (never slash evidence/derivations just to game detectors).
     - **中文术语后禁止冗余英文括号**: Avoid AI-style repeated parenthetical glosses like `暗通道先验（Dark Channel Prior, DCP）` on every mention; register defined terms/symbols once in `session-memory/` and maintain rolling section summaries (`已处理段落摘要`) to prevent cross-section contradiction while protecting LaTeX commands (`\ref`, `\cite`, math environments).
3. **Additional Cloned Academic Writing & Review Skills in `../upstream-skills/`** (see [SOURCES_CATALOG.md](SOURCES_CATALOG.md) for full file manifests & SHAs):
   - [`WenyuChiou/academic-writing-skills`](https://github.com/WenyuChiou/academic-writing-skills) (`../upstream-skills/04-genres-academic-tech-social/academic-writing-skills/`)
   - [`YuanZHAO321/Scientific-Writing-zh`](https://github.com/YuanZHAO321/Scientific-Writing-zh) (`../upstream-skills/04-genres-academic-tech-social/Scientific-Writing-zh/`)
   - [`Orchestra-Research/AI-Research-SKILLs`](https://github.com/Orchestra-Research/AI-Research-SKILLs) (`../upstream-skills/04-genres-academic-tech-social/AI-Research-SKILLs-paper-writing/`)
   - [`zLanqing/codex-claude-academic-skills`](https://github.com/zLanqing/codex-claude-academic-skills) (`../upstream-skills/04-genres-academic-tech-social/codex-claude-academic-skills/`)
   - [`dengzhe-hou/research-writing-prompts`](https://github.com/dengzhe-hou/research-writing-prompts) (`../upstream-skills/04-genres-academic-tech-social/research-writing-prompts/`)
   - [`xf686/Meet-Reviewer-2`](https://github.com/xf686/Meet-Reviewer-2) (`../upstream-skills/04-genres-academic-tech-social/Meet-Reviewer-2/`)

---

### 1.6 Peer-Review & Rebuttal Polishing — Published Scholar Guides & Chinese实战贴

#### A. Frédo Durand (MIT CSAIL) & Ramesh Raskar — *Rebuttal Advice (Do's and Don'ts)*
- **Verified URL**: `https://people.csail.mit.edu/fredo/rebuttal_advice.txt`
- **Verbatim Rules**:
  - *"Be concise. Program committee members have 20 rebuttals to read. Make it easy to find information. Have section titles."*
  - *"Do not quote the criticisms from the reviews. No need to have the PC members read negative points an extra time. Instead, label your section with the positive answer to the point."*
  - *"Do not say 'it may seem trivial but it was hard'. Do not say 'reviewer XXX asks if...' Just give the answer."*
  - *"Don't whine. Don't complain that you could not address XXX because it involves too much work."*
  - *"If a reviewer asks for info, don't refer them to another paper: provide the info!"*
  - *"Don't mention a final version: you imply it's already accepted. A good compromise is to say 'a revised version'."*
  - *"Avoid long tedious intros (thank you blah blah.... we will address blah blah...). Maybe simply: `We thank the reviewers for their thorough comments.` ... No conclusion. No `we'll be happy to address further questions`."*
  - *"Avoid 'we acknowledge' (which makes it sound like you are at fault) and say 'we agree'."*
  - *"Your goal at this stage is to give supportive reviewers enough ammunition so that they can convince the others."*

#### B. Andreas Zeller (CISPA / Saarland University) — *Patterns for Writing Good Rebuttals*
- **Verified URL**: `https://andreas-zeller.info/2012/10/01/patterns-for-writing-good-rebuttals.html`
- **Verbatim Patterns**:
  - **Identify the undecided / Identify & Arm the champion**: Focus persuasion on undecided reviewers and arm your champion with concrete refutations of every detractor point.
  - **Write for the PC chair**: Stick to facts checkable in under 1 minute (*"reviewer claims 'no Foo' when Section 3 is named 'All about Foo'"*). *"If all reviewers misunderstood your paper, the problem is not the reviewers."*
  - **Convince (Show, don't promise)**: *"If the reviewer asks: 'Do you have a formal definition of Foo?', don't say 'Yes'. But don't say 'Thanks! We'll add this.' either. Say: **'A Foo is a Bar within a Qux range; we'll add a detailed definition.'**"*
  - **Choose comments wisely**: Focus on major concerns where reviewers doubt you can fix the paper; do not waste space promising to fix typos.
  - **No tricks**: Never game word/character limits by replacing spaces with underscores or impenetrable acronyms.

#### C. Maarten Sap (CMU, learned from Yejin Choi & Noah Smith) — *Writing Rebuttals*
- **Verified URL**: `https://maartensap.com/notes/05-rebuttals.html`
- **Verbatim Workflow & Framing Rules**:
  - **First read**: Color-code reviews in a doc (Green = positive snippets, Red = negative, Orange = addressable), launch quick data analyses immediately, *"Draft an angry response. Then, sleep on it!"*
  - **Promise clarifications rather than "correcting" the reviewer**: Use *"we'll clarify [something that we already wrote in the paper] in the final version"*.
  - **Positive Action Headers**: *"Headers should summarize the rebuttal point, not the weakness/question. For example, say **'Clarifying the statistical significance of our findings'** instead of **'Are the findings significant?'**"*
  - **AC Confidential Note**: Flag ARR-documented reviewing biases such as *"lazy thinking"* (`https://aclrollingreview.org/reviewertutorial#6-check-for-lazy-thinking`) respectfully to the Area Chair.

#### D. 魏秀参 (Wei Xiu-Shen) — 《浅谈学术论文 rebuttal》（知乎专栏 / 腾讯云开发者社区授权转载）
- **Author**: 魏秀参博士（旷视南京研究院负责人 / 教授）
- **Verified URLs**: `https://zhuanlan.zhihu.com/p/104298923` | Mirror: `https://developer.cloud.tencent.com/article/1588193`
- **Verbatim Core Principles & Empirical Data**:
  - **「知彼解己原则」**：*“首先去了解对方，然后再争取让对方了解自己”*——约 50% 以上审稿人在 deadline 最后三天内完成评审（引自 NAACL-HLT 2019 Gao et al.），需站在审稿人与 AC 视角排兵布阵，逐点回应、切忌漏点。
  - **四类核心质疑拆解**：
    1. **喷「novelty」**：重新梳理贡献，澄清并非 trivial 简单拼接，强调独特 intuition/insight，或「围魏救赵」突出整体范式简洁有效。
    2. **喷「factual error」**：若确系笔误大方致谢并承诺更正；若因表述不清导致误解，回应 *“我们已经修改了这部分描述，实际上是这样做的……”*；若审稿人自身出现事实性错误，在回复开头与 AC Message 中礼貌指出以降低其负面意见在 AC 心中的置信度。
    3. **喷「涨点不足」**：无证据裸喷则列举同期顶会 SOTA 涨点幅度证明可比；带参考文献质疑则指出实验设置差异（如输入分辨率、backbone 不同）。
    4. **喷「实验不足」**：能补则直接补表/图；周期内无法完成则说明客观原因并承诺修订版补充；不合理实验则实事求是阐明边界。
  - **CVPR 2019 超 15,000 条审稿意见 Rebuttal 前后真实统计（原文数据）**：
    - 「逆天改命」（Strong Reject $\to$ Positive）：**0.8%**
    - 「强势逆转」（Weak Reject $\to$ Positive）：**6.9%**
    - 「力挽狂澜」（Borderline $\to$ Positive）：**33.6%**
    - 「错失良机」（Borderline $\to$ Negative）：**约 56%**
    - 「画蛇添足」（Weak Accept $\to$ Negative）：**15.5%**
    - 「弄巧成拙」（Strong Accept $\to$ Negative）：**5.2%**
  - **Cloned Rebuttal Skills in `../upstream-skills/`**:
    - [`MLNLP-World/Paper-Rebuttal-Tips`](https://github.com/MLNLP-World/Paper-Rebuttal-Tips) (`../upstream-skills/04-genres-academic-tech-social/Paper-Rebuttal-Tips/` — 28 AI/LLM rebuttal scenarios + `paper-rebuttal-skill`)
    - [`yuangao-tum/rebuttal-skills`](https://github.com/yuangao-tum/rebuttal-skills) (`../upstream-skills/04-genres-academic-tech-social/rebuttal-skills/` — `write-rebuttal` + 28 `nlp-rebuttal` templates)

#### E. 牛客网网友实测分享 — 《【未来准备9】GitHub项目：去除AI味的Prompt》
- **Author / Platform**: `sagima`（山东大学，牛客网讨论帖，2025-04-23）
- **Verified URL**: `https://www.nowcoder.com/discuss/744582593399578624`
- **Netizen Reported Empirical Test**: Tested on **Gemini 2.5 Pro** (reasoning mode) evaluated against **腾讯朱雀大模型检测**: rewriting 5,000 characters reduced detected AI rate from **~70% to ~17%**; targeted local rewrites pushed it lower.
- **Verbatim Shared Prompt Excerpt (from `sagima` post)**:
  > **Guidelines for Humanization**:
  > 1. **句式灵动**：告别死板。长短结合，并列、从句、口语化表达交替使用。
  > 2. **词汇鲜活**：拒绝模板化。用具体、形象、有温度的词替换中性、抽象、生硬的词。多用动词，少用被动。
  > 3. **自然过渡**：抛弃“首先/其次/总之”。使用更隐性、符合思维流的连接方式（如“说到这里”、“另一方面”、“更重要的是”、“回过头来看”等）。
  > 4. **视角与情感**：适度引入……**展示而非说教 (Show, don't tell)**。
  > 7. **避免 AI 习语**：坚决去除“值得注意的是”、“不难发现”、“基于以上分析”等高频 AI 特征短语。
  > **Constraints**: 核心信息、关键数据不得篡改或遗漏；避免过度修饰或炫技。


---

## Genre 2: Technical Blogs, READMEs & Developer Documentation

### 2.1 Google Developer Documentation Style Guide — *Highlights* & *Active Voice*
- **Author / Organization**: Google for Developers (Licensed under CC-BY 4.0)
- **Verified URLs**:
  - `https://developers.google.com/style/highlights`
  - `https://developers.google.com/style/voice`

#### Verbatim Developer Documentation Rules
- **Tone and Content (`highlights`)**:
  - *"Be conversational and friendly without being frivolous."*
  - *"Don't pre-announce anything in documentation."*
  - *"Use descriptive link text."*
  - *"Write accessibly. Write for a global audience."*
- **Language and Grammar (`highlights` & `voice`)**:
  - *"Use second person: `'you'` rather than `'we.'`"*
  - *"Use active voice: make clear who's performing the action."*
  - *"Put conditions before instructions, not after."*
  - **Google's Verbatim Active-vs-Passive Comparison (`voice`)**:
    - **Recommended**: *"Send a query to the service. The server sends an acknowledgment."*
    - **Not recommended**: *"The service is queried, and an acknowledgment is sent."* / *"The service is queried by you, and an acknowledgment is sent by the server."*
  - **Three Documented Exceptions Where Passive Voice Is Appropriate (`voice`)**:
    1. *To emphasize an object over an action*: `"The file is saved."`
    2. *To de-emphasize a subject or actor (avoiding blaming the user)*: Recommended `"Over 50 conflicts were found in the file."` vs Not recommended `"You created over 50 conflicts in the file."`
    3. *If readers don't need to know who's responsible for the action*: `"The database was purged in January."`
- **Formatting, Punctuation, and Organization (`highlights`)**:
  - *"Use sentence case for document titles and section headings."*
  - *"Use numbered lists for sequences. Use bulleted lists for most other lists. Use description lists for pairs of related pieces of data."*
  - *"Use serial commas. Put code-related text in code font. Put UI elements in bold. Use unambiguous date formatting."*

---

### 2.2 Daniele Procida — *Diátaxis Technical Documentation Framework*
- **Author**: Daniele Procida
- **Platform**: Official Diátaxis Specification
- **Verified URLs**: `https://diataxis.fr/` | `https://diataxis.fr/start-here/`

#### Verbatim Four-Quadrant Architecture (Eliminating Mixed-Mode AI Doc Slop)
- *"Diátaxis identifies four distinct needs, and four corresponding forms of documentation — **tutorials**, **how-to guides**, **technical reference** and **explanation**. It places them in a systematic relationship, and proposes that documentation should itself be organised around the structures of those needs."*
  1. **Tutorials** (*learning-oriented*): Lessons that take the learner safely through a practical experience.
  2. **How-to guides** (*task/problem-oriented*): Practical step-by-step directions showing a competent user how to solve a real-world problem.
  3. **Technical Reference** (*information-oriented*): Austere, accurate technical descriptions of machinery, APIs, and parameters.
  4. **Explanation** (*understanding-oriented*): Discursive context, architecture rationale, trade-offs, and background.
- **Documented Adopters Quoted on `diataxis.fr`**: Cloudflare developer docs (Adam Schwartz), Gatsby open-source docs (Megan Sullivan), Vonage internal docs (Greg Frileux).

---

### 2.3 Paul Graham — *Write Simply* (2021) & *Writing, Briefly* (2005)
- **Author**: Paul Graham (Y Combinator Co-founder & Essayist)
- **Verified URLs**:
  - *Write Simply* (March 2021): `https://paulgraham.com/simply.html`
  - *Writing, Briefly* (March 2005): `https://paulgraham.com/writing44.html`

#### Verbatim Prose Principles
- **From *Write Simply* (`https://paulgraham.com/simply.html`)**:
  - *"I try to write using ordinary words and simple sentences. That kind of writing is easier to read, and the easier something is to read, the more deeply readers will engage with it. The less energy they expend on your prose, the more they'll have left for your ideas."*
  - **Saltintesta**: *"My goal when writing might be called saltintesta: the ideas leap into your head and you barely notice the words that got them there."*
  - **Anti-pretension & Honesty**: *"When you write in a fancy way to impress people, you're making them do extra work just so you can seem cool. It's like trailing a long train behind you that readers have to carry... Of course, fancy writing doesn't just conceal ideas. It can also conceal the lack of them. Whereas writing simply keeps you honest. If you say nothing simply, it will be obvious to everyone, including you."*
  - **Global / ESL Readership**: *"Remember, if you're writing in English, that a lot of your readers won't be native English speakers. Their understanding of ideas may be way ahead of their understanding of English. So you can't assume that writing about a difficult topic means you can use difficult words."*
  - **Draft fast, edit by cutting**: *"I write the first draft fast, then spend days editing it, trying to get everything just right. Much of this editing is cutting, and that makes simple writing even simpler."*
- **From *Writing, Briefly* (`https://paulgraham.com/writing44.html`)**:
  - *"Write a bad version 1 as fast as you can; rewrite it over and over; cut out everything unnecessary; write in a conversational tone; develop a nose for bad writing, so you can see and fix it in yours... if you can't get started, tell someone what you plan to write about, then write down what you said; expect 80% of the ideas in an essay to happen after you start writing it, and 50% of those you start with to be wrong... don't try to sound impressive; use footnotes to contain digressions; use anaphora to knit sentences together; **read your essays out loud to see (a) where you stumble over awkward phrases and (b) which bits are boring (the paragraphs you dread reading)**... write for a reader who won't read the essay as carefully as you do, just as pop songs are designed to sound ok on crappy car radios... **use simple, germanic words**; learn to distinguish surprises from digressions; learn to recognize the approach of an ending, and when one appears, grab it."*

---

### 2.4 Eugene Yan — *How to Write Better with The Why, What, How Framework* & *ML Design Docs*
- **Author**: Eugene Yan (Applied Scientist, Amazon)
- **Verified URLs**:
  - `https://eugeneyan.com/writing/writing-docs-why-what-how/`
  - `https://eugeneyan.com/writing/ml-design-docs/`

#### Verbatim Engineering Document Spine & Audience Alignment
- **Three Core Engineering Artifacts**:
  1. **One-pagers** (stakeholder alignment & scope-creep guardrails)
  2. **Design docs** (methodology, system context diagrams, offline ML metrics & p99 latency/throughput benchmarks, plus explicit **out-of-scope** boundaries)
  3. **After-action reviews / Correction of Errors** (blameless 5-Whys root-cause diagnosis, customer/revenue impact, and owned follow-up actions)
- **Author's Verbatim Bad-vs-Good `"Why"` Framing (`https://eugeneyan.com/writing/writing-docs-why-what-how/`)**:
  - **Loses business audience immediately**: *"We need to procure GPU clusters for distributed training of SOTA deep learning models that will improve nDCG@10 by 20%."*
  - **Aligned to reader's terms**: *"We need to invest in infrastructure to improve customer recommendations, with an expected conversion and revenue uplift of 5%."*

---

### 2.5 Julia Evans (`jvns.ca`) — Authentic Technical Blogging Guides
- **Author**: Julia Evans (Creator of *Wizard Zines* & `jvns.ca`)
- **Verified URLs**:
  - *Blog about what you've struggled with* (May 24, 2021): `https://jvns.ca/blog/2021/05/24/blog-about-what-you-ve-struggled-with/`
  - *Some blogging myths* (June 5, 2023): `https://jvns.ca/blog/2023/06/05/some-blogging-myths/`

#### Verbatim Practitioner Rules for Non-Generic Technical Blogs
- **Anchor on Real Debugging / Learning Struggles (`blog-about-what-you-ve-struggled-with`)**:
  - *"Struggle with something (usually computer-related) -> Eventually (days or months or years later), figure out how to solve some of the problems I had -> Write a blog post about what helped me."*
  - *"It's not about the struggle, it's about what you learned... If I instead think about what I've struggled with Go, it suddenly gets MUCH clearer – one thing I've had trouble with is deadlocks! That's way more specific, and a lot more likely to be useful to other people than an intro to Go modules."*
  - *"Write it down while you still remember what was hard."*
- **Concrete Personal Stories Over Timeless Generalities (`some-blogging-myths`)**:
  - *"Technology changes, and the details matter... I would love to read 1 person's story of exactly how they did it in 2023."*
- **Honest Epistemic Qualifiers Instead of False AI Omniscience (`some-blogging-myths`)**:
  - *"My main strategy here is to just add qualifiers like `'My understanding is..'` or `'I think..'` before statements that I'm not totally sure of."* (Author's verbatim examples: *"I think the MTU on my local network is 1500 bytes."* / *"So far my understanding is that there are 2 route table entries you need to set..."*)
- **Write for One Specific Person (`some-blogging-myths`)**:
  - *"It's common for people writing advanced posts (like 'how malloc works') to try to include very basic definitions for beginners. The problem is that you end up writing something that feels like it wasn't written for anyone: beginners will get confused... and more advanced readers will be bored... **The easiest way to start was to pick one person and write for them** (a friend, a coworker, or just a past version of yourself)."*

---

### 2.6 Hacker News Practitioner Thread — *Ask HN: What Are the Best Engineering Blogs with Real-World Depth?*
- **Platform**: Hacker News (`item?id=46363921`, Dec 23, 2025)
- **Verified URL**: `https://news.ycombinator.com/item?id=46363921`
- **Verbatim Engineer Takeaways & Live AI-Tell Callouts**:
  - **Grounded ground-up depth (`yrand`, `https://news.ycombinator.com/item?id=46364152`)**: *"A badly written article usually either goes really shallow or skips some facts when going into depth and requires catchup elsewhere to actually understand it."*
  - **Zero-fluff technical writing (`nchmy`, `https://news.ycombinator.com/item?id=46364190`)**: Citing `https://infrequently.org` (Alex Russell): *"There's zero fluff and considerable detail (footnotes are practically blog posts themselves)."*
  - **Practitioner-endorsed deep engineering blogs cited across the thread**: Google Project Zero (`projectzero.google`), Cloudflare Blog (`blog.cloudflare.com`), Tailscale (`tailscale.com/blog`), Stripe Engineering (`stripe.com/blog/engineering`), Armin Ronacher (`lucumr.pocoo.org`), Antirez (`antirez.com`), Simon Willison (`simonwillison.net`), Michał Zalewski (`lcamtuf.substack.com`), Raymond Chen's *The Old New Thing*.
  - **Real-world HN reader reaction to LLM-formatted questions (`mitjam`, `https://news.ycombinator.com/item?id=46364307` & `vibesareoff`, `https://news.ycombinator.com/item?id=46364394`)**: When the OP used an em-dash + tidy 4-point numbered rubric, commenters immediately replied: *"Maybe it's just because I'm LLMing a bit too much, recently, but this question sounds to me like a prompt."* / *"Ask the LLM you wrote this post with!"*

---

### 2.7 Verified Open-Source Technical Docs & README Skills (`../upstream-skills/`)
1. **Anthropic Official `doc-coauthoring` Skill** (`199,160★`, commit `e4bb5d960d87126ff3b3a8af1a104b7db67560ba`)
   - **Verified URL**: `https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring` | **Local Verbatim Copy**: `../upstream-skills/05-visual-image-figure-and-ui/anthropics-skills/skills/doc-coauthoring/SKILL.md`
   - Three-stage workflow for decision docs, RFCs, technical specs, and PRDs: Stage 1 Context Gathering (structured clarifying questions) -> Stage 2 Section-by-Section Refinement & Brainstorming -> Stage 3 Reader Testing (testing the document with a fresh context-free subagent to catch ambiguity and blind spots).
2. **Cursor `pstack` Technical Writing Skills** (`18,589★`, commit `7a583913eb1b8d1a0ee76753d1a2cf072e7b54f9`)
   - **Verified URL**: `https://github.com/cursor/plugins/tree/main/pstack/skills` | **Local Verbatim Copy**: `../upstream-skills/04-genres-academic-tech-social/cursor-pstack-technical-writing/pstack/skills/` (`technical-writing/SKILL.md`, `in-your-own-words/SKILL.md`, `principle-minimize-reader-load/SKILL.md`).
3. **`Omer-Dahan/readme-skill`** (MIT, commit `cba03e3e2fb0a64a45983bf50e627c81060add6b`)
   - **Verified URL**: `https://github.com/Omer-Dahan/readme-skill` | **Local Verbatim Copy**: `../upstream-skills/04-genres-academic-tech-social/readme-skill/`
   - Extracts a strict code-verified `fact-inventory.md` from the repository before drafting a GitHub README, paired with a house-style template, render check, and independent verification pass so zero unimplemented features or AI marketing hallucinations appear in the README.
4. **`RichardLitt/standard-readme`** (`3,900+★`, commit `5d18ad4db6a39fde5dc845258828153eda9828e8`)
   - **Verified URL**: `https://github.com/RichardLitt/standard-readme` | **Local Verbatim Copy**: `../upstream-skills/04-genres-academic-tech-social/standard-readme/spec.md`

---

## Genre 3: Social Media, 微信公众号, 小红书, LinkedIn & Cold / Professional Emails

### 3.1 微信公众号 & 中文长文去AI味实战 — 少数派 (sspai.com) 创作者实测

#### A. 踏雪寻仙 — 《你写的文章？都是 ai 味》（少数派，2026-02-24）
- **Author / Platform**: 踏雪寻仙（少数派 sspai.com 作者）
- **Verified URL**: `https://sspai.com/post/106564`
- **Verbatim Core Diagnosis**:
  - **改好的人味标准**：「认识他的人说：『对，他就是这么说话的。』不认识他的人说：『背后有个真实的人。』」
  - **AI 味三大症状与本质**：「空洞比喻让句子看起来高级。AI口头禅让段落读起来熟悉。总分总结构让文章看起来完整。三个凑在一起，堆砌文字，不说人话。**AI味的本质：用确定的套话，掩盖不确定的思考。**」
- **Verbatim「五步，把你写回去」工作流**:
  1. **第一步：先用自己的内容填充** — 「不要一开始就让AI写。先自己把要说的东西写出来，哪怕写得乱、写得糙、句子不通顺……你写的那些糙稿，就是这篇文章里唯一属于你的东西。」
  2. **第二步：让AI优化，不是重写（改稿五不纪律）** — 「不加事实，不编细节，不改立场，不改程度，不改语气。『有一定难度』不能变成『根本不行』，『可以考虑』不能变成『强烈建议』。AI总想帮你优化，但很多时候，优化就是歪曲。」
  3. **第三步：三角色分离提示词（原文原句）**：
     - **作者（写初稿）**：`「你是[作者名]，用自己的话写东西，不装，不升华。以第一人称写，口语化风格。」`（作者注：*「第一人称这一个指令，能解决一半的AI味。」*）
     - **编辑（改稿）**：`「你是一名编辑，任务是改稿，不是重写。改完之后，这篇文章里要有一个真实的人在说一件真实的事。」`
     - **读者（审稿）**：`「你是这篇文章的目标读者，一个刚开始用AI写作、感觉哪里不对劲的普通人。读完告诉我，哪句话让你停下来，哪句话让你跳过去。」`
  4. **第四步：具体负面约束优于空泛正面词** — 「『自然』『有人味』『口语化』，这些词对你有意义，对AI是空的……负面约束有时候比正面描述更有效：`『不要四字成语，不要排比句，不要总结性收尾。』`」
  5. **第五步：少样本好坏示例对比（原文原例）**：
     - **坏例子**：「在当今快速发展的数字化转型浪潮中，我部门积极响应公司战略号召，致力于通过创新技术手段提升业务效能。」
     - **好例子**：「公司在推数字化，上面要求做，我们就做了。目标是把效率提上去，具体措施还在落实。」
- **Verbatim「AI味句式库」与「四场景人味对照」**:
  - **GPT 风格**：「我就在这，不躲不藏，稳稳接住你」「不是……而是……」「首先……其次……最后……」——刻意共情，句式固定，结尾常加「希望这个想法对你有帮助」。
  - **国产 AI 风格**：「您好！感谢您提出这个问题」「我将从以下几个方面：1.…2.…3.」——过度礼貌，必用序号分点，结尾加总结句。
  - **通用通病**：「融入了、结合了、实现了」「这不仅是……更是……」——「了」字滥用，顿号堆砌并列词，引号加破折号强行制造重点。
  - **四场景人味来源**：
    - **微信回复**：人味来自即兴感，看完马上打的温度；AI味是回复完整、逻辑清晰，读起来像通知。
    - **推文**：人味来自一个让人想接话的缺口，有自己的角度；AI味是论点加论据加总结，读起来像小作文。
    - **内部汇报**：人味来自具体的事，有数字、有进度、有判断；AI味是全在表态，没有一句在说事。
    - **长文**：人味来自节奏，有松有紧，某几句发力，其他句子喘气；AI味是结构太对称，每段都有总结句——「几乎每段都有金句，也是一种AI味。」

#### B. 小胡小胡0009 — 《AI + Skill，能够让生成的文章去除 AI 味吗？》（少数派 Matrix 精选，2026-04-30）
- **Author / Platform**: 小胡小胡0009（少数派 Matrix 首页推荐，基于自建 `mp-article-skill` 与卡兹克开源 Skill 对照实测 Claude Opus 4.6 / Claude Sonnet 4.6 / GLM 5.1）
- **Verified URL**: `https://sspai.com/post/109288`
- **Six Empirically Documented AI Tells in Chinese Long-Form / 公众号 Articles (Verbatim Findings)**:
  1. **「不是 A，而是 B」句式泛滥与标点禁令的间接破除法**：
     - 作者实测发现：即使未直接写禁令，**禁止 AI 使用冒号（`：`）和破折号（`——`）** 能显著减少 AI 句式，因为 AI 最爱用的三类模板均依赖这两个标点：
       - 「不是 A，而是 B」常写成 `「A——不是 B」`
       - 定义式总结常写成 `「关键在于：A 是 B」`
       - 解释性展开常写成 `「原因在于：……」`
  2. **过度戏剧化的悬念与情绪过载**：「出了一身冷汗」「触目惊心」「令人警觉」「背后发凉」远超实际实验情绪强度（审读 subagent 修正示例：将「背后发凉」降级为「愣了一下」）。
  3. **比喻链过度延伸**：原文将「遥控器」比喻强行拆出「频道、音量、天线」三个子比喻一一对应三个结论，「工整到失真。真实写作中，比喻通常是点到即止的，AI 的倾向是把它当框架一路铺满。」
  4. **否定式定义 + 对称公式化小标题**：如「这不是『模型好坏』的问题」「你认真对待这个请求，AI 就认真对待这个输出」，读起来像同一个标题生成器产物；改后更像人话的小标题示例：「实验是怎么设计的」「情感激励有用，但它『努力』的方式有点野」。
  5. **多案例三段式同构**：四个案例全部严格重复「实验设计 $\to$ 结果 $\to$ 短句+破折号/冒号小结」，像教案的「本节要点」。
  6. **PPT 切页式程式化过渡句**：「看完……后，一个自然的追问是」「前面两个案例讲的都是……现在我们来看……」「如果说案例 1 验证了……案例 2 要验证的则是另一个更微妙的变量」。
- **Context-Isolated Subagent Review Architecture**:
  - 写作前先做三件事：**理解意图（切入角度/深度偏好/核心主旨/素材补充）、读取个人范文校准语感、确认大纲后停下等待人工反馈**。
  - 初稿完成后启动三个**上下文隔离的独立 subagent**（「独立审读」「事实核查」「终审自检」），只传文章正文不传对话背景，防止主 Agent 盲目自信。

---

### 3.2 小红书 (Xiaohongshu / RED) 去AI味与「活人感」实战

#### A. 陌晨 — 《3招秒去AI味！让文章像人写的，附提示词》（人人都是产品经理，2025-07-22）
- **Author / Platform**: 陌晨（人人都是产品经理 woshipm.com）
- **Verified URL**: `https://www.woshipm.com/ai/6244919.html`
- **Verbatim Three Prompt Formulas for Authentic Social / 小红书 Copy**:
  1. **三层叠加法（场景层 + 情感层 + 细节层）**：
     - 场景层：`“以深圳城中村出租屋为背景”`
     - 情感层：`“用‘孤独但自由’的矛盾感”`
     - 细节层：`“加入‘窗外霓虹灯在晾衣绳上投下的光影’”`
  2. **反套路公式（打破 AI 顺向概率思维）**：
     - 公式：`“先写[常规观点]，再用‘但’转折，加入[意外细节]”`
     - 原文示例：`“所有人都说秋天适合恋爱，但我只喜欢捡落叶——尤其是被踩碎时咔嚓咔嚓的声音”`
  3. **五感锚定法**：
     - 公式：`“必须包含[视觉]+[听觉]+[嗅觉]元素”`
     - 原文示例：`“描写清晨菜市场：红色的辣椒堆、称秤的叮咚声、酱油缸的咸香”`
  - **原文避坑对照**：
    - 过度规整排比：`“春天是绿的，夏天是红的，秋天是黄的”` $\to$ 不规则句式：`“春天绿得冒泡泡，夏天红得像要烧起来”`
    - 抽象形容词堆砌：`“这款产品非常好，特别棒”` $\to$ 具体量化：`“充电 5 分钟，刷剧 2 小时”`

#### B. Verified Open-Source 公众号 / 小红书 / 中文去AI味 Skills (`../upstream-skills/`)
1. **`KKKKhazix/human-writing`** (`4,706★`, MIT, commit `288297b6c2d9b6df23e0ceb64888443f15cfbcc3`, Author: 数字生命卡兹克)
   - **Verified URL**: `https://github.com/KKKKhazix/human-writing` | **Local Verbatim Copy**: `../upstream-skills/02-chinese-and-bilingual/human-writing/`
2. **`imraywang/wewrite`** (`3,749★`, MIT, commit `d99083bfd7aa8c2cd00aae82243d1b45c0a8abf7`)
   - **Verified URL**: `https://github.com/imraywang/wewrite` | **Local Verbatim Copy**: `../upstream-skills/04-genres-academic-tech-social/wewrite/skills/` (`wewrite-write`, `wewrite-review`, `wewrite-rewrite`, `wewrite-style`, `wewrite-learn`).
3. **`guzhezao/xhs-content-skill`** (`96★`, commit `65fc96064b534face6884cb97d0763514d78c4c2`)
   - **Verified URL**: `https://github.com/guzhezao/xhs-content-skill` | **Local Verbatim Copy**: `../upstream-skills/04-genres-academic-tech-social/xhs-content-skill/SKILL.md`
4. **`meikis/remove-ai-flavor-writing-skill`** (`4★`, MIT, commit `5edd9fa055292cdb854b210e806ad4fb64910bbe`)
   - **Verified URL**: `https://github.com/meikis/remove-ai-flavor-writing-skill` | **Local Verbatim Copy**: `../upstream-skills/04-genres-academic-tech-social/remove-ai-flavor-writing-skill/SKILL.md`
   - Targets binary contrast shells (`不是 A，而是 B` / `并非 A，而是 B` / `与其说 A，不如说 B`), staged sequence shells (`先 A，再 B`), essence claims (`真正重要的是` / `核心在于` / `底层逻辑`), assistant route markers (`下面我们来` / `值得注意的是` / `说白了` / `划重点` / `拆一拆`), and fake engagement questions at the end of 小红书 / 公众号 posts.
5. **`Liuxiangjian-ai/official-document-skill`** (`470★`, MIT, commit `cbe5f8cd8aa79c8d977ff858994780f306cebb66`)
   - **Verified URL**: `https://github.com/Liuxiangjian-ai/official-document-skill` | **Local Verbatim Copy**: `../upstream-skills/04-genres-academic-tech-social/official-document-skill/SKILL.md`

---

### 3.3 LinkedIn & Western Social Media — Anti-"Broetry" & Anti-AI-Slop Guides

#### A. Melanie Goodman (*The Link Tank* Substack) — *Stop Asking AI to Write Your LinkedIn Posts*
- **Author / Platform**: Melanie Goodman (*The Link Tank* Substack, Oct 29, 2026)
- **Verified URL**: `https://melaniegoodmanlinkedinconsultant.substack.com/p/stop-asking-ai-to-write-your-linkedin`
- **Documented Platform Enforcement & Quotes**:
  - **LinkedIn Editor-in-Chief Dan Roth (CNN, Oct 18, 2026)**: *"I know you think you're doing the right thing with your perfectly bulleted list and your hook at the top, and you followed all the advice from LinkedIn advisors across the internet. But what works is being human."*
  - **Dan Roth's Two-Question Pre-Post Test**: *"Did you enjoy reading this? Do you see yourself in this?"*
  - **Platform Changes Cited**: LinkedIn removed its `"Enhance post"` AI rewriter, added a `"Seems like AI slop"` user-report option (used >1M times in its first two weeks), and deployed classifiers checking out-of-network distribution (LinkedIn VP of Engineering Tim Jurka reported 94% precision on AI-slop detection and a 40% reduction in views of flagged slop, defined by LinkedIn as *"low-effort, likely AI-generated content that may sound polished on the surface but lacks a clear point of view, unique perspective, or substance"*).
- **Verbatim 6-Step "The Human Middle" Workflow**:
  1. **Step 1 — Get interviewed before you write**: Ask AI to interview you one question at a time for 5 minutes to surface a real client conversation, number, or mistake (*`"Before you start any task, ask me two or three multiple-choice questions about audience, purpose and format"`*).
  2. **Step 2 — Choose one point**: One post, one point; state it in a single sentence before drafting.
  3. **Step 3 — Write the middle yourself**: Write every sentence in your own words (`150–250 words`) with no AI tab open (*"An honest half-formed point beats a finished-sounding empty one"*).
  4. **Step 4 — Hand it over for checking only**: Ask AI strictly for a list of problems/clichés with an explicit ban on rewriting.
  5. **Step 5 — Fix what you agree with, by hand**: Reject any edit that alters meaning or rhythm.
  6. **Step 6 — Run Dan Roth's two-question test on your phone**.
- **Critical Failure Mode Highlighted**: *"Asking AI to 'make it sound more human'. This produces a convincing imitation of a human, complete with invented anecdotes. You end up with a fluent post about something that never happened. Keep the human detail coming from you."*

#### B. Hacker News Community Thread — *AI Content Is Everywhere on Social Media, Especially LinkedIn*
- **Platform**: Hacker News (`item?id=48847940`, July 9, 2026)
- **Verified URL**: `https://news.ycombinator.com/item?id=48847940`
- **Verbatim Netizen Observations on Social Media AI Tells**:
  - **Contrived corporate analogies (`scientifik`, `https://news.ycombinator.com/item?id=48848615`)**: *"Totally contrived stories and 'lessons' to how ordering at Starbucks is like managing cloud infrastructure."*
  - **Multi-paragraph thesis captions (`volkk`, `https://news.ycombinator.com/item?id=48848591`)**: *"Before AI, the descriptions of sports videos or meme videos were 2 sentences, now they're entire theses [giant 3-4 paragraph things]."*
  - **LLM speech-pattern contagion (`ikesau`, `https://news.ycombinator.com/item?id=48848508`)**: *"I've read blogs from people who I'm quite sure are above pasting AI output directly into their words who nevertheless are sounding more and more like AI as the sum of all their conversations with Claude begins to rub off on them."*
  - **False-positive warning on non-native English writers (`timpera`, `https://news.ycombinator.com/item?id=48848529` & `dvt`, `https://news.ycombinator.com/item?id=48848625`)**: Citing Stanford HAI (`https://hai.stanford.edu/news/ai-detectors-biased-against-non-native-english-writers`), warning that heuristic detectors target surface markers (rule of three, em dashes) and falsely flag ESL writers.

---

### 3.4 Cold Outreach & Professional / Academic Emails

#### A. Josh Clarke (Built For B2B) — *AI Cold Email: How to Use AI Without Killing Your Reply Rate*
- **Author / Platform**: Josh Clarke (Built For B2B, May 19, 2026 — tested across 200,000 sent B2B emails)
- **Verified URL**: `https://www.builtforb2b.com/blog/ai-cold-email-how-to-use-ai-without-killing-reply-rate`
- **Verbatim Three-Layer AI Cold Email Architecture**:
  - *"AI cold email works when you treat it as a research and assembly engine, not a writer."*
  - **Layer 1 (Research)**: Surface a specific, non-generic weekly trigger (job post, funding, podcast, hiring pattern, tech stack change). *"If AI cannot find a specific, non-generic reason to email the prospect this week, do not email them."*
  - **Layer 2 (Assembly)**: *"AI assembles the first line. Not the body. Not the CTA. Just the opener that ties the signal to the offer... The body and CTA are written once by a human and never touched by AI."*
  - **What AI Should NEVER Write**: (1) **Subject lines**, (2) **Closing lines / CTAs** (ban *"Are you open to a 15-minute chat?"*), and (3) **The actual offer**.
- **The Five Places AI Breaks Cold Email Reply Rates (Verbatim)**:
  1. **Over-personalisation**: *"Hi Sarah, I saw your podcast on Spotify, your LinkedIn post about Series B, and noticed you went to MIT."* -> Creepy, not personal. One signal, one sentence.
  2. **Compliments that feel hollow**: *"Your company is doing amazing work in fintech"* -> Cut all compliments; open with the signal, not flattery.
  3. **Triple-paragraph proof**: AI defaults to 3 press-release paragraphs; best-performing cold emails are **50 to 90 words** (One signal. One offer. One ask).
  4. **Buzzword cascade**: Ban *"streamline operations"*, *"drive efficiency"*, *"transform pipeline"*; use the buyer's domain nouns (e.g., *"routes and loads"* in logistics).
  5. **False urgency**: Ban *"We have a limited window"* / *"Open for the next 48 hours"*.
- **Verbatim 200k-Email Tested Prompt Constraint**:
  - Feed the LLM only (1) one-sentence signal, (2) buyer role/pain/phrase, and (3) strict constraints: **`"Under 60 words. No buzzwords. No questions in the opener. End with one specific ask."`**

#### B. `coreyhaines31/marketingskills` — `cold-email`, `copywriting`, `copy-editing`, `social` & `emails` Skills
- **Repository**: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (`62,119★`, MIT, commit `5b2b400eec1e7e1cec76245a715d0b0d4fd2a9c1`)
- **Local Verbatim Copy**: `../upstream-skills/04-genres-academic-tech-social/marketingskills-copy-social-email/skills/`
- **Verbatim Cold Email De-AI Rules (`skills/cold-email/SKILL.md` L31–96)**:
  - **Write like a peer, not a vendor**: *"Use contractions. Read it aloud. If it sounds like marketing copy, rewrite it... No AI tells like `'it's not X, it's Y'`."*
  - **Explicit AI-Tell Blacklist (`SKILL.md` L70)**: Avoid *"I hope this email finds you well"*, *"I came across your profile"*, *"leverage"*, *"synergy"*, *"best-in-class"*.
  - **Personalization Litmus Test (`SKILL.md` L41)**: *"If you remove the personalized opening and the email still makes sense, the personalization isn't working."*
  - **Subject Lines (`SKILL.md` L89–96)**: *"Short, boring, internal-looking. 2–4 words, lowercase, no punctuation tricks. Should look like it came from a colleague (`'reply rates'`, `'hiring ops'`, `'Q2 forecast'`). No product pitches, no urgency, no emojis, no prospect's first name."*
  - **Follow-Ups (`SKILL.md` L103)**: Ban `"Just checking in"`; every follow-up must add a new angle, proof point, or standalone resource.

#### C. Prof. Matt Might — *How to Send and Reply to Email* (Academic & Technical Correspondence)
- **Author**: Prof. Matt Might
- **Verified URL**: `https://matt.might.net/articles/how-to-email/`
- **Verbatim Rules**:
  - *"Email is not mail in electronic form. You are not writing a letter. Email should be formatted into points--not paragraphs."*
  - **Keep it short**: *"Try living with the five sentences rule for a week."*
  - **Subject (`<= 72` chars)**: *"If the entire email fits in the subject, put it in the subject... Otherwise, the subject should contain the most critical details, such as the date, time and location of a meeting, or the top action item and deadline."*
  - **Points, not paragraphs**: *"Put a blank line after every point, which usually means after every independent thought, and certainly after every question... Large blocks of text short-circuit reader attention."*
  - **Reply inline to points**: Quote only relevant points and reply directly beneath each point rather than top-posting a dense paragraph.
  - **Action items in top 5 lines**: *"Assume that only the top 5 lines of any email will be read. Put anything critical in those lines."*
  - **Sign-off**: *"A `'Thanks!'` often comes off as more sincere than `'Sincerely.'`"*

#### D. Anthropic Official `internal-comms` Skill (`../upstream-skills/`)
- **Verified URL**: `https://github.com/anthropics/skills/tree/main/skills/internal-comms` | **Local Verbatim Copy**: `../upstream-skills/05-visual-image-figure-and-ui/anthropics-skills/skills/internal-comms/` (`SKILL.md` + `examples/3p-updates.md`, `company-newsletter.md`, `faq-answers.md`, `general-comms.md`).
