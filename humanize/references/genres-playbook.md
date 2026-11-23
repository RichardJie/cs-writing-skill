# Multi-Genre Humanization Playbook — Engineering, Social, Career, Spoken & Creative

Removing AI voice is never one-size-fits-all: stripping buzzwords makes a GitHub README crisp, whereas stripping rhythm and subjective friction makes a Substack essay or Bilibili script sound dead. Conversely, injecting casual slang ruins an incident postmortem or PhD Statement of Purpose.

Use the **Genre Calibration Matrix** first to lock the target register, then apply the matching domain playbook below.

> **Hard Fact-Preservation Rule Across All Genres ([../SKILL.md](../SKILL.md)):** Never fabricate outages, benchmark numbers, prices, personal anecdotes, or resume metrics to make text "sound more human." Work strictly with facts in the source draft; where a genre demands concrete specifics that the draft omits, surface an explicit placeholder (`[TODO: insert exact P99 delta]`, `[补充真实耗时/踩坑细节]`) instead of inventing fiction. Pair this genre playbook with [../english.md](../english.md), [../chinese.md](../chinese.md), [bilingual-tech-writing.md](bilingual-tech-writing.md), and [model-fingerprints.md](model-fingerprints.md).

---

## 1. Genre Calibration Matrix

| Genre | Voice Temperature | Sentence Rhythm | First-Person (`I / We / 我`) | Formatting & Visual Rules | #1 Fatal AI Tell to Purge |
|:---|:---|:---|:---|:---|:---|
| **Tech Blog / Deep-Dive** | Pragmatic, opinionated, candid | High burstiness (code + short punch + explanation) | Yes (`I` or team `We`) | Code/logs early; minimal bolding | *"In modern distributed systems, scalability is crucial..."* |
| **GitHub README** | Dry, utilitarian, zero-hype | Ultra-compact declarative | Minimal (`The CLI...`) | Copy-paste Quickstart in top 20 lines; zero emoji bullet spam | `🚀 Blazingly Fast, Next-Gen, Seamless` |
| **Incident Postmortem** | Clinical, blameless, exact | Crisp, timestamped, active | System actors + team `We` | UTC timeline table + 5-Whys + ticketed actions | Passive evasion (*"An issue was experienced..."*) + moralizing |
| **微信公众号 (WeChat)** | Conversational, sharp, grounded | Medium-short paragraphs, natural pauses | Strong (`我`) | Sparse bolding (<=3 per 1k chars); no symmetric 4-char headers | 「在这个焦虑的时代」+ 爹味说教 + 结尾升华熬鸡汤 |
| **小红书 (Xiaohongshu)** | Candid peer sharing, tactile | Short spoken beats, natural line breaks | Strong (`我`) | Concrete specs/prices/cons; zero robotic 1-emoji-per-line lists | 「家人们谁懂啊！绝绝子✨🔥」假亢奋百科清单 |
| **知乎 (Zhihu)** | Domain insider, analytical, dry wit | Dense insight + punchy verdict | Practitioner (`我`) | Mechanism breakdown + cost math; kill textbook 1-2-3 outlines | 复读题目 + 「先说结论：辩证看待」骑墙正确的废话 |
| **X / Twitter** | High-signal, compressed, direct | 1–3 crisp sentences per post | Direct | Lead with the chart/code/takeaway on line 1 | `"🧵 Most people get X wrong. Here are 9 secrets 👇"` |
| **LinkedIn** | Grounded operator, collegial | Normal multi-sentence paragraphs | Direct (`I / We`) | Ban 1-sentence-per-line "broetry" spacing | Contrived hiring fables + `"Agree? 👇"` |
| **Substack / Essay** | Idiosyncratic, inquisitive | Long sinuous runs + sudden 4-word stops | Reflective (`I`) | Plain prose paragraphs; minimal subheaders | Claude essayist voice (*"Here's the thing"*, *"sit with"*) |
| **Cold / Work Email** | Respectful, peer-to-peer, brief | <= 120 words total, scannable | Direct (`I`) | BLUF (ask in 3 lines); zero decorative formatting | *"I hope this email finds you thriving"* + flattery |
| **Grad School SOP** | Intellectual, focused, mature | Crisp narrative + technical precision | Scholarly (`I`) | Pure prose paragraphs; zero bold/bullets | Childhood origin stories + *"vibrant tapestry"* |
| **Resume / CV** | Metric-dense, mechanistic | Tight verb-first fragments | Implied | 1–2 lines per bullet; exact stack + baseline->target delta | *"Spearheaded synergistic cross-functional initiatives"* |
| **PRD / Product Spec** | Unambiguous, edge-case obsessed | Structured tables & state rules | Product/System actors | Explicit Non-Goals + Failure State Matrix | *"Empower seamless holistic user journeys"* |
| **Video / Podcast Script** | Ear-first, breathable, deictic | <= 15 words / <= 18 CN chars per breath | Spoken (`我 / 咱们 / You`) | Written for breath units; zero `former/latter` or nested clauses | Written-essay syntax read aloud + scripted `[laughs]` |
| **Creative Fiction** | Concrete, subtextual, unsentimental | Varied cadence matched to scene tension | POV-locked | Physical staging over psychological summary | *Ozone, shivers down spine, testament* + moralizing scene endings |

