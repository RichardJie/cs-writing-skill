#!/usr/bin/env python3
"""Checks every skill the way CI does: frontmatter, references/, evals/, Related Skills, dated numbers, the README table
and the plugin manifests. Prints one line per problem and exits 1 if there are any. Standard library only."""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANNED = [r"\bhonestly\b", r"\bdelve\b", r"\bgame[- ]changer\b", r"\bin today's\b", r"\bnot just [\w ]{1,30},? but\b",
          r"\bisn't (?:just )?[\w ]{1,30}[,;] it's\b", r"\bhonest\b", r"\btransparent\b", r"\bunbiased\b", r"\bseamless",
          r"\bsupercharge", r"\brevolutioni[sz]e", r"world's leading", r"#1\b", "\u2014", r"\bleverage", r"\brobust", r"\belevate", r"\bunlock", r"\btransparent"]
problems = []


def bad(where, what):
    problems.append(f"{where}: {what}")


skills = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md")))
readme = open(os.path.join(ROOT, "README.md")).read()
for name in skills:
    d = os.path.join(ROOT, "skills", name)
    t = open(os.path.join(d, "SKILL.md")).read()
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    fm = m.group(1) if m else ""
    if not re.search(r"^name: %s$" % re.escape(name), fm, re.M):
        bad(name, "frontmatter name must equal the folder name")
    desc = re.search(r"^description: (.*)$", fm, re.M)
    if not desc or len(desc.group(1)) < 250:
        bad(name, "description under 250 characters")
    elif len(re.findall(r"(?<!\w)'[^']{3,60}'(?!\w)|\"[^\"]{3,60}\"", desc.group(1))) < 5:
        bad(name, "description needs 5+ quoted trigger phrases")
    if "version:" not in fm:
        bad(name, "metadata.version missing")
    if not glob.glob(os.path.join(d, "references", "*.md")):
        bad(name, "no references/*.md")
    try:
        ev = json.load(open(os.path.join(d, "evals", "evals.json")))
        if len(ev.get("evals", [])) < 2 or any(len(e.get("assertions", [])) < 3 for e in ev["evals"]):
            bad(name, "evals need 2+ cases with 3+ assertions each")
    except (OSError, ValueError) as e:
        bad(name, f"evals/evals.json: {e}")
    sec = t.split("## Related Skills", 1)[1] if "## Related Skills" in t else ""
    if sum(1 for o in skills if o != name and re.search(r"\b%s\b" % re.escape(o), sec)) < 2:
        bad(name, "Related Skills must name 2+ sibling skills")
    files = [t] + [open(p).read() for p in glob.glob(os.path.join(d, "references", "*.md"))]
    if any(re.search(r"\d+(?:\.\d+)?%|\$\d", f) for f in files) and not re.search(r"20\d\d-\d\d", "".join(files)):
        bad(name, "numbers without a YYYY-MM date")
    for b in BANNED:
        hit = re.search(b, "".join(files).lower())
        if hit:
            bad(name, f"AI-tell phrase: {hit.group(0)}")
    if "pie-chart-generator.com/api/stats" not in t:
        bad(name, "Data section must name https://www.pie-chart-generator.com/api/stats")
    if f"skills/{name}/" not in readme:
        bad("README.md", f"{name} not in the skills table")
for f in ("plugin.json", "marketplace.json"):
    try:
        json.load(open(os.path.join(ROOT, ".claude-plugin", f)))
    except (OSError, ValueError) as e:
        bad(f".claude-plugin/{f}", str(e))
print("\n".join(problems) or f"ok: {len(skills)} skills")
sys.exit(1 if problems else 0)
