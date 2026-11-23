# Curated Verified Sources: Image Generation, Scientific Figure & UI De-AI ("生图与视觉去AI味")

> **Provenance Mandate (`零AI自创铁律`)**: This document contains **zero AI-invented rules, zero synthetic Before/After examples, and zero unverified claims**. Every parameter, prompt, table, negative-prompt list, and critique item below is extracted directly from verified official documentation, peer-reviewed publications, commit-pinned open-source skills in `../upstream-skills/05-visual-image-figure-and-ui/`, or real community/netizen posts, with exact URLs and author/platform attributions attached to every single section.

---

## Part I — Image Generation De-AI & Photorealism ("生图去AI味与去塑料感")

### 1. Official Model Documentation & Parameters

#### 1.1 Midjourney Official Documentation — Raw Mode (`--style raw`) & Stylize (`--stylize` / `--s`)
- **Author / Platform**: Midjourney Official Help Center (`docs.midjourney.com`)
- **Verified URLs**:
  - Raw Mode: <https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw>
  - Stylize Parameter: <https://docs.midjourney.com/hc/en-us/articles/32196176868109-Stylize>
- **Documented Official Mechanics & Parameters**:
  - **`--style raw` (Raw Mode, v5.1+)**: Replaces Midjourney's default opinionated aesthetic pipeline ("automatic beautification") with a literal, less-processed pipeline so simple prompts produce more photographic/neutral results and detailed camera/lighting prompts retain direct control.
  - **`--stylize <0–1000>` / `--s <0–1000>` (Default: `100`)**: Controls how strongly Midjourney's default artistic aesthetic training is applied:
    - Low values (`--s 0` to `--s 50` / `--s 100`): Closely match prompt details with minimal automatic artistic embellishment.
    - High values (`--s 250` to `--s 1000`): Apply heavy Midjourney artistic stylization, moving further away from literal photographic prompts.

---

#### 1.2 Black Forest Labs Official Documentation — FLUX Raw Mode (`"raw": true`), Photographic Descriptors & Working Without Negative Prompts
- **Author / Platform**: Black Forest Labs Inc. (`docs.bfl.ai` / `black-forest-labs/flux`)
- **Verified URLs**:
  - Raw Mode (`FLUX1.1 [pro] Ultra`): <https://docs.bfl.ai/flux_models/flux_1_1_pro_ultra_raw.md>
  - Style, Aesthetics & Text: <https://docs.bfl.ai/guides/prompting_unified_style.md>
  - Technical Parameters (Negative Prompt Replacement): <https://docs.bfl.ai/guides/prompting_unified_technical.md>
  - Upstream Open-Weight Repo: <https://github.com/black-forest-labs/flux>
- **Verbatim Official Excerpts**:
  - **FLUX Raw Mode** (`flux_1_1_pro_ultra_raw.md`):
    > "FLUX1.1 [pro] also supports **Raw mode** for creators seeking authenticity. When enabled, Raw mode captures the genuine feel of candid photography, generating images with a less synthetic, more natural aesthetic. This mode significantly increases diversity in human subjects and enhances the realism of nature photography.
    > Enable Raw mode by setting `"raw": true` in your API request for more authentic, natural-looking results."
  - **Concrete Medium Over Vague Labels** (`prompting_unified_style.md`):
    > "Specify the medium, texture, and lighting: a flash snapshot, a grainy night photograph, or an anime poster. Concrete descriptions give more direction than labels such as 'aesthetic' or 'professional'."

  | Style | Official BFL Key Descriptors (`prompting_unified_style.md`) |
  | :--- | :--- |
  | **Modern Digital** | `“shot on Sony A7IV, clean sharp, high dynamic range”` |
  | **2000s Digicam** | `“early digital camera, slight noise, flash photography, candid, 2000s digicam style”` |
  | **80s Vintage** | `“film grain, warm color cast, soft focus, 80s vintage photo”` |
  | **Analog Film** | `“shot on Kodak Portra 400, natural grain, organic colors”` |

  - **Working Without Negative Prompts** (`prompting_unified_technical.md`):
    > "FLUX 3 Image has no negative prompt field. If a negative instruction gives an unwanted result, describe the intended scene directly: 'an empty promenade' instead of 'no crowds'."

  | Instead of... (BFL Official Table) | Write... |
  | :--- | :--- |
  | `“no people”` | `“empty”, “deserted”, “solitary”` |
  | `“no colors”` | `“monochrome”, “black and white”, “grayscale”` |
  | `“no text”` | `“clean surfaces”, “unmarked”, “blank”` |
  | `“no background clutter”` | `“plain studio backdrop in one color”` |
  | `“no modern elements”` | `“traditional”, “historical”, “period-accurate”` |

---

#### 1.3 HuggingFace `diffusers` Official `FluxPipeline` Documentation — `guidance_scale` Trade-Off
- **Author / Platform**: The HuggingFace Team (`huggingface/diffusers`, Apache-2.0)
- **Verified URL**: <https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/flux/pipeline_flux.py>
- **Verbatim Docstring**:
  > `guidance_scale` (`float`, *optional*, defaults to 3.5):
  > "Embedded guiddance scale is enabled by setting `guidance_scale` > 1. Higher `guidance_scale` encourages a model to generate images more aligned with `prompt` at the expense of lower image quality. Guidance-distilled models approximates true classifer-free guidance for `guidance_scale` > 1."

