# Strict Text/Image Turn Separation Policy

Version: 2.0.5

This policy is mandatory for this guide and for every generated specialized figure-making skill.

## Core Rule

A generated skill must separate target-paper figure production from explanatory reference display.

- `TEXT_ONLY`: prose, planning, analysis, critique, prompt writing, state update, confirmation request, and inline display of allowed or required reference images.
- `IMAGE_ONLY`: target-paper first-round candidate-board generation, target-paper second-round variant generation, target-paper draft/formal figure generation, target-paper final figure generation, and target-paper revision image generation. No prose, no state footer, no caption, no explanation, and no SVG/Mermaid/TikZ/Graphviz/HTML-CSS/canvas/matplotlib/code-generated diagram substitute. Native image results may be returned/exported by the host as bitmap files such as PNG, JPEG, JPG, or WebP.

Allowed reference images inside a `TEXT_ONLY` reply:

- already-saved package-local subtype/style atlas or reference images;
- non-target concept diagrams that explain visual grammar, workflow, taxonomy axes, decision logic, or modeling patterns;
- non-target visual-structure examples that explain layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture;
- non-target example images created while building or demonstrating the specialized skill itself.

Required reference display:

- If a text turn explains or compares subtype, layout grammar, visual style, density, metaphor, modeling pattern, candidate scheme differences, or final content architecture, it must include a Markdown image embed for a relevant saved atlas/reference image or non-target concept/modeling example.
- If a text turn explains or defines visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture, it must include a Markdown image embed for a saved reference or non-target visual-structure concept/modeling image. Prose, bullets, ASCII, Mermaid, SVG, or code-rendered sketches do not count as the structure display.
- Pure state synchronization, caption/body text, simple confirmation, and ordinary restatement of an already registered image batch do not require a new concept/example image.
- If a required image is missing, record `concept_example_required`, `concept_example_status`, `concept_example_role`, `concept_example_trigger_reason`, and the generation/repair action.
- If a required visual-structure image is missing, also record `visual_structure_image_required`, `visual_structure_image_status`, `visual_structure_image_role`, `visual_structure_image_trigger_reason`, and the generation/repair action.

These inline concept/example/structure images must be clearly detached from the user's target paper: they are not candidate figures, not draft/final paper figures, not selectable visual directions, and not evidence that P5, P6b-IMAGE, or P8 has been completed. Record them as `non_target_reference` or `concept_example`, not as `candidate_image_batch_id` or `second_round_candidate_batch_id`.

Target-paper candidate images, second-round variants, draft figures, formal figure candidates, final figures, and revisions must not be embedded in a prose reply. They must use a dedicated `IMAGE_ONLY` turn. When relevant saved atlas assets or non-target concept/example assets are shown in text, use real Markdown image syntax; listing file paths or manifest rows is not enough.

## First Reply / Startup Gate

The first assistant reply after a skill is triggered must always be `STARTUP_PLAN_ONLY`, which is a strict `TEXT_ONLY` submode.

Even if the user's first message asks for images, the first assistant reply must not call image generation. It must only show the workflow/startup plan, record the received material as pending, and ask the user to continue or confirm.

For generated specialized skills, the first-trigger example, default prompt, and starter messages must preserve the target-paper generation boundary. They must display all already-saved subtype/style atlas boards with Markdown image embeds when those assets exist, but they must not analyze the target paper, generate target-paper candidate images, call an `IMAGE_ONLY` action, or produce draft/final paper figures in the first assistant response.

## Text Turn Stop Rule

If an assistant turn emits visible prose, markdown, table, YAML state, caption, prompt, or next-step help, it must stop before target-paper image generation. It may propose the next target-paper image batch and may show required reference/structure images with Markdown image embeds. If the host supports creating a non-target concept/example/structure image and embedding it inline in the same text reply, that is allowed only when the image is explicitly explanatory and detached from the target paper. If the host cannot do that cleanly, generate/save the concept/example/structure image first and embed it in a later `TEXT_ONLY` reply.

At first-round visual decision points for the target paper, the text turn should recommend 4 / 5 / 6 generated candidate images, defaulting to 6, with high direction-level diversity. At P6b, the text turn should recommend 4 / 5 / 6 second-round variants, defaulting to 6, varying paper-local optimization axes around the selected first-round winner. It must also state that ChatGPT web uses **Create image** through **ChatGPT Images 2.0**, Codex uses `$imagegen` first, and if `$imagegen` is unavailable Codex uses ChatGPT Images 2.0 API or another approved image-generation API. Native bitmap outputs such as PNG/JPEG/WebP are allowed, and SVG, Mermaid, or code-rendered diagrams/files are not.

## Image Turn Purity Rule

If the user has explicitly requested target-paper candidate, second-round variant, draft, final, or revision image generation and the state is sufficient, the next assistant turn must be `IMAGE_ONLY`. That turn must contain only the native image generation action. It must not include a plan, status footer, caption, critique, or textual explanation.

If native image generation is unavailable, do not replace the `IMAGE_ONLY` turn with SVG, Mermaid, HTML/CSS, canvas, plotting-library, or code-drawn figures. Stop in a `TEXT_ONLY` turn and provide a copyable imagegen/API prompt handoff.

## Generated-Skill Requirements

Every generated specialized figure-making skill must include these rules in:

- `SKILL.md` operating contract;
- workflow/state contract;
- prompt/rendering policy;
- startup example;
- state footer template;
- release checklist.

A generated skill is not production-locked if its first-trigger path can perform target-paper image generation, if it embeds target-paper candidate/final images inside a prose reply, if it treats non-target concept/example/structure images as candidate boards or second-round batches, if it fails to display available saved subtype/style atlas boards at startup with Markdown image embeds, if it only lists atlas paths, if any template permits target-paper image generation inside a text response, if an abstract-decision text turn omits required concept/example display without missing/repair state, if a visual-structure text turn describes structure with prose/bullets only, or if P6 first-round selection can move directly to P7/P8 without P6b/P6b-IMAGE/P6c.

Release validation must include an adversarial startup case where the user asks to generate target-paper images immediately. Passing output is startup text only plus already-saved atlas embeds when available. If the generated skill emits target-paper candidate/final imagery in that first response, lock validation fails.
