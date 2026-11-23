# Visual Style Taxonomy and Selection Protocol

Version: 2.0.5

Use this reference when the conversation reaches visual language, style-family selection, candidate-board design, or image-prompt construction.

## Core Rule

Style is chosen after reader effect, paper claim, figure role, and layout logic. When style or visual structure is a live decision, present 4-6 relevant options, normally 6, and recommend one default. If a saved style/layout/structure atlas board exists, display it with a Markdown image embed in the `TEXT_ONLY` reply before asking the user to choose. Do not describe layout skeleton, panel choreography, module topology, or arrow grammar with prose/bullets only. Then require the visual candidate-board bridge unless the user explicitly skips image candidates.

## Style Families

- Clean editorial flat
- Formal architecture schematic
- Mechanism snapshot
- Premium scientific illustration
- Isometric / soft 3D
- Low-poly / abstract 3D
- Cartoon / comic-lite
- Storyboard panels
- Tile / card / mosaic board
- Paper-cut / layered collage
- Blueprint / technical drawing
- Dashboard / interface metaphor
- Mini-evidence infographic
- Minimal line-art schematic
- Photorealistic / cinematic, only when concrete realism is necessary

## Visual Communication Art Style Axis

Generated skills must treat visual communication art style as a first-class taxonomy axis, not a loose decoration. The saved atlas should include labeled examples for the style families relevant to the generated figure class. At minimum, classify style choices by:

- abstraction level: literal / schematic / symbolic / metaphorical;
- dimensionality: flat / layered / isometric / 3D;
- visual language: editorial, technical, infographic, interface-like, storyboard, scientific illustration;
- communication tone: formal, explanatory, premium, playful-light, reviewer-facing;
- density: sparse, balanced, dense, appendix-grade.

When discussing this axis in text, display the matching saved style board or thumbnail with Markdown image syntax if present. If it is absent, record the missing style atlas asset and recommend generating or repairing it. Plain path lists do not count as display.

## Style-Board Protocol

When style selection matters:

1. `TEXT_ONLY`: compare 4-6 style families, normally 6, and recommend a default.
2. `TEXT_ONLY`: display any relevant saved style atlas board with a Markdown image embed, then set up a style candidate board. Hold figure thesis, panel plan, labels, and color semantics fixed; vary only style family.
3. `IMAGE_ONLY`: generate/display 4-6 style candidates, normally 6.
4. `TEXT_ONLY`: record the image batch and ask the user to select, revise, combine, or request another board.

Do not ask the user to lock a style from prose alone unless they explicitly choose text-only selection.

## Reference Image Use

If the user provides reference figures, analyze transferable principles rather than copying:

- line weight and shape language;
- flat/layered/isometric/3D depth model;
- object realism;
- color semantics;
- density and whitespace;
- label placement;
- panel rhythm;
- seriousness or playfulness.

Record per-image preferred attributes and negative-reference constraints.