---

### 2. Open-Source Image De-Slop & Physical Realism Frameworks (Verbatim from `../upstream-skills/05-visual-image-figure-and-ui/`)

#### 2.1 Serge Shima (`smixs/visual-skills`) — *De-Slop: Killing the "AI Look"*
- **Author / License / Repo**: Serge Shima (`smixs`) · CC BY 4.0 · Commit `61a60d317f0fa0c3dc98902e58a7cb178838ae3f`
- **Verified URL**: <https://github.com/smixs/visual-skills/blob/61a60d317f0fa0c3dc98902e58a7cb178838ae3f/image/references/de-slop.md>
- **Local Copy**: `../upstream-skills/05-visual-image-figure-and-ui/visual-skills/image/references/de-slop.md`
- **Verbatim Diagnostic Table & Rules**:
  > "The premise: both model families carry a strong prior toward an idealized image. Left alone they beautify — skin loses pores, faces gain symmetry, clothes lose creases, backgrounds gain saturation. Anything in the reference that differs from that ideal is quietly discarded unless you escalate it."

  | Axis | What the model reaches for | What a real reference usually has |
  |---|---|---|
  | Eyes | large, round, wide-open, symmetric | narrow, hooded, monolid, one eye smaller |
  | Face | V-line jaw, doll proportions, mirror symmetry | long or flat midface, visible asymmetry |
  | Skin | poreless, glowing, even tone | pores, peach fuzz, redness zones, uneven tone |
  | Body | idealized silhouette | flat, square, heavy, or simply ordinary |
  | Clothing | tighter, newer, more skin | the exact coverage and wear of the reference |
  | Hair | volumized, glossy, every strand placed | flatter, clumped, flyaways, dull ends |
  | Stance | model pose, chin up | the awkward real stance from the reference |
  | Casting | idol / influencer look | an ordinary person |
  | Background | saturated, tidy, gradient | muted, cluttered, one named hex |
  | Extras | adds earrings, props, signage, text | explicitly absent |

  - **Boosters Banned from Positive Slots (§3, verbatim)**:
    > "These words push the prior harder, they do not add fidelity: `4K`, `8K`, `ultra-detailed`, `hyper-detailed`, `ultra-realistic`, `photorealistic render`, `masterpiece`, `best quality`, `sharp focus`, `crisp`, `intricate detail`, `flawless`, `stunning`, `perfect`."
  - **Capture Pipeline Instead of Adjectives (§4, verbatim)**:

  | Medium | What to state | Residue to ask for |
  |---|---|---|
  | Video frame grab | grabbed from handheld footage, not a photo | soft detail, mild compression blocking, slight motion smear |
  | Film scan | 35mm colour negative, lab scan | visible grain, halation around highlights, soft blacks |
  | Phone photo | phone camera, auto HDR off | smeared shadow noise, faint edge halo, slightly flat tone |
  | Mirrorless / DSLR still | natural light, no flash, no retouch | fine sensor noise, natural falloff, unpolished skin |

  - **Located Imperfections (§5) & Grading (§6, verbatim)**:
    > "An imperfection without a location gets ignored or sprayed everywhere. Name the place:
    > - skin — `'pores across the nose and cheeks, redness at the nostril wings, one mole below the left jaw'`
    > - hair — `'two flyaways above the crown, ends clumped on the right shoulder'`
    > - fabric — `'creases at the elbow bend, collar sitting slightly askew on the left'`
    > - environment — `'scuffed baseboard behind the subject, uneven paint on the wall'`
    > - optics — `'one blown highlight on the forehead, slight motion blur on the near hand'`"
    > "Ban the glow family in `Constraints`: HDR, bloom, high clarity, luminous or radiant skin, glossy hair highlights, perfectly even background."

---

