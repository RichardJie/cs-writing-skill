---
name: winston-presentations
description: Write, structure, and critique presentations, talks, pitches, thesis defenses, class presentations and job talks using the principles from Patrick Winston's MIT lecture "How to Speak". Produces a promise-first outline, slide text, speaker notes, and a rehearsal checklist. Use this skill whenever the user wants to prepare, write, improve, or review a presentation, talk, pitch, defense (soutenance), class presentation (exposé), lecture, or slide deck — even if they only say "help me with my slides", "make my pitch better", "I present tomorrow", or "review my deck" — and use it BEFORE building a .pptx so the content is right before the file is generated.
---

# Winston Presentations

Help the user prepare a presentation that an audience will understand and remember, using the method from Patrick Winston's "How to Speak" (MIT). The core belief: speaking well is a skill you build with knowledge, practice and a few concrete rules, not a talent you either have or lack.

Reply in the user's language. Default to the user's own language for slides and notes too, unless they ask otherwise.

## Step 0: Frame (ask at most one question)

Find out, from the conversation first: the **context** (defense, job talk, pitch, class presentation, lecture, conference talk), the **audience**, the **duration**, and the **language**. If something is missing, state a reasonable assumption and continue. Ask only one question, and only if the answer would change the whole structure. Then read `references/contexts.md` and apply the matching variant.

## Step 1: Promise and core idea

Before any slide, write down:

1. **The empowerment promise**: one sentence saying what the audience will be able to know or do by the end. Open with it. A joke at the start lands badly because the audience is still settling in; a promise gives people a reason to stay.
2. **The salient idea**: the one thing to remember if they forget everything else. Give it a short **name** (a slogan or label), and say what it is *not* (building a fence), so it cannot be confused with a similar idea.
3. **The 5 S check** (memorability): does the talk have a **Symbol** (one visual that stands for the idea), a **Slogan**, a **Surprise**, a **Salient** idea (it stands out, one only), and a **Story**?

## Step 2: Structure

Draft the outline using the context variant. Then apply these four techniques, because attention drifts constantly and the structure must catch people who drop out:

- **Cycle**: state the core idea at least three times, in different words (promise, middle, conclusion).
- **Fence**: contrast with the nearest neighbour idea.
- **Verbal punctuation**: announce transitions ("first... second... that was the problem, now the solution") so a listener who drifted can get back on.
- **One question, then wait**: ask one real question and leave a long silence (up to about seven seconds). Avoid questions that are too obvious or too hard.

## Step 3: Slide text

Slides are for exposing ideas, not for teaching them: a person cannot read and listen at the same time, so dense slides make the audience stop listening.

- One idea per slide, and a handful of words. Rule of thumb (not Winston's number): over ~20 words, it is a handout, not a slide.
- Very large text. If it needs a small font, there is too much on it.
- No bullet walls, no logos on every slide, no slide titles that only repeat what the speaker says.
- Prefer a picture, a diagram, or a single sentence. Leave empty space; empty space is the audience's thinking room.
- Never read the slides aloud.
- Put collaborators' names on the **first** slide, not the last.
- Use a small arrow added in the slide, not a laser pointer (a laser pointer makes the speaker turn their back).
- If the idea is hard to explain, suggest a board or a physical prop instead of more slides.

See `references/examples.md` for before/after rewrites.

## Step 4: Speaker notes

For each slide, write a short note: what to say, where the core idea is **cycled**, the **verbal punctuation** line, and any **pause**. Mark where to look at the audience, not the screen.

## Step 5: Ending

- The **last slide** states the **contributions**: what the audience now has or what the speaker did. Not "Thank you", not "Questions?", not a conclusions list nobody asked for.
- The **last words**: a joke is acceptable at the end, when the audience is tuned in. Avoid a bare "thank you", which suggests people stayed out of politeness. Prefer a sincere salute to the audience.
- If an institution requires acknowledgments or a "questions" slide, follow the institution first and keep the contributions slide just before it.

## Step 6: Rehearsal and room checklist

Always give this checklist (details in `references/winston-principles.md`):

- Rehearse out loud, ideally in front of friends who **do not** know the subject. Experts fill in the gaps mentally and give false reassurance.
- Visit the room beforehand if possible. Aim for good lighting (dim light makes people sleepy), a room that is more than half full, and a time when people are alert (mid-morning is ideal).
- Print the slides on a table and look for density.
- Keep hands out of pockets and behind the back; use them to gesture or hold a prop.

## Output format

Unless the user asks otherwise, give the result **in the chat as plain text**:

1. **Promise** and **core idea** (named, with fence)
2. **Outline** (with the three cycles marked)
3. **Slides**: number, on-slide text, speaker note
4. **Ending**: contributions slide + last words
5. **Checklist**

If the user wants a PowerPoint file, finish this plan first, get approval, then use the available presentation (pptx) skill to build it.

## Review mode

If the user shares an existing deck or script: audit it against Steps 1-5, list the **three highest-impact problems** first, and rewrite two or three slides as concrete examples rather than rewriting everything. Keep the feedback direct and kind.

## Attribution

Based on Patrick H. Winston's lecture "How to Speak" (MIT OpenCourseWare / IAP). This skill is an independent paraphrase and is not affiliated with MIT.
