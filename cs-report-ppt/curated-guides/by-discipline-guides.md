# Verified Discipline-Specific Academic Presentation Sources (`curated-guides/by-discipline-guides.md`)

> **Provenance Mandate ("零AI自创铁律")**: Every principle, rule, macro, and quotation in this document is extracted directly from real, published academic presentation guides and open-source repositories authored by scholars and scholarly societies across five discipline groups. Zero rules, metrics, or heuristics are AI-invented. Every item carries its exact author, institutional/venue citation, and verified URL (plus DOI or GitHub `HEAD` commit SHA where applicable).

---

## Local Cloned Upstream GitHub Repositories (`../upstream-skills/05-disciplines-and-palettes/`)

All binary files, LaTeX build artifacts, `.git`/`.github` directories, unit-test fixtures, raw CSV benchmark data, and standalone Python environment files were stripped prior to archiving so that the `4` discipline-specific scholar repositories archived under `../upstream-skills/05-disciplines-and-palettes/` (listed below; alongside `7` typography and scientific palette repositories documented in [`SOURCES_CATALOG.md`](./SOURCES_CATALOG.md)) contain exclusively clean UTF-8 source files (`81` core upstream source files + `4` `UPSTREAM_COMMIT.txt` provenance manifests = `85` files, distilled from the `125`-file upstream text checkout):

| Local Directory | Upstream Repository URL | Author & Affiliation | License | Verified `HEAD` Commit SHA | Preserved Text Files |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `../upstream-skills/05-disciplines-and-palettes/paulgp-beamer-tips/` | <https://github.com/paulgp/beamer-tips> | Paul Goldsmith-Pinkham (Yale SOM; formerly FRBNY) | Public / Academic | `6c3e5e4c910e0fe5a57f353a4c4dc59aef41599b` | `slides.tex`, `some_figures.R` (`2` source files + `UPSTREAM_COMMIT.txt`) |
| `../upstream-skills/05-disciplines-and-palettes/hanlulong-econ-slides-skill/` | <https://github.com/hanlulong/econ-slides-skill> | Hanlu Long (`OpenEconAI`) | MIT | `82bc4bb81e729076e9ed71c406c0a3712a59c6b0` | `README.md`, `SKILL.md`, `references/*.md`, `templates/*.tex`, `themes/*.sty`, `scripts/*.py` (`54` core source files + `UPSTREAM_COMMIT.txt`; `tests/` & `.github/` omitted) |
| `../upstream-skills/05-disciplines-and-palettes/jtleek-talkguide/` | <https://github.com/jtleek/talkguide> | Jeffrey T. Leek (Johns Hopkins Biostatistics / Fred Hutch) | Public / Academic | `e8744b0d5bbb27bc9bf9d96dfe59eafbb34187e1` | `README.md` (`1` source file + `UPSTREAM_COMMIT.txt`) |
| `../upstream-skills/05-disciplines-and-palettes/kbroman-Talk_Graphs/` | <https://github.com/kbroman/Talk_Graphs> | Karl W. Broman (UW–Madison Biostatistics & Medical Informatics) | CC0-1.0 | `6152203a2d6191291f266af5aed8895927554da7` | `ReadMe.md`, `License.md`, `more_on_graphs.tex`, `topten.tex`, `plots_to_avoid.Rmd`, `R/*.R` (`24` core source files + `UPSTREAM_COMMIT.txt`; `R/rafa_data.csv` omitted) |

---

## 1. Economics, Finance, Management, and Quantitative Social Science

### 1.1 Paul Goldsmith-Pinkham — *Tips + Tricks with Beamer for Economists*
- **Citation**: Paul Goldsmith-Pinkham (Federal Reserve Bank of New York / Yale School of Management), *Tips + Tricks with Beamer for Economists* (Beamer source deck & slides).
- **Verified URLs**:
  - GitHub Repository: <https://github.com/paulgp/beamer-tips> (`HEAD`: `6c3e5e4c910e0fe5a57f353a4c4dc59aef41599b`, archived locally at `../upstream-skills/05-disciplines-and-palettes/paulgp-beamer-tips/slides.tex`)
  - Compiled Slide Deck: <https://paulgp.com/beamer_tips.pdf> (HTTP `200`)
- **Extracted Principles, Macros, and Verbatim Quotes (`slides.tex`)**:
  - **Widescreen Aspect Ratio (`16:9`)**: Uses `\documentclass[notes,11pt, aspectratio=169]{beamer}` (`slides.tex`, line 1). *"If you use 16:9 perspective, use an image on the side!"* (line 252); *"It's much more modern looking in 16:9"* (line 815).
  - **Line-Length & Wide-Spacing Discipline**: Defines `\newenvironment{wideitemize}{\itemize\addtolength{\itemsep}{10pt}}{\enditemize}` (line 117) to prevent text cramming:
    - *"That way you don't write too much text on a slide!"* (line 248)
    - *"Rule of thumb 1: 45-75 characters a line"* (line 249)
    - *"Rule of thumb 2: sentence on one line"* (line 250)
    - *"Better to make one point well on a slide / Than to overwhelm an audience with text"* (lines 269, 273)
  - **Colorblind-Safe Palette & Auditorium Contrast**: Explicitly warns *"The traditional red-blue colors are bad for those who are color blind"* (line 310) and defines an Okabe–Ito RGB palette in LaTeX (lines 65–68, 78):
    - `blue`: `RGB(0, 114, 178)` — primary structural/text accent (`frametitle`, `itemize item`)
    - `red`: `RGB(213, 94, 0)` — contrast and emphasis
    - `yellow`: `RGB(240, 228, 66)` — section `transitionframe` background
    - `green`: `RGB(0, 158, 115)` — secondary backup accent
    - `MyBackground`: `RGB(255, 253, 218)` — warm off-white background; *"Make your figures in R or Stata have the same background color (Or transparent)"* (lines 331–333); *"In large auditoriums, go black background with white text"* (line 335).
  - **Typography & Never Shrinking Font to Cram Text**: Uses sans-serif Lato (`\usepackage[default]{lato}`, line 12) with `mathpazo` math (`\usepackage{mathpazo}`, line 27) and strips Beamer navigation clutter (`\setbeamertemplate{navigation symbols}{}`, line 93):
    - *"Don't change the font size to fit the text / You're likely putting too much text if you do / There's really no excuse: If you need a busy slide, make it a backup / Then have a link, and click to it"* (lines 386–391).
    - *"Font size matters for graphs too! ... Things on your computer look too big but audience will thank you"* (lines 405, 437).
  - **Figures & Regression Tables**:
    - Figures: *"When possible, make graphic central"* (line 485). When stepping across specifications or effects via `\only<1>`, `\only<2>`, `\only<3>`, *"keep the similar axes"* (line 514).
    - Regression Tables: Uses `booktabs` (`\toprule`, `\cmidrule`, `\bottomrule`) inside `\makebox[\linewidth][c]{\begin{tabular}...}` without the floating `table` environment (lines 529–535). Highlights target estimates with TikZ overlay boxes (`\tikz[overlay,remember picture]`, lines 540–560) or reveals rows/columns with `\onslide`, adding: *"Just don't overuse it"* and *"If you haven't practiced, the clicking through slides will be artificial"* (lines 593, 621).
  - **Equations**: *"Don't overdo it when putting up equations (either regressions or theorems) / Try adding color and text to highlight the relevant formula"* — demonstrated via colored `\underbrace{...}_{\text{Reduced Form}}` and `\underbrace{...}_{\text{First Stage}}` on the Imbens & Angrist (1994) IV estimator (lines 769–774).
  - **Appendix & Hyperlinked Backup Buttons**: Uses `\usepackage{appendixnumberbeamer}` and `\appendix` so the main-talk frame counter stops at the final main slide, paired with `\hyperlink{label}{\beamergotobutton{...}}` (lines 39, 828–851).

