# cs-writing-skill

Cross-harness Agent Skill pack. Each skill lives in its own directory with a `SKILL.md`; optional `agents/openai.yaml` supplies harness-specific UI strings.

```text
cs-writing-skill/
├── README.md
├── paper-boundaries/      # Prevent defensive writing: press-conference principle
│   ├── SKILL.md
│   └── agents/openai.yaml
├── plain/                 # Explanation technique: make hard ideas click
│   ├── SKILL.md
│   └── agents/openai.yaml
└── humanize/              # Remove AI voice (:chinese / :english tracks)
    ├── SKILL.md           # Hub router
    ├── chinese.md         # 去 AI 味 — 七步手术法 + 中文模式
    ├── english.md         # Pattern catalog + direct-statement rules
    └── agents/openai.yaml
```

## Skills

| Skill | Role | Typical use |
|-------|------|-------------|
| `paper-boundaries` | Prevent defensive paper writing and narrative self-undermining | Revise abstracts, restructure experiments, catch self-undermining phrasing |
| `plain` | Explain difficult concepts clearly | Walk through a paper/model with a small worked example, fix misconceptions |
| `humanize` | Remove AI tone from prose | `:chinese` for 去AI味; `:english` for humanize / remove AI tells |

The three skills are independent: `paper-boundaries` governs *how to write and organize evidence without defensive self-undermining*; `plain` governs *how to explain and repair understanding*; `humanize` governs *how to strip AI voice from finished prose*.

---

## MIRASIM

### Install

1. Open **Plugins → Skill Pack → Install from GitHub**
2. Enter the repo URL: `https://github.com/RichardJie/cs-writing-skill`
3. MIRASIM discovers every top-level subdirectory that contains a `SKILL.md` and installs each as a separate skill

Install location: `~/.mirasim/skills/<skill-name>/`

### Update

Click **Update** on a skill card, or run **Install from GitHub** again (overwrites the local copy).

### Usage

Use **slash commands** in the MIRASIM chat input:

| Command | What it does |
|---------|--------------|
| `/paper-boundaries` | Revise, compress, or restructure narrative under the press-conference principle |
| `/plain` | Explain a concept with a small, domain-native numerical walkthrough |
| `/humanize :chinese` | 去 AI 味 — 七步手术法，中文模式扫描 |
| `/humanize :english` | Humanize English — pattern catalog, em-dash ban, direct-statement rules |

Natural-language triggers also work, for example:

- "Use paper-boundaries to revise this abstract"
- "Use plain to explain what attention is actually computing"
- "去 AI 味 / humanize :chinese this paragraph"
- "humanize :english — remove AI tells from this README"

### Humanize language tracks

One installable skill (`humanize/`), two tracks via prompt tag:

| Tag | Reads | Best for |
|-----|-------|----------|
| `:chinese` | `humanize/chinese.md` | Chinese prose, 公众号, CN blogs |
| `:english` | `humanize/english.md` | English essays, READMEs, LinkedIn, docs |

If no tag is given, infer from input language; ask once when unclear.

### Note on descriptions

MIRASIM reads the `description` field from each `SKILL.md` frontmatter using a **single-line** parser. Do not use YAML folded scalars (`>-`); the card will show `>-` instead of the text.

---

## Claude Code

### Install

```bash
git clone https://github.com/RichardJie/cs-writing-skill.git /tmp/cs-writing-skill
mkdir -p ~/.claude/skills
cp -R /tmp/cs-writing-skill/paper-boundaries ~/.claude/skills/
cp -R /tmp/cs-writing-skill/plain ~/.claude/skills/
cp -R /tmp/cs-writing-skill/humanize ~/.claude/skills/
```

Project-scoped install: copy skill directories to `<project>/.claude/skills/`.

### Usage

Mention the skill by name or describe a matching task; explicit invocation: `$paper-boundaries` / `$plain` / `$humanize :english` / `$humanize :chinese`.

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
- Long sub-skills use progressive disclosure (`humanize/chinese.md`, `humanize/english.md`) referenced from the hub `SKILL.md`
