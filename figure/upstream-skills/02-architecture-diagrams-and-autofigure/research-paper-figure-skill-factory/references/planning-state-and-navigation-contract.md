# Planning, State, and Navigation Contract

Version: 2.0.5

## Every TEXT_ONLY Reply

Every text reply must contain, in this order:

1. `当前执行计划` near the beginning.
2. The substantive answer.
3. A default recommendation when multiple options/actions exist.
4. `当前状态与产物` immediately before the final section, automatically listing current status and current outputs.
5. `下一步你可以这样问` as the final section.

The status/output section is mandatory for every `TEXT_ONLY` reply. It must not be omitted because the answer is short, corrective, or mostly explanatory.

For generated specialized figure-making skills, the state/footer must also list the full workflow steps and the current position, and every step introduction must mark whether the current/next response is `TEXT_ONLY` or `IMAGE_ONLY`.

## Off-Recommended-Prompt Handling

Users do not need to follow the recommended prompt wording. A generated specialized skill must handle valid free-form requests and then align the result with the original workflow state.

For every text reply, record:

- `user_request_interpreted_action`;
- `workflow_step_before_user_request`;
- `workflow_step_after_user_request`;
- `state_transition_reason`;
- `off_recommended_prompt_handling`: `not_needed` / `handled_and_mapped` / `blocked_missing_prerequisites` / `mapped_to_text_setup_before_image_only`;
- `prerequisites_inferred_or_missing`.

If the user asks for an action out of order, map it to the nearest valid workflow step instead of ignoring the request or restarting. If a request to generate images arrives during a text reply, stop at the nearest `TEXT_ONLY` setup or confirmation step and set the next action to the required `IMAGE_ONLY` step. If a request asks for a later deliverable such as caption or final prompt before prerequisites are complete, answer what can be answered, record the missing prerequisites, and mark the current position accordingly.

## Visible Plan Requirements

The visible plan must include:

- current workflow code: `S0`, `B1`-`B9`, `P1`-`P6`, `P6b`, `P6b-IMAGE`, `P6c`, or `P7`-`P9`;
- current layer: Startup gate / Skill Builder layer / Figure Production layer;
- turn goal;
- compact checklist;
- whether the plan changed.

## Abstract-Decision Concept Example Gate

If a text reply explains or compares subtype, layout grammar, visual style, density, metaphor, modeling pattern, candidate scheme differences, or final content architecture, it must display a saved atlas/reference image or non-target concept/modeling example image with Markdown syntax.

The footer must record:

- `concept_example_required`;
- `concept_example_status`;
- `concept_example_role`;
- `concept_example_trigger_reason`.

Pure state synchronization, caption/body text, simple confirmation, and ordinary restatement of an already registered image batch do not require a new concept/example image.

## Visual-Structure Image Gate

If a text reply explains or defines visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture, it must display a saved atlas/reference image or non-target visual-structure concept/modeling example with Markdown syntax.

The generated skill must not use prose, bullets, tables, ASCII, Mermaid, SVG, or code-rendered sketches as the sole visual-structure representation. If the useful structure preview would be target-paper-specific, defer it to P5/P6b-IMAGE/P8 `IMAGE_ONLY` and show only a generic reference/concept structure image in text.

The footer must record:

- `visual_structure_image_required`;
- `visual_structure_image_status`;
- `visual_structure_image_role`;
- `visual_structure_image_trigger_reason`.

## Best-Practice Second-Round Gate

Generated specialized skills must treat the first image round as broad direction-setting and the second image round as paper-local optimization.

- P4/P5: generate 4-6 first-round candidate images, normally 6, with high diversity across subtype, layout grammar, metaphor, density, panel rhythm, or style family.
- P6: record `candidate_image_batch_id` and select the current best first-round direction.
- P6b: set up 4-6 paper-local optimization axes, normally 6. Keep first-round direction elements fixed and vary local module relationships, evidence/case anchors, label economy, panel transitions, color semantics, callout placement, or reviewer readability.
- P6b-IMAGE: generate 4-6 second-round variants, normally 6, with a new `second_round_candidate_batch_id`.
- P6c: record the second-round batch and set `selected_second_round_candidate`.

The footer must record `best_practice_divergence_status`, `best_practice_divergence_axes`, `second_round_candidate_batch_id`, and `selected_second_round_candidate`. P7/P8 cannot proceed after P6 unless P6b/P6b-IMAGE/P6c is complete or the user explicitly overrides the gate and the limitation is recorded.

