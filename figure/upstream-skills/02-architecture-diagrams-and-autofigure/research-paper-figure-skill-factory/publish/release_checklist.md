# Release Checklist - v2.0.5

## Factory Package

- [ ] `SKILL.md` has name, description, MIT-0 license, version 2.0.5, and OpenClaw metadata.
- [ ] `VERSION` is 2.0.5.
- [ ] `metadata.json` is valid JSON and says 2.0.5.
- [ ] `agents/openai.yaml` says 2.0.5.
- [ ] Startup workflow lists S0, B1-B9, P1-P6, P6b, P6b-IMAGE, P6c, and P7-P9.
- [ ] Skill Builder layer remains specialized-skill-first.
- [ ] Full-feasible local PDF coverage policy remains active.
- [ ] Target-paper candidate/final image isolation remains active.
- [ ] Saved package-local atlas/reference images are allowed in text replies.
- [ ] Abstract-decision text turns must display a saved reference or non-target concept/modeling example image, or record missing status and repair action.
- [ ] Abstract-decision triggers include subtype, layout grammar, visual style, density, metaphor, modeling pattern, candidate scheme differences, and final content architecture.
- [ ] Visual-structure text turns must not use prose/bullets only; if they discuss visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture, they must embed a saved reference or non-target visual-structure concept/modeling image when technically possible.
- [ ] If a paper-specific structure preview is needed, it is deferred to P5/P6b-IMAGE/P8 `IMAGE_ONLY`, and the text reply embeds only a generic structure/reference image.
- [ ] Pure state sync, caption/body text, simple confirmation, and ordinary restatement of already registered image batches do not require a new concept/example image.
- [ ] Target-paper candidate images, second-round variants, draft figures, final figures, and revisions are never embedded in text replies.
- [ ] Inline non-target concept/example images do not count as candidate-board batches, do not set `candidate_image_batch_id`, and do not set `second_round_candidate_batch_id`.
- [ ] First-round P4/P5 policy maximizes direction-level diversity.
- [ ] P6 selects only the current best first-round direction and cannot go directly to P7/P8.
- [ ] P6b/P6b-IMAGE/P6c second-round policy optimizes the selected direction around paper-local details and best practices.
- [ ] Saved atlas display is defined as renderable Markdown image embeds, not plain path lists.
- [ ] Off-recommended user requests are handled by mapping the result to the nearest original workflow step and updating state.
- [ ] Codex desktop display rule resolves package-local atlas paths to absolute filesystem paths.
- [ ] ChatGPT Sources display rule attempts source-asset display or package-relative Markdown embeds and records host-blocked rendering when needed.
- [ ] ChatGPT web Create image / ChatGPT Images 2.0 route remains active.
- [ ] Codex `$imagegen` first route remains active.

## Generated Skill Subtype/Style Atlas

Before any generated specialized figure-making skill can be production-locked, verify:

- [ ] The generated skill includes `assets/subtype-atlas/manifest.json`.
- [ ] The generated skill includes `assets/subtype-atlas/boards/`.
- [ ] The generated skill includes `assets/subtype-atlas/thumbnails/`.
- [ ] The generated skill includes `references/subtype-illustration-atlas.md`.
- [ ] Atlas coverage includes reader question, narrative role, logical gap, visual rhetoric, visual grammar/layout, paper slot, density/detail level, and visual communication art style.
- [ ] Each supported subtype has at least one representative illustration or thumbnail.
- [ ] Composite boards visibly label subtype names.
- [ ] Large taxonomies use hierarchical boards when needed.
- [ ] `manifest.json` records classification angle, subtype, image path, thumbnail path, board path, generation route, build time or build id, intended use, transferable visual attributes, limitations, and abstract-decision trigger support when relevant.
- [ ] The first factory text reply after B6 atlas generation embeds the newly saved atlas boards with Markdown image syntax.
- [ ] First/startup reply displays all available saved atlas boards with Markdown image embeds without target-paper analysis or target-paper image generation.
- [ ] Text replies that discuss subtype, layout grammar, visual style, density, metaphor, modeling pattern, candidate scheme differences, or final content architecture display relevant saved images or non-target concept/modeling examples with Markdown image embeds, or record missing assets and repair action.
- [ ] Text replies that discuss visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture display a relevant saved image or non-target visual-structure concept/modeling example with Markdown image embeds, or record missing assets and repair action.
- [ ] Text replies that display saved atlas or concept/example images do not generate target-paper candidate/final images in the same turn.
- [ ] Text replies never embed target-paper candidate, second-round variant, draft, final, or revision images.

## Generated Skill Candidate-Image Bridge

Before any generated specialized figure-making skill can be locked, verify:

