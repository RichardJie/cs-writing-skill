# Discipline-Specific Academic Slide Grammar: Biomedical, Economics/Social Sciences & Humanities (`disciplines-biomed-econ-humanities.md`)

> **Module Role**: Non-CS/EE scholarly discipline playbook (`Biomedical, Clinical Medicine, Neuroscience, Bioinformatics, Chemistry, Economics, Finance, Management, Computational Social Science, Humanities, Law, History, Education, Qualitative Research`) for [`cs-report-ppt`](../SKILL.md). Works alongside [`marginal_annotations.md`](marginal_annotations.md), [`omml_syntax_guide.md`](omml_syntax_guide.md), [`languages-and-typography.md`](languages-and-typography.md), and [`palettes-and-layouts.md`](palettes-and-layouts.md).

This reference specification extends the universal academic presentation engine (`cs-report-ppt`) beyond Computer Science and Electrical Engineering into three major scholarly super-clusters:

1. **Cluster I — Biomedical, Clinical Medicine, Neuroscience, Bioinformatics & Chemistry** (*Cell*, *Nature*, *Science*, *NEJM*, *The Lancet*, *JAMA*, *Nature Neuroscience*, *Bioinformatics*, *JACS*, *Angewandte Chemie*).
2. **Cluster II — Economics, Finance, Management & Computational Social Science** (*AER*, *QJE*, *Econometrica*, *JPE*, *JF*, *RFS*, *AMJ*, *SMJ*, *ASR*, *Management Science*, NBER / AEA / AFA / AOM / 国内经管顶刊如《经济研究》《管理世界》).
3. **Cluster III — Humanities, Law, History, Education & Qualitative Research** (*AHR*, *Past & Present*, *Harvard Law Review*, *AERA / Review of Educational Research*, qualitative sociology/anthropology, 国内人文法史教顶刊如《历史研究》《中国社会科学》《法学研究》《教育研究》).

Every rule in this module integrates directly with the core invariants of `cs-report-ppt`:
- **16:9 Widescreen Canvas**: $13.333'' \times 7.500''$ (`usable content zone`: $X = 0.600'', Y = 1.650'', W = 12.133'', H = 5.200''$).
- **Figure & Evidence Dominance ($\ge 80\%$ Visual/Structured Asset Coverage)**: Every discipline replaces prose walls with its native evidentiary artifacts—microscopy panels, Kaplan-Meier survival curves, event-study coefficient plots, focal 5-row econometric tables, archival facsimiles, or Gioia coding structures.
- **Native Vector OMML Math (`latex_to_omml.py`)**: Hazard ratios, Cox proportional-hazards models, differential expression thresholds, TWFE/IV/RDD econometric specifications, chemical kinetics, and standardized effect sizes render as crisp OpenXML `<m:oMath>` / `<m:oMathPara>` objects.
- **High-DPI Asset Harvesting (`crop_figures.py`, $\ge 300\text{ DPI}$) & Pure Vision-in-the-Loop QA (`view_file`, $\ge 150\text{ DPI}$)**: No slide ships until visually audited for text collisions, scale-bar legibility, regression-table readability, and aspect-ratio lock.

---

## 0. Cross-Disciplinary Detection & Adaptation Routing Matrix

When ingesting a manuscript PDF, working paper, monograph chapter, or slide brief, inspect its venue, section headers, statistical conventions, and visual assets to route automatically to the right disciplinary grammar:

