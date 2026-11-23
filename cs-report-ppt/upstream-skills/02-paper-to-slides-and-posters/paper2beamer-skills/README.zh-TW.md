# paper2beamer-skills

[English](README.md) | **繁體中文**

一套可重複使用的**技能庫**，用來閱讀、理解、講解與彙整學術論文——**不限研究領域**，並可透過每個工作區的 `domain.md` 調整成你的研究方向。

它不是一個「PDF 轉投影片」的工具。目標是協助研究者閱讀、理解、重新組織、講解、評析並彙整論文，讓產出讀起來像是一位細心的研究生準備了一場研討會報告或研究備忘錄——而不是大型語言模型隨手列出的淺薄條列。

> **狀態：實驗性質——早期釋出。** 這是一套可重複使用的技能庫，而非成熟產品。它主要是以**代理人工作流程**（由 AI 代理人閱讀各 `SKILL.md` 並照著執行）的形式測試，而非傳統 CLI 工具，目前實際測試仍相當有限。**請務必手動檢查產出**——確認投影片能編譯且易讀，並在依賴或上台前，核對每一個論點、數字與引用是否與原始論文相符。介面與用語仍可能變動。

## 專案內容

```text
.
├── AGENTS.md                 # 任務分流 + 給代理人的全域原則
├── README.md                 # 英文版說明
├── README.zh-TW.md           # 本檔（繁體中文）
├── LICENSE                   # MIT License
├── CHANGELOG.md              # 版本／變更紀錄
├── Makefile                  # repo 層級測試 / compile / hygiene checks
├── docs/                     # quickstart、prompt 範本、copyright policy
├── skills/
│   ├── paper-beamer-deck/        # 單篇論文 → 詳盡的 XeLaTeX Beamer 投影片
│   │   ├── SKILL.md
│   │   ├── templates/            # main.tex, Makefile, notes.md
│   │   ├── scripts/              # log 把關、PDF 轉圖、決定性的圖片擷取
│   │   └── examples/
│   └── research-gap-analysis/    # 多篇論文 → 研究缺口分析報告
│       ├── SKILL.md
│       ├── templates/            # research-gap-analysis.md, paper-matrix.md, reading-note.md
│       └── examples/
└── workspace-template/       # 複製這個資料夾即可建立新的論文研讀工作區
    ├── AGENTS.md
    ├── papers/  slides/  analysis/
    ├── domain.md                 # 選用：你的研究領域與聽眾（技能會據此調整）
    ├── theme.tex                 # 工作區層級的佈景主題設定：改一次即可套用到所有投影片
    └── beamerthemeSimple.sty     # 內建的預設 Simple Beamer 佈景主題（無 logo）
```

## 可用技能

| 技能 | 適用時機 | 產出 |
|------|----------|------|
| **[paper-beamer-deck](skills/paper-beamer-deck/SKILL.md)** | 想要針對**單一**論文做投影片／摘要／講解 | 在 `slides/<name>/` 下產生一份詳盡、可直接上台的 XeLaTeX Beamer 投影片（含講者備註） |
| **[research-gap-analysis](skills/research-gap-analysis/SKILL.md)** | 想要比較／彙整**多篇**論文並找出研究缺口 | 在 `analysis/<topic>/` 下產生結構化的研究缺口報告、比較矩陣與逐篇閱讀筆記，**並**在 `slides/<topic>-gap-analysis/` 產生一份彙整投影片 |

代理人使用方式：開啟對應的 `SKILL.md` 並照著做。倉庫根目錄的 `AGENTS.md` 負責把任務分流到正確的技能，並說明共用原則。

如果是第一次使用，建議先看：
- [`docs/quickstart.md`](docs/quickstart.md) — 從 PDF 到 reviewed deck 的最短路徑。
- [`docs/prompts.md`](docs/prompts.md) — 常見工作流的 prompt 範本。
- [`docs/copyright.md`](docs/copyright.md) — repository 與 workspace 的 copyright hygiene。

## 安裝與使用

有兩種使用方式，擇一即可。

### 方式 A — 自包含工作區（最簡單）

把 `workspace-template/` 複製成一個新資料夾，並將 `skills/` 目錄一起放進去，讓工作區自帶一份技能、佈景主題與樣板。所有東西都在同一個地方，之後不再依賴本倉庫。

```bash
cp -r workspace-template ../my-topic-workspace
cp -r skills            ../my-topic-workspace/skills
cd ../my-topic-workspace
# 把 PDF 放進 papers/，接著呼叫某個技能（見下方兩個「使用…」段落）
```

