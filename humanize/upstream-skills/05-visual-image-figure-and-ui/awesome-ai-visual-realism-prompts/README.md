# Awesome AI Visual Realism Prompts

> A cookbook of prompt-engineering principles to get **photorealistic and cinematic** results from AI image/video models — Higgsfield (Nano Banana / Seedance / Cinema Studio), Midjourney, Flux, Veo, Kling, Sora, and beyond.

Distilled from production work on 9:16 short-form video, commercial product photography, and AI-augmented filmmaking. Tool-agnostic. Use these principles to upgrade *any* T2I/T2V/I2V prompt you write.

---

## Why this exists

Most AI prompt advice on the internet is generic ("cinematic, 4k, photorealistic"). It doesn't tell you **what photorealism actually requires** at the perceptual level:

- Skin must have **subsurface scattering**, not flat color
- Liquids must obey **Fresnel reflections** and **caustics**
- Cloth must show **anisotropic weave** and **wrinkle physics**
- Contact between objects must show **occlusion shadow** and **micro-bounce light**
- A cinematic shot has a **lens choice, an aperture, a movement, and a master DP reference** — not just "cinematic"

This cookbook gives you the vocabulary.

---

## Table of Contents

| # | Doc | What's inside |
|---|---|---|
| 01 | [Physical Realism](docs/01-physical-realism.md) | PBR / SSS / liquids / cloth / contact / anatomy / Anti-AI-Slop checklist |
| 02 | [Cinematic Lighting](docs/02-cinematic-lighting.md) | 5 master cinematographer signature lighting setups |
| 03 | [Composition](docs/03-composition.md) | Signature framing from Kubrick / Wes Anderson / Wong Kar-wai / Tarkovsky |
| 04 | [Camera Motion Vocabulary](docs/04-camera-motion.md) | 12 cinematography movement terms with prompt examples |
| 05 | [Action Grammar](docs/05-action-grammar.md) | 8 commercial-style actions (beauty / product / fashion) |
| 06 | [Higgsfield Cinema Studio Rules](docs/06-higgsfield-cinema-studio.md) | 6 hard rules + 3 lessons learned |
| 07 | [Seedance Cinema Modes](docs/07-seedance-cinema-modes.md) | 5 mode grammar (Narrative / Studio / Action / Performance / Atmospheric) |

Plus:
- [`prompts/`](prompts/) — Drop-in templates by category
- [`examples/`](examples/) — Community contributions welcome (open PR)

---

## How to use

### Quick start

1. **Pick the layer you need** — most prompts fail because they're missing only one layer. Skim the TOC, find what's missing.
2. **Stack don't replace** — physical realism + lighting + composition + motion are independent. Stack them in a single prompt.
3. **Anchor to a master** — instead of "cinematic," write "cinematography in the style of Roger Deakins, low-key key light camera-right, ambient bounce from below."
4. **Read the Anti-Slop checklist** — every prompt failure has a name. Doc 01 has the list.

### Prompt anatomy template

A production-quality prompt has roughly 5 stacked layers:

```
[Subject + Action]
  + [Physical Realism details — see doc 01]
  + [Lighting — see doc 02]
  + [Composition — see doc 03]
  + [Camera motion / lens — see doc 04]
  + [Style anchor — DP / film stock / decade]
```

See [`prompts/anatomy-template.md`](prompts/anatomy-template.md) for full worked examples.

---

## Who this is for

- Prompt engineers tired of "cinematic, 4k, hyperrealistic" failures
- AI filmmakers using Higgsfield / Veo / Kling / Sora for short-form video
- Commercial photographers using Nano Banana / Midjourney / Flux for product shots
- Anyone moving from "AI looks AI" → "AI looks photographed"

This is *not* a Higgsfield tutorial — though the principles work especially well with Seedance i2v and Nano Banana Pro, because those models reward precise physical-realism vocabulary.

---

## Contributing

PRs welcome — especially:
- More master DP signature lighting recipes
- New Anti-AI-Slop failure modes you've found
- Worked examples (prompt + output image + analysis)

Open an issue first if you're adding a whole new doc.

---

## License

MIT — see [LICENSE](LICENSE).

You may use, modify, and redistribute these prompts and principles in commercial work. Attribution appreciated but not required.

---

## Author / Credits

Compiled by **[@keng_1304](https://instagram.com/keng_1304)** — director / AI workflow builder, based in Taipei.

Studio: [tzukao.com](https://tzukao.com)

If this saved you a credit, ping me on IG. If you ship something interesting with it, I'd love to see.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

---

> *"AI looking AI is a vocabulary problem, not a model problem."*