---

## 2. Domain 1: Engineering & Developer Prose

### 2.1 Technical Blogs & Engineering Deep-Dives (EN & CN)

**Diagnostic AI Tells:**
- Opening with a Wikipedia history of containers, databases, or LLMs before mentioning the actual engineering problem.
- Toy `foo / bar / UserService` abstractions with suspiciously clean numbers.
- Cheerleader transitions (*"Now comes the exciting part!"*, *"Let's dive into how we effortlessly solved this!"*).
- Hiding ugly trade-offs behind a triumphant conclusion.

**Rewrite Rules:**
1. **Start at the Crime Scene:** Open with the failing metric, `perf` flamegraph anomaly, OOM killer log, or counterintuitive benchmark number.
2. **Show Real Artifacts:** Prefer a 6-line `EXPLAIN ANALYZE` snippet, memory layout struct, or `git diff` over three paragraphs of abstract prose.
3. **Keep the Dead Ends:** Mentioning the obvious fix that *didn't* work (and why) proves a human actually debugged the system.
4. **State When NOT to Copy You:** Close with concrete operational caveats (e.g., write amplification cost, kernel version requirement).

**Before (EN — AI Engineering Blog Opener):**
> In today's fast-paced cloud-native landscape, maintaining low tail latency in distributed key-value stores is more critical than ever. As microservices scale, garbage collection pauses can become a silent killer, underscoring the need for meticulous memory management. In this blog post, we will delve into how our team leveraged Rust's zero-cost abstractions to overhaul our caching tier, achieving blazingly fast performance and seamless scalability.

**After (EN — Real Systems Engineer Opener):**
> Every Tuesday at 04:15 UTC, P99.9 read latency on our session cache spiked from 1.9 ms to 340 ms for ninety seconds. CPU utilization sat at 38%, network bandwidth had 6 Gbps of headroom, and Go's `GODEBUG=gctrace=1` showed only 4 ms STW pauses. The culprit turned out to be Linux transparent hugepage compaction stalling `epoll_wait` inside a 96 GB heap full of pointer-heavy map buckets. Moving just the hot ring buffer off-heap (first via `mmap` byte slices in Go, then a 1,400-line Rust FFI shard) cut P99.9 to 2.3 ms flat. Here is where the Go `mmap` prototype hit a wall and why we paid the FFI tax anyway.

---

### 2.2 GitHub READMEs & Developer Documentation

**Diagnostic AI Tells:**
- H1 followed by a tagline packed with `Next-Gen`, `AI-Native`, `Lightweight yet Powerful`, `Production-Ready`, `Blazingly Fast`.
- Feature lists where every line starts with `🚀`, `✨`, `🔒`, `⚡`, `🧩` and repeats vague promises (*"Modular architecture: Easily extend components"*).
- Making the developer scroll past 80 lines of philosophy before seeing what CLI command or function call the package exposes.

**Rewrite Rules:**
1. **The 10-Second One-Liner:** `<Name> is a <concrete noun> that <exact input -> output transformation> in/for <runtime/constraint>.` Zero unquantified speed adjectives.
2. **Code Above the Fold:** Show `install` + a 5-line runnable example with actual output within the first 25 lines.
3. **Receipts for Speed Claims:** If you claim speed, state what you measured against on what hardware (`Parses 1 GB NDJSON in 0.82s on M3 Max vs. 3.9s in jq 1.7`), or delete *"fast"*.
4. **Explicit Non-Goals:** Add 3 bullets saying what the library deliberately omits.

**Before (AI Vibe-Coded README):**
> # 🚀 FluxPipe — Next-Gen Blazingly Fast Data Orchestration
> FluxPipe isn't just another ETL tool; it's a lightweight, developer-first paradigm shift for modern data workflows.
> - ✨ **Seamless Integration:** Effortlessly connect your favorite sources and sinks.
> - ⚡ **Blazingly Fast:** Built from the ground up in Rust for unparalleled throughput.
> - 🧠 **Smart Retries:** Intelligently handles transient network hiccups out of the box.