| Disciplinary Sub-Track | Diagnostic Signals in Source PDF | Default Palette Preset | Recommended Spine Track | Primary Visual Evidence Unit | Primary Failure Mode to Prevent |
|:---|:---|:---|:---|:---|:---|
| **1A. Wet-Lab Biology, Neuro & Bioinformatics** | *Methods* at end or STAR Methods; Western blots, IF/IHC, scRNA-seq UMAP, volcano plots, fMRI MNI maps | `nature_slate_teal` or `academic_mono` | **Track 1A** (14-Slide Translational Bio Spine) | Cropped sub-panels (`Fig. 2b–c`) + scale bar + SuperPlot quantification | Pasting an entire 9-panel *Cell*/*Nature* composite figure onto one slide |
| **1B. Clinical Medicine & Epidemiology** | PICO, NCT trial ID, CONSORT/PRISMA, Table 1 baseline demographics, Kaplan-Meier, Cox HR, CTCAE safety | `oxford_navy` or `nature_slate_teal` | **Track 1B** (14-Slide Clinical Trial Spine) | 4-stage CONSORT flow + KM curve with aligned `Number at Risk` table + Forest plot | KM curve missing `At-Risk` table; unreadable 22-box raw CONSORT dump |
| **1C. Synthetic, Medicinal & Materials Chemistry** | Reaction arrows, `mol%`, `ee`/`dr`, NMR/HRMS, substrate scope (`3a–3z`), catalytic cycle, DFT $\Delta G^\ddagger$ | `academic_mono` or `oxford_navy` | **Track 1C** (14-Slide Chemical Synthesis Spine) | Vector reaction scheme + curated 8-substrate grid + clockwise catalytic cycle | Dumping a 36-compound SI scope table or blurry rasterized ChemDraw structures |
| **2A. Economics, Finance & Public Policy** | Identification strategy, TWFE, DID, IV/2SLS, RDD, Stata/R `reghdfe` tables, `(SE)` clustered, NBER style | `oxford_navy` or `academic_mono` | **Track 2A** (14-Slide Applied Micro / Finance Spine) | Causal DAG + Event-study / RDD binscatter + 5-row focal regression table with FE `✓` | Pasting a 40-row $\times$ 9-col Stata `estout` LaTeX table screenshot at `6pt` font |
| **2B. Management, OB/Strategy & CSS** | Hypotheses `H1–H4`, SEM path model, moderation `±1 SD` slopes, text-as-data / network / field experiment | `oxford_navy` or `cvpr_clean_blue` | **Track 2B** (14-Slide Behavioral / Strategy Spine) | Construct path diagram + Simple Slopes interaction plot + coefficient forest plot | Cluttered SEM diagram full of $\varepsilon_i$ error ovals and unreadable fit indices |
| **3A. History, Literature & Philosophy** | Footnote citations, archival fond/folio numbers, classical/foreign primary excerpts, periodization | `mit_crimson_neutral` or `academic_mono` | **Track 3A** (14-Slide Archival Humanities Spine) | High-DPI archival facsimile + bilingual close-reading callout ($\le 45$ words) | 250-word single-spaced block quotes read aloud verbatim by the presenter |
| **3B. Law & Comparative Legal Studies** | Statutory sections (`§`), judicial splits, constitutional clauses, comparative jurisdictions, doctrinal tests | `oxford_navy` or `academic_mono` | **Track 3B** (14-Slide Doctrinal & Empirical Law Spine) | Statutory text close-reading highlight box + Comparative Jurisdiction Matrix | Copying full statutory subsections without isolating operative ambiguous triggers |
| **3C. Qualitative Research & Education** | Interviews ($N$), ethnography, Gioia /扎根理论三级编码, pre-post classroom intervention, Cohen's $d$ | `oxford_navy` or `nature_slate_teal` | **Track 3C** (14-Slide Qualitative / Mixed-Methods Spine) | 3-tier Gioia coding flow + Conceptual $2 \times 2$ matrix + Raincloud / `Cohen's d` card | Screenshot of raw NVivo node tree or 35-row manuscript coding table |

---

# Part I: Biomedical, Clinical Medicine, Neuroscience, Bioinformatics & Chemistry

## 1.1 Slide-by-Slide Spines (14-Slide Standard)

### Track 1A: Wet-Lab Biology, Neuroscience & Bioinformatics Spine (*Nature* / *Cell* / *Science* Paradigm)

| Slide # | Category Badge | Standard Slide Title Pattern | Layout Model | Harvested / Constructed Visual Asset | Mandatory Empirical & Statistical Elements | Marginal Callout |
|:---|:---|:---|:---|:---|:---|:---|
| **1** | `PAPER OVERVIEW` | `[Full Paper Title + Graphical Abstract Hero]` | `split_equal_2col` | **Graphical Abstract** (or `Fig. 1a` schematic) | Authors, journal/year, DOI, model organism/cohort badge, 1-sentence central biological discovery. | None |
| **2** | `PATHOPHYSIOLOGICAL CONTEXT` | `[Disease Burden / Unresolved Biological Mystery]` | `split_65_35` | **Pathway / Anatomical Context Diagram** | Clinical prevalence or biological paradox; why prior canonical pathway models fail to explain phenotype. | `[Translational Relevance]` |
| **3** | `EXPERIMENTAL PARADIGM` | `[Model System, Cohort & Multi-Modal Assay Pipeline]` | `hero_1col` | **Wet-Lab / Multi-Omics Workflow Schematic** | Mouse line (`Cre-LoxP` genotype), cell line, or patient biobank ($N$); timepoints; sequencing/imaging modalities. | None |
| **4** | `PRIMARY PHENOTYPE` | `[Core Phenotypic Discovery in Vivo / Patient Tissue]` | `split_65_35` | **Cropped Microscopy / fMRI / Histology (`Fig. 1b–d`)** | Mandatory physical scale bar (`µm`), channel labels, paired dot-bar quantification ($n$ biological replicates, exact $p$). | `[Assay Reproducibility]` |
| **5** | `CELLULAR LANDSCAPE` | `[Single-Cell / Spatial / Circuit Atlas Resolution]` | `split_equal_2col` | **UMAP / Spatial Transcriptomics / Brain Parcellation** | Total cells/nuclei ($N$) post-QC, condition split (Control vs Disease), locked cell-type palette, proportion shift $\Delta\%$. | None |
| **6** | `MOLECULAR SIGNATURE` | `[Differential Expression & Enriched Pathways]` | `split_equal_2col` | **Volcano Plot (Left) + Top-8 GO/GSEA Bar Plot (Right)** | Thresholds ($|\log_2\text{FC}| > 1.0, \text{FDR} < 0.05$), top 8–10 italicized gene callouts, normalized enrichment score (NES). | None |
| **7** | `CANDIDATE TARGET` | `[Identification of Master Regulator / Receptor / Circuit]` | `split_65_35` | **Clustered Marker Heatmap / ChIP-seq Track / Blot** | Z-score colorbar, loading control (`GAPDH`/`β-actin`) + kDa markers, binding motif or structural domain callout. | `[Mechanistic Target]` |
| **8** | `LOSS-OF-FUNCTION PROOF` | `[Genetic Knockout / Knockdown / Optogenetic Inhibition]` | `split_equal_2col` | **WT vs KO/shRNA Paired Assay (`Fig. 3a–c`)** | Knockout validation blot/qPCR + phenotypic abolition; individual replicate points + two-sided test statistic. | None |
| **9** | `GAIN-OF-FUNCTION & RESCUE` | `[Overexpression / Add-Back Rescue Confirms Sufficiency]` | `split_equal_2col` | **WT vs KO vs KO+Rescue 3-Group Comparison (`Fig. 4`)** | Catalytic-dead mutant control (if enzymatic) vs wild-type rescue; statistical bracket across all 3 arms (`****p < 0.0001`). | None |
| **10** | `STRUCTURAL / CIRCUIT MECHANISM` | `[Downstream Signaling Cascade / Neural Circuit Dynamics]` | `split_65_35` | **Co-IP / Cryo-EM / Calcium Imaging / fMRI Connectivity** | Direct physical interaction ($K_d$ in nM via SPR/ITC) or MNI peak coordinates `(x, y, z)` + cluster FWE $p$-value. | `[Mechanistic Interpretability]` |
| **11** | `PRECLINICAL THERAPEUTIC TEST` | `[Pharmacological Inhibition / In Vivo Efficacy]` | `split_equal_2col` | **Dose-Response ($\text{IC}_{50}$) + Tumor/Symptom Curve** | Dosing regimen (`mg/kg`, route, schedule), body-weight toxicity check, survival or behavioral recovery delta. | None |
| **12** | `HUMAN CLINICAL TRANSLATION` | `[Validation in Independent Patient Cohorts]` | `split_65_35` | **Patient IHC + TCGA/Clinical Kaplan-Meier Curve** | Independent human cohort ($N$), Hazard Ratio (`HR [95% CI]`), Log-rank $p$-value, `Number at Risk` table underneath. | `[Clinical Translation]` |
| **13** | `WORKING MODEL & CRITIQUE` | `[Integrated Biological Model vs Methodological Caveats]` | `split_equal_2col` | **Left: Clean Working Mechanism Diagram; Right: Critique** | Left: `WT` vs `Treated` state diagram. Right: Mouse-to-human gap, off-target risks, sample size or sex-bias limits. | None |
| **14** | `DISCUSSION & LAB SYNERGY` | `[Open Questions & Immediate Experimental Roadmap]` | `split_65_35` | **3 Follow-Up Questions + 3-Phase Wet/Dry Lab Plan** | Concrete reagent/dataset transfer (`GEO GSE...`, plasmid/antibody ID) and 4-week validation milestones. | `[Own Lab Synergy]` |

---

### Track 1B: Clinical Trial & Epidemiology Spine (*NEJM* / *Lancet* / *JAMA* Paradigm)

| Slide # | Category Badge | Slide Focus | Layout Model | Mandatory Visual / Table Specification |
|:---|:---|:---|:---|:---|
| **1** | `TRIAL OVERVIEW` | Title, Acronym, Registry (`NCT#`), Funding | `hero_1col` | Trial acronym badge, Phase II/III design tag, multi-center site count, simultaneous NEJM/Lancet DOI. |
| **2** | `CLINICAL RATIONALE` | Standard-of-Care Failure & Unmet Need | `split_65_35` | Historical 5-year survival / relapse rate chart + biological rationale for investigational agent. |
| **3** | `PICO & STUDY DESIGN` | Randomization, Blinding & Endpoints | `hero_1col` | **Trial Schema Timeline**: Screening $\rightarrow$ Stratification factors $\rightarrow$ `1:1` Randomization arms (dose/schedule) $\rightarrow$ Primary & Key Secondary Endpoints. |
| **4** | `PATIENT DISPOSITION` | **Simplified 4-Stage CONSORT Flowchart** | `hero_1col` | Native vector 4-row flow: `Assessed (n)` $\rightarrow$ `Randomized (n)` $\rightarrow$ `Received Intervention (n)` $\rightarrow$ `ITT / Per-Protocol Analyzed (n)` + attrition reasons. |
| **5** | `BASELINE CHARACTERISTICS` | **Condensed Table 1 (6–8 Key Rows)** | `split_65_35` | Age, Sex, ECOG/severity score, key biomarker strata (`PD-L1 ≥ 50%`) across Arms; prove randomization balance (no $p$-values on RCT Table 1 per NEJM rule). |
| **6** | `STATISTICAL HIERARCHY` | Alpha-Spending, Power & Estimand | `split_equal_2col` | Target HR, required events, interim O'Brien-Fleming boundaries, hierarchical gatekeeping sequence for multiplicity control. |
| **7** | `PRIMARY ENDPOINT` | **Kaplan-Meier Survival Curve + Risk Table** | `split_65_35` | Step curve with censor ticks, median PFS/OS (`months`), stratified `HR (95% CI)`, two-sided Log-rank $p$, aligned `No. at Risk` table at bottom. |
| **8** | `KEY SECONDARY ENDPOINT` | Overall Survival / ORR Waterfall / Landmark | `split_equal_2col` | 12/24-month landmark rates, RECIST waterfall or swimmer plot with CR/PR/SD/PD color coding. |
| **9** | `PRESPECIFIED SUBGROUPS` | **Subgroup Forest Plot** | `hero_1col` | Point-estimate squares scaled to $n$, 95% CI whiskers, vertical `HR = 1.0` null line, right-aligned `HR (95% CI)` + $P_{\text{interaction}}$. |
| **10** | `PATIENT-REPORTED OUTCOMES`| QoL / Time-to-Deterioration (PROs) | `split_equal_2col` | Longitudinal EORTC QLQ-C30 / EQ-5D mixed-model mean change (`±95% CI`) with clinically meaningful threshold dashed line. |
| **11** | `SAFETY & TOLERABILITY` | **Treatment-Emergent Adverse Events (TEAEs)** | `split_65_35` | Tornado / Diverging bar chart comparing All-Grade vs **Grade $\ge 3$** AEs, dose reductions (`%`), and treatment-related discontinuations (`%`). |
| **12** | `BIOMARKER EXPLORATION` | ctDNA Clearance / Exploratory Correlates | `split_equal_2col` | Post-hoc vs prespecified badge clearly marked; biomarker-positive vs negative stratified response curves. |
| **13** | `INTERNAL & EXTERNAL VALIDITY`| Trial Strengths vs Limitations | `split_equal_2col` | Crossover confounding on OS, open-label bias vs blinded independent central review (BICR), underrepresented demographic generalizability. |
| **14** | `CLINICAL PRACTICE IMPACT` | Guideline Positioning & Next Trials | `split_65_35` | Where the regimen slots into NCCN/ESMO/AHA first-line vs second-line treatment algorithms. |

---

### Track 1C: Synthetic, Medicinal & Materials Chemistry Spine (*JACS* / *Angewandte* Paradigm)

1. **Slide 1 (`TRANSFORMATION HERO`)**: Single crisp vector reaction scheme: `Reactant A + Reactant B ──[Cat. / Conditions]──> Product C` with newly formed bond highlighted in **Crimson (`#DC2626`)** + 3 key metrics (`up to 96% yield`, `>20:1 dr`, `99% ee`).
2. **Slide 2 (`SYNTHETIC BOTTLENECK`)**: Classical 5-step toxic/protecting-group route vs proposed 1-step C–H / catalytic disconnection; bioactive natural products/drugs containing the target scaffold.
3. **Slide 3 (`DESIGN HYPOTHESIS`)**: Steric/electronic challenge (e.g., $\beta$-hydride elimination competing with reductive elimination) + ligand design rationale.
4. **Slide 4 (`REACTION OPTIMIZATION`)**: **6-Entry Optimization Table** (never 25 entries!): `Entry 1: Standard conditions (88% yield, 94% ee)` at top, followed by 5 deviation entries (`w/o Ligand L1 -> 12%`, `Ligand L2 -> 45%`, `Solvent THF -> 61%`, `RT instead of 60 °C -> 34%`, `Air atmosphere -> 79%`).
5. **Slide 5 (`SUBSTRATE SCOPE I — ARYL / ELECTRONIC`)**: **$2 \times 4$ Curated Structure Grid** (`grid_4col` split vertically): isolated yields (`%`) and `ee`/`dr` beneath each structure, grouped into Electron-Donating (`-OMe`, `-Me`), Electron-Withdrawing (`-CF3`, `-CN`), Sterically Hindered (`ortho-iPr`), and Heterocycles (`pyridine`, `indole`).
6. **Slide 6 (`SUBSTRATE SCOPE II — COMPLEX & LIMITATIONS`)**: **Late-Stage Functionalization** of drug molecules (e.g., Celecoxib, Estrone derivatives) + dedicated **Unsuccessful / Low-Yield Substrates Box** (`<5%` or `N.R.`) explaining *why* (e.g., strongly coordinating free primary amine poisons Pd catalyst).
7. **Slide 7 (`SYNTHETIC UTILITY`)**: `10 mmol` gram-scale reaction (`1.84 g, 85% yield`) + 3–4 divergent downstream derivatizations preserving enantiopurity (`99% -> 98% ee`).
8. **Slide 8 (`MECHANISTIC CONTROLS`)**: Radical clock / TEMPO trapping experiment + Deuterium labeling / Kinetic Isotope Effect (`KIE: k_H / k_D = 3.4`, indicating C–H cleavage is turnover-limiting).
9. **Slide 9 (`INTERMEDIATE ISOLATION`)**: X-ray crystal structure (ORTEP thermal ellipsoid at 50% probability, selected bond lengths in `Å`) or operando NMR/IR kinetic profile.
10. **Slide 10 (`PROPOSED CATALYTIC CYCLE`)**: Clockwise native/high-DPI catalytic cycle with explicit metal oxidation states (`Ni(0)` $\rightarrow$ `Ni(II)` $\rightarrow$ `Ni(III)` $\rightarrow$ `Ni(I)`), off-cycle resting state, and stereodetermining transition state `[TS-1]‡` quadrant model.
11. **Slide 11 (`DFT FREE ENERGY PROFILE`)**: Reaction coordinate diagram ($\Delta G$ in `kcal/mol`, `0.0` reference) comparing favored $(R)$-pathway vs disfavored $(S)$-pathway ($\Delta\Delta G^\ddagger = 2.4\text{ kcal/mol} \approx 96\%\text{ ee}$).
12. **Slide 12 (`BENCHMARKING VS PRIOR ART`)**: Comparison matrix across catalyst loading (`mol%`), functional group tolerance, temperature, and Green Chemistry E-factor / atom economy.
13. **Slide 13 (`CRITICAL ASSESSMENT`)**: Scope blindspots (e.g., unactivated alkyl chlorides, air-sensitive glovebox requirement, precious metal cost) vs mechanistic rigor.
14. **Slide 14 (`LAB SYNERGY & NEXT TARGETS`)**: Direct application to in-house total synthesis / medicinal SAR campaign.

---

## 1.2 Biomedical & Chemical Visual Asset Surgery Rules

### Rule B1: Multi-Panel *Nature* / *Cell* Figure Deconstruction (Zero Composite Dump Rule)
Manuscript figures in *Cell*, *Nature*, and *Science* pack 8 to 14 panels (`Fig. 2a–l`) onto a portrait page ($7.2'' \times 9.5''$). **Never embed a full multi-panel figure raw onto a 16:9 slide.** Apply one of three deterministic surgeries:

1. **Sub-Panel PyMuPDF Crop & Re-Pairing (Preferred)**:
   - Use `crop_figures.py` at `350 DPI` to slice individual panels (`Fig. 2a` assay schematic, `Fig. 2b` microscopy image, `Fig. 2c` bar-dot quantification).
   - Re-compose horizontally on the 16:9 canvas: e.g., `Fig. 2a` across a top banner (`x=0.60", y=1.65", w=12.13", h=1.40"`), `Fig. 2b` bottom-left (`x=0.60", y=3.25", w=5.92", h=3.60"`), and `Fig. 2c` bottom-right (`x=6.82", y=3.25", w=5.92", h=3.60"`).
   - Keep original panel letter badges (`a`, `b`, `c`) intact or add crisp `12pt Bold` corner pills (`Fig. 2b`) so audience cross-referencing to the paper stays exact.
2. **Spotlight Mask Overlay (When Spatial Adjacency Matters)**:
   - If panels must stay in their native composite arrangement, cover non-focal panels with a semi-transparent white/slate mask (`#FFFFFF` at `65%` opacity or `#0F172A` at `55%` opacity, `no border`) and frame the active panel with a `2.0pt` solid accent border (`#0D9488` or `#DC2626`).
3. **Sequential Slide Splitting**:
   - Allocate max **2–3 related sub-panels per slide**. Split a 9-panel figure across 3 consecutive narrative slides (e.g., *Phenotype* $\rightarrow$ *Loss-of-Function* $\rightarrow$ *Rescue*).

### Rule B2: Microscopy, Western Blot & Statistical Quantification Integrity

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Slide 8: Loss of TREM2 Abolishes Microglial Lipid Clearance in Vivo          │
├──────────────────────────────────────┬───────────────────────────────────────┤
│  CARD 0: Confocal IF + Western Blot  │  CARD 1: Biological Replicate Quant.  │
│  (x=0.60", y=1.65", w=5.916", h=5.20")│  (x=6.816", y=1.65", w=5.916", h=5.20")│
│  ┌───────────────┐ ┌───────────────┐ │                                       │
│  │ WT Cortex     │ │ Trem2-/-      │ │   Lipid Droplet Area / IBA1+ Cell (%) │
│  │ IBA1 / BODIPY │ │ IBA1 / BODIPY │ │     40 ┤         ┌──── **** ────┐     │
│  │         [20µm]│ │         [20µm]│ │     30 ┤         │  p = 0.00004 │     │
│  └───────────────┘ └───────────────┘ │     20 ┤         │       ● ●    │     │
│  Western Blot (Sorted Microglia):    │     10 ┤   ● ●   │     ┌─────┐  │     │
│  TREM2   [====]    [    ]  ← 28 kDa  │      0 ┼──┌───┐──┴─────┤  ●  ├──┴──   │
│  p-SYK   [====]    [ .  ]  ← 72 kDa  │           │ ● │        └─────┘        │
│  GAPDH   [====]    [====]  ← 37 kDa  │            WT          Trem2-/-       │
│                                      │   • n = 6 mice/group (Mean ± SD)      │
│                                      │   • Two-tailed unpaired t-test        │
└──────────────────────────────────────┴───────────────────────────────────────┘
```

1. **Microscopy Scale Bars (Mandatory)**:
   - Never crop off the original scale bar. If the embedded scale-bar label inside the paper figure drops below `9pt` equivalent when scaled onto the slide, overlay a crisp vector scale bar in the bottom-right corner of the micrograph: solid rectangle (`h = 0.045"`, white `#FFFFFF` on dark fluorescence or `#000000` on brightfield H&E/IHC) with a `11–12pt Bold` label (`50 µm`) on a subtle `50%`-opacity contrast backing pill.
   - **Ban bare magnification strings** (`"400×"` or `"20× objective"`) without a physical micron/nanometer bar, because slide projection rescales physical dimensions.
   - **Colorblind-Safe Channels**: Annotate every fluorescence channel explicitly above or inside the panel in matching colored bold text (`DAPI` `#3B82F6` | `IBA1 (Magenta)` `#EC4899` | `BODIPY (Green)` `#22C55E`). Never rely on unannotated red-green merges alone.
2. **Western Blot Integrity**:
   - Always include **Target Protein name** on the left, **Molecular Weight (`kDa`)** on the right, and a matched **Loading Control** (`GAPDH`, `β-actin`, `α-tubulin`, `Vinculin`, or `Ponceau/Total Protein`) aligned lane-for-lane directly below.
   - If non-contiguous lanes were spliced in the source paper, preserve visible thin splice hairlines (`1pt` black/white gap) — never mask splices seamlessly.
   - Always pair qualitative blots with quantitative densitometry (`n ≥ 3` independent biological replicates) or state replication count explicitly (`Representative of n = 3 independent experiments`).
3. **Statistical Signifiers & Ban on Naked Bar Plots**:
   - When generating native charts from paper summary tables or supplementary source data, prefer **Dot-over-Bar / Box-Dot / SuperPlots** over plain solid bars wherever individual data points exist.
   - Always state **4 statistical metadata items** in the card caption or footer (`11–12pt`): (a) definition of $n$ (`n = 8 mice/group`, never ambiguous technical vs biological replicates), (b) center & dispersion (`Mean ± SD`, `Mean ± SEM`, or `Median [IQR]`), (c) exact statistical test (`Two-way ANOVA with Tukey post-hoc` / `Two-sided Mann-Whitney U`), and (d) exact $p$-value (`p = 0.0034`) alongside standard star tiers (`*p < 0.05`, `**p < 0.01`, `***p < 0.001`, `****p < 0.0001`, `ns: p ≥ 0.05`).

### Rule B3: Kaplan-Meier Curves, CONSORT Diagrams & Forest Plots

1. **Simplified 4-Stage Slide CONSORT Flowchart (`hero_1col`: $W = 12.133'', H = 5.200''$)**:
   - Manuscript CONSORT diagrams often contain 18–25 dense text boxes with `7pt` exclusion lists. Rebuild as a native 4-tier DrawingML flowchart (`12–13pt` font):
     - **Tier 1 (`Y = 1.85", H = 0.75"`)**: Centered `Enrollment` box (`Assessed for eligibility: N = 1,240`) with right-branch exclusion callout (`Excluded: n = 380 • Did not meet criteria: 290 • Declined: 90`).
     - **Tier 2 (`Y = 2.85", H = 0.65"`)**: Highlighted `Randomized (N = 860, 1:1 stratified)` pill.
     - **Tier 3 (`Y = 3.75", H = 1.25"`)**: Split left (`Experimental Arm: n = 430; Received treatment: 426; Discontinued: 41 [AE: 18, Progression: 23]`) and right (`Control Arm: n = 430; Received treatment: 422; Discontinued: 64 [AE: 14, Progression: 50]`).
     - **Tier 4 (`Y = 5.25", H = 1.25"`)**: Bold bordered `Primary ITT Analysis` boxes (`Analyzed: n = 430 [100% ITT]; Per-protocol: n = 389` vs `Analyzed: n = 430 [100% ITT]; Per-protocol: n = 358`).
2. **Kaplan-Meier Survival Curve Anatomy**:
   - **Never crop off the `Number at Risk` table** beneath a harvested KM plot! When harvesting from NEJM/Lancet/JCO PDFs with `crop_figures.py`, expand the bounding box vertically to capture the X-axis label **plus** all rows of `No. at risk`.
   - Overlay or verify a clean floating callout badge (`13pt Bold`) inside the upper-right open quadrant of the plot:
     - `Median PFS: 14.8 vs 8.2 mo`
     - `Stratified HR = 0.58 (95% CI, 0.46–0.73)`
     - `Two-sided Log-rank P < 0.0001`

### Rule B4: Bioinformatics Omics & Neuroimaging Standards
- **Gene & Protein Nomenclature Discipline** (strictly enforced in titles & bullets):
  - **Human gene / mRNA**: *ALL CAPS ITALICS* (`*BRCA1*`, `*TREM2*`, `*TP53*`); **Human protein**: ALL CAPS ROMAN (`BRCA1`, `TREM2`, `p53`).
  - **Mouse/Rat gene / mRNA**: *Sentence-case italics* (`*Brca1*`, `*Trem2*`, `*Trp53*`); **Mouse/Rat protein**: ALL CAPS ROMAN (`BRCA1`, `TREM2`).
- **Volcano & Heatmap Hygiene**:
  - Volcano plots must label at most **8–12 focal genes** using non-overlapping leader lines (`ggrepel` style); never display 60 overlapping gene strings.
  - Heatmaps must display **functional module brackets** (e.g., *Interferon-Stimulated Genes*, *Oxidative Phosphorylation*) rather than 400 microscopic row labels.
- **Neuroimaging (fMRI / PET / EEG)**:
  - Every brain slice card must state orientation (`Radiological: R on L` or `Neurological: L on L`), anatomical template (`MNI152`), peak coordinate `(x, y, z mm)`, statistic colorbar (`t` or `z`), and multiple-comparison correction (`Cluster-level p_FWE < 0.05` or `TFCE`).

---

## 1.3 Biomedical Native OMML Formula Templates

Inject via `{{MATH_DISPLAY:...}}` / `latex_to_omml.py`:

1. **Cox Proportional Hazards Model**:
   ```latex
   h(t \mid \mathbf{X}_i) = h_0(t) \exp\left( \beta_1 \text{Arm}_i + \boldsymbol{\gamma}^\top \mathbf{Z}_i \right), \quad \text{HR} = \exp(\hat{\beta}_1) = 0.58 \; [0.46, 0.73]
   ```
2. **Hill-Langmuir Dose-Response / Binding Affinity**:
   ```latex
   E([L]) = E_{\min} + \frac{E_{\max} - E_{\min}}{1 + \left(\text{IC}_{50} / [L]\right)^{n_H}}, \quad K_i = \frac{\text{IC}_{50}}{1 + [S]/K_m}
   ```
3. **Differential Expression & Eyring Transition-State Barrier (Chemistry)**:
   ```latex
   \text{FDR}_g = p_g^{\text{adj}} < 0.05 \;\wedge\; |\log_2(\mu_{\text{KO},g} / \mu_{\text{WT},g})| \ge 1.0, \qquad \Delta\Delta G^\ddagger = -RT \ln\left(\frac{\text{er}_R}{\text{er}_S}\right)
   ```

---

## 1.4 Biomedical & Chemistry Assertion-Evidence Headline Templates (EN & CN)

| Bad Topic Label (Banned) | Good English Assertion Headline ($\le 14$ words) | Good Chinese Assertion Headline (动宾结论式标题，$\le 24$ 字) |
|:---|:---|:---|
| `Figure 2: Western Blot and IF` | `Microglial TREM2 Loss Halves SYK Phosphorylation and Lipid Clearance` | `小胶质细胞 TREM2 缺失使 SYK 磷酸化与脂质清除下降逾半` |
| `Primary Endpoint Results` | `Adjuvant Osimertinib Cuts CNS Relapse or Death Risk by 76% (HR = 0.24)` | `奥希替尼辅助治疗降低中枢复发或死亡风险达 76%（HR=0.24）` |
| `Substrate Scope` | `Dual Ni/Photoredox Catalysis Tolerates Heterocycles and Drug Scaffolds` | `镍/光氧化还原双催化广泛兼容杂环与复杂药物分子骨架` |
| `fMRI Connectivity Analysis` | `Default-Mode Hypoconnectivity Tracks Preclinical Amyloid Burden` | `默认网络功能连接减弱精准映射临床前期淀粉样蛋白负荷` |

---

# Part II: Economics, Finance, Management & Computational Social Science

## 2.1 Core Seminar Philosophy ("The Applied Micro / Empirical Finance Standard")

Following top economics/finance seminar norms (Jesse Shapiro's *How to Give an Applied Micro Talk*, Paul Goldsmith-Pinkham's Beamer standards, NBER / AFA / AOM conventions):
1. **Preview Quantitative Magnitude by Slide 2**: Never withhold the main empirical answer like a murder mystery. State both the **causal effect sign** and its **economic magnitude** (% of sample mean or SD shift) upfront.
2. **Institutional Context Before Greek Letters**: Dedicate a visual slide to the concrete policy reform, market microstructure rule, or natural experiment timeline *before* writing the econometric equation.
3. **Visual First Stage / Event Study Over Raw Tables**: Never show an event study, RDD, or IV first stage solely as rows of numbers—show the coefficient plot or binned scatterplot (`binscatter`).
4. **Surgical 5-Row Regression Tables**: Strip 35 control-variable rows down to the **1–3 focal causal parameters** + **Fixed-Effects Checkmarks (`✓`)** + **`Dep. Var. Mean`**.

---

## 2.2 Slide-by-Slide Spines (14-Slide Standard)

### Track 2A: Empirical Economics, Finance & Public Policy Spine (Causal Inference Standard)

| Slide # | Category Badge | Standard Slide Title Pattern | Layout Model | Key Visual / Table Asset | Mandatory Econometric Content | Marginal Callout |
|:---|:---|:---|:---|:---|:---|:---|
| **1** | `PAPER OVERVIEW` | `[Paper Title + 3-Bullet Preview of Main Magnitude]` | `hero_1col` | **Teaser Event-Study / Binscatter (Optional Split)** | Authors, NBER/CEPR/Journal status, 1-line Question, Identification hook, Headline causal magnitude. | None |
| **2** | `MOTIVATION & CONTRIBUTION` | `[Economic Puzzle, Policy Stakes & Literature Delta]` | `split_65_35` | **Stylized Fact Time-Series / Cross-Country Plot + 3-Stream Literature Positioning** | Economic friction/puzzle; sharp contrast with 2–3 closest prior papers (avoiding 4-slide laundry-list literature reviews). | `[Policy / Market Relevance]` |
| **3** | `INSTITUTIONAL SETTING` | `[Policy Shock / Market Mechanism & Rollout Timeline]` | `hero_1col` | **Horizontal Rollout Timeline + Spatial Treatment Map** | Who gets treated, when, and by what administrative rule; institutional reason why timing/cutoff is quasi-random. | None |
| **4** | `CONCEPTUAL FRAMEWORK` | `[Theoretical Predictions & Competing Channels]` | `split_equal_2col` | **Equilibrium Diagram / Comparative Statics Sign Table** | Minimalist model intuition ($\partial Y^* / \partial D > 0$ via Channel A vs $<0$ via Channel B) yielding sharp testable predictions. | None |
| **5** | `DATA & SAMPLE` | `[Administrative / Panel Data Merge & Summary Stats]` | `split_65_35` | **Data Linkage Flowchart + Condensed 5-Row Summary Stats** | Sample period, unit of observation ($i \times t$), $N$, key variable means/SDs (`Mean`, `SD`, `P25`, `P75`) to anchor magnitudes. | None |
| **6** | `IDENTIFICATION & SPECIFICATION` | `[Causal DAG, Empirical Equation & Identifying Assumption]` | `split_equal_2col` | **Left: Native Vector Causal DAG; Right: Native OMML Spec** | Exact fixed-effects level, clustering level of SEs (e.g., clustered at state/firm level, matching treatment assignment), explicit threats. | `[Causal Identification Audit]` |
| **7** | `VISUAL IDENTIFICATION` | `[Dynamic Event Study / IV First Stage / RDD Binscatter]` | `split_65_35` | **Harvested High-DPI Event-Study / `rdplot` / `binscatter`** | Flat pre-trends ($k < 0$ joint $F$-test $p$), sharp post-shock break, or KP $F$-stat / McCrary density $p$-value in side card. | None |
| **8** | `BASELINE ESTIMATES` | `[Main Causal Effect: Focal 5-Row Regression Table]` | `asymmetric_2row` | **Rebuilt 5-Row Focal Table (Top) + Economic Magnitude Translation Cards (Bottom)** | Progressive columns `(1)–(4)`, focal $\hat{\beta}$ bolded, `(SE)` in parens, `FE: ✓`, `N`, `R²`, `Dep. Var. Mean`, `% of Mean` interpretation. | None |
| **9** | `THREATS & ROBUSTNESS` | `[Ruling Out Confounders, Staggered Bias & Placebos]` | `quadrant_2x2` | **Modern Estimator Plot (CS/SA) + Permutation Placebo Distribution + Specification Curve** | Staggered-DID heterogeneity-robust estimators, leave-one-out, alternative clustering, randomization inference $p$-value. | `[Econometric Robustness]` |
| **10** | `ECONOMIC MECHANISMS` | `[Dissecting Channels: Mediation / Intermediate Outcomes]` | `split_equal_2col` | **Channel Decomposition Table (`D -> M1, M2`) or Horse-Race** | Empirical test of competing mechanisms ($M_1$ confirmed vs $M_2$ ruled out with statistical null + tight CI). | None |
| **11** | `HETEROGENEITY ANALYSIS` | `[Cross-Sectional Variation Confirms Mechanism]` | `split_65_35` | **Subgroup Coefficient Forest Plot ($\hat{\beta} \pm 95\%\text{ CI}$)** | Ex-ante constrained vs unconstrained firms / high- vs low-exposure regions, reporting interaction $p$-value ($H_0: \beta_{\text{High}} = \beta_{\text{Low}}$). | `[External Validity]` |
| **12** | `WELFARE / COUNTERFACTUAL` | `[Aggregate Economic Magnitude, Spillovers & Welfare]` | `split_equal_2col` | **Counterfactual Simulation / Cost-Benefit Bar Breakdown** | General-equilibrium spillover check (SUTVA audit), back-of-the-envelope MVPF (Marginal Value of Public Funds) or dollar impact. | None |
| **13** | `CRITICAL ASSESSMENT` | `[Core Contributions vs Identification Boundaries]` | `split_equal_2col` | **Balanced Dual Cards (Strengths vs Referee Critiques)** | LATE vs ATE external validity, Lucas critique, short-run vs long-run persistence, data measurement caveats. | None |
| **14** | `POLICY & RESEARCH AGENDA` | `[Policy Takeaways & Follow-Up Research Extensions]` | `split_65_35` | **Policy Design Rules + Lab/Team Replication & Extension Plan** | Replication package availability (`AEA Data & Code`), open identification extensions for our research group. | `[Own Lab Synergy]` |

---

### Track 2B: Management, Strategy, OB & Computational Social Science Adaptations
When presenting **Management / OB / Behavioral / CSS** papers (*AMJ*, *SMJ*, *Management Science*, *Nature Human Behaviour*), adapt Slides 3–11 of Track 2A as follows:
- **Slide 3–4 (`THEORETICAL MODEL & HYPOTHESES`)**: Draw a clean left-to-right **Conceptual Box-and-Arrow Model**: `Antecedent (X)` $\xrightarrow{H_1 (+)}$ `Mediator (M)` $\xrightarrow{H_2 (+)}$ `Outcome (Y)`, with `Moderator (W)` pointing vertically to the arrow labeled `H3 (+ / Buffering)`. Keep hypothesis text inside cards concise ($\le 18$ words per hypothesis).
- **Slide 5–6 (`DATA / EXPERIMENTAL / CSS PIPELINE`)**: For Computational Social Science (LLM annotations, digital trace data, social networks), show the **Corpus $\rightarrow$ Representation/Classifier $\rightarrow$ Human Gold-Standard Validation** pipeline (`Krippendorff's α ≥ 0.82`, macro-F1, prompt-sensitivity audit against measurement bias).
- **Slide 9–10 (`MODERATION SIMPLE SLOPES & SEM`)**:
  - Plot conditional slopes at **Low ($-1\text{ SD}$) vs High ($+1\text{ SD}$)** moderator values with `95% CI` ribbons and plain-language axis titles (never raw centered variable codes like `Z_Auton_c`).
  - For SEM path diagrams: **strip out residual error ovals ($\varepsilon_1 \dots \varepsilon_k$) and indicator factor loadings** (move CFA measurement validity `AVE > 0.50, CR > 0.70, HTMT < 0.85` to Slide 5); render significant paths as `2.0pt` solid arrows (`β = 0.31***`) and non-significant paths as `1.2pt` dashed gray arrows (`β = 0.04 ns`), with a corner fit badge (`χ²/df = 1.84, CFI = 0.97, RMSEA = 0.041, SRMR = 0.035`).

---

## 2.3 Deterministic Table Surgery: Converting a 40-Row Stata/R Dump into a 5-Row Focal Slide Table

### The Cardinal Sin of Economics/Finance Slides
Taking a screenshot of a full-page LaTeX/Word regression table (`esttab`, `outreg2`, `stargazer`, `modelsummary`) with 8–10 columns, 25 control variables, `8pt` Times New Roman, and unreadable footnotes guarantees zero audience comprehension.

### The 6-Step Stata-to-Slide Surgery Protocol
1. **Prune Columns to $\le 5$ Progressive Specifications**: Select only the narrative spine of columns: e.g., `(1) Raw / Baseline OLS`, `(2) + Baseline Controls`, `(3) + Full High-Dim Fixed Effects (Preferred)`, `(4) Alternative Outcome / Subsample`.
2. **Isolate 1–3 Focal Parameter Rows ONLY**: Keep *only* the treatment variable (`Treat × Post`), key interaction (`Treat × Post × Constrained`), or endogenous regressor (`Log Tariff Exposure`). Collapse *all* 15–30 control variables into a single bottom checkmark row (`Firm & Macro Controls: ✓`).
3. **Humanize Variable Labels**: Rewrite Stata code names (`did_post_treat`, `ln_pat_cit_1`, `soe_dum`) into crystal-clear domain phrases (`Carbon Trading Pilot × Post`, `Log(1 + Forward Citations)`, `State-Owned Enterprise`).
4. **Standardize Precision & Inference Formatting**:
   - Round coefficients and standard errors uniformly to **3 decimal places** (or 2 if large magnitudes)—never 6 decimal places (`0.0423891`).
   - Place clustered standard errors in parentheses `(0.011)` directly below or beside the coefficient in muted slate (`#475569`), and bold + tint (`#EFF6FF` or `#F3F4F6`) the focal treatment row.
5. **Enforce the Mandatory Bottom Metadata Block**:
   - **Fixed Effects Checkmarks**: Explicit `✓` (green/black bold) vs `—` (muted gray dash) for each absorbed dimension (`Firm FE`, `Industry × Year FE`, `City Linear Trend`).
   - **Scale & Fit Row**: `Observations (N)` (with comma separators `48,620`), `R² / Within R²` (or `KP rk Wald F-stat` for 2SLS), and **`Dep. Var. Mean`** (mandatory so the audience can divide $\hat{\beta} / \bar{Y}$ instantly!).
6. **Add an Economic Magnitude Callout Strip Below the Table**: Explicitly translate the preferred column's $\hat{\beta}$ into real-world units!

### Concrete Before-vs-After Transformation Example

**❌ BEFORE (Banned Raw Stata/LaTeX Dump — Never Put on Slide)**:
> Unreadable screenshot of `Table 3: Baseline Regression` with 9 columns `(1)-(9)` and 36 rows (`treat_post`, `size`, `lev`, `roa`, `cash`, `age`, `top1`, `board`, `indep`, `tobinq`, `capex`, `gdp_g`, `pop_ln`, `_cons`, plus verbose `t`-statistics, 4-line 7pt footnote).

**✅ AFTER (Agent-Executable Native PPTX Table in `asymmetric_2row` Top Card: $x=0.60'', y=1.65'', w=12.133'', h=3.20''$, Font `13.5pt`)**:

| Dependent Variable: **Log(Green Patent Count + 1)** | (1) TWFE Baseline | (2) + Firm Controls | (3) **Preferred (Ind×Year FE)** | (4) Poisson QMLE |
|:---|:---:|:---:|:---:|:---:|
| **ETS Pilot $\times$ Post** *(Focal Causal Effect)* | **0.094\*\*\*** *(0.026)* | **0.086\*\*\*** *(0.024)* | **0.081\*\*\*** *(0.021)* | **0.192\*\*\*** *(0.049)* |
| Firm-Level Time-Varying Controls (7 vars) | — | ✓ | **✓** | ✓ |
| Firm Fixed Effects | ✓ | ✓ | **✓** | ✓ |
| Year Fixed Effects | ✓ | ✓ | Absorbed | Absorbed |
| Industry $\times$ Year Fixed Effects | — | — | **✓** | ✓ |
| Observations ($N$) | 42,850 | 42,850 | **42,850** | 39,120 |
| Adjusted $R^2$ / Pseudo $R^2$ | 0.684 | 0.701 | **0.738** | 0.412 |
| **Dep. Var. Sample Mean ($\bar{Y}$)** | **0.440** | **0.440** | **0.440** | **0.715** |

*Bottom Takeaway Cards (`y = 5.05", h = 1.80"`)*:
- **Card Left (`Economic Magnitude`)**: Preferred Col. (3) $\hat{\beta} = 0.081$ ($p < 0.001$, SEs clustered at city level, 285 clusters) implies an **+8.4% increase** in green patenting ($\approx \mathbf{18.4\%}$ of the sample mean $\bar{Y} = 0.44$).
- **Card Right (`Specification Stability`)**: Absorbing granular 2-digit `Industry × Year` shocks (Col. 2 $\rightarrow$ Col. 3) attenuates $\hat{\beta}$ by less than $6\%$, bounding omitted industry-demand bias (Oster $\delta = 3.8 > 1$).

---

## 2.4 Causal Inference Visual Grammar & Native OMML Equations

### 1. Identification Strategy DAGs (Native DrawingML Vector Recipe)
Construct inside Left Card of Slide 6 (`x = 0.60", y = 1.65", w = 5.916", h = 5.20"`):
- **Treatment Node ($D$)**: Left-middle `roundRect` (`fill: #DBEAFE`, `border: #1D4ED8`, `2.0pt`).
- **Outcome Node ($Y$)**: Right-middle `roundRect` (`fill: #DCFCE7`, `border: #15803D`, `2.0pt`).
- **Causal Arrow ($D \rightarrow Y$)**: Bold solid arrow (`2.5pt`, `#0F172A`) labeled `Causal Effect β`.
- **Observed / Fixed-Effect Confounder ($X, \alpha_i, \lambda_t$)**: Top `rect` (`fill: #F1F5F9`, `border: #64748B`) with arrows to both $D$ and $Y$, overlaid with `[Blocked via Firm + Ind×Year FE]` pill.
- **Instrument ($Z$, if IV)**: Far-left `oval` (`fill: #FEF3C7`, `border: #D97706`) with solid arrow $Z \rightarrow D$ (`Relevance: KP F = 38.4`) and dashed gray arrow $Z \dashrightarrow Y$ crossed out with crimson `✗` (`Exclusion Restriction`).

### 2. DID Event-Study, IV & RDD Visual Checklist
- **DID Event-Study Plot**:
  1. Horizontal dashed zero line ($Y = 0$) and vertical dashed treatment onset line between $k = -1$ and $k = 0$.
  2. Normalized omitted period $k = -1$ plotted explicitly as a hollow circle pinned at `0` with zero whisker.
  3. Two-zone subtle background tint or top bracket: `Pre-Treatment (Parallel Trends Check: p = 0.68)` vs `Post-Treatment Dynamic Effects`.
  4. Estimator badge in top-left corner: `Callaway & Sant'Anna (2021) / Sun & Abraham (2021), 95% CI`.
- **RDD Binned Scatterplot (`rdplot`)**:
  1. Vertical cutoff line at normalized running variable $X_i - c = 0$.
  2. Equal-spaced or quantile-spaced bin dots (`#64748B`) + separate local polynomial curves and `95% CI` ribbons on left and right of cutoff.
  3. Annotate jump arrow $\hat{\tau}_{\text{SRD}}$ right at $c = 0$, plus CCT bandwidth (`h = 12.4`) and McCrary density discontinuity $p$-value (`p = 0.51 — no sorting at threshold`).

### 3. Econometric Native OMML Templates (`latex_to_omml.py`)
- **Dynamic Event-Study Specification**:
  ```latex
  Y_{i,c,t} = \alpha_i + \lambda_{s(i),t} + \sum_{k = -5,\, k \neq -1}^{+5} \beta_k \cdot \mathbb{I}[t - E_c = k] + \boldsymbol{\Gamma}^\top \mathbf{X}_{i,t} + \varepsilon_{i,c,t}
  ```
- **Two-Stage Least Squares (2SLS) System**:
  ```latex
  \text{1st Stage: } D_{i,t} = \pi Z_{i,t} + \boldsymbol{\Phi}^\top \mathbf{X}_{i,t} + \mu_i + \tau_t + u_{i,t}, \qquad \text{2nd Stage: } Y_{i,t} = \beta \widehat{D}_{i,t} + \boldsymbol{\Theta}^\top \mathbf{X}_{i,t} + \mu_i + \tau_t + \varepsilon_{i,t}
  ```
- **Local Linear Regression Discontinuity**:
  ```latex
  Y_i = \alpha + \tau \cdot \mathbb{I}[R_i \ge c] + \beta_1 (R_i - c) + \beta_2 \mathbb{I}[R_i \ge c] \cdot (R_i - c) + \varepsilon_i, \quad |R_i - c| \le h_{\text{CCT}}
  ```

---

## 2.5 Econ / Finance / Management Headline Templates (EN & CN)

| Bad Topic Label (Banned) | Good English Assertion Headline ($\le 14$ words) | Good Chinese Assertion Headline (动宾结论式标题，$\le 24$ 字) |
|:---|:---|:---|
| `Baseline Regression Results` | `Carbon Pricing Boosts Firm Green Patenting by 18% of Sample Mean` | `碳排放权交易试点使企业绿色专利产出提升均值之 18%` |
| `Parallel Trends Test` | `Pre-Reform Trends Track Zero Closely Before Diverging Immediately Post-Shock` | `政策冲击前实验组与对照组趋势高度平行，冲击后显著分化` |
| `Mechanism Analysis` | `R&D Reallocation—Not Leverage Expansion—Drives the Innovation Gain` | `研发资源重配置而非负债扩张主导了企业绿色创新增长` |
| `Moderation Hypothesis H3` | `High Task Autonomy Doubles the Return to Algorithmic Coaching (+1 SD)` | `高任务自主权使算法辅导的绩效增益翻倍（+1 SD 简单斜率）` |

---

# Part III: Humanities, Law, History, Education & Qualitative Research

## 3.1 Core Philosophy: Text & Archive as Visual Evidence

In Humanities, Law, History, and Qualitative Social Science, **primary texts, archival manuscripts, statutory clauses, informant voices, and conceptual typologies ARE the empirical figures**.
- **The Fatal Trap**: Treating slides either as a teleprompter script (pasting 250-word paragraphs and reading them aloud) OR stripping away primary textual texture into sterile corporate bullet points.
- **The Solution**: Frame every primary excerpt as a curated **Visual Artifact Card** ($\le 45$ words of verbatim text, paired with facsimile/provenance, typographic hierarchy, lexical callouts, and analytical synthesis).

---

## 3.2 Slide-by-Slide Spines (14-Slide Standard)

### Track 3A: History, Literature, Philosophy & Archival Humanities Spine

| Slide # | Category Badge | Slide Role | Layout Model | Visual / Textual Artifact | Mandatory Scholarly Rigor |
|:---|:---|:---|:---|:---|:---|
| **1** | `MONOGRAPH / PAPER OVERVIEW` | Title, Historical Period, Core Thesis | `split_equal_2col` | **Iconic Archival Plate / Woodcut / Map + Citation Card** | Period/geography badge (e.g., *Qing Jiangnan, 1720–1840*), central historiographical thesis. |
| **2** | `HISTORIOGRAPHICAL PUZZLE` | Concrete Historical Anomaly / Paradox | `split_65_35` | **Vignette Artifact (1 Micro-Case / Court Record)** | Open with a concrete archival micro-puzzle that conventional orthodoxy cannot explain. |
| **3** | `SCHOLARLY INTERVENTION` | Competing Historiographical Schools | `grid_3col` | **3-Column School Comparison (`Orthodoxy A` vs `Revisionism B` vs `This Study`)** | Name key scholars/schools, pinpoint their shared blindspot, state your conceptual shift. |
| **4** | `CORPUS & ARCHIVAL BASE` | Sources, Archives & Silences | `split_65_35` | **Geographical Archive Map + Corpus Inventory Table** | Archive repositories, document genres, volume ($N$ memorials/dossiers), reading "against the grain" note. |
| **5** | `PERIODIZATION / TIMELINE` | Structural Chronology & Turning Points | `hero_1col` | **3-Era Horizontal Periodization Ribbon** | Macro institutional/political inflection points anchoring the close readings ahead. |
| **6** | `CONCEPTUAL FRAMEWORK` | Analytical Typology / $2 \times 2$ Matrix | `quadrant_2x2` | **Orthogonal $2 \times 2$ Conceptual Matrix** | Define core analytical categories (e.g., *State Legibility* $\times$ *Local Vernacular Mediation*). |
| **7** | `MOVEMENT I: CLOSE READING` | **Primary Source Analysis I (Baseline)** | `split_equal_2col` | **Left: High-DPI Manuscript Facsimile (Zoom Box); Right: Bilingual Transcription + Gloss** | Exact archival shelfmark/folio, author $\rightarrow$ audience, $\le 45$-word excerpt with 6–8 pivot words highlighted. |
| **8** | `LEXICAL / SEMANTIC SHIFT` | Philological / Discourse Tracking | `split_65_35` | **Term Evolution Timeline or Corpus Frequency Trajectory** | How a key concept (e.g., *gong/公*, *jurisdiction*, *Bildung*) mutates in meaning across periods/genres. |
| **9** | `MOVEMENT II: CLOSE READING` | **Primary Source Analysis II (Rupture)** | `split_equal_2col` | **Paired Counter-Archive (Official Decree vs Subaltern Petition)** | Juxtapose elite/state framing against vernacular/litigant practice to expose tension. |
| **10** | `COMPARATIVE SYNTHESIS` | Cross-Case / Regional / Textual Matrix | `hero_1col` | **3-Case $\times$ 4-Dimension Comparative Synthesis Table** | Prove the close readings represent a structural pattern rather than isolated anecdotes. |
| **11** | `COUNTER-ARGUMENTS` | Addressing Alternative Readings | `split_equal_2col` | **Objection / Archival Bias vs Rebuttal Evidence** | Directly confront survivorship bias, scribal formulaic conventions, or regional exceptionalism. |
| **12** | `THEORETICAL PAYOFF` | Broader Conceptual Re-theorization | `split_65_35` | **Revised Conceptual Model Diagram** | How the historical/textual findings reshape broader theory beyond the narrow subfield. |
| **13** | `SCOPE & SILENCES` | Archival Boundaries & Unrecovered Voices | `split_equal_2col` | **Contributions vs Source Limitations** | Honest accounting of what extant archives cannot see (unrecorded oral/gendered/marginal actors). |
| **14** | `CODA & RESEARCH HORIZONS` | Next Archival Fonds & Seminar Questions | `split_65_35` | **3 Interpretive Questions + Next Archival / Digital Humanities Plan** | Concrete next archive/corpus linkages and cross-disciplinary dialogue prompts. |

---

### Track 3B: Legal Scholarship & Comparative Doctrine Spine
- **Slide 1–2 (`JUDICIAL SPLIT / REGULATORY CRISIS`)**: Concrete case hypothetical or circuit split map (e.g., *2nd & 9th Circuits* vs *5th & 7th Circuits*; or *Supreme People's Court Guiding Case* tension).
- **Slide 3–4 (`STATUTORY / CONSTITUTIONAL CLOSE READING`)**: `split_equal_2col`: Left card displays exact statutory clause (`15 U.S.C. § ...` or `《民法典》第 X 条`) in `15pt Georgia / 华文中宋` with crimson callout brackets around the **2–3 operative ambiguous words**; Right card contrasts **Textualist**, **Purposivist**, and **Doctrinal Precedent** readings.
- **Slide 5–7 (`COMPARATIVE DOCTRINAL MATRIX`)**: Structured 4-column table comparing Jurisdictions (`US / EU AI Act / China / Germany`) across *Trigger Threshold*, *Mens Rea / Liability Standard*, *Burden of Proof*, and *Remedial Gap*.
- **Slide 8–10 (`NORMATIVE / EMPIRICAL CRITIQUE & PROPOSED TEST`)**: Explicit 3-prong **Proposed Judicial Test / Safe-Harbor Framework** rendered as a clean decision flowchart (`Step 1 Threshold` $\rightarrow$ `Step 2 Burden Shift` $\rightarrow$ `Step 3 Proportional Remedy`).
- **Slide 11–14 (`EDGE-CASE STRESS TEST & IMPLICATIONS`)**: Apply the proposed test to 3 hard borderline cases (`quadrant_2x2` or `grid_3col`) to prove doctrinal determinacy.

---

### Track 3C: Qualitative Sociology, Anthropology, Management & Education Spine
- **Slide 1–3 (`EMPIRICAL PUZZLE & THEORETICAL LENS`)**: Field puzzle + why existing theory predicts X while informants enact Y.
- **Slide 4 (`FIELDSITE, CORPUS & TRUSTWORTHINESS`)**: `grid_3col`: (1) Fieldsite / Intervention design ($N = 64$ semi-structured interviews, $180\text{ hrs}$ ethnographic observation, $420$ archival memos), (2) Sampling & Triangulation matrix, (3) **Methodological Rigor Badges** (`Theoretical Saturation at Interview #52`, `Inter-coder Cohen's κ = 0.86`, `Member-Checking`).
- **Slide 5 (`GIOIA / GROUNDED THEORY DATA STRUCTURE OVERVIEW`)**: Full 3-tier architecture (`1st-Order Informant Concepts` $\rightarrow$ `2nd-Order Themes` $\rightarrow$ `Aggregate Dimensions`) at bird's-eye scale with focal branch highlighted.
- **Slide 6–9 (`THEMATIC DEEP-DIVES 1–3 + MIXED-METHODS OUTCOMES`)**: One slide per Aggregate Dimension pairing **2 crisp Informant Quotes** (with pseudonym/role tag `[ Nurse #14, ICU, 8 yrs ]`) + analytical mechanism; for **Education / Mixed-Methods Interventions**, dedicate Slide 8–9 to **Pre- vs Post-Intervention Paired Plots + Focal `Cohen's d` Effect Size Card** (`d = 0.82, 95% CI [0.54, 1.10] — Large Practical Effect`, paired with rubric error reduction `%`).
- **Slide 10–11 (`DYNAMIC PROCESS MODEL / CONCEPTUAL 2×2 MATRIX`)**: Grounded process model showing temporal phases, boundary triggers, and feedback loops (distinguishing *Data Structure* static taxonomy from *Grounded Theory* dynamic model!).
- **Slide 12–14 (`BOUNDARY CONDITIONS, PEDAGOGICAL / POLICY DESIGN & ROADMAP`)**.

---

## 3.3 Humanities & Qualitative Layout Blueprints

### Rule H1: Archival Primary Source & Bilingual Close-Reading Card (`split_equal_2col`)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Slide 7: Magistrates Recast Customary Lineage Trusts as Taxable Commercials  │
├──────────────────────────────────────┬───────────────────────────────────────┤
│  CARD 0: Archival Facsimile & Meta   │  CARD 1: Bilingual Close Reading      │
│  (x=0.60", y=1.65", w=5.916", h=5.20")│  (x=6.816", y=1.65", w=5.916", h=5.20")│
│  ┌────────────────────────────────┐  │  ▌ ORIGINAL EXCERPT (15pt Serif):     │
│  │  [High-DPI 300+ Scan of Folio] │  │  ▌ 「名雖祀產，實同**市肆牟利**，未便   │
│  │       ┏━━━━━━━━━━━━━━━┓        │  │  ▌   任其藉詞**蠲免**……」             │
│  │       ┃ Red Zoom Box  ┃        │  │  ───────────────────────────────────  │
│  │       ┗━━━━━━━━━━━━━━━┛        │  │  ▌ ANALYTICAL TRANSLATION (13.5pt):   │
│  └────────────────────────────────┘  │  ▌ "Though styled *ancestral estate*  │
│  • Archive: First Historical Archives│  │ (*sichan*), in substance it seeks  │
│    of China,戶科題本 #02-01-04-219   │  │ **market profit** (*mouli*) and    │
│  • Date / Actor: Qianlong 42 (1777), │  │ cannot claim **tax exemption**."   │
│    Suzhou Prefect -> Board of Revenue│  • Lexical Pivot: Equating *sichan*   │
│  • Genre: Routine Fiscal Memorial    │    with *shisi* collapses ritual      │
│                                      │    immunity into commercial liability.│
└──────────────────────────────────────┴───────────────────────────────────────┘
```

1. **Strict 45-Word Verbatim Ceiling**: Never paste more than **45 English words** (or **75 Chinese characters**) of a continuous block quote inside a single card. Ellipsize (`[...]`) non-essential clauses ruthlessly.
2. **Bilingual Typographic Contrast**:
   - Render the **Original Source Text** on top (or left) in a scholarly serif (`Georgia`, `Garamond`, `华文中宋`, or `方正书宋`, `14–16pt`), enclosed in a warm ivory/parchment-tinted sub-card (`#FAF8F5` or `#F9FAFB` with `2pt` left border).
   - Render the **Working Translation** directly beneath in clean sans-serif (`Arial` / `微软雅黑`, `13–14pt`, `#1F2937`).
   - **Preserve Untranslatable Terms Inline**: Keep doctrinally or culturally loaded source terms in bold italics alongside the gloss (e.g., *sichan* [ancestral trust], *doli incapax*, *Verstehen*, *礼治*), and dedicate 1 bullet below to unpacking the exact semantic work that term performs.
3. **Mandatory 4-Item Provenance Badge**: Every archival or legal quote card must carry `Repository/Court`, `Document/Statute ID`, `Date`, and `Speaker → Addressee` (`10.5–11.5pt` muted slate `#4B5563`).

### Rule H2: Rebuilding Gioia / 扎根理论三级编码 Diagrams (`grid_3col` Progressive Flow)
Never paste a 35-row manuscript Gioia table or raw NVivo tree. Rebuild as a native **3-Column Chevron Architecture** (`y = 1.65", h = 5.20"`):
- **Column 1 (`x = 0.600", w = 3.877"`) — `1st-Order Informant Concepts` (开放式编码)**:
  - Max **4 informant-centric cards** (`h = 0.95"` each), written in *italicized informant vernacular* with quotation marks and respondent IDs: e.g., *"Hiding prompts so managers think I wrote it myself" (`[Eng #09]`)*.
- **Column 2 (`x = 4.727", w = 3.877"`) — `2nd-Order Theoretical Themes` (主轴编码)**:
  - **2 researcher-centric theme cards** (`h = 2.05"` each, bold title + brief analytical definition) connected via bracket arrows from pairs of Column 1 concepts: e.g., **`Covert Competence Signaling`** & **`Algorithmic Stigma Avoidance`**.
- **Column 3 (`x = 8.854", w = 3.877"`) — `Aggregate Dimension` (选择性编码 / 核心范畴)**:
  - **1 high-contrast anchor card** (`h = 4.35"`, accented border `2.0pt`) uniting the themes into the core theoretical construct: e.g., **`Shadow AI Craftwork`**, complete with corpus prevalence (`Observed in 47/64 informants [73%]`) and link to downstream process outcome.

### Rule H3: Orthogonal $2 \times 2$ Conceptual Typology Matrix (`quadrant_2x2`)
- Explicitly draw **Axis Arrows** along the outer left (`Y-axis: Low ← Institutional Formalization → High`) and top/bottom (`X-axis: Elite Monopoly ← Interpretive Authority → Vernacular Pluralism`).
- Inside each of the 4 quadrants (`w = 5.916", h = 2.475"`), enforce a strict **3-Part Micro-Template**:
  1. **Archetype Name** (`16pt Bold`, e.g., `I. Codified State Orthodoxy`).
  2. **2 Analytical Attributes** (`12.5pt`, $\le 10$ words each).
  3. **1 Concrete Historical / Legal / Empirical Exemplar Pill** at the bottom (`11.5pt Bold`, e.g., `Exemplar: 1740 Qing Sub-Statute Revision`).
- Highlight the **focal quadrant** introduced or occupied by the paper's thesis with a `2.0pt` theme accent border and soft tint (`#EFF6FF` or `#FEF2F2`).

---

## 3.4 Humanities, Law & Education Headline Templates (EN & CN)

| Bad Topic Label (Banned) | Good English Assertion Headline ($\le 14$ words) | Good Chinese Assertion Headline (动宾结论式标题，$\le 24$ 字) |
|:---|:---|:---|
| `Archival Source Analysis` | `1777 Fiscal Memorials Reframe Kinship Trusts as Commercial Tax Shelters` | `乾隆四十二年户科题本将宗族祀产重定性为牟利商产` |
| `Circuit Split Overview` | `Circuit Courts Split Over Whether Algorithmic Pricing Requires Express Agreement` | `巡回法院就算法默示合谋是否需明示协议陷入裁判分裂` |
| `Grounded Theory Coding` | `Three-Stage Coding Reveals "Shadow AI Craftwork" Across 73% of Engineers` | `三级扎根编码揭示七成工程师采取“隐蔽式 AI 工艺”策略` |
| `Pre-Post Test Scores` | `Statutory Close-Reading Rubric Training Yields a Large Gain (Cohen's d = 0.82)` | `法条精读量表干预显著提升法律推理表现（Cohen's d=0.82）` |

---

# Part IV: Cross-Disciplinary Marginal Callout ("旁注") Extension & Vision QA Checklist

## 4.1 Discipline-Adapted Marginal Callout Taxonomy (`split_65_35` Side-Note Card)

Replace CS-specific callout badges (`[State Memory Inertia]`, `[Computational & Hardware Efficiency]`) with discipline-native classes when routing outside CS/EE:

| Super-Cluster | Slide 2 Callout Class | Slide 5 / 6 Callout Class | Slide 8 / 9 Callout Class | Slide 11 / 12 Callout Class | Slide 14 Callout Class |
|:---|:---|:---|:---|:---|:---|
| **I. Biomed / Clinical / Chem** | `[Translational / Clinical Gap]` | `[Cohort / Model Lineage]` | `[Assay & Mechanistic Rigor]` | `[Safety, PK/PD & Scalability]` | `[Own Lab Reagent / Cohort Synergy]` |
| **II. Econ / Fin / Mgmt / CSS** | `[Policy & Market Friction]` | `[Causal Identification Audit]` | `[Econometric Robustness]` | `[External Validity & Welfare]` | `[Team Data / Identification Synergy]` |
| **III. Humanities / Law / Qual**| `[Historiographical / Doctrinal Tension]` | `[Archival / Corpus Provenance]` | `[Close-Reading / Coding Audit]` | `[Comparative / Normative Scope]` | `[Seminar Corpus & Theory Synergy]` |

---

## 4.2 Anti-Patterns & Mandatory Vision-in-the-Loop (`view_file`) Inspection Rubric

Before finalizing any deck in these three super-clusters, rasterize every slide to `150+ DPI` PNG and audit with `view_file` against these 12 high-frequency defects:

| # | Discipline | Anti-Pattern (Automatic Fail) | Vision-in-the-Loop (`view_file`) Pass Criterion |
|:---|:---|:---|:---|
| **1** | Biomed | Whole-page 8–12 panel *Nature*/*Cell* figure pasted onto one slide | Max 2–3 sub-panels per slide (`≥ 11pt` visual axis text readability) or spotlight-masked |
| **2** | Biomed | Micrograph missing physical scale bar or relying on `"400×"` text | Crisp `µm`/`nm` scale bar visible in bottom corner with legible high-contrast label |
| **3** | Biomed | Western blot lacking `kDa` markers, loading control, or replicate $n$ | Target band + `GAPDH`/`β-actin` aligned vertically + `kDa` labels + $n$ biological replicates |
| **4** | Clinical | Kaplan-Meier curve cropped above `Number at Risk` table | Full `No. at Risk` table aligned cleanly beneath X-axis + floating `HR (95% CI), P` badge |
| **5** | Chemistry | Blurry low-DPI ChemDraw bitmap or 30-compound SI scope dump | Razor-sharp `1.5–2pt` bonds, curated 6–8 substrate grid + 1 diagnostic failed substrate |
| **6** | Econ / Fin | Screenshot of 30–40 row Stata/LaTeX regression table (`<10pt` font) | Native 4–5 col $\times$ 1–3 focal-row table (`≥ 13pt`), `FE: ✓` rows, and `Dep. Var. Mean` |
| **7** | Econ / Fin | Reporting `"significant positive β"` without economic magnitude | Slide explicitly translates $\hat{\beta}$ into `% of sample mean` or `SD` units |
| **8** | Econ / Fin | DID reported only as static TWFE number without pre-trend visual | Event-study dynamic plot shows flat $k < 0$ pre-trends (`p`-value shown) and normalized $k=-1$ |
| **9** | Mgmt / CSS | SEM diagram cluttered with $\varepsilon_i$ error circles & tiny text | Clean latent/observed box-arrow paths (`≥ 13pt`), error ovals omitted, fit badge isolated |
| **10** | Humanities | Single-spaced 150–300 word block quote filling the entire slide | Verbatim quote strictly $\le 45$ words (EN) / $\le 75$ chars (CN) with 6–8 bold pivot words |
| **11** | Law / Hist | Primary quote or statute lacking provenance / translation split | Original serif above/left + clean translation below/right + 4-item provenance footer |
| **12** | Qualitative | Raw NVivo screenshot or 35-row manuscript Gioia table | Native 3-column chevron flow (`1st-Order` $\rightarrow$ `2nd-Order` $\rightarrow$ `Aggregate`) + $\kappa$/saturation badge |