#### 2.2 `keng1304/awesome-ai-visual-realism-prompts` — *Physical Realism Vocabulary*
- **Author / License / Repo**: `keng1304` (`tzukao.com`) · MIT · Commit `b850b0ef1d774cdeed85f906397f93f5f918ac41`
- **Verified URL**: <https://github.com/keng1304/awesome-ai-visual-realism-prompts/blob/b850b0ef1d774cdeed85f906397f93f5f918ac41/docs/01-physical-realism.md>
- **Local Copy**: `../upstream-skills/05-visual-image-figure-and-ui/awesome-ai-visual-realism-prompts/docs/01-physical-realism.md`
- **Verbatim Physical Layers & Prompt Blocks**:
  - **Layer 1 — Skin (Subsurface Scattering)**:
    ```text
    subsurface scattering on skin, faint translucency at ears and nostrils,
    soft warm bloom under direct light, visible pores and fine vellus hair,
    realistic skin texture with subtle imperfections,
    no plastic shine, no airbrushed look
    ```
    - Anti-slop checklist: ❌ `"smooth skin"` (too smooth = uncanny), ❌ `"perfect skin"` (no pores = doll), ❌ `"beautiful complexion"` (vague) → ✅ `"natural skin texture, fine pores visible at 1:1 crop, subsurface scattering"`.
  - **Layer 2 — Liquids (Fresnel + Caustics)**:
    ```text
    fresnel reflection on water surface, caustic light patterns on the pool floor,
    realistic refraction through glass, surface tension visible at the meniscus,
    droplets with proper specular highlights, no flat painted water
    ```
  - **Layer 3 — Cloth (Anisotropic Weave)**:
    ```text
    visible fabric weave structure, anisotropic specular highlights on silk,
    natural wrinkle patterns following gravity and body movement,
    realistic cloth physics, no flat-shaded fabric, no painted-on clothing
    ```
  - **Layer 4 — Contact Physics (Ambient Occlusion & Micro-Bounce)**:
    ```text
    realistic contact shadows at the base, subtle color bounce from
    the red surface onto the white object, soft deformation where the
    hand grips, no floating objects, no missing contact shadows
    ```
  - **Layer 5 — Anatomy & Posture Negative Prompts**:
    - Hands: `extra fingers, fused fingers, deformed hands, mannequin hands`
    - Eyes: `glassy eyes, doll eyes, dead stare, missing catchlight`

---

### 3. Verified English Community Guides & Netizen Techniques

#### 3.1 The Raw Camera Filename Prefix Exploit (`IMG_xxxx.CR2` / `IMG_xxxxxxxx.HEIC`)
- **Authors / Platforms**:
  - Matt Growcoot (*PetaPixel*, Apr 7, 2025), quoting X creators Min Choi (`@minchoi`), MetricsMule (`@metricsmule`), Levi Foster (`@cybermynd`), Nick St. Pierre (`@nickfloats`), and Reddit user `u/Salmontunabear`: <https://petapixel.com/2025/04/07/people-are-using-camera-filenames-to-make-midjourney-more-photorealistic/>
  - Reddit empirical test on `r/StableDiffusion`: <https://www.reddit.com/r/StableDiffusion/comments/1fxdm1n/i_tested_the_use_of_a_random_filename_1234jpg_to/>
- **Verbatim Quotes & Documented Prompts**:
  - **Matt Growcoot / Min Choi** (*PetaPixel*):
    > "Choi chose CR2, Canon's previous generation RAW image file format. For example, Choi used the prompt `'IMG_7249.CR2'` followed by `'casual selfie at X.'` The results are astonishing, producing images that are almost impossible to detect as synthetic."
  - **MetricsMule (`@metricsmule`, Apr 5, 2025, quoted verbatim in *PetaPixel*)**:
    > `"Want a cheat code to use in the Midjourney v7 update? Use this to start your prompt 👉 IMG_9854.CR2: Try it first by pasting that and nothing else. Then try it again by adding a specific subject after the :"`
  - **Levi Foster (`@cybermynd`, Apr 4, 2025, quoted verbatim in *PetaPixel*)**:
    > `"AI is trained on photos. Many real photos have file names like IMG_02202021.HEIC — so if you feed it just a typical file name in the prompt and that’s it, it will generate a realistic looking picture because the data that corresponds is always real."` (Example prompt cited: `"IMG_07242020.HEIC"`).

---

#### 3.2 Fixing FLUX Waxy/Plastic Skin, Guidance Scale, Upscale Melting & "Flux Chin" (Cleft Chin)
- **Authors / Platforms / Verified URLs**:
  - `r/StableDiffusion`: *Any prompting ideas to get more realistic skin?* — <https://www.reddit.com/r/StableDiffusion/comments/1f1ouq6/any_prompting_ideas_to_get_more_realistic_skin/>
  - `r/comfyui`: *Plastic skin using Flux? Fix with this workflow* — <https://www.reddit.com/r/comfyui/comments/1eyyy35/plastic_skin_using_flux_fix_with_this_workflow/>
  - `r/StableDiffusion`: *I wanted to achieve some natural look with Flux* — <https://www.reddit.com/r/StableDiffusion/comments/1frrpnl/i_wanted_to_achieve_some_natural_look_with_flux/>
  - `r/FluxAI`: *How to create a consistent images with realistic skin* — <https://www.reddit.com/r/FluxAI/comments/1usckp9/how_to_create_a_consistent_images_with_realistic/>
  - Civitai Resource: `AIDigitalMediaAgency`, *Photorealistic Skin ⛔️ No plastic [FLUX]* (34,171+ downloads) — <https://civitai.com/models/1157318/photorealistic-skin-no-plastic-flux>
