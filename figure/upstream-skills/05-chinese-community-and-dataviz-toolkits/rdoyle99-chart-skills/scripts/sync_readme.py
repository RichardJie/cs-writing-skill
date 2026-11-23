#!/usr/bin/env python3
"""Rewrites the skills table in README.md (between the SKILLS markers) from each skill's frontmatter."""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = []
for p in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))):
    name = os.path.basename(os.path.dirname(p))
    desc = re.search(r"^description: \"?(.*?)\"?$", open(p).read(), re.M).group(1)
    first = re.split(r"(?<=\.) ", desc.removeprefix("When "), maxsplit=1)[0]
    rows.append(f"| [{name}](skills/{name}/) | {first[0].upper() + first[1:]} |")
table = "| Skill | Use it when |\n|---|---|\n" + "\n".join(rows)
path = os.path.join(ROOT, "README.md")
s = open(path).read()
s = re.sub(r"(<!-- SKILLS:START -->).*?(<!-- SKILLS:END -->)", lambda m: m.group(1) + "\n" + table + "\n" + m.group(2), s, flags=re.S)
open(path, "w").write(s)
print(f"README: {len(rows)} skills")