---

## 4.3 Quantitative Density, Table & Typography Budgets by Discipline

Agents generating slides via `python-pptx` or `pptxgenjs` must enforce these hard numerical ceilings before rendering:

| Asset / Card Type | Target Grid Model | Max Rows $\times$ Cols | Min Font Floor (`pt`) | Border / Rule Styling | Strict Density Ceiling |
|:---|:---|:---|:---|:---|:---|
| **Clinical Baseline `Table 1`** | `split_65_35` (Main) | $\le 8\text{ rows} \times 4\text{ cols}$ | `12.5 pt` | Booktabs (`1.5pt` top/bottom, `0.75pt` header rule, `0pt` vertical lines) | Summarize continuous vars as `Mean ± SD` or `Median (IQR)`; categorical as `n (%)`. |
| **Chemistry Optimization Table** | `split_65_35` (Main) | $\le 6\text{ entries} \times 4\text{ cols}$ | `13.0 pt` | Booktabs + top highlight row (`#EFF6FF`) for optimal Entry 1 | Columns: `Entry`, `Deviation from Standard Conditions`, `Yield (%)`, `ee / dr`. |
| **Chemistry Substrate Scope** | `grid_4col` ($2\times 4$ cells) | $6\text{–}8$ structures max | `12.0 pt` labels | Clean rounded cards (`0.08"` radius), `1.5pt` bond strokes | Include `Product ID (3a)`, `Yield (%)`, `dr/ee`, and $\ge 1$ diagnostic limitation (`<5%`). |
| **Econ / Finance Focal Table** | `asymmetric_2row` (Top) | $1\text{–}3$ focal rows + $3\text{–}4$ FE/stat rows $\times \le 5\text{ cols}$ | `13.0 pt` (`11.5pt` SEs) | Booktabs (`1.5pt` outer, `0.75pt` separating focal rows from FE `✓` block, `0pt` vertical) | Always report `(Clustered SE)`, `FE: ✓ / —`, `N`, `R²`, and **`Dep. Var. Mean`**. |
| **Subgroup / Heterogeneity Forest**| `hero_1col` or `split_65_35` | $\le 9$ subgroup rows | `12.5 pt` | Vertical dashed null line (`1.0pt`, `#64748B` at `HR=1` or `β=0`) | Align graphical CIs horizontally with exact right-aligned text `Est. [95% CI]`. |
| **Archival / Statutory Close Read**| `split_equal_2col` | 1 source block + 1 translation block | `14.0 pt` source / `13.0 pt` trans. | Left accent bar (`0.06"`, `#991B1B` or `#1E3A8A`) on ivory/slate tint | $\le 45$ English words ($\le 75$ Chinese chars) verbatim; bold **only 6–8 pivot words**. |
| **Gioia / Grounded Coding Flow** | `grid_3col` | $\le 4$ `1st-order` $\rightarrow$ $2$ `2nd-order` $\rightarrow$ $1$ `Aggregate` | `12.0 pt` quotes / `13.5 pt` themes | `1.5pt` card borders + `1.5pt` directional bracket connectors | Show 1 Aggregate Dimension deep-dive per slide; never cram all 30 codes onto 1 slide. |
| **Conceptual $2 \times 2$ Matrix** | `quadrant_2x2` | $2 \times 2$ quadrants | `15.0 pt` title / `12.5 pt` body | Orthogonal axis arrows (`2.0pt`) + highlighted thesis quadrant | Max `1 Archetype Title + 2 micro-bullets (≤10 words) + 1 Exemplar badge` per cell. |