### 1.2 Jesse M. Shapiro — *How to Give an Applied Micro Talk: Unauthoritative Notes*
- **Citation**: Jesse M. Shapiro (Harvard University; formerly Brown University), *How to Give an Applied Micro Talk: Unauthoritative Notes* (Lecture/seminar guide).
- **Verified URL**: <https://shapiro.scholars.harvard.edu/notes-and-lectures> (Author lecture notes portal; cited across NBER/Harvard/World Bank training syllabi and `hanlulong/econ-slides-skill`).
- **Extracted Principles and Verbatim Quotes**:
  - **Assume Audience Indifference & Win the Opening Window**: Assume your audience starts out indifferent to your topic; you have roughly 1–2 slides (the first few minutes) to make them care via a concrete fact, anecdote, or clear policy/welfare question.
    - Verbatim benchmark after the introduction: *"By now... the audience believes in your question, understands what you measure and how, [and] understands what you will do with your data and why. Otherwise... the talk is already over, you just don't know it."*
  - **Screen Space Equals Spoken Emphasis**:
    - Verbatim rule: *"Don't put anything on a slide you don't plan to talk about."*
    - Verbatim attention rule: *"While you are talking, some people are not listening. Instead they are looking at your slides."* Because listeners cannot flip back like paper readers, slides must be sparse enough to read instantly yet self-sufficient enough for a listener whose attention lapsed to catch back up.
  - **Map Economic Assumptions to Econometric Identification**: Explicitly state the target parameter, what economic question/welfare object it answers, and why institutional features justify the econometric identifying assumption.
  - **Disciplined Vulnerability Handling**: Pause deliberately to address the *primary* threat to validity and how sensitivity is assessed, rather than pre-empting every minor quibble, listing every failed specification, or getting bogged down in technical minutiae nobody in the room would ask about.

### 1.3 John H. Cochrane — *Writing Tips for Ph.D. Students* (§4 "Seminar Presentations")
- **Citation**: John H. Cochrane (University of Chicago Booth School of Business / Hoover Institution, Stanford University), *Writing Tips for Ph.D. Students* (2005), Section on Seminar Presentations, pp. 9–12.
- **Verified URL**: <https://faculty.wcas.northwestern.edu/mdo738/teaching/cochrane.pdf> (HTTP `200`).
- **Extracted Principles and Verbatim Quotes**:
  - **Cut Throat-Clearing Motivation & Literature Reviews; Lead with the Contribution**:
    - *"Most seminars are a disaster. They start with pointless motivation and policy implications, which the audience can't follow since we don't know the result. Then we get a long literature review, which is even more boring... Get to the #1 important contribution as fast as possible."*
    - *"You don't need any literature review or motivation in a seminar."*
  - **Pacing & Slide Digestibility**:
    - *"You have to leave slides up for a decent amount of time in order for people to digest them. That means you will not be able to put up 1 slide per minute!"*
  - **Memory Constraint Across Slides for Equations**:
    - *"People don't remember equations from one slide to the next."* Keep notation concrete and self-contained on the slide where it is used rather than expecting listeners to recall symbol definitions from ten slides earlier.
  - **Eliminate Self-Congratulatory Adjectives**:
    - *"Don't use adjectives to describe your work: 'striking results,' 'very significant' coefficients, etc. If the work merits adjectives, the world will give them to you."*

### 1.4 Monika Piazzesi, Rachael Meager, and AEA / CSWEP Seminar Guidelines
- **Citations & Verified URLs**:
  - Monika Piazzesi (Stanford University), *Tips on How to Avoid Disaster in Presentations*: <https://web.stanford.edu/~niederle/piazzesi.pdf> (HTTP `200`).
  - Rachael Meager (LSE / UNSW), *Public Speaking for Academic Economists*: <https://sites.google.com/view/rachaelmeager>.
  - American Economic Association (AEA) / CSWEP Presentation & Seminar Advice: <https://www.aeaweb.org/about-aea/committees/cswep>.
- **Extracted Principles and Verbatim Rules**:
  - **The Cross-Subfield Intelligibility Test (Piazzesi)**: Design the setup and main-result slides so that a smart economist from a *different* subfield can follow the question, mechanism, and headline result.
  - **Define Every Symbol Shown (Piazzesi)**: *"Explain every symbol on your slides."* Never flash an equation and wave past undefined parameters; state the marginal contribution relative to the closest 1–2 papers rather than reciting a survey.
  - **Seminar Time & Slide Budget (Piazzesi / CSWEP)**: In a 75-minute economics seminar, budget 45–50 minutes of prepared speech (roughly 15–25 slides) to accommodate 25–30 minutes of live interruptions.
  - **Economic Magnitudes Over Regression Walls (Piazzesi / AEA)**: Never project a 17-column regression table copied straight from the paper. Show only the columns and coefficients you verbally interpret, and translate estimates into economic units (*"If X increases by one standard deviation, Y changes by..."*).
  - **No Apologetic Framing & Direct Vocal Projection (Meager / CSWEP)**: Do not open by apologizing for data limits or unfinished extensions; face the room rather than reading off the projection screen.

