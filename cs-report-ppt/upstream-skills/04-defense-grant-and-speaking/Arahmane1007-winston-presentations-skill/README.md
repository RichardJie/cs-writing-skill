# winston-presentations

A Claude skill that helps you write better presentations, talks, pitches and thesis defenses using the principles of Patrick Winston's MIT lecture [*How to Speak*](https://www.youtube.com/watch?v=Unzc731iCUY).

Un skill Claude pour préparer de meilleures présentations (soutenances, exposés, pitchs, job talks) à partir des conseils de la conférence *How to Speak* de Patrick Winston (MIT).

## What it does

Given your topic, audience and duration, Claude produces:

1. An **empowerment promise** and a **named core idea** (with a "fence")
2. An **outline** with the core idea cycled three times
3. **Slide text** (sparse, one idea per slide) and **speaker notes**
4. A strong **ending** (contributions slide, no bare "thank you")
5. A **rehearsal and room checklist**

It can also **review** an existing deck and rewrite its weakest slides. When you want a `.pptx`, it plans the content first, then hands off to a presentation-building skill.

## Install

- **Claude.ai**: download `winston-presentations.skill` from the Releases page, then use *Save skill* on the file card, or add the `winston-presentations/` folder through your skills settings.
- **Claude Code**: copy the `winston-presentations/` folder into `~/.claude/skills/` (or your project's `.claude/skills/`).

## Structure

```
winston-presentations/
├── SKILL.md                      # workflow and rules
└── references/
    ├── winston-principles.md     # the why behind each rule
    ├── contexts.md               # defense, job talk, pitch, class, lecture...
    └── examples.md               # before/after rewrites
```

## Contributing

Issues and pull requests are welcome: new context variants, better examples, translations of the examples, or corrections to how Winston's ideas are applied. Rules that go beyond what Winston said are marked *(adaptation)* in `references/contexts.md`.

## Credits and license

Based on Patrick H. Winston's lecture *How to Speak* (MIT OpenCourseWare). This project is an independent paraphrase, not affiliated with or endorsed by MIT. Released under the MIT License (see `LICENSE`).