---

## 4.4 Specialized 16:9 Coordinate Blueprints (`13.333" × 7.500"`)

### Blueprint 1: *Cell* / *Nature* Graphical Abstract Slide (`hero_1col` 3-State Biological Flow)
When constructing a clean vector Graphical Abstract or Working Model (Slide 1 or Slide 13) without harvested artwork:
- **Anti-AI-Slop Rule**: Never use Midjourney/DALL-E glowing 3D sci-fi brains, neon DNA helices, or isometric plastic cells. Use flat, clean vector geometric primitives (`oval` membranes, `roundRect` receptors, crisp solid/inhibitory T-bar arrows `┤`).
- **3-Column Compartmental Coordinates (`Y = 1.650", H = 5.200"`)**:
  - **Zone 1 — Homeostasis / Wild-Type (`x = 0.600", w = 3.800"`)**: Soft neutral fill (`#F8FAFC`), header pill `1. HEALTHY / WILD-TYPE`, intact signaling arrow `Receptor ──> Kinase ──> Gene ON`.
  - **Zone 2 — Pathological Perturbation (`x = 4.766", w = 3.800"`)**: Soft rose tint (`#FFF1F2`, border `#E11D48`), header pill `2. DISEASE / MUTANT LOSS`, crimson `✗` over mutated node + blunt T-bar inhibitory connector (`──┤`) showing blocked clearance / hyper-inflammation.
  - **Zone 3 — Therapeutic Rescue (`x = 8.933", w = 3.800"`)**: Soft teal/emerald tint (`#F0FDFA`, border `#0D9488`), header pill `3. SMALL-MOLECULE / GENE RESCUE`, drug ligand badge (`IC50 = 14 nM`) restoring downstream pathway flux.