### 1.5 Marc F. Bellemare — *22 Tips for Conference and Seminar Presentations*
- **Citation**: Marc F. Bellemare (University of Minnesota), *"22 Tips for Conference and Seminar Presentations"*, *Agricultural Economics—Without Apology* (April 2014; updated edition).
- **Verified URLs**: <https://marcfbellemare.com/wordpress/10053> and <https://marcfbellemare.com/wordpress/12797>.
- **Extracted Principles and Verbatim Quotes**:
  - **No Murder Mysteries — Preview Results Early**:
    - *"This isn't a murder mystery: it's only when people know where you're taking them that they can enjoy the scenery along the way."*
  - **Keith Head's Introduction Formula**: Structure the opening around Hook, Research Question, Antecedents (minimal), Value Added, and Roadmap, skipping standalone multi-slide literature reviews.
  - **Strict Time Matching**: Calibrate slide count to the exact session format (short conference slot vs. full departmental seminar) and maintain a conversational, unmemorized spoken delivery without reading slides verbatim.

### 1.6 Jonathan A. Schwabish — *An Economist's Guide to Visualizing Data*
- **Citation**: Jonathan A. Schwabish, *"An Economist's Guide to Visualizing Data"*, *Journal of Economic Perspectives* 28(1): 209–234 (Winter 2014), `doi:10.1257/jep.28.1.209`; expanded in *Better Presentations: A Guide for Scholars, Researchers, and Wonks* (Columbia University Press, 2016).
- **Verified URL**: <https://www.aeaweb.org/articles?id=10.1257/jep.28.1.209> (HTTP `200`).
- **Three Core Visualization Principles (Verbatim)**:
  1. **Show the data**: Maximize data focus and display the underlying distribution/patterns honestly rather than obscuring them behind summary chrome.
  2. **Reduce the clutter**: Strip heavy gridlines, redundant tick labels, dark shading, pseudo-3D effects, and separate legends that impede pre-attentive visual processing.
  3. **Integrate the text and the graph**: Place direct line labels, callouts, and active takeaway titles onto or immediately beside the plotted series so the audience's eyes never bounce between a legend and the data.

### 1.7 Hanlu Long — `hanlulong/econ-slides-skill` (Open-Source Synthesis of Economics Talk Norms)
- **Citation**: Hanlu Long, *Econ Slides Skill* (`OpenEconAI`), MIT License.
- **Verified URL**: <https://github.com/hanlulong/econ-slides-skill> (`HEAD`: `82bc4bb81e729076e9ed71c406c0a3712a59c6b0`, archived locally at `../upstream-skills/05-disciplines-and-palettes/hanlulong-econ-slides-skill/`).
- **Extracted Operational Rules (`skills/econ-slides/references/slide-rules.md`)**:
  - **Single-Column Default**: Draft frames in one reading column by default; use two columns *only* for simultaneous comparisons (paired panels, before/after, data vs. model, treated vs. control).
  - **Bullet & Line Discipline**: 1–4 top-level bullets per text frame, no third nesting level, no mechanical arrow bullets (`\item[$\Rightarrow$]`), and one rendered line per title/bullet whenever possible without shrinking global slide font size.
  - **Deck-Wide Concept Color Ledger**: Assign at most ≤ 3 active Okabe–Ito concept colors across a slide (`cTreat`, `cModel`, etc.) and hold each concept's color invariant across every equation, bullet, and figure in the deck.
  - **Handout-Safe Overlays**: Tag `\only` swaps as `\only<1|handout:0>{build}\only<2|handout:1>{final}` so `[handout]` compilation never overprints frames; avoid decorative `\pause` chains.

---

## 2. Biomedical, Life Sciences, and Chemistry

### 2.1 Philip E. Bourne — *Ten Simple Rules for Making Good Oral Presentations*
- **Citation**: Philip E. Bourne (University of California San Diego), *"Ten Simple Rules for Making Good Oral Presentations"*, *PLOS Computational Biology* 3(4): e77 (2007), `doi:10.1371/journal.pcbi.0030077`.
- **Verified URLs**:
  - Journal Article (Open Access CC-BY): <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030077> (HTTP `200`)
  - PubMed Central: <https://pmc.ncbi.nlm.nih.gov/articles/PMC1857815/>
- **All Ten Rules (Verbatim Rule Headings Extracted from PLOS JATS XML)**:
  1. **Rule 1: Talk to the Audience** — Pitch background and depth to who is actually in the room rather than reciting your own lab notes.
  2. **Rule 2: Less is More** — Overloading slides with dense text and tangential sub-experiments loses listeners; concision leaves room for productive Q&A.
  3. **Rule 3: Only Talk When You Have Something to Say** — Present coherent findings or well-formulated problems rather than premature filler.
  4. **Rule 4: Make the Take-Home Message Persistent** — If an attendee remembers your core takeaway a week later, the talk succeeded; reinforce that central message repeatedly.
  5. **Rule 5: Be Logical** — Treat the talk as a structured story with clear causal transitions from question to method, result, and implication.
  6. **Rule 6: Treat the Floor as a Stage** — Presentations combine rigorous science with live delivery, presence, and audience engagement.
  7. **Rule 7: Practice and Time Your Presentation** — Rehearse aloud under realistic timing constraints; never overrun the allotted slot.
  8. **Rule 8: Use Visuals Sparingly but Effectively** — Roughly 1 slide per minute as an upper bound; avoid gratuitous animations and text walls, favoring self-explanatory diagrams/plots.
  9. **Rule 9: Review Audio and/or Video of Your Presentations** — Audit your own recorded talks to eliminate verbal tics, pacing errors, and cluttered slides.
  10. **Rule 10: Provide Appropriate Acknowledgments** — Credit genuine collaborators and funding clearly without letting a marathon acknowledgment reel consume closing momentum.

### 2.2 Thomas C. Erren & Philip E. Bourne — *Ten Simple Rules for a Good Poster Presentation*
- **Citation**: Thomas C. Erren & Philip E. Bourne, *"Ten Simple Rules for a Good Poster Presentation"*, *PLOS Computational Biology* 3(5): e102 (2007), `doi:10.1371/journal.pcbi.0030102`.
- **Verified URL**: <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030102> (HTTP `200`).
- **All Ten Rules (Verbatim Rule Headings Extracted from PLOS JATS XML)**:
  1. **Rule 1: Define the Purpose**
  2. **Rule 2: Sell Your Work in Ten Seconds**
  3. **Rule 3: The Title Is Important**
  4. **Rule 4: Poster Acceptance Means Nothing**
  5. **Rule 5: Many of the Rules for Writing a Good Paper Apply to Posters, Too**
  6. **Rule 6: Good Posters Have Unique Features Not Pertinent to Papers** (visual hierarchy from a distance, minimal prose blocks, graphical flow)
  7. **Rule 7: Layout and Format Are Critical**
  8. **Rule 8: Content Is Important, but Keep It Concise**
  9. **Rule 9: Posters Should Have Your Personality**
  10. **Rule 10: The Impact of a Poster Happens Both During and After the Poster Session**

