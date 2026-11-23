# Published Empirical LLM Excess-Vocabulary Studies & Classic Prose Rules (Verbatim Primary Archive)

> **Source Authority & Provenance (100% Verbatim / Faithful Primary Material — Zero AI Self-Invention)**
> Every word list, statistical table, methodological formula, and prose rule in this archive is extracted directly from verified peer-reviewed publications, arXiv preprints, open-source research repositories, and authoritative primary essay archives:
> 1. **Kobak et al. (*Science Advances*, 2025)** — *Delving into LLM-assisted writing in biomedical publications through excess vocabulary* | DOI: [`10.1126/sciadv.adt3813`](https://doi.org/10.1126/sciadv.adt3813) | arXiv: [`2406.07016`](https://arxiv.org/abs/2406.07016) | GitHub: [`berenslab/llm-excess-vocab`](https://github.com/berenslab/llm-excess-vocab) (MIT License, commit `53db991afc251782106cd817a1c3fa47a4d41781`)
> 2. **Liang et al. (Stanford / ICML 2024)** — *Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews* | arXiv: [`2403.07183`](https://arxiv.org/abs/2403.07183) | DOI: [`10.48550/arXiv.2403.07183`](https://doi.org/10.48550/arXiv.2403.07183) | PMLR [`v235/liang24b`](https://proceedings.mlr.press/v235/liang24b.html)
> 3. **Liang et al. (Stanford / *Nature Human Behaviour*, 2025)** — *Mapping the Increasing Use of LLMs in Scientific Papers* (*Quantifying large language model usage in scientific papers*) | Journal DOI: [`10.1038/s41562-025-02273-8`](https://doi.org/10.1038/s41562-025-02273-8) | arXiv: [`2404.01268`](https://arxiv.org/abs/2404.01268) | GitHub: [`Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers`](https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers) (MIT License, commit `8defb86079a566e0196d2ab0cc88ff9823d25813`)
> 4. **Andrew Gray (University College London, 2024)** — *ChatGPT "contamination": estimating the prevalence of LLMs in the scholarly literature* | arXiv: [`2403.16887`](https://arxiv.org/abs/2403.16887) | DOI: [`10.48550/arXiv.2403.16887`](https://doi.org/10.48550/arXiv.2403.16887) | UCL Dataset DOI: [`10.5522/04/25471957`](https://doi.org/10.5522/04/25471957)
> 5. **Juzek & Ward (Florida State University / COLING 2025)** — *Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models* | ACL Anthology: [`2025.coling-main.426`](https://aclanthology.org/2025.coling-main.426/) | arXiv: [`2412.11385`](https://arxiv.org/abs/2412.11385) | GitHub: [`tjuzek/delve`](https://github.com/tjuzek/delve) (MIT-0 / CC0 1.0)
> 6. **George Orwell (*Horizon*, April 1946)** — *Politics and the English Language* | Primary Archive: [The Orwell Foundation](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/)
> 7. **Paul Graham (`paulgraham.com`, 2005–2025)** — [*Writing, Briefly*](https://paulgraham.com/writing44.html) (2005), [*Write Like You Talk*](https://paulgraham.com/talk.html) (2015), [*How to Write Usefully*](https://paulgraham.com/useful.html) (2020), [*Write Simply*](https://paulgraham.com/simply.html) (2021), [*Putting Ideas into Words*](https://paulgraham.com/words.html) (2022), [*Good Writing*](https://paulgraham.com/goodwriting.html) (2025)

---

# Part I: Published Empirical LLM Excess-Vocabulary & Stylometry Studies

## 1. Kobak, González-Márquez, Horvát, & Lause (*Science Advances*, 2025) — PubMed Excess Vocabulary

> **Verified Source Metadata**
> - **Authors:** Dmitry Kobak, Rita González-Márquez, Emőke-Ágnes Horvát, Jan Lause
> - **Title:** *Delving into LLM-assisted writing in biomedical publications through excess vocabulary* (originally circulated in preprint/repo links as `chatgpt-excess-words` / *Delving into ChatGPT usage in academic writing through excess vocabulary*)
> - **Publication:** *Science Advances*, Vol. 11, No. 27, eadt3813 (2 July 2025)
> - **DOI:** [https://doi.org/10.1126/sciadv.adt3813](https://doi.org/10.1126/sciadv.adt3813) | **PMID:** `40601754` | **PMC:** `PMC12219543`
> - **arXiv Preprint:** [https://arxiv.org/abs/2406.07016](https://arxiv.org/abs/2406.07016) (`arXiv:2406.07016v5`)
> - **GitHub Repository:** [https://github.com/berenslab/llm-excess-vocab](https://github.com/berenslab/llm-excess-vocab) (MIT License, Commit SHA: `53db991afc251782106cd817a1c3fa47a4d41781`; archived locally in `../upstream-skills/03-models-and-stylometry-data/berenslab-llm-excess-vocab/`)

### 1.1 Empirical Methodology & Core Findings (Verbatim from `arXiv:2406.07016v5`)

- **Corpus Scale:** Over 15 million biomedical abstracts indexed by PubMed from 2010–2024 (26.7K tracked words with annual occurrence frequency $> 10^{-4}$).
- **Counterfactual Excess Metrics:** For target year $Y$ with observed abstract frequency $p$, expected counterfactual frequency $q$ is extrapolated linearly from years $Y-3$ and $Y-2$:
  $$q = p_{-2} + 2 \cdot \max\{p_{-2} - p_{-3}, 0\}, \qquad r = \frac{p}{q}, \qquad \delta = p - q$$
  Excess words are defined by $\delta > 0.01$ or $\log_{10} r > \frac{\log_{10} 2}{4} \log_{10} p$.
- **Shift from Content Nouns to LLM Style Verbs & Adjectives:**
  > "Across all 26.7 K words, we found many with strong excess usage in 2024 (Figure 2). Less common words with strong excess usage included *delves* ($r=28.0$), *underscores* ($r=13.8$), and *showcasing* ($r=10.7$), together with their grammatical inflections (Figure 2a). More common words with strong excess usage included *potential* ($\delta=0.052$), *findings* ($\delta=0.041$), and *crucial* ($\delta=0.037$) (Figure 2b)."
  >
  > "The excess vocabulary during the Covid pandemic consisted almost entirely of content words (such as *respiratory*, *remdesivir*, etc.), whereas the excess vocabulary in 2024 consisted almost entirely of style words (Figure 3a)."
- **Lower-Bound Prevalence of LLM-Assisted Abstracts in 2024 (13.5% Overall):**
  - **10 Common Excess Style Words Set ($\Delta_{\text{common}} = 0.134$):**
    `across`, `additionally`, `comprehensive`, `crucial`, `enhancing`, `exhibited`, `insights`, `notably`, `particularly`, `within`
  - **291 Rare Excess Style Words Set ($p < 0.02$, $\Delta_{\text{rare}} = 0.136$):** Combined non-overlapping lower bound $\Delta = (\Delta_{\text{common}} + \Delta_{\text{rare}})/2 = 0.135$ (**13.5%** of all 2024 PubMed abstracts, i.e., $>200,000$ papers/year; reaching $\Delta = 0.25$ in *Sensors*, $0.21$ across MDPI, $0.20$ in *Cureus* and Frontiers, vs. $0.07$ in *Nature/Science/Cell*).

### 1.2 Empirical PubMed Word Trajectory Table (2010–2024, Verbatim from `results/figures_data/figure1.csv`)

> **Source File:** [`berenslab/llm-excess-vocab/results/figures_data/figure1.csv`](https://github.com/berenslab/llm-excess-vocab/blob/53db991afc251782106cd817a1c3fa47a4d41781/results/figures_data/figure1.csv) (Note how `delves`, `crucial`, `potential`, `these`, and `significant` surge in 2023–2024 while plain `important` drops from `0.123075` in 2022 to `0.098844` in 2024.)

| Year | delves | crucial | potential | these | significant | important | pandemic | ebola | convolutional |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2010 | 0.000014 | 0.016559 | 0.115363 | 0.356381 | 0.170088 | 0.119832 | 0.002621 | 0.000115 | 0.000019 |
| 2011 | 0.000019 | 0.017199 | 0.119109 | 0.353738 | 0.171803 | 0.121747 | 0.002869 | 0.000163 | 0.000007 |
| 2012 | 0.000016 | 0.017645 | 0.123283 | 0.351403 | 0.176177 | 0.123324 | 0.002220 | 0.000136 | 0.000011 |
| 2013 | 0.000006 | 0.018512 | 0.128186 | 0.349304 | 0.180404 | 0.124893 | 0.001806 | 0.000107 | 0.000019 |
| 2014 | 0.000021 | 0.019257 | 0.132930 | 0.344400 | 0.182210 | 0.126217 | 0.001526 | 0.000322 | 0.000028 |
| 2015 | 0.000020 | 0.020057 | 0.137393 | 0.341330 | 0.183411 | 0.125733 | 0.001279 | 0.001062 | 0.000074 |
| 2016 | 0.000021 | 0.020950 | 0.141976 | 0.339079 | 0.182669 | 0.125524 | 0.001092 | 0.000987 | 0.000195 |
| 2017 | 0.000017 | 0.022131 | 0.149274 | 0.338596 | 0.183327 | 0.125913 | 0.001051 | 0.000868 | 0.000634 |
| 2018 | 0.000028 | 0.022875 | 0.154388 | 0.334749 | 0.183482 | 0.125102 | 0.000962 | 0.000674 | 0.001464 |
| 2019 | 0.000039 | 0.024257 | 0.158958 | 0.329728 | 0.183687 | 0.125173 | 0.000880 | 0.000581 | 0.002446 |
| 2020 | 0.000043 | 0.026119 | 0.164027 | 0.324281 | 0.184384 | 0.123009 | 0.020024 | 0.000635 | 0.003232 |
| 2021 | 0.000049 | 0.027687 | 0.167372 | 0.319552 | 0.189387 | 0.122571 | 0.037406 | 0.000558 | 0.004139 |
| 2022 | 0.000075 | 0.029624 | 0.169388 | 0.308885 | 0.194550 | 0.123075 | 0.038294 | 0.000398 | 0.005172 |
| 2023 | 0.000746 | 0.040191 | 0.185275 | 0.318071 | 0.205981 | 0.116477 | 0.029592 | 0.000340 | 0.005155 |
| 2024 | 0.003573 | 0.070602 | 0.225259 | 0.350596 | 0.251300 | 0.098844 | 0.018684 | 0.000292 | 0.005157 |

### 1.3 All 291 Rare Excess Style Words in 2024 ($p < 0.02$, Verbatim from Figure S6 of `arXiv:2406.07016v5`)

> **Source:** Kobak et al., `arXiv:2406.07016v5`, Supplementary Figure S6 (*"All 291 excess style words in 2024 with frequency below 0.02"*):

> accentuates, acknowledges, acknowledging, addresses, adept, adhered, adhering, advancement, advancements, advancing, advocates, advocating, affirming, afflicted, aiding, akin, align, aligning, aligns, alongside, amidst, assessments, attains, attributed, augmenting, avenue, avenues, bolster, bolstered, bolstering, broader, burgeoning, capabilities, capitalizing, categorized, categorizes, categorizing, combating, commendable, compelling, complicates, complicating, comprehending, comprising, consequently, consolidates, contributing, conversely, correlating, crafted, crafting, culminating, customizing, delineates, delve, delved, delves, delving, demonstrating, dependability, dependable, detailing, detrimentally, diminishes, diminishing, discern, discerned, discernible, discerning, displaying, disrupts, distinctions, distinctive, elevate, elevates, elevating, elucidate, elucidates, elucidating, embracing, emerges, emphasises, emphasising, emphasize, emphasizes, emphasizing, employing, employs, empowers, emulating, emulation, enabling, encapsulates, encompass, encompassed, encompasses, encompassing, endeavors, endeavours, enduring, enhancements, enhances, ensuring, equipping, escalating, evaluates, evolving, exacerbating, examines, exceeding, excels, exceptional, exceptionally, exerting, exhibiting, exhibits, expedite, expediting, exploration, explores, facilitated, facilitates, facilitating, featuring, formidable, fostering, fosters, foundational, furnish, garnered, garnering, gauged, grappling, groundbreaking, groundwork, harness, harnesses, harnessing, heighten, heightened, hinder, hinges, hinting, hold, holds, illuminates, illuminating, imbalances, impacting, impede, impeding, imperative, impressive, inadequately, incorporates, incorporating, influencing, inherent, initially, innovative, inquiries, integrates, integrating, integration, interconnectedness, interplay, intricacies, intricate, intricately, introduces, invaluable, investigates, involves, juxtaposed, leverages, leveraging, maintaining, merges, methodologies, meticulous, meticulously, multifaceted, necessitate, necessitates, necessitating, necessity, notable, noteworthy, nuanced, nuances, offering, optimizing, orchestrating, outlines, overlook, overlooking, paving, persist, pinpoint, pinpointed, pinpointing, pioneering, pioneers, pivotal, poised, pose, posed, poses, posing, predominantly, preserving, pressing, promise, pronounced, propelling, realm, realms, recognizing, refine, refines, refining, remarkable, renowned, revealing, reveals, revolutionize, revolutionizing, revolves, scrutinize, scrutinized, scrutinizing, seamless, seamlessly, seeks, serves, serving, shaping, shedding, showcased, showcases, showcasing, signifying, solidify, spanned, spanning, spurred, stands, stemming, strategically, streamline, streamlined, streamlines, streamlining, struggle, substantiated, substantiates, surged, surmount, surpass, surpassed, surpasses, surpassing, swift, swiftly, thorough, transformative, typically, ultimately, uncharted, uncovering, underexplored, underscore, underscored, underscores, underscoring, unexplored, unlocking, unparalleled, unraveling, unveil, unveiled, unveiling, unveils, uphold, upholding, urging, utilizes, varying, versatility, warranting, yielding

### 1.4 Complete Catalog of All Annotated `style` Excess Words (Verbatim from `results/excess_words.csv`)

> **Source File:** [`berenslab/llm-excess-vocab/results/excess_words.csv`](https://github.com/berenslab/llm-excess-vocab/blob/53db991afc251782106cd817a1c3fa47a4d41781/results/excess_words.csv) (407 pure `style` words + 27 dual `content/style` or `style/content` words out of 900 total excess words annotated blind to year across 2013–2024; parenthetical notes are the authors' exact `comment` column entries).

#### Verbs (`part_of_speech = verb`) — 268 words

`accentuates`, `achieving`, `acknowledges`, `acknowledging`, `address`, `addresses`, `addressing`, `adhered`, `adhering`, `advancing`, `advocates`, `advocating`, `affirming`, `afflicted`, `aiding`, `aims`, `align`, `aligning`, `aligns`, `announced`, `apologizes`, `assess`, `assessed`, `assessing`, `attains`, `attributed`, `augmenting`, `based`, `bolster`, `bolstered`, `bolstering`, `burgeoning`, `capitalizing`, `categorized`, `categorizes`, `categorizing`, `challenge`, `combating`, `complicates`, `complicating`, `comprehend`, `comprehending`, `comprising`, `conducted`, `consequently`, `consolidates`, `contributing` (contributing factors), `correlating`, `crafted`, `crafting`, `culminating`, `customizing`, `declare`, `declared`, `delineates`, `delve`, `delved`, `delves`, `delving`, `demonstrated`, `demonstrates`, `demonstrating`, `detailing`, `diminishes`, `diminishing`, `discern`, `discerned`, `discerning`, `displaying`, `disrupts`, `easing`, `elevate`, `elevated`, `elevates`, `elevating`, `elucidate`, `elucidates`, `elucidating`, `embracing`, `emerged`, `emerges`, `emphasises`, `emphasising`, `emphasize`, `emphasizes`, `emphasizing`, `employed`, `employing`, `employs`, `empowers`, `emulating`, `enabling`, `encapsulates`, `encompass`, `encompassed`, `encompasses`, `encompassing`, `endangering`, `enduring`, `enhance`, `enhanced`, `enhances`, `enhancing`, `ensuring`, `equipping`, `escalating`, `evaluates`, `evolving`, `exacerbating`, `examines`, `exceeding`, `excels`, `exerting`, `exhibit`, `exhibited`, `exhibiting`, `exhibits`, `expedite`, `expediting`, `explores`, `facilitated`, `facilitates`, `facilitating`, `featuring`, `focusing`, `fostering`, `fosters`, `furnish`, `garnered`, `garnering`, `gauged`, `grappling`, `harness`, `harnesses`, `harnessing`, `heighten`, `highlight`, `highlighting`, `highlights`, `hinder`, `hinges`, `hinting`, `hold`, `holds`, `identified`, `illuminates`, `imbalances`, `impacting`, `impede`, `incorporates`, `incorporating`, `indicating`, `influencing`, `integrates`, `integrating`, `investigates`, `involves`, `involving`, `leading`, `leverages`, `leveraging`, `linked`, `maintaining`, `merges`, `necessitate`, `necessitates`, `necessitating`, `need`, `observed`, `offer`, `offering`, `offers`, `optimizing`, `orchestrating`, `outlines`, `overlook`, `overlooking`, `overwhelmed`, `paving`, `persist`, `pinpoint`, `pinpointed`, `pinpointing`, `pioneering`, `poised`, `pose`, `posed`, `poses`, `posing`, `postponed`, `presents`, `preserving`, `promise`, `promising`, `propelling`, `providing`, `realizes`, `recognizing`, `refine`, `refines`, `refining`, `reframing`, `remains`, `resulting`, `rethink`, `revealed`, `revealing`, `reveals`, `revolutionize`, `revolutionizing`, `revolves`, `scrutinize`, `scrutinized`, `scrutinizing`, `seeks`, `serves`, `serving`, `shaping`, `shedding`, `showcased`, `showcases`, `showcasing`, `signifying`, `solidify`, `spanned`, `spanning`, `spurred`, `stands`, `stemming`, `streamline`, `streamlined`, `streamlines`, `streamlining`, `struggle`, `substantiated`, `substantiates`, `surged`, `surmount`, `surpass`, `surpassed`, `surpasses`, `surpassing`, `uncovering`, `underexplored`, `underscore`, `underscored`, `underscores`, `underscoring`, `understanding`, `unlocking`, `unraveling`, `unveil`, `unveiled`, `unveiling`, `unveils`, `uphold`, `upholding`, `urging`, `using`, `utilized`, `utilizes`, `utilizing`, `varying`, `verifies`, `wandering`, `warranting`, `were`, `yielding`

#### Adjectives (`part_of_speech = adjective`) — 53 words

`adept`, `akin`, `broader`, `commendable`, `compelling`, `comprehensive`, `crucial`, `dependable`, `discernible`, `distinct`, `distinctive`, `diverse`, `exceptional`, `formidable`, `foundational`, `groundbreaking`, `heightened`, `illuminating`, `impactful`, `impeding`, `imperative`, `impressive`, `inherent`, `innovative`, `intricate`, `introduces`, `invaluable`, `juxtaposed`, `meticulous`, `multifaceted`, `notable`, `noteworthy`, `nuanced`, `pivotal`, `potential`, `precise`, `pressing`, `prevalent`, `primary`, `pronounced`, `remarkable`, `renowned`, `seamless`, `strategically`, `substantial`, `swift`, `thorough`, `transformative`, `uncharted`, `unexplored`, `unparalleled`, `valuable`, `various`

#### Nouns (`part_of_speech = noun` / `nount`) — 44 words

`advancement`, `advancements`, `analysis`, `approach`, `assessments`, `avenue`, `avenues`, `capabilities`, `challenges`, `complex`, `conditions`, `dependability`, `distinctions`, `emulation`, `endeavors` ("research endeavors"), `endeavours` (BE version), `enhancements`, `essentials`, `exploration`, `findings`, `groundwork`, `hardest`, `impact`, `individuals`, `inquiries`, `insights`, `integration`, `interconnectedness`, `interplay`, `intricacies`, `limitations`, `methodologies`, `necessity`, `nuances`, `outcomes`, `pioneers`, `realm`, `realms`, `research`, `role`, `statement`, `strategies`, `techniques`, `versatility`

#### Adverbs (`part_of_speech = adverb` / `advebr`) — 24 words

`additionally`, `conversely`, `deductively`, `detrimentally`, `effectively`, `exceptionally`, `however`, `inadequately`, `initially`, `intricately`, `meticulously`, `notably`, `particularly`, `potentially`, `predominantly`, `primarily`, `seamlessly`, `specifically`, `subsequently`, `swiftly`, `thereby`, `typically`, `ultimately`, `within`

#### Prepositions (`part_of_speech = preposition`) — 12 words

`across`, `alongside`, `amid`, `amidst`, `between`, `despite`, `during`, `including`, `into`, `midst`, `through`, `while`

#### Pronouns, Particles & Dual-POS (`pronoun`, `pronoun/adverb`, `noun/verb`, `particle`) — 6 words

`both` [pronoun/adverb], `fight` [noun/verb], `like` [particle], `their` [pronoun], `these` [pronoun], `this` [pronoun]

#### Dual-Annotated `content/style`, `style/content` & `style/count` Words — 27 words

`background` [content/style; noun] (can be both), `closures` [content/style; noun] (used in many contexts, like businesses), `complexities` [content/style; noun] (complexity can be a term as in computational complexity, or a general term), `concurrently` [content/style; adverb] (in principle style, but often used in a specific context (concurrency of disease symptoms or medications)), `deeper` [content/style; adjective] (can potentially refer to deep learning / deep networks), `efficacy` [style/count; noun] (can refer to vaccine efficacy), `faces` [content/style; noun/verb] (can be content noun (face) or style verb (to face)), `heterogenous` [content/style; adjective] (can have technical meanings but can also be used in other contexts), `inaugural` [content/style; adjective] (unsure), `investigation` [content/style; noun] (“investigation” can be a synonym of “study” or “experiment” which is style), `landscape` [content/style; noun] (can have technical meaning but also used as a style word), `lies` [content/style; noun/verb] (can be noun (plural from lie) or a verb (3rd person singular)), `minimizing` [content/style; verb] (can have technical and non-technical meanings), `mirroring` [content/style; verb] (can have technical and non-technical meanings), `modulating` [content/style; verb] (can have technical and non-technical meanings), `originality` [content/style; noun], `prioritize` [content/style; verb] (edge case -- "vaccine prioritizations"), `prioritizes` [content/style; verb], `prioritizing` [content/style; verb], `prominence` [content/style; noun] ("linguistic prominence" and some other terms), `prompting` [content/style; verb] (can be about LLM prompts), `reliance` [content/style; noun] (can have technical and non-technical meanings), `remotely` [content/style; adjective], `resuming` [content/style; verb] (can relate to covid pandemic), `significant` [content/style; adjective] (can mean "statistically significant" but not necessarily), `standardizing` [style/content; verb] (can have technical and non-technical meanings), `synthesizes` [style/content; verb] (can have technical and non-technical meanings)

---

## 2. Liang et al. (Stanford University, ICML 2024) — Top 100 AI Adjectives & Top 100 AI Adverbs in Peer Reviews

> **Verified Source Metadata**
> - **Authors:** Weixin Liang, Zachary Izzo, Yaohui Zhang, Haley Lepp, Hancheng Cao, Xuandong Zhao, Lingjiao Chen, Haotian Ye, Sheng Liu, Zhi Huang, Daniel A. McFarland, James Y. Zou
> - **Title:** *Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews*
> - **Venue:** *Proceedings of the 41st International Conference on Machine Learning (ICML 2024)*, PMLR 235:29575–29620
> - **arXiv URL & DOI:** [https://arxiv.org/abs/2403.07183](https://arxiv.org/abs/2403.07183) (`arXiv:2403.07183v4`) | [https://doi.org/10.48550/arXiv.2403.07183](https://doi.org/10.48550/arXiv.2403.07183)
> - **GitHub Framework Repository:** [https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers](https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers)

### 2.1 Core Empirical Findings (Verbatim from `arXiv:2403.07183v4`)

- **Sudden Post-ChatGPT Spike in Peer-Review Adjectives (Figure 1):**
  > "We find a significant shift in the frequency of certain tokens in ICLR 2024, with adjectives such as 'commendable', 'meticulous', and 'intricate' showing 9.8, 34.7, and 11.2-fold increases in probability of occurring in a sentence. We find a similar trend in NeurIPS but not in Nature Portfolio journals."
- **Behavioral Correlates Found by Liang et al.:** Higher estimated AI-modified fraction ($\alpha$) in conference peer reviews is empirically associated with reviews submitted closer to deadlines (*deadline effect*), reviews containing fewer specific references to scholarly literature (*reference effect*), lower author-reviewer rebuttal engagement (*low reply effect*), higher inter-reviewer textual convergence (*homogenization effect*), and lower self-reported reviewer confidence (*low confidence effect*).

### 2.2 Verbatim Table 2: Top 100 Adjectives Disproportionately Used More Frequently by AI

> **Source:** Liang et al. (`arXiv:2403.07183v4`, Appendix Table 2, exact order of the 100 tokens):

1. `commendable`, 2. `innovative`, 3. `meticulous`, 4. `intricate`, 5. `notable`, 6. `versatile`, 7. `noteworthy`, 8. `invaluable`, 9. `pivotal`, 10. `potent`, 11. `fresh`, 12. `ingenious`, 13. `cogent`, 14. `ongoing`, 15. `tangible`, 16. `profound`, 17. `methodical`, 18. `laudable`, 19. `lucid`, 20. `appreciable`, 21. `fascinating`, 22. `adaptable`, 23. `admirable`, 24. `refreshing`, 25. `proficient`, 26. `intriguing`, 27. `thoughtful`, 28. `credible`, 29. `exceptional`, 30. `digestible`, 31. `prevalent`, 32. `interpretative`, 33. `remarkable`, 34. `seamless`, 35. `economical`, 36. `proactive`, 37. `interdisciplinary`, 38. `sustainable`, 39. `optimizable`, 40. `comprehensive`, 41. `vital`, 42. `pragmatic`, 43. `comprehensible`, 44. `unique`, 45. `fuller`, 46. `authentic`, 47. `foundational`, 48. `distinctive`, 49. `pertinent`, 50. `valuable`, 51. `invasive`, 52. `speedy`, 53. `inherent`, 54. `considerable`, 55. `holistic`, 56. `insightful`, 57. `operational`, 58. `substantial`, 59. `compelling`, 60. `technological`, 61. `beneficial`, 62. `excellent`, 63. `keen`, 64. `cultural`, 65. `unauthorized`, 66. `strategic`, 67. `expansive`, 68. `prospective`, 69. `vivid`, 70. `consequential`, 71. `manageable`, 72. `unprecedented`, 73. `inclusive`, 74. `asymmetrical`, 75. `cohesive`, 76. `replicable`, 77. `quicker`, 78. `defensive`, 79. `wider`, 80. `imaginative`, 81. `traditional`, 82. `competent`, 83. `contentious`, 84. `widespread`, 85. `environmental`, 86. `instrumental`, 87. `substantive`, 88. `creative`, 89. `academic`, 90. `sizeable`, 91. `extant`, 92. `demonstrable`, 93. `prudent`, 94. `practicable`, 95. `signatory`, 96. `continental`, 97. `unnoticed`, 98. `automotive`, 99. `minimalistic`, 100. `intelligent`

### 2.3 Verbatim Table 3: Top 100 Adverbs Disproportionately Used More Frequently by AI

> **Source:** Liang et al. (`arXiv:2403.07183v4`, Appendix Table 3, exact order of the 100 tokens):

1. `meticulously`, 2. `reportedly`, 3. `lucidly`, 4. `innovatively`, 5. `aptly`, 6. `methodically`, 7. `excellently`, 8. `compellingly`, 9. `impressively`, 10. `undoubtedly`, 11. `scholarly`, 12. `strategically`, 13. `intriguingly`, 14. `competently`, 15. `intelligently`, 16. `hitherto`, 17. `thoughtfully`, 18. `profoundly`, 19. `undeniably`, 20. `admirably`, 21. `creatively`, 22. `logically`, 23. `markedly`, 24. `thereby`, 25. `contextually`, 26. `distinctly`, 27. `judiciously`, 28. `cleverly`, 29. `invariably`, 30. `successfully`, 31. `chiefly`, 32. `refreshingly`, 33. `constructively`, 34. `inadvertently`, 35. `effectively`, 36. `intellectually`, 37. `rightly`, 38. `convincingly`, 39. `comprehensively`, 40. `seamlessly`, 41. `predominantly`, 42. `coherently`, 43. `evidently`, 44. `notably`, 45. `professionally`, 46. `subtly`, 47. `synergistically`, 48. `productively`, 49. `purportedly`, 50. `remarkably`, 51. `traditionally`, 52. `starkly`, 53. `promptly`, 54. `richly`, 55. `nonetheless`, 56. `elegantly`, 57. `smartly`, 58. `solidly`, 59. `inadequately`, 60. `effortlessly`, 61. `forth`, 62. `firmly`, 63. `autonomously`, 64. `duly`, 65. `critically`, 66. `immensely`, 67. `beautifully`, 68. `maliciously`, 69. `finely`, 70. `succinctly`, 71. `further`, 72. `robustly`, 73. `decidedly`, 74. `conclusively`, 75. `diversely`, 76. `exceptionally`, 77. `concurrently`, 78. `appreciably`, 79. `methodologically`, 80. `universally`, 81. `thoroughly`, 82. `soundly`, 83. `particularly`, 84. `elaborately`, 85. `uniquely`, 86. `neatly`, 87. `definitively`, 88. `substantively`, 89. `usefully`, 90. `adversely`, 91. `primarily`, 92. `principally`, 93. `discriminatively`, 94. `efficiently`, 95. `scientifically`, 96. `alike`, 97. `herein`, 98. `additionally`, 99. `subsequently`, 100. `potentially`

### 2.4 Verbatim Table 7 & Table 8: Estimated AI-Modified Review Fraction ($\alpha$) Across Conferences vs. *Nature* Portfolio

> **Source:** Liang et al. (`arXiv:2403.07183v4`, Appendix Tables 7 & 8 — Adjective-based MLE estimates):

**Table 7 (ML Conferences — Post-ChatGPT Surge in NeurIPS '23, ICLR '24, CoRL '23, EMNLP '23):**

| No. | Validation Data Source | Estimated $\alpha$ | CI ($\pm$) |
| --- | --- | --- | --- |
| (1) | NeurIPS 2019 | 1.7% | 0.3% |
| (2) | NeurIPS 2020 | 1.4% | 0.1% |
| (3) | NeurIPS 2021 | 1.6% | 0.2% |
| (4) | NeurIPS 2022 | 1.9% | 0.2% |
| (5) | NeurIPS 2023 | 9.1% | 0.2% |
| (6) | ICLR 2023 | 1.6% | 0.1% |
| (7) | ICLR 2024 | 10.6% | 0.2% |
| (8) | CoRL 2021 | 2.4% | 0.7% |
| (9) | CoRL 2022 | 2.4% | 0.6% |
| (10) | CoRL 2023 | 6.5% | 0.7% |
| (11) | EMNLP 2023 | 16.9% | 0.5% |

**Table 8 (*Nature* Family Journals — Pre/Post-ChatGPT Control Baseline):**

| No. | Validation Data Source | Estimated $\alpha$ | CI ($\pm$) |
| --- | --- | --- | --- |
| (1) | Nature portfolio 2019 | 0.8% | 0.2% |
| (2) | Nature portfolio 2020 | 0.7% | 0.2% |
| (3) | Nature portfolio 2021 | 1.1% | 0.2% |
| (4) | Nature portfolio 2022 | 1.0% | 0.3% |
| (5) | Nature portfolio 2023 | 1.6% | 0.2% |

---

## 3. Liang et al. (Stanford University, *Nature Human Behaviour*, 2025) — LLM Usage Across 950,965 Scientific Papers

> **Verified Source Metadata**
> - **Authors:** Weixin Liang, Yaohui Zhang, Zhengxuan Wu, Haley Lepp, Wenlong Ji, Xuandong Zhao, Hancheng Cao, Sheng Liu, Siyu He, Zhi Huang, Diyi Yang, Christopher Potts, Christopher D. Manning, James Y. Zou
> - **Preprint Title:** *Mapping the Increasing Use of LLMs in Scientific Papers* ([`arXiv:2404.01268`](https://arxiv.org/abs/2404.01268), DOI: [`10.48550/arXiv.2404.01268`](https://doi.org/10.48550/arXiv.2404.01268))
> - **Published Journal Article:** *Quantifying large language model usage in scientific papers*, *Nature Human Behaviour* (2025), DOI: [https://doi.org/10.1038/s41562-025-02273-8](https://doi.org/10.1038/s41562-025-02273-8)
> - **GitHub Repository:** [https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers](https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers) (MIT License, Commit SHA: `8defb86079a566e0196d2ab0cc88ff9823d25813`; archived locally in `../upstream-skills/03-models-and-stylometry-data/Weixin-Liang-Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers/`)

### 3.1 Top Disproportionate Scientific LLM Words & Corpus Findings (Verbatim from `arXiv:2404.01268v1`)

- **Dataset:** 950,965 papers published between January 2020 and February 2024 across arXiv, bioRxiv, and *Nature* portfolio journals.
- **Top 4 Log-Odds Disproportionate LLM Marker Words in CS Abstracts & Introductions (Figures 2 & 11):**
  - `realm`
  - `intricate`
  - `showcasing`
  - `pivotal`
- **Discipline-Level LLM-Modified Sentence Proportions ($\alpha$ by February 2024):**
  > "Our results indicate that the largest and fastest growth was observed in Computer Science papers, with $\alpha$ reaching 17.5% for abstracts and 15.3% for introductions by February 2024. In contrast, Mathematics papers and the Nature portfolio showed the least increase, with $\alpha$ reaching 4.9% and 6.3% for abstracts and 3.5% and 6.4% for introductions, respectively."
- **Structural Correlates of LLM Modification (Sections 5.2–5.4):**
  1. **Higher First-Author Preprint Volume:** Papers by first authors who post preprints more frequently have significantly higher LLM-modified fractions.
  2. **Crowded Research Areas / Flattened Diversity:** Papers with smaller embedding distance to their nearest neighboring peer exhibit significantly higher LLM modification ("which could indicate higher use in more crowded fields of study... or that generated-text is flattening writing diversity").
  3. **Shorter Paper Length:** Papers under 5,000 words consistently exhibit higher LLM modification than papers above 5,000 words across `cs.CV` and `cs.LG`.

---

## 4. Andrew Gray (University College London, 2024) — Scholarly Literature Keyword Contamination

> **Verified Source Metadata**
> - **Author:** Andrew Gray (UCL Library Services, University College London; ORCID [`0000-0002-2910-3033`](https://orcid.org/0000-0002-2910-3033))
> - **Title:** *ChatGPT "contamination": estimating the prevalence of LLMs in the scholarly literature*
> - **arXiv URL & DOI:** [https://arxiv.org/abs/2403.16887](https://arxiv.org/abs/2403.16887) (`arXiv:2403.16887v1`) | [https://doi.org/10.48550/arXiv.2403.16887](https://doi.org/10.48550/arXiv.2403.16887)
> - **Published Dataset:** Gray, Andrew (2024). *LLM related keywords in Dimensions - search counts*. University College London. DOI: [https://doi.org/10.5522/04/25471957](https://doi.org/10.5522/04/25471957)

### 4.1 Verbatim 36-Term Test Matrix (Page 3 of `arXiv:2403.16887v1`, >5.3 Million 2023 Articles in Dimensions)

| Rank | Tested Adjectives | Tested Adverbs | Neutral Control Words |
| --- | --- | --- | --- |
| 1 | `commendable` | `meticulously` | `consider` |
| 2 | `innovative` | `reportedly` | `conclusion` |
| 3 | `meticulous` | `lucidly` | `furthermore` |
| 4 | `intricate` | `innovatively` | `relative` |
| 5 | `notable` | `aptly` | `technical` |
| 6 | `versatile` | `methodically` | `blue` |
| 7 | `noteworthy` | `excellently` | `red` |
| 8 | `invaluable` | `compellingly` | `yellow` |
| 9 | `pivotal` | `impressively` | `before` |
| 10 | `potent` | `undoubtedly` | `after` |
| 11 | `fresh` | `scholarly` | `earlier` |
| 12 | `ingenious` | `strategically` | `later` |

- **Additional Unplanned ChatGPT Markers Documented by Gray (Page 9):**
  - `groundbreaking`: **+52%** increase in 2023 full-text articles.
  - `outwith` (traditionally restricted to Scottish English, unexpectedly favored by ChatGPT): **+185%** increase in 2023 (nearly tripled).
  - Single-word 2023 YoY spikes (Pages 5–6): `meticulously` (**+137%**), `intricate` (**+117%**, rising from ~50,000 to >100,000 papers/year), `commendable` (**+83%**), `meticulous` (**+59%**), `methodically` (**+26%**), `innovatively` (**+26%**). Co-occurrence of both `intricate` AND `meticulous` in the same paper increased **seven-fold** in 2023; `intricate` AND `notable` increased **four-fold** (Page 8).

### 4.2 Verbatim Combined-Terms & Multi-Term Tables (Pages 7 & 8 of `arXiv:2403.16887v1`)

| Group | Indicator Query | 2022 Papers | 2023 Papers | YoY Increase |
| --- | --- | --- | --- | --- |
| **1 (1x Strong)** | `intricate OR meticulous OR meticulously OR commendable` | 86,988 | 159,655 | **+83.5%** |
| **2 (1x Medium)** | `notable OR pivotal OR invaluable OR noteworthy OR methodically OR strategically` | 574,753 | 668,535 | **+16.3%** |
| **3 (1x Weak)** | `innovative OR versatile` | 490,213 | 535,996 | **+9.3%** |
| **4 (1x Strong/Medium)** | Group 1 OR Group 2 (10 terms) | 634,831 | 752,334 | **+18.5%** |
| **5 (1x All 12)** | Group 1 OR Group 2 OR Group 3 (12 terms) | 1,000,870 | 1,116,686 | **+11.7%** |
| **6 (2x Strong)** | Any $\ge 2$ terms from `{intricate, meticulous, meticulously, commendable}` | 3,045 | 16,950 | **+468.4%** |
| **7 (2x Medium)** | Any $\ge 2$ terms from `{notable, pivotal, invaluable, noteworthy, methodically, strategically}` | 70,375 | 115,560 | **+67.7%** |
| **8 (2x Weak)** | Both `innovative` AND `versatile` | 24,807 | 32,819 | **+35.1%** |
| **9 (2x Strong/Medium)** | Any $\ge 2$ terms from Group 1/2 (10 terms) | 93,002 | 163,746 | **+79.8%** |
| **10 (2x All 12)** | Any $\ge 2$ terms from Group 1/2/3 (12 terms) | 207,512 | 296,073 | **+45.7%** |

- **Non-Disclosure Rate (Page 9):** Out of 1,116,686 articles in Group 5 in 2023, only **767 (<0.1%)** matched any disclosure query (`chatGPT OR GPT OR openAI OR LLM OR "large language model" OR "artificial intelligence"`), and most of those were articles *about* LLMs rather than disclosures.

---

## 5. Juzek & Ward (COLING 2025) — *Why Does ChatGPT "Delve" So Much?* (21 Focal Words & RLHF Origin)

> **Verified Source Metadata**
> - **Authors:** Tom S. Juzek, Zina B. Ward (Florida State University)
> - **Title:** *Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models*
> - **Venue:** *Proceedings of the 31st International Conference on Computational Linguistics (COLING 2025)*, pp. 6397–6411
> - **ACL Anthology URL:** [https://aclanthology.org/2025.coling-main.426/](https://aclanthology.org/2025.coling-main.426/)
> - **arXiv URL & DOI:** [https://arxiv.org/abs/2412.11385](https://arxiv.org/abs/2412.11385) (`arXiv:2412.11385v1`) | [https://doi.org/10.48550/arXiv.2412.11385](https://doi.org/10.48550/arXiv.2412.11385)
> - **GitHub Repository:** [https://github.com/tjuzek/delve](https://github.com/tjuzek/delve) (Code: MIT-0, Data: CC0 1.0; archived locally in `../upstream-skills/03-models-and-stylometry-data/tjuzek-delve/`)

### 5.1 Verbatim Table 2: All 21 Focal Words Overrepresented in 2024 Scientific Abstracts vs. 2020

> **Source:** Juzek & Ward (`arXiv:2412.11385v1`, Table 2 — occurrences per million words `opm` in scientific abstracts):

| Word | opm (2020) | opm (2024) | Increase (%) |
| --- | --- | --- | --- |
| `delves` | 0.21 | 14.38 | 6697.14 |
| `delved` | 0.12 | 2.90 | 2240.47 |
| `delving` | 0.12 | 2.38 | 1816.83 |
| `showcasing` | 0.59 | 8.79 | 1396.03 |
| `delve` | 0.58 | 8.50 | 1374.92 |
| `boasts` | 0.11 | 1.15 | 918.18 |
| `underscores` | 4.50 | 45.19 | 903.61 |
| `comprehending` | 0.56 | 5.58 | 898.95 |
| `intricacies` | 0.60 | 5.22 | 772.85 |
| `surpassing` | 1.37 | 10.50 | 667.48 |
| `intricate` | 6.22 | 44.22 | 611.24 |
| `underscoring` | 2.70 | 17.17 | 536.94 |
| `garnered` | 2.44 | 13.13 | 437.19 |
| `showcases` | 0.82 | 4.31 | 422.45 |
| `emphasizing` | 8.30 | 41.27 | 397.12 |
| `underscore` | 7.42 | 36.40 | 390.65 |
| `realm` | 2.25 | 10.85 | 381.10 |
| `surpasses` | 0.85 | 3.96 | 367.55 |
| `groundbreaking` | 0.87 | 3.75 | 330.42 |
| `advancements` | 12.49 | 47.17 | 277.59 |
| `aligns` | 1.55 | 5.68 | 266.97 |

### 5.2 Verbatim Table 3: Occurrences per Million (`opm`) in ChatGPT-3.5 & ChatGPT-4o-mini vs. Human Corpora

> **Source:** Juzek & Ward (`arXiv:2412.11385v1`, Table 3 — comparing synthetic ChatGPT abstracts against arXiv, Leipzig Corpora Collection [LCC], PubMed, and Wikipedia):

| Word | ChatGPT 3.5 (opm) | ChatGPT 4o-mini (opm) | arXiv (opm) | LCC (opm) | PubMed (opm) | Wikipedia (opm) |
| --- | --- | --- | --- | --- | --- | --- |
| `of` | 45624.84 | 42622.65 | 42842.72 | 27363.47 | 38634.99 | 23116.18 |
| `and` | 38889.24 | 32537.79 | 26395.28 | 28488.53 | 39469.96 | 21149.63 |
| `the` | 63174.05 | 55111.23 | 72009.63 | 59324.62 | 52139.05 | 53379.32 |
| `data` | 978.91 | 1075.59 | 2484.20 | 418.29 | 1734.75 | 142.81 |
| `results` | 4074.64 | 3307.32 | 2352.13 | 244.52 | 1722.07 | 95.37 |
| `i` | 32.21 | 61.17 | 414.03 | 4715.42 | 214.82 | 8041.61 |
| `year` | 78.50 | 61.77 | 37.58 | 1076.29 | 217.25 | 397.61 |
| `patients` | 4416.82 | 3936.56 | 48.97 | 131.48 | 4775.73 | 23.04 |
| `advancements` | 319.37 | 407.59 | 22.54 | 2.56 | 15.53 | 1.11 |
| `aligns` | 6.71 | 19.99 | 6.68 | 1.32 | 1.89 | 0.90 |
| `boasts` | 5.37 | 0.61 | 0.43 | 14.11 | 0.16 | 1.48 |
| `comprehending` | 6.71 | 7.27 | 1.77 | 0.37 | 0.99 | 0.31 |
| `delve` | 19.46 | 18.17 | 4.07 | 2.23 | 0.98 | 1.21 |
| `delves` | 183.17 | 23.01 | 3.20 | 0.79 | 0.32 | 0.53 |
| `delved` | 6.71 | 0.61 | 0.30 | 0.61 | 0.18 | 0.38 |
| `delving` | 8.72 | 0.61 | 0.72 | 0.76 | 0.24 | 0.61 |
| `emphasizing` | 138.21 | 367.61 | 10.21 | 2.82 | 9.92 | 2.64 |
| `garnered` | 20.80 | 173.21 | 4.09 | 4.34 | 2.74 | 4.61 |
| `groundbreaking` | 38.92 | 17.56 | 2.47 | 5.91 | 1.02 | 2.26 |
| `intricate` | 163.04 | 316.14 | 17.87 | 4.79 | 6.22 | 2.13 |
| `intricacies` | 15.43 | 27.25 | 1.98 | 1.24 | 0.68 | 0.68 |
| `realm` | 10.74 | 54.51 | 11.53 | 9.22 | 2.27 | 8.46 |
| `showcases` | 28.85 | 4.24 | 3.19 | 4.65 | 1.05 | 1.46 |
| `showcasing` | 30.19 | 58.14 | 5.89 | 5.42 | 0.75 | 1.65 |
| `surpasses` | 4.03 | 4.24 | 11.16 | 1.14 | 1.04 | 0.40 |
| `surpassing` | 5.37 | 17.56 | 7.61 | 1.66 | 1.51 | 1.42 |
| `underscore` | 18.12 | 1365.08 | 5.17 | 1.53 | 7.91 | 0.72 |
| `underscores` | 60.39 | 1048.94 | 4.95 | 1.90 | 4.91 | 0.90 |
| `underscoring` | 10.06 | 313.71 | 2.57 | 0.66 | 3.15 | 0.20 |

### 5.3 Empirical Findings on the Source of Lexical Overrepresentation

- **Not Caused by Pretraining Corpora or Architecture:** In Table 3, human corpora (`arXiv`, `LCC`, `PubMed`, `Wikipedia`) have 1–2 orders of magnitude lower frequencies of focal words (e.g., `underscore` is `0.72` opm in Wikipedia and `5.17` opm in arXiv, vs. **`1365.08` opm** in ChatGPT-4o-mini; `delves` is `0.32` opm in PubMed vs. **`183.17` opm** in ChatGPT-3.5).
- **RLHF / Alignment Effect (Tables 1 & 4):** Comparing base models (`Llama 2-Base`, `Llama 3-Base`, `Llama 3.1-Base`) against instruction/RLHF-aligned chat models (`Llama 2-Chat`, `Llama 3-Chat`, `Llama 3.1-Chat`) shows that per-word entropy drops selectively on ChatGPT-generated abstracts only *after* chat/RLHF alignment (`1.633` $\to$ `0.886` in Llama 2), implicating human feedback alignment stages as a driver of lexical overrepresentation.

---

# Part II: Classic Authoritative Prose Checklists & Published Writing Rules

## 6. George Orwell — *Politics and the English Language* (*Horizon*, April 1946)

> **Verified Source Metadata**
> - **Author:** George Orwell (Eric Arthur Blair)
> - **Title:** *Politics and the English Language* (originally published in *Horizon*, Vol. 13, Issue 76, April 1946)
> - **Primary Verified URL:** [https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/) (The Orwell Foundation, reproduced with permission of the Orwell Estate)

### 6.1 Orwell's Six Elementary Rules (Verbatim)

> **Source:** [The Orwell Foundation — *Politics and the English Language*](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/)

1. **i. Never use a metaphor, simile or other figure of speech which you are used to seeing in print.**
2. **ii. Never use a long word where a short one will do.**
3. **iii. If it is possible to cut a word out, always cut it out.**
4. **iv. Never use the passive where you can use the active.**
5. **v. Never use a foreign phrase, a scientific word or a jargon word if you can think of an everyday English equivalent.**
6. **vi. Break any of these rules sooner than say anything outright barbarous.**

### 6.2 Orwell's Six Diagnostic Questions for Every Sentence (Verbatim Excerpt)

> "A scrupulous writer, in every sentence that he writes, will ask himself at least four questions, thus: *What am I trying to say? What words will express it? What image or idiom will make it clearer? Is this image fresh enough to have an effect?* And he will probably ask himself two more: *Could I put it more shortly? Have I said anything that is avoidably ugly?* But you are not obliged to go to all this trouble. You can shirk it by simply throwing your mind open and letting the ready-made phrases come crowding in. They will construct your sentences for you – even think your thoughts for you, to a certain extent – and at need they will perform the important service of partially concealing your meaning even from yourself."

### 6.3 Orwell's Core Diagnostic Thesis: "Prefabricated Hen-House" Prose (Verbatim Excerpts)

> "Now, it is clear that the decline of a language must ultimately have political and economic causes: it is not due simply to the bad influence of this or that individual writer. But an effect can become a cause, reinforcing the original cause and producing the same effect in an intensified form, and so on indefinitely. A man may take to drink because he feels himself to be a failure, and then fail all the more completely because he drinks. It is rather the same thing that is happening to the English language. It becomes ugly and inaccurate because our thoughts are foolish, but the slovenliness of our language makes it easier for us to have foolish thoughts. The point is that the process is reversible. Modern English, especially written English, is full of bad habits which spread by imitation and which can be avoided if one is willing to take the necessary trouble. If one gets rid of these habits one can think more clearly, and to think clearly is a necessary first step toward political regeneration: so that the fight against bad English is not frivolous and is not the exclusive concern of professional writers. I will come back to this presently, and I hope that by that time the meaning of what I have said here will have become clearer. Meanwhile, here are five specimens of the English language as it is now habitually written."

> "Each of these passages has faults of its own, but, quite apart from avoidable ugliness, two qualities are common to all of them. The first is staleness of imagery; the other is lack of precision. The writer either has a meaning and cannot express it, or he inadvertently says something else, or he is almost indifferent as to whether his words mean anything or not. This mixture of vagueness and sheer incompetence is the most marked characteristic of modern English prose, and especially of any kind of political writing. As soon as certain topics are raised, the concrete melts into the abstract and no one seems able to think of turns of speech that are not hackneyed: prose consists less and less of words chosen for the sake of their meaning, and more and more of phrases tacked together like the sections of a prefabricated hen-house. I list below, with notes and examples, various of the tricks by means of which the work of prose-construction is habitually dodged."

### 6.4 Orwell's Four Categories of Dodging Prose-Construction (Verbatim Definitions & Word Lists)

#### (1) Dying Metaphors
> "Dying metaphors. A newly invented metaphor assists thought by evoking a visual image, while on the other hand a metaphor which is technically ‘dead’ (e. g. iron resolution) has in effect reverted to being an ordinary word and can generally be used without loss of vividness. But in between these two classes there is a huge dump of worn-out metaphors which have lost all evocative power and are merely used because they save people the trouble of inventing phrases for themselves. Examples are: Ring the changes on, take up the cudgels for, toe the line, ride roughshod over, stand shoulder to shoulder with, play into the hands of, no axe to grind, grist to the mill, fishing in troubled waters, on the order of the day, Achilles’ heel, swan song, hotbed. Many of these are used without knowledge of their meaning (what is a ‘rift’, for instance?), and incompatible metaphors are frequently mixed, a sure sign that the writer is not interested in what he is saying. Some metaphors now current have been twisted out of their original meaning without those who use them even being aware of the fact. For example, toe the line is sometimes written as tow the line. Another example is the hammer and the anvil, now always used with the implication that the anvil gets the worst of it. In real life it is always the anvil that breaks the hammer, never the other way about: a writer who stopped to think what he was saying would avoid perverting the original phrase."

#### (2) Operators, or Verbal False Limbs
> "Operators, or verbal false limbs. These save the trouble of picking out appropriate verbs and nouns, and at the same time pad each sentence with extra syllables which give it an appearance of symmetry. Characteristic phrases are: render inoperative, militate against, prove unacceptable, make contact with, be subject to, give rise to, give grounds for, have the effect of, play a leading part (role) in, make itself felt, take effect, exhibit a tendency to, serve the purpose of, etc. etc. The keynote is the elimination of simple verbs. Instead of being a single word, such as break, stop, spoil, mend, kill, a verb becomes a phrase, made up of a noun or adjective tacked on to some general-purposes verb such as prove, serve, form, play, render. In addition, the passive voice is wherever possible used in preference to the active, and noun constructions are used instead of gerunds (by examination of instead of by examining). The range of verbs is further cut down by means of the -ize and de- formations, and banal statements are given an appearance of profundity by means of the not un- formation. Simple conjunctions and prepositions are replaced by such phrases as with respect to, having regard to, the fact that, by dint of, in view of, in the interests of, on the hypothesis that; and the ends of sentences are saved from anticlimax by such resounding commonplaces as greatly to be desired, cannot be left out of account, a development to be expected in the near future, deserving of serious consideration, brought to a satisfactory conclusion, and so on and so forth."

#### (3) Pretentious Diction
> "Pretentious diction. Words like phenomenon, element, individual (as noun), objective, categorical, effective, virtual, basic, primary, promote, constitute, exhibit, exploit, utilize, eliminate, liquidate, are used to dress up simple statements and give an air of scientific impartiality to biassed judgements. Adjectives like epoch-making, epic, historic, unforgettable, triumphant, age-old, inevitable, inexorable, veritable, are used to dignify the sordid processes of international politics, while writing that aims at glorifying war usually takes on an archaic colour, its characteristic words being: realm, throne, chariot, mailed fist, trident, sword, shield, buckler, banner, jackboot, clarion. Foreign words and expressions such as cul de sac, ancien régime, deus ex machina, mutatis mutandis, status quo, Gleichschaltung, Weltanschauung, are used to give an air of culture and elegance. Except for the useful abbreviations i.e., e.g., and etc., there is no real need for any of the hundreds of foreign phrases now current in English. Bad writers, and especially scientific, political and sociological writers, are nearly always haunted by the notion that Latin or Greek words are grander than Saxon ones, and unnecessary words like expedite, ameliorate, predict, extraneous, deracinated, clandestine, sub-aqueous and hundreds of others constantly gain ground from their Anglo-Saxon opposite numbers[1]. The jargon peculiar to Marxist writing (hyena, hangman, cannibal, petty bourgeois, these gentry, lackey, flunkey, mad dog, White Guard, etc.) consists largely of words translated from Russian, German, or French; but the normal way of coining a new word is to use a Latin or Greek root with the appropriate affix and, where necessary, the -ize formation. It is often easier to make up words of this kind (deregionalize, impermissible, extramarital, non-fragmentatory and so forth) than to think up the English words that will cover one’s meaning. The result, in general, is an increase in slovenliness and vagueness."

#### (4) Meaningless Words
> "Meaningless words. In certain kinds of writing, particularly in art criticism and literary criticism, it is normal to come across long passages which are almost completely lacking in meaning[2]. Words like romantic, plastic, values, human, dead, sentimental, natural, vitality, as used in art criticism, are strictly meaningless, in the sense that they not only do not point to any discoverable object, but are hardly even expected to do so by the reader. When one critic writes, ‘The outstanding feature of Mr. X’s work is its living quality’, while another writes, ‘The immediately striking thing about Mr. X’s work is its peculiar deadness’, the reader accepts this as a simple difference of opinion. If words like black and white were involved, instead of the jargon words dead and living, he would see at once that language was being used in an improper way. Many political words are similarly abused. The word Fascism has now no meaning except in so far as it signifies ‘something not desirable’. The words democracy, socialism, freedom, patriotic, realistic, justice, have each of them several different meanings which cannot be reconciled with one another. In the case of a word like democracy, not only is there no agreed definition, but the attempt to make one is resisted from all sides. It is almost universally felt that when we call a country democratic we are praising it: consequently the defenders of every kind of régime claim that it is a democracy, and fear that they might have to stop using that word if it were tied down to any one meaning. Words of this kind are often used in a consciously dishonest way. That is, the person who uses them has his own private definition, but allows his hearer to think he means something quite different. Statements like Marshal Pétain was a true patriot, The Soviet press is the freest in the world, The Catholic Church is opposed to persecution, are almost always made with intent to deceive. Other words used in variable meanings, in most cases more or less dishonestly, are: class, totalitarian, science, progressive, reactionary, bourgeois, equality."

### 6.5 Orwell's Canonical Ecclesiastes Translation Specimen (Verbatim)

- **Original English (*Ecclesiastes* 9:11 — 49 words, 60 syllables, six vivid concrete images):**
  > "I returned and saw under the sun, that the race is not to the swift, nor the battle to the strong, neither yet bread to the wise, nor yet riches to men of understanding, nor yet favour to men of skill; but time and chance happeneth to them all."
- **Orwell's Parody in "Modern English of the Worst Sort" (38 words, 90 syllables, 18 Latin-root words + 1 Greek-root word, zero concrete images):**
  > "Objective consideration of contemporary phenomena compels the conclusion that success or failure in competitive activities exhibits no tendency to be commensurate with innate capacity, but that a considerable element of the unpredictable must invariably be taken into account."
- **Orwell's Verbatim Analysis of the Specimen:**
  > "This is a parody, but not a very gross one. Exhibit 3 above, for instance, contains several patches of the same kind of English. It will be seen that I have not made a full translation. The beginning and ending of the sentence follow the original meaning fairly closely, but in the middle the concrete illustrations – race, battle, bread – dissolve into the vague phrase ‘success or failure in competitive activities’. This had to be so, because no modern writer of the kind I am discussing – no one capable of using phrases like ‘objective’ consideration of contemporary phenomena’ – would ever tabulate his thoughts in that precise and detailed way. The whole tendency of modern prose is away from concreteness. Now analyse these two sentences a little more closely. The first contains 49 words but only 60 syllables, and all its words are those of everyday life. The second contains 38 words of 90 syllables: 18 of its words are from Latin roots, and one from Greek. The first sentence contains six vivid images, and only one phrase (‘time and chance’) that could be called vague. The second contains not a single fresh, arresting phrase, and in spite of its 90 syllables it gives only a shortened version of the meaning contained in the first. Yet without a doubt it is the second kind of sentence that is gaining ground in modern English. I do not want to exaggerate. This kind of writing is not yet universal, and outcrops of simplicity will occur here and there in the worst-written page. Still if you or I were told to write a few lines on the uncertainty of human fortunes, we should probably come much nearer to my imaginary sentence than to the one from Ecclesiastes."

### 6.6 Letting the Meaning Choose the Word (Verbatim Closing Passages)

> "To begin with it has nothing to do with archaism, with the salvaging of obsolete words and turns of speech, or with the setting up of a ‘standard English’ which must never be departed from. On the contrary, it is especially concerned with the scrapping of every word or idiom which has outworn its usefulness. It has nothing to do with correct grammar and syntax, which are of no importance so long as one makes one’s meaning clear or with the avoidance of Americanisms, or with having what is called a ‘good prose style’. On the other hand it is not concerned with fake simplicity and the attempt to make written English colloquial. Nor does it even imply in every case preferring the Saxon word to the Latin one, though it does imply using the fewest and shortest words that will cover one’s meaning. What is above all needed is to let the meaning choose the word, and not the other way about. In prose, the worst thing one can do with words is to surrender to them. When you think of a concrete object, you think wordlessly, and then, if you want to describe the thing you have been visualising, you probably hunt about till you find the exact words that seem to fit it. When you think of something abstract you are more inclined to use words from the start, and unless you make a conscious effort to prevent it, the existing dialect will come rushing in and do the job for you, at the expense of blurring or even changing your meaning. Probably it is better to put off using words as long as possible and get one’s meanings as clear as one can through pictures and sensations. Afterward one can choose – not simply accept – the phrases that will best cover the meaning, and then switch round and decide what impression one’s words are likely to make on another person. This last effort of the mind cuts out all stale or mixed images, all prefabricated phrases, needless repetitions, and humbug and vagueness generally. But one can often be in doubt about the effect of a word or a phrase, and one needs rules that one can rely on when instinct fails. I think the following rules will cover most cases:"

> "I have not here been considering the literary use of language, but merely language as an instrument for expressing and not for concealing or preventing thought. Stuart Chase and others have come near to claiming that all abstract words are meaningless, and have used this as a pretext for advocating a kind of political quietism. Since you don’t know what Fascism is, how can you struggle against Fascism? One need not swallow such absurdities as this, but one ought to recognize that the present political chaos is connected with the decay of language, and that one can probably bring about some improvement by starting at the verbal end. If you simplify your English, you are freed from the worst follies of orthodoxy. You cannot speak any of the necessary dialects, and when you make a stupid remark its stupidity will be obvious, even to yourself. Political language – and with variations this is true of all political parties, from Conservatives to Anarchists – is designed to make lies sound truthful and murder respectable, and to give an appearance of solidity to pure wind. One cannot change this all in a moment, but one can at least change one’s own habits, and from time to time one can even, if one jeers loudly enough, send some worn-out and useless phrase – some jackboot, Achilles’ heel, hotbed, melting pot, acid test, veritable inferno or other lump of verbal refuse – into the dustbin where it belongs."

---

## 7. Paul Graham — Published Writing Rules & Essays (`paulgraham.com`, 2005–2025)

> **Verified Source Metadata**
> - **Author:** Paul Graham
> - **Platform:** `paulgraham.com` (Paul Graham's official essays archive: [https://paulgraham.com/articles.html](https://paulgraham.com/articles.html))
> - **Verified Essay URLs Collected Below:**
>   1. [*Writing, Briefly*](https://paulgraham.com/writing44.html) (March 2005)
>   2. [*Write Like You Talk*](https://paulgraham.com/talk.html) (October 2015)
>   3. [*How to Write Usefully*](https://paulgraham.com/useful.html) (February 2020)
>   4. [*Write Simply*](https://paulgraham.com/simply.html) (March 2021)
>   5. [*Putting Ideas into Words*](https://paulgraham.com/words.html) (February 2022)
>   6. [*Good Writing*](https://paulgraham.com/goodwriting.html) (May 2025)

---

### 7.1 *Writing, Briefly* (March 2005) — Complete Verbatim Checklist of 36 Directives

> **Verified URL:** [https://paulgraham.com/writing44.html](https://paulgraham.com/writing44.html)

> "(In the process of answering an email, I accidentally wrote a tiny essay about writing. I usually spend weeks on an essay. This one took 67 minutes—23 of writing, and 44 of rewriting.)"
>
> "I think it's far more important to write well than most people realize. Writing doesn't just communicate ideas; it generates them. If you're bad at writing and don't like to do it, you'll miss out on most of the ideas writing would have generated."

**Paul Graham's Verbatim 36 Semicolon-Separated Directives ("As for how to write well, here's the short version:"):**

1. "Write a bad version 1 as fast as you can"
2. "rewrite it over and over"
3. "cut out everything unnecessary"
4. "write in a conversational tone"
5. "develop a nose for bad writing, so you can see and fix it in yours"
6. "imitate writers you like"
7. "if you can't get started, tell someone what you plan to write about, then write down what you said"
8. "expect 80% of the ideas in an essay to happen after you start writing it, and 50% of those you start with to be wrong"
9. "be confident enough to cut"
10. "have friends you trust read your stuff and tell you which bits are confusing or drag"
11. "don't (always) make detailed outlines"
12. "mull ideas over for a few days before writing"
13. "carry a small notebook or scrap paper with you"
14. "start writing when you think of the first sentence"
15. "if a deadline forces you to start before that, just say the most important sentence first"
16. "write about stuff you like"
17. "don't try to sound impressive"
18. "don't hesitate to change the topic on the fly"
19. "use footnotes to contain digressions"
20. "use anaphora to knit sentences together"
21. "read your essays out loud to see (a) where you stumble over awkward phrases and (b) which bits are boring (the paragraphs you dread reading)"
22. "try to tell the reader something new and useful"
23. "work in fairly big quanta of time"
24. "when you restart, begin by rereading what you have so far"
25. "when you finish, leave yourself something easy to start with"
26. "accumulate notes for topics you plan to cover at the bottom of the file"
27. "don't feel obliged to cover any of them"
28. "write for a reader who won't read the essay as carefully as you do, just as pop songs are designed to sound ok on crappy car radios"
29. "if you say anything mistaken, fix it immediately"
30. "ask friends which sentence you'll regret most"
31. "go back and tone down harsh remarks"
32. "publish stuff online, because an audience makes you write more, and thus generate more ideas"
33. "print out drafts instead of just looking at them on the screen"
34. "use simple, germanic words"
35. "learn to distinguish surprises from digressions"
36. "learn to recognize the approach of an ending, and when one appears, grab it."

---

### 7.2 *Write Simply* (March 2021) — Complete Verbatim Essay

> **Verified URL:** [https://paulgraham.com/simply.html](https://paulgraham.com/simply.html)

> March 2021
>
> I try to write using ordinary words and simple sentences.
>
> That kind of writing is easier to read, and the easier something is to read, the more deeply readers will engage with it. The less energy they expend on your prose, the more they'll have left for your ideas.
>
> And the further they'll read. Most readers' energy tends to flag part way through an article or essay. If the friction of reading is low enough, more keep going till the end.
>
> There's an Italian dish called saltimbocca, which means "leap into the mouth." My goal when writing might be called saltintesta: the ideas leap into your head and you barely notice the words that got them there.
>
> It's too much to hope that writing could ever be pure ideas. You might not even want it to be. But for most writers, most of the time, that's the goal to aim for. The gap between most writing and pure ideas is not filled with poetry.
>
> Plus it's more considerate to write simply. When you write in a fancy way to impress people, you're making them do extra work just so you can seem cool. It's like trailing a long train behind you that readers have to carry.
>
> And remember, if you're writing in English, that a lot of your readers won't be native English speakers. Their understanding of ideas may be way ahead of their understanding of English. So you can't assume that writing about a difficult topic means you can use difficult words.
>
> Of course, fancy writing doesn't just conceal ideas. It can also conceal the lack of them. That's why some people write that way, to conceal the fact that they have nothing to say. Whereas writing simply keeps you honest. If you say nothing simply, it will be obvious to everyone, including you.
>
> Simple writing also lasts better. People reading your stuff in the future will be in much the same position as people from other countries reading it today. The culture and the language will have changed. It's not vain to care about that, any more than it's vain for a woodworker to build a chair to last.
>
> Indeed, lasting is not merely an accidental quality of chairs, or writing. It's a sign you did a good job.
>
> But although these are all real advantages of writing simply, none of them are why I do it. The main reason I write simply is that it offends me not to. When I write a sentence that seems too complicated, or that uses unnecessarily intellectual words, it doesn't seem fancy to me. It seems clumsy.
>
> There are of course times when you want to use a complicated sentence or fancy word for effect. But you should never do it by accident.
>
> The other reason my writing ends up being simple is the way I do it. I write the first draft fast, then spend days editing it, trying to get everything just right. Much of this editing is cutting, and that makes simple writing even simpler.

---

### 7.3 *Write Like You Talk* (October 2015) — Complete Verbatim Rules & Passages

> **Verified URL:** [https://paulgraham.com/talk.html](https://paulgraham.com/talk.html)

> October 2015
>
> Here's a simple trick for getting more people to read what you write: write in spoken language.
>
> Something comes over most people when they start writing. They write in a different language than they'd use if they were talking to a friend. The sentence structure and even the words are different. No one uses "pen" as a verb in spoken English. You'd feel like an idiot using "pen" instead of "write" in a conversation with a friend.
>
> The last straw for me was a sentence I read a couple days ago: The mercurial Spaniard himself declared: "After Altamira, all is decadence." It's from Neil Oliver's A History of Ancient Britain. I feel bad making an example of this book, because it's no worse than lots of others. But just imagine calling Picasso "the mercurial Spaniard" when talking to a friend. Even one sentence of this would raise eyebrows in conversation. And yet people write whole books of it.
>
> Ok, so written and spoken language are different. Does that make written language worse?
>
> If you want people to read and understand what you write, yes. Written language is more complex, which makes it more work to read. It's also more formal and distant, which gives the reader's attention permission to drift. But perhaps worst of all, the complex sentences and fancy words give you, the writer, the false impression that you're saying more than you actually are.
>
> You don't need complex sentences to express complex ideas. When specialists in some abstruse topic talk to one another about ideas in their field, they don't use sentences any more complex than they do when talking about what to have for lunch. They use different words, certainly. But even those they use no more than necessary. And in my experience, the harder the subject, the more informally experts speak. Partly, I think, because they have less to prove, and partly because the harder the ideas you're talking about, the less you can afford to let language get in the way.
>
> Informal language is the athletic clothing of ideas.
>
> I'm not saying spoken language always works best. Poetry is as much music as text, so you can say things you wouldn't say in conversation. And there are a handful of writers who can get away with using fancy language in prose. And then of course there are cases where writers don't want to make it easy to understand what they're saying—in corporate announcements of bad news, for example, or at the more bogus end of the humanities. But for nearly everyone else, spoken language is better.
>
> It seems to be hard for most people to write in spoken language. So perhaps the best solution is to write your first draft the way you usually would, then afterward look at each sentence and ask "Is this the way I'd say this if I were talking to a friend?" If it isn't, imagine what you would say, and use that instead. After a while this filter will start to operate as you write. When you write something you wouldn't say, you'll hear the clank as it hits the page.
>
> Before I publish a new essay, I read it out loud and fix everything that doesn't sound like conversation. I even fix bits that are phonetically awkward; I don't know if that's necessary, but it doesn't cost much.
>
> This trick may not always be enough. I've seen writing so far removed from spoken language that it couldn't be fixed sentence by sentence. For cases like that there's a more drastic solution. After writing the first draft, try explaining to a friend what you just wrote. Then replace the draft with what you said to your friend.
>
> People often tell me how much my essays sound like me talking. The fact that this seems worthy of comment shows how rarely people manage to write in spoken language. Otherwise everyone's writing would sound like them talking.
>
> If you simply manage to write in spoken language, you'll be ahead of 95% of writers. And it's so easy to do: just don't let a sentence through unless it's the way you'd say it to a friend.
>
> Thanks to Patrick Collison and Jessica Livingston for reading drafts of this.

---

### 7.4 *How to Write Usefully* (February 2020) — Verbatim Core Principles & Editing Rules

> **Verified URL:** [https://paulgraham.com/useful.html](https://paulgraham.com/useful.html)

- **The Usefulness Formula (`Correctness × Importance × Novelty × Strength`) & Vaporous Academic Hedging:**
  > "What should an essay be? Many people would say persuasive. That's what a lot of us were taught essays should be. But I think we can aim for something more ambitious: that an essay should be useful."
  >
  > "To start with, that means it should be correct. But it's not enough merely to be correct. It's easy to make a statement correct by making it vague. That's a common flaw in academic writing, for example. If you know nothing at all about an issue, you can't go wrong by saying that the issue is a complex one, that there are many factors to be considered, that it's a mistake to take too simplistic a view of it, and so on."
  >
  > "Though no doubt correct, such statements tell the reader nothing. Useful writing makes claims that are as strong as they can be made without becoming false."
  >
  > "Precision and correctness are like opposing forces. It's easy to satisfy one if you ignore the other. The converse of vaporous academic writing is the bold, but false, rhetoric of demagogues. Useful writing is bold, but true."
  >
  > "Let's put them all together. Useful writing tells people something true and important that they didn't already know, and tells them as unequivocally as possible."
- **The Robert Morris Deletion Trick & "Loose, Then Tight" Editing ("Briars That Catch Your Sleeve"):**
  > "How can you ensure that the things you say are true and novel and important? Believe it or not, there is a trick for doing this. I learned it from my friend Robert Morris, who has a horror of saying anything dumb. His trick is not to say anything unless he's sure it's worth hearing. This makes it hard to get opinions out of him, but when you do, they're usually right."
  >
  > "Translated into essay writing, what this means is that if you write a bad sentence, you don't publish it. You delete it and try again. Often you abandon whole branches of four or five paragraphs. Sometimes a whole essay."
  >
  > "My strategy is loose, then tight. I write the first draft of an essay fast, trying out all kinds of ideas. Then I spend days rewriting it very carefully."
  >
  > "I've never tried to count how many times I proofread essays, but I'm sure there are sentences I've read 100 times before publishing them. When I proofread an essay, there are usually passages that stick out in an annoying way, sometimes because they're clumsily written, and sometimes because I'm not sure they're true. The annoyance starts out unconscious, but after the tenth reading or so I'm saying "Ugh, that part" each time I hit it. They become like briars that catch your sleeve as you walk past. Usually I won't publish an essay till they're all gone till I can read through the whole thing without the feeling of anything catching."
- **Skillful Qualification vs. Empty Hedging:**
  > "The fourth component of useful writing, strength, comes from two things: thinking well, and the skillful use of qualification. These two counterbalance each other, like the accelerator and clutch in a car with a manual transmission. As you try to refine the expression of an idea, you adjust the qualification accordingly. Something you're sure of, you can state baldly with no qualification at all, as I did the four components of useful writing. Whereas points that seem dubious have to be held at arm's length with perhapses."
  >
  > "Some say that qualifications weaken writing. For example, that you should never begin a sentence in an essay with "I think," because if you're saying it, then of course you think it. And it's true that "I think x" is a weaker statement than simply "x." Which is exactly why you need "I think." You need it to express your degree of certainty."
  >
  > "But qualifications are not scalars. They're not just experimental error. There must be 50 things they can express: how broadly something applies, how you know it, how happy you are it's so, even how it could be falsified. I'm not going to try to explore the structure of qualification here. It's probably more complex than the whole topic of writing usefully. Instead I'll just give you a practical tip: Don't underestimate qualification. It's an important skill in its own right, not just a sort of tax you have to pay in order to avoid saying things that are false. So learn and use its full range. It may not be fully half of having good ideas, but it's part of having them."
- **Simplicity & Avoiding Defensive "Bars on the Windows":**
  > "There's one other quality I aim for in essays: to say things as simply as possible. But I don't think this is a component of usefulness. It's more a matter of consideration for the reader. And it's a practical aid in getting things right; a mistake is more obvious when expressed in simple language. But I'll admit that the main reason I write simply is not for the reader's sake or because it helps get things right, but because it bothers me to use more or fancier words than I need to. It seems inelegant, like a program that's too long."
  >
  > "But I don't think you should explicitly forestall intentional misinterpretations in the body of an essay. An essay is a place to meet honest readers. You don't want to spoil your house by putting bars on the windows to protect against dishonest ones. The place to protect against intentional misinterpretations is in end-notes. But don't think you can predict them all. People are as ingenious at misrepresenting you when you say something they don't want to hear as they are at coming up with rationalizations for things they want to do but know they shouldn't. I suspect it's the same skill."

---

### 7.5 *Putting Ideas into Words* (February 2022) — Verbatim "Complete Stranger" Reading Test

> **Verified URL:** [https://paulgraham.com/words.html](https://paulgraham.com/words.html)

> "Writing about something, even something you know well, usually shows you that you didn't know it as well as you thought. Putting ideas into words is a severe test. The first words you choose are usually wrong; you have to rewrite sentences over and over to get them exactly right. And your ideas won't just be imprecise, but incomplete too. Half the ideas that end up in an essay will be ones you thought of while you were writing it. Indeed, that's why I write them."
>
> "It's not just having to commit your ideas to specific words that makes writing so exacting. The real test is reading what you've written. You have to pretend to be a neutral reader who knows nothing of what's in your head, only what you wrote. When he reads what you wrote, does it seem correct? Does it seem complete? If you make an effort, you can read your writing as if you were a complete stranger, and when you do the news is usually bad. It takes me many cycles before I can get an essay past the stranger. But the stranger is rational, so you always can, if you ask him what he needs. If he's not satisfied because you failed to mention x or didn't qualify some sentence sufficiently, then you mention x or add more qualifications. Happy now? It may cost you some nice sentences, but you have to resign yourself to that. You just have to make them as good as you can and still satisfy the stranger."
>
> "Putting ideas into words doesn't have to mean writing, of course. You can also do it the old way, by talking. But in my experience, writing is the stricter test. You have to commit to a single, optimal sequence of words. Less can go unsaid when you don't have tone of voice to carry meaning. And you can focus in a way that would seem excessive in conversation. I'll often spend 2 weeks on an essay and reread drafts 50 times. If you did that in conversation it would seem evidence of some kind of mental disorder. If you're lazy, of course, writing and talking are equally useless. But if you want to push yourself to get things right, writing is the steeper hill. [3]"
>
> "The reason I've spent so long establishing this rather obvious point is that it leads to another that many people will find shocking. If writing down your ideas always makes them more precise and more complete, then no one who hasn't written about a topic has fully formed ideas about it. And someone who never writes has no fully formed ideas about anything nontrivial."

---

### 7.6 *Good Writing* (May 2025) — Verbatim Principles on Rhythm, Rewriting & Truth

> **Verified URL:** [https://paulgraham.com/goodwriting.html](https://paulgraham.com/goodwriting.html)

> "There are two senses in which writing can be good: it can sound good, and the ideas can be right. It can have nice, flowing sentences, and it can draw correct conclusions about important things. It might seem as if these two kinds of good would be unrelated, like the speed of a car and the color it's painted. And yet I don't think they are. I think writing that sounds good is more likely to be right."
>
> "The best analogy for this phenomenon is when you shake a bin full of different objects. The shakes are arbitrary motions. Or more precisely, they're not calculated to make any two specific objects fit more closely together. And yet repeated shaking inevitably makes the objects discover brilliantly clever ways of packing themselves. Gravity won't let them become less tightly packed, so any change has to be a change for the better. [2]"
>
> "The reason is that it makes the essay easier to read. It's less work to read writing that flows well. How does that help the writer? Because the writer is the first reader. When I'm working on an essay, I spend far more time reading than writing. I'll reread some parts 50 or 100 times, replaying the thoughts in them and asking myself, like someone sanding a piece of wood, does anything catch? Does anything feel wrong? And the easier the essay is to read, the easier it is to notice if something catches."
>
> "When writing sounds good, it's mostly because it has good rhythm. But the rhythm of good writing is not the rhythm of music, or the meter of verse. It's not so regular. If it were, it wouldn't be good, because the rhythm of good writing has to match the ideas in it, and ideas have all kinds of different shapes. Sometimes they're simple and you just state them. But other times they're more subtle, and you need longer, more complicated sentences to tease out all the implications."
>
> "An essay is a cleaned up train of thought, in the same way dialogue is cleaned up conversation, and a train of thought has a natural rhythm. So when an essay sounds good, it's not merely because it has a pleasing rhythm, but because it has its natural one. Which means you can use getting the rhythm right as a heuristic for getting the ideas right. And not just in principle: good writers do both simultaneously as a matter of course. Often I don't even distinguish between the two problems. I just think Ugh, this doesn't sound right; what do I mean to say here? [3]"
>
> "So it's not quite right to say that better sounding writing is more likely to be true. Better sounding writing is more likely to be internally consistent. If the writer is honest, internal consistency and truth converge."