**After (Maintainer-Grade README):**
> # fluxpipe
> `fluxpipe` streams Postgres logical replication slots directly into Parquet files on S3 with bounded memory (< 64 MB RSS) and zero JVM dependencies.
>
> ```bash
> cargo install fluxpipe
> fluxpipe --slot orders_cdc --pg "$DATABASE_URL" --s3 s3://warehouse/orders/ --flush-seconds 60
> ```
>
> **Benchmarks (c7g.xlarge, Postgres 16 -> S3 us-east-1):** Sustains 185,000 rows/sec (210 MB/s uncompressed) at 42 MB RSS.
>
> **Non-goals:** No in-flight SQL joins, no schema-registry daemon, and no exactly-once cross-region two-phase commit (downstream readers deduplicate on `(lsn, xid)`).

---

### 2.3 Incident Postmortems / Engineering RCAs (`线上故障复盘`)

**Diagnostic AI Tells:**
- Passive corporate fog (*"A configuration discrepancy was introduced, resulting in suboptimal availability"*).
- Dramatic storytelling (*"Chaos ensued as alerts flooded the war room"*) or preachy endings (*"This incident serves as a humbling testament to the complexity of DNS"*).

**Rewrite Rules:**
1. **4-Line Metadata Header:** Date, Duration (exact minutes), User Impact (% failed requests / affected endpoints), Root Trigger (1 concrete sentence).
2. **Active Mechanistic Chain:** Name systems and code paths clearly (*"Deploy `#8841` set `max_idle_conns = 0` in `auth-proxy`, forcing a new TLS handshake per RPC and exhausting ephemeral ports on `nat-gw-02` within 4 minutes"*), while keeping human framing blameless (*"CI lacked bounds validation on connection-pool YAML"*).
3. **Deterministic Remediation Only:** Ban *"Be more careful during code review."* Every action item must be a code change, alert threshold, or automated gate with an owner.

**Before (AI Corporate Slop Postmortem):**
> On November 12, an unexpected service degradation occurred across our checkout ecosystem, impacting user transactions. Upon thorough investigation, it was determined that a caching misconfiguration interacted unfavorably with peak traffic patterns. Our dedicated engineering team worked tirelessly to restore stability. Moving forward, this incident underscores the vital importance of comprehensive staging validation.

**After (Engineering RCA Summary):**
> **Impact:** From 14:08 to 14:31 UTC on Nov 12 (23 min), 41% of `/v2/checkout/confirm` POST requests returned `HTTP 503` (19,400 failed checkouts).
> **Root Cause:** PR `#4912` changed the Redis session key prefix from `sess:v1:` to `sess:v2:` without dual-reading `v1` keys. All active carts fell back to synchronous Postgres lookups, saturating `pg-primary` `max_connections` (500/500) within 90 seconds.
> **Recovery:** Rolled back `checkout-api` to `v2.18.3` at 14:27 UTC; connection pool drained to baseline by 14:31 UTC.
> **Corrective Actions:**
> - `[ENG-902, @lin]` Add CI migration lint rejecting Redis key-prefix edits without a dual-read adapter flag.
> - `[ENG-905, @patel]` Cap `checkout-api` Postgres fallback concurrency via token bucket (`limit=50`) so cache misses shed load with `Retry-After` instead of exhausting global DB connections.

---

## 3. Domain 2: Social Media & Public Creator Platforms

### 3.1 微信公众号 (WeChat Official Accounts — 深度评论与行业长文)

**AI 病灶诊断：**
- **时代背景起手式：** 「随着 AI 时代的全面到来，各行各业正在经历一场前所未有的深刻变革……」
- **爹味导师腔：** 「你必须清醒地认识到」「普通人破局的唯一出路在于……」
- **四字对仗小标题癖：** `01 认知觉醒：打破思维藩篱`、`02 价值重构：构筑核心壁垒`、`03 长期主义：静待时间的玫瑰`。
- **满屏机械加粗 + 结尾强行升华：** 每段必有一句加粗「金句」，最后一段必喊口号。

**去 AI 味改写规则：**
1. **切口极小化：** 第一段只写一个具体的人、一笔具体的账、一句刚听到的原话或一个反常小细节。
2. **砸碎对称小标题：** 小标题直接用大白话陈述核心判断（如「算完毛利率，一半加盟商当场退群」）。
3. **有偏见的真话代替面面俱到：** 砍掉「固然有弊端，但也带来了机遇」的骑墙段，直接亮明你站在哪一边、凭什么这么算。
4. **冷收尾：** 讲完最后一个事实或反讽细节直接停笔，绝不写「让我们拭目以待 / 未来已来」。

