# 06 — Higgsfield Cinema Studio Rules

Higgsfield Cinema Studio is a multi-scene narrative video generator. It accepts an **anchor image** + scene-by-scene descriptions and produces multi-shot sequences with character consistency.

These 6 rules cover how to write prompts that actually use what Cinema Studio is good at, and 3 lessons learned from production runs.

> Applies to Cinema Studio 2.5 / 3.0. Other Higgsfield modes (Soul V2 for single character, Marketing Studio for ads, Nano Banana for stills) have different conventions — see `higgsfield-generate` skill docs.

---

## The 6 hard rules

### Rule 1 — Anchor first, story second

Cinema Studio uses the anchor image to lock character/wardrobe/environment. Write the anchor description fully before describing any scene action.

```
ANCHOR: A young woman in a navy linen jumpsuit, shoulder-length brown
hair with subtle waves, standing in a sunlit minimalist apartment with
white walls and a single large window camera-left. Natural soft lighting,
85mm shallow depth of field.

SCENE 1: She sits on the windowsill, looking out at...
SCENE 2: She walks slowly to the kitchen island...
```

If the anchor is vague, every scene drifts.

---

### Rule 2 — 2 to 6 scenes, not more

Cinema Studio degrades past 6 scenes. Drift accumulates — by scene 7 the character looks different. Hard cap: **6 scenes per generation**.

Long sequences? Run two generations and concatenate in post.

---

### Rule 3 — Action verb per scene, no nested actions

Each scene = one clear action verb.

```
✅ SCENE 1: She picks up a coffee mug
✅ SCENE 2: She walks to the window
✅ SCENE 3: She looks out at the city skyline

❌ SCENE 1: She picks up coffee, walks to window, then looks at sky,
            then sips while smiling and pets her cat
```

Nested actions confuse the temporal model. Split into separate scenes.

---

### Rule 4 — Camera motion declared per scene

Specify camera movement for each scene. Don't let the model pick.

```
SCENE 1 — [Camera: locked-off mid-shot, no movement]
She sits on the windowsill.

SCENE 2 — [Camera: tracking shot following her steps, parallel to action]
She walks to the kitchen island.

SCENE 3 — [Camera: slow push-in to close-up over 4 seconds]
She pours water from a glass pitcher.
```

See [04 — Camera Motion](04-camera-motion.md) for vocabulary.

---

### Rule 5 — Lighting continuity must be stated

If the anchor says "soft warm window light, late afternoon," every scene must reaffirm or explicitly transition the lighting.

```
SCENE 1: ... [lighting: continuing late afternoon warm window key]
SCENE 2: ... [lighting: same key, now backlit as she walks past window]
SCENE 3: ... [lighting: TRANSITION — sun has set, warm practical lamp now key]
```

Without this, lighting jumps between scenes randomly.

---

### Rule 6 — Negative prompt at the end

Cinema Studio accepts a negative prompt. Use it to lock out failure modes:

```
NEGATIVE: cartoon style, anime, plastic skin, deformed hands,
character outfit change between scenes, hair color shift,
multiple people appearing, daytime/nighttime jump
```

---

## The 3 lessons learned

### Lesson 1 — Wardrobe drift is the #1 consistency killer

Even with an anchor image, wardrobe drifts by scene 3. Mitigation:

- Use distinctive wardrobe elements (a bright scarf, a specific color jacket)
- Mention the wardrobe in every scene description, not just the anchor
- Avoid generic outfits ("white shirt, blue jeans") — the model invents details and they drift

### Lesson 2 — Don't change setting mid-generation

Cinema Studio handles character continuity. It does **not** handle environment continuity well. If scene 1 is indoors and scene 3 is outdoors, the connecting scene 2 will be a mess.

Mitigation: keep all 2-6 scenes in the same setting. Use a follow-up generation for the next setting.

### Lesson 3 — Time-of-day shifts need scene-level lighting reset

If you want to show "morning → noon → evening," you cannot do it in one Cinema Studio generation. Lighting will drift unpredictably.

Mitigation: 1 generation per time-of-day, then concatenate.

---

## Worked example — bad vs good

### Bad

```
A woman in a kitchen makes breakfast. She cooks eggs, then sits at the
table, then drinks coffee, then opens her laptop and works.
```

Problems: 4+ scenes nested, no anchor, no camera direction, no lighting.

### Good

```
ANCHOR: A 30-year-old woman with shoulder-length dark hair, wearing a
charcoal grey wool cardigan over a white t-shirt, in a sunlit Scandinavian
kitchen with white walls, light oak counters, and a large east-facing
window providing warm morning light from camera-right. Shot 35mm, f/2.8,
natural color grade.

SCENE 1 — [Camera: locked-off wide, no movement] [Lighting: warm morning
window key from camera-right, cool ambient fill]
She stands at the counter cracking eggs into a bowl. Slow deliberate motion.

SCENE 2 — [Camera: slow push-in from wide to medium over 4s] [Lighting:
same morning key]
She pours the eggs into a hot pan, gentle sizzle.

SCENE 3 — [Camera: medium close-up, locked off] [Lighting: same morning key]
She tilts the pan, eggs fold over. Subtle smile of satisfaction.

NEGATIVE: cartoon style, deformed hands, outfit change, multiple people,
nighttime, harsh lighting, plastic skin
```

3 scenes, clear anchor, camera per scene, lighting continuity, negative prompt.

---

## Common mistakes

- ❌ Writing 7+ scenes → drift will ruin the last 2.
- ❌ Anchor too vague ("a person in a room") → no character lock.
- ❌ Switching environments mid-generation → connector scenes break.
- ❌ Forgetting negative prompt → wardrobe drift, hand horror, etc.
- ✅ 2-6 scenes, one setting, one time-of-day, full anchor, per-scene camera/lighting, explicit negative.

---

## Next

→ [07 — Seedance Cinema Modes](07-seedance-cinema-modes.md)
