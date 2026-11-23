# Two-Layer Skill Builder Workflow

Version: 2.0.5

## Purpose

The factory first generates a specialized figure-making skill for a chosen paper-figure class, then uses that locked generated skill for arbitrary target-paper production.

## Layer A: Skill Builder

B1-B9 produce a reusable skill:

1. Target figure-class brief.
2. Corpus plan.
3. Lawful local corpus and retrieval manifest.
4. Figure/caption/panel evidence extraction.
5. Evidence-backed taxonomy and subtype/style atlas coverage plan.
6. Saved subtype/style illustration atlas and specialized skill blueprint.
7. Generated skill artifacts.
8. Test report and patches.
9. Locked generated skill with slug, version, package path, limitations, and test results.

## Layer B: Figure Production

P1-P9 plus P6b/P6c use the generated skill:

1. P1 startup/material intake with available saved atlas display.
2. P2 figure need diagnosis and subtype routing with relevant saved atlas or concept/example display.
3. P3 reader-effect contract and 4-6 text candidates, with saved style/layout boards or non-target concept/modeling examples when abstract decisions are discussed.
4. P4 diverse first-round visual candidate-board setup with an embedded generic structure/reference image when structure is discussed.
5. P5 `IMAGE_ONLY` diverse first-round candidate-board generation.
6. P6 first-round candidate review and current-best direction selection.
7. P6b best-practice paper-local divergence setup with an embedded generic optimization-structure image when structure is discussed.
8. P6b-IMAGE `IMAGE_ONLY` second-round variant generation.
9. P6c second-round review and final direction lock.
10. P7 final image brief.
11. P8 `IMAGE_ONLY` formal generation/revision.
12. P9 review, caption, legend, and body text.

P4/P5/P6 are mandatory after multi-option text decisions unless the user explicitly chooses text-only selection. P6b/P6b-IMAGE/P6c are mandatory after P6 first-round selection unless the user explicitly overrides the second round and the limitation is recorded.

The first image round should maximize high-level diversity to establish direction. The second image round should keep the chosen direction mostly fixed and optimize around paper-local details such as module relationships, evidence/case anchors, label economy, panel transitions, color semantics, callout placement, and reviewer readability.

Generated skills must package `assets/subtype-atlas/manifest.json`, `assets/subtype-atlas/boards/`, `assets/subtype-atlas/thumbnails/`, and `references/subtype-illustration-atlas.md`. Saved atlas boards and non-target concept/modeling example images must appear in `TEXT_ONLY` replies for abstract-decision triggers. Saved reference or non-target visual-structure images must appear when text replies explain layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture; text-only structure descriptions are invalid. Target-paper candidate/final/revision generation remains `IMAGE_ONLY`.

## Production Unlock

P1-P9 are available only when:

```yaml
production_unlocked: true
production_unlocked_by: generated_skill_locked | full_production_fast_track
```

If the generated skill is not locked and the user has not chosen fast-track, continue builder B2-B9 rather than target-paper production.