- **Community-Documented Fixes (Extracted from the Verified Threads Above)**:
  1. **Lower Distilled Guidance (`FluxGuidance`)**: Dropping `guidance` from the default `3.5–4.0` down to **`1.5 – 2.5`** (commonly `1.8 – 2.3` on `FLUX.1-dev`) reduces commercial studio over-smoothing and porcelain/plastic sheen.
  2. **Low-Denoise Upscaling**: High-denoise second passes melt away microscopic pores and freckles; users keep detailer/upscaler denoise low (`0.15 – 0.20`) or pair alternative ComfyUI sampler/scheduler combinations (e.g., `deis` + `ddim_uniform`) to preserve micro-contrast.
  3. **Countering "Flux Chin" (Prominent Cleft / Butt Chin)**: Community threads on `r/StableDiffusion` and `r/FluxAI` document that `FLUX.1-dev` strongly associates "beautiful face" captions with a cleft chin due to VLM captioning/dataset bias, and that positive prompt phrasing alone is unreliable, leading creators to use dedicated anti-cleft/skin LoRAs (e.g., Civitai `1157318` trigger word `aidmarealisticskin` at strength `0.5 - 0.85`, or community `"AntiFlux - Chin"` / `"DaChinFix"` LoRAs).

---

#### 3.3 Banishing "Midjourney Glow" & Thinking Like a Camera
- **Platforms / Verified URLs**:
  - `r/midjourney`: *Can anyone give me some advice on how to generate...* — <https://www.reddit.com/r/midjourney/comments/1frc9o0/can_anyone_give_me_some_advice_on_how_to_generate/>
  - `r/promptingmagic`: *From Amateur to Pro: The Complete Midjourney...* — <https://www.reddit.com/r/promptingmagic/comments/1mynjq2/from_amateur_to_pro_the_complete_midjourney/>
  - `r/Aiarty`: *The Ultimate Guide to Photorealism in Midjourney* — <https://www.reddit.com/r/Aiarty/comments/1qwhkpe/the_ultimate_guide_to_photorealism_in_midjourney/>
- **Community-Documented Rules & Prompts**:
  - Avoid digital-art trigger buzzwords (`photorealistic`, `ultra-realistic`, `8K`, `hyper-detailed`, `high definition`) which activate glossy CGI/digital-painting training clusters ("Midjourney glow").
  - Combine `--style raw` with low stylize (`--s 50` to `--s 250`) and explicit camera body + focal length + film stock + natural light physics (e.g., `Canon EOS R5`, `Sony A7R V`, `Hasselblad X1D`, `35mm lens`, `85mm f/1.4 lens`, `Kodak Portra 400`, `Fujifilm Pro 400H`, `Ilford HP5`).
  - Community Portrait & Street Templates cited in guides:
    - `Candid environmental portrait of an elderly artisan in a dusty workshop, soft natural window light illuminating side of face, fine skin texture and wrinkles, shot on Sony A7R V, 85mm f/1.4 lens, Kodak Portra 400, documentary style --ar 4:5 --style raw --v 6.1`
    - `Street photography of a rainy Tokyo crosswalk at night, neon reflections bouncing off wet asphalt, shot on Fujifilm X-T5, 35mm lens, subtle film grain, natural motion blur in background --ar 16:9 --style raw --v 6.1`

---

#### 3.4 Stable Diffusion (SD 1.5 / SDXL / SD 3.5) Negative Prompt Mechanics & Token Lists
- **Author / Platform**: Anthony Clicheroux (`stablediffusion.fr`, updated Sept 28, 2026)
- **Verified URL**: <https://stablediffusion.fr/zh/guide/negative-prompt>
- **Verbatim Extracted Lists & Technical Boundaries**:
  - **General Quality (SD 1.5, SDXL)**:
    ```text
    blurry, low quality, lowres, jpeg artifacts, watermark, text, signature, cropped, out of frame
    ```
  - **People & Portraits**:
    ```text
    deformed, bad anatomy, extra fingers, missing fingers, extra limbs, mutated hands, poorly drawn face, asymmetric eyes
    ```
  - **Photography (Anti-Render / Anti-CGI)**:
    ```text
    painting, drawing, illustration, cartoon, 3d render, cgi, oversaturated, overexposed
    ```
  - **Documented Failure Conditions (verbatim)**:
    - **CFG = 1 / Distilled Turbo Models**: *"CFG 设为 1：负面提示词在原理上就被忽略。SD 1.5 和 SDXL 请用 5 到 8。SDXL Turbo 不使用 CFG，会忽略负面提示词；LCM LoRA 以 CFG 1 到 2 运行，几乎不受它影响。Stable Diffusion 3.5 Large Turbo 同样不使用 CFG，负面提示词也会被忽略。"*
    - **Weight Cap**: Keep `(term:weight)` below `1.5` (*"超过 1.5 后，模型会为了服从而扭曲其他部分"*), and limit negative prompts to 10–20 targeted tokens rather than long copy-pasted salads.

---

### 4. Verified Chinese Community Guides ("中文社区生图去塑料感与反精致实战")

