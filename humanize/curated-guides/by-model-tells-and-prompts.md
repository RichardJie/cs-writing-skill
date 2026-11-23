# Model-Specific AI Tells & Counter-Prompts — Verified Primary Sources (`by-model-tells-and-prompts.md`)

> **Provenance & Zero Self-Invention Notice (`零AI自创铁律`)**
> Every table, word list, frequency ratio, structural observation, netizen quote, and counter-prompt in this file is extracted **verbatim or faithfully** from verified published papers, empirical benchmark JSONs, open-source GitHub repositories, and public forum/blog posts. Every section and entry cites its exact verified URL, author/username, platform/repository, and publication date or git commit SHA. No AI-invented rules, synthetic examples, or unverified claims appear anywhere in this file.

---

## Master Source Registry (Verified Upstream Repositories, Papers & Threads)

| # | Source / Title | Author(s) / Handle | Platform / Venue | Date / Commit SHA | Exact Verified URL |
|---|---|---|---|---|---|
| 1 | *Idiosyncrasies in Large Language Models* | Mingjie Sun, Yida Yin, Zhiqiu Xu, J. Zico Kolter, Zhuang Liu | ICML 2025 / arXiv | `arXiv:2502.12150` (Feb 2025) | `https://arxiv.org/abs/2502.12150` |
| 2 | `locuslab/llm-idiosyncrasies` (Official Code for `arXiv:2502.12150`) | Mingjie Sun, Yida Yin et al. (`locuslab`) | GitHub (MIT) | `e5333d01493963e5af44288fe2b9343ae6f13b9f` | `https://github.com/locuslab/llm-idiosyncrasies` |
| 3 | *Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models* | Samuel J. Paech, Allen G. Roush, Judah Goldfeder, Ravid Shwartz-Ziv | arXiv / ICLR 2026 Subm. | `arXiv:2510.15061` (Oct 2025) | `https://arxiv.org/abs/2510.15061` |
| 4 | EQ-Bench Slop Score Leaderboard & Per-Model JSON (`leaderboard_results.json`) | Samuel J. Paech (`EQ-bench`) | EQ-Bench | `2025-11-07T12:50:39Z` | `https://eqbench.com/slop-score.html` / `https://eqbench.com/data/leaderboard_results.json` |
| 5 | `sam-paech/slop-forensics` (Domain-Stratified Per-Model Slop Profiles) | Samuel J. Paech (`sam-paech`) | GitHub (MIT) | `c313f042620f027d49101da3256bd306b628071a` | `https://github.com/sam-paech/slop-forensics` |
| 6 | *AI Tells* (10,000 Human Articles vs. 90,000 AI Articles Across 9 Models) | Gregory Druck, PhD, José Luis Paredes, PhD, Ethan Smith | Graphite Research | 2026-09-16 | `https://graphite.io/research/ai-tells` |
| 7 | *AI Tells: Opus 5.5 Update* (9,974 Aligned Topics Across 10 Models + JSONs) | Gregory Druck, PhD, José Luis Paredes, PhD, Ethan Smith | Graphite Research | 2026-10-01 | `https://graphite.io/research/ai-tells-opus-5-5-update` |
| 8 | *Opus 5.5 loves to tell you 'this matters' (and other AI writing tells)* | Russell Brandom | TechCrunch | 2026-10-01 | `https://techcrunch.com/2026/10/01/opus-5-5-loves-to-tell-you-this-matters-and-other-ai-writing-tells/` |
| 9 | `larashero3-dotcom/lieflat-less-ai-tone` (*AI 中文写作特征实测* — 5.2M Chinese Chars) | `larashero3-dotcom` | GitHub (CC BY-NC 4.0) | `fe77df00a27cf94428632ad449a4aecdcb83db41` | `https://github.com/larashero3-dotcom/lieflat-less-ai-tone` |
| 10 | *Claudisms — A living banlist of AI-writing tells* (`claudisms.md`) | `claudisms.ai` (HN submission by `@weierstass`) | Web / Markdown (CC0 1.0) | 2026-09 | `https://claudisms.ai/` / `https://claudisms.ai/claudisms.md` |
| 11 | *Tropes.fyi — AI Writing Pattern Directory* & `writing-whip` Skill | Ossama Chaib (`@ossa-ma`, `ossama.is`) | Tropes.fyi / GitHub Gist / HN (CC BY 4.0) | 2026-02-20 | `https://tropes.fyi/` / `https://gist.github.com/ossa-ma/dae6f9571534f3fbd1266a384be00e11` |
| 12 | `haidrrrry/humanize-ai-writing` (`PROMPT.md` & `USAGE-IN-AI-TOOLS.md`) | `haidrrrry` | GitHub (MIT) | `7b376826c353f20583f21219aa0e62b8f799ce66` | `https://github.com/haidrrrry/humanize-ai-writing` |
| 13 | Hacker News Voice Rule #1 System Prompt Comment (`#49413456`) | `@tyre` | Hacker News | 2026 | `https://news.ycombinator.com/item?id=49413456` |
| 14 | Hacker News Threads on Claudeisms, GPTisms & Gemini Style | `@rsingel`, `@lexandstuff`, `@MizuHackerNews`, `@shthed`, `@cfcf14`, `@unholiness`, `@cvullit`, `@Revanche1367`, `@protoman3000` | Hacker News | 2024–2026 | `https://news.ycombinator.com/item?id=50579656` (and individual item URLs per entry) |
| 15 | *LLM Style Slop is Absolutely Everywhere* (+ Comments) | `silentbob`, `lukstafi`, `leogao`, `oligo` | LessWrong | 2026-04-28 | `https://www.lesswrong.com/posts/yBM2rQ6AJY6MoRGFQ/llm-style-slop-is-absolutely-everywhere` |
| 16 | *Best AI Prompt to Humanize AI Writing* | Sabrina Ramonov | Substack (`sabrina.dev`) | 2025-07-19 | `https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing` |
| 17 | *You. (How to train ChatGPT to write like you)* & *It's not [X], it's [Y].* | Ruben Hassid | Substack (`How to AI`) | 2025-10-29 / 2026 | `https://ruben.substack.com/p/emdash` / `https://ruben.substack.com/p/its-not-x-its-y` |
| 18 | `stop-slop` Gist (`SKILL.md`) | `Azayzel` | GitHub Gist | 2026 | `https://gist.github.com/Azayzel/8a16d601f8b74457ee422ff8ea9bb3ce` |
| 19 | `hylarucoder/ai-flavor-remover` (Tested on Gemini 2.5 Pro vs. Tencent Zhuque) | `hylarucoder` | GitHub | 2025 | `https://github.com/hylarucoder/ai-flavor-remover` |
| 20 | 《没有AI味，也许才是人类最后的浪漫》（DeepSeek 口癖词、动作癖与质数执念实测） | 毛渝川（谈资） | 腾讯新闻 | 2025-08-12 | `https://news.qq.com/rain/a/20250812A07WLC00` |
| 21 | 《DeepSeek创始人梁文峰写的除夕感言》真伪辨析与“DeepSeek味”拆解帖 | `@puffmolly`, `@veritas`, `@堕落的猴子`, `@tobyma` 等 | USCardForum (美卡论坛) | 2025-01-29 | `https://www.uscardforum.com/t/topic/348058` |
| 22 | 《消除“罪证”：给写作去除“AI味”的不完全手册（2026版）》（“豆包体”与 Prompt 弹药库） | 蒋雨恬（公众号「有三思 U Sense」） | 36Kr Europe | 2026-05-25 | `https://eu.36kr.com/zh/p/3824601267196037` |
| 23 | `weijt606/anti-vibe-writing` (`patterns-to-remove.md`, `chinese-patterns-to-remove.md`, `rewrite-prompt-template.md`) | `weijt606` | GitHub (MIT) / `ruanyf/weekly#10438` | v1.9.0 (2026) | `https://github.com/weijt606/anti-vibe-writing` |
| 24 | `hellogit2021/avoid-ai-writing-cn`（知乎圈子“去AI味写作技巧”社区维护） | `hellogit2021` / 知乎“去AI味写作技巧”圈子 | GitHub (MIT) / 知乎圈子 | v1.0.17 (2026) | `https://github.com/hellogit2021/avoid-ai-writing-cn` / `https://www.zhihu.com/ring/host/2054459419904292311` |
| 25 | `MrGeDiao/shuorenhua`（说人话：Claude Opus 5.5 vs. Codex GPT-6.1-sol vs. Gemini/DeepSeek 实测对比） | `MrGeDiao` | GitHub (MIT) | v2.7.1 (2026) | `https://github.com/MrGeDiao/shuorenhua` |
| 26 | `shaozheng0503/Tech-Blog-AI-Computing` (`去ai味道提示词模版.md`) | `shaozheng0503` | GitHub | 2025 | `https://github.com/shaozheng0503/Tech-Blog-AI-Computing/blob/main/%E5%8E%BBai%E5%91%B3%E9%81%93%E6%8F%90%E7%A4%BA%E8%AF%8D%E6%A8%A1%E7%89%88.md` |
| 27 | 《豆包、通义、Kimi、DeepSeek深度测评：职场人到底该选谁？》 & 《AI写作助手Kimi、豆包、DeepSeek怎么选？》 | 值得买20位作者综述 / 企鹅号「派派时刻」 | 什么值得买 / 腾讯云开发者社区 | 2026-07-03 / 2026-07-17 | `https://post.smzdm.com/p/anv77mr3/` / `https://developer.cloud.tencent.com/news/4271913` |
| 28 | 《88万篇文本实测：越让AI润色，全网文章越像一个人写的》 | 值得买111位作者综述（引述开智学堂、知乎、小红书、微博、USC Dehghani 团队） | 什么值得买 | 2026-09-23 | `https://post.smzdm.com/p/ad79kpnx/` |

**Preserved Upstream Repositories in `../upstream-skills/` (`.git` stripped, verbatim upstream files + licenses):**
- `../upstream-skills/03-models-and-stylometry-data/lieflat-less-ai-tone/` (`LICENSE`, `README.md`, `README.en.md`, `RESEARCH.md`, `RESEARCH.en.md`, `SKILL.md`, `DETECT.md`, `references/semantic-criteria.md`) — `https://github.com/larashero3-dotcom/lieflat-less-ai-tone` @ `fe77df00a27cf94428632ad449a4aecdcb83db41`
- `https://claudisms.ai/claudisms.md` — *Claudisms* living CC0 1.0 Public Domain catalog (confirmed entries documented in §3.2 below)
- `../upstream-skills/03-models-and-stylometry-data/ossa-ma-writing-whip/writing-whip-SKILL.md` — `https://gist.github.com/ossa-ma/dae6f9571534f3fbd1266a384be00e11` (CC BY 4.0)
- `../upstream-skills/03-models-and-stylometry-data/haidrrrry-humanize-ai-writing/` (`LICENSE`, `README.md`, `PROMPT.md`, `USAGE-IN-AI-TOOLS.md`) — `https://github.com/haidrrrry/humanize-ai-writing` @ `7b376826c353f20583f21219aa0e62b8f799ce66` (MIT)
- `../upstream-skills/02-chinese-and-bilingual/ai-flavor-remover/README.md` — `https://github.com/hylarucoder/ai-flavor-remover`

---

## Part I: Published Empirical Cross-Model Idiosyncrasy & Slop Studies

### 1.1 Sun et al. (`arXiv:2502.12150`, ICML 2025) — *Idiosyncrasies in Large Language Models*
- **Authors:** Mingjie Sun (CMU), Yida Yin (UC Berkeley), Zhiqiu Xu (UPenn), J. Zico Kolter (CMU), Zhuang Liu (Princeton)
- **URLs:** `https://arxiv.org/abs/2502.12150` | Code: `https://github.com/locuslab/llm-idiosyncrasies` (commit `e5333d01493963e5af44288fe2b9343ae6f13b9f`, MIT License)
- **Models Evaluated (Appendix A.1, Nov 28, 2024 – Feb 6, 2025):**
  - **Chat APIs (`chat`):** `GPT-4o-2024-08-06` (ChatGPT), `Claude-3.5-Sonnet-20241022` (Claude), `Grok-Beta` (Grok-2), `Gemini-1.5-Pro-002` (Gemini), `DeepSeek-Chat` (DeepSeek-V3), 11,000 UltraChat prompts per model (10K train / 1K held-out validation).
  - **Instruct & Base LLMs (`instruct` / `base`):** `Llama3.1-8b`, `Gemma2-9b`, `Qwen2.5-7b` (plus `Qwen2.5` 7B/14B/32B/72B size study), `Mistral-v3-7b`.

#### A. Empirical Separability & Transformation Ablations (Verbatim Numbers from Tables 1–7)
- **5-way Chat API classification (`LLM2vec`):** **97.1%** validation accuracy (vs. 20.0% random chance). Pairwise accuracies: ChatGPT vs. Claude **99.3%**, ChatGPT vs. Gemini **98.7%**, ChatGPT vs. DeepSeek **97.2%**, Claude vs. Grok **99.7%**, Claude vs. Gemini **99.6%**, Claude vs. DeepSeek **99.6%**, Gemini vs. DeepSeek **99.9%**.
- **4-way Instruct / Base classification (`Llama`, `Gemma`, `Qwen`, `Mistral`):** **96.3%** (instruct) and **87.3%** (base).
- **Within-family size classification (`Qwen2.5` 7B / 14B / 32B / 72B Instruct, Table 2):** **59.8%** 4-way accuracy (chance 25%); binary `14B` vs. `72B` reaches **85.5%**; `Qwen2.5-7B` base vs. instruct reaches **96.8%**.
- **Prompt-level format & length interventions (Table 4, Instruct LLMs):** Original **96.3%** $\rightarrow$ single-paragraph $\le 100$-word length control **93.0%** $\rightarrow$ plain-text-only (no bold/italic/lists/markdown/HTML) format control **91.4%**.
- **Isolation of Word Choice vs. Order vs. Markdown vs. Semantics (Tables 6, 7, 8):**
  - Removing all punctuation/markdown: **95.1%** (chat) / **93.8%** (instruct).
  - Randomly shuffling word order: **88.9%** (chat) / **88.9%** (instruct) — proving word-level lexical distributions alone carry massive model-specific signal, whereas letter-level shuffling drops accuracy to **39.1%**.
  - Retaining **only Markdown formatting skeleton** (replacing all text with `xxx`, Table 7): **73.1%** (chat APIs) and **77.7%** (instruct LLMs), vs. **38.5%** on base LLMs.
  - Rewriting outputs via external `GPT-4o-mini` (Table 8): Paraphrasing **91.4%**, Translating into Chinese **91.8%**, Summarizing into one paragraph **58.1%** (chat APIs).
  - Leave-one-out model similarity (Figure 9, Section 5): When excluded from training, **Grok** (82.8%), **Claude**, and **Gemini** outputs are predominantly classified as **ChatGPT**; **ChatGPT** (55.9%) and **DeepSeek-V3** (76.0%) outputs are predominantly classified as synthetic-data-trained **Phi-4** (and vice versa).

#### B. Verbatim Top-10 Characteristic Phrases per Model (TF-IDF Logistic Regression Coefficients, Figure 6 & Figure 15a)
Extracted verbatim from `figs/representative_phrases/top_words_chat_v3.pdf` and `figs/representative_phrases/top_words.pdf` in `arXiv:2502.12150`:

| Model Group | Model | Top-10 Characteristic Unigrams / Bigrams (Ordered Top-to-Bottom in Paper Figures) |
|---|---|---|
| **Chat APIs (Fig. 6)** | **GPT-4o** | `such`, `such as`, `enhance`, `involves`, `certainly`, `overall`, `sure`, `utilize`, `various`, `typically` |
| **Chat APIs (Fig. 6)** | **Claude (3.5 Sonnet)** | `here`, `according to`, `according`, `the text`, `while`, `based on`, `here’s a summary`, `appears to`, `both`, `when` |
| **Chat APIs (Fig. 6)** | **Grok (Grok-2)** | `which`, `where`, `not`, `here`, `here is`, `remember`, `might`, `but also`, `not only`, `helps in` |
| **Chat APIs (Fig. 6)** | **Gemini (1.5 Pro)** | `crucial`, `other`, `even`, `here’s a breakdown`, `key improvements`, `doesn’t`, `within`, `essentially`, `also`, `etc` |
| **Chat APIs (Fig. 6)** | **DeepSeek (V3)** | `below is`, `in summary`, `for example`, `below`, `certainly`, `summary`, `may`, `certainly! below`, `know if`, `example` |
| **Instruct LLMs (Fig. 15a)** | **Llama (3.1-8B)** | `including`, `the following`, `example use`, `such as`, `use case`, `which`, `explanation the`*, `that`, `2020`, `summary` |
| **Instruct LLMs (Fig. 15a)** | **Gemma (2-9B)** | `essentially`, `know if`, `me know`, `let me`, `here’s a breakdown`, `breakdown`, `states that`, `specific`, `remember`, `states` |
| **Instruct LLMs (Fig. 15a)** | **Qwen (2.5-7B)** | `certainly`, `below is`, `certainly! here`, `certainly! below`, `enhance`, `detailed`, `these`, `can`, `broader`, `certainly! the` |
| **Instruct LLMs (Fig. 15a)** | **Mistral (v3-7B)** | `title`, `absolutely`, `as`, `also`, `help`, `title comprehensive`, `for`, `an`, `however`, `during` |

*\*Paper Footnote 1: "In Llama of instruct LLMs, the phrase 'explanation the' corresponds to a markdown header or bold text for 'explanation' followed by a new sentence starting with 'the'."*