**Before (公众号 AI 腔):**
> 在消费降级的时代背景下，餐饮行业正面临着前所未有的机遇与挑战。许多传统餐饮老板陷入了价格战的泥潭，不仅利润被严重侵蚀，更失去了品牌的核心竞争力。**其实，打败你的往往不是对手，而是你固步自封的认知。** 餐饮人唯有拥抱数字化转型、深耕供应链闭环，才能在激烈的市场洗牌中穿越周期，静待花开。

**After (活人感深度号写法):**
> 上礼拜去华强北跟老周吃猪脚饭，他指着街对面那家刚把招牌拆下来的湘菜馆跟我算了一笔账。那家店上个月上了团购 39 块 9 双人餐，周末排队排到马路牙子上，月底一盘账：流水涨了四成，净亏六万二。平台抽点、投流买榜、预制菜冷链损耗，三刀切下来，老板相当于每天贴钱请整条街的人吃饭。现在谁再跟餐饮老板聊什么「品牌心智」「穿越周期」，大概率会被直接拉黑。房东下个月五号收租的时候，从来不听你讲长期主义。

---

### 3.2 小红书 (Xiaohongshu / RED — 真实经验帖与种草/避坑)

**AI 病灶诊断：**
- 滞后两年的网梗堆砌：「家人们谁懂啊！！真的绝绝子！按头安利！宝子们闭眼冲✨🔥💖」
- 每行固定一个 emoji + 四字冒号标题的说明书排版（`💡 外观设计：简约大气`、`🔋 续航表现：持久耐用`）。
- 只有抽象夸奖，没有入手价、身高体重/肤质/户型前提、耗时、以及**哪怕一个真实缺点**。

**去 AI 味改写规则：**
1. **前提先行：** 第一句直接报自己的约束条件（如「混油敏皮 / 深圳回南天实测两周」「租房党预算 400 以内」）。
2. **必须保留「毛边与槽点」：** 真人分享一定有不完美体感（线太短、包装难撕、某种情况下翻车）——写出具体使用边界比夸十句更像活人。
3. **口语短句分段：** 删光句首排队 emoji，像给闺蜜/同事发微信语音转文字一样自然断句。

**Before (AI 小红书种草腔):**
> 家人们谁懂啊！这款人体工学椅真的是打工人福音✨！
> 🌟 支撑感强：贴合腰椎曲线，久坐不累！
> 💨 透气网布：夏天坐着也清爽舒适！
> 💰 性价比高：千元价位天花板，宝子们闭眼冲就完事了🔥！

**After (真实体感小红书笔记):**
> 身高 163、体重 48kg，每天写代码坐够 10 小时的腰突选手，自费 1180 买了这把椅子，坐满三个月说点大实话。
> 先夸救命的地方：它的腰托是前后能顶出来的那种，我这种瘦子往前调到二档刚好卡住第四节腰椎，下午四五点腰不会再像以前那样酸得想躺地上。
> 但有两个槽点小个子一定要注意！第一，它最低座高还是偏高一丢丢，我不穿鞋脚后跟会悬空半厘米，最后自己花二十块钱配了个脚踏才舒服；第二，扶手塑料感挺重的，晃动有点旷量。如果你身高 165 以上、只看重护腰，这价位能打；低于 158 的姐妹千万先去线下试坐再掏钱。

---

### 3.3 知乎 (Zhihu — 硬核行业拆解与问答)

**AI 病灶诊断：**
- 开头把题干抄一遍：「关于『为什么现在……』这个问题，背后涉及经济、技术与心理等多重维度的因素。先说结论：机遇与风险并存。」
- 百科全书式「一、宏观层面；二、企业层面；三、个人层面」，每段正确的废话，零行业内幕细节。

**去 AI 味改写规则：**
1. **第一行亮底牌或直接拆台：** 用从业年限/经手项目量级切入，或直接指出题干前提就错了。
2. **用机制与利益链代替道德评价：** 解释清楚「谁出钱、谁背锅、KPI 怎么考核的」，AI 永远写不出真实的组织摩擦和草台班子逻辑。

**Before (AI 知乎回答):**
> 为什么很多大企业的内部工具反而不如外部开源软件好用？这是一个非常值得探讨的组织管理问题。首先，大企业内部流程复杂，安全合规要求极高，往往牺牲了用户体验；其次，内部研发团队缺乏市场竞争压力，迭代动力不足；最后，跨部门沟通成本高昂也导致需求响应滞后。综上所述，这是效率与安全权衡的必然结果。

