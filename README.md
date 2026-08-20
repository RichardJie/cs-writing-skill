# cs-writing-skill

Cross-harness Agent Skill pack. Each skill lives in its own directory with a `SKILL.md`; optional `agents/openai.yaml` supplies harness-specific UI strings.

```text
cs-writing-skill/
├── README.md
├── cs-writing/          # Writing boundaries: press-conference principle
│   ├── SKILL.md
│   └── agents/openai.yaml
└── plain/               # Explanation technique: make hard ideas click
    ├── SKILL.md
    └── agents/openai.yaml
```

## Skills

| Skill | Role | Typical use |
|-------|------|-------------|
| `cs-writing` | Constrain paper narrative and writing boundaries | Revise abstracts, restructure experiments, catch self-undermining phrasing |
| `plain` | Explain difficult concepts clearly | Walk through a paper/model with a small worked example, fix misconceptions |

The two skills are independent: `cs-writing` governs *how to write and organize evidence*; `plain` governs *how to explain and repair understanding*.

---

## MIRASIM

### Install

1. Open **Plugins → Skill Pack → Install from GitHub**
2. Enter the repo URL: `https://github.com/RichardJie/cs-writing-skill`
3. MIRASIM discovers every subdirectory that contains a `SKILL.md` and installs each as a separate skill

Install location: `~/.mirasim/skills/<skill-name>/`

### Update

Click **Update** on a skill card, or run **Install from GitHub** again (overwrites the local copy).

### Usage

Use **slash commands** in the MIRASIM chat input:

| Command | What it does |
|---------|--------------|
| `/cs-writing` | Revise, compress, or restructure narrative under the press-conference principle |
| `/plain` | Explain a concept with a small, domain-native numerical walkthrough |

Natural-language triggers also work, for example:

- "Use cs-writing to revise this abstract"
- "Use plain to explain what attention is actually computing"

### Note on descriptions

MIRASIM reads the `description` field from each `SKILL.md` frontmatter using a **single-line** parser. Do not use YAML folded scalars (`>-`); the card will show `>-` instead of the text.

---

## Claude Code

### Install

```bash
git clone https://github.com/RichardJie/cs-writing-skill.git /tmp/cs-writing-skill
mkdir -p ~/.claude/skills
cp -R /tmp/cs-writing-skill/cs-writing ~/.claude/skills/
cp -R /tmp/cs-writing-skill/plain ~/.claude/skills/
```

Project-scoped install: copy skill directories to `<project>/.claude/skills/`.

### Usage

Mention the skill by name or describe a matching task; explicit invocation: `$cs-writing` / `$plain`.

---

## Adding a New Skill

1. Create `<skill-name>/SKILL.md` at the repo root (required)
2. Optionally add `<skill-name>/agents/openai.yaml` for harness UI strings
3. Frontmatter example:

```yaml
---
name: my-skill
description: "Single-line description; parses correctly in MIRASIM and other harnesses"
---
```

4. Commit, push, then reinstall or click **Update** in your harness.

## Conventions

- One skill = one top-level directory + `SKILL.md`
- Always use a single quoted `description` line (MIRASIM-compatible)
- `agents/openai.yaml` is optional metadata; MIRASIM skill cards do not read it
- Keep each skill focused; do not merge unrelated responsibilities