在這種版面配置下，從工作區根目錄看，輔助腳本路徑為 `skills/paper-beamer-deck/scripts/…`（投影片的 Makefile 已會透過 `../../skills/…`／`../../../skills/…` 自動找到 `check_latex_log.py`）。適合想要每個專案各有一份可攜、固定版本的情況。

### 方式 B — 外部技能倉庫（共用、可更新）

把本倉庫放在某個固定位置，再由各工作區以路徑或 git submodule 參照它，讓多個工作區共用同一份、可集中更新的技能。

```bash
# 一次性：把技能倉庫 clone 到固定位置
git clone https://github.com/Haouo/paper2beamer-skills ~/tools/paper2beamer-skills

# 每個專案：建立一個指向它的工作區
cp -r ~/tools/paper2beamer-skills/workspace-template ../my-topic-workspace
cd ../my-topic-workspace
ln -s ~/tools/paper2beamer-skills/skills skills      # 或用 git submodule（見下）
```

若專案本身是 git 倉庫，可改用 submodule：

```bash
git submodule add https://github.com/Haouo/paper2beamer-skills .skills-src
ln -s .skills-src/skills skills
```

把代理人指向該工作區，並告訴它技能的位置（例如透過 symlink 的 `skills/`）。適合多個工作區要追蹤同一份技能、並以 `git pull`／`git submodule update` 取得更新的情況。

> 兩種方式中，代理人都是從 `SKILL.md` 讀取技能，並把產出寫進工作區的 `papers/ slides/ analysis/`。技能檔本身是參考資料，不需要「安裝」到任何執行環境中。

## 使用 Beamer 投影片技能

你不需要手動跑編譯——這些由代理人完成。你要做的：

