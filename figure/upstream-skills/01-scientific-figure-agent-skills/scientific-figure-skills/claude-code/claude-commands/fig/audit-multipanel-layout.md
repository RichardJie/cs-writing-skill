---
description: "Audit multi-panel layout geometry, colorbars, semantic colors, and optical grid quality (scientific-figure-suite: fig-audit-multipanel-layout)"
argument-hint: "[figure request, file paths, or options]"
---

Run the `fig-audit-multipanel-layout` alias of the globally installed `scientific-figure-suite`
skill.

1. Load the skill: invoke `/scientific-figure-suite` via the Skill tool, or read
   `~/.claude/skills/scientific-figure-suite/SKILL.md` if the Skill tool is
   unavailable.
2. Read the command recipe
   `~/.claude/skills/scientific-figure-suite/commands/fig-audit-multipanel-layout.md`.
3. Follow the recipe and the SKILL.md Command Alias Router entry for
   `fig-audit-multipanel-layout`, applying the SKILL.md rules (scientific priority, no data
   fabrication, journal-status guardrail, project-local memory under
   `.claude/scientific-figure-memory/`).
4. Run any suite script as `python "$HOME/.claude/skills/scientific-figure-suite/scripts/<name>.py" ...`
   from the project root, and never install packages or download data without
   explicit approval.

Task text (alias already stripped): $ARGUMENTS