**After (知乎老手回答):**
> 带过三年大厂内部研发效能平台，说个得罪人的实话：**内部工具难用，是因为决定你升职加薪的人根本不用这套工具。**
> 外部 SaaS 做难用了，客户明年不续费，公司直接死；但内部工具呢？一纸安全红线发文「全员强制迁移至自研流水线」，DAU 第二天直接拉满 100%，团队年底晋升 PPT 上写的是「覆盖全集团 3 万研发，渗透率 99.2%」。至于一线开发点个发布按钮要跳五个审批页、每次构建慢四分钟？那叫「精细化权限管控能力」。只要立项逻辑还是靠向老板汇报「造了多大的轮子」拿预算，不用靠向一线工程师收订阅费活命，这事无解。

---

### 3.4 X / Twitter, LinkedIn & Substack

#### X / Twitter (Single Posts & Technical Threads)
- **Kill:** `"🧵 99% of developers still prompt LLMs wrong. I spent 300 hours reading source code. Here are 7 game-changing techniques (Save this!) 👇"` + `"Let that sink in."`
- **Write:** Put the sharpest mechanism or number in Tweet 1 with zero meta-commentary.
  - *Before:* `Most engineers underestimate SQLite. It's not just a toy DB—it's a powerhouse! Here's why you should care 🧵👇`
  - *After:* `SQLite in WAL mode with mmap_size=268435456 and synchronous=NORMAL handled 48,000 writes/sec and 310,000 point reads/sec on a $24 Hetzner NVMe box before p99 crossed 4ms. Exact pragma config + Go benchmark repo:`

#### LinkedIn (Killing "Broetry")
- **Kill:** Single-sentence-per-line dramatic cliffhangers, fake airport/barista wisdom parables, humblebrags disguised as leadership lessons, and `"Thoughts? Agree? 👇"`.
- **Write:** Standard 3–4 sentence paragraphs grounded in real work tradeoffs.
  - *Before:*
    > Yesterday, my junior developer took down production for 20 minutes.
    >
    > Everyone expected me to fire him.
    >
    > Instead, I bought him lunch.
    >
    > Leadership isn't about punishment—it's about psychological safety. Agree? 👇
  - *After:*
    > A bad migration locked our `orders` table for 18 minutes yesterday because our staging DB only has 50k rows: `ALTER TABLE` ran in 12ms in staging and stalled behind a long reporting query in prod. Blaming the engineer who merged it fixes nothing; any of us would have trusted a green CI check. Today we added `lock_timeout = '2s'` to our migration runner wrapper and replayed production table statistics into staging nightly.

#### Substack & Longform Essays (Killing the "Claude Essayist" Cadence)
- **Kill:** `"Here's the thing about..."`, `"Let's sit with that tension"`, `"Perhaps the real question isn't X, but Y"`, rhythmic 3-paragraph symmetry, and cozy therapeutic conclusions.
- **Write:** Anchor abstract claims in stubborn historical, textual, or personal specifics; allow unresolved irritation or sharp asymmetry; end on an image or concrete implication rather than a sermon.

---

## 4. Domain 3: Career, Admissions & Product Specs

### 4.1 Workplace & Academic Cold Emails (`职场沟通与博士套磁邮件`)

**Rules:**
1. **Zero Health Inquiries:** Delete *"I hope this email finds you well / thriving amidst a busy semester."*
2. **Zero Adjective Worship in Faculty Cold Emails:** Professors delete *"I was deeply fascinated by your groundbreaking CVPR paper"* on sight. Reference a **specific technical mechanism, limitation, or extension** proving you actually read the math/code.
3. **Hard 120-Word Ceiling + Single Low-Friction Ask.**

**Before (AI PhD Cold Email):**
> Dear Professor Smith,
> I hope this email finds you well! My name is Alex, a passionate senior undergraduate majoring in Computer Science. Having long admired your pioneering research in the realm of efficient machine learning, I was utterly captivated while delving into your recent ICML paper on sparse attention. My extensive background in PyTorch and deep learning aligns seamlessly with your vibrant lab, and I would be honored to discuss potential PhD opportunities with you.

**After (High-Signal PhD Cold Email):**
> Dear Prof. Smith,
> I am a CS senior at [University] applying to [School]'s PhD program this December. While reproducing your ICML '25 block-sparse attention kernel on variable-length code repos, I noticed tile utilization drops below 40% when AST-aligned spans straddle 128-token boundaries; packing spans via a greedy prefix bin-packer recovered 1.7x prefill throughput on RepoBench (code + plot: [link]).
>
> I am exploring whether this packing invariant extends to your recent multi-turn agent KV cache work. Are you recruiting PhD students for Fall 2027? My CV and 1-page research note are attached.

