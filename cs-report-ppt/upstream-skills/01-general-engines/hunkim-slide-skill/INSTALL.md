# INSTALL

**This file is written for an agent.** If a user hands you this repository URL and says
"install this for me", follow it top to bottom. Humans can just read the
[README](README.md) instead.

- Repository: <https://github.com/hunkim/slide-skill>
- What it is: an Agent Skill — a single `SKILL.md` at the repo root, named `slide-design`.
- Dependencies: **none.** No API key, no runtime, no scripts. Clone and you are done.

## 1. Choose the install directory

The directory must be named **`slide-design`** — hosts match the folder name against the
skill's `name:` field. The repository is named `slide-skill`; the skill inside is
`slide-design`. Do not clone into a folder called `slide-skill`.

| Host | Personal (every project) | Project-local |
|---|---|---|
| Claude Code | `~/.claude/skills/slide-design` | `<project>/.claude/skills/slide-design` |
| Codex CLI | `~/.codex/skills/slide-design` | `<project>/.agents/skills/slide-design` |
| Claude app (Cowork) | upload a `.skill` bundle — step 4 | — |

Default to the personal directory unless the user says they want it for one project only.
On Windows, `~` is `$env:USERPROFILE` (`%USERPROFILE%`).

## 2. Clone

macOS / Linux / WSL:

```bash
git clone https://github.com/hunkim/slide-skill.git ~/.claude/skills/slide-design
```

Windows PowerShell:

```powershell
git clone https://github.com/hunkim/slide-skill.git "$env:USERPROFILE\.claude\skills\slide-design"
```

If the directory already exists, update it instead of deleting the user's copy:
`git -C <dir> pull --ff-only`. If `git` is missing: `winget install Git.Git` on Windows,
`brew install git` on macOS, the distro package manager on Linux.

## 3. Verify

`SKILL.md` must exist in the install directory and start with YAML frontmatter containing
`name: slide-design`:

```bash
head -3 <dir>/SKILL.md
```

Windows: `Get-Content "<dir>\SKILL.md" -TotalCount 3`

That is the whole check — there is nothing to execute and nothing to configure.

## 4. Cowork (Claude app) only

Cowork installs a bundle, not a clone:

```bash
git clone https://github.com/hunkim/slide-skill.git slide-design
rm -rf slide-design/.git
zip -Xr slide-design.skill slide-design
```

```powershell
git clone https://github.com/hunkim/slide-skill.git slide-design
Remove-Item -Recurse -Force slide-design\.git
Compress-Archive -Path slide-design -DestinationPath slide-design.zip
Rename-Item slide-design.zip slide-design.skill
```

Tell the user to attach the `.skill` file in the chat window and save it.

## 5. Report back

Tell the user, in their language:

1. Where it was installed.
2. That the host picks the skill up on a **new session** (restart Codex if it doesn't
   appear).
3. That it loads by itself whenever they ask for slides, a deck, or a presentation — in
   English or Korean ("발표자료 만들어줘") — and also when they say a slide is
   "too complex" / "너무 복잡해". They can also call it by name: `use the slide-design skill`.