### 2.3 Susan K. McConnell — *Designing Effective Scientific Presentations* (Stanford Biology / iBiology)
- **Citation**: Susan K. McConnell (Department of Biology, Stanford University), *Designing Effective Scientific Presentations* (iBiology Professional Development Lecture).
- **Verified URL**: <https://www.ibiology.org/professional-development/designing-effective-scientific-presentations/> (HTTP `200`).
- **Extracted Slide Design & Delivery Principles**:
  - **Sans-Serif Typography at High Legibility**: Use clean sans-serif typefaces (Arial, Helvetica, Trebuchet) at 28–44 pt rather than serif fonts (e.g., Times New Roman), whose thin terminal strokes blur on projection screens.
  - **Colorblind Accessibility & Venue-Calibrated Contrast**: Never rely on red–green or red–blue pairings (which fail for deuteranopic/protanopic viewers in fluorescence microscopy and heatmaps); use high-contrast accessible pairs such as blue and yellow. Maintain consistent background polarity across the entire deck (dark backgrounds reduce glare in large darkened lecture halls; light backgrounds suit well-lit seminar rooms).
  - **One Main Idea per Slide & Progressive Disclosure**: Restrict every slide to a single takeaway; build multi-step biological pathways or experimental schematics incrementally with clean, non-distracting appearances rather than dumping complex multi-panel journal figures onto one slide.
  - **Narrative Arc & "Home Slides"**: Organize around a scientific story (question -> experimental test -> discovery) rather than a chronological lab log, returning to an anchor "home slide" at major transitions to keep listeners oriented.

### 2.4 Uri Alon — *How To Give a Good Talk* (*Molecular Cell*)
- **Citation**: Uri Alon (Weizmann Institute of Science), *"How To Give a Good Talk"*, *Molecular Cell* 36(2): 165–167 (October 2009), `doi:10.1016/j.molcel.2009.11.006`.
- **Verified URLs**: <https://pubmed.ncbi.nlm.nih.gov/19854123/> and <https://doi.org/10.1016/j.molcel.2009.11.006>.
- **Extracted Principles**:
  - **Single Core Premise**: Distill the entire talk into one overarching premise sentence before making slides.
  - **Full-Sentence Assertion Titles**: Write every slide title as a complete declarative sentence stating that slide's scientific conclusion (not a topic label like *"Western blot"* or *"Experiment 2"*).
  - **Dramatic Story Structure**: Frame the introduction around a clear gap/conflict in biological understanding so the experimental design and result land as its resolution.
  - **Q&A Emotional Decoupling**: Listen past hostile or tense phrasing and respond calmly to the underlying scientific content of the question.

### 2.5 Jean-luc Doumont — *Effective Oral Presentations* (*Nature Education* / Scitable)
- **Citation**: Jean-luc Doumont (Principiae; author of *Trees, Maps, and Theorems: Effective Communication for Rational Minds*, 2009), *"Effective Oral Presentations"*, *Scitable by Nature Education* (2010).
- **Verified URL**: <https://www.nature.com/scitable/topicpage/effective-oral-presentations-13906743/> (HTTP `200`).
- **Extracted Principles**:
  - **Assertion–Evidence Slide Architecture**: Replace generic noun-phrase headers with assertive full-sentence takeaway titles paired directly with visual evidence (a clean plot, schematic, or image) rather than bulleted prose lists.
  - **Zero Zero-Information Ink**: Remove repeated institutional logos, decorative borders, and background textures so 100% of visual contrast serves the message and minimizes audience cognitive load.

### 2.6 Jeffrey T. Leek — *The Leek Group Guide to Giving Talks* (Computational Biology & Biostatistics)
- **Citation**: Jeffrey T. Leek (Johns Hopkins Bloomberg School of Public Health / Fred Hutchinson Cancer Center), *The Leek Group Guide to Giving Talks*.
- **Verified URL**: <https://github.com/jtleek/talkguide> (`HEAD`: `e8744b0d5bbb27bc9bf9d96dfe59eafbb34187e1`, archived locally at `../upstream-skills/05-disciplines-and-palettes/jtleek-talkguide/README.md`).
- **Extracted Rules and Verbatim Quotes (`README.md`)**:
  - **Purpose of Scientific Talks**: *"As a scientist, it is hard to accept that the primary purpose of a talk is advertising, not science... There is __no way__ to convey any reasonably complicated scientific idea completely in an hour. If you entertain people __they might go read your paper/use your code__"* (lines 28–33).
  - **Ordered Explanatory Pipeline**:
    1. *"__Always lead with a brief, understandable to everyone statement of your problem__."* (line 63)
    2. *"Explain the data and measurement technology before you explain the features you will use"* (line 64)
    3. *"Explain the features you will use to model data before you explain the model"* (line 65)
    4. *"When presenting results, make sure you are telling a story."* (line 66)
  - **Typography & Figures**:
    - *"Fonts can never be too big. Go huge. Small fonts will be met with anger."* (line 78)
    - *"All figures should have big axes in plain English."* (line 82)
    - *"Pictures beat words by a ratio of 1000 to 1."* (line 85)
  - **Three-Step Spoken Walkthrough for Every Figure** (lines 94–96):
    1. State what the figure communicates (*"this figure shows our method has higher accuracy"*).
    2. State the axes (*"the y-axis is sensitivity the x-axis is 1-specificity"*).
    3. State the visual pattern to look for (*"curves that go straight up at zero and across the top of the plot are best"*).
  - **Equations in Computational Biology / Stats Talks** (lines 104–111):
    - Explain the data *before* showing any equation.
    - *"Whenever possible use words instead of symbols in equations (_Expression = Noise + Signal_ is better than _E = N + S_ is better than _Y = X + E_)"*.
    - *"No more than two subscripts"*.
  - **Job Talks & Time Discipline**: Present brief bookend summaries of your broader research program at the start and end, *"__But only talk about one specific project when giving the talk__"* (line 119). Always finish on time; if earlier speakers ran over, cut material on the fly (*"The value you gain by making your audience happy >>>> the extra 5 minutes of details"*, line 153).