#### 4.1 什么值得买 (SMZDM) — *"反精致"法则、光学瑕疵全局滤镜与精确光圈控制*
- **Title / Author / Platform**: *《FLUX三个版本怎么选哪个强？写实图消除塑料感方法都在这》* · 什么值得买软件技能频道（聚合57位全网作者实测）
- **Verified URL**: <https://post.m.smzdm.com/p/a70rz7zl/>
- **Verbatim Quotes**:
  > "“塑料感”是AI写实图像最大的痛点。很多人习惯堆“超写实、8K、极致细节”这类词，结果反而越描越假。核心问题在于：**AI默认会生成左右对称、皮肤完美无瑕的假人，越强调完美，越像CG建模。**"
  > "根据多个来源的实测经验，真正管用的方向是“反精致”——用真实的摄影术语替代模糊的渲染词。具体做法是：
  > - **指定具体的相机型号和镜头焦段**，比如“shot on Canon EOS R5, 85mm f/1.4”；
  > - **添加不完美的物理细节**，如“可见的皮肤毛孔、凌乱的头发、轻微的运动模糊”；
  > - **指定光线类型**，如“窗边侧漫射自然光、戏剧性光影”，避免平光照亮全场。
  > 有经验的创作者还会加入“光学瑕疵”作为全局滤镜——胶片颗粒、高感光度噪点、轻微色散或镜头眩光，这些真实相机在复杂环境下必然产生的缺陷，反而是骗过人眼的关键。"
  > "除了“反精致”，**景深控制**也是决定写实感的重要因素。光圈数值和虚化效果刚好相反：数字越小虚化越强（如f/1.2、f/2.8适合人像特写），数字越大背景越清晰（如f/11、f/16适合完整交代环境）。与其反复写“虚化背景”这种模糊形容词，不如直接写具体的光圈参数，AI能更精准地识别和执行。"

---

#### 4.2 稀土掘金 (Juejin) — *"数字蜡像"特征诊断（高饱和 + 失真磨皮 + 毛玻璃假虚化）*
- **Title / Author / Platform**: *《告别塑料感：FLUX.1 Krea，那个让AI图像不再“AI”的模型》* · 作者：`小墨同学boy`（稀土掘金，2025-08-02）
- **Verified URL**: <https://juejin.cn/post/7533459820096913450>
- **Verbatim Quote**:
  > "你一定见过那种一眼就能认出的AI画作：过度饱和的色彩，光滑到失真的皮肤，以及无论前景多清晰、背景都仿佛隔着一层毛玻璃的模糊感。这种被戏称为“数字蜡像”的风格，曾是我们判断一张图片是否由AI生成的潜规则。"
  > "模型不再盲目追求传统美学评分器上的高分，而是引入了**人类反馈强化学习（RLHF）**……过滤掉那些技术上正确但美学上平庸的方案，生成的结果自然更贴近人类摄影师的审美直觉。"

---

## Part II — Scientific Figure De-AI, Academic Integrity & Visualization Standards ("科研绘图去AI味与学术规范")

### 5. Official Publisher Policies & Research Integrity Case Studies

#### 5.1 Nature Portfolio / Springer Nature Official Editorial Policy on Generative AI in Images & Figures
- **Author / Organization**: Nature Portfolio / Springer Nature
- **Verified URLs**:
  - <https://www.nature.com/nature-portfolio/editorial-policies/ai>
  - <https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation>
- **Documented Policy Rules**:
  - Nature Portfolio **prohibits the use of generative AI images, videos, or figures** in published manuscripts (covering both conceptual scientific illustrations and primary research data such as microscopy, gels, blots, or clinical images), except in narrow editor-approved cases where AI itself is the subject of study or via contracted agencies with full legal provenance.
  - Non-generative machine-learning tools used to process/analyze data images must be explicitly disclosed in the figure caption/Methods, while standard code-driven charts/flowcharts derived accurately from real data remain permitted.

---

#### 5.2 Dr. Elisabeth Bik (*Science Integrity Digest*) — Anatomy of Botched Midjourney Scientific Figures
- **Author / Platform**: Dr. Elisabeth Bik (*Science Integrity Digest*, Feb 15, 2024), analyzing Xinyu Guo et al., *Frontiers in Cell and Developmental Biology* 2024 (`DOI: 10.3389/fcell.2023.1339390`, subsequently retracted)
- **Verified URL**: <https://scienceintegritydigest.com/2024/02/15/the-rat-with-the-big-balls-and-enormous-penis-how-frontiers-published-a-paper-with-botched-ai-generated-images/>
- **Verbatim Documented Failure Modes of Generative AI Scientific Diagrams**:
  > "The figures in the paper were generated by the AI tool Midjourney, which generated some pretty, but nonsensical, illustrations with unreadable text. It appears that neither the editor nor the two peer reviewers looked at the figures at all."
  > "The authors disclose that the figures were generated by Midjourney, but the images are – ahem – anatomically and scientifically incorrect. Figure 1 features an illustration of a rat, sitting up like a squirrel, with four enormous testicles and a giant … penis? The figure includes indecipherable labels like `'testtomcels'`, `'senctolic'`, `'dissilced'`, `'iollotte sserotgomar'` and `'diƨlocttal stem ells'`."
  > "Figure 2 appears to show an impressive scientific diagram of the JAK-STAT signaling pathway. Or does it explain how to make a donut with colorful sprinkles? Again the words and numbers are made up. What do `'signal bıidimg the recetein'`, `'Sinkecler'`, `'dimimeriom eme'`, `'Tramioncatiion of 2xℇpens'`, `'ↄ'`, and `'proprounization'` mean?"

---

