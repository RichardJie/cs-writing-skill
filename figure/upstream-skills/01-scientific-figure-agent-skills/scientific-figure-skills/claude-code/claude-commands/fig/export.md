---
description: "Export and submission package mode for scientific figures (scientific-figure-suite: fig-export)"
argument-hint: "<figure files, formats, target journal>"
---

Run the `fig-export` alias of the globally installed `scientific-figure-suite`
skill.

1. Load the skill: invoke `/scientific-figure-suite` via the Skill tool, or read
   `~/.claude/skills/scientific-figure-suite/SKILL.md` if the Skill tool is
   unavailable.
2. Read the command recipe
   `~/.claude/skills/scientific-figure-suite/commands/fig-export.md`.
3. Follow the recipe and the SKILL.md Command Alias Router entry for
   `fig-export`, applying the SKILL.md rules (scientific priority, no data
   fabrication, journal-status guardrail, project-local memory under
   `.claude/scientific-figure-memory/`).
4. Run any suite script as `python "$HOME/.claude/skills/scientific-figure-suite/scripts/<name>.py" ...`
   from the project root, and never install packages or download data without
   explicit approval.

Task text (alias already stripped): $ARGUMENTS