### 2.7 Prashant V. Kamat (*ACS Energy Letters*) & American Chemical Society (ACS) Oral Presentation Guides
- **Citations & Verified URLs**:
  - Prashant V. Kamat (University of Notre Dame; Editor-in-Chief, *ACS Energy Letters*), *"Are You Making the Right Presentation at the Scientific Meeting?"*, *ACS Energy Letters* 2(2): 408–409 (2017), `doi:10.1021/acsenergylett.7b00014` (<https://doi.org/10.1021/acsenergylett.7b00014>).
  - American Chemical Society (ACS), *Mastering the Art of Scientific Publication and Presentation* / *inChemistry* Oral Presentation Guidelines (<https://www.acs.org/>).
- **Extracted Chemistry Presentation Rules**:
  - **No Supporting-Information Data Dumps**: Never paste raw full-page NMR spectra, crowded chromatograms, or dense synthesis screening tables straight from a manuscript's Supporting Information; crop/zoom into the diagnostic ppm region or catalytic cycle and enlarge chemical structure labels for ballroom legibility.
  - **25-Word Big-Picture Anchor**: Open by answering *What chemical problem are you solving?* and *Why does it matter?* before detailing synthetic routes, kinetics, or characterization.
  - **15-Minute ACS Contributed Talk Discipline**: Edit ruthlessly for standard 15-minute ACS division slots (12 minutes speaking + 3 minutes Q&A) so mechanistic conclusions are never rushed.

---

## 3. Mathematics, Statistics, and Theoretical Sciences

### 3.1 Paul R. Halmos — *How to Talk Mathematics* (*Notices of the AMS*, 1974)
- **Citation**: Paul R. Halmos, *"How to Talk Mathematics"*, *Notices of the American Mathematical Society* 21(3): 155–158 (April 1974).
- **Verified URL**: <https://faculty.washington.edu/heagerty/Courses/b572/public/HalmosHowToTalk.pdf> (HTTP `200`).
- **Extracted Principles and Verbatim Quotes**:
  - **Rhetorical Goal — Attract and Inform**:
    - *"What is the purpose of a public lecture? Answer: to attract and to inform... the purpose of a public lecture is to inform, but to do so in a manner that makes it possible for the audience to absorb the information."*
  - **Concrete Special Cases Over Abstract Generality**:
    - *"To prepare a talk, the first thing to know is the subject, and very close second is the audience."*
    - *"My recommendations amount to this: make it simple, organized and short. Make your lecture simple (special and concrete); be sure to prove something and ask something; prepare, in detail; organize the content and adjust to the level of the audience; keep it short... and remember that less is more."*
  - **Never Greet an Audience with a Wall of Formulas**:
    - *"Do not, ever, greet an audience with a carefully prepared blackboard (or overhead projector sheets) crammed with formulas, definitions, and theorems."*
  - **The "Walk in the Woods" Heuristic**: Explain definitions and theorems as if walking in the woods with a mathematician friend with no paper at hand—introducing heavy symbolic notation only where unavoidable.
  - **Rigorous Modular Preparation, Extemporaneous Delivery**:
    - *"Organize your public lecture, plan it, prepare it carefully, and then deliver it impromptu, extemporaneously."* Build the talk out of self-contained modules near the end that can be cleanly omitted without scrambling if time runs short.

### 3.2 Terence Tao — *Talks Are Not the Same as Papers*
- **Citation**: Terence Tao (Department of Mathematics, UCLA), *"Talks are not the same as papers"*, *What's New* (`terrytao.wordpress.com`).
- **Verified URL**: <https://terrytao.wordpress.com/career-advice/talks-are-not-the-same-as-papers/> (HTTP `200`).
- **Extracted Principles**:
  - **Never Convert Paper Pages Directly into Slides**: Unlike paper readers, talk listeners cannot flip back to check notation, technical hypotheses, or lemma numbers; cramming full formal statements and epsilon-delta bookkeeping onto slides guarantees losing the room.
  - **Present the Informal Meta-Story Omitted from the Paper**: Use the talk as a *complement* to the paper—conveying geometric/heuristic intuition, why naive approaches fail (false starts), how the proof strategy was discovered, and where the genuine novelty sits while glossing over routine technical estimates.
  - **Front-Load Accessible Toy Examples**: Dedicate the opening minutes to elementary examples and background context so non-specialists stay engaged and specialists gain a fresh conceptual framing before new theorems appear.

### 3.3 John E. McCarthy — *How to Give a Good Colloquium* (*CMS Notes* / AMS, 1999)
- **Citation**: John E. McCarthy (Washington University in St. Louis), *"How to Give a Good Colloquium"*, *Canadian Mathematical Society Notes* 31(5): 3–4 (September 1999); reprinted by the American Mathematical Society.
- **Verified URLs**: <https://www.ams.org/profession/leaders/workshops/gcoll.pdf> and <https://www.math.wustl.edu/~sk/books/newsurv.pdf> (HTTP `200`).
- **Eight Core Colloquium Rules (Extracted with Verbatim Rule-of-Thumb)**:
  1. **Don't be intimidated by experts in the audience**: Never pitch a department-wide colloquium exclusively to three subfield specialists in the front row or say *"I'm sure everybody here knows..."*.
  2. **Don't try to impress the audience with arcane brilliance**: Avoid dropping undefined jargon (e.g., Koszul complexes, bornology) prefaced by a false *"apology to the experts"* that freezes out 90% of the room.
  3. **Make the first 20 minutes accessible to first/second-year graduate students**.
  4. **Carry everyone along**: Pair formal definitions with informal geometric/intuitive descriptions and periodically zoom back out to the big picture.
  5. **Anchor abstract theory in concrete examples**.
  6. **Keep proofs ultra-short ("Prove only tautologies")**: Verbatim rule of thumb: *"Do not give a proof that exceeds 3 lines."* State main theorems under clean "nice" assumptions rather than burying the insight under pathological regularity conditions.
  7. **Put the theorem in context**: Explain why the result matters and how it connects to broader open problems across mathematics.
  8. **Watch the audience**: Monitor faces continuously and slow down or re-illustrate when eyes glaze over.

### 3.4 Gian-Carlo Rota — *Ten Lessons I Wish I Had Been Taught* (*Notices of the AMS*, 1997)
- **Citation**: Gian-Carlo Rota (MIT), *"Ten Lessons I Wish I Had Been Taught"*, *Notices of the American Mathematical Society* 44(1): 22–25 (January 1997).
- **Verified URL**: <https://www.ams.org/notices/199701/comm-rota.pdf>.
- **Extracted Principles and Verbatim Quotes**:
  - **One Point per Lecture**: Every mathematical lecture should communicate *one* central point, developed from multiple angles so listeners leave remembering that single idea permanently.
  - **Blackboard / Visual Surface Discipline (Verbatim)**:
    - *"a. Make sure the blackboard is spotless... By starting with a spotless blackboard you will subtly convey the impression that the lecture they are about to hear is equally spotless."*
    - *"b. Start writing on the top left-hand corner. What we write on the blackboard should correspond to what we want an attentive listener to take down in their notes."*

### 3.5 Karl W. Broman — *Creating Effective Figures and Tables / Plots to Avoid* (Statistics)
- **Citation**: Karl W. Broman (Department of Biostatistics & Medical Informatics, University of Wisconsin–Madison), *Talk_Graphs* (`more_on_graphs.tex`, `plots_to_avoid.Rmd`, `topten.tex`), CC0-1.0.
- **Verified URLs**: <https://github.com/kbroman/Talk_Graphs> (`HEAD`: `6152203a2d6191291f266af5aed8895927554da7`, archived locally at `../upstream-skills/05-disciplines-and-palettes/kbroman-Talk_Graphs/`) and <https://kbroman.org/topten_worstgraphs/>.
- **Nine Summary Rules for Statistical Graphics in Talks (Verbatim from `more_on_graphs.tex`, lines 537–554)**:
  1. *"Put the things to be compared next to each other"*
  2. *"Use color to set things apart, but consider color blind folks"*
  3. *"Use position rather than angle or area to represent quantities"*
  4. *"Align things vertically to ease comparisons"*
  5. *"Use common axis limits to ease comparisons"*
  6. *"Use labels rather than legends"*
  7. *"Sort on meaningful variables (not alphabetically)"*
  8. *"Must 0 be included in the axis limits?"* (question automatic zero-baselines when small relative differences matter)
  9. *"Consider taking logs and/or differences"* (e.g., Bland–Altman / MA difference-vs-average plots rather than raw correlation scatterplots that mask 2-fold error)
- **Statistical Display Anti-Patterns to Eliminate (`plots_to_avoid.Rmd`)**:
  - Pie charts and donut plots (human vision judges linear position/length accurately, not angles or areas).
  - "Dynamite" barplots of group means with SE "antennas" (hide sample distribution, skewness, and outliers; replace with dotplots/stripcharts or boxplots, and scatterplots/slopegraphs for paired data).
  - Regression lines plotted without the underlying data scatter.
  - Gratuitous pseudo-3D bars/curves and raw unrounded software output (*"In tables, every digit should be meaningful. Don't drop ending 0's"*, `plots_to_avoid.Rmd`, line 323).

---

## 4. Computer Science, Systems, and Engineering

### 4.1 David A. Patterson — *How to Give a Bad Talk* (The Ten Commandments, UC Berkeley CS)
- **Citation**: David A. Patterson (Computer Science Division, University of California, Berkeley; 2017 ACM A.M. Turing Award Laureate), *How to Give a Bad Talk* (circa 1983), with annotations recorded by Mark D. Hill.
- **Verified URL**: <https://pages.cs.wisc.edu/~markhill/conference-talk.html#badtalk> (HTTP `200`, scraped directly).
- **All Ten Commandments (Verbatim)**:
  1. **I. Thou shalt not be neat** — *"Why waste research time preparing slides? Ignore spelling, grammar and legibility. Who cares what 50 people think?"*
  2. **II. Thou shalt not waste space** — *"Transparencies are expensive. If you can save five slides in each of four talks per year, you save $7.00/year!"* (Irony: cramming slides instead of using generous whitespace.)
  3. **III. Thou shalt not covet brevity** — *"Do you want to continue the stereotype that engineers can't write? Always use complete sentences, never just key words. If possible, use whole paragraphs and read every word."*
  4. **IV. Thou shalt cover thy naked slides** — *"You need the suspense! Overlays are too flashy."* (Critiquing mechanical paper/strip-covering of overhead slides to manufacture artificial suspense.)
  5. **V. Thou shalt not write large** — *"Be humble -- use a small font. Important people sit in front. Who cares about the riff-raff?"*
  6. **VI. Thou shalt not use color** — *"Flagrant use of color indicates uncareful research. It's also unfair to emphasize some words over others."*
  7. **VII. Thou shalt not illustrate** — *"Confucius says 'A picture = 10K words,' but Dijkstra says 'Pictures are for weak minds.' Who are you going to believe? Wisdom from the ages or the person who first counted goto's?"*
  8. **VIII. Thou shalt not make eye contact** — *"You should avert eyes to show respect. Blocking screen can also add mystery."*
  9. **IX. Thou shalt not skip slides in a long talk** — *"You prepared the slides; people came for your whole talk; so just talk faster. Skip your summary and conclusions if necessary."*
  10. **X. Thou shalt not practice** — *"Why waste research time practicing a talk? It could take several hours out of your two years of research. How can you appear spontaneous if you practice? If you do practice, argue with any suggestions you get and make sure your talk is longer than the time you have to present it."*
  - **Closing Maxim**: *"Commandment X is most important. Even if you break the other nine, this one can save you."*

### 4.2 Mark D. Hill — *Oral Presentation Advice* (UW–Madison CS Systems Architecture)
- **Citation**: Mark D. Hill (Computer Sciences Department, University of Wisconsin–Madison), *Oral Presentation Advice* (April 1992; revised January 1997).
- **Verified URL**: <https://pages.cs.wisc.edu/~markhill/conference-talk.html> (HTTP `200`, scraped directly).
- **Extracted Principles & Generic 20-Minute CS Conference Talk Budget (~12 Slides at ~2 Min/Slide)**:
  - **Core Heuristic**: K.I.S.S. (1–3 key points max) + Forecast–Body–Summary (*"tell them what you're going to tell them (Forecast), tell them, and tell them what you told them (Summary)"*). Pitch the Forecast and Summary to everyone; pitch the body to sub-area experts.
  - **20-Minute CS Conference Slide Allocation**:
    - Title / Author / Affiliation: `1` slide
    - **Forecast**: `1` slide — *"Give gist of problem attacked and insight found (What is the one idea you want people to leave with? This is the 'abstract' of an oral presentation.)"*
    - Outline: `1` slide
    - Motivation & Problem Statement: `1–2` slides (*"Most researchers overestimate how much the audience knows about the problem they are attacking."*)
    - Related Work: `0–1` slides (*"Cover superficially or omit; refer people to your paper."*)
    - Methods: `1` slide
    - **Results**: `4–6` slides (*"Do not superficially cover all results; cover key result well. Do not just present numbers; interpret them to give insights. Do not put up large tables of numbers."*)
    - Summary: `1` slide; Future Work: `0–1` slides; Backup Slides: `0–3` uncounted slides.
  - **CS Faculty Job Talk Algorithm**: Start from a 20-minute conference talk -> expand the 5-minute introduction into **20 minutes** accessible to the entire CS department -> present core results -> add **10 minutes** of thesis depth for sub-area faculty -> return to a broadly accessible summary -> add **10 minutes** surveying broader research breadth -> reserve **5 minutes** for questions.

### 4.3 Jonathan Richard Shewchuk — *Giving an Academic Talk* (UC Berkeley EECS)
- **Citation**: Jonathan Richard Shewchuk (Department of Electrical Engineering and Computer Sciences, UC Berkeley), *Giving an Academic Talk*.
- **Verified URL**: <https://people.eecs.berkeley.edu/~jrs/speaking.html> (HTTP `200`, scraped directly).
- **Extracted Rules and Verbatim Quotes**:
  - **The 12-Word Ceiling & Visual-First Mandate**:
    - *"If you want to be a great speaker, you must first accept the fact that a slide with more than twelve words on it is usually counterproductive."*
    - *"First, your new modus operandi is to express all your ideas in pictures. Resort to text only where illustrations fail you. As an exercise, try to make a talk where the only text is the slide titles, and perhaps a few two-word labels on figures."*
    - *"Today, speakers project their index cards (as a list of bullet points) and make their audiences read them. Please understand that this is a hostile act."*
  - **Concrete Typography, Margin, Chrome, and Formula Rules**:
    - *"I use 38 point text and 42–50 point titles."*
    - *"Projected slides, unlike printed documents, do not need margins."*
    - *"Use only sans-serif fonts. They're easier to see from the back of the room. (Exception: math fonts usually have serifs.)"*
    - *"Some people put accretions like project logos, the talk title, and the conference name on every page. Don't."*
    - *"For slides with formulae, one of my favorite tricks is to add arrows and labels pointing to the variables in a formula, reminding the audience what each one means. Few people will remember nomenclature that you defined on a previous slide."*
  - **Two-Part Novelty Question & The Onion vs. Clew Model**:
    - Answer *both* parts of novelty: (1) *"What does your method accomplish that no previous method accomplishes?"* and (2) *"What algorithmic or methodological idea enables your method to accomplish more?"*
    - **Onion Model vs. Clew Model** (quoting Herman Haverkort): Linear "clew" talks lose listeners permanently the moment they miss one slide; an **onion talk** *"starts with the main message, and adds depth in successive layers around it, always returning to the main message between layers."*
  - **Slide Title Audit & Delivery Mechanics**:
    - *"When audience members wake up mid-talk and try to pay attention again, the first thing they'll do is look at your current slide's title. Make sure it tells them why you're babbling on about grommets right now."*
    - **Pointers**: Prefer a physical telescoping pointer; if using a laser pointer, *hold it steady* rather than circling frantically, and never point with the laptop mouse cursor.
    - **Laptop Gaze Trap**: Place the laptop where you cannot stare at it; look at the projection screen only when directing the audience's eyes there, and look at the audience when you want them listening to your voice.
    - **Articulate Silence & Zero Meta-Commentary**: *"Silence can be articulate. Leave a long pause right after making a key point... Demand your right to remain silent."* Never say *"I guess I'm running out of time; I'll just go through this quickly"* — silently skip to land cleanly, and end explicitly with *"Thank you"* to cue applause before Q&A.

### 4.4 Kayvon Fatahalian — *Tips for Giving Clear Talks* (Stanford CS)
- **Citation**: Kayvon Fatahalian (Department of Computer Science, Stanford University; formerly Carnegie Mellon University), *Tips for Giving Clear Talks*.
- **Verified URL**: <https://graphics.stanford.edu/~kayvonf/misc/cleartalktips.pdf> (HTTP `200`).
- **Extracted Principles and Verbatim Maxims**:
  - **"Every sentence matters"**: Cut any spoken or visual element whose concrete benefit to the listener cannot be justified.
  - **"The audience prefers not to think"** (about bookkeeping or implicit leaps you can state plainly).
  - **"Surprises are bad: Say *why* before *what*"**: Always motivate *why* a component, design choice, or graph is needed *before* showing its mechanism.
  - **"One point per slide, and the point is the title of the slide"**: Replace passive topic headers (*"Results"*) with quantitative claim headers (*"Method X reduces rendering latency by 2x"*) so listeners immediately know what claim the graph proves.
  - **Structured Graph Walkthrough**: (1) State the question the graph answers -> (2) Define the axes -> (3) Walk directly to the single takeaway trend.

### 4.5 Simon Peyton Jones (*How to Give a Great Research Talk*) & Patrick H. Winston (*How to Speak*, MIT)
- **Citations & Verified URLs**:
  - Simon Peyton Jones (Microsoft Research / Epic Games / University of Cambridge), *How to Give a Great Research Talk*: <https://simon.peytonjones.org/great-research-talk/> (HTTP `200`).
  - Patrick H. Winston (MIT CSAIL), *How to Speak* (MIT OpenCourseWare `RES.TLL-005`): <https://ocw.mit.edu/courses/res-tll-005-how-to-speak-january-iap-2018/> (HTTP `200`).
- **Extracted Principles**:
  - **20% Motivation / 80% One Key Idea — Narrow & Deep (Peyton Jones)**: A research talk is a "taster" to make listeners eager to read the paper. Omit upfront outline slides and upfront related-work surveys; teach your core technical idea via worked concrete examples rather than abstract generalities.
  - **Empowerment Promise & Single Language Processor (Winston)**: Open with an *empowerment promise* (what listeners will understand/do afterward) rather than a joke. Humans have only one language processor—if slides carry dense text, listeners read and stop hearing you (*"slides are seasoning, not the main course"*).
  - **Winston's Star & The Contributions Closing Slide (Winston)**: Anchor memory with five S's (**Symbol**, **Slogan**, **Surprise**, **Salient Idea**, **Story**), and *never* leave a useless *"Thank You / Questions?"* slide projected during Q&A—keep a **Contributions** slide on screen so the audience stares at your core achievements throughout the discussion.

---

## 5. Humanities, History, Literary Studies, and Qualitative Research

### 5.1 Linda K. Kerber — *Conference Rules: Everything You Need to Know about Presenting a Scholarly Paper in Public* (AHA)
- **Citation**: Linda K. Kerber (University of Iowa; 2006 President of the American Historical Association), *"Conference Rules: Everything You Need to Know about Presenting a Scholarly Paper in Public"*, *The Chronicle of Higher Education* (March 2008); reprinted in *Perspectives on History* (American Historical Association, May 2008).
- **Verified URL**: <https://www.historians.org/perspectives-article/conference-rules-everything-you-need-to-know-about-presenting-a-scholarly-paper-in-public-may-2008/>.
- **Extracted Humanities Orality & Panel Rules (with Verbatim Quotes)**:
  - **Writing for the Ear vs. Writing for the Eye**:
    - *"A paper written for the ears to hear must be substantially different from a paper written for the eyes to read."* Listeners cannot re-read complex subordinate clauses, skim footnotes, or recover once lost in dense archival prose.
  - **Prepared Naturalness (Quoting Dorothy Kenyon)**:
    - A public talk must *"always seem to be improvised, but it must never be improvised."*
  - **Scrupulous Word-Count & Clock Math**: One standard double-spaced page (~250 words) equals ~2 minutes of clear oral delivery; a 15–20 minute humanities panel slot strictly caps a spoken text at **8–10 double-spaced pages** (2,000–2,500 words). Overrunning steals time from fellow panelists, commentators, and audience Q&A.
  - **Harnessing Adrenaline**:
    - *"Without adrenaline you will be a boring speaker. But too much anxiety will get in the way of what you have to do."* Rehearse aloud, inspect the room and lectern ahead of time, avoid physical fidgeting, and resist unscripted tangents that blow the clock.

### 5.2 American Historical Association (AHA) — *Tips for Presenting a Paper at the Annual Meeting*
- **Citation**: American Historical Association, *"Tips for Presenting a Paper at the Annual Meeting"*, *Perspectives on History* (December 2012).
- **Verified URL**: <https://www.historians.org/perspectives-article/tips-for-presenting-a-paper-at-the-annual-meeting-december-2012/>.
- **Extracted Principles**:
  - **Break the Verbatim Reading Habit**: Prefer speaking from structured outlines or specially formatted oral scripts (large font, wide spacing, breathing/emphasis cues) rather than reading a journal manuscript head-down.
  - **Primary Visual Sources Over Prose Slides**: In historical and qualitative presentations, slides should showcase primary visual evidence—maps, archival photographs, manuscripts, political cartoons, material culture—not walls of secondary historiographical prose or multi-paragraph block quotes.
  - **Cut Historiographical Throat-Clearing**: Present *one* clear historical intervention backed by vivid primary evidence, framing the opening so both subfield specialists and broader historians grasp the stakes.

### 5.3 Modern Language Association (MLA) — *Access Guidelines* & Farr and Lau (*Profession*)
- **Citations & Verified URLs**:
  - Modern Language Association (MLA), *Access Guidelines for MLA Convention Session Organizers and Presenters*: <https://www.mla.org/Events/Planning-a-Convention-Session/Access-Guidelines-for-MLA-Convention-Session-Organizers-and-Presenters> (HTTP `200`).
  - Jason S. Farr & Travis Chi Wing Lau, *"Toward a More Accessible Conference Presentation"*, *Profession* (Modern Language Association): <https://profession.mla.org/toward-a-more-accessible-conference-presentation/> (HTTP `200`).
- **Extracted Humanities Slide, Handout, and Accessibility Standards (with Verbatim Quote)**:
  - **Foundational Access Principle (Farr & Lau)**:
    - *"Able-bodiedness should not be a prerequisite for conference participation. If conferences are centered on the sharing of ideas, then access is the key to creating inclusive communities that help facilitate this fundamental aspect of our profession."*
  - **Six-Line Slide Cap & Sans-Serif Typography**:
    - Never exceed **6 lines of text per slide**; split long literary or archival block quotations across sequential slides rather than shrinking text (Farr & Lau).
    - Minimum **18 pt** font (**24 pt+** strongly recommended) in clean sans-serif faces (Arial, Calibri, Verdana); avoid italics blocks, underlining, all-caps, low-contrast palettes, or free-floating text boxes without unique slide titles for screen readers (MLA Access Guidelines).
  - **Verbal Image Descriptions**: Verbally describe every non-decorative image, archival facsimile, or chart in spoken delivery—and factor those descriptions into rehearsal timing.
  - **Large-Print & Digital Access Copies**: Bring printed large-print script/quote handouts (16–18 pt, double-spaced) and/or share a digital link/QR code (e.g., Humanities Commons / CORE) before beginning, plus advance copies for ASL interpreters.
  - **Microphone & Pacing Etiquette**: Always use the microphone without asking *"Can everyone hear me without the mic?"*, and speak at a measured pace (~120–130 wpm) so non-native listeners, ASL interpreters, and live auto-captioning keep pace.

### 5.4 Paul N. Edwards — *How to Give an Academic Talk* (History of Technology / STS / Qualitative Research)
- **Citation**: Paul N. Edwards (School of Information, University of Michigan / Program in Science, Technology & Society, Stanford University), *How to Give an Academic Talk, v5.2*.
- **Verified URL**: <https://pne.people.si.umich.edu/PDF/howtotalk.pdf> (HTTP `200`).
- **Extracted Principles and Verbatim Contrasts**:
  - **Critique of "Giving a Paper"**:
    - *"Presentations are not journal articles. They are a completely different medium of communication, and they require a different set of skills."* Treating an oral slot as "reading a paper" hides the scholar behind written armor at the audience's expense.
  - **Three Simultaneous Obligations**: (1) *Communicate* arguments and evidence, (2) *Persuade* the audience they hold, and (3) *Engage and entertain* tired conference listeners.
  - **"Usually Better vs. Usually Worse" Delivery Matrix (Verbatim Pairs)**:
    - *Talk* vs. *Read*
    - *Stand* vs. *Sit*
    - *Move* vs. *Stand still*
    - *Vary the pitch of your voice* vs. *Speak in a monotone*
    - *Speak loudly and clearly, toward the audience* vs. *Mumble, facing downward*
    - *Make eye contact* vs. *Stare at your notes, the floor, or the screen*
  - **Five-Minute "Idea Units" & Decisive Endings**: Structure talks around ~5-minute conceptual "idea units" anchored by visual evidence and clear titles rather than bullet-point teleprompters, and craft an intentional closing cadence (*"Talks need a sense of an ending. You'll develop your own style of doing this. Make it."*).
