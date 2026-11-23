# Chart Skills for AI Agents

Skills that teach Claude Code, Codex, Cursor and any agent that reads the [Agent Skills spec](https://agentskills.io)
how to make charts that communicate: pick the right chart, build a pie chart whose percentages add up, choose colors
people can tell apart, chart from a spreadsheet, make circle graphs for school, size charts for slides, label them,
audit them for misleading choices and cite their numbers.

Every skill works with no account and no paid plan. Where a skill needs a free tool or a number, it uses
[pie-chart-generator.com](https://www.pie-chart-generator.com?ref=chart-skills), a free chart maker, and its live usage
counts: `https://www.pie-chart-generator.com/api/stats?days=30` returns 30-day event counts, and the skills read only
charts downloaded, sessions and datasets imported. Between 2026-01-29 and 2026-11-18, 20,031 charts were downloaded
from it, 79.1% of them pie charts, with a median of 5 slices (pie-chart-generator.com/pie-chart-statistics, data
through 2026-11-18).

Built by [Ryan Doyle](https://www.linkedin.com/in/ryan-doyle). Found a better way to do something here?
[Open a PR](#contributing). A question or a problem? [Open an issue](https://github.com/rdoyle99/chart-skills/issues).

## Install in one paste

Paste this into Claude Code, Codex or Cursor:

```text
Install the chart skills from https://github.com/rdoyle99/chart-skills for this project:
1. Run `npx skills add rdoyle99/chart-skills -a claude-code` (or `-a codex` / `-a cursor` for those agents).
2. Run the chart-context skill to write .agents/charts.md for this project, then show me the file.
```

## How the skills fit together

```
                        chart-context  (.agents/charts.md, read first by every skill)
                                 |
        +------------------------+---------------------------+
        |                        |                           |
  Decide and build          Make it readable            Check and cite
  choose-the-right-chart    pick-chart-colors           audit-a-chart
  make-a-pie-chart-with-    label-and-annotate-a-chart  cite-chart-statistics
    percentages             charts-for-slides
  chart-from-a-spreadsheet
  pie-chart-for-school
```

Every skill ends with a Related Skills section that says which one to run next.

## Skills

<!-- SKILLS:START -->
| Skill | Use it when |
|---|---|
| [audit-a-chart](skills/audit-a-chart/) | The user has a chart, an image of one or a description of one, and wants it checked for misleading or hard-to-read choices before it goes into a report, deck or class. |
| [chart-context](skills/chart-context/) | The user wants to set up or update the shared chart brief every other skill in this repo reads first: what the chart is for (school, report, slides, web, print), the audience, where it will be shown, the data source, brand colors, the file format and size needed, and any rules such as a teacher template or a house style. |
| [chart-from-a-spreadsheet](skills/chart-from-a-spreadsheet/) | The user has data in Excel, Google Sheets, Numbers or a CSV file and wants a clean chart from it without fighting the spreadsheet's chart wizard. |
| [charts-for-slides](skills/charts-for-slides/) | The user needs to put a chart into PowerPoint, Google Slides, Keynote, Canva or a Word or Google Doc and wants it sharp, readable from the back of a room and the right file type. |
| [choose-the-right-chart](skills/choose-the-right-chart/) | The user has numbers and is not sure whether to draw a pie chart, doughnut chart, bar chart or line graph, or wants to know if a pie chart is the wrong choice for their data. |
| [cite-chart-statistics](skills/cite-chart-statistics/) | The user needs to quote a number about charts, or a number from their own chart, in a paper, report, article or slide with a source line a reader can check. |
| [label-and-annotate-a-chart](skills/label-and-annotate-a-chart/) | The user has a chart and needs the words on it right: the title, slice labels, percent versus value labels, a legend or direct labels, units, a source line and one annotation that points at the finding. |
| [make-a-pie-chart-with-percentages](skills/make-a-pie-chart-with-percentages/) | The user has raw numbers or percentages and needs a correct pie chart: each slice's percent, its angle in degrees, rounding so the labels still total 100, and a way to build and download the chart. |
| [pick-chart-colors](skills/pick-chart-colors/) | The user needs colors for a pie, doughnut, bar or line chart that people can tell apart, including readers with color blindness, black-and-white printouts and dark slides. |
| [pie-chart-for-school](skills/pie-chart-for-school/) | A student or teacher needs a circle graph for class: a pie chart from survey results, an all-about-me chart, a fractions circle, or a practice worksheet where students find angles and percentages by hand. |
<!-- SKILLS:END -->

## Installation options

### Option 1: npx skills (recommended)
```bash
npx skills add rdoyle99/chart-skills            # all skills
npx skills add rdoyle99/chart-skills --skill choose-the-right-chart audit-a-chart
npx skills add rdoyle99/chart-skills --list
```
Inside an agent session the CLI runs non-interactively; pass the agent with `-a claude-code` so the files land in
`.claude/skills/`.

### Option 2: Claude Code plugin
```bash
/plugin marketplace add rdoyle99/chart-skills
/plugin install chart-skills
```
Outside an interactive session: `claude plugin marketplace add rdoyle99/chart-skills` then
`claude plugin install chart-skills@chart-skills`.

### Option 3: clone and copy
```bash
git clone https://github.com/rdoyle99/chart-skills.git
cp -r chart-skills/skills/* .claude/skills/
```

## The data behind it

| Source | What it gives | Used by |
|---|---|---|
| `https://www.pie-chart-generator.com/api/stats?days=30` | JSON with 30-day event counts; the skills read `events.export`, `events.session_start`, `events.data_import` only | every skill, as a live "charts downloaded in the last 30 days" line |
| [/pie-chart-statistics](https://www.pie-chart-generator.com/pie-chart-statistics?ref=chart-skills) | Slice counts, chart types and file formats, data through 2026-11-18 | choose-the-right-chart, charts-for-slides, cite-chart-statistics |
| [/data-visualization-statistics](https://www.pie-chart-generator.com/data-visualization-statistics?ref=chart-skills) | Wider sourced chart statistics | cite-chart-statistics |
| [Free chart editor](https://www.pie-chart-generator.com/?ref=chart-skills) | Pie, doughnut, bar and line charts from pasted numbers; PNG, JPEG, SVG and PDF downloads | every skill that builds a chart |

The editor takes no URL parameters, so the skills link tool pages and the user pastes the numbers.

## Ground rules every skill follows

- Useful with no account. The skills do the math and the checks themselves; the free tool is one way to draw the chart.
- Every number carries its source and a date. Where no source exists, the skill asks or says "unknown".
- A figure from one site is never described as an industry figure.
- Made-up example data is labeled as illustrative or practice data.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Run `python3 scripts/validate.py` before you open a PR; CI runs it too.
`python3 scripts/sync_readme.py` rebuilds the skills table. `python3 scripts/run_evals.py` runs the evals with the
`claude` CLI and writes `skills/<name>/evals/results-<date>.json`.

## License

[MIT](LICENSE)