### 6. Peer-Reviewed Visualization Standards & Open-Source Scientific Figure Skills

#### 6.1 Rougier, Droettboom & Bourne (2014) — *Ten Simple Rules for Better Figures*
- **Authors / Venue / License**: Nicolas P. Rougier (INRIA), Michael Droettboom (STScI), Philip E. Bourne (NIH) · *PLOS Computational Biology* 10(9): e1003833 (Sept 2014) · CC0 Public Domain
- **Verified URLs**:
  - Paper: <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833> (DOI: `10.1371/journal.pcbi.1003833`)
  - Official Companion Code Repo (`../upstream-skills/05-visual-image-figure-and-ui/ten-rules/`, SHA `75ecbdc2ce197564ed77c21a4492ae89ccab0ca8`): <https://github.com/rougier/ten-rules>
- **Verbatim Excerpts of Key Anti-Default / Anti-Chartjunk Rules**:
  1. **Rule 1: Know Your Audience** — *"Identify, as early as possible in the design process, the audience and the message the visual is to convey."*
  2. **Rule 2: Identify Your Message** — *"Only after identifying the message will it be worth the time to develop your figure."*
  3. **Rule 3: Adapt the Figure to the Support Medium** — *"Ideally, each type of support medium requires a different figure, and you should abandon the practice of extracting a figure from your article to be put, as is, in your oral presentation."*
  4. **Rule 4: Captions Are Not Optional** — *"The caption explains how to read the figure and provides additional precision for what cannot be graphically represented."*
  5. **Rule 5: Do Not Trust the Defaults** — *"You can usually recognize the specific style of each software package (Matlab, Excel, Keynote, etc.) or library (LaTeX, matplotlib, gnuplot, etc.) thanks to the choice of these default settings... In other words, they are good enough for any plot but they are best for none. All plots require at least some manual tuning."*
  6. **Rule 6: Use Color Effectively** — *"Ask yourself, 'Is there any reason this plot is blue and not black?' If you don't know the answer, just keep it black... Do not use the default colormap (e.g., jet or rainbow) unless there is an explicit reason to do so."*
  7. **Rule 7: Do Not Mislead the Reader** — *"You can also make explicit choices that are wrong by design, such as using pie charts or 3-D charts to compare quantities. These two kinds of plots are known to induce an incorrect perception of quantities."*
  8. **Rule 8: Avoid “Chartjunk”** — *"Chartjunk refers to all the unnecessary or confusing visual elements found in a figure that do not improve the message (in the best case) or add confusion (in the worst case)... Edward Tufte argues that any decorations that do not tell the viewer something new must be banned: 'Regardless of the cause, it is all non-data-ink or redundant data-ink, and it is often chartjunk.'"*
  9. **Rule 9: Message Trumps Beauty** — *"There exists a myriad of online graphics in which aesthetic is the first criterion and content comes in second place. Even if a lot of those graphics might be considered beautiful, most of them do not fit the scientific framework. Remember, in science, message and readability of the figure is the most important aspect while beauty is only an option."*
  10. **Rule 10: Get the Right Tool** — *"The software or library you're using to make a visualization can be different from the software or library you're using to conduct your research."*

---

#### 6.2 Open-Source Academic Figure Skills (`scipilot-figure-skill`, `SCIFIG`, `happy-figure-skill`)
- **Verified Upstream Repositories (Saved Verbatim in `../upstream-skills/05-visual-image-figure-and-ui/`)**:
  1. **`Haojae/scipilot-figure-skill`** (MIT, 2,892 stars, Commit `43098ddb9e6a6d142218540c114f9ed38922fc42`): <https://github.com/Haojae/scipilot-figure-skill/blob/43098ddb9e6a6d142218540c114f9ed38922fc42/references/viz_pitfalls.md>
     - Documents 18 active-interception reviewer pitfalls (`P1`–`P18`): P1 bare mean bar charts hiding `n` and distributions (`PLoS Biology` / `Nature Methods` ban), P2 misleading dual Y-axes, P3 pie & 3D charts, P4 truncated Y-axes, P5 missing colorbars, P6 connecting discrete categories with lines, P7 excessive color, P10 chartjunk, P13 red-green colorblindness failure, P14 `rainbow`/`jet` colormaps, P16 CJK/minus-sign tofu boxes, P17 clipped text/overlapping legends, P18 misaligned multi-panel labels.
  2. **`nrokh/ScientificFigures` (SCIFIG)** (Nataliya Rokhmanova & Andrew K. Schulz, Max Planck Institute for Intelligent Systems, MIT, Commit `57359c0ef3dd15c7daaf5d7172cf45f9d752e5f4`): <https://github.com/nrokh/ScientificFigures/blob/57359c0ef3dd15c7daaf5d7172cf45f9d752e5f4/SCIFIGwithAI/README.md>
     - Verbatim 6-attribute SCIFIG Figure Rubric for coding agents: `1. Scale & Resolution`, `2. Units & Labels`, `3. Colors (muted by default, saturated only for emphasis)`, `4. Emphasis (never imply a trend that isn't in the data)`, `5. Ink:Content Ratio (remove grid lines, boxes, redundant legends)`, `6. Accessibility (deuteranopia/protanopia/tritanopia + grayscale check)`, plus strict rule: *"Never change data values, filtering, or statistics while editing a figure."*
  3. **`BAIKEMARK/happy-figure-skill`** (CC BY-NC-SA 4.0, Commit `6292597250ed874d65756d13a492f6eefe07fb65`): <https://github.com/BAIKEMARK/happy-figure-skill/blob/6292597250ed874d65756d13a492f6eefe07fb65/references/prompt-quality-check.md>
     - Enforces strict text whitelist (`图中所有可见文字只能使用以下内容`) to prevent gibberish AI text in schematic diagrams and forbids asking image models to fabricate data curves, measurements, microscopy, or experimental photo evidence.

