# rebuttal-skills

Two composable [Claude Code](https://claude.com/claude-code) skills for writing conference/journal **author-response rebuttals** (NeurIPS, ICLR, ICML, CVPR/ICCV/ECCV, AAAI, ACL/ARR/EMNLP, IEEE venues, …).

| Skill | What it does | When it triggers |
|---|---|---|
| [`write-rebuttal`](skills/write-rebuttal/SKILL.md) | The **overall process**: two-audience mindset (reviewers *and* the Area Chair), itemize → brain-dump → draft → revise, 18 drafting tactics, the neutral-third-party test, rebuttal-experiment planning, plus an advisory lint script. | "Write my rebuttal", "respond to reviewers", "author response", planning rebuttal experiments. |
| [`nlp-rebuttal`](skills/nlp-rebuttal/SKILL.md) | The **per-concern playbook**: 28 recurring reviewer-concern scenarios (novelty, "simple combination", weak baselines, marginal gains, missing ablations, no significance, data leakage, no human eval, reproducibility, …), each with a bad-answer anti-pattern and a recommended answer template, routed by a concern table. | "The reviewer says…", "R2 complains…", drafting a reply to one specific review comment. |

**They compose:** `write-rebuttal` shapes the whole response (structure, ordering, tone, the note to the AC); `nlp-rebuttal` picks the strategy and template for each individual answer.

## Install

### Option A — as a Claude Code plugin

```
/plugin marketplace add yuangao-tum/rebuttal-skills
/plugin install rebuttal-skills@rebuttal-skills
```

### Option B — copy the skills directly

```bash
git clone https://github.com/yuangao-tum/rebuttal-skills.git
cp -r rebuttal-skills/skills/write-rebuttal rebuttal-skills/skills/nlp-rebuttal ~/.claude/skills/
```

(Or copy into `.claude/skills/` inside a project to scope them to that project.)

## Usage

Once installed, the skills trigger automatically when you work on a rebuttal, or invoke them explicitly:

- *"Here are my ICLR reviews — help me write the rebuttal"* → `write-rebuttal` drives the process end-to-end.
- *"R2 says our method is just a combination of existing techniques"* → `nlp-rebuttal` routes to the matching scenario (Tip 3) and adapts its template.
- Before posting, run the mechanical check:

```bash
python skills/write-rebuttal/scripts/lint_rebuttal.py rebuttal.md
```

It flags promise-language with no numbers ("we will add…"), unfilled placeholders, missing AC-facing summary, and pre-written outcomes — advisory only.

## What's inside

```
skills/
├── write-rebuttal/
│   ├── SKILL.md                          # process, 18 tactics summary, anti-patterns
│   ├── references/eighteen-tips.md       # all 18 tactics with examples + concern→tip map
│   ├── references/rebuttal-skeleton.md   # structure, micro-templates, AC dashboard tables, checklist
│   ├── assets/rebuttal-template.tex      # compilable LaTeX skeleton (colour-coded reviewers,
│   │                                     #   quote boxes, AC standing + coverage tables)
│   └── scripts/lint_rebuttal.py          # advisory rebuttal linter (stdlib only)
└── nlp-rebuttal/
    ├── SKILL.md                          # concern router (28 scenarios), cross-cutting rules
    ├── references/innovation-theory.md   # tips 1–7: novelty, motivation, theory, limitations
    ├── references/communication-writing.md # tips 8–12: related work, clarity, misunderstandings
    └── references/experiments-evidence.md  # tips 13–28: baselines, ablations, significance, …
```

## Credits

- `write-rebuttal` is distilled from Devi Parikh, Dhruv Batra & Stefan Lee, [*How we write rebuttals*](https://deviparikh.medium.com/how-we-write-rebuttals-dc84742fece1). All credit for the method goes to the original authors.
- `nlp-rebuttal` is translated and adapted from [MLNLP-World/Paper-Rebuttal-Tips](https://github.com/MLNLP-World/Paper-Rebuttal-Tips) (Chinese original). All credit for the scenario collection goes to the MLNLP community contributors. The upstream repository carries no explicit license; the adaptation here is shared with attribution for research/educational purposes and will be adjusted or removed at the upstream authors' request.

## License

This repository is released under the [MIT License](LICENSE).