---

### 4.2 Graduate Statement of Purpose (SOP / Personal Statement)

**AdCom AI Red Flags:**
- Childhood origin stories (*"Watching my grandmother struggle with illness sparked my lifelong passion..."*, *"My first Hello World..."*).
- Explaining to CS professors why AI/systems is important.
- Listing tasks (*"I cleaned data, trained ResNet, and achieved 91% accuracy"*) with zero intellectual agency or failure analysis.
- Generic closing paragraph (*"X University's collaborative culture and world-renowned faculty make it the ideal place..."*).

**Rewrite Rules:**
1. **Paragraph 1 = Your Research Problem:** Open directly with the technical tension you want to spend five years solving.
2. **Project Paragraphs = Hypothesis -> Obstacle -> Insight:** Show how you think when standard baselines break. One well-dissected negative result beats three buzzword-stuffed internships.
3. **Faculty Fit = Concrete Problem Intersection:** Name 2–3 professors and state *which specific technical question* bridges your prior work and their active agenda.

**Before (AI SOP Excerpt):**
> Ever since I built my first neural network, I have been fascinated by how machines learn representations. During my research internship at Lab X, I spearheaded an innovative project on multimodal alignment, leveraging contrastive learning to bridge vision and language. Through meticulous experimentation, I overcame numerous challenges and boosted retrieval accuracy by 6%, which solidified my passion for pursuing a PhD in your esteemed department.

**After (AdCom-Ready SOP Excerpt):**
> Contrastive vision-language encoders map images and captions into a shared hypersphere, yet they systematically discard spatial prepositions ("the mug *behind* the laptop" scores identically to "the mug *beside* the laptop"). At Lab X under Prof. [Name], I tested whether hard-negative caption swapping fixes relational blindness in CLIP-ViT-L. Naive swaps collapsed zero-shot ImageNet accuracy by 4.8% because token-shuffled negatives encouraged the text encoder to shortcut on syntactic bigram artifacts and ignore scene geometry. Constraining negative perturbations to object-centric bounding-box crops preserved ImageNet parity while lifting ARO spatial attribution by 11.2% ([Preprint/Venue]). Teaching encoders compositional structure without sacrificing web-scale lexical coverage is the exact tension I want to pursue in my PhD.

---

### 4.3 Resumes & CVs (`中英文简历去黑话`)

**Rules:**
- Ban empty power-verb triads (*Spearheaded, Orchestrated, Championed, Empowered, Synergized*) and Chinese PM buzzwords (*赋能、抓手、闭环、颗粒度对齐、沉淀方法论*).
- Enforce **Engineered Artifact + Mechanism + Workload Scale + Baseline->Target Metric**:

| ❌ AI Buzzword Resume Bullet | ✅ Human Engineer / PM Bullet |
|:---|:---|
| *Leveraged cutting-edge LLM RAG pipelines to revolutionize internal knowledge retrieval, boosting efficiency by 80%.* | *Built hybrid BM25 + BGE-M3 retrieval service over 1.4M Confluence pages; added cross-encoder reranking that raised Top-3 answer hit rate from 54% to 81% across 3,200 daily employee queries.* |
| *负责用户增长闭环体系搭建，通过多维精细化运营策略赋能转化率显著提升。* | *重构新客注册至首单漏斗：砍掉 3 步非必要实名表单并将优惠券前置至商详页，使首单 24h 转化率从 11.4% 提升至 16.9%（AB 实验样本 40 万 UV）。* |

---

### 4.4 Product Requirement Documents (PRDs & Specs)

**Rules:**
- Delete vision poetry (*"Create a delightful, frictionless AI copilot experience"*).
- Every PRD section must answer deterministic engineering questions: **Exact User Trigger -> Input Constraints -> System State Mutation -> Latency Budget -> Edge/Error Fallback -> Falsifiable Success & Rollback Metric.**

**Before (AI PRD Requirement):**
> The smart summary feature shall seamlessly synthesize long customer support threads, empowering agents to grasp context effortlessly and resolve tickets faster.

**After (Executable PRD Requirement):**
> - **Trigger:** Render summary card automatically when ticket message count `>= 6` AND total thread length `>= 400 tokens`; hide component on shorter threads.
> - **Latency & Fallback:** Stream first token within `600 ms` (P95); if LLM upstream exceeds `2,500 ms` or returns `5xx`, collapse card silently without blocking composer focus.
> - **Citation Grounding:** Every bullet must append `[#msg_id]` anchor scrolling to the source customer reply; strip bullets containing unverified refund amounts.
> - **Kill Criterion:** Roll back if agent manual edit/dismiss rate exceeds `35%` or median handle time fails to drop by `>= 12%` after 14-day 20% cohort rollout.