---

## Part III — UI, Web & Frontend Visual De-AI ("UI与网页视觉去AI味 / Anti-AI-Slop Design")

### 7. Official & High-Adoption Open-Source Anti-AI-Slop UI Skills

#### 7.1 Anthropic Official `frontend-design` Skill — 5-Cluster Calibration of AI-Generated UI Tells
- **Author / License / Repo**: Anthropic (`anthropics/skills`) · Apache-2.0 · Commit `e4bb5d960d87126ff3b3a8af1a104b7db67560ba`
- **Verified URL**: <https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/frontend-design/SKILL.md>
- **Local Copy**: `../upstream-skills/05-visual-image-figure-and-ui/anthropics-skills/skills/frontend-design/SKILL.md`
- **Verbatim Calibration List of Generated-Page Tells**:
  > "Avoid these default typographic treatments; they are the commonest tells of a generated page:
  > - Accenting just a single word or phrase in a headline, like putting one word in italic/bold or a different color.
  > - Using all caps for labels.
  > - Adding unnecessary typographic labels above content."
  >
  > "For calibration, AI-generated design right now clusters around some traits:
  > 1. a warm cream background (near `#F4F1EA`) with a high-contrast serif display and a terracotta or warm-clay accent (often near `#D97757` — Anthropic's own Claude-interaction accent, so on a user's brief it reads as a tell);
  > 2. a near-black background with a single bright acid-green or vermilion accent;
  > 3. a broadsheet-style layout with hairline rules, zero border-radius, and dense newspaper-like columns;
  > 4. the SaaS-card kit: content chopped into identical rounded cards, one border-radius on everything regardless of hierarchy, the same soft grey shadow (`rgba(0,0,0,.1)`) under each, and gradient washes as decoration;
  > 5. template chrome that appears whatever the subject: a tracked-out ALL-CAPS eyebrow label above every heading; meta strings joined with middle dots (`'A · B · C'`); labels built as `'WORD — fragment'` with a spaced em dash; tinted near-black (`#0B0B0B`, `#111`) standing in for black; a monospace face for small data labels; a `'→'` appended to link and button text."

---

#### 7.2 Together AI / Nutlope `hallmark` (59,708 Stars) — Non-Waivable "Floor" Against Generated UI
- **Author / License / Repo**: Hassan El Mghari (`Nutlope`) / Hallmark Contributors (Powered by Together AI) · MIT · Commit `04977e15f3dfd6ee4b74c887dac3eb52665d6c92`
- **Verified URL**: <https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/skills/hallmark/SKILL.md>
- **Local Copy**: `../upstream-skills/05-visual-image-figure-and-ui/hallmark/skills/hallmark/SKILL.md`
- **Verbatim Excerpts from `The Floor` (Rules 1–14)**:
  - *"3. Never one italic word inside a roman heading."*
  - *"8. Never an invented metric, testimonial, logo wall or case-study count."*
  - *"9. Never an eyebrow, and never a label in tracked capitals or small caps: labels, captions, table heads, tags and nav links are the body face (or the theme's label face), a step smaller, sentence or lower case, untracked."*
  - *"10. Never middle-dot-joined meta strings, arrows glued to link text, or decorative status dots."*
  - *"11. Never a purple-to-blue gradient, a card inside a card, an emoji as an icon, or a hand-drawn browser or OS window."*

---

#### 7.3 `h3nryprod01/design-taste` & `Ferousco-dev/anti-slop-design` — CSS, Copy & Imagery Bans
- **Verified Upstream URLs**:
  - `h3nryprod01/design-taste` (`reference/anti-slop.md`, MIT/Apache-2.0, Commit `3218793173ba67d88840296a45b0aec189d0a224`): <https://github.com/h3nryprod01/design-taste/blob/3218793173ba67d88840296a45b0aec189d0a224/reference/anti-slop.md>
  - `Ferousco-dev/anti-slop-design` (`references/10-image-media-patterns.md`, MIT, Commit `484f99edef59020e564cf28fdf77aaca27b32c3f`): <https://github.com/Ferousco-dev/anti-slop-design/blob/484f99edef59020e564cf28fdf77aaca27b32c3f/skills/anti-slop-design/references/10-image-media-patterns.md>