## Two-Layer State Requirements

The state footer must never hide whether the assistant is:

- building a specialized figure-making skill; or
- using a generated specialized skill for a concrete target paper figure.

Required builder-layer fields:

- target figure class;
- target specialized skill slug/name;
- corpus and acquisition status;
- corpus coverage status: candidate/accessible/processed/skipped PDF counts, skipped reasons, processing scope, and whether representative pages are only audit aids;
- figure inspection reliability;
- label and multi-label coverage when one paper or figure can support multiple figure classes;
- taxonomy status;
- generated skill status/version;
- test/patch status;
- shortcut/fallback status.

Required production-layer fields:

- active specialized skill;
- target paper material status;
- figure need state;
- reference/sample image status, including per-image attribute preferences when provided;
- visual style and decision board state;
- required visual-structure image display state;
- first-round diversity and candidate batch state;
- best-practice second-round state;
- prompt/generation/review artifacts;
- full production-step list and current position, including the response mode for the current step.

Required output fields:

- outputs produced in the current turn;
- cumulative outputs produced so far;
- output paths, package names, prompt IDs, candidate IDs, image-batch IDs, or artifact names when available;
- pending planned outputs;
- whether the previous `IMAGE_ONLY` image batch has been recorded into state;
- interpreted user action, workflow step before the request, workflow step after handling the request, and the reason for that state transition.

## Next-Question Consistency

The only copyable next-turn prompts may appear in `下一步你可以这样问`. The first item should match the recommended default.

If the reply presents multiple schemes, layouts, styles, prompts, or other visual options, the first/recommended prompt must ask to generate/display multiple diverse first-round candidate images or schematic boards, normally 6, rather than merely asking the user to choose from text.

If P6 has selected a first-round direction, the first/recommended prompt must ask to enter P6b and set up second-round best-practice paper-local optimization axes.

If P6b setup is complete, the first/recommended prompt must ask to generate/display multiple second-round target-paper variants, normally 6.

Always include the fallback prompt:

`请使用 **<当前skill名称>**，根据当前状态，提供下一步提问建议。`

Every final `下一步你可以这样问` section must include a short session-continuation reminder: the assistant should continue from the active session/history by default, so the user does not need to manually upload or paste state during normal follow-up turns.

## Startup Gate

The first trigger must be a plan-only turn. It cannot analyze, download, build the specialized skill, construct prompts, generate images, or invoke image generation after the startup text.

If the user's first message asks to generate images immediately, record that request as pending only. The first assistant response is still startup text only and must not include `$imagegen`, a text-to-image API call, or any target-paper image artifact. Already-saved atlas images may be displayed by generated specialized skills as reference display.

## Stepwise Confirmation Gate

Generated specialized skills must guide one step at a time. A normal text turn should present the current step, the decision/options for that step, a default recommendation, and the exact confirmation or choice needed to continue. Do not jump from an initial request directly to final prompt, final figure, caption package, or paper text unless the required prior gates are already confirmed in state.

Require explicit user confirmation or choice before major transitions, including startup to B1, locking figure subtype/layout/metaphor/style, generating first-round candidate boards, selecting the first-round current best, generating P6b-IMAGE second-round variants, approving the final image brief, and starting any formal image-generation batch.

This gate does not mean refusing all non-recommended phrasing. It means interpreting the user's actual request, doing valid work, then placing the session at the correct original workflow step with prerequisites and pending actions recorded.

## Fast-Track Handling

If the user explicitly asks to skip the builder layer and directly make a figure, record skipped steps and fallback skill/taxonomy. Do not pretend a domain-specific generated skill exists unless it has been produced or provided.

## Response Modality Invariant

State must include whether the current response is `TEXT_ONLY` or `IMAGE_ONLY`. A text response cannot transition to target-paper candidate/final/revision image generation inside the same assistant response. If target-paper image generation is ready, set the next turn to the required `IMAGE_ONLY` step, then stop.

Non-target concept/modeling example images, including visual-structure examples, must be embedded in text replies when they are required explanatory references and do not satisfy P5, P6b-IMAGE, P8, the candidate-image bridge, or the second-round gate.

`IMAGE_ONLY` responses cannot include the status/output footer. The next `TEXT_ONLY` response after an `IMAGE_ONLY` response must record the generated image batch under `当前状态与产物`.