---

## 5. Domain 4: Spoken Video/Podcast Scripts & Creative Writing

### 5.1 Spoken Video & Podcast Scripts (`B站 / YouTube / 播客逐字口播稿`)

Written essays fail miserably when read into a microphone because **listeners cannot re-read a sentence or see punctuation.**

**Diagnostic Written-Leakage Tells:**
- Eye-only pointers: `the former / the latter` (`前者 / 后者`), `as mentioned above` (`如前文所述`), `respectively` (`分别`), parenthetical asides `(see chart)`.
- Left-branching Chinese noun monsters: `「那个在去年三季度因为供应链断裂而不得不推迟发布的旗舰芯片架构……」` (listener forgets the subject before reaching the verb).
- Literary connectors nobody says out loud: `Furthermore, Moreover, Consequently` / `此外、不仅如此、综上所述、换言之`.
- Cringey AI podcast stage directions: `[Host 1 chuckles warmly] Oh totally, Alex! What a fascinating perspective!`

**5-Step Ear-First Conversion Protocol:**
1. **15-Word / 18-Char Breath Rule (`气口切分`):** Break every long clause into units speakable in one relaxed breath.
2. **Subject-First Right-Branching:** Name the person/thing first, then layer short follow-up beats (*"Take Nvidia's H100. Last autumn, supply dried up overnight. Why? CoWoS packaging at TSMC hit a hard ceiling."*).
3. **Repeat Nouns Instead of Pronouns:** Replace `it / the former / 后者` with the concrete noun (`Postgres`, `老王那家工厂`) so listeners tuning back in never lose the thread.
4. **Spoken Signposts:** Replace `1, 2, 3` headers with natural ear hooks (`先说最反常识的一件事`, `但真正要命的问题在后头`, `"Now look at what happens to the bill"`).
5. **Read-Aloud Stumble Test:** Any consonant cluster or formal phrase your tongue trips over gets swapped for everyday speech (`进行深度的剖析` -> `咱们拆开算笔账`; `utilize` -> `use`).

**Before (CN — 书面稿直接当 B 站口播念):**
> 尽管高带宽内存（HBM）在提升大模型推理吞吐量方面发挥着至关重要的作用，但由于其三维堆叠封装工艺良率较低且产能受限，导致算力卡的整体制造成本居高不下，前者往往占据了后者物料清单成本的近一半。

**After (CN — 真人呼吸感 B 站硬核口播稿):**
> 决定大模型跑得快不快的头号瓶颈其实是显存，也就是咱们常听到的 HBM。这玩意儿有多贵呢？一张几万块的算力卡拆开看，光这一圈显存颗粒，就吃掉了差不多一半的硬件成本。为什么死活降不下来？因为它得把八层甚至十二层芯片像叠千层饼一样竖着焊在一起，中间打几千个微米级的孔。只要有一层歪了一丁点，整颗全废。

---

### 5.2 Creative Writing & Narrative Nonfiction (`小说与非虚构文学去 AI 味`)

LLMs trained on amateur web fiction and purple prose default to melodramatic clichés, over-explained emotions, and tidy moral epiphanies at the end of every scene.

**LLM Fiction Cliché Blacklist (Purge Immediately):**
- **English Sensory & Body Clichés:** *the metallic tang of blood and ozone*, *a chill / shivers ran down her spine*, *let out a breath she didn't realize she was holding*, *heart hammered against his ribs*, *knuckles whitened*, *voice barely above a whisper*, *eyes narrowed imperceptibly*, *neon lights bleeding into rain-slicked asphalt*, *a symphony / tapestry / kaleidoscope of unspoken emotions*, *time seemed to stand still*, default unprompted character names (*Elara, Lyra, Kael, Marcus Vance, Elena Rostova*).
- **Chinese AI 小说/故事套话：** `空气中弥漫着……的气息`、`命运的齿轮在这一刻悄然转动`、`嘴角勾起一抹不易察觉的弧度（三分凉薄四分漫不经心）`、`眼底闪过一丝复杂难明的情绪`、`心脏仿佛被一只无形的大手死死攥住`、`时间仿佛在这一刻按下了暂停键`。
- **The "Epiphany Tail" Disease:** Ending every scene with 2–3 sentences summarizing the theme (*"Watching the train vanish into the fog, he finally understood that letting go wasn't defeat; it was the beginning of freedom."*).