### Blueprint 2: Chemistry Reaction Header + $2 \times 4$ Substrate Scope Grid
- **Top Reaction Banner (`x = 0.600", y = 1.650", w = 12.133", h = 1.450"`)**:
  - Left Reactants (`x = 0.90", w = 3.80"`), Center Reaction Arrow (`x = 4.90", y = 2.38", w = 3.10"`), Right Product (`x = 8.20", w = 3.80"`).
  - **Above Arrow Box (`x = 4.80", y = 1.78", w = 3.30", h = 0.52"`, `12pt Arial`)**: `[Ni(cod)2] (5 mol%), L4* (6 mol%), Ir-PC (1 mol%) / Blue LEDs, DME, 25 °C`.
  - **Below Arrow Box (`x = 4.80", y = 2.45", w = 3.30", h = 0.40"`, `12pt Bold`)**: `12 h, up to 95% yield, 97:3 er`.
- **Bottom $2 \times 4$ Curated Scope Grid (`y_row1 = 3.300", y_row2 = 5.125", h_cell = 1.675", w_cell = 2.883"`, `gapX = 0.200"`)**:
  - Cells `1–7`: Cropped vector/350-DPI product structures (`3a–3g`) with newly formed bond in `#DC2626` and bottom pill `3a: 91%, 96% ee`.
  - Cell `8` (`x = 9.849", y = 5.125"`): Dashed slate border (`#94A3B8`) titled **`Unsuccessful Substrate`** (`3x: <5% yield — ortho-NO2 quenches excited Ir*`).