1. 在工作區（見下文）中，把論文放到 `papers/<name>.pdf`。
2. 叫代理人去做（見[範例提示語](#範例提示語)）。可選擇先指定一種**視覺 QA 節奏（cadence）**——技能會在開頭問一次，預設 **risk-targeted**：
   - **one-shot** — 每批都做編譯＋log 把關，最後對整份做一次視覺檢查＋積極修補。最快。
   - **risk-targeted**（預設）— 每批都做編譯＋log 把關，但只對高風險投影片（TikZ、大圖／裁切圖、寬表格、結果圖）做視覺檢查，最後再做一次整份視覺檢查。
   - **incremental** — 每一批都做視覺檢查。最徹底，但視覺 QA 成本約 10 倍。

接著代理人會依照 [`SKILL.md`](skills/paper-beamer-deck/SKILL.md)：閱讀論文、擬大綱、**小批次**撰寫投影片、每批都跑「編譯警告即失敗」的 log 把關（便宜，所有模式皆然）、依你選的 cadence 做視覺 QA，最後一定會做一次**整份投影片的強制視覺檢查**——破版的投影片用拆分／重新設計來修正，而不是把字縮小。
產出會落在 `slides/<paper-short-name>/`（`main.tex`、`notes.md`、`figures/`）。
投影片使用內建的 Simple 佈景主題（`\usetheme{Simple}`），且**需要 XeLaTeX**；樣板的 `Makefile`／`main.tex` 會從工作區根目錄解析佈景主題。

當來源論文是 PDF 時，代理人會先執行決定性的圖片擷取流程：

```bash
python3 skills/paper-beamer-deck/scripts/figure_extraction/extract_figures.py \
  papers/<paper>.pdf --out build/figures/<paper-short-name>
```

這會寫出 `figures.json`、`pages/` 底下的高解析度整頁轉圖、`figures/`
底下的圖片裁切，以及 `previews/index.html` 驗證頁。
投影片產生流程會讀取 `figures.json`，並且只在檢查 preview 後使用
`status: ok` 的紀錄。
如果版面擷取失敗，流程會把整頁轉圖留給人工檢查，並將圖片紀錄標成
`needs_manual_review`，而不是假裝產生了可靠的近似裁切。

<details>
<summary>代理人在幕後實際執行的指令</summary>

```bash
# 建立投影片目錄
mkdir -p slides/<paper-short-name>/figures
cp skills/paper-beamer-deck/templates/{main.tex,Makefile,notes.md} slides/<paper-short-name>/

# 每一批之後（便宜，所有模式）：編譯＋log 把關
cd slides/<paper-short-name>
make                 # xelatex ×2 + 編譯警告即失敗的把關

# 當 cadence 需要時才讀頁面圖片（這是昂貴的步驟）
python3 ../../skills/paper-beamer-deck/scripts/render_pdf_pages.py main.pdf --pages 1-10
```
</details>

輔助腳本：
- `scripts/check_latex_log.py` — 遇到 LaTeX／套件錯誤、缺檔、overfull h/vbox、未定義的參照／引用時，讓編譯失敗。
- `scripts/render_pdf_pages.py` — 透過 `pdftoppm`／`pdftocairo`／ImageMagick 把頁面轉成 PNG（盡力而為；若都未安裝會提示安裝方式）。
- `scripts/figure_extraction/extract_figures.py` — 將 PDF 圖片 metadata／裁切寫入 `figures.json`，轉出整頁圖片，支援 `figure_overrides.json`，並產生 `previews/index.html`。
- `scripts/figure_extraction/verify_figures.py` — 在產生投影片前檢查 `figures.json`、bbox 邊界、crop 檔案與疑似空白裁切。
- `scripts/figure_extraction/select_figures.py` — 依 label 或 manifest index，把 `status: ok` 的圖片複製到 deck 的 `figures/` 目錄。
- `scripts/figure_extraction/schema.md` — 穩定的 `figures.json` schema。
- `scripts/generate_quality_report.py` — 產生 deck 的 `quality_report.md`，彙整 build、視覺 QA、figure 與 open-risk 狀態。
- `scripts/check_deck_sources.py` — 檢查來源追蹤與重用圖表 attribution 的基本要求。
- `scripts/check_visual_qa.py` — 檢查 final visual inspection 的 rendered page 覆蓋。
- `scripts/doctor.py` — 診斷常見工作區依賴與設定問題。
- `scripts/extract_pdf_figures.md` — 手動／除錯用的備援說明。

輔助腳本有回歸測試（不需要 LaTeX／poppler；圖片擷取 smoke test 需要 PyMuPDF）：

```bash
make check
```

## 使用研究缺口分析技能

如同上一節，工作由代理人完成——你的部分是放入論文並提出需求。此技能有兩種輸出模式，請在開頭說明要哪一種（預設 `memo+deck`）：

- **`memo+deck`**（預設）：書面分析**加上**一份彙整投影片。成本較高——還要編譯並視覺檢查一份 LaTeX 投影片（需要 XeLaTeX）。
- **`memo-only`**：只產生 Markdown 報告、比較矩陣與閱讀筆記。成本較低、不用 LaTeX。若你只需要書面分析、或沒有 XeLaTeX，請選這個。

1. 把論文放到 `papers/`。
2. 叫代理人去做（見[範例提示語](#範例提示語)），並說明要哪一種模式。

接著代理人會依照 [`SKILL.md`](skills/research-gap-analysis/SKILL.md)：建立比較矩陣，並**跨論文**彙整（而非逐篇）——明確／隱含／方法／部署／機會型缺口，每一項評為「強／中／弱」，論點要有論文佐證，並標註不確定之處。在 `memo+deck` 模式下，再為整體分析做**一份**彙整投影片（研究地景 → 分類法 → 比較 → 分級缺口 → 研究方向，整個分析只做一份、而非每篇一份），沿用 Beamer 編譯／QA 工具，以及與投影片技能相同的可選視覺 QA cadence。
產出會落在 `analysis/<topic>/`（投影片則在 `slides/<topic>-gap-analysis/`）。

<details>
<summary>代理人在幕後實際執行的指令</summary>

```bash
# 建立分析資料夾
mkdir -p analysis/<topic>/reading-notes analysis/<topic>/figures
cp skills/research-gap-analysis/templates/research-gap-analysis.md analysis/<topic>/
cp skills/research-gap-analysis/templates/paper-matrix.md          analysis/<topic>/
cp skills/research-gap-analysis/templates/reading-note.md          analysis/<topic>/reading-notes/<paper>.md

# memo+deck 模式：建立彙整投影片並編譯（QA cadence 與投影片技能相同）
mkdir -p slides/<topic>-gap-analysis/figures
cp skills/research-gap-analysis/templates/slides-main.tex  slides/<topic>-gap-analysis/main.tex
cp skills/research-gap-analysis/templates/slides-notes.md  slides/<topic>-gap-analysis/notes.md
cp skills/paper-beamer-deck/templates/Makefile             slides/<topic>-gap-analysis/
cd slides/<topic>-gap-analysis && make
```
</details>

關於在複製出來的工作區內如何使用這些技能，請參考 [`workspace-template/AGENTS.md`](workspace-template/AGENTS.md)；兩種接法請見上方的[安裝與使用](#安裝與使用)。

## 範例提示語

**單篇論文 Beamer 投影片**
- 「閱讀 `papers/foo.pdf` 並做一份詳盡的 Beamer 投影片。」
- 「為研討會做一份能講解這篇論文、可直接上台的投影片。」
- 「用投影片加講者備註，摘要並教學論文 X。」

**多篇論文研究缺口分析**
- 「分析這些論文並找出研究缺口。」
- 「比較 A、B、C 三篇論文，告訴我缺了什麼。」
- 「這個領域已經做了什麼、還有什麼沒解決？請建議研究方向。」

## 適用於任何領域

這些技能**不限研究領域**——其工作流程（理解 → 擬大綱 → 報告，以及比較 → 彙整 → 找缺口）適用於任何以實證或方法為主的研究，不只是資訊科學。若要把背景深度、術語以及「如何判斷證據」調整成你的領域，請填寫每個工作區的 `domain.md`（你的領域、聽眾、預設背景、關鍵術語）。若維持空白，技能就保持中立，並假設聽眾為各篇論文所屬領域的一般研究生。`skills/*/examples/` 下的範例使用計算機架構主題，純粹只是示意。

## 佈景主題

投影片預設使用內建的 **Simple** 主題，但主題是一個可替換、工作區層級的單一設定。每個工作區根目錄都有一個 `theme.tex`，所有投影片都會載入它；改一次即可套用到所有投影片（若該檔不存在，投影片會回退到 Simple）。三種做法：

1. **任何已安裝的 Beamer 主題** — 在 `theme.tex` 改用例如 `\usetheme{metropolis}` 或 `\usetheme{Madrid}`（需已安裝於你的 TeX 發行版）。
2. **你自己的自訂主題** — 把 `beamerthemeMyTheme.sty`（以及它需要的圖檔）放到工作區根目錄，並在 `theme.tex` 設定 `\usetheme{MyTheme}`。投影片的 `Makefile` 已把工作區根目錄加入 `TEXINPUTS`，因此會自動找到該 `.sty`。
3. **微調內建主題** — 在 `theme.tex` 的 `\usetheme{Simple}` 之前設定 `\definecolor{simpleAccent}{RGB}{...}` 來更改強調色。

若只想改單一份投影片，把該投影片 `main.tex` 中的 `\InputIfFileExists{../../theme.tex}{}{...}` 那一行直接換成 `\usetheme{...}`。細節請見 [`workspace-template/AGENTS.md`](workspace-template/AGENTS.md#theming)。

## 環境需求

- **XeLaTeX**（TeX Live 或類似發行版）以編譯 Beamer 投影片。內建的 Simple 主題是自包含的（無 logo／素材），若未安裝 TeX Gyre Heros／Fira Mono 會回退到預設字型。要使用自己的主題請見[佈景主題](#佈景主題)。
- **Python 3**，給輔助腳本使用（僅用標準函式庫）。
- **PyMuPDF**（`python3 -m pip install pymupdf`），用於決定性的來源 PDF 圖片擷取。
- 轉成 PDF 頁面圖片時可選用：`poppler-utils`（`pdftoppm`／`pdftocairo`）或 ImageMagick + Ghostscript。
- 版面感知圖片偵測建議使用：`docling`。
  第一次使用可能會下載 Docling 模型 artifacts；掃描型 PDF 若加上 `--docling-ocr`，也可能需要 OCR 模型 artifacts。
  若機器離線，請先在有網路時跑一次 warm-cache conversion，或讓 Docling 指向已準備好的 artifacts cache。
- 版面感知圖片偵測的舊式選用備援：`pdffigures2`。

為什麼不只擷取 PDF 內嵌圖片？
許多學術論文圖片其實是向量圖、折線圖，或由多個 PDF 物件組成的複合圖。
直接擷取內嵌圖片可能漏掉它們、把同一張圖切成多塊，或遺漏向量標籤與座標軸。
因此圖片流程採用版面 metadata 加上高解析度整頁轉圖後裁切，讓向量與混合型圖片能保留論文中的實際外觀。

手動 bbox 覆寫使用 `figure_overrides.json`：

```json
[
  {
    "label": "Figure 3",
    "page": 5,
    "bbox": [72, 120, 520, 430],
    "caption": "Manually corrected Figure 3"
  }
]
```

把它放在目前目錄或輸出目錄，或用 `--overrides path/to/figure_overrides.json`
指定，接著重新執行擷取器。
擷取器也會寫出 `figure_overrides.example.json`，附上頁面尺寸與 placeholder bbox，方便人工修正。

常用圖片指令：

```bash
# 過濾過小或類型不需要的 layout 偵測。
python3 skills/paper-beamer-deck/scripts/figure_extraction/extract_figures.py \
  papers/foo.pdf --out build/figures/foo --type picture,chart,table --min-area-ratio 0.01

# 在投影片使用前驗證 manifest 與 crop。
python3 skills/paper-beamer-deck/scripts/figure_extraction/verify_figures.py \
  build/figures/foo/figures.json

# 把選到的圖片複製到 deck。
python3 skills/paper-beamer-deck/scripts/figure_extraction/select_figures.py \
  build/figures/foo/figures.json --labels "Figure 1,Table 2" --copy-to slides/foo/figures
```

Preview HTML 會同時顯示 crop，以及渲染頁面上的紅色 bbox overlay，方便快速抓出錯誤偵測。
接受 deck 前，也可以用輔助腳本產生品質報告並跑輕量檢查：

```bash
python3 skills/paper-beamer-deck/scripts/generate_quality_report.py slides/foo \
  --figures-json build/figures/foo/figures.json
python3 skills/paper-beamer-deck/scripts/check_deck_sources.py slides/foo
python3 skills/paper-beamer-deck/scripts/check_visual_qa.py slides/foo
python3 skills/paper-beamer-deck/scripts/doctor.py .
```

## 環境快速檢測（Smoke test）

花一分鐘確認你的環境能編譯並檢視投影片。請在倉庫根目錄（或含有 `skills/` 目錄的工作區）執行。

**1. XeLaTeX 可用嗎？**

```bash
xelatex --version        # 應印出 "XeTeX 3.x …"；若顯示 "command not found"，請安裝 TeX Live
```

**2. 把關機制是否正常？** 餵 `check_latex_log.py` 一個含已知問題的小 log，確認它會失敗（exit code `1`）；再餵一個乾淨的 log，確認它通過（exit `0`）：

```bash
printf 'Overfull \\hbox (12.0pt too wide) in paragraph at lines 1--2\n' > /tmp/bad.log
python3 skills/paper-beamer-deck/scripts/check_latex_log.py /tmp/bad.log ; echo "exit=$?"   # 失敗，exit=1

printf 'Output written on main.pdf (3 pages).\n' > /tmp/ok.log
python3 skills/paper-beamer-deck/scripts/check_latex_log.py /tmp/ok.log  ; echo "exit=$?"   # 通過，exit=0
```

**3. 能把 PDF 轉成頁面圖片嗎？** 僅在你已有編譯好的 `main.pdf`（例如在某個投影片目錄 `make` 之後）時：

```bash
python3 skills/paper-beamer-deck/scripts/render_pdf_pages.py main.pdf --pages 1-3 --out _preview
# 會輸出 _preview/main-page-*.png；打開來檢視投影片。
# 若未安裝任何 PDF 工具，它會印出安裝提示並以非零碼結束（不會丟出 traceback）。
```

**4. 能執行圖片擷取的備援模式嗎？** 僅在你已安裝 PyMuPDF 且有任一有效論文 PDF 時：

```bash
python3 skills/paper-beamer-deck/scripts/figure_extraction/extract_figures.py \
  papers/foo.pdf --out build/figures/foo
# 預設 backend 是 --backend auto：先 Docling，再 pdffigures2。
# 若沒有 layout backend 成功，預期會產生 pages/page_*.png、figures.json、
# previews/index.html，以及 needs_manual_review 紀錄／操作說明。
```

回歸測試使用程式產生的 synthetic PDF fixture，不提交任何複製自真實論文的內容。
可用 `PAPER_BEAMER_RUN_DOCLING_SMOKE=1` 開啟選用的 live Docling smoke test；在 hermetic CI 請保持關閉。
本倉庫也包含 GitHub Actions 測試／compile check workflow、`CHANGELOG.md`，
以及只使用 synthetic 範例的 `skills/paper-beamer-deck/examples/gallery.md`。

Repository hygiene checks 會擋掉 tracked paper PDFs / binary assets 和壞掉的本地 Markdown 連結：

```bash
make hygiene
```

**5.（選用）完整樣板編譯。** 把投影片樣板複製到工作區並編譯：

```bash
cp -r workspace-template /tmp/ws && cp -r skills /tmp/ws/skills
mkdir -p /tmp/ws/slides/demo/figures
cp skills/paper-beamer-deck/templates/{main.tex,Makefile} /tmp/ws/slides/demo/
( cd /tmp/ws/slides/demo && make )   # 應產生 "main.pdf" 並通過把關
```

## 授權

MIT License。請見 [`LICENSE`](LICENSE)。