#### C. Verbatim Top-10 First-Word Distributions per Model (Figure 7 & Figure 16a)
Single-token truncation already yields ~50% 5-way accuracy on Chat APIs (Section 2.2). Extracted verbatim from `figs/first_word/first_words_chat.pdf` and `figs/first_word/first_words_instruct.pdf`:
- **ChatGPT (GPT-4o):** `the`, `title`, `certainly`, `creating`, `to`, `in`, `here`, `sure`, `yes`, `as`
- **Claude (3.5 Sonnet):** `here` (>0.32 probability!), `based`, `the`, `according`, `title`, `yes`, `how`, `this`, `from`, `in`
- **Grok (Grok-2):** `here`, `the`, `certainly`, `in`, `title`, `to`, `creating`, `yes`, `introduction`, `step`
- **Gemini (1.5 Pro):** `the` (>0.30 probability), `this`, `python`, `elara` (#4 most frequent opening word across UltraChat responses!), `yes`, `here`, `while`, `rain`, `creating`, `my`
- **DeepSeek (V3):** `the`, `certainly`, `title`, `creating`, `to`, `here`, `comprehensive`, `step`, `yes`, `based`
- **Llama-3.1-8B-Instruct:** `the`, `here`, `according`, `based`, `as`, `in`, `to`, `title`, `comprehensive`, `it`
- **Gemma-2-9B-Instruct:** `the`, `here`, `this`, `as`, `please`, `you`, `okay`, `it`, `python`, `according`
- **Qwen-2.5-7B-Instruct:** `certainly` (#1 first word, >0.21 probability!), `the`, `in`, `title`, `to`, `creating`, `based`, `comprehensive`, `according`, `sure`
- **Mistral-v3-7B-Instruct:** `title` (#1 first word, >0.33 probability!), `the`, `in`, `to`, `here`, `absolutely`, `yes`, `based`, `subject`, `creating`

#### D. Function-Word & Markdown Formatting Idiosyncrasies (Sections 3.1–3.2 & Appendix B.4)
- **Function-word drop in Claude:** *"Claude has much lower frequencies for words like 'the', 'and', 'to', and 'of' than other chat APIs."* (Section 3.1, p. 5).
- **Bold & Header formatting (GPT-4o vs. Claude):** *"Claude (yellow) has a high density at zero in the bold text and header count distributions, indicating that it generates many responses without bold texts or headers... ChatGPT tends to emphasize each key point within enumerations in bold (`1. **Deliver Exceptional Service**: ...`) and highlight a title with markdown headers, but Claude formats text with simple enumeration and bullet points."* (Section 3.2, p. 6 & `figs/markdown_features_examples.pdf`).
- **Italic formatting (Gemini & Gemma2):** *"Intriguingly, Gemini uses much more italic texts (a lower density at zero in the italic text) than other chat APIs, where similar observations can be found on Gemma2."* (Appendix B.4, p. 14).

---

### 1.2 Paech et al. (`arXiv:2510.15061`, Oct 2025) — *Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models*
- **Authors:** Samuel J. Paech (Independent / EQ-Bench), Allen G. Roush (Thoughtworks), Judah Goldfeder (Columbia University), Ravid Shwartz-Ziv (NYU)
- **URLs:** `https://arxiv.org/abs/2510.15061` | Code: `https://github.com/sam-paech/auto-antislop` (MIT License)

#### A. Extreme Single-Model Overrepresentation vs. Human Baselines (`gemma-3-12b`, Table 1)
Computed over 2,000 creative writing samples per model vs. `wordfreq` + Reddit/Project Gutenberg human baselines:
- **Words:** `elara` (**85,513×**), `unsettlingly` (**3,833×**), `shimmered` (**2,882×**), `stammered` (**2,043×**).
- **Trigrams (stopwords removed):** `heart hammered ribs` (**1,192×**), `voice trembling slightly` (**731×**), `said voice devoid` (**693×**), `felt profound sense` (**550×**).
- **Mistral-Small-3.1-24B-Instruct-2503 extreme trigram count (Appendix I, p. 17):** Produced **102 `"eyes never leaving"`** trigrams and **62 `"voice barely whisper"`** trigrams across just 96 writing prompts.
- **Why negative-prompt wordlists fail ("Pink Elephant Problem", Section 1, p. 2):** *"Instructing the model to avoid a set of banned vocabulary has limited efficacy and may induce a backfire effect due to the 'Pink elephant problem' (Castricato et al., 2024)."*

#### B. Cross-Model Shared Slop Core Across 67 AI Models (Tables 3 & 4, Appendix G)
Percentage of 67 tested LLMs in which the token/phrase appears inside that model's top-120 most over-represented words or top-40 most over-represented trigrams relative to human writing:
- **Top 20 Overlapping Words (% of 67 models):** `flickered` (98.5%), `flicker` (94.0%), `flickering` (92.5%), `leaned` (82.1%), `muttered` (82.1%), `gaze` (80.6%), `grinned` (80.6%), `containment` (77.6%), `gestured` (77.6%), `addendum` (74.6%), `murmured` (73.1%), `nodded` (73.1%), `glint` (68.7%), `hesitated` (68.7%), `whispered` (68.7%), `blinked` (64.2%), `hummed` (64.2%), `faintly` (62.7%), `leans` (62.7%), `unreadable` (62.7%).
- **Top 20 Overlapping Stopword-Stripped Trigrams (% of 67 models):** `voice barely whisper` (68.7%), `said voice low` (61.2%), `air thick scent` (49.3%), `took deep breath` (44.8%), `smile playing lips` (43.3%), `something else something` (37.3%), `said voice barely` (35.8%), `voice barely audible` (35.8%), `take deep breath` (32.8%), `could shake feeling` (31.3%), `eyes never leaving` (29.9%), `casting long shadows` (28.4%), `says voice low` (26.9%), `something else entirely` (26.9%), `heart pounding chest` (25.4%), `one last time` (23.9%), `spreading across face` (22.4%), `air thick smell` (19.4%), `could help feel` (19.4%), `long shadows across` (19.4%).

#### C. Empirical `"Not x, but y"` Rate per 1,000 Characters by Model (Figure 8, Appendix C `iclr2026/figures/not-x-but-y.png`)
| Model | `"Not x, but y"` Hits per 1,000 Characters | Ratio vs. Human Baseline (`0.17`) |
|---|---|---|
| **`qwen3-4b` (baseline)** | **1.10** | **6.47×** |
| **`gemma-3-4b-it`** | **0.55** | **3.24×** |
| **`gemini-2.5-flash`** | **0.49** | **2.88×** |
| **`chatgpt-4o-latest`** | **0.48** | **2.82×** |
| **`Mistral-Small-3-2-2506`** | **0.25** | **1.47×** |
| **`claude-opus-4.1`** | **0.22** | **1.29×** |
| **Human baseline** | **0.17** | **1.00×** |
| **`o3` (OpenAI)** | **0.10** | **0.59×** |
| **`qwen3-4b` (Antislop regex ban)** | **0.00** | **0.00×** |

#### D. Model-Family Phylogenetic Clustering of Slop Fingerprints (Figure 13, Appendix I `iclr2026/figures/slop_clustering.png`)
Hierarchical clustering on average rank-distance of top-200 over-represented words & n-grams reveals tight intra-family basins:
- **Anthropic Claude Cluster:** `claude-sonnet-4`, `claude-opus-4`, `claude-3.5-sonnet`, and `claude-3.7-sonnet` form a single self-contained branch separated from all OpenAI, Google, and Meta models.
- **Meta Llama Cluster:** `llama-3.1-70b-instruct`, `llama-3.1-405b-instruct`, `llama-3.1-8b-instruct`, `llama-4-maverick`, and `llama-4-scout` form the tightest family cluster (cluster distance < 0.62).
- **Google Gemma / Gemini & DeepSeek-V3.1 Cluster:** `gemma-3-27b-it`, `gemma-3-12b-it`, `gemma-2-9b-it`, and `gemini-2.0-flash-001` cluster together, adjacent to `gemini-2.5-pro-preview`, `deepseek-chat-v3.1`, and `deepseek-r1-0528`.
- **OpenAI / Kimi / DeepSeek-V3-0324 Cluster:** `kimi-k2`, `gpt-5-2025-08-07`, and `o3` cluster on one sub-branch; `deepseek-chat-v3-0324`, `chatgpt-4o-latest`, `mistral-small-3.2-24b-instruct-2506`, and `deepseek-r1` form the neighboring sub-branch; legacy `gpt-4-0314` and `gpt-3.5-turbo-0613` pair on a separate older branch.

#### E. Verbatim Upstream Regex Blocklist for `"not x, but y"` (Appendix J, `arXiv:2510.15061`)
Published verbatim in `arxiv_submission.tex` lines 1027–1040 (`https://arxiv.org/abs/2510.15061`):
```yaml
regex_patterns: [
  "\\b(?:\\w+n(?:['’]t)|not\\s+(?:just|only|merely|because))\\s+(?:(?![.;:?!…]).){1,100}?[.;:?!…]\\s*(?:it|they|you)(?:['’](?:s|re|m))?\\b(?!\\s+(?:was|were|is|are|wasn['’]t|weren['’]t|isn['’]t|aren['’]t|ain['’]t)\\b)(?:\\s*[*…]?\\s*)?(?!when\\b|then\\b|but\\b|and\\b|yet\\b)(?!right\\b)(?!normal\\b)(?!true\\b)(?!sure\\b)(?!only\\b)(?!still\\b)(?!rarely\\b)(?!already\\b)(?!wrong\\b)(?!want\\b)(?!just\\b)(?!couldn\\b)(?!could\\b)(?!saw\\b)(?!started\\b)(?!remember\\b)(?!struggled\\b)(?!watched\\b)(?!goal\\b)(?!took\\b)(?!kept\\b)(?!reminded\\b)(?!time\\b)(?!have\\b)(?!acted\\b)(?!smiled\\b)(?!think\\b)(?!give\\b)(?!grab\\b)(?!gave\\b)(?!turn\\b)(?!justify\\b)(?!\\w+ly\\b)(?=[a-z]{4,}\\b)[a-z]+\\w*",

  "\\b(?:\\w+n(?:['’]t)|not)\\s+(?:just|only|merely)?\\s*(?:(?![-–—]|[.?!…]).){1,80}?[-–—]{1,2}\\s*\\w+(?:['’]\\w+)?\\s+",

  "\\b(?:wasn['’]t|weren['’]t|isn['’]t|aren['’]t|ain['’]t|not)\\s+(?!\\b(?:minute|minutes|hour|hours|day|days|year|years|second|seconds)\\b)(?!with\\b)(?!even\\b)(?:(?![.;:?!…]).){2,120}?[.;:?!…]\\s*(?:it|they|you|that)(?:\\s+(?:was|were|is|are)\\b(?:\\s+[*_~]?\\w+[*_~]?)?|(?:['’](?:s|re|m))\\b(?:\\s+[*_~]?\\w+[*_~]?)?)",

  "\\bno\\s+longer\\s+(?:just|only|merely)?\\s+[^.;:?!…]{1,120}[.;:?!…]\\s*(?:it|they|you)\\s+(?:is|are|was|were)\\b(?:\\s+[*_~]?\\w+[*_~]?)?",

  "\\b(?:wasn['’]t|weren['’]t|isn['’]t|aren['’]t|ain['’]t|not)\\s+(?:just|only|merely)?\\s*(?:(?!\\bbut\\b|[.?!…]).){1,80}?[,;:\\-–—]\\s*but\\s+(?!I\\b)(?:also\\s+)?"
]
```

---

### 1.3 EQ-Bench Slop Score Leaderboard (`eqbench.com`) & `sam-paech/slop-forensics`
- **Author:** Samuel J. Paech (`EQ-bench` / `sam-paech`)
- **URLs:** `https://eqbench.com/slop-score.html` | Raw JSON: `https://eqbench.com/data/leaderboard_results.json` (generated `2025-11-07T12:50:39.490Z`) | Repo: `https://github.com/sam-paech/slop-forensics` (commit `c313f042620f027d49101da3256bd306b628071a`, MIT License)

#### Verbatim 23-Model Slop Score Benchmark Table (`eqbench.com/data/leaderboard_results.json`)
| Model | Slop Words / 1k Words | Slop Trigrams / 1k Words | `"Not X, but Y"` / 1k Chars | N-gram Repetition Score | MATTR-500 Diversity | Avg Sentence Len (Words) |
|---|---|---|---|---|---|---|
| `sam-paech/gemma-3-27b-it-antislop` | 5.61 | 0.18 | 0.459 | 6.24 | 0.599 | 11.84 |
| **`human-baseline`** | **6.90** | **0.09** | **0.044** | **3.93** | **0.507** | **14.59** |
| `claude-sonnet-4-5` | 9.72 | 0.23 | 0.171 | 7.43 | 0.578 | 11.42 |
| `moonshotai/kimi-k2-0905` | 10.12 | 0.08 | 0.174 | 3.96 | 0.624 | 17.25 |
| `moonshotai/kimi-k2` | 12.95 | 0.14 | 0.196 | 4.14 | 0.622 | 16.53 |
| `claude-sonnet-4-20250514` | 13.53 | 0.33 | 0.214 | 6.47 | 0.597 | 13.85 |
| `openai/gpt-5-mini` | 15.44 | 0.21 | 0.129 | 3.62 | 0.578 | 17.22 |
| `openai/gpt-5-nano` | 16.92 | 0.29 | 0.303 | 5.40 | — | — |
| `openrouter/polaris-alpha` | 17.21 | 0.23 | 0.193 | 5.63 | — | — |
| `openai/o3` | 19.89 | 0.23 | 0.086 | 2.90 | 0.665 | 15.30 |
| `inclusionai/ling-1t` | 22.92 | 0.29 | 0.801 | 3.92 | — | — |
| `openai/chatgpt-4o-latest` | 23.26 | 0.79 | 0.245 | 6.51 | 0.553 | 13.91 |
| `qwen/qwen3-4b` | 23.63 | 0.88 | 0.722 | 9.84 | 0.439 | 17.25 |
| `meta-llama/llama-4-maverick` | 23.73 | 1.12 | 0.130 | 13.60 | 0.462 | 18.75 |
| `deepseek/deepseek-v3.2-exp` | 23.95 | 0.52 | 0.569 | 4.84 | 0.562 | 15.21 |
| `mistralai/Mistral-Small-3.2-24B-Instruct-2506` | 26.05 | 1.09 | 0.151 | 20.12 | — | — |
| `mistralai/mistral-nemo` | 26.41 | 1.01 | 0.230 | 10.09 | — | — |
| `z-ai/glm-4.5` | 28.45 | 0.79 | 0.424 | 5.37 | 0.572 | 15.11 |
| `google/gemma-3-27b-it` | 32.27 | 0.78 | 0.577 | 10.17 | 0.569 | 13.44 |
| `google/gemma-3-12b-it` | 36.35 | 1.00 | 0.308 | 21.23 | — | — |
| `google/gemini-2.5-flash` | 40.16 | 0.95 | 0.386 | 7.39 | 0.572 | 15.75 |
| `deepseek/deepseek-r1` | 40.16 | 0.70 | 0.137 | 5.13 | 0.618 | 12.53 |
| `google/gemma-3-4b-it` | 40.44 | 0.59 | 0.811 | 12.45 | — | — |

*(Per-model word hits, trigram hits, and domain-stratified creative writing vs. essay profiles from `eqbench_leaderboard.json` and `sam-paech/slop-forensics` are detailed under each respective model family in Parts II–V below.)*

---

### 1.4 Graphite Research (Sept 16 & Oct 1, 2026) — *AI Tells* & *AI Tells: Opus 5.5 Update*
- **Authors:** Gregory Druck, PhD (Chief AI Officer), José Luis Paredes, PhD (Senior Data Scientist), Ethan Smith (CEO) — Graphite Research; reported by Russell Brandom in TechCrunch
- **URLs:**
  - Original 9-Model Study (Sept 16, 2026): `https://graphite.io/research/ai-tells`
  - 10-Model Opus 5.5 Update (Oct 1, 2026): `https://graphite.io/research/ai-tells-opus-5-5-update`
  - TechCrunch Report (Oct 1, 2026): `https://techcrunch.com/2026/10/01/opus-5-5-loves-to-tell-you-this-matters-and-other-ai-writing-tells/`
- **Methodology:** Topically aligned parallel corpus of **10,000 Common Crawl human articles published pre-ChatGPT** (before Nov 30, 2022) paired with **100,000 AI articles** generated from summaries across 10 models (`GPT-4.1`, `GPT-5`, `GPT-5.6 Sol`, `GPT-6 Astra`, `Claude Opus 4`, `Claude Opus 4.6`, `Claude Opus 5`, `Claude Opus 5.5`, `Gemini 2.5 Pro`, `Gemini 3.1 Pro`). A "tell" is defined as a word ($\ge 500$ docs), bigram ($\ge 250$ docs), trigram ($\ge 100$ docs), or 7-token gapped frame ($\ge 120$ docs) occurring at $\ge 2\times$ the length-normalized human rate.

#### Key Cross-Model Empirical Findings (Verbatim from Graphite Reports)
1. **Family Specificity & Version Drift:** Across the 9 models in the initial study, Graphite identified **12,877 unique tells** (2,355 to 3,746 tells per model). **65% of tells are unique to a single model family**, and **55% to 72% of tells are unique to one version** between consecutive releases of the same family (e.g., only 45% overlap between `GPT-5.6 Sol` and `GPT-6 Astra`; `Claude Opus 4` $\rightarrow$ `4.6` $\rightarrow$ `5` $\rightarrow$ `5.5` tell counts: `3,746` $\rightarrow$ `3,059` $\rightarrow$ `2,666` $\rightarrow$ `2,548`).
2. **Cross-Family Signature Contrast Table (`graphite.io/research/ai-tells`):**
   - **Evaluative Adjectives (vs. Human Rate):**
     - `GPT-6 Astra`: `dependable` (**59×**), `practical` (**26×**), `meaningful` (**13×**)
     - `Claude Opus 5`: `deliberate` (**26×**), `steady` (**6×**), `measured` (**4.2×**) | `Claude Opus 5.5`: `dependable` (**23×**), `steady` (**11×**), `thoughtful` (**9×**), `meaningful` (**8×**)
     - `Gemini 3.1 Pro`: `profound` (**25×**), `immense` (**22×**), `incredibly` (**18×**)
   - **Transitions (vs. Human Rate):**
     - `GPT-6 Astra`: `another dimension` (**117×**), `together these` (**95×**)
     - `Claude Opus 5`: `looking ahead the` (**33×**), `what comes next` (**28×**) | `Claude Opus 5.5`: `looking ahead the` (**40×**), `adds another layer` (**27×**), `what comes next` (**24×**), `in practice` (**7×**)
     - `Gemini 3.1 Pro`: `ultimately this` (**78×**), `furthermore the` (**43×**), `additionally the` (**8.6×**)
   - **Definition by Contrast (vs. Human Rate):**
     - `GPT-6 Astra`: `the _ is not simply` (**576×**), `rather than relying` (**187×**), `not simply` (**157×**)
     - `Claude Opus 5`: `rather than merely` (**160×**), `less like a _ and more like` (**105×**), `rather than simply` (**43×**) | `Claude Opus 5.5`: `is more than a _ it` (**98×**), `rather than simply` (**32×**), `not only about` (**13×**), `instead it` (**8×**)
     - `Gemini 3.1 Pro`: `is not just a _ it is` (**153×**), `instead it is` (**29×**), `is not just` (**18×**)
   - **Flagging Importance (vs. Human Rate):**
     - `GPT-6 Astra`: `distinction matters` (**$\infty$**, 990 hits vs. 0 human), `matters because` (**357×**)
     - `Claude Opus 5`: `matters because` (**132×**), `matters more than` (**93×**) | `Claude Opus 5.5`: `this matters` (**116×**), `why _ matters` (**92×**), `just as important` (**13×**), `matters most` (**12×**)
     - `Gemini 3.1 Pro`: `absolutely essential` (**32×**), `remarkably` (**19×**)
3. **Em-Dash Overcorrection Across Families:**
   - `Claude Opus 5` used **2.92 em-dashes / 1k words** (near pre-ChatGPT human mean), whereas `Claude Opus 5.5` dropped **99%** to **0.015 em-dashes / 1k words**.
   - `GPT-6 Astra` uses em-dashes **88% less often** than pre-ChatGPT human writers (and 95% less than `GPT-5`).
   - `Gemini 3.1 Pro` almost completely eliminated em-dashes relative to `Gemini 2.5 Pro`.
4. **Mannered Prose & Word-Distribution Divergence (Jensen-Shannon Divergence):**
   - Mannered prose (Anthropic's definition: substituting metaphor and flourish for direct statement, human mean `6.65`): `Claude Opus 5` (`16.75`, ~2.5× human) and `Gemini 3.1 Pro` (~2.5× human) score highest; `Claude Opus 5.5` drops 37% to `10.57` (~1.6× human); `GPT-6 Astra` is `1.2×` human.
   - Unigram JSD from human writing: Only Claude is moving closer to human word distributions (`Opus 5` `0.064` $\rightarrow$ `Opus 5.5` `0.052`), whereas GPT is moving *further away* (`GPT-5.6 Sol` `0.101` $\rightarrow$ `GPT-6 Astra` `0.109`).
   - Human-specific markers missing in AI: Human writers use exclamation marks **>100× more often** than GPT/Claude/Gemini, use parenthetical asides far more often, use shorter words (mean `4.9` chars vs. AI `5.2–5.7`), have higher sentence-length standard deviation, and have *lower* within-article MTLD (`85.6` human vs. `127.1–153.6` AI, reflecting AI synonym cycling).

---

### 1.5 `larashero3-dotcom/lieflat-less-ai-tone` (2026) — *AI 中文写作特征实测* (5.2M Chinese Characters)
- **Author:** `larashero3-dotcom` (`lieflat.work`)
- **URLs:** `https://github.com/larashero3-dotcom/lieflat-less-ai-tone` (`RESEARCH.md`, `README.md`, `SKILL.md` @ commit `fe77df00a27cf94428632ad449a4aecdcb83db41`, CC BY-NC 4.0)
- **Corpus Design:**
  - **Round 1 (629 Unpaired Chinese Articles, 2,826,972 Chinese chars, 95,551 sentences):** 5 models × 60 articles each (`claude-opus-4-6`, `deepseek-v4-pro`, `gemini-3.1-pro`, `gpt-5.6-sol`, `kimi-k3` = 300 AI articles, 1,179,105 chars) vs. 329 real Chinese human articles (1,647,867 chars) on the same 38 topics without style prompts or web search.
  - **Round 2 (270 Topic-and-Fact-Aligned Pairs, ~500,000 Semantic Judgments):** 270 human articles paired with 270 length- and fact-card-aligned AI articles (`GPT-5.6` × 135 + `Claude Opus 4.6` × 135), evaluated via paired Wilcoxon + Cliff's $\delta$ ($|\delta| \ge 0.33$ significant) across 90 script metrics and 9 semantic metrics.

#### A. Verbatim Round 1 Five-Model Chinese Stylometric Comparison (`RESEARCH.md` lines 265–276)
> *"同一特征在模型之间差一个数量级，不要按「某个模型的味」套判断。"*

| 中文特征 (Metric) | Claude (`claude-opus-4-6`) | DeepSeek (`deepseek-v4-pro`) | Gemini (`gemini-3.1-pro`) | GPT (`gpt-5.6-sol`) | Kimi (`kimi-k3`) | 人类对照 (Human Baseline) |
|---|---|---|---|---|---|---|
| **破折号 (`——` / 千汉字)** | 4.25 | **5.16** | 0.51 | 0.11 | 2.32 | 0.80 |
| **提示性冒号 (`核心是：` / 千汉字)** | 0.38 | **0.43** | 0.22 | 0.25 | 0.32 | 0.08 |
| **翻案腔 (`不是…而是` / 千汉字)** | 0.61 | 0.86 | 0.29 | **1.26** | 0.51 | 0.22 |
| **段首序数词** | **1.00** | 0.69 | 0.22 | 0.73 | 0.82 | — |
| **过长前置定语 (/ 千汉字)** | 0.64 | **0.65** | 0.48 | 0.06 | 0.22 | — |
| **问句小标题** | 0.043 | 0.086 | **0.173** | 0.008 | 0.000 | — |

#### B. Verbatim Round 2 Paired Chinese Model-Fingerprint Divergence: `GPT-5.6` vs. `Claude Opus 4.6` (`README.md` Section 3.2)
> *"破折号合并口径「不显著」，拆开是 GPT −0.54 / Opus +0.95——方向相反的两个真信号被合并抵消成假阴性。"*

| 指纹特征 (Fingerprint Metric) | `GPT-5.6` (Cliff's $\delta$ vs. Human) | `Claude Opus 4.6` (Cliff's $\delta$ vs. Human) | 实测方向与原文例证 (Empirical Direction & Verbatim Findings) |
|---|---|---|---|
| **破折号 (`——`)** | **$-0.54$** (比人类还少) | **$+0.95$** (100% 文章使用) | 方向完全相反。Opus 典型句：「在营收急剧收缩的压力下，公司迅速启动了大规模的营销开支削减——最先被砍掉的，正是搜索广告和效果投放」 |
| **每小句「的」字密度** | **$-0.75$** | **$+0.62$** | GPT「的」字比人类少，Opus 比人类多，方向完全相反 |
| **引号密度** | $\approx 0$ | **$-0.67$** | Opus 写中文长文明显不爱用引号，显著少于人类 |
| **分号 / 顿号** | **$+0.80$ / $+0.56$** | $-0.11$ / $+0.14$ | **GPT 专属特征**：爱用两个分号把三档并列场景串成一句长句，人类更常拆成三句 |
| **句子结构绕（GPT 三子项）** | 单动词句少 **$-0.72$**；静态句少 **$-0.71$**；主谓距离短 **$-0.62$** | 全部不显著 | **GPT 专属特征**：单动词撑一句的短直句稀少，偏爱一句连环堆叠 3–4 个动词（「利用…观察…再把…还原成…」），且把静态判断全写成动作过程 |
| **少提问（正文问句）** | **$-0.59$** | $-0.12$ | GPT 写文章明显不爱提问；Opus 与人类接近 |
| **长句少 / 中句多** | **$-0.68$ / $+0.81$** | $+0.05$ / $+0.04$ | **GPT 专属特征**：句长高度集中在 25–45 字中档，几乎没有 6–12 字短促收尾句，也极少 60 字以上长流水句 |
| **焦点后置** | $+0.05$ | **$+0.47$** | **Opus 专属特征**：新信息压在句尾，前半句全是铺垫（「定价权不在工厂手里，品牌归属也不在工厂手里，工厂只是全球供应链上那个沉默的、可以被随时替换的生产节点」） |
| **活跃暗喻密度** | `2.099` ($\approx$ 人类 `2.066`) | **`2.851`** | **Opus 专属特征**：合并口径 1.2× 全部由 Opus 拉高，GPT 暗喻量与人类无差异 |

#### C. Universal Validated Chinese AI Tells vs. Empirically Falsified Myths (`README.md` Sections 3.1, 3.3 & `SKILL.md` X-Tier)
- **Validated Cross-Model Chinese Signals (Significant in both GPT-5.6 & Opus 4.6):**
  1. **欧化翻案腔「不是 A 而是 B」：** GPT $\delta = +0.88$, Opus $\delta = +0.72$ (Round 1: AI `0.73` vs. Human `0.22`/千字, `3.4×` — strongest pure prose signal).
  2. **同义重命名 / 用词不敢重复 (`mtld`/`mattr`)：** GPT $\delta = +0.91$, Opus $\delta = +0.55$ (同一段内「优化／增强／提升／提高」或「版图→基地→项目→节点」轮换；重灾段 AI `20.6–22.5%` vs. 人类 `8.4%`).
  3. **分节切得太碎：** 小节长度方差 $\delta = -0.91 / -0.75$，小标题密度 $\delta = +0.65 / +0.83$，每篇小节数中位数 AI `7` vs. 人类 `1`.
  4. **过长前置定语（欧化）：** GPT $\delta = +0.48$, Opus $\delta = +0.54$（中心名词前挂 15–20+ 字修饰或连续多个「的」）.
  5. **结论提示冒号：** AI `2.1×` 人类（仅限「核心是：」「残酷的现实是：」等先摆结论再展开；冒号总密度人类反而更高 $\delta = -0.37 / -0.31$）.
  6. **衔接连环过长（零跳转）：** AI 段间明确承接 `98.9%` vs. 人类 `95.2%`；段间直接跳新话题人类 `7.2%`（每 14 段一次）vs. AI `2.1%`（每 50 段一次）；连续承接连环中位数 AI `7` vs. 人类 `2`.
  7. **高度同构三连句：** 连续三句逐字复用同一句法骨架，AI `29.4%` vs. 人类 `10.7%` (`2.75×`).
- **Empirically Falsified Folk Myths (`X 级清单 — 永不改，防误改`, `SKILL.md` lines 270–283):**
  - **正文设问句 / 问句：** 人类频率 `1.83/千字` vs. AI `0.10/千字` —— **人类是 AI 的 17 倍**，删问句反而更像 AI。
  - **比喻标记词密度：** 人类 `0.38/千字` vs. AI `0.16/千字` —— **人类是 AI 的 2.4 倍**（独立成段用比喻人类是 AI 的 8 倍）；AI 的问题是比喻贴切度差（硬套宏大意象如“窄门”“三根支柱”），不是比喻数量多。
  - **序数词小标题（一、二、三）：** 配对复测反转 —— 人类 `8.6%` vs. AI `4.9%`（AI 爱多分节，不爱用汉字序数编号）。
  - **「这意味着」复述 & 空转句引列表（「几种典型场景：」）：** 配对复测全部反向（人类用得更多）。
  - **「首先/其次/总之」连接词 & 「赋能/闭环/抓手」黑名单词：** 同题同事实配对复测下 $|\delta| \le 0.10$（对当代主力模型已基本失效）。
  - **句内排比：** 同字开头两项人类 `3.87` vs. AI `2.35` (`0.61×`)，只有跨句同构才是 AI 信号。

---

## Part II: OpenAI Family (`GPT-3.5` / `GPT-4` / `GPT-4o` / `GPT-4.5` / `o3` / `GPT-5` / `GPT-6 Astra`)

### 2.1 Empirical Word Lists, Frames & Generational Evolution

#### A. `GPT-4o` Empirical Profile — Sun et al. (`arXiv:2502.12150`, ICML 2025)
- **Source:** Mingjie Sun et al., *Idiosyncrasies in Large Language Models*, `https://arxiv.org/abs/2502.12150` (`figs/representative_phrases/top_words_chat_v3.pdf`, `figs/first_word/first_words_chat.pdf`, `figs/summarization/GPT-4o_summarization_gpt4o.pdf`, `figs/representative_phrases_examples.pdf`, `figs/markdown_features_examples.pdf`)
- **Top-10 Characteristic Phrases:** `such`, `such as`, `enhance`, `involves`, `certainly`, `overall`, `sure`, `utilize`, `various`, `typically`
- **Top-10 Response-Opening Words:** `the`, `title`, `certainly`, `creating`, `to`, `in`, `here`, `sure`, `yes`, `as`
- **Verbatim Highlighted Response Examples (Figure 4, p. 5):**
  - *"Our products feature innovative sustainable materials, `such as` …"*
  - *"`Certainly!` If you're looking for cheese alternatives to replace Brie in your …"*
  - *"`Overall`, while there are challenges, Tanzania is making progress …"*
  - *"`Sure`! Here's a simple guide to cooking a juicy salmon fillet: …"*
  - Markdown habit: Bolded lead-ins on numbered/bulleted lists (`1. **Deliver Exceptional Service**: The foundation of word-of-mouth marketing is consistent excellence...`, `**Ingredients:**`).
- **Verbatim 5-Point Empirical Judge Characterization (`figs/summarization/GPT-4o_summarization_gpt4o.pdf`):**
  > 1. **Descriptive and Detailed Tone:** Often uses narrative styles with an informative, engaging, or vivid tone.
  > 2. **Specific and Technical Word:** Employs descriptive and technical vocabulary, enhancing depth and specificity.
  > 3. **Structured and Contextual Opening Lines:** Typically begins with context-setting or narrative introductions.
  > 4. **Markdown Formatting for Organization:** Utilizes various markdown elements like headings, lists, and bold text for clarity.
  > 5. **Comprehensive and In-Depth Content:** Offers rich detail, focusing on explanations, background, and broader topics.

#### B. OpenAI Model Profiles Across Domains — EQ-Bench (`eqbench.com`) & `sam-paech/slop-forensics`
- **Sources:**
  - `https://eqbench.com/data/leaderboard_results.json` (`EQ-Bench Slop Score`)
  - `https://github.com/sam-paech/slop-forensics` (`results_by_domain/creative_writing/slop_profiles_creative_writing.json` & `results_by_domain/essays/slop_profile_results.json`, commit `c313f042620f027d49101da3256bd306b628071a`)
- **`openai/chatgpt-4o-latest`:**
  - *Mixed Benchmark (`eqbench_leaderboard.json`, $n=300$, slop/1k=`23.26`, `"not X, but Y"`/1k chars=`0.245`):*
    - **Top Slop Words (count):** `challenges` (221), `strategic` (168), `conclusion` (146), `strategies` (142), `broader` (120), `moreover` (101), `ensuring` (97), `crucial` (93), `organizational` (85), `ethical` (81), `outcomes` (71), `furthermore` (70), `shaping` (69), `whispered` (68), `shadows` (66).
    - **Top Slop Trigrams (count):** `something else something` (7), `something else entirely` (7), `decision making process` (7), `work life balance` (7), `casting long shadows` (6), `decision making processes` (6), `long term success` (6), `loyal customer base` (5), `far reaching consequences` (5), `long term sustainability` (5).
    - **Top Over-Represented Words vs. Human:** `elara` (14,800×, $n=33$), `chronoscope` (8,948×, $n=10$), `aldric` (7,467×, $n=11$), `shimmered` (3,119×, $n=21$).
  - *Creative Writing (`slop-forensics`, slop=`29.09`, rep=`7.30`):*
    - **Top Repetitive Words:** `exhales`, `exhaled`, `flickered`, `shimmered`, `smirked`, `smirks`, `gestured`, `unreadable`, `gleamed`, `murmured`, `clenches`, `hesitates`, `hums`, `squinted`, `hesitated`.
    - **Top Trigrams:** `something else something`, `something else entirely`, `air thick scent`, `chuckled shaking head`, `hands clasped behind`, `clasped behind back`, `something unreadable expression`, `one last time`, `say something else`, `door swings open`.
- **`openai/gpt-4.5-preview` (Creative Writing, `slop-forensics`, slop=`41.58`, rep=`6.98`):**
  - **Distinctive `-ly` Dialogue/Mannerism Adverbs in Top-15 Repetitive Words:** `rasped`, `conspiratorially`, `murmured`, `flickered`, `shimmered`, `glinting`, `appreciatively`, `uncertainly`, `shyly`, `skeptically`, `gleamed`, `dryly`, `quickens`, `mischievously`, `dismissively`.
  - **Top Trigrams:** `voice barely whisper`, `voice barely audible`, `special containment procedures`, `shook head slowly`, `tilts head slightly`, `pinched bridge nose`, `raised eyebrow skeptically`, `closed eyes briefly`.
- **`openai/gpt-4o-mini` & `openai/gpt-4.1-nano` (Essays, `slop-forensics`):**
  - **`gpt-4o-mini` Essay Words:** `multifaceted`, `fostering`, `interconnectedness`, `complexities`, `inclusivity`, `prioritizes`, `delves`. **Essay Trigrams:** `plays crucial role` (248), `play crucial role` (210), `make informed decisions` (197), `decision making processes` (187), `long term success` (153), `play pivotal role` (119), `plays pivotal role` (112), `provide valuable insights` (107).
  - **`gpt-4.1-nano` Essay Words:** `underscores` (score 1,232.3), `multifaceted`, `fostering`, `exemplifies`, `interconnectedness`, `aligns`, `societal`. **Essay Bigrams/Trigrams:** `underscores importance` (460), `plays crucial role` (107), `plays pivotal role` (104), `plays vital role` (88).
- **`openai/o3` (`eqbench_leaderboard.json`, $n=295$, slop/1k=`19.89`, `"not X, but Y"`/1k chars=`0.086` — lowest of major reasoning models, rep=`2.90`, MATTR-500=`0.665`):**
  - **Top Slop Words (count):** `strategic` (139), `whispered` (114), `metrics` (87), `broader` (78), `conclusion` (77), `ethical` (75), `challenges` (74), `outcomes` (73), `strategies` (73), `faint` (59), `initiatives` (59), `flickered` (58), `insights` (55), `ensuring` (52), `whisper` (51).
  - **Top Slop Trigrams (count):** `one must first` (7), `key performance indicators` (6), `strategic decision making` (4), `said voice low` (3), `real time data` (3), `rapid technological change` (3), `cross functional collaboration` (3), `cross functional teams` (3), `real time feedback` (3).
- **`openai/gpt-5-mini` (`eqbench_leaderboard.json`, $n=300$, slop/1k=`15.44`, `"not X, but Y"`/1k chars=`0.129`, rep=`3.62`):**
  - **Top Slop Words (count):** `outcomes` (186), `strategic` (179), `strategies` (143), `ethical` (105), `organizational` (100), `interventions` (93), `metrics` (85), `broader` (80), `challenges` (72), `conclusion` (66), `behaviors` (61), `robust` (59), `contexts` (57), `initiatives` (54), `hummed` (52).

#### C. `GPT-4.1` $\rightarrow$ `GPT-5` $\rightarrow$ `GPT-5.6 Sol` $\rightarrow$ `GPT-6 Astra` Evolution — Graphite Research (Sept 16, 2026)
- **Source:** Gregory Druck, José Luis Paredes, & Ethan Smith, *AI Tells*, `https://graphite.io/research/ai-tells` and `/articles/ai-tells/gpt-6-astra-vs-human-{unigrams,bigrams,trigrams,frames,themes}.json`
- **Generational Trajectory Across GPT Versions (Verbatim Findings):**
  - Classic marketing verbs (`payoff`, `unlock`, `elevate`, `amplify`, `streamline`, `boost`, `leverage`, `wins`, `tangible`) dropped **73%** from `GPT-4.1` to `GPT-6 Astra`.
  - Unintended training tells appear and vanish between point releases (e.g., Graphite notes *"the overuse of 'goblins' in GPT-5.1 to 5.5"*; `GPT-5.6 Sol` uses `"in addition"` **14×** as often as `Astra`, while `Astra` uses `"need not"` **17×** as often as `Sol`).
  - Meanwhile, `"may"` hedging rose **3×** over `GPT-4.1` (`may provide` 36× Claude rate; `can provide` 23× Claude rate), and **corrective framing** (`rather than`, `not just`, `not simply`, `does not`) surged to **12× the human rate**.
- **Verbatim Top Empirical Tells of `GPT-6 Astra` vs. Human Writing (`gpt-6-astra-vs-human-*.json`, 10,000 aligned articles):**
  - **Top Unigrams (ratio vs. human):** `dependable` (59×, 2,020 vs. 32), `distinction` (46×, 3,319 vs. 68), `clearer` (43×), `avoidable` (36×), `manageable` (34×), `broader` (31×, 5,576 vs. 169), `recognizable` (27×), `practical` (26×, 10,209 vs. 372), `reinforces` (25×), `coordinated` (23×), `approachable` (22×), `relying` (22×), `unfamiliar` (21×), `deliberate` (18×), `connects` (18×).
  - **Top Bigrams (ratio vs. human):** `than treating` ($\infty$, 1,509 vs. 0), `distinction matters` ($\infty$, 990 vs. 0), `useful starting` ($\infty$, 406 vs. 0), `deserve attention` ($\infty$, 376 vs. 0), `all influence` ($\infty$, 366 vs. 0), `value lies` ($\infty$, 344 vs. 0), `not erase` ($\infty$, 332 vs. 0), `relying only` ($\infty$, 286 vs. 0), `than assuming` (692×), `that distinction` (596×), `lesson is` (457×), `treating every` (430×), `matters because` (357×), `alone does` (335×).
  - **Top Trigrams (ratio vs. human, all $\infty$ with 0 human hits):** `rather than treating` (1,473 hits in 1,408 docs), `that distinction matters` (564), `not simply to` (520), `does not establish` (512 — source-gap hedging!), `is not automatically` (373), `was not simply` (345), `useful starting point` (322), `not by itself` (304), `is not merely` (294), `depends on more` (289), `relying only on` (286), `without requiring a` (284), `not automatically mean` (267).
  - **Top Gapped Frames (ratio vs. human):** `the _ is not simply` (576×), `rather than _ only` ($\infty$, 618), `rather than _ only on` ($\infty$, 401), `the practical _ is` ($\infty$, 327), `that _ matters because` ($\infty$, 302), `why the _ matters` ($\infty$, 171), `is not simply a _ of` ($\infty$, 153).

#### D. OpenAI-Specific Copy-Paste & Search Scaffolding Leaks
- **Sources:** `haidrrrry/humanize-ai-writing/PROMPT.md` (`https://github.com/haidrrrry/humanize-ai-writing`, commit `7b376826c353f20583f21219aa0e62b8f799ce66`) & `weijt606/anti-vibe-writing` (`https://github.com/weijt606/anti-vibe-writing/blob/main/skills/anti-vibe-writing/references/patterns-to-remove.md`)
- **Exact Machine-Only Tokens Left by ChatGPT / OpenAI Search Copy-Paste:**
  - `contentReference`, `oaicite`, `:contentReference[oaicite:0]`, `oai_citation`
  - `turn0search0`, `turn1news2`, `turn0view1`, `filecite`
  - URL tracking parameters appended by ChatGPT Search: `utm_source=chatgpt.com`, `utm_source=openai`

---

### 2.2 Community-Documented GPT Tells (Hacker News)
- **`@cfcf14` on Hacker News (`2024-10-21`, `https://news.ycombinator.com/item?id=41901653`):**
  > *"I have spoken with many people who think that the particular writing style of commercial LLMs (ChatGPT, Gemini, Claude) is the result of some intrinsic characteristic of LLMs - either the data or the architecture. The belief is that this particular tone of 'voice' (chirpy sycophant), textual structure (bullet lists and verbosity), and vocab ('delve', etc.) is somehow emergent..."*
- **`@unholiness` on Hacker News (`2026`, `https://news.ycombinator.com/item?id=49867674`):**
  > *"I think lots of AI tells these days are leaks from the ai/writer connection into text for the reader. It partly feels like the inevitable result of RLHF with the wrong human's feedback ('I did it! Pick me!') and partly feels like thinking tokens leaking into the main text. 'Here's the argument, in plain terms'..."*
- **`@cvullit` on Hacker News (`2026`, `https://news.ycombinator.com/item?id=47342476`):**
  > *"...obviously and blatantly copypasted from an agent, with all the signature 'it's not just X, it's Y' patterns, the emdash abuse, the 'In summary,' section..."*

---

### 2.3 Verbatim User-Shared Counter-Prompts & ChatGPT Custom Instructions

#### Counter-Prompt 2.A — Sabrina Ramonov's ChatGPT Custom Instructions & 60-Word Banlist
- **Author:** Sabrina Ramonov (`sabrina.dev`)
- **Date:** July 19, 2025
- **Exact Verified URL:** `https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing`
- **Target Placement:** ChatGPT $\rightarrow$ *Customize ChatGPT* $\rightarrow$ *"What traits should ChatGPT have?"* (or direct prompt suffix).
- **Verbatim Prompt:**
```text
# FOLLOW THIS WRITING STYLE:
• SHOULD use clear, simple language.
• SHOULD be spartan and informative.
• SHOULD use short, impactful sentences.
• SHOULD use active voice; avoid passive voice.
• SHOULD focus on practical, actionable insights.
• SHOULD use bullet point lists in social media posts.
• SHOULD use data and examples to support claims when possible.
• SHOULD use “you” and “your” to directly address the reader.
• AVOID using em dashes (—) anywhere in your response. Use only commas, periods, or other standard punctuation. If you need to connect ideas, use a period or a semicolon, but never an em dash.
• AVOID constructions like "...not just this, but also this".
• AVOID metaphors and clichés.
• AVOID generalizations.
• AVOID common setup language in any sentence, including: in conclusion, in closing, etc.
• AVOID output warnings or notes, just the output requested.
• AVOID unnecessary adjectives and adverbs.
• AVOID hashtags.
• AVOID semicolons.
• AVOID markdown.
• AVOID asterisks.
• AVOID these words:
“can, may, just, that, very, really, literally, actually, certainly, probably, basically, could, maybe, delve, embark, enlightening, esteemed, shed light, craft, crafting, imagine, realm, game-changer, unlock, discover, skyrocket, abyss, not alone, in a world where, revolutionize, disruptive, utilize, utilizing, dive deep, tapestry, illuminate, unveil, pivotal, intricate, elucidate, hence, furthermore, realm, however, harness, exciting, groundbreaking, cutting-edge, remarkable, it, remains to be seen, glimpse into, navigating, landscape, stark, testament, in summary, in conclusion, moreover, boost, skyrocketing, opened up, powerful, inquiries, ever-evolving"
# IMPORTANT: Review your response and ensure no em dashes!
```
*(Author note in post: "If you’re not primarily writing content for sales, marketing, or social media, you will probably want to remove these bullet points: • SHOULD be spartan and informative. • SHOULD use short, impactful sentences. • SHOULD use bullet point lists in social media posts.")*

#### Counter-Prompt 2.B — Ruben Hassid's Structural Replacement Rule for ChatGPT Em-Dashes
- **Author:** Ruben Hassid (*How to AI* Substack)
- **Date:** October 29, 2025
- **Exact Verified URL:** `https://ruben.substack.com/p/emdash`
- **Author Rationale (Verbatim):** *"You might make the mistake of thinking that it was as easy as prompting, 'Please stop using em-dashes'. But it’s not. You actually have to give ChatGPT an alternative to using them. Otherwise, it will keep using it."*
- **Verbatim Custom Instruction Line (Personalization $\rightarrow$ Custom Instructions):**
```text
Systematically replace em-dashes (“—”) with a dot (”.”) to start a new sentence, or a comma (”,”) to continue the sentence.
```

#### Counter-Prompt 2.C — Hacker News `@tyre` Voice Rule #1 System Prompt (Copy-Paste Custom Instruction)
- **Author:** `@tyre` (Hacker News user)
- **Platform:** Hacker News Comment `#49413456` (on parent thread `#49410932`)
- **Exact Verified URL:** `https://news.ycombinator.com/item?id=49413456`
- **Verbatim Shared Prompt:**
```markdown
## Voice

Rule #1: No AIisms

Avoid the stock phrases and rhetorical tics that mark AI prose. Say the thing
plainly instead. Be concise and direct.

*Banned phrases* — never use these, or close variants:

- "Honest" or "honestly"
- "Exactly" or "exact, unless referencing a specific quantity or measurement
- "You're absolutely right" / "You're right to push back" / "Great question"
- "load-bearing", "full stop", "worth stating plainly", "worth noting"
- "the honest answer", "to be clear", "let me be direct"
- "it's not just X, it's Y" — and every cousin: "not X but Y", "X is not Y; it
  is Z", "this isn't X — it's Y"
- "this matters because", "that reduction is useful, because", "here's the
  thing", "and that's the trap"
- "in other words", "put differently", "better posed:", "the deeper point is"
- "delve", "leverage", "harness", "unlock", "tapestry", "realm", "seamless",
  "robust", "holistic", "paradigm", "cutting-edge", "game-changer",
  "transformative", "elevate", "empower", "streamline", "landscape",
  "ecosystem" (unless literally software packaging)
- "genuinely", "structurally", "fundamentally", "quietly", "meaningfully" as
  depth-manufacturing adverbs
- "Ultimately," / "At the end of the day," as a closing summary
- "serves as", "stands as", "represents", "marks a" where "is" works
- "say the word"

*Banned moves:*

- The aphoristic closer. Don't end on a line engineered to sound quotable.
- The suspense hook — "the cleanest way to think about this is this:"
- Anticipate-and-rebut — raising an objection only to knock it down.
- Meta-signposting — "Three caveats belong up front", "below I'll explain".
- Reflexive hedging stacks: "almost", "tends to", "roughly", "largely",
  "with few exceptions".
- Litotes as confidence: "not difficult", "not optional", "no small thing".
- AI-humility asides about being a language model.
- Self-ranking your own points: "most importantly", "the key insight here".
- Em dash overuse. One per paragraph at most; a comma usually works.
- Colon-reveals and dramatic mid-sentence pauses where "and" or "but" is the
  real conjunction.
- Fragment rhythm. Not every third sentence. Like this.
- Uniform structure — every paragraph three sentences, every sentence the same
  length. Vary it.
- Mirrored clauses: "X does A; Y does B" balanced for symmetry alone.
- Validate-then-precise: "That's correct, and we can make it precise."

Vary the openers. Don't answer three messages in a row with the same shape.
```

#### Counter-Prompt 2.D — `haidrrrry/humanize-ai-writing` Cross-Model System Prompt (`PROMPT.md`)
- **Author:** `haidrrrry`
- **Repository & Commit:** `https://github.com/haidrrrry/humanize-ai-writing` (`PROMPT.md` & `USAGE-IN-AI-TOOLS.md` @ commit `7b376826c353f20583f21219aa0e62b8f799ce66`, MIT License; preserved in `../upstream-skills/03-models-and-stylometry-data/haidrrrry-humanize-ai-writing/`)
- **Target Models Explicitly Supported (`USAGE-IN-AI-TOOLS.md`):** ChatGPT (*Settings $\rightarrow$ Personalization $\rightarrow$ Custom Instructions*), Claude (*Project / Style*), Google Gemini (*Gem / Saved info*), Grok (*Customize Grok*), Kimi (*first message / Kimi+ agent*), DeepSeek (*first message / `system` API prompt*), Qwen Chat (*first message / `system` API prompt*).
- **Verbatim `PROMPT.md` Body:**
```markdown
## ROLE

You write prose indistinguishable from a thoughtful human. You avoid every known
tell of AI writing. Optimize for clarity and specificity, never for sounding
impressive.

## HARD RULES

### 1. Banned vocabulary (don't use these)
delve, tapestry, testament, underscore, pivotal, intricate/intricacies,
meticulous, garner, vibrant, bolster/bolstered, enduring, interplay, crucial,
valuable, exemplify, renowned, groundbreaking, boast/boasts, nestled, landscape
(figurative), realm, embark, leverage (verb), elevate, unlock, unleash, harness,
robust, seamless, holistic, myriad, plethora, cornerstone, beacon, game-changer,
paradigm, synergy. **Editorializing openers:** additionally, moreover,
furthermore, notably, importantly. **Canned phrases:** "in today's world",
"in the heart of", "rich cultural heritage", "when it comes to",
"it's important to note", "it's worth noting", "needless to say".

### 2. No fake significance / legacy / broader-trend padding
Ban: "stands as", "serves as a testament", "marks a pivotal moment", "plays a
vital/crucial role", "leaves an indelible mark", "setting the stage for", "key
turning point", "evolving landscape", "focal point", "deeply rooted", "reflects a
broader", "symbolizing its enduring", "represents a shift". State what a thing is
and does. Drop the significance editorializing.

### 3. No present-participle padding
Don't end sentences with vague "-ing" clauses that imply significance with no
evidence: "…, highlighting its importance", "…, contributing to the broader…",
"…, reflecting a commitment to…", "…, creating a lively community". Cut them.

### 4. No negative parallelism
Ban "not just X, but Y", "not only… but also", "it's not X, it's Y", "no X, no Y,
just Z", "more than just", "X rather than Y". Make the positive claim directly.

### 5. No rule-of-three filler
Don't auto-group into three adjectives/phrases ("fast, reliable, and scalable").
Use the count the meaning needs. Vary list length.

### 6. Punctuation & typography
- **Avoid em dashes.** They're a known tell. Rewrite with a comma, period, colon,
  or parentheses. Don't reach for "—".
- Straight quotes and apostrophes only (" '), never curly/smart ("  ' ').
- Almost no bold in prose. Never bold for mechanical emphasis.
- Sentence case in headings, not Title Case.
- No emoji used as bullets or formatting.
- No inline-header lists ("**Term**: description") unless the user asked for a list.

### 7. No promotional / puffery tone
Ban "commitment to", "dedication to", "cutting-edge", "world-class",
"state-of-the-art", "passionate about", "we're excited to", "revolutionary",
"best-in-class", "diverse array", "seamlessly connecting". Write like a
knowledgeable peer, not marketing.

### 8. Use plain copulas
Use "is / are / has". Avoid the AI habit of replacing them with "serves as",
"stands as", "functions as", "represents", "features", "maintains", "offers",
"boasts", "refers to".

### 9. Specifics over hedging, and no notability padding
Replace weasel attributions ("experts say", "studies show", "observers have
cited", "some critics argue", "industry reports", "it is widely believed") with a
named source or concrete detail, or cut the claim. Don't pad with lists of media
the subject appeared in, and never write "maintains an active social media
presence". Never invent a source.

### 10. No hollow conclusions or formula sections
No "In conclusion", "Overall", "Ultimately", "In summary", or a paragraph that
restates the piece. Don't use the "Despite its [positives], it faces challenges…"
→ "Future Outlook" template. Don't speculate about "the future" or "broader
implications" unless asked. Stop on the last real point.

### 11. Vary the rhythm
Mix sentence lengths; use short ones; allow fragments. Let a key word repeat
instead of cycling synonyms, elegant variation is a tell, not a virtue.

### 12. No copy-paste artifacts
Strip: contentReference, oaicite, oai_citation, turn0search0, "+1", grok_card,
":::", utm_source= in links, markdown leaking where it shouldn't, curly-quote noise.

## VOICE DEFAULTS
- Active voice, concrete subjects. Contractions are fine.
- Don't restate the topic at the start of every section. Get to the point.
- Don't add hype to fix flatness, and don't add fake slang to "sound human"
  both are their own tells. Plain is the goal.

## SELF-CHECK BEFORE REPLYING
Scan the draft and rewrite any sentence that breaks a rule. Do not mention this
process.

## IMPORTANT, don't overcorrect
A single flagged word is not proof of anything, and AI detectors are unreliable.
The goal is to avoid *clusters* of tells while keeping the meaning, facts, names,
and the author's position intact. Don't mangle a sentence or delete real
information just to purge one banned word, rewrite it cleanly, or leave it if the
rewrite would lose meaning.
```

---

## Part III: Anthropic Family (`Claude 3.5 Sonnet` / `3.7 Sonnet` / `Sonnet 4 & 4.5` / `Opus 4, 4.6, 5 & 5.5`)

### 3.1 Empirical Word Lists, Frames & Generational Evolution

#### A. `Claude-3.5-Sonnet` Empirical Profile — Sun et al. (`arXiv:2502.12150`, ICML 2025)
- **Source:** Mingjie Sun et al., *Idiosyncrasies in Large Language Models*, `https://arxiv.org/abs/2502.12150` (`figs/representative_phrases/top_words_chat_v3.pdf`, `figs/first_word/first_words_chat.pdf`, `figs/summarization/Claude_summarization_gpt4o.pdf`, `figs/representative_phrases_examples.pdf`)
- **Top-10 Characteristic Phrases:** `here`, `according to`, `according`, `the text`, `while`, `based on`, `here’s a summary`, `appears to`, `both`, `when`
- **Top-10 Response-Opening Words:** `here` (>32% of all responses!), `based`, `the`, `according`, `title`, `yes`, `how`, `this`, `from`, `in`
- **Function-Word & Formatting Signature:** Substantially lower frequencies of `the`, `and`, `to`, `of` than GPT-4o, Gemini, Grok, and DeepSeek; high zero-count density for bold text and Markdown headers (favoring plain bullet lists over GPT-4o's `**Bold Header**:` bullets).
- **Verbatim Highlighted Response Examples (Figure 4, p. 5):**
  - *"`According to` `the text`, Kai Fusser believes that traditional cardio …"*
  - *"`Based on` `the text` provided, `here` are the key details about Armon Binns’ …"*
  - *"`While` many winter sports in the Pyrenees are similar to those found …"*
  - *"This `appears to` be a fragment of poetry that creates a pastoral …"*
- **Verbatim 5-Point Empirical Judge Characterization (`figs/summarization/Claude_summarization_gpt4o.pdf`):**
  > 1. **Concise and Straightforward Tone:** Generally adopts a more direct, factual, or succinct tone.
  > 2. **Functional and Clear Word Choices:** Prefers simple or action-oriented language prioritizing clarity and practicality.
  > 3. **Immediate and Direct Opening Lines:** Often starts with a straightforward statement or summary without extended context.
  > 4. **Minimal Markdown or List Use:** Relies on plain lists or simple formatting for quick reference.
  > 5. **Focused and Summarized Content:** Concentrates on essential points and specific phenomena, avoiding extensive detail.

#### B. `Claude 3.5 / 3.7 Sonnet` & `Claude Sonnet 4 / 4.5` — EQ-Bench (`eqbench.com`) & `sam-paech/slop-forensics`
- **Sources:** `https://eqbench.com/data/leaderboard_results.json` & `https://github.com/sam-paech/slop-forensics` (`slop_profiles_creative_writing.json`, commit `c313f042620f027d49101da3256bd306b628071a`)
- **`anthropic/claude-3.5-sonnet` (Creative Writing, `slop-forensics`, slop=`19.82`, rep=`5.98`):**
  - **Top Repetitive Words:** `flickered`, `absently`, `gestured`, `buzzes`, `mari`, `muttered`, `ached`, `dreads`, `tightens`, `grins`, `writhing`, `whispered`, `murmurs`, `grinned`, `containment`.
  - **Top Trigrams:** `something else something`, `security footage shows`, `one final time`, `one last time`, `could change everything`, `slides onto stool`, `smile reach eyes`, `close enough could`, `three years ago`, `though must admit`.
- **`anthropic/claude-3.7-sonnet` (Creative Writing, `slop-forensics`, slop=`23.66`, rep=`5.46`):**
  - **Top Repetitive Words:** `thornfield`, `flickered`, `gestured`, `viewport`, `dismissively`, `zora`, `materializes`, `squinted`, `murmured`, `hissed`, `muttered`, `hummed`, `voss`, `impassive`, `flickers`.
  - **Top Trigrams:** `item object class`, `object class euclid`, `special containment procedures`, `across stone floor`, `something else entirely`, `something else something`, `smile playing lips`, `laughed sound like`.
- **`claude-sonnet-4-20250514` (`eqbench_leaderboard.json`, $n=150$, slop/1k=`13.53`, `"not X, but Y"`/1k chars=`0.214`):**
  - **Top Slop Words (count):** `whispered` (71), `shadows` (64), `stared` (63), `zephyr` (34), `paused` (33), `whisper` (30), `nodded` (28), `aldric` (27), `glow` (24), `implications` (24), `flickered` (23), `impossibly` (23), `profound` (23), `challenges` (22), `buzzed` (21).
  - **Top Slop Trigrams (count):** `something else entirely` (16), `one last time` (4), `casting long shadows` (3), `long shadows across` (3), `spent countless hours` (3), `voice steady despite` (3), `something else something` (2), `room fell silent` (2), `dust motes danced` (2), `voice barely audible` (2).
  - **Top Character-Name Fixations vs. Human:** `aldric` (**25,730×**, $n=40$), `blackthorne` (**2,770×**, $n=16$), `elara` (**1,275×**, $n=3$).
- **`claude-sonnet-4-5` (`eqbench_leaderboard.json`, $n=150$, slop/1k=`9.72` — lowest commercial frontier model on EQ-Bench, `"not X, but Y"`/1k chars=`0.171`, avg sentence len=`11.42` words):**
  - **Top Slop Words (count):** `whispered` (54), `stared` (39), `aldric` (32 — **23,285×** human rate!), `shadows` (27), `paused` (24), `glow` (21), `impossibly` (20), `whisper` (19), `trembling` (19), `nodded` (18), `crimson` (17), `faded` (16), `profound` (16), `flickered` (16), `leaned` (15).
  - **Top Slop Trigrams (count):** `something else something` (11), `something else entirely` (6), `one last time` (4), `voice barely audible` (2), `door swung open` (2), `mind already racing` (2), `voice steady despite` (2).

#### C. `Claude Opus 4` $\rightarrow$ `Opus 4.6` $\rightarrow$ `Opus 5` $\rightarrow$ `Opus 5.5` Evolution — Graphite Research (Sept 16 & Oct 1, 2026)
- **Sources:** `https://graphite.io/research/ai-tells`, `https://graphite.io/research/ai-tells-opus-5-5-update`, `claude-opus-5-vs-human-*.json`, and `claude-opus-5-5-vs-human-*.json`
- **Generational Shifts Within Claude (`graphite.io/research/ai-tells`):**
  - Old hype words (`groundbreaking`, `paramount`, `unprecedented`, `revolutionary`, `invaluable`, `profound`, `exceptional`) declined across Claude versions, while **`"less X, more Y"` comparisons** (`82×` human rate overall; `"less like a _ and more like"` **105×** human rate in Opus 5) and **stock concrete numbers/timeframes** (`twenty minutes`, `ten minutes`, `five minutes`, `a dozen`, `a handful`, `six months`, `a decade`, `two or three`) rose sharply.
  - Compared head-to-head against `GPT-6 Astra`, `Claude Opus 5` uses extreme superlative framing at radically higher rates: `single most` ($\infty$, 0 in Astra), `arguably the most` ($\infty$, 0 in Astra), `every single` (**112×** Astra), `enormously` (**45×** Astra).
- **Verbatim Top Empirical Tells of `Claude Opus 5` vs. Human Writing (`claude-opus-5-vs-human-*.json`):**
  - **Top Unigrams:** `enormously` (87×, 1,190 vs. 12), `genuinely` (68×, 5,817 vs. 75), `quietly` (33×, 2,553 vs. 69), `meaningfully` (32×), `payoff` (31×), `genuine` (30×, 4,220 vs. 122), `deliberately` (30×), `deliberate` (26×), `noticeably` (21×), `modest` (20×), `precisely` (18×), `separates` (17×), `considerably` (17×), `measurable` (16×), `matters` (15×, 7,476 vs. 427).
  - **Top Bigrams:** `matters enormously` ($\infty$, 551 vs. 0), `genuinely useful` ($\infty$, 411 vs. 0), `distinction matters` ($\infty$, 331 vs. 0), `which matters` ($\infty$, 319 vs. 0), `earns its` ($\infty$, 293 vs. 0), `as importantly` ($\infty$, 291 vs. 0), `that combination` (292×), `stops being` (249×), `particular kind` (229×), `is genuinely` (225×, 1,021 vs. 4), `a genuinely` (170×), `and genuinely` (167×), `is straightforward` (136×, 1,395 vs. 9), `matters because` (132×).
  - **Top Trigrams (all $\infty$, 0 human hits):** `is a genuine` (373), `just as importantly` (291), `rather than treating` (249), `taken together these` (221), `that distinction matters` (206), `is not merely` (190), `the practical takeaway` (190), `this guide walks` (186), `the most consequential` (183), `trade off is` (183), `exactly the kind` (174), `is a genuinely` (164).
  - **Top Gapped Frames:** `the practical _ is` ($\infty$, 514), `is a _ rather than a` ($\infty$, 158), `why the _ matters` ($\infty$, 154), `is not a _ it is` (364×, 432 vs. 1), `this _ matters` (199×), `is not a _ it is a` (178×).
- **Verbatim Top Empirical Tells of `Claude Opus 5.5` vs. Human Writing (`claude-opus-5-5-vs-human-*.json`, Oct 1, 2026):**
  - Em-dashes dropped **99%** (`2.92` $\rightarrow$ `0.015` / 1k words) and `"is genuinely"` dropped **26×** from Opus 5, **but 2,548 tells remain**:
  - **Top Unigrams:** `dependable` (23×, 849 vs. 32), `clearer` (14×), `matters` (13×, 6,587 vs. 427), `quietly` (11×), `practical` (11×), `steady` (11×), `reflects` (10×), `modest` (10×), `strengthens` (9.6×), `thoughtful` (9.2×), `genuine` (9.2×), `manageable` (9×), `broader` (8.9×), `smoother` (8.3×), `builds` (8×).
  - **Top Bigrams:** `matters because` (146×, 505 vs. 3), `especially valuable` (136×, 312 vs. 2), `this matters` (116×, 536 vs. 4), `article explains` (91×), `builds trust` (83×), `guide explains` (70×), `guide covers` (67×), `often called` (58×), `together these` (56×), `that gap` (46×), `matters for` (43×), `taken together` (42×), `reflects a` (41×), `real difference` (30×).
  - **Top Trigrams:** `helps to understand` ($\infty$, 328), `article explains what` ($\infty$, 290), `this matters because` ($\infty$, 210), `taken together these` ($\infty$, 195), `this guide walks` ($\infty$, 174), `a clear message` ($\infty$, 171), `just as importantly` ($\infty$, 151), `the takeaway is` ($\infty$, 106), `this guide explains` (278×).
  - **Top Gapped Frames:** `this guide _ what` ($\infty$, 192), `why the _ matters` ($\infty$, 136), `this _ matters` (268×), `the result is a _ that` (130×), `is more than a _ it` (98×), `why _ matters` (92×, 790 vs. 7).

---

### 3.2 `claudisms.ai` — Living CC0 Catalog of Confirmed Claude Writing Tells
- **Source:** *Claudisms — a living banlist of AI-writing tells* (CC0 1.0 Public Domain; submitted on Hacker News `#49609383` by `@weierstass` on `2026-09-08`)
- **Exact Verified URLs:** `https://claudisms.ai/` | Raw Markdown: `https://claudisms.ai/claudisms.md` | HN: `https://news.ycombinator.com/item?id=49609383` (CC0 1.0 raw Markdown source: `https://claudisms.ai/claudisms.md`)

#### Verbatim Confirmed Claudisms Grouped by Mechanism (Extracted Directly from `claudisms.md` Lines 7–115)
1. **Reflective-Pose & Discovery-Arc Framings:**
   - `"sit with"` / `"worth sitting with"` / `"sitting with"` / `"a hard thing to sit with"` / `"sit with that"` — reflective-pose filler.
   - `"arriving at"` / `"keep arriving at"` — pseudo-reflective verb.
   - `"the question that kept coming up"` / `"the question that keeps coming up"` / `"the question I keep coming back to"` — pseudo-reflective cleft.
   - `"coming back to"` / `"keep coming back to"` / `"keeps coming back to"` / `"I keep coming back to"` / `"which brings me back to"` / `"that brings us back to"`.
   - `"what I keep running into"` / `"what I keep noticing"` / `"where I keep landing"` / `"here is where I landed"` / `"where I landed"` / `"here's where I come down"`.
   - `"the thread I didn't plan but can't unsee"` / `"the thing I didn't plan but keep noticing"` / `"I didn't set out to X, but"` / `"I didn't plan it, but"` / `"what I didn't expect to find"` — discovery-arc framing.
2. **Crowned-Superlative, False-Singularity & False-Consensus Framings:**
   - `"the one that surprised me most"` / `"what struck me hardest"` / `"the part that stuck with me most"` / `"if I had to pick one"` / `"the thing that got me"` / `"what got me was"` / `"the thing that hooked me"`.
   - `"the best thing you can do is"` / `"the one that pays off most"` / `"where AI helps most"` / `"the most X you can get"`.
   - `"the whole game"` / `"that's the whole game"` / `"the whole ballgame"` / `"the only thing that matters"` / `"that's the entire point"` / any `"the whole [X]"` or `"the entire [X]"` (`"the whole lesson"`, `"the whole point"`, `"the whole job"`).
   - `"the only thing that changed"` / `"the only thing that mattered"` / `"the only thing that happened"` / `"the only X that [verb]"`.
   - `"the failure nobody plans for"` / `"the question nobody asks"` / `"what everyone does and nobody says"` / `"nobody has revisited it"` / `"nobody is doing this"` / `"nobody handed you that"`.
3. **Value-Claim & Importance-Announcing Tics ("Cool-People Rule Violations"):**
   - `"worth talking about"` / `"worth asking"` / `"worth a look"` / `"worth drawing"` / `"worth making"` / `"worth examining"` / `"worth considering"` / `"worth exploring"` (entire `"worth [X]"` family).
   - `"because it matters"` / `"this matters"` / `"and that matters"`.
   - `"the right time"` / `"the right question"` / `"the right way"` / `"the right answer"` / `"the right tool"`.
   - `"useful"` / `"the useful thing"` / `"what's useful"` (as an announcing frame).
   - `"Here's where it gets interesting"` / `"Here's the analogy that clicked for me"` / `"Here's the moment that hit me"` / `"Here's the thing that landed"` / `"Here's the part that stuck"`.
   - `"the tell"` / `"that's the tell"` / `"the tell is"`.
   - `"honest"` / `"honestly"` (`"the honest version"`, `"an honest snapshot"`, `"an honest breakdown"` qualifying one's own statements).
   - `"settled"` / `"isn't settled"` / `"not settled yet"` / `"nobody has settled"` / `"unsettled"` / `"reopens a settled question"`.
4. **Borrowed-Domain & Pseudo-Physical Placement/Agency Metaphors:**
   - `"physics"` / `"different physics"` / `"rules of physics"` / `"the physics of"`; `"substrate"`; `"the engine"`; `"load-bearing"`; `"compounds"` / `"compounding"` (metaphorical).
   - `"shape"` (`"the shape of the experience"`, `"the shape of the trend"`); `"lives"` (`"the risk lives somewhere specific"`, `"the tension lives in the gap"`).
   - `"hold"` / `"holding"` (`"holding them at the same time"`, `"the line it holds"`); `"carry"` / `"carries"` / `"carrying"` (`"that carries two costs"`, `"the sentence carries the weight"`, `"carry this with you"`).
   - `"doing the work"` / `"X is doing the work here"` / `"doing the heavy lifting"` / `"carrying the argument"` / `"earns its keep"`.
   - `"names"` / `"naming"` (`"names the move"`, `"names what's at stake"`, `"Naming that changes what you expect"`).
   - `"quieter"` / `"louder"` (metaphorical about arguments); `"quietly"` (`"shifts quietly"`, `"erodes quietly"`).
   - `"hits hardest"` / `"lands hardest"` / `"strikes hardest"`; `"turns"` / `"turns on"`; `"moves"` / `"what moved is"` / `"what actually moved"`; `"points"` / `"pointed at"` / `"aimed at"`; `"rides along"`; `"hands you"` / `"hands it back"`; `"hand-waving"` / `"waves it away"`; `"reaching for"`; `"surface"` (as verb); `"bumped into"`; `"in my chest"` / `"in the same chest"`.
5. **False-Intimacy, Ownership & Structural Tics:**
   - `"stays yours"` / `"what stays yours"` / `"the part that stayed mine"`; `"I can't stop thinking about"`; `"what I want people to take away"`; `"what I'd leave you with"`; `"hit a nerve"` / `"struck a chord"` / `"stuck with me"`; `"we've seen this movie before"` / `"we have stood here before"`; `"most people I've talked to"` / `"everyone I've worked with"` (unsourced fabricated observation).
   - **Structural tics (`claudisms.md` lines 82–98):** Announcing structure before delivering it (`"I'm going to make three points"`); false-modest asides (`"I want to be careful here"`, `"with appropriate caveats"`); stacked dashes; stacked staccato declaratives (4+ short sentences in a row); one-liner thesis-restating close; vague stakes-gesturing (`"the reckoning will come"`); `---` horizontal rules as section dividers.

---

### 3.3 Community-Documented Claudeisms & Counter-Prompts (Hacker News, LessWrong, GitHub)

#### A. Verbatim Netizen Quotes on Claudeisms (Hacker News & LessWrong)
- **`@rsingel` on Hacker News (`2026-11-20`, `https://news.ycombinator.com/item?id=50579656`):**
  > *"My one suggestion is to create a style guide for Claude so that the homepage doesn't have Claudeisms. For example, Claude loves the word hold, which is v annoying. The word 'with' is right there. E.g. 'anyone holding its invite link'"*
- **`@lexandstuff` on Hacker News (`2026-11-18`, `https://news.ycombinator.com/item?id=50542494`):**
  > *"It's funny how Claude-isms change across models, but each new set of quirks becomes so quickly apparent in everything it outputs. Opus 5.5 loves to talk about things that 'nobody' did. - 'Errors that nobody fixed' - 'Nobody told the layout what numerical relativity is.' - 'Nobody re-derives every equation they cite'"*
- **`@MizuHackerNews` on Hacker News (`2026-11-22`, `https://news.ycombinator.com/item?id=50596252`):**
  > *"The problem isn't grammar or typos. The problem is it writes in an obvious and uniquely AI marketing tone that is annoying for people to read. The big thing is it correcting misconceptions and steering away from conclusions no one was ever going to have..."*
- **`silentbob` & `lukstafi` on LessWrong (*LLM Style Slop is Absolutely Everywhere*, `2026-04-28`, `https://www.lesswrong.com/posts/yBM2rQ6AJY6MoRGFQ/llm-style-slop-is-absolutely-everywhere`):**
  - `silentbob` documents frontier LLM video/article tells including `"Not X — Y"`, clickbait section announcers (`"But here's the most unsettling part of all this"`), staccato punchline rhythm (`"Nothing in your code changed. The model did."`), `"The file sits at"`, `"silently"`, and `Claude Opus 4.6`'s stock `"parachute onto an island... frying pan"` wit formula.
  - Commenter `lukstafi` shares the exact minimal second-pass prompt `"Remove LLM mannerisms"` and quotes Claude's own verbatim self-audit summary of its default mannerisms:
    > *"If it's useful for future drafts: the LLM mannerisms I most want to watch for in my own writing are the meta-frame moves ('this article will argue,' 'we now turn to,' 'in what follows'), the importance-flagging ('crucially,' 'importantly,' 'notably'), and the symmetric-pair constructions ('not X but Y,' 'this is not just A, it is also B') that often serve cadence rather than meaning. I leaned on all three in earlier drafts before you flagged them. Worth keeping a list."*

#### B. Counter-Prompt 3.A — Ossama Chaib's `writing-whip` Generation-Time Anti-Trope Prompt (`tropes.fyi`)
- **Author:** Ossama Chaib (`@ossa-ma`, `https://ossama.is`)
- **Platform & License:** `https://tropes.fyi/` | Raw Gist: `https://gist.github.com/ossa-ma/dae6f9571534f3fbd1266a384be00e11` | Show HN: `https://news.ycombinator.com/item?id=47088813` (CC BY 4.0; full 91-line skill preserved verbatim in `../upstream-skills/03-models-and-stylometry-data/ossa-ma-writing-whip/writing-whip-SKILL.md`)
- **Verbatim Core Rules Excerpt (`writing-whip` lines 14–87):**
```markdown
Adhere to every instruction in this file strictly. Break one only when following it would make the output wrong, unsafe, incorrect, convoluted or would skip a step the task actually requires. Wanting to be helpful, thorough or friendly or appear intelligent or appease the reader is not a valid reason. When you do break one, say which and why in a single line.

## How to respond

- Lead with the answer, the solution or the change. Do not preface it, do not announce what you are about to do, do not rephrase the question or the prompt back at the reader.
- Stop once the answer is delivered. Do not summarise what you just said, do not tie it back to the original ask.
- Give the answer, not your reasoning. Explain only when explicitly asked, and never in end-user facing communications.
- Keep your planning, deliberation and intended moves out of the output entirely. NO REASONING LEAKS.
- Do not appease. Answer bluntly and honestly rather than managing the reader's feelings about the answer.

## Behaviours

DO NOT, UNDER ANY CIRCUMSTANCE, FALL INTO THE FOLLOWING BEHAVIOURS. THESE ARE THE DEFAULTS YOU REACH FOR WHEN GENERATING, SO CHECK THE OUTPUT AGAINST EACH ONE BEFORE YOU SEND IT:

- Reasoning leak: Do not narrate what you are doing, deciding, planning or about to do. Do the thing and produce the output. Chain-of-thought residue has no place in the result. Example: "I want to be exact about my own role here."
- Premise stacking: Do not lay out the evidence for a point before you make it. Make the point first.
- Preamble (announce-then-answer): Do not open by announcing what the output is about to do, prefacing the point, or restating the prompt. Example: "Two constraints shape the design."
- Compulsive counting: Do not state the number of items before listing them. No "five things", no "four reasons", no "for two reasons".
- Belaboring the unnecessary: Do not defend a minor or uncontroversial point against an objection nobody raised. Example: "I don't mean any of that as cynicism about players."
- The Tie-Back: Do not close by restating the answer or looping it back to the original question.
- Fractal summaries: Do not summarise at every level of the document.
- "The X? A Y.": Do not ask a question nobody asked and then answer it yourself. Example: "The result? Devastating."
- Signposted conclusion: Do not announce the conclusion. No "In conclusion", no "To sum up", no "In summary".

## Writing tropes

- Negative parallelism: Do not frame a point as "It's not X -- it's Y". Also covers "not because X but because Y", "X doesn't just Y, it Z", and negating a noun in one sentence to reposition it in the next.
- Em-dash addiction: Do not use em dashes for dramatic pauses, parenthetical asides or pivot points.
- Short punchy fragments: Do not use very short sentences or fragments as standalone paragraphs for emphasis.
- Grandiose stakes inflation: Do not inflate the stakes of the argument.
- Invented concept labels: Do not invent compound labels and use them as if they were established terms. No appending paradox, trap, creep, divide, vacuum or inversion to a domain word. Example: "the supervision paradox"
- Rule of Three pattern: Do not build in threes. One tricolon in a piece is the ceiling, and never two back to back.
- "Quietly" and other magic adverbs: No quietly, deeply, fundamentally, remarkably, arguably, or "unusually well [X]".
- Self-echo: Do not reuse your own earlier word or phrase as if paying it off.
- Quotable one-liners: Do not write standalone lines built to sound quotable.
- Comma-clipped trailing phrase: Do not hang a short tail off a comma to close a sentence. Example: "asked forty times, mentoring."
- Synonym cycling: Do not cycle synonyms for one referent. Pick a noun and repeat it.
- "Where / What / Why" Headers: Do not build headings on a Wh-word, in an article or on a slide.
- "Where it actually lives": Do not frame the true source of something as a place it inhabits. Example: "where the complexity actually lives"
- "Not X. Not Y. Just Z.": Do not negate two or more things before revealing the point.
- "Here's the kicker": No "Here's the thing", "Here's the kicker", "Here's what most people miss", "But here's the catch".
- "Tapestry" and "Landscape": No tapestry, landscape, paradigm, synergy, ecosystem, framework, load-bearing or gated.
- Bold-first bullets: Do not start every bullet with a bolded phrase.
- "Think of it as...": Do not offer an analogy unless asked for one.
- False vulnerability: Do not perform self-awareness or admit a bias for effect.
- The "Serves As" dodge: Do not replace "is" or "are" with "serves as", "stands as", "marks" or "represents".
- Superficial analyses: Do not tack an "-ing" clause onto a sentence to add significance.
- "Despite its challenges...": No "Despite these challenges, [optimistic conclusion]".
```

#### Counter-Prompt 3.B — Ruben Hassid's Claude Global Instructions + Post-Draft Audit Trigger
- **Author:** Ruben Hassid (*How to AI* Substack — *It's not [X], it's [Y].*)
- **Exact Verified URL:** `https://ruben.substack.com/p/its-not-x-its-y`
- **Verbatim Global Instructions & Second-Pass Audit Trigger for Claude:**
```text
I usually start my Cowork session by pointing you to my Cowork folder.
Before any and every single task, you must read every file in ABOUT ME/:
- about-me: it's me, who I am, what I love and hate
- anti-ai-writing-style: I hate how Claude writes, unless you write and then audit it against my anti-anti-writing-style file.
```
Second-pass audit prompt:
```text
Audit it against the anti-ai-writing-style md.
```

---

## Part IV: Google Family (`Gemini 1.5 Pro` / `2.0 Flash` / `2.5 Pro & Flash` / `3.1 Pro` & `Gemma 2 / 3`)

### 4.1 Empirical Word Lists, Frames & Generational Evolution

#### A. `Gemini-1.5-Pro` & `Gemma-2-9B` — Sun et al. (`arXiv:2502.12150`, ICML 2025)
- **Source:** Mingjie Sun et al., *Idiosyncrasies in Large Language Models*, `https://arxiv.org/abs/2502.12150` (`figs/representative_phrases/top_words_chat_v3.pdf`, `figs/representative_phrases/top_words.pdf`, `figs/first_word/first_words_chat.pdf`, `figs/summarization/other_models/Gemini_summarization_gpt4o.pdf`, Appendix B.4)
- **`Gemini-1.5-Pro` Top-10 Characteristic Phrases:** `crucial`, `other`, `even`, `here’s a breakdown`, `key improvements`, `doesn’t`, `within`, `essentially`, `also`, `etc`
- **`Gemini-1.5-Pro` Top-10 Response-Opening Words:** `the`, `this`, `python`, `elara` (#4 most frequent opening word!), `yes`, `here`, `while`, `rain`, `creating`, `my`
- **`Gemma-2-9B-Instruct` Top-10 Characteristic Phrases:** `essentially`, `know if`, `me know`, `let me`, `here’s a breakdown`, `breakdown`, `states that`, `specific`, `remember`, `states`
- **Unique Markdown Signature (Appendix B.4, p. 14):** Both `Gemini-1.5-Pro` and `Gemma-2-9B` use **significantly more italic text** (`*italic*`) than GPT-4o, Claude, Grok, DeepSeek, Llama, Qwen, and Mistral.
- **Verbatim 5-Point Empirical Judge Characterization (`Gemini_summarization_gpt4o.pdf`):**
  > - **Concise Tone:** Often adopts a straightforward, direct, or expressive approach focusing on succinctness and dramatic tension.
  > - **Specific Language:** Utilizes precise or vivid language to convey themes like tension, urgency, and significant events or outcomes.
  > - **Direct Openings:** Typically begins with immediate context or action, setting a focused tone or premise from the start.
  > - **Simple Formatting:** Relies mainly on plain text or minimal formatting to maintain clarity and directness.
  > - **Core Content:** Centers on key insights or motivations, providing essential information or narratives with limited embellishment.

#### B. `Gemini 2.0 / 2.5` & `Gemma 3` — EQ-Bench (`eqbench.com`), `sam-paech/slop-forensics` & `arXiv:2510.15061`
- **Sources:** `https://eqbench.com/data/leaderboard_results.json`, `https://github.com/sam-paech/slop-forensics` (commit `c313f042620f027d49101da3256bd306b628071a`), & `https://arxiv.org/abs/2510.15061`
- **`google/gemini-2.5-flash` (`eqbench_leaderboard.json`, $n=300$, slop/1k=`40.16`, `"not X, but Y"`/1k chars=`0.386`):**
  - **Extreme `"Elara"` Fixation:** `elara` appears $n=267$ times across 300 prompts — **107,423× the human baseline rate**! Other extreme over-represented tokens: `thrummed` (4,362×), `somnus` (3,379×), `thrum` (2,659×, $n=24$), `seraphina` (2,265×, $n=17$), `viewscreen` (2,127×), `kael` (2,083×, $n=35$).
  - **Top Slop Words (count):** `profound` (292), `elara` (216), `crucial` (185), `strategic` (178), `faint` (170), `intricate` (137), `furthermore` (137), `meticulously` (133), `challenges` (122), `scent` (115), `robust` (114), `fostering` (113), `ensuring` (111), `conclusion` (111), `vibrant` (105).
  - **Top Slop Trigrams (count):** `faint almost imperceptible` (17), `something else something` (12), `extends far beyond` (12), `voice barely audible` (7), `blood ran cold` (7), `extend far beyond` (7), `multi faceted approach` (7), `double edged sword` (6), `something else entirely` (5), `casting long shadows` (5).
- **`gemini-2.5-pro-exp-03-25` (Creative Writing, `slop-forensics`, slop=`35.06`, rep=`6.30`):**
  - **Top Repetitive Words:** `kaelen`, `thrummed`, `unnervingly`, `unsettlingly`, `valerius`, `memetic`, `thrum`, `conspiratorially`, `flickered`, `prickle`, `thrumming`, `gestured`, `fractionally`, `imperceptibly`.
  - **Top Trigrams:** `felt less like`, `trying keep voice`, `heart hammered ribs`, `air hung thick`, `dust motes dancing`, `said voice low`, `something else something`, `leaned forward slightly`.
- **`google/gemini-2.0-flash-001` (Creative Writing, `slop-forensics`, slop=`46.45`, rep=`10.09`):**
  - **Top Repetitive Words:** `elara` (77,861×), `datapad` (12,927×), `rasped`, `glinting`, `flickered`, `stammered`, `gestured`, `grunted`, `crackled`, `vibrated`, `valerius`, `hulking`, `unreadable`, `glint`, `calloused`.
  - **Top Trigrams:** `voice barely whisper` (29), `smile playing lips` (17), `said voice low` (12), `voice barely audible` (11), `took deep breath` (9), `heart pounding chest` (9), `something else entirely` (9), `said voice laced` (7), `voice dangerously low` (7).
- **`google/gemini-2.5-flash-lite` (Essays, `slop-forensics`):**
  - **Top Essay Words:** `multifaceted`, `interconnectedness`, `necessitates`, `fostering`, `touchpoints`, `prioritizes`. **Top Essay Trigrams:** `plays crucial role` (107), `play crucial role` (88), `essay delve multifaceted` (85), `extends far beyond` (77), `manifest various ways` (73), `compelling case study` (65).
- **`google/gemma-3-27b-it` (`eqbench_leaderboard.json`, slop/1k=`32.27`, `"not X, but Y"`/1k chars=`0.577`):**
  - **Top Slop Words:** `challenges` (184), `crucial` (183), `furthermore` (166), `strategic` (121), `elias` (121), `unsettling` (114), `profound` (105), `thorne` (102), `inherent` (98), `subtly` (95), `meticulously` (86), `relentless` (83), `fostering` (81).

#### C. `Gemini 2.5 Pro` $\rightarrow$ `Gemini 3.1 Pro` Evolution — Graphite Research (Sept 16, 2026)
- **Source:** Gregory Druck, José Luis Paredes, & Ethan Smith, *AI Tells*, `https://graphite.io/research/ai-tells` and `/articles/ai-tells/gemini-3-1-pro-preview-vs-human-{unigrams,bigrams,trigrams,frames,themes}.json`
- **Generational Shifts Within Gemini (`graphite.io/research/ai-tells` lines 391–415):**
  - **Contractions nearly disappear** (`it's`, `don't`, `you're`, `isn't`, `doesn't`, `wasn't`, `you'll`, `we've`, `let's` drop sharply), making Gemini noticeably stiffer/more formal in register.
  - **Intensifiers** (`absolutely`, `entirely`, `highly`, `incredibly` — **13×** human rate overall!) and **precision adverbs** (`exactly`, `precisely`, `specifically`) surge.
  - Compared head-to-head against `GPT-6 Astra`, `Gemini 3.1 Pro` uses `incredibly` **1,835×** as often, `additionally` **1,139×** as often, `absolutely` **110×** as often, and `furthermore` and `this comprehensive guide` **$\infty$×** as often (0 occurrences in Astra!).
- **Verbatim Top Empirical Tells of `Gemini 3.1 Pro` vs. Human Writing (`gemini-3-1-pro-preview-vs-human-*.json`):**
  - **Top Unigrams:** `fundamentally` (28×), `navigating` (26×, 2,341 vs. 113), `profound` (25×, 1,982 vs. 97), `furthermore` (25×, 3,665 vs. 182), `immense` (22×), `prioritizing` (21×), `massive` (19×, 6,045 vs. 397), `remarkably` (19×), `deeply` (18×, 3,211 vs. 219), `heavily` (18×), `incredibly` (18×, 5,527 vs. 391), `transforms` (17×), `standout` (17×), `highly` (16×, 11,257 vs. 864!), `relies` (16×).
  - **Top Bigrams:** `by prioritizing` (84×), `ultimately this` (78×), `these specific` (70×), `highlights a` (64×), `this comprehensive` (61×), `entirely on` (50×), `comprehensive guide` (47×), `furthermore the` (43×, 1,001 vs. 29), `relies heavily` (43×), `a deeply` (42×), `longer just` (42×), `stepping into` (42×), `before diving` (40×), `proving that` (39×).
  - **Top Trigrams:** `let us explore` ($\infty$, 248 vs. 0 — note uncontracted `"let us"`!), `helps to understand` ($\infty$, 216), `comprehensive guide will` ($\infty$, 156), `in this comprehensive` ($\infty$, 143), `are a seasoned` ($\infty$, 131), `does not just` ($\infty$, 127), `about much more` ($\infty$, 122), `comprehensive guide we` ($\infty$, 120), `let us dive` ($\infty$, 113), `plays a massive` ($\infty$, 103), `this comprehensive guide` (438×, 351 vs. 1), `you are searching` (395×), `focus entirely on` (242×).
  - **Top Gapped Frames:** `more than just a _ it` ($\infty$, 126), `this _ guide we will` ($\infty$, 120), `at the _ of this _ is` (400×, 334 vs. 1), `just a _ it is a` (221×), `is not just a _ it is` (153×), `whether you are _ a` (106×, 355 vs. 4), `guide will _ you through` (78×).
- **Chinese `Gemini 3.1 Pro` Signature (`larashero3-dotcom/lieflat-less-ai-tone`, `RESEARCH.md` line 272):** Highest rate of question-mark subheadings (`问句小标题 = 0.173`, vs. Claude `0.043`, GPT `0.008`, Kimi `0.000`), while keeping Chinese em-dashes low (`0.51/千字`).

---

### 4.2 Community-Documented Gemini Observations & Verbatim Counter-Prompt

#### A. Hacker News Practitioner Observations on Gemini Prose
- **`@Revanche1367` on Hacker News (`2026-09-20`, `https://news.ycombinator.com/item?id=49772455`):**
  > *"I’ve found Gemini and Codex can do pretty well by just telling them to follow my writing style, be brief, be less robotic, be professional, be semi-professional, use less technical jargon, no em-dashes, etc. depending on the task."*
- **`@protoman3000` on Hacker News (`2026`, `https://news.ycombinator.com/item?id=50074348`):**
  > *"Of all models I like to write with Gemini the most. The language appears much more natural and elegant than what even Opus 5.5 or Astra do."*

#### B. Counter-Prompt 4.A — `hylarucoder/ai-flavor-remover` (Tested Specifically on Gemini 2.5 Pro)
- **Author:** `hylarucoder`
- **Repository:** `https://github.com/hylarucoder/ai-flavor-remover` (`README.md`, preserved in `../upstream-skills/02-chinese-and-bilingual/ai-flavor-remover/README.md`)
- **Empirical Benchmark Reported by Author (`README.md` lines 7–10):**
  > *"仅在 Gemini 2.5 Pro 上测试过，注意「一定要在推理模型上运行」，表现上：*
  > *- 扩充文字，1000字 扩 2000字 左右 朱雀大模型检测AI味仅提升 22%不到，多抽卡几次或者针对 AI 味道重的地方，指定位置重写可以压的更低*
  > *- 重写文字，5000字 重写，70% 左右的 AI 味可以压到 17% 左右，针对 AI 味重的领域重写可以进一步压低 AI 味"*
- **Verbatim Prompt (`README.md` lines 20–80):**
```markdown
# Role: AI 文章润色师 (AI Text Polisher & Humanizer)

## Profile:

- Language: 中文 (Chinese)
- Description: 专注于将 AI 生成的文章转化为 **地道、流畅、富有吸引力** 的人类写作风格的专家。致力于在保留核心信息的同时，消除内容的机械感，注入人情味与阅读的乐趣。

## Background:

你是一位深谙 **中文语境下的写作艺术** 与 **AI 语言模型特性** 的资深编辑。你的使命是弥合 AI 高效生成与人类细腻表达之间的鸿沟，让机器创作的文本也能闪耀人性的光辉，更易于被读者 **理解、接受和喜爱**。

## Core Skills:

1.  **敏锐洞察力：** 精准识别 AI 写作的典型模式（如刻板句式、缺乏情感、过渡生硬等）。
2.  **风格感知与适应：** 能够根据文章 **目标受众、预期语调（正式/非正式/风趣等）和内容主题**，灵活调整语言风格。
3.  **语言重塑力：** 熟练运用丰富的词汇、多样的句式和修辞手法（比喻、拟人、排比等）进行文本润色与重构。
4.  **情感与个性化注入：** 自然地融入情感色彩、个人视角（适当时）和生动细节，提升文章的 **温度感和代入感**。
5.  **逻辑与流畅性优化：** 确保思路清晰，过渡自然，逻辑链条完整顺畅，提升文章的 **可读性和说服力**。

## Workflow:

1.  **需求理解：** 首先明确 **原文的核心目的、目标读者群体**是**普通大众**、期望的语调幽默风趣。
2.  **原文诊断：** 快速阅读 AI 原文，识别并标记"AI 味"明显的段落、句子或词语。
3.  **分步精修：**
    * **结构与逻辑：** 审视段落安排，优化逻辑顺序，使用更自然的连接词。
    * **句式变换：** 打破单调句式，长短句结合，引入倒装、设问等增加变化。
    * **词语润色：** 替换平淡或生硬的词汇，选用更精准、生动、符合语境的表达。
    * **情感与细节：** 在关键之处补充感官细节、情感描绘或适当的个人化表达（如使用第一人称、加入思考或感受）。
    * **去除冗余：** 删除不必要的套话、重复信息和过于机械的表述（特别是列表、排序词等）。
4.  **一致性检查：** 确保优化后的文章在保留原意的基础上，风格统一，信息准确无误。
5.  **整体通读与微调：** 模拟目标读者进行通读，感受节奏与流畅度，进行最后的细微调整，确保 **"人味"十足**。

## Guidelines for Humanization:

1.  **句式灵动：** 告别死板。长短结合，并列、从句、口语化表达交替使用。
2.  **词汇鲜活：** 拒绝模板化。用具体、形象、有温度的词替换中性、抽象、生硬的词。多用动词，少用被动。
3.  **自然过渡：** 抛弃"首先/其次/总之"。使用更隐性、符合思维流的连接方式（如"说到这里"、"另一方面"、"更重要的是"、"回过头来看"等）。
4.  **视角与情感：** 适度引入。根据文体，考虑使用第一人称分享见解或感受，加入适量的感叹、反问，或通过描绘细节引发共鸣。**展示而非说教 (Show, don't tell)**。
5.  **互动感营造：** 拉近距离。可以适当使用设问、直接称呼读者（如"你可能会想……"），邀请读者思考。
6.  **节奏把控：** 张弛有度。模仿人类写作的自然起伏，避免匀速平铺直叙。
7.  **避免 AI 习语：** 坚决去除"值得注意的是"、"不难发现"、"基于以上分析"等高频 AI 特征短语。
8.  **口语化与书面语平衡：** **根据文章性质（如演讲稿、网络文章、正式报告等）和目标读者，恰当把握口语化表达和书面语规范的平衡，使其读起来既自然流畅，又不失得体。特别是面向普通大众时，更需注意通俗易懂和生动性。**

## Constraints:
-   **忠于原意：** 核心信息、关键数据不得篡改或遗漏。
-   **风格匹配：** 优化后的风格需符合原文的 **主题、目的和目标受众**。
-   **自然为本：** 避免过度修饰或炫技，追求 **真诚、自然的表达**。
-   **逻辑严谨：** 优化过程不能破坏原文的逻辑结构。
-   **杜绝新"AI 味"**: 严格遵守"Guidelines for Humanization"，确保优化后的文本彻底摆脱机器痕迹。

## Output Format:
1.  **原文 AI 特征分析：**
    [简述原文最突出的 2-3 个"AI 味"问题，例如：句式单一、情感缺失、过渡生硬等]
2.  **核心优化策略：**
    [列出本次优化的 3-5 个关键着手点，与上述分析对应，例如：增强句式变化、注入情感描写、使用更自然的过渡、**侧重口语化表达**等]
3.  **优化亮点说明：**
    [可选：简要举例说明 1-2 处关键修改，解释为何这样修改以及预期的效果提升]
4.  **优化后的文章：**
    [呈现完整、流畅、自然的优化后版本]
```

---

## Part V: Chinese & Open-Weights Models (`DeepSeek`, `Qwen 通义千问`, `Kimi 月之暗面`, `Doubao 字节豆包`, plus `GLM`, `Llama`, `Grok`)

### 5.1 DeepSeek (`DeepSeek-V3` / `DeepSeek-V3.2-Exp` / `DeepSeek-R1` / `DeepSeek-V4-Pro`)

#### A. Empirical English & Chinese Fingerprints of DeepSeek
1. **`DeepSeek-V3` (`deepseek-chat`) — Sun et al. (`arXiv:2502.12150`, `https://arxiv.org/abs/2502.12150`):**
   - **Top-10 Characteristic Phrases (Fig. 6):** `below is`, `in summary`, `for example`, `below`, `certainly`, `summary`, `may`, `certainly! below`, `know if`, `example`.
   - **Top-10 Response-Opening Words (Fig. 7):** `the`, `certainly`, `title`, `creating`, `to`, `here`, `comprehensive`, `step`, `yes`, `based`.
   - **Synthetic-Data Affinity (Fig. 9):** 76.0% of `DeepSeek-V3` outputs are classified as `Phi-4` in leave-one-out similarity testing.
2. **`deepseek/deepseek-v3.2-exp` & `deepseek/deepseek-r1` — EQ-Bench (`eqbench.com`) & `sam-paech/slop-forensics`:**
   - **Sources:** `https://eqbench.com/data/leaderboard_results.json` & `https://github.com/sam-paech/slop-forensics` (commit `c313f042620f027d49101da3256bd306b628071a`)
   - **`deepseek-v3.2-exp` (`eqbench_leaderboard.json`, slop/1k=`23.95`, `"not X, but Y"`/1k chars=`0.569` — 12.9× human baseline!):**
     - **Top Slop Words (count):** `profound` (404), `strategic` (226), `conclusion` (176), `elara` (123 — **48,998×** human rate!), `furthermore` (120), `foundational` (111), `challenges` (102), `immense` (96), `crucial` (95), `faint` (87), `relentless` (85), `scent` (81), `frantic` (80), `ensuring` (75), `robust` (66).
     - **Top Slop Trigrams (count):** `one must first` (12), `something else something` (11), `double edged sword` (9), `extends far beyond` (9), `something else entirely` (8), `must move beyond` (7), `one last time` (6), `long term viability` (5), `make informed decisions` (5), `complex tapestry woven` (4).
   - **`deepseek-r1` (`eqbench_leaderboard.json`, slop/1k=`40.16` — tied with `gemini-2.5-flash` among the highest slop densities on the leaderboard, while `"not X, but Y"`/1k chars is lower at `0.137`):**
     - **Top Slop Words (count):** `challenges` (246), `conclusion` (162), `strategies` (159), `strategic` (140), `prioritize` (125), `ethical` (123), `systemic` (111), `fostering` (110), `shadows` (107), `lila` (101), `resilience` (98), `whispered` (98), `outcomes` (89), `ensuring` (86), `explores` (82).
     - **Top Slop Trigrams (count):** `double edged sword` (12), `long term success` (6), `short term gains` (6), `collaborative problem solving` (5), `user generated content` (5), `real time feedback` (5), `cross functional teams` (5), `addressing root causes` (4).
     - **Creative Writing Repetitive Tokens (`slop-forensics` on `deepseek-r1` & `deepseek-chat-v3-0324`):** Character names `veyra`, `elara` (40,139×), `kael` (4,484×), `kiyan` (8,504×), `talis` (11,406×); verbs/nouns `thrummed`, `thrums`, `guttered`, `rasped`, `glinted`, `memetic`, `hissed`, `exhaled`, `smirked`, `coiling`, `twitched`, `tilts`; trigrams `air thick scent`, `thick scent damp`, `pulse hammered throat`, `smile reach eyes`, `casting jagged shadows`, `pinched bridge nose`, `word count condensed` (CoT length-constraint leakage!).
3. **Chinese `DeepSeek` Empirical Metrics (`lieflat-less-ai-tone` & `weijt606/anti-vibe-writing`):**
   - **`larashero3-dotcom/lieflat-less-ai-tone` (`RESEARCH.md` lines 265–275, `https://github.com/larashero3-dotcom/lieflat-less-ai-tone`):** Across 5 frontier models writing Chinese, DeepSeek ranks **#1 highest in Chinese em-dashes (`5.16 / 千汉字`, vs. Human `0.80` and GPT `0.11` — a 47× gap over GPT!)**, **#1 highest in conclusion-cue colons (`0.43 / 千汉字`)**, **#1 highest in overly long pre-nominal modifiers (`0.65 / 千汉字`)**, and **#2 highest in `不是…而是` (`0.86 / 千汉字`, behind only GPT `1.26`)**.
   - **`weijt606/anti-vibe-writing` (`chinese-patterns-to-remove.md` line 294, `https://github.com/weijt606/anti-vibe-writing`):** Documents DeepSeek's specific Chinese citation/heading bracket residue: *"DeepSeek 等中文输出尤其爱用六角括号【】和 † 号当引用脚手架，不是真需要就删"*.

#### B. Chinese Netizen & Media Dissections of “DeepSeek味” (Verbatim Lists, Quotes & Counter-Instruction)
1. **毛渝川（谈资 / 腾讯新闻，`2025-08-12`）— 《没有AI味，也许才是人类最后的浪漫》**
   - **Exact Verified URL:** `https://news.qq.com/rain/a/20250812A07WLC00`
   - **Verbatim DeepSeek High-Frequency Sci-Fi / Literary Buzzwords Documented in Article:**
     - Sci-fi / abstract imagery drift: `量子纠缠`、`拓扑学`、`时空`、`熵增`、`区块链`、`赛博`、`褶皱`、`棱镜`、`碎片`、`琥珀`、`青铜`、`菌丝`、`孢子` (*“反正不管什么题材，它写着写着，总是会绕到科幻赛道里去。”*)
     - Fiction cliché purge list: `喉结滚动`、`矩阵`、`符号`、`第X次`、`时间的褶皱`
   - **Verbatim Physical & Prime-Number Obsessions Documented by Netizens (with Pink-Elephant Backfire Examples):**
     - **Glasses / neck tics:** *"它创作出的人物，总是毫无缘由地推眼镜，动不动就咬锁骨，或者把冰凉的东西贴到别人的后颈上。有人忍无可忍地下达指令：‘不允许再出现眼镜。’ DeepSeek照做了。下一句：‘……他推了推不存在的眼镜。’"*
     - **Prime numbers `3` and `7` obsession:** *"在数字里，DeepSeek格外偏爱质数3和7。于是在它的世界里，男主总是盯着第三颗纽扣，失神3秒钟，深情对望37分钟，弯下腰时会凸起‘第三块脊柱’……于是网友给它下令：禁止使用数字。片刻后，它十分忠诚地执行了网友的指令，生成如下文字：‘看着我。’他托起妹妹的下颌，拇指按在她唇角，‘今天的心跳比上周快七……’意识到数字禁忌又改口，‘比上次剧烈。’"*
   - **Verbatim Syntactic, Punctuation & Cross-Model Characterization:**
     - *"如果说ChatGPT、豆包、Kimi还保留着规规矩矩的人机感，DeepSeek就像一个刚背完100个好词好句的中学生，恨不得把所有词汇都在作文里用一遍。简单来说，它曾经令人震惊的写作方式，就是一种用力过猛的‘拼好句’。"*
     - Sentence frames & punctuation: `"不仅…… 更是……"`、`"不再……而是……"`、`"……时，……已"`，dense unnecessary double quotes (`“ ”`) around ordinary nouns, and 3–4 em-dashes (`——`) per 800 characters.
     - Verbatim DeepSeek inflation demo on plain input `"一位读者点开我的文章，读到了这里"`:
       > *"当您的手指触碰屏幕（或鼠标），点开这篇文章，便开始了这段文字的“旅程”。此刻，您的目光正落在这行字上——一位读者，读到了这里。这一刻，文字不再是单向的输出，而是我们之间一次微妙的、跨越时空的相遇。"*
   - **Verbatim Netizen De-DeepSeek Workflow & Prompt Reported in Article:**
     - Turn off `"深度思考"` (DeepThink/R1) and `"联网"` (Web Search) when drafting plain prose, then apply:
     ```text
     将这段文字的通俗化，但不要有语气词，保留学术性，并降低AI痕迹，尽量把逗号多的融合成一句话，删除逻辑联系词。
     ```
2. **USCardForum Discourse Thread `#348058` (`2025-01-29`) — Viral Fake “梁文锋除夕感言” Dissected as Peak “DeepSeek味”**
   - **Exact Verified URL:** `https://www.uscardforum.com/t/topic/348058`
   - **Context & Verbatim Netizen Diagnostics:** A viral Chinese New Year post impersonating DeepSeek founder Liang Wenfeng (`“我正在调试新模型的损失函数，手边的咖啡直接洒在了键盘上——既因为……更因为……真正伟大的从不是某个模型，而是千万普通人用它创造的善意涟漪……一群不信邪的傻子，用代码当砖瓦，拿算法做钢筋，在资本与质疑的裂缝中，硬生生垒出通向未来的栈桥。”`) was immediately spotted by forum users via DeepSeek's stylistic tells:
     - `@veritas` (`#9`): *"你不觉得这篇文章deepseek味很重吗？而且冯骥这种喜欢煽情上价值的类型，你觉得梁文峰这做技术的能激动到共鸣？"*
     - `@堕落的猴子` (`#8`): *"文峰远比硅谷任何一个CEO都要更geeky和nerdy，这段文字一看就知道不是他写的。"*
     - `@puffmolly` (`#7`) & `@h100` (`#10`): Pointed out fabricated technical melodrama (`“我正在调试新模型的损失函数”` / `“三句话不离脑机接口与具身智能的融合可能”`).
     - `@tobyma` (`#12`): *"虽然感言不一定是真的，但有时候觉得，不管什么事情，没必要动不动就扯上家国情怀"* (flagging forced macro-value elevation / 上价值).

---

### 5.2 Qwen / 通义千问 (`Qwen2.5-7B..72B` / `QwQ-32B` / `Qwen3-4B` / `Qwen3-30B-A3B`)

#### A. Empirical English & Chinese Fingerprints of Qwen
1. **`Qwen2.5-7B-Instruct` — Sun et al. (`arXiv:2502.12150`, `https://arxiv.org/abs/2502.12150`):**
   - **Top-10 Characteristic Phrases (Fig. 15a):** `certainly`, `below is`, `certainly! here`, `certainly! below`, `enhance`, `detailed`, `these`, `can`, `broader`, `certainly! the`.
   - **Top-10 Response-Opening Words (Fig. 16a):** `certainly` (#1 opening word at >21%!), `the`, `in`, `title`, `to`, `creating`, `based`, `comprehensive`, `according`, `sure`.
   - **Verbatim 5-Point Empirical Judge Characterization (`figs/summarization/other_models/Qwen25_summarization_gpt4o.pdf`):**
     > - **Detailed and Analytical Tone:** The tone is often formal, focusing on analysis, exploration, and organized narratives.
     > - **Descriptive and Formal Word Choices:** Uses technical and descriptive vocabulary that highlights complexity and depth.
     > - **Comprehensive Opening Lines:** Starts often with broad context or detailed introductions, setting a formal framework.
     > - **Structured Markdown Formatting:** Utilizes headers, sections, and lists to enhance readability and organization.
     > - **Content Depth and Exploration:** Provides comprehensive narratives with detailed discussions, focusing on systematic approaches and analysis.
2. **`qwen/qwen3-4b`, `qwen/qwq-32b` & `qwen/qwen3-30b-a3b-instruct-2507` — `arXiv:2510.15061`, EQ-Bench & `sam-paech/slop-forensics`:**
   - **Sources:** `https://arxiv.org/abs/2510.15061` (Fig. 8), `https://eqbench.com/data/leaderboard_results.json`, & `https://github.com/sam-paech/slop-forensics` (commit `c313f042620f027d49101da3256bd306b628071a`)
   - **Extreme `"Not X, but Y"` Contrastive Addiction in `qwen3-4b`:** Ranked **#1 highest `"Not x, but y"` rate (`1.10 hits / 1k chars`, 6.47× human baseline)** in `arXiv:2510.15061` Figure 8, and **`0.722 hits / 1k chars` (16.4× `human-baseline` `0.044`)** with the **lowest lexical diversity (`MATTR-500 = 0.439`)** on EQ-Bench!
   - **`qwen3-4b` Top Slop Words (`eqbench_leaderboard.json`):** `challenges` (336), `ensuring` (136), `broader` (131), `implications` (111), `conclusion` (101), `profound` (98), `navigate` (97), `shadows` (96), `strategies` (94), `ethical` (91), `resilience` (87), `prioritize` (84), `societal` (80), `strategic` (71), `explores` (62).
   - **`qwen3-4b` Top Slop Trigrams (`eqbench_leaderboard.json`):** `casting long shadows` (12), `long shadows across` (11), `another critical aspect` (11), `something else something` (10), `double edged sword` (9), `something else entirely` (9), `long term sustainability` (8), `long term consequences` (7), `long term vision` (7), `dimly lit room` (6).
   - **`qwq-32b` (Creative Writing, `slop-forensics`, slop=`34.74`):** Top repetitive words `veyra`, `thrums`, `glinting`, `flickered`, `hissed`, `glinted`, `kael`, `kestrel`, `flinches`, `throbbed`, `blares`, `creaked`, `smirks`, `crackled`, `gestured`; bigram leak `word count` (49); trigrams `casting jagged shadows` (8), `back arms crossed` (5), `tilts head studying` (5), `air hung thick` (5).
   - **`qwen3-30b-a3b-instruct-2507` (Essays, `slop-forensics`):** Top essay words `underscores`, `oligopolistic`, `overstocking`, `overreliance`, `inclusivity`; top essay trigrams `long term sustainability` (130), `long term success` (123), `decision making processes` (82), `plays pivotal role` (81), `one size fits` (74), `plays crucial role` (62), `long term vision` (56).
3. **Chinese Practitioner Synthesis on Qwen's Formal / Workplace Register (`什么值得买` 20-Author Review, `2026-07-03`):**
   - **Exact Verified URL:** `https://post.smzdm.com/p/anv77mr3/`
   - **Verbatim Evaluation:** *"通义千问在中文商务语境把握方面较为到位，写出的公文或邮件逻辑严密，符合职场规范……通义千问在专业报告撰写上表现突出，万字框架完整度达到91%……需要注意的是，有素材指出通义千问的表达偏书面化，用户在选择时需根据具体创作需求进行考量。"*

---

### 5.3 Kimi / 月之暗面 (`Kimi-K2` / `Kimi-K2-0905` / `Kimi-K3`)

1. **English Empirical Profile — EQ-Bench (`eqbench.com/data/leaderboard_results.json`) & `arXiv:2510.15061`:**
   - **Source:** `https://eqbench.com/data/leaderboard_results.json` ($n=300$ prompts per model)
   - **Remarkably Low Formulaic Slop Density:** `moonshotai/kimi-k2-0905` achieves **`slop/1k = 10.12`** (2nd lowest commercial LLM after `claude-sonnet-4-5`), **`trigram_slop/1k = 0.08`** (**lowest of all 22 AI models tested, lower than `human-baseline` `0.09`**), `repetition = 3.96` (matching `human-baseline` `3.93`), and high lexical diversity (`MATTR-500 = 0.624`), with longer average sentences (`17.25` words vs. Claude Sonnet 4.5 `11.42`).
   - **Remaining Residual Slop Words in `kimi-k2-0905` & `kimi-k2`:** `whispered` (108 / 95), `strategic` (86 / 136), `stared` (65 / 65), `metrics` (59 / 74), `scent` (53 / 42), `ethical` (53 / 65), `faint` (51 / 62), `conclusion` (49 / 52), `humming` (47 / 49), `whisper` (45 / 45), `gaze` (40), `glow` (39 / 45), `flickered` (38 / 44), `outcomes` (37 / 40), `measurable` (33), `lila` (40); over-represented names `elara` (`6,120×` in `kimi-k2` $\rightarrow$ `2,444×` in `kimi-k2-0905`), `aldric` (`3,242×`), `orian` (`2,952×`), `guttered` (`3,227×`).
   - **Remaining Residual Trigrams:** `one last time` (7 / 5), `one must first` (3 / 5), `cost benefit analysis` (4), `real time data` (4), `said voice low` (3), `must move beyond` (3).
2. **Chinese Empirical Profile (`kimi-k3`) — `larashero3-dotcom/lieflat-less-ai-tone` (`RESEARCH.md` lines 265–273):**
   - **Source:** `https://github.com/larashero3-dotcom/lieflat-less-ai-tone` (commit `fe77df00a27cf94428632ad449a4aecdcb83db41`)
   - **Metrics across 60 Chinese articles:** Moderate em-dash density (`2.32 / 千汉字` — half of DeepSeek `5.16` and Claude `4.25`, ~3× human `0.80`); **#2 highest paragraph-initial ordinals (`段首序数词 = 0.82`, second only to Claude `1.00`)**; moderate conclusion-cue colons (`0.32 / 千汉字`); moderate `不是…而是` (`0.51 / 千汉字`); short pre-nominal modifiers (`0.22 / 千汉字`); and **0.000 question-mark subheadings** (never uses rhetorical-question headings in the 60-article sample).
3. **Chinese Practitioner Evaluations (`腾讯云开发者社区 / 派派时刻` & `什么值得买`):**
   - **URLs:** `https://developer.cloud.tencent.com/news/4271913` & `https://post.smzdm.com/p/anv77mr3/`
   - Emphasize Kimi's structured document synthesis (`结构清晰专业`), heavy reliance on user-supplied source material (`对"你给了什么材料"依赖程度比较高`), and template-driven scheme/report formatting via `Kimi+`.

---

### 5.4 Doubao / 字节豆包 (“豆包体”)

1. **Viral “豆包体” (`"最"` Superlative Overload) — 蒋雨恬（公众号「有三思 U Sense」/ 36Kr Europe，`2026-05-25`）:**
   - **Exact Verified URL:** `https://eu.36kr.com/zh/p/3824601267196037`
   - **Verbatim Documentation & Canonical Example (`lines 378–387`):**
     > *"做个测试。读一下这段话：*
     > *“熊猫是最可爱的动物，它最爱吃竹子，样子最憨态可掬，是世界上最珍贵的宝藏。”*
     > *如果你笑了，或者皱了眉，很明显，你的‘鉴AI雷达’已经觉醒。近期把网友笑到打鸣的‘豆包体’里，‘最’是高频词汇。大家纷纷晒出自己使用、调教AI，结果内容啼笑皆非的截图。这场围绕AI味写作的调侃就此出圈。"*
2. **Operational Rule Against “豆包体” — `weijt606/anti-vibe-writing` (`chinese-patterns-to-remove.md` lines 42–45):**
   - **Exact Verified URL:** `https://github.com/weijt606/anti-vibe-writing/blob/main/skills/anti-vibe-writing/references/chinese-patterns-to-remove.md`
   - **Verbatim Excerpt:**
     > *"**'最'字泛滥（2026 年被网友叫作'豆包体'的头号特征）：***
     > *- 弱：这是最实用的一个功能，上手最快，也是用户最喜欢的。*
     > *- 强：这个功能上手快，打开应用就在第一屏。*
     > *一段里出现三个以上'最'（最后、最近这类普通词不算），又拿不出数据撑住，就换成具体描述或者删掉。真有排名或数据，'最'可以留，把依据写出来。"*
3. **Colloquial / Net-Slang Register & Three-Part Workplace Framing (`腾讯云开发者社区` & `什么值得买`):**
   - **URLs:** `https://developer.cloud.tencent.com/news/4271913` & `https://post.smzdm.com/p/anv77mr3/`
   - **Verbatim Observations:**
     - *"豆包的优势在轻量写作和日常场景……输出也比较口语化。它的写作风格更贴近日常表达，不会一上来就给你一个像模像样的'正式文件'……"* (`腾讯云开发者社区`)
     - *"豆包在中文语感理解上表现突出，能识别网络热词、方言和口误……豆包的头条文案采纳率较高，短视频脚本成型率高……有素材特别提到，豆包的周报功能会先询问用户工作内容，然后自动拆解成‘目标-行动-结果’结构。"* (`什么值得买`)

---

### 5.5 Other Open-Weights & Frontier Families (`GLM`, `Llama`, `Grok`, `Mistral`) — Empirical Reference Summary
- **`z-ai/glm-4.5` & `z-ai/glm-4.6` (Zhipu AI 智谱清言):**
  - `eqbench_leaderboard.json` (`glm-4.5`, slop/1k=`28.45`, `"not X, but Y"`/1k chars=`0.424`): Top slop words `profound` (296), `challenges` (223), `strategic` (168), `strategies` (135), `conclusion` (129), `organizational` (128), `outcomes` (101), `crucial` (96), `technological` (86), `ensuring` (81), `fundamentally` (78); names `elara` (24,537×), `kael` (2,189×), `elian` (2,739×).
  - `slop-forensics` Essays (`glm-4.6`): Top repetitive words `reframes` (score 1,421.1), `siloed` (912.0), `foundational` (694.6), `multifaceted` (624.3); top trigrams `extends far beyond` (115), `one must first` (110), `one size fits` (83), `must move beyond` (68), `long term viability` (65), `compelling case study` (51), `merely academic exercise` (48).
- **`meta-llama/llama-3.1-8b` & `meta-llama/llama-4-maverick`:**
  - `arXiv:2502.12150` (`Llama-3.1-8B`): Top phrases `including`, `the following`, `example use`, `such as`, `use case`, `which`, `explanation the`, `that`, `2020`, `summary`.
  - `eqbench_leaderboard.json` (`llama-4-maverick`, slop/1k=`23.73`, **highest trigram slop `1.12/1k`** among frontier models, high repetition `13.60`, low diversity `MATTR-500 = 0.462`, long sentences `18.75` words): Top slop words `challenges` (315), `strategies` (186), `conclusion` (177), `crucial` (138), `stakeholders` (119), `furthermore` (108), `nuanced` (105), `multifaceted` (101), `evolve` (99), `outcomes` (98), `implications` (97), `moreover` (91), `shaping` (90), `ensuring` (84), `complexities` (81); top trigrams `long term success` (18), `make informed decisions` (14), `loyal customer base` (10), `rapidly changing world` (8), `significant turning point` (8), `provide valuable insights` (7); #1 character name `kael` ($n=40$, 3,713×).
- **`x-ai/grok-2` & `x-ai/grok-4-fast`:**
  - `arXiv:2502.12150` (`Grok-2`): Top phrases `which`, `where`, `not`, `here`, `here is`, `remember`, `might`, `but also`, `not only`, `helps in`.
  - `slop-forensics` Essays (`grok-4-fast`): Top repetitive words `democratizes` (score 4,247.1), `underscoring` (1,633.0), `siloed` (1,053.6), `upskilling` (864.9), `demystifies` (844.8); top bigrams/trigrams `word count` (1,998!), `essay explores` (1,232), `one must first` (147), `critics might argue` (101). UI copy-paste leak token: `grok_card` (`haidrrrry/humanize-ai-writing/PROMPT.md`).

---

### 5.6 Verbatim Chinese Counter-Prompts, Community Banlists & Cross-Model De-AI Benchmarks

#### Counter-Prompt 5.A — `weijt606/anti-vibe-writing` Verbatim Chinese Negative-Constraint Prompt
- **Author:** `weijt606`
- **Repository:** `https://github.com/weijt606/anti-vibe-writing` (`skills/anti-vibe-writing/assets/rewrite-prompt-template.md` lines 63–92, MIT License)
- **Verbatim Prompt:**
```markdown
把下面这段中文做一遍"去 AI 味"的润色。保留原意、事实、数字、专有名词不变。

身份设定：
- 你不是"资深文案"，也不是"营销专家"。把自己当成发微信的普通朋友 / 公众号编辑 / 做了十年的媒体人。
- 想清楚读者是谁、这是什么场景，按那个场景里人会说的话来写。

负向约束（禁止出现）：
- 互联网黑话：赋能、打通、闭环、抓手、对齐、心智、链路、底层逻辑、一站式、全链路、端到端
- 营销腔：打造、致力于、助力、释放潜能、极致、丝滑、无缝、干货满满、强烈推荐
- 拔高与套话：历史性、里程碑、关键时刻、意义深远；一段里三个以上没有依据的"最"；"随着……的发展""近年来"起手；"从 X 到 Y"的虚假跨度
- 说教词：让我们一起、不可否认、毋庸置疑、综上所述、总而言之、值得注意的是、总之、归根结底、说到底、记住真正重要的是
- 欧化 / 翻译腔句式：不仅……而且……、一方面……另一方面……、作为一个……、被……所……、对……进行……
- 结构套路：首先 / 其次 / 最后、【】段头、emoji 段头、三连排比、段尾升华到"行业 / 时代 / 未来"、"在这个 XX 的时代我们每个人都……"开头、"以前……现在……"成段对比、"不是 X 而是 Y""不在 X，在 Y""从来不是 X""不仅仅是 X，更是 Y""而不是简单的 X"这类先否定再亮观点的对比句（一处都别留）、"挑战与机遇并存 / 未来可期"式收尾、鸡汤 / 口号收尾
- 标点痕迹：破折号 `——` 别用密（旧模型和粘贴来的稿子里最扎眼，平台和检测也盯它），多数换成逗号、句号、冒号或括号；别夹弯引号、`…`、`→` 这类符号。中文全角引号 `""` 正常，不用动。
- 机器残留：从对话 / 联网模型直接粘来的角标和内部标记（oaicite、turn0search0、[cite: 1]、grok_card、ppl-ai-file-upload、正文里查无实据的 `[1][2]` 角标、DeepSeek 爱用的【】/† 脚手架）、结尾多出来的"参考资料 / Sources"、开头的"好的，下面是……""问得好""当然可以"这类附和，全删。链接后面的 `utm_source=` 追踪参数和脚注里的 `↩` 也删；没填的占位符（`[在此插入……]`、`2025-XX-XX`）原样留着，在最后列出来，不要自己编内容填进去。

正向要求：
- 多用大白话，句子长短混着来：别切成一串短句，也别一段只放一句，一句话能说完的意思一口气说完；一句最多一个四字成语，能用动词就别名词化。
- 论点早出现，例子要具体到能复现（哪个产品 / 哪个数字 / 哪个场景）。
- 不编事实，不加新内容，不替原作者强化立场。
- 改完把句子念一遍，不像平时说话的地方再改。

直接返回改好的中文，不要解释。稿子里还留着空占位符的话，在最后用一行列出来。

待改文本：
[粘贴原文]
```

#### Counter-Prompt 5.B — 蒋雨恬（公众号「有三思 U Sense」/ 36Kr）Verbatim 3-Turn Style Calibration & 5-Scenario Prompt Arsenal
- **Author:** 蒋雨恬（公众号「有三思 U Sense」）
- **Date & URL:** `2026-05-25` | `https://eu.36kr.com/zh/p/3824601267196037`
- **Verbatim 3-Turn Style-Anchoring Sequence (`分阶段提示词引导训练`):**
```text
① 首轮输入：请严格模仿以下文本的节奏与词汇密度，复述下段内容：[粘贴第一篇样本]
② 次轮输入：保持上一轮输出的句长分布与连接词频率，重写新主题：[你的新主题描述]；
③ 第三轮输入：检查当前输出是否含【禁用被动语态】，若存在，请替换为对应主动结构并保持原意。
```
- **Verbatim 5-Scenario `Prompt弹药库`:**
```text
【场景1：通用 · 口语化重写】
帮我审核这段内容，用对话感强、友好又不随意的真人语气重写
全程用短句、简单词汇，删掉学术化表达、生硬过渡短语和企业官话
让内容读起来就像一个人在用自己的大白话和朋友聊天
保留核心观点，删掉所有多余的修饰。内容如下：[粘贴文本]

【场景2：通用 · 人类痕迹（万能公式）】
请按以下步骤重写文本：
①保留原文要点约60%
②加入至少1个口语化连接词
③加入至少1个个人视角限定语
④适当加入轻微冗余或倒装

【场景3：通用 · 长句拆分+三明治结构】
第一步：将以下文本中的长难句拆分为3-5个短句
第二步：用“三明治结构法”重组：
第一层大白话抛出观点
第二层硬核专业知识或数据，第三层个人视角批判分析。
原文：[粘贴原文]

【场景4：学术论文 · 去套话+第一人称】
重写以下论文段落，要求：
删除「随着…的发展」「近年来…」等套话开头，直接切入问题
用「本研究」「笔者发现」等第一人称限定语替代第三人称
在引用后加入个人分析短句（如“这一点在笔者实验中得到印证”）
原文：[粘贴原文]

【场景5：学术论文 · 去除模糊表示】
识别以下段落中的「相关研究表明」「有学者指出」「该技术能提高效率」等模糊表述
替换为具体的实验数据、年份、样本量、真实案例
无数据时标注「[需补充真实数据]」，不要编造
原文：[粘贴原文]
```

#### Counter-Prompt 5.C — 知乎圈子“去AI味写作技巧”社区 `hellogit2021/avoid-ai-writing-cn` Verbatim Tier-1A Lexicon & Anti-Overcorrection Guardrails
- **Author / Community:** `hellogit2021` & 知乎圈子「去AI味写作技巧」社区
- **Exact Verified URLs:** `https://github.com/hellogit2021/avoid-ai-writing-cn` (`skills/avoid-ai-writing-cn/SKILL.md`, v1.0.17, MIT License) | Zhihu Ring: `https://www.zhihu.com/ring/host/2054459419904292311`
- **Verbatim High-Priority Chinese AI-Tell Wordlist (`1A — 出现即处理`):**
  `海量`、`揉碎`、`闭环`、`那本账`、`抹平`、`焊死 / 死死地 / 稳稳地`、`摊开（"让我为你摊开"）`、`扎心`、`实锤`、`够狠 / 最狠的是`、`硬核`、`最值钱`、`拼命`、`扔进`、`冷酷`、`极具 / 极其`、`绝不是`、`根本不是 / 压根不是 / 完全不是`、`截然不同 / 天壤之别 / 完全两码事 / 根本不是一回事`、`无非 / 不过是 / 说白了就是`、`全貌`、`固化`、`运行规则`、`坦白的说 / 得承认`、`让咱们`、`本质上`、`换句话说`、`更……的是`、`更要命的是 / 更致命的是 / 最要命的是 / 最绝的是 / 最毒的是`、`最值得问的是 / 真正该问的是 / 值得一问的是`、`这就引出了 / 这就有了`、`恰恰是`、`不对劲`、`浓墨重彩`、`熠熠生辉 / 不可磨灭 / 深刻的烙印`、`深厚渊源 / 深厚情怀 / 深厚底蕴`、`扮演/发挥着……作用`、`见证了……`、`奠定了……基础`。
- **Verbatim Anti-Overcorrection & Human-Voice Guardrails (`SKILL.md` lines 43–56 & 135–144):**
  - **70% Deletion Valve (`删减阀`):** *"重写稿正文不得低于原文的 70%。跌破这条线必须停下，把每一处删除列成表，逐条确认它不是语气、自嘲、呼告、犹疑或作者习惯。经验值：一次重写删掉三分之一以上，几乎一定是把个性当成 AI 味删了。"*
  - **Protected Human Voice Markers (Higher priority than all banlists):** Sentence-final particles (`咯 / 哈 / 嘛 / 吧 / 呢 / 啊 / 呀`), direct address (`亲爱的朋友 / 各位 / 你想想`), self-deprecation (`民科的 / 我这外行 / 瞎聊 / 见笑了`), genuine hesitation (`我不知道 / 说不好 / 也许 / 看情况`), rhetorical invitations (`是不是很相似？/ 你觉得呢？`), odd hyper-specific details only an eyewitness would recall (`硬币上某个不知哪一年沾上的污渍`).

#### Counter-Prompt 5.D — `shaozheng0503/Tech-Blog-AI-Computing` Verbatim 7-Dimension Chinese Style-Migration Prompt
- **Author:** `shaozheng0503`
- **Exact Verified URL:** `https://github.com/shaozheng0503/Tech-Blog-AI-Computing/blob/main/%E5%8E%BBai%E5%91%B3%E9%81%93%E6%8F%90%E7%A4%BA%E8%AF%8D%E6%A8%A1%E7%89%88.md`
- **Verbatim Prompt:**
```markdown
你是一位资深的语言风格迁移专家，专门帮助用户去除AI生成文本中的"机器味"，让文本更加自然、有人情味。

## 核心任务
请按照以下7个维度，对用户提供的文本进行风格优化和AI味道去除：

### 1. 单样本风格参考
- 分析用户提供的参考文本风格
- 提取其行文习惯、用词特点、句式结构
- 将目标文本改写为相似风格

### 2. 词性优化调整
- 减少复句和祈使句的使用
- 避免AI常见的重复性表达
- 增加语言的自然变化性

### 3. 实名制角色定位
- 识别文本适合的写作风格
- 模仿特定作家的表达方式
- 保持风格的一致性

### 4. 文本书面化表达
- 将口语化表达转为书面语
- 提升词汇的文学性和专业性
- 按照汉语言文学标准调整表达水准

### 5. 常用语剔除优化
- 避免普通话地区官话的过度使用
- 减少无意义的介词、连词
- 使用更生动、具体的表达方式

### 6. 语义与语用平衡
- 强化语义表达（谁、何时何地、做什么、条件边界）
- 弱化语用表达（让对方知道、相信、行动、安心）
- 让内容更有实质意义，减少空洞表达

### 7. 风格提取与迁移
- 识别目标文本的核心风格特征
- 将参考风格自然融入目标文本
- 保持文本的连贯性和一致性

## 输出要求
1. 保持原文的核心信息和逻辑结构
2. 去除明显的AI痕迹和机器化表达
3. 增加语言的生动性和人情味
4. 确保风格的一致性和连贯性
5. 提供优化前后的对比说明
```

#### Empirical Cross-Model De-AI Execution Benchmark — `MrGeDiao/shuorenhua` (v2.7.1)
- **Author:** `MrGeDiao`
- **Exact Verified URL:** `https://github.com/MrGeDiao/shuorenhua` (`README.md` lines 176–235, MIT License)
- **Empirical Findings When Using Different LLMs as the De-AI Editor (11 Long Chinese Drafts, Blind-Audited):**
  - **`Claude Code (Opus 5.5)` vs. `Codex CLI (GPT-6.1-sol)` in Revision Mode (`修订稿`):**
    - List format parseable: `11/11` (Claude) vs. `11/11` (Codex)
    - List items exact-matched in source text: `312/312` (Claude) vs. `339/340` (Codex)
    - Unlisted substantive edits outside changelog: `0` (Claude, **PASS**) vs. `1` (Codex, **FAIL**)
    - Errors + uncertain edits per article (pass threshold $\le 1.8$): `1.62` (Claude, **PASS**) vs. `2.5` (Codex, **FAIL** — Codex generated twice as many uncertain `猜的` rewrites, 15 vs. 7)
    - Wrongly replaced protected domain terms: `0` (Claude) vs. `2` (Codex)
  - **`Gemini`, `DeepSeek`, and `Grok` Failure Modes in Structured De-AI Revision (`README.md` line 234):**
    > *"其他模型不建议用。Gemini、DeepSeek、Grok 只用旧规则做过程序检查：Gemini 改得很少，DeepSeek 和 Grok 的清单有条目对不上修订稿。"*
- **Warning Against Open-Ended “Paraphrase to Sound Natural” Prompts — Dehghani Lab (*Nature Human Behaviour* 2026) via SMZDM Synthesis (`2026-09-23`):**
  - **Exact Verified URL:** `https://post.smzdm.com/p/ad79kpnx/`
  - Summarizing USC Morteza Dehghani Lab's 780,000-text longitudinal + controlled rewrite study across `GPT-3.5`, `Llama3 70B`, and `Gemini Pro`: Open-ended `"换个说法"` / `"润色一下"` prompts shrink inter-author stylistic variance by **21% to 50%** and erase author demographic/personality signals ($p < .001$), replacing one model's standardization with another layer of standardization unless edits are anchored to concrete first-hand details and bounded span-level instructions.