### Blueprint 3: Unified Forest Plot (Clinical Subgroups OR Econometric Heterogeneity)
Inside `hero_1col` (`x = 0.600", y = 1.650", w = 12.133", h = 5.200"`), partition horizontally into 4 aligned columns with zero misregistration:
1. **Col A — Subgroup / Sample Split Label (`x = 0.85", w = 3.20"`)**: Bold category header (`Age`, `Firm Financial Constraint`) + indented strata (`< 65 yr`, `≥ 65 yr`).
2. **Col B — Sample / Event Count (`x = 4.15", w = 1.60"`)**: Monospace/tabular numerals (`214 / 430` or `N = 18,420`).
3. **Col C — Graphical Point-and-Whisker Canvas (`x = 5.90", w = 3.80"`)**:
   - Vertical dashed reference line (`HR = 1.0` on log scale, or `β = 0.0` on linear scale).
   - Directional axis footer arrows (`← Favors Intervention` | `Favors Control →`).
   - Square marker centered at point estimate (area $\propto$ precision $1/\text{SE}^2$) + horizontal `1.75pt` whisker spanning `[LCL, UCL]`.
4. **Col D — Tabular Estimate & Interaction $P$ (`x = 9.85", w = 2.60"`)**: Right-aligned `0.54 (0.41–0.71)` and `P_int = 0.018`.