- **Verbatim Documented UI & Media Tells**:
  - **CSS / Structural Tells (`h3nryprod01/design-taste`)**:
    - Side-stripe borders (`border-left` / `border-right` > 1px colored card accents)
    - Gradient text (`background-clip: text` with gradient background)
    - "Ghost-card" pairing (`border: 1px solid X` + wide `box-shadow` with blur ≥ 16px)
    - Over-rounding (`border-radius: 32px+` on cards/sections)
    - `<div>`-built fake product screenshots / fake terminals in heroes (*"It is the #1 LLM-design Tell"*)
    - Fake version footers (`v0.6.2-rc.1`, `last sync 4s ago · main`) and decorative colored status dots
  - **Web Imagery & Icon Slop (`Ferousco-dev/anti-slop-design`, `10-image-media-patterns.md`)**:
    - Never generate AI human faces for customer testimonials or team photos.
    - Ban generic stock clichés (*"Diverse colleagues laughing around a laptop"*, *"A person pointing at a whiteboard covered in meaningless diagrams"*).
    - Ban unmodified "Corporate Memphis" flat faceless vector packs and semantic-free filler icons (*"A shield for 'security', a lightning bolt for 'speed', a globe for 'global'"*) or emoji as UI icons.

---

### 8. Developer Essays & Hacker News Empirical Discussions on UI Slop

#### 8.1 Ken Imoto (*DEV Community* / *Zenn*) — *3 UI Slop Patterns in AI UI Generators*
- **Author / Platform**: Ken Imoto (`kenimo49`) · *DEV Community* (drawn from Chapter 7 of *AI Slop Escape Guide* on Zenn)
- **Verified URL**: <https://dev.to/kenimo49/3-ui-slop-patterns-in-ai-ui-generators-purple-gradients-inter-fonts-uniform-cards-11l6>
- **Verbatim Three Convergence Patterns & Published Slop Score**:
  1. **Pattern 1: Purple Gradient Syndrome** — *"Prompt any 2026 generator for a landing page hero and you get the same background. A diagonal gradient from purple to blue, sometimes with a floating geometric shape in the top right. Left-aligned heading, right-side mockup image... Escape path: Pick a background that is not a gradient and not pure white. Textured off-whites, warm earth tones, deep single-color navy."*
  2. **Pattern 2: Inter Font Dependency Syndrome** — *"Shipping an Inter-only product in 2026 is a tell: 'we did not spend one hour on type.' Escape path: Pair Inter with something that announces intent. Serif + mono for a developer tool. Display + grotesque for consumer."*
  3. **Pattern 3: Uniform Rounded Card Syndrome** — Verbatim Tailwind pattern flagged by Ken Imoto:
     ```html
     <!-- The exact Tailwind pattern every generator reaches for -->
     <div class="rounded-lg shadow-md p-6">
       <Icon class="h-10 w-10 text-indigo-500" />
       <h3 class="mt-4 font-semibold">...</h3>
       <p class="mt-2 text-sm text-gray-600">...</p>
     </div>
     ```
     *"Escape path: Break the grid. One hero card at 2× size. One row of three, then one row of two, then one standalone."*
  - **Ken Imoto's Published Weighted Slop Score Formula (verbatim)**:
    ```text
    Slop Score = (Gradient_penalty × 0.30) + (Inter_penalty × 0.25) + (Grid_uniformity × 0.20)
               + (Color_convergence × 0.15) + (Element_predictability × 0.10)
    ```
    (`0–30`: Distinctive · `31–60`: Mostly generic · `61–80`: Typical AI slop · `81–100`: Pure template)

---

#### 8.2 Volpe (`envs.net`) & Hacker News — Toolkit Anchoring (`Qt` Style) & Why Negative Bans Shift to the Second-Most-Likely Cliché
- **Authors / Platforms / Verified URLs**:
  - Volpe (`envs.net`, June 12, 2026): *Slightly reducing the sloppiness of AI generated front end* — <https://envs.net/~volpe/blog/posts/reduce-slop.html>
  - Hacker News Thread (`219 points`, posted by `FergusArgyll`): <https://news.ycombinator.com/item?id=48504912>
  - Hacker News Thread on Anti-Slop System Prompts: <https://news.ycombinator.com/item?id=47050348>
- **Verbatim Quotes**:
  - **Volpe** (`envs.net/~volpe/blog/posts/reduce-slop.html`):
    > "Slop is not a distinct style, it can be overlaid on top of many others. Even when I got it to make a page to look like X, it looked like X with slop. Only one generation stuck out to me. Simply asking it to make it look like a Qt app - to my tasteless eyes - removed almost all feeling of slop."
  - **`voxleone` on Hacker News (`item?id=48505610`) explaining why `Qt` works**:
    > "Qt is heavily represented in training data. Qt has existed for decades and the model has likely seen Qt tutorials, screenshots, source code, discussions, etc. As a result, 'Qt application' is a highly coherent concept in the latent space. 'Qt app' is almost like a named distribution."
  - **`lich_king` on Hacker News (`item?id=47051624`) on the second-order cliché trap of anti-slop prompts**:
    > "Keep in mind that LLMs are trying to predict the most likely token. If your prompt prohibits the most likely token, they output the next most likely token. So, attempts to force creativity by prohibiting cliches just create another cliche."