**4 Craft Rules for Human Literary Texture:**
1. **Stage Objects, Delete Emotion Labels:** Never write `"she said, masking her resentment."` Give her a specific physical task (`She scraped the burnt toast into the sink without looking up and asked if he wanted eggs`). Let the reader supply the emotion.
2. **Trade Lyric Adjectives for Mundane Nouns:** Specificity lives in slightly ugly, dated, concrete nouns—a cracked plastic parking pass, lukewarm vending-machine barley tea, a 2014 Honda Odyssey with one mismatched fender—not *"ethereal twilight shadows."*
3. **Asymmetric, Oblique Dialogue:** Real people dodge questions, interrupt, change the subject to parking fees, or answer five lines too late. Ban characters delivering polished three-sentence speeches about their trauma.
4. **Lop Off the Last Two Sentences:** After drafting a scene, test deleting the final summarizing paragraph. Ending on a concrete gesture or an unanswered line trusts the reader and instantly kills AI moralizing.

**Before (EN — Typical LLM Fiction Scene):**
> Rain lashed against the diner window, casting neon reflections across the worn formica table between them. Sarah wrapped her trembling hands around the porcelain mug, letting out a breath she didn't know she had been holding. The air between them felt thick with unspoken regrets—a fragile tapestry of ten years unraveling in silence.
> "I got the job in Chicago," Marcus said, his voice barely above a whisper, eyes heavy with guilt.
> A cold shiver ran down Sarah's spine, her heart hammering against her ribs. Yet as she looked at him, she realized that holding onto the past would only break them both. Sometimes love meant knowing when to walk away.

**After (EN — Subtextual, Concrete Human Scene):**
> Fluorescent grease clung to the laminated breakfast menu. Sarah used her thumbnail to peel a dried corner of ketchup off the salt shaker while Marcus checked his phone twice, face down, then face up again.
> "Chicago wants me there by the fourteenth," he said. "They're covering the U-Haul."
> She stopped picking at the glass. Outside, a delivery guy in a yellow poncho was trying to wedge a hand truck through the revolving door, backing traffic onto Broadway.
> "Keep the toaster oven," she said. "The cord shorts out if you bend it left, so don't pack it at the bottom."

**Before (CN — 典型 AI 故事腔):**
> 病房里的空气中弥漫着刺鼻的消毒水气息，令人窒息。陈默站在病床前，看着父亲鬓角斑白的白发，心脏仿佛被一只无形的大手狠狠揪住，眼眶不禁湿润了。曾经那个顶天立地的男人，如今却如此脆弱。这一刻他终于明白，子欲养而亲不待从来不是一句空话，成长的代价往往来得猝不及防。

**After (CN — 克制具象叙事):**
> 输液管里有一小截气泡卡在调节轮下面，陈默拿食指弹了三下没弹走。老头醒着，没睁眼，左手一直去摸枕头底下那串磨掉漆的电瓶车钥匙。
> 「车我锁住院部棚子里了，充电器拔了。」陈默说。
> 老头喉咙里哼了一声，翻过身冲着墙：「棚子东头漏雨，你明早挪到保安亭后边。」说完再没吭声。走廊推餐车的铝盆撞得哐当响，卖的是两块钱一碗的白粥。

---

## 6. Cross-Genre Anti-Overcorrection Guardrails (`跨体裁防矫枉过正红线`)

1. **Never Inject Slang Into High-Trust Documents:** Do not put internet slang, rhetorical fragments, or snark into incident postmortems, PRDs, grant proposals, SOPs, or formal workplace emails. High-trust genres prove humanity through **specificity and structural directness**, not informality.
2. **Never Strip Required Domain / ATS Keywords From Resumes & Docs:** Replacing `Kubernetes`, `idempotency`, or `HIPAA compliance` with "plain everyday words" harms technical precision and resume searchability—only strip *decorative* buzzwords (`synergistic`, `empower`, `blazingly`).
3. **Never Fake Lived Experience (`严禁伪造亲身经历与数据`):** When rewriting a Xiaohongshu review, Zhihu answer, SOP, or tech blog, if the user's input has no concrete personal anecdote or metric, **do not invent fake roommates, fake losses of 20,000 RMB, or fake latency benchmarks.** Leave explicit `[补充你的真实使用时长/具体槽点]` or `[insert measured p99 before/after]` brackets so the human author fills in real truth.
4. **Preserve Platform Formatting Mechanics:** Keep Markdown code fences untouched in READMEs/blogs; keep line lengths mobile-friendly on WeChat/Xiaohongshu without turning formal essays into 1-line LinkedIn broetry.