### Blueprint 4: Education & Behavioral Pre-Post Intervention + Effect Size Equations
Pair a pre-post paired distribution chart (`x = 0.600", w = 7.700"`) with an **Effect Size Translation Side-Card** (`x = 8.600", w = 4.133"`) using native OMML (`latex_to_omml.py`):
```latex
d_{\text{Cohen}} = \frac{\bar{Y}_{\text{post}} - \bar{Y}_{\text{pre}}}{s_{\text{pooled}}} = 0.82 \; [0.54, 1.10], \qquad s_{\text{pooled}} = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}
```
- **Substantive Translation Rule**: Always accompany $d$, Hedges' $g$, or partial $\eta_p^2$ with a plain-domain interpretation (e.g., `d = 0.82 shifts the median treatment learner to the 79th percentile of the control classroom`, or translates into `+4.3 months of additional learning progress` per Education Endowment Foundation / What Works Clearinghouse norms).

---

## 4.5 Agent-Executable Slide IR Schemas (JSON Reference)

### Schema A: Focal 5-Row Econometric Regression Slide (`asymmetric_2row`)
```json
{
  "slide_index": 8,
  "discipline_track": "econ_causal_2A",
  "layout": "asymmetric_2row",
  "tracker": "BASELINE ESTIMATES • SLIDE 08 OF 14",
  "title": "Carbon Pricing Boosts Firm Green Patenting by 18% of Sample Mean",
  "subtitle": "Estimates remain stable across firm controls, Industry × Year shocks, and count models.",
  "focal_regression_table": {
    "dep_var_label": "Log(Green Patent Count + 1)",
    "columns": ["(1) Baseline", "(2) + Controls", "(3) Preferred", "(4) Poisson"],
    "highlight_col_index": 2,
    "focal_rows": [
      {
        "variable": "ETS Pilot × Post",
        "estimates": ["0.094***", "0.086***", "0.081***", "0.192***"],
        "std_errors": ["(0.026)", "(0.024)", "(0.021)", "(0.049)"],
        "highlight_row": true
      }
    ],
    "fe_checkmark_rows": [
      { "label": "Time-Varying Firm Controls", "values": ["—", "✓", "✓", "✓"] },
      { "label": "Firm Fixed Effects", "values": ["✓", "✓", "✓", "✓"] },
      { "label": "Industry × Year Fixed Effects", "values": ["—", "—", "✓", "✓"] }
    ],
    "summary_rows": [
      { "label": "Observations (N)", "values": ["42,850", "42,850", "42,850", "39,120"] },
      { "label": "Adjusted / Pseudo R²", "values": ["0.684", "0.701", "0.738", "0.412"] },
      { "label": "Dep. Var. Sample Mean", "values": ["0.440", "0.440", "0.440", "0.715"] }
    ],
    "footnote": "Standard errors clustered at the city level (285 clusters) in parentheses. * p < 0.10, ** p < 0.05, *** p < 0.01."
  },
  "bottom_cards": [
    {
      "title": "Economic Magnitude Translation",
      "bullets": [
        "Preferred Col. (3) β = 0.081 implies an +8.4% rise in green patents (18.4% of sample mean 0.44).",
        "Equivalent to closing 31% of the pre-policy innovation gap between SOEs and private manufacturers."
      ]
    },
    {
      "title": "Identification Stability (Oster Bounds)",
      "bullets": [
        "Adding 2-digit Industry × Year FE shifts β from 0.086 to 0.081 (<6% attenuation) while R² rises to 0.738.",
        "Oster (2019) selection ratio δ = 3.8 (> 1.0 cutoff) rules out unobservable time-varying confounders."
      ]
    }
  ]
}
```