- [ ] Production workflow includes P1-P6/P6b/P6b-IMAGE/P6c/P7-P9 or a stricter equivalent.
- [ ] P3 or equivalent produces 4-6 text candidates, normally 6.
- [ ] After text candidates, the first recommended next prompt asks to generate/display diverse first-round candidate images or schematic candidates, normally 6.
- [ ] P4 or equivalent is a `TEXT_ONLY` first-round visual candidate-board setup step.
- [ ] P5 or equivalent is an `IMAGE_ONLY` diverse first-round candidate-board generation step.
- [ ] P6 or equivalent is a `TEXT_ONLY` first-round candidate-review/current-best selection step.
- [ ] P6b or equivalent is a `TEXT_ONLY` best-practice paper-local divergence setup step.
- [ ] P6b-IMAGE or equivalent is an `IMAGE_ONLY` second-round variant generation step.
- [ ] P6c or equivalent is a `TEXT_ONLY` second-round review/final direction lock step.
- [ ] The workflow does not move from text candidates directly to final prompt, formal image generation, caption, or text-only lock unless the user explicitly skips image candidates.
- [ ] The workflow does not move from P6 first-round selection directly to P7/P8 unless the user explicitly overrides the second round and the limitation is recorded.
- [ ] State footer includes `visual_candidate_board_status`, `candidate_image_batch_id`, `selected_visual_candidate`, `best_practice_divergence_status`, `best_practice_divergence_axes`, `second_round_candidate_batch_id`, and `selected_second_round_candidate`.
- [ ] State footer includes `concept_example_required`, `concept_example_status`, `concept_example_role`, and `concept_example_trigger_reason`.
- [ ] State footer includes `visual_structure_image_required`, `visual_structure_image_status`, `visual_structure_image_role`, and `visual_structure_image_trigger_reason`.
- [ ] State footer includes `user_request_interpreted_action`, `workflow_step_before_user_request`, `workflow_step_after_user_request`, `state_transition_reason`, and `off_recommended_prompt_handling`.
- [ ] The next text reply after each `IMAGE_ONLY` generation records the generated image batch.
- [ ] Examples include startup with saved atlas, text candidates, first-round visual-board setup, image-only first-round board, candidate review, required concept/example reference display, visual-structure-as-image display, P6b divergence setup, P6b-IMAGE second-round variants, and P6c second-round selection.
- [ ] Startup, style/layout, abstract-decision, and visual-structure examples contain actual `![alt](...)` Markdown image embeds for saved atlas/reference or concept/example images.
- [ ] Rendering route uses ChatGPT web Create image / ChatGPT Images 2.0 and Codex `$imagegen` first.
- [ ] SVG/Mermaid/TikZ/Graphviz/HTML-CSS/canvas/matplotlib/code-rendered visual fallbacks are forbidden.
- [ ] Inline concept/example images are not treated as satisfying P5, P6b-IMAGE, P8, or the candidate-image bridge.

## Required Failing Tests

- [ ] Fail if no subtype/style atlas is generated and packaged.
- [ ] Fail if first/startup reply does not display available saved atlas boards with Markdown image embeds.
- [ ] Fail if first/startup reply only lists paths, file names, manifest rows, or prose descriptions instead of `![alt](...)` image embeds.
- [ ] Fail if a text reply discusses subtype/layout/style/density/metaphor/modeling/candidate differences/final content architecture but neither displays a relevant saved image or non-target concept/example with Markdown image syntax nor records why it is missing plus repair action.
- [ ] Fail if a text reply explains visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture using only prose, bullets, ASCII, Mermaid, SVG, or a code-rendered sketch.
- [ ] Fail if Codex local image display uses unresolved relative paths instead of absolute filesystem paths.
- [ ] Fail if a valid non-recommended/free-form user request is answered without mapping the completed work back to S0/B1-B9/P1-P6/P6b/P6b-IMAGE/P6c/P7-P9.
- [ ] Fail if a user asks to generate images during a text turn and the skill either generates live target-paper images in that text reply or fails to map the request to the required setup/current step before `IMAGE_ONLY`.
- [ ] Fail if the state footer omits before-step, after-step, interpreted action, or transition reason.
- [ ] Fail if a text reply performs target-paper candidate/final/revision image generation.
- [ ] Fail if a text reply embeds target-paper candidate, second-round variant, draft, final, or revision images.
- [ ] Fail if a non-target concept/example image is recorded as a candidate image batch or second-round candidate batch.
- [ ] Fail if an `IMAGE_ONLY` reply includes prose, caption, status footer, or next-step text.
- [ ] Fail if P6 selected one first-round best candidate and the workflow then enters P7/P8 without P6b/P6b-IMAGE/P6c.
