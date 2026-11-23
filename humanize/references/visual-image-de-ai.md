# Visual & Image Generation De-AI Guide (生图与摄影视觉去 AI 味)

Strip the synthetic "AI look" (塑料蜡质感、糖水片 HDR、绝对居中构图、假笑凝视、虚化滥用) from generated photography, editorial portraits, lifestyle imagery, and commercial scenes.

> **Module Cross-Navigation ([../SKILL.md](../SKILL.md)):** Use this guide for photorealistic, editorial, documentary, and product image generation (`:image`, `:photo`, `:mj`, `:flux`). For academic architecture diagrams, *Nature*/*NeurIPS* plots, and web/SaaS frontend interfaces, switch to [scientific-figures-and-ui-de-ai.md](scientific-figures-and-ui-de-ai.md).

---

## 1. Why AI Images Look Like AI: Optical Physics vs. Statistical Averages

Modern text-to-image and multimodal generators optimize for human preference scores (RLHF aesthetic rewards) trained disproportionately on commercial stock photography, retouched beauty campaigns, and 3D CG renders. Left unconstrained, every model gravitates toward the same statistical comfort zone:

1. **Zero surface entropy:** Skin lacks pores and vellus hair; tables have no dust or scratches; shirts have zero wear creases.
2. **Impossible dual-key lighting:** Warm golden rim light paired with cool cyan fill shadows ("Midjourney glow"), even inside a windowless room or under overcast skies.
3. **Mathematical centering:** Subjects sit dead-center on the vertical axis, shoulders squared, staring straight into the lens with a symmetrical half-smile.
4. **Optical contradictions:** Smartphone street snapshots rendered with creamy `f/1.2` background obliteration that violates lens physics.

### The Core Principle

> **Stop prompting for "quality." Prompt for optical physics, sensor limitations, candid staging, and lived-in entropy.**

Words like `photorealistic`, `hyperrealistic`, `8K`, `masterpiece`, and `ultra-detailed` act as **poison tokens**: in training captions, real photographers almost never tag raw Leica or Canon files as `"hyperrealistic 8k masterpiece"`, whereas CG artists on ArtStation do. Using those words actively steers latent space *away* from real cameras and *into* glossy 3D renders.

### The 3-Stage Visual De-AI Pipeline

| Stage | Objective | Primary Lever |
|-------|-----------|---------------|
| **1. Pre-Generation Prompt Surgery** | Replace quality buzzwords with physical optics, real lighting, anatomical micro-texture, and asymmetric candid action | Camera/lens/film anchors, single-source lighting, room clutter |
| **2. Model Parameter & Reference Control** | Disable built-in aesthetic beauty filters and over-baked guidance | `--style raw`, low `--stylize`, `raw: true`, low CFG (`1.8–4.5`), `--sref` |
| **3. Post-Processing Optical Emulation** | Break pixel-level digital sterility in the final 20% | Micro-contrast softening, midtone film grain, red-channel halation, black-point lift |

---

## 2. Diagnostic Catalog of Visual AI Tells (`V1–V12`)

Scan generated images or user prompts for **clusters** of these 12 visual tells before rewriting prompts or post-processing pixels.

| ID | Visual Tell (CN / EN) | What It Looks Like | Root Cause & Fix |
|----|-----------------------|--------------------|------------------|
| **V1** | **Waxy / Plastic Skin** (`塑料磨皮肌 / 蜡像感`) | Poreless cheeks, uniform rubbery specular highlights, missing peach fuzz (vellus hair), "Flux cleft chin" or supermodel cheekbones on ordinary people | High CFG + beauty-retouched training bias. Drop CFG; specify `unretouched skin texture, visible pores, fine vellus hair, localized T-zone oil sheen, minor blemishes`. |
| **V2** | **HDR & Teal-Orange Glow** (`糖水片 HDR / 青橙光晕`) | Crushed dark cyan shadows + glowing orange rim highlights; every sunset or alley looks like a movie poster | Aesthetic post-training reward model. Enable `--style raw` / `raw: true`; specify single natural light source + muted film color science (`Kodak Portra 400`, `5600K daylight`). |
| **V3** | **Warm Amber / Sepia Cast** (`GPT 暖黄偏色滤镜`) | White walls, paper, teeth, and shirts turn creamy yellow-amber (`~4000K` wash) | Baked bias in ChatGPT / `gpt-image-1`. Explicitly anchor `daylight white balance 5600K, stark pure white highlights, zero warm amber or sepia cast`; cut trigger words like `cozy` or `cinematic`. |
| **V4** | **Dead-Center Symmetry** (`绝对居中与强迫症对称`) | Subject dead-center vertically, bilateral room background symmetry, rigid passport-photo posture | Safe spatial prior in diffusion denoising. Prompt `rule-of-thirds off-center framing`, `foreground doorway occlusion`, `2-degree candid horizon tilt`, `cropped edge`. |
| **V5** | **Sterile Showroom Rooms** (`样板间无菌环境`) | Spotless kitchen counters, unwrinkled clothes, generic potted monstera plants, dry coffee mugs with no residue | Lack of entropy specification. Inject 2–3 specific lived-in items: `tangled charging cable, half-drunk water glass with condensation ring, scuffed wooden tabletop, wrinkled cotton sleeve`. |
| **V6** | **The Stock Gaze** (`AI 千码凝视 / 假笑模特脸`) | Direct eye contact with parted lips or polite stock-photo smile while soldering, coding, cooking, or walking | Portrait caption bias. Direct the gaze away from the lens: `glancing down at notebook, caught mid-sentence, looking past the frame, unposed candid moment`. |
| **V7** | **Bokeh Abuse** (`背景虚化滥用 / 景深违和`) | Creamy `f/1.2` blurred background behind a wide-angle street scene or casual phone snapshot | Flux/MJ default depth separation. Match aperture to lens physics: `28mm f/5.6` or `deep depth of field, f/8, sharp environmental background throughout`. |
| **V8** | **Unmotivated Rim Light** (`无来源轮廓假光`) | Bright hair backlight inside a dim room with no window behind the subject; contradictory dual shadows | Generic `"cinematic/studio lighting"` tokens. Define **one** physical light source and its direction: `lit solely by overcast north-facing window on camera left, natural shadow falloff`. |
| **V9** | **Micro-Text & Anatomical Slop** (`微距乱码与手齿伪影`) | Melted pseudo-Latin storefront signs, 6th finger, fused knuckles, 40 uniform teeth, asymmetric earrings | Token/spatial resolution limits. Keep background text out of focus or quote exact short strings (`Ideogram`/`GPT-Image`/`Flux`); hide or ground hands on concrete objects (`hands resting flat on ceramic mug`). |
| **V10** | **Physics & Continuity Breaks** (`物理穿帮与几何断裂`) | Chair legs vanishing under tables, eyeglass temples disappearing before ears, mirror reflection mismatch, floating bag straps | Local patch attention missing global topology. Inspect object attachment points (`eyeglass arms resting over ears`, `strap anchored to shoulder`); inpaint structural breaks. |
| **V11** | **CFG Frequency Burn** (`高频锐化烤焦感`) | Crunchy pores, metallic wire-like hair strands, harsh haloing around edges, posterized skin shadows | Guidance scale (`CFG`) set too high (`>5.5` in SDXL, `>4.0` in Flux Dev) or aggressive upscaler denoise. Lower CFG (`2.0–4.0`); soften Texture (`-10`) in post. |
| **V12** | **Poison Quality Buzzwords** (`质量词反向污染`) | Image looks like an Unreal Engine cutscene or DeviantArt digital airbrush painting despite asking for a "photo" | Prompt contains `photorealistic, hyperrealistic, 8k, masterpiece, ultra-detailed, octane render`. Delete every single one. |

---

## 3. Prompt Engineering Playbook: Optics, Film, Lighting & Entropy

Structure realistic prompts like a **photographer's field log**, not an adjective soup:

```text
[Optional Raw Filename Anchor] + [Shot Type & Off-Center Framing] + [Ordinary Subject, Gaze & Micro-Anatomy]
+ [Wardrobe Wear & Lived-In Environment Entropy] + [Single Physical Light Source] + [Camera Body, Focal Length, Aperture & Film/Sensor Profile]
```

### 3.1 Poison Words vs. Optical Replacements (Mandatory Purge)

| Delete Immediately (Poison Trigger) | Replace With (Physical Optical Grounding) |
|-------------------------------------|-------------------------------------------|
| `photorealistic`, `hyperrealistic`, `ultra-realistic` | `unedited 35mm documentary photograph`, `raw DSLR still`, `candid editorial photograph` |
| `8k`, `UHD`, `insanely detailed`, `masterpiece`, `best quality` | `natural optical sharpness`, `fine silver-halide grain`, `subtle lens softness at corners` |
| `cinematic lighting`, `dramatic lighting`, `volumetric god rays` | `diffused overcast daylight`, `single side window light`, `harsh overhead fluorescent tubes` |
| `studio lighting`, `perfect lighting` | `soft bounced key light with natural shadow falloff`, `direct on-camera flash with hard wall shadow` |
| `beautiful woman / handsome man`, `flawless skin` | `ordinary 34-year-old commuter, subtle asymmetrical features, visible pores, slight under-eye tiredness` |
| `bokeh`, `blurry background` (unqualified) | `shot on 50mm at f/2.8 with gradual optical falloff` *or* `28mm at f/8 with readable street context` |
| `vibrant colors`, `stunning color grading` | `Kodak Portra 400 color profile`, `muted neutral daylight 5600K`, `true-to-life ungraded sRGB` |
| `modern room`, `cozy cafe` | `narrow Taipei coffee bar with scuffed walnut counter, stacked paper filters, steamed glass window` |

### 3.2 Camera, Lens & Sensor Pairing Matrix

Never mix incompatible hardware (e.g., never pair `iPhone snapshot` with `85mm f/1.2` and `Kodak Tri-X`). Pick **one** coherent optical rig per image:

| Target Aesthetic | Camera & Sensor / Film | Lens & Aperture | Signature Optical Traits to Mention |
|------------------|------------------------|-----------------|-------------------------------------|
| **Street Documentary / Photojournalism** | `Leica M6` or `Ricoh GR III` | `28mm f/4` or `35mm f/2.8` | Deep environmental context, slight motion blur on passing pedestrians, high-contrast street shadows |
| **Candid Editorial Portrait** | `Canon EOS R5` or `Contax G2` on `Kodak Portra 400` | `50mm f/2` or `85mm f/2.2` | Sharp focus on near eye, natural eyelash/pore detail, gentle background separation without total blur |
| **90s / Y2K Party & Youth Snapshot** | `Contax T2` point-and-shoot or `2004 Sony Cyber-shot CCD digicam` | `38mm f/2.8` built-in lens | Direct harsh on-camera flash, red-eye/specular skin shine, hard dark shadow right behind head, slight vignette |
| **Smartphone UGC / Casual Everyday** | `iPhone 15 Pro main camera, raw DNG` | `24mm equivalent, f/1.78` (wide deep DoF due to small sensor) | Deep focus across room, computational dynamic range, slight wide-angle perspective stretch near edges, handheld framing |
| **Night Urban / Neon Interior** | `35mm motion picture still` on `CineStill 800T` | `35mm T1.5 cine prime` | Tungsten-balanced cool shadows, subtle reddish-orange halation around neon tubes and streetlamps, visible 800-ISO grain |
| **Clean Architectural / Interior** | `Hasselblad X2D` or `Canon TS-E tilt-shift` | `24mm tilt-shift at f/8, ISO 100` | Corrected vertical lines, natural daylight gradient across drywall, crisp fabric weave and wood grain |

#### The Raw Filename Prefix Technique (Use Selectively)

In **Flux.1 (`Dev` / `Schnell`)** and **SDXL** checkpoints trained on raw camera metadata from Flickr/Commons, prefixing prompts with camera file tokens shifts latent retrieval away from curated art portfolios toward unedited camera rolls:

- **Canon DSLR RAW:** `IMG_4829.CR2, ...`
- **Nikon DSLR RAW:** `DSC_0412.NEF, ...`
- **Sony Mirrorless RAW:** `DSC08192.ARW, ...`
- **Smartphone Casual:** `IMG_2041.JPG, ...` or `IMG_5921.HEIC, ...`

> **Guardrail on Filename Tokens:** Do **not** use `IMG_xxxx.CR2` prefixes in text-obsessed generators (**Ideogram**, **Recraft V3**, and occasionally **GPT-Image**), which may literally render `"IMG_4829.CR2"` as stamped text in the corner of the image. Use them primarily in **Flux.1** and **SDXL**.

### 3.3 Film Stock Color Science Lexicon

| Film Stock | Color & Contrast Behavior | Best Scene Match |
|------------|---------------------------|------------------|
| **Kodak Portra 400** | Warm-neutral skin tones, soft highlight roll-off, fine organic grain, low shadow contrast | Daylight/window portraits, lifestyle, editorial |
| **Kodak Gold 200** | Nostalgic warm yellows, punchier consumer contrast, noticeable 35mm grain | Summer outdoors, casual travel, family/street |
| **Fujifilm Pro 400H / Superia 400** | Cooler cyan-green shadow tint, soft pastel greens, clean neutral skin | Overcast cities, cafes, rainy street scenes, East Asian street photography |
| **CineStill 800T** | Tungsten `3200K` balance, cool blue night shadows, signature red-orange halation around point lights | Night markets, diners, subway platforms, rainy neon |
| **Ilford HP5 Plus 400 / Kodak Tri-X 400** | Classic silver-gelatin monochrome, gritty midtone grain, rich shadow separation | Documentary, workshop/industrial, moody candid portraits |

### 3.4 Bilingual Skin, Wardrobe & Entropy Token Bank (中英对照去塑料词库)

- **Human Skin & Hair (真实肤质与毛发):**
  - `unretouched natural skin texture, visible pores on nose and cheeks` (未修图的自然肤质，鼻翼与脸颊可见真实毛孔)
  - `fine vellus peach fuzz catching side light` (侧光下可见细微面部绒毛)
  - `localized natural sebaceous sheen on forehead, matte cheeks` (额头局部自然微汗油光，双颊哑光，拒绝全脸涂油蜡感)
  - `slight asymmetrical smile lines, faint under-eye creases, stray flyaway hairs` (轻微不对称笑纹、淡淡眼下细纹、自然散落的碎发)
- **Wardrobe Wear (衣物生活折痕):**
  - `lived-in washed heavyweight cotton t-shirt with slight collar relax` (水洗重磅棉T恤，领口自然微松)
  - `natural elbow creases on linen jacket, stray lint fiber` (亚麻外套肘部自然折痕、细微织物纹理)
- **Environmental Clutter (空间烟火气细节):**
  - `scuffed oak table with faint water rings, receipt tucked under ceramic saucer, tangled white USB-C cord` (有轻微划痕与水渍印的橡木桌、压在碟下的小票、缠绕的充电线)
  - `smudged glass storefront, peeling sticker residue on aluminum lamppost, wet uneven asphalt` (带指纹痕迹的橱窗玻璃、路灯杆上残留的半截贴纸、积水不平的柏油路)

---

## 4. Negative Prompt Engineering & Model Boundaries

Negative prompts work **only** when the inference pipeline computes unconditional/negative classifier-free guidance (`CFG > 1.0`). Applying them blindly across architectures causes failures:

| Architecture Family | Negative Prompt Mechanism | Correct Strategy |
|---------------------|---------------------------|------------------|
| **Midjourney v6.1 / v7** | `--no` flag (negative semantic weight `-0.5`) | Keep `--no` short (`5–10` concrete visual nouns/adjectives). Never write `"--no no plastic"` (double negative). |
| **SDXL / SD 3.5** | Native Negative Conditioning (`CFG 3.0–5.5`) | Essential. Weight anti-wax and anti-CGI tokens at `1.1–1.3`; avoid bloated 150-token SD1.5 copy-pasta (`bad_prompt_version2`) which degrades composition. |
| **Flux.1 (`Dev` / `Schnell` / API)** | Guidance-distilled (`CFG = 1.0` internally unless custom Negative-CFG ComfyUI node is used) | Standard Flux ignores negative prompt boxes, and typing `"no plastic skin, no bokeh"` inside the positive prompt triggers the **pink-elephant effect** (generating *more* bokeh). State the **affirmative opposite**: `matte unretouched skin with pores; deep f/8 focus with sharp background`. |
| **GPT-Image / Gemini Nano-Banana** | Multimodal LLM instruction parser | Understands explicit natural-language exclusions at the end of a prompt (`Strictly avoid: warm yellow filter, airbrushed skin, 3D render sheen`), best paired with affirmative specs (`5600K neutral white`). |

### Copy-Paste Negative Prompt Banks

**Midjourney (`--no` suffix):**
```text
--no airbrushed, plastic skin, smooth skin, 3d render, cgi, illustration, studio rim light, teal and orange, symmetrical composition, oversaturated
```

**SDXL (`RealVisXL` / `Juggernaut XL`) & `SD 3.5 Large` Negative Box:**
```text
(plastic skin, waxy skin, airbrushed, doll-like, smooth poreless skin:1.25), 3d render, cgi, octane render, unreal engine, digital painting, anime, cartoon, oversaturated, neon glow, artificial rim lighting, symmetrical passport pose, heavy bokeh blur, deformed hands, fused fingers, extra digits, garbled text, watermark
```

**Affirmative Anti-Slop Clause (for `Flux.1`, `GPT-Image`, `Gemini`, `Imagen` positive prompts):**
```text
Unretouched documentary photograph with neutral 5600K daylight white balance, matte skin with visible pores and natural imperfections, single physically motivated light source, and deep optical focus across a lived-in background.
```

---

## 5. Model-Specific De-AI Workflows

### 5.1 Midjourney (v6.1 / v7)

Midjourney's default aesthetic pipeline injects dramatic contrast, teal-orange color grading, and editorial model bone structure. Strip it down with four controls:

1. **Always append `--style raw`:** Disables Midjourney's opinionated beautification layer so ordinary faces, flat lighting, and messy rooms stay ordinary.
2. **Lower `--stylize` (`--s`):** Default is `100`; users often crank it to `250–750`, which produces hyper-glossy AI art. Keep `--s` between **`20` and `100`** (`--s 50` is the documentary sweet spot).
3. **Anchor texture with `--sref` (Style Reference):** Pass 1–2 real unedited analog scans or raw street photos via `--sref <url>` with moderate style weight (`--sw 60` to `--sw 120`) to inherit authentic grain and dynamic range without copying subject content.
4. **Keep `--weird` near zero (`0–20`):** High `--weird` breaks symmetry but introduces surreal uncanny artifacts.

```text
/imagine prompt: Candid documentary photograph of a tired software engineer in his late 30s debugging hardware at a cluttered workbench, glancing down at an oscilloscope probe, unretouched skin with slight stubble and under-eye shadows, faded grey sweatshirt, overhead 4000K fluorescent shop light, shot on Leica Q2 28mm f/4, natural grain --ar 3:2 --style raw --s 50 --no airbrushed, teal and orange, studio lighting, bokeh
```

### 5.2 Flux.1 (`Flux 1.1 Pro Ultra`, `Flux.1 Dev`, `Flux.1 Schnell`)

Flux has world-class prompt adherence and hand anatomy, but exhibits **three signature tells**: waxy skin sheen, extreme shallow-depth-of-field bokeh addiction, and the chiseled/dimpled **"Flux chin"**.

1. **`Flux 1.1 Pro Ultra` — Turn ON `raw` mode (`--raw` / `"raw": true`):** Black Forest Labs built Raw Mode specifically to strip synthetic polish, restoring natural candid framing, flat ambient light, and organic skin asymmetry.
2. **`Flux.1 Dev` (ComfyUI / Local) — Drop `FluxGuidance` to `1.8 – 2.8`:** The default `3.5` guidance is tuned for punchy commercial illustrations. Dropping `FluxGuidance` to **`2.0–2.5`** (with `28–35` steps, `Euler` + `Beta` or `Deis` + `ddim_uniform`) immediately eliminates plastic specular highlights on foreheads and cheeks.
3. **Kill Flux Bokeh Addiction Explicitly:** Never leave background focus unspecified in Flux. Always write `deep depth of field, shot at f/8, sharp detailed background in focus` unless you genuinely want an `85mm f/1.8` portrait.
4. **Neutralize the "Flux Chin":** On close-up portraits, include `soft natural jawline, smooth rounded chin` to override the base weight bias toward cleft/chiseled chins.
5. **LoRA Restraint:** If using community realism/amateur-photo LoRAs (e.g., *Amateur Photography* or *Boring Reality*), cap strength at **`0.35 – 0.60`**. At `1.0`, LoRAs fry micro-textures and inject repetitive CCTV artifacts.

### 5.3 Stable Diffusion (`SDXL`: RealVisXL / Juggernaut XL & `SD 3.5 Large`)

1. **Use Native Aspect Buckets Only:** Generate at `896×1152` (3:4 portrait), `1152×896` (4:3 landscape), or `1024×1024`—never `512×512` or arbitrary non-divisible-by-64 sizes.
2. **Keep CFG Low (`3.0 – 4.5`):** In `RealVisXL v5` and `Juggernaut XL`, `CFG 7.0` bakes orange skin and plastic cheekbones. Run **`CFG 3.5–4.5`** with `DPM++ 2M SDE Karras` (`30–38` steps). Use **Perturbed-Attention Guidance (`PAG 1.5`)** if structural coherence needs a boost without raising CFG contrast.
3. **`ADetailer` / Face-Fix Denoise Cap (`<= 0.32`):** High `ADetailer` denoising (`0.45+`) erases grainy candid faces and pastes a smooth, front-lit supermodel mask onto a gritty body—an instant collage tell. Keep face inpaint denoise at **`0.22 – 0.32`** with the *exact same* lighting and grain prompt.

### 5.4 OpenAI `GPT-Image` (`gpt-image-1` / ChatGPT Image Generation)

`gpt-image-1` excels at multi-object spatial logic and embedded typography, but suffers from a notorious **warm amber/sepia tint ("yellow filter")** and posterized midtone smoothing.

1. **Mandatory White-Balance Override Clause:** Append explicit Kelvin and highlight anchors to every photographic prompt:
   > `Color science: neutral 5600K daylight white balance, crisp pure white highlights (#FFFFFF on white surfaces), cool-neutral shadows, zero warm amber wash, no sepia filter, no golden-hour tint.`
2. **Audit Warm Trigger Words:** Words like `cozy`, `warm`, `vintage`, `cinematic`, `nostalgic`, `lamp-lit`, and `rustic` cause `gpt-image-1` to drench the entire frame in orange-brown. Replace `cozy home office` with `lived-in apartment desk with neutral white drywall and overcast daylight from a side window`.
3. **Iterative Texture Follow-Up:** In conversational mode, inspect draft 1 and issue targeted surgical edits: *"Keep the exact composition, strip 100% of the yellow warm cast so the wall is neutral cool white, reduce background blur to f/5.6, and add subtle 35mm sensor grain."*

### 5.5 Google `Gemini Nano-Banana` (`gemini-2.5-flash-image` / Gemini 3 Pro Image) & `Imagen 3 / 4`

Google's multimodal image engines render exceptionally clean optics and accurate physics, so their primary tell is **ultra-clean commercial stock perfection** (looking like a Fortune 500 brochure rather than a candid moment).

1. **Write Causal Paragraphs, Not Tag Soup:** Describe *why* light and objects behave as they do (*"Afternoon rain has just stopped, leaving damp dark patches on the concrete sidewalk and faint mist on the cyclist's glasses"*).
2. **Multi-Image Reference Grounding (Nano-Banana):** Supply a real reference photograph specifically for lighting/color texture and instruct: *"Match the flat overcast exposure, muted dynamic range, and handheld framing of Reference Image 1 without beautifying skin or boosting saturation."*
3. **De-Stockify Subjects & Rooms:** Explicitly request non-model demographics, slightly awkward candid timing (*caught mid-blink or mid-step*), and asymmetrical background clutter to break Imagen's polished commercial-ad prior.

### 5.6 `Ideogram` (2.0 / 3.0) & `Recraft V3`

1. **Ideogram — Turn `Magic Prompt` OFF:** Ideogram's `Magic Prompt` rewrites terse user inputs into flowery, dramatic descriptions full of cinematic clichés. Set `Magic Prompt: Off`, select style `Realistic`, put any in-scene text inside exact quotes (`"NO PARKING"`), and describe physical weathering on the text carrier (*faded screen-printed ink on chipped aluminum sign, slight dirt streak*).
2. **Recraft V3 — `Photorealism -> Raw` + Low Artistic Level:** Explicitly select the `Photorealism` family (`Natural Light` or `Raw` sub-style) and dial the **Artistic** slider down (`0–25%`). Upload a real unretouched photograph as a style reference when building multi-asset brand sets. Avoid `IMG_xxxx.CR2` prefixes here.

---

## 6. Post-Processing Optical Recipes: The Final 20%

Even the best raw generator output has **zero true optical chromatic aberration, overly crisp digital edges, and uniform noise-free shadow floors**. A 90-second post-processing pass destroys pixel-level AI sterility.

### 6.1 Adobe Lightroom / Camera Raw Preset Values

| Panel | Parameter | Setting | Optical Purpose |
|-------|-----------|---------|-----------------|
| **Basic** | White Balance Temp | `-3` to `-8` (especially on GPT-Image) | Neutralizes synthetic amber bias |
| **Basic** | Highlights / Blacks | Highlights `-15`, Blacks `+8` | Softens digital clipping; prevents crushed CGI blacks |
| **Presence** | **Texture** / **Clarity** | Texture **`-8` to `-14`**, Clarity **`-5` to `-10`** | Takes the "razor-fried" AI micro-contrast edge off skin and foliage |
| **Tone Curve** | RGB Point Curve | Lift `(0, 0)` → **`(0, 10)`**; pull `(255, 255)` → **`(255, 248)`** | Emulates analog paper D-max and subtle highlight shoulder roll-off |
| **Effects** | **Grain** | Amount **`24–34`**, Size **`35–48`**, Roughness **`55`** | Replaces sterile flat pixel runs with organic silver-halide clumping |
| **Masking** | Luminance Range (`Top 10%`) | Clarity `-25`, Temp `+6`, Exposure `+0.08` | Subtle thermal highlight bloom around lamps and window frames |

### 6.2 Adobe Photoshop: Authentic Red-Channel Halation & Midtone Grain

Real analog film grain does **not** sit uniformly over pure black or pure white (`Add Noise` at `100%` looks like a cheap mobile filter), and real halation occurs when bright light penetrates the emulsion and scatters back into the **red-sensitive layer**.

1. **Physical Red-Channel Halation (CineStill / 35mm Effect):**
   - Duplicate the merged image layer (`Halation`).
   - Run `Image -> Apply Image` (`Channel: Red`, `Blending: Normal`, `100%`), then use `Levels` (`Ctrl+L`) to crush everything below luminance `210` to pure black (`0`), keeping only extreme specular highlights and window/neon edges.
   - Tint the isolated highlights warm red-orange (`Hue/Saturation` Colorize: `Hue 10`, `Sat 75`), apply `Filter -> Blur -> Gaussian Blur` (`14–32 px` on a 2K image), set layer blend mode to **`Screen`** or **`Linear Dodge (Add)`** at **`20–35%` opacity**.
2. **Luminance-Weighted Film Grain (`Blend If` Method):**
   - Create a `50% Gray` layer (`Edit -> Fill -> 50% Gray`), convert to **Smart Object**, set blend mode to **`Overlay`** or **`Soft Light`**.
   - Apply `Filter -> Noise -> Add Noise` (`Amount: 7–10%`, `Gaussian`, `Monochromatic`), followed by `Filter -> Blur -> Gaussian Blur` (`0.4–0.6 px`) so grain isn't single-pixel digital snow.
   - Open `Layer Style -> Blend If: Gray` on `Underlying Layer`. Hold `Alt/Option` to split the endpoint triangles: drag the shadow slider to **`0 / 40`** and the highlight slider to **`210 / 255`**. Grain now embeds naturally into midtones while sparing deep blacks and clean highlights.

### 6.3 DaVinci Resolve 3-Node Pipeline (Stills & AI Video)

- **Node 1 (`De-Digital Curve`):** Pull `Midtone Detail` to **`-10` to `-15`**; lift `Lift` master wheel `+0.01` and soften `Gain` `-0.02`.
- **Node 2 (`Halation`):** Resolve Studio `Halation` OFX (`Threshold 0.78`, `Strength 0.28`, `Spread 0.35`, `Secondary Glow` off) — or in Resolve Free, luminance-key top `12%` highs into a `0.35` red-weighted blur node set to `Screen` composite mode.
- **Node 3 (`35mm Grain`):** `Film Grain` OFX preset **`35mm 400T`** or **`Kodak 5219 500T`**, `Grain Size 0.36`, `Grain Strength 0.32`, `Texture 0.55`.

### 6.4 Automated Python Optical Humanizer (`Pillow` + `NumPy`)

For batch-processing generated assets in local pipelines (requires only `Pillow` and `NumPy`), this script applies micro-softening, red-orange highlight halation, midtone-weighted grain, and a subtle analog matte curve:

```python
import numpy as np
from PIL import Image, ImageFilter


def humanize_ai_image(
    input_path: str,
    output_path: str,
    soften_alpha: float = 0.18,
    halation_strength: float = 0.22,
    grain_sigma: float = 0.028,
    black_lift: float = 0.03,
    seed: int = 42,
) -> None:
    """Apply subtle optical softening, red-channel halation, midtone grain, and matte black lift."""
    rng = np.random.default_rng(seed)
    img = Image.open(input_path).convert("RGB")

    # 1. Tame razor-sharp AI micro-contrast slightly
    soft = img.filter(ImageFilter.GaussianBlur(radius=0.55))
    arr = (1.0 - soften_alpha) * (np.asarray(img, dtype=np.float32) / 255.0) + (
        soften_alpha * (np.asarray(soft, dtype=np.float32) / 255.0)
    )

    # 2. Red-orange highlight halation on top ~12% luminance
    luma = 0.2126 * arr[..., 0] + 0.7152 * arr[..., 1] + 0.0722 * arr[..., 2]
    high_mask = np.clip((luma - 0.86) / 0.14, 0.0, 1.0)
    mask_img = Image.fromarray((high_mask * 255.0).astype(np.uint8), mode="L")
    spread_radius = max(6.0, min(img.size) * 0.012)
    halo = np.asarray(
        mask_img.filter(ImageFilter.GaussianBlur(radius=spread_radius)),
        dtype=np.float32,
    ) / 255.0
    tint = np.array([1.0, 0.34, 0.08], dtype=np.float32)  # warm emulsion scatter
    arr = 1.0 - (1.0 - arr) * (1.0 - halation_strength * halo[..., None] * tint)

    # 3. Luminance-weighted organic grain (strongest in midtones, gentle in blacks/whites)
    noise_h, noise_w = max(1, img.height // 2), max(1, img.width // 2)
    coarse_noise = rng.normal(0.0, 1.0, size=(noise_h, noise_w)).astype(np.float32)
    grain_img = Image.fromarray(
        np.clip((coarse_noise * 32.0 + 128.0), 0, 255).astype(np.uint8), mode="L"
    ).resize(img.size, resample=Image.Resampling.BILINEAR)
    grain = (np.asarray(grain_img, dtype=np.float32) - 128.0) / 32.0
    midtone_weight = 4.0 * luma * (1.0 - luma)  # peaks at 1.0 when luma=0.5, 0 at 0/1
    arr = arr + grain[..., None] * grain_sigma * (0.25 + 0.75 * midtone_weight[..., None])

    # 4. Subtle analog black-point lift & highlight roll-off
    arr = black_lift + arr * (0.985 - black_lift)
    out = np.clip(arr * 255.0, 0, 255).astype(np.uint8)
    Image.fromarray(out, mode="RGB").save(output_path, quality=94, subsampling=0)
```

---

## 7. Before-vs-After Case Studies (Bilingual CN / EN)

### Case 1: Tech Founder / Researcher Portrait (人像去蜡像感与假棚拍光)

- **User Intent (CN):** 生成一张 35 岁华人硬件工程师在实验室工作台前的照片，用于个人主页和专访配图。
- **Before (AI Slop Prompt):**
  > `A handsome 35-year-old Asian male engineer in a modern high-tech laboratory, looking at camera with a confident smile, cinematic lighting, bokeh background, photorealistic, hyper-detailed, 8k, masterpiece.`
  - *Failure:* Produces a K-drama model in a glowing blue sci-fi lab with waxy airbrushed skin, orange hair rim-light, and meaningless blurred neon monitors.
- **After (Humanized Prompt — Midjourney v7 / Flux 1.1 Pro Ultra Raw):**
  > `Unedited editorial portrait of a 35-year-old Chinese hardware engineer seated off-center at a cluttered electronics lab bench, turning slightly from a logic analyzer screen mid-thought, relaxed unposed expression, unretouched natural skin texture with visible pores, slight late-afternoon stubble, black-rimmed glasses with subtle lens reflection, lived-in navy crew-neck sweater with pushed-up sleeves. Background in moderate focus showing oscilloscopes, spooled solder wire, and anti-static mats. Lit by flat 4500K overhead lab fluorescents mixed with overcast afternoon light from a side window. Shot on Canon EOS R5, 50mm f/2.8, neutral daylight color balance, subtle fine grain --ar 4:5 --style raw --s 45 --no airbrushed, neon, sci-fi, bokeh obliteration, studio rim light`

### Case 2: Street Food Night Documentary (夜景纪实去赛博青橙光晕)

- **User Intent (CN):** 雨夜街头面摊老板煮面的纪实抓拍，要有烟火气，不要赛博朋克味。
- **Before (AI Slop Prompt):**
  > `Street vendor cooking noodles in a rainy alley at night, vibrant neon reflections, dramatic volumetric steam, ultra-realistic photography, 8k HDR.`
  - *Failure:* Turns an ordinary noodle cart into *Blade Runner* with magenta-cyan puddles and CGI smoke.
- **After (Humanized Prompt — Flux.1 Dev at `guidance 2.2`):**
  > `DSC08419.ARW, candid 35mm documentary photograph of an older street vendor in his 60s ladling broth from a dented aluminum pot at a cramped Taipei curbside noodle cart after rain, looking down at the bowl, slight motion blur on his right hand and rising steam, weathered skin with sweat sheen, faded striped apron with broth stains. Stacked plastic stools, handwritten laminated price card taped to stainless steel hood, wet dark asphalt. Lit solely by a bare warm tungsten bulb hanging inside the cart and harsh greenish fluorescent light from a 24-hour pharmacy behind him. Shot on 35mm lens at f/2.8, CineStill 800T color profile, subtle red halation around the bare bulb, deep street context visible.`

### Case 3: Casual Smartphone Lifestyle / UGC (日常手机抓拍去网红精修感)

- **User Intent (CN):** 朋友在周末早晨杂乱餐桌边喝咖啡看手机的随手拍。
- **Before (AI Slop Prompt):**
  > `Beautiful young woman drinking coffee in a cozy sunlit kitchen, morning glow, soft bokeh, flawless skin, Instagram lifestyle photo.`
- **After (Humanized Prompt — Flux / Gemini Nano-Banana):**
  > `IMG_6104.HEIC, casual handheld iPhone main-camera snapshot (24mm equivalent, deep natural focus) of a 28-year-old woman slouched at a small apartment dining table on Sunday morning, squinting slightly at her phone while holding a chipped ceramic mug, messy clipped-up hair with loose strands, zero makeup, natural under-eye crease, oversized faded grey hoodie. On the table: torn croissant crumbs on a paper napkin, keys, and a half-open laptop. Hard direct morning sunlight cutting across half the table from a side blinds window, unedited true-to-life exposure.`

### Case 4: GPT-Image Clean Interior / Product Scene (空间与静物去暖黄偏色)

- **User Intent (CN):** 极简北欧风书桌上的机械键盘与咖啡杯实拍图，白墙白桌面要干净不发黄。
- **Before (AI Slop Prompt):**
  > `A cozy minimalist desk setup with a mechanical keyboard and ceramic coffee mug, warm natural sunlight, realistic photo.`
  - *Failure in GPT-Image:* Drenches the entire white wall, keycaps, and mug in a heavy `4000K` yellow-sepia wash.
- **After (Humanized Prompt — `gpt-image-1`):**
  > `Overhead three-quarter photograph of a custom anodized silver 75% mechanical keyboard with matte grey PBT keycaps on a pale ash-wood desk beside a matte white stoneware mug with black coffee residue inside, coiled grey braided USB-C cable, open dot-grid notebook with handwritten ink notes in the corner, matte cool-white drywall behind the desk. Shot on 50mm macro lens at f/5.6. Color science: strict 5600K overcast daylight white balance, stark neutral whites on the wall and mug, cool-grey shadows, zero yellow filter, no warm amber cast, no sepia overlay.`

### Case 5: Embedded Storefront Signage & Packaging (`Ideogram` / `Recraft V3` 去数码贴图感)

- **User Intent (CN):** 一家开了二十年的街角五金店橱窗，玻璃上贴着营业时间，不要像 AI 刚P上去的发光字。
- **Before (AI Slop Prompt):**
  > `A realistic vintage hardware store window with a sign saying "CHEN HARDWARE - OPEN 8AM TO 6PM", ultra detailed, cinematic street photo.`
  - *Failure:* Renders pristine vector-sharp floating letters hovering slightly in front of spotless glass with zero weathering or reflection continuity.
- **After (Humanized Prompt — `Ideogram` Realistic Mode, `Magic Prompt: OFF`):**
  > `Unedited overcast street photograph of a 25-year-old neighborhood hardware storefront. Sun-faded red and white vinyl decal lettering adhered to the inside of dusty plate glass reading "CHEN HARDWARE" on the top line and "OPEN 8:00 - 18:00" below, with one corner of the letter E slightly peeling and faint squeegee streaks across the glass. Behind the window: tangled extension cords, dusty cardboard Makita boxes, hand-written yellow price tags, reflected parked scooters on the wet sidewalk outside. Shot on 35mm lens at f/5.6, neutral Fujifilm Superia 400 color.`

---

## 8. Upscaler & Detail-Enhancer Restraint (防止高清放大器“幻觉式毛孔”)

Generative upscalers (**Magnific**, **Krea Enhancer**, **SUPIR**, **ComfyUI Ultimate SD Upscale**) introduce a distinct second-generation AI tell: **"fractal skin hallucination"**—etching deep leathery pores onto 20-year-old faces, carving fake woodgrain into smooth plastic, or inventing tiny faces inside background foliage.

| Upscaler Tool | Failure Trigger | Safe Humanized Parameter Window |
|---------------|-----------------|---------------------------------|
| **Magnific AI / Krea** | `Creativity > 2`, `HDR > 1` | Keep `Creativity` at **`-2` to `+1`**, `HDR` at **`-2` to `0`**, `Resemblance` **`+3` to `+6`**, style `Portraits (Soft)` or `Film & Photography`. |
| **ComfyUI Tiled / Ultimate SD Upscale** | `denoise >= 0.40` | Cap `denoise` at **`0.18 – 0.28`** using a `4x-UltraSharp` or `4x_NMKD-Siax_200k` pixel pre-upscale so tiles never invent new anatomy. |
| **SUPIR** | `s_cfg > 4.5` or aggressive sharpness prompt | Keep `s_cfg` **`2.0 – 3.2`**, `EDM` sampler, and pass neutral captioning (`natural unsharpened photograph, subtle film grain`). |

---

## 9. Rapid Prompt Scanner & 10-Point Visual Audit Rubric

### 9.1 Pre-Generation Poison-Token Grep

Scan candidate prompts before submission; rewrite if **any** match hits:

```regex
(?i)\b(photorealistic|hyperrealistic|ultra[- ]?realistic|8k|4k uhd|masterpiece|best quality|insanely detailed|octane render|unreal engine|cinematic lighting|trending on artstation|flawless skin)\b
```

### 9.2 Post-Generation 10-Point Visual De-AI Checklist

Score `1` point for each verified human signal (`9–10` = publication/editorial ready; `<= 6` = visible AI slop, regenerate or post-process):

1. **Skin Micro-Anatomy:** Visible pores and localized (not uniform) T-zone sheen; zero rubbery airbrushed cheek planes (`V1`).
2. **White-Balance Honesty:** Neutral whites look neutral (`5200K–5800K`) unless tungsten/sunset is physically shown in-frame; zero unprompted GPT sepia wash (`V3`) or MJ teal-orange split (`V2`).
3. **Single-Source Shadow Consistency:** Nose, chin, collar, and table objects cast shadows in **one** coherent geometric direction (`V8`).
4. **Lens-Consistent Depth of Field:** Background blur matches the implied focal length and sensor size—no `f/1.2` bokeh on wide street or smartphone shots (`V7`).
5. **Asymmetric Framing:** Primary subject or horizon avoids rigid bilateral passport symmetry unless stylistically required (`V4`).
6. **Candid Gaze & Micro-Action:** Subject has natural eye focus and lived-in posture rather than a vacant stock-photo camera stare (`V6`).
7. **Environmental Entropy:** At least 2 imperfect real-world details exist (creased fabric, cable, dust, wear mark, uneven clutter) (`V5`).
8. **Topological & Hand Integrity:** Eyeglass temples, chair legs, fingers, teeth count, and reflections connect continuously (`V9`, `V10`).
9. **Text Carrier Realism:** Background signs are either naturally out-of-focus or spelled accurately with physical surface wear (`V9`).
10. **Organic Noise Floor:** Shadow/midtone transitions carry subtle luminance-weighted grain rather than sterile zero-noise bands or fried CFG edges (`V11`).

---

## 10. Anti-Overcorrection Guardrails & Ethical Boundaries

De-AI-ing can backfire when users replace **"plastic gloss slop"** with **"grunge film slop."** Enforce these five guardrails:

1. **Ban "Grunge Slop" on Clean Commercial Contexts:** Do **not** inject heavy 35mm film grain, `CineStill` light leaks, dusty scratches, or harsh paparazzo flash into corporate executive headshots, clean medical/industrial product photography, or contemporary architectural portfolios. Clean studio lighting (`Profoto octabox, f/8, ISO 100, Hasselblad medium format`) *is* how real commercial photographers shoot—humanize those via **pore micro-texture, natural fabric drape, and accurate neutral color**, not fake 1990s film dirt.
2. **Never Stack Contradictory Optics:** A prompt containing `shot on iPhone 15 Pro` + `85mm f/1.2 lens` + `Kodak Portra 400 film` feeds contradictory priors that degrade sharpness and framing. Pick **one** camera medium and respect its focal length and depth-of-field physics.
3. **Preserve Intentional Symmetry:** If the user is shooting Wes Anderson pastiche, classical religious architecture, or passport/ID layouts, symmetry is intentional—do not force Dutch tilts or foreground clutter.
4. **Check Corners for Token Leakage:** Whenever using camera filename anchors (`IMG_4829.CR2`) or film border terms (`35mm film`), inspect all four corners to verify the generator did not draw fake sprockets, timestamps (`'98 04 12`), or literal filename text unless requested.
5. **Strict Provenance & Evidentiary Ethics:** Visual humanization exists solely to elevate aesthetic craft in creative, editorial, design, and illustrative workflows. **Never** tamper with, strip, or forge cryptographic provenance standards (such as C2PA Content Credentials), and **never** use photorealistic generation to fabricate journalistic photo-evidence, clinical/patient imagery, or primary scientific experimental data (microscopy, western blots, sensor captures).