### Schema B: Archival Bilingual Close-Reading Slide (`split_equal_2col`)
```json
{
  "slide_index": 7,
  "discipline_track": "humanities_archival_3A",
  "layout": "split_equal_2col",
  "tracker": "MOVEMENT I: CLOSE READING • SLIDE 07 OF 14",
  "title": "1777 Fiscal Memorials Recast Kinship Trusts as Commercial Tax Shelters",
  "subtitle": "Prefectural magistrates pierced ritual nomenclature by auditing market lease revenues.",
  "left_artifact_card": {
    "image_path": "figures/fha_memorial_1777_crop_350dpi.png",
    "zoom_bbox_norm": [0.32, 0.18, 0.24, 0.62],
    "provenance": {
      "repository": "First Historical Archives of China (FHAC), Beijing",
      "shelfmark": "Huke Tiben (戶科題本) #02-01-04-0219-014",
      "date": "Qianlong 42 / 8th Lunar Month (Sept. 1777)",
      "actors": "Suzhou Prefect → Grand Council & Board of Revenue"
    }
  },
  "right_close_reading_card": {
    "source_lang": "Classical Chinese",
    "source_font": "STZhongsong",
    "original_excerpt": "「名雖祀產，實同**市肆牟利**，未便任其藉詞**蠲免**……」",
    "working_translation": "\"Though styled an *ancestral estate* (*sichan*), in substance it operates like a **urban shop seeking profit** (*shisi mouli*), and cannot claim **tax exemption** (*juanmian*).\"",
    "word_count_en": 28,
    "lexical_callouts": [
      {
        "term": "sichan → shisi (祀產 → 市肆)",
        "analysis": "Collapses the legal boundary between sacred lineage property and taxable commercial real estate."
      },
      {
        "term": "jieci juanmian (藉詞蠲免)",
        "analysis": "Frames customary tax immunity not as orthodox filial virtue, but as strategic fiscal evasion."
      }
    ]
  }
}
```
