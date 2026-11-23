# Research Paper Figure Skill Factory

Research Paper Figure Skill Factory builds reusable, evidence-backed, class-specific figure-making skills for scientific papers, then uses those generated skills for concrete target-paper figures.

The factory supports lawful literature/source acquisition, full-feasible local PDF coverage where available, structured figure/caption extraction, multi-label figure taxonomy, specialized skill generation, skill testing, packaging, and concrete figure production.

Version 2.0.5 adds mandatory visual-structure image display, abstract-decision concept/reference display, and a two-round visual selection workflow:

- generated skills must prebuild a subtype/style atlas during the builder layer;
- generated skills must show available saved atlas boards on first startup without target-paper analysis or target-paper image generation;
- later text replies that discuss subtype, layout grammar, visual style, density, metaphor, modeling pattern, candidate scheme differences, or final content architecture must display relevant saved atlas/reference images or non-target concept/modeling examples, or record missing status and repair action;
- later text replies must not describe visual structure, layout skeleton, panel choreography, module topology, arrow grammar, or content architecture with prose/bullets only; they must embed a saved reference or non-target visual-structure concept/modeling image when technically possible;
- saved atlas display and non-target concept/modeling example images are allowed in text replies, but target-paper candidate/final image generation remains separated into `IMAGE_ONLY` turns;
- first-round candidate boards should maximize direction-level diversity;
- after P6 selects the current best first-round image, generated skills must run P6b/P6b-IMAGE/P6c for paper-local best-practice optimization before P7 final prompt construction.

Rendering route is strict: ChatGPT web uses Create image through ChatGPT Images 2.0; Codex uses `$imagegen` first and falls back only to ChatGPT Images 2.0 API or another approved image-generation API. Native PNG/JPEG/WebP outputs from that route are allowed. SVG, Mermaid, TikZ, Graphviz, HTML/CSS, canvas, matplotlib, and code-rendered images are forbidden as generated candidate, draft, final, atlas, or fallback visuals.
