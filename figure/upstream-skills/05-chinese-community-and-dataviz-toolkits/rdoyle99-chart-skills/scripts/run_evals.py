#!/usr/bin/env python3
"""Runs each skill's evals through a headless agent and grades every assertion with a second call.

Usage: run_evals.py [skill ...] [--model sonnet]
Needs the `claude` CLI signed in. Per case: one call answers the prompt with SKILL.md and references/ loaded, one call
grades the answer against the assertions and returns JSON. Writes skills/<name>/evals/results-<YYYY-MM-DD>.json with
pass_rate and each case's verdicts. The test agent gets WebFetch, so it can read the live stats API; files it
would write are shown inline.
"""
import argparse
import datetime as dt
import glob
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




def claude(prompt, model, tools=False):
    cmd = ["claude", "-p", "--model", model, "--output-format", "text"]
    if tools:  # the test agent can fetch the live stats API, as a user's agent could
        cmd += ["--allowedTools", "WebFetch"]
    out = subprocess.run(cmd, input=prompt,
                         capture_output=True, text=True, timeout=600)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip()[:300])
    return out.stdout.strip()


def skill_bundle(name):
    d = os.path.join(ROOT, "skills", name)
    parts = [open(os.path.join(d, "SKILL.md")).read()]
    for p in sorted(glob.glob(os.path.join(d, "references", "*.md"))):
        parts.append(f"\n\n--- references/{os.path.basename(p)} ---\n" + open(p).read())
    return "".join(parts)


def run(name, model):
    ev = json.load(open(os.path.join(ROOT, "skills", name, "evals", "evals.json")))
    bundle = skill_bundle(name)
    cases, passed, total = [], 0, 0
    for e in ev["evals"]:
        answer = claude(
            "You are an AI agent with this skill loaded:\n\n" + bundle +
            "\n\n---\nThe stats API tools are live; call them when the skill says to. There is no project "
            "folder, so where the skill says to read or write a file, show the file's contents in your answer instead. "
            "Do the whole task now, don't describe what you would do.\n\nUser: " + e["prompt"], model, tools=True)
        grade = claude(
            "Grade this agent answer. For each assertion return pass true/false and a one-line reason. A stated tool "
            "call counts as a call. Reply with JSON only: {\"verdicts\": [{\"assertion\": str, \"pass\": bool, "
            "\"reason\": str}]}\n\nExpected: " + e.get("expected_output", "") + "\n\nAssertions:\n" +
            "\n".join("- " + a for a in e["assertions"]) + "\n\nAnswer:\n" + answer, model)
        m = re.search(r"\{.*\}", grade, re.S)
        verdicts = json.loads(m.group(0))["verdicts"] if m else []
        ok = sum(1 for v in verdicts if v.get("pass"))
        passed += ok
        total += len(e["assertions"])
        cases.append({"id": e["id"], "passed": ok, "of": len(e["assertions"]), "verdicts": verdicts,
                      "answer_chars": len(answer)})
        print(f"  {name} #{e['id']}: {ok}/{len(e['assertions'])}")
    res = {"skill": name, "date": dt.date.today().isoformat(), "model": model,
           "pass_rate": round(passed / total, 3) if total else 0, "cases": cases}
    out = os.path.join(ROOT, "skills", name, "evals", f"results-{res['date']}.json")
    json.dump(res, open(out, "w"), indent=1)
    return res


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("skills", nargs="*")
    p.add_argument("--model", default="sonnet")
    a = p.parse_args()
    names = a.skills or sorted(os.path.basename(os.path.dirname(x)) for x in glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md")))
    for n in names:
        try:
            r = run(n, a.model)
            print(f"{n}: pass_rate {r['pass_rate']}")
        except Exception as e:  # noqa: BLE001  one skill's failure shouldn't stop the rest; it is printed
            print(f"{n}: ERROR {e}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
