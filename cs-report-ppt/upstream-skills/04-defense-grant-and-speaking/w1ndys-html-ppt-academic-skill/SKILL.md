---
name: html-ppt-academic
description: Academic HTML PPT Studio — create thesis defense, proposal defense, midterm review, research group meeting, and academic presentation decks as static HTML. Use when the user asks for 论文答辩, 毕业答辩, 开题报告, 中期答辩, 预答辩, 硕士论文, 博士论文, 本科毕设, 学术汇报, 研究生组会, research presentation, thesis defense, dissertation defense, proposal defense, or any university-style academic slides.
---

# html-ppt-academic — Academic HTML PPT Skill

Create formal academic presentation decks as static HTML/CSS/JS. This skill is adapted from the `html-ppt-skill` design philosophy: token-driven themes, reusable layouts, full-deck templates, keyboard navigation, and presenter notes.

## When To Use

Use this skill when the user needs:

- 本科毕业设计答辩 PPT
- 硕士或博士论文答辩 PPT
- 开题报告、中期答辩、预答辩
- 研究生组会、论文精读、学术会议汇报
- 教师课程汇报、科研项目结题汇报
- Formal academic slides with speaker notes

Trigger keywords include: `论文答辩`, `毕业答辩`, `开题报告`, `中期答辩`, `预答辩`, `本科毕设`, `硕士论文`, `博士论文`, `研究生组会`, `学术汇报`, `thesis defense`, `dissertation defense`, `proposal defense`, `academic presentation`.

## Required Clarifications

Before authoring a deck, determine these fields from the user's request or ask concise questions:

1. Degree level: undergraduate, master, PhD, course project, research group meeting.
2. Defense type: proposal, midterm, final defense, pre-defense, seminar.
3. Discipline: computer science, engineering, medicine, economics, education, humanities, social science, art/design.
4. Duration and slide count: for example 8 minutes / 10 slides, 15 minutes / 12 slides, 30 minutes / 20 slides.
5. Visual preference: blue academic, red university, minimal white, serif paper.
6. Required identity fields: school, college, major, title, student, advisor, date, logo.

If the user provides rich content, choose tasteful defaults and proceed:

- Master/PhD final defense → `thesis-defense` template + `thesis-defense-blue` theme.
- Undergraduate graduation defense → `thesis-defense` template + `thesis-defense-minimal` theme.
- Humanities/social science → `thesis-defense-serif` theme.
- University/government/policy topic → `thesis-defense-red` theme.

## Default Deck Structure

For final thesis defense, use this structure:

1. Cover
2. Table of contents
3. Research background and significance
4. Literature review and research gap
5. Research objectives and questions
6. Technical route or research framework
7. Method, model, or system design
8. Experiment design or case study setup
9. Results and analysis
10. Contributions and innovations
11. Conclusion, limitations, and future work
12. Thanks and Q&A

For proposal defense, replace result-heavy slides with:

- Research plan
- Feasibility analysis
- Schedule and milestones
- Expected outcomes

For midterm defense, emphasize:

- Completed work
- Current progress
- Problems encountered
- Next-stage plan

## Authoring Rules

- Use `templates/full-decks/thesis-defense/` as the starting point for defense decks.
- Use `templates/style-presets/thesis-defense.json` to select slide plan, theme, and density rules.
- Put audience-facing content on slides and speaker guidance in `<aside class="notes">`.
- Keep each slide focused on one academic argument.
- Prefer diagrams, tables, and charts over long paragraphs.
- Use 3-5 bullets per content slide.
- Keep animations minimal: `fade-up`, `rise-in`, `stagger-list`.
- Use academic wording: precise, evidence-based, formal, and concise.
- Add Q&A backup slides when the topic suggests likely committee questions.
- Avoid decorative visual effects in formal defense decks.

## Speaker Notes Rules

For thesis defense decks, every slide should include `<aside class="notes">`.

- 80-180 Chinese characters per slide for short defenses.
- 150-300 Chinese characters per slide for 15-30 minute defenses.
- Highlight the transition logic: why this slide follows the previous one.
- Include oral explanation cues, data interpretation cues, and defense reminders.
- Do not place presenter-only reminders directly on the visible slide.

## File Structure

```text
html-ppt-academic-skill/
├── SKILL.md
├── README.md
├── assets/
│   ├── base.css
│   ├── runtime.js
│   └── themes/
│       ├── thesis-defense-blue.css
│       ├── thesis-defense-red.css
│       ├── thesis-defense-minimal.css
│       └── thesis-defense-serif.css
├── templates/
│   ├── full-decks/thesis-defense/
│   ├── single-page/
│   └── style-presets/
├── references/
│   ├── thesis-defense.md
│   ├── themes.md
│   └── customization.md
├── scripts/
│   └── new-deck.sh
└── examples/
    └── thesis-defense-demo/
```

## Quick Start

```bash
# Create a new academic deck
./scripts/new-deck.sh my-defense thesis-defense

# Open the generated deck
open examples/my-defense/index.html
```

Keyboard shortcuts:

```text
← → Space PgUp PgDn    navigate
F                      fullscreen
S                      presenter notes window
O                      slide overview
T                      cycle configured themes
```

## Recommended Output

When completing a deck, provide:

- Generated deck path
- Selected template and theme
- Slide count
- Notes coverage
- Any missing user-provided fields such as school logo or advisor name
