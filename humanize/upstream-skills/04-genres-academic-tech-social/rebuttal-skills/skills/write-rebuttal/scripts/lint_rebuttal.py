#!/usr/bin/env python3
"""Advisory linter for author-response rebuttals (Parikh-Batra-Lee method).

Flags the mechanical smells the method warns against. Judgment stays with the
author -- this only surfaces candidates.

Usage:
    python lint_rebuttal.py <rebuttal.tex | rebuttal.md>
"""
import re
import sys
from pathlib import Path

# Tip 13: "don't promise, do" -- promise language with no number nearby is a smell.
PROMISE_PATTERNS = [
    r"\bwe will (add|include|discuss|report|provide|incorporate|show|run)\b",
    r"\bin the (final|camera[- ]ready|revised) version\b",
    r"\bwe plan to\b",
    r"\bwill be added\b",
    r"\bwe intend to\b",
]
# Unfilled placeholders (LaTeX \NEW{}, \Rtodo{}, [INSERT], [\ldots], TODO, ...).
PLACEHOLDER_PATTERNS = [
    r"\\NEW\{",
    r"\\Rtodo\{",
    r"\[INSERT[:\]]",
    r"\[\\ldots\]",
    r"\bTODO\b", r"\bTBD\b", r"\bXXX\b", r"\bFIXME\b",
    r"_{3,}",
]
# Pre-committed outcomes: asserting a result that a placeholder shows isn't computed.
PRECOMMIT_HINTS = [
    r"\bis significant\b", r"\bsignificantly (increases|improves|outperforms|higher|lower)\b",
    r"\boutperforms\b", r"\bbeats\b",
]
# Tip-1 / AC-facing structure signals.
AC_SIGNALS = [r"area chair", r"\bAC\b", r"meta[- ]review", r"decision summary", r"\bRAC"]
THANK_SIGNALS = [r"\bthank", r"\bwe are grateful", r"\bappreciate"]
STAT_SIGNALS = [r"p\s*[=<>]", r"\bCI\b", r"confidence interval", r"effect size",
                r"\bp-value", r"±", r"\+/-", r"\bstd\b", r"\bseeds?\b", r"%\b"]


def scan(text, patterns, flags=re.I):
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        for p in patterns:
            if re.search(p, line, flags):
                hits.append((i, line.strip()[:110], p))
    return hits


def near_number(text, idx, window=160):
    seg = text[max(0, idx - window): idx + window]
    return bool(re.search(r"\d", seg))


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"! file not found: {path}")
        sys.exit(2)
    text = path.read_text(errors="ignore")
    low = text.lower()
    print(f"== Rebuttal lint: {path.name} ==\n")

    n_flags = 0

    # 1. Promise language (Tip 13)
    promises = scan(text, PROMISE_PATTERNS)
    # keep only promises NOT accompanied by a number on the same line
    weak = [(ln, s, p) for (ln, s, p) in promises if not re.search(r"\d", s)]
    if weak:
        n_flags += len(weak)
        print(f"[Tip 13] {len(weak)} promise(s) with no number on the line "
              f"-- 'don't promise, do':")
        for ln, s, _ in weak[:12]:
            print(f"    L{ln}: {s}")
        print()

    # 2. Unfilled placeholders
    ph = scan(text, PLACEHOLDER_PATTERNS)
    if ph:
        n_flags += len(ph)
        print(f"[Placeholders] {len(ph)} unfilled slot(s) -- fill with computed values "
              f"before posting:")
        for ln, s, _ in ph[:12]:
            print(f"    L{ln}: {s}")
        print()

    # 3. Pre-committed outcomes next to placeholders (Tips 13/15 overclaim risk)
    for m in re.finditer("|".join(PRECOMMIT_HINTS), text, re.I):
        seg = text[max(0, m.start() - 200): m.end() + 200]
        if re.search(r"\\NEW\{|\[INSERT", seg):
            n_flags += 1
            line_no = text[: m.start()].count("\n") + 1
            print(f"[Tip 13/15] L{line_no}: asserts an outcome "
                  f"('{m.group(0)}') next to an UNFILLED placeholder -- "
                  f"you may be pre-writing a result before running it.")
    if n_flags:
        print()

    # 4. AC-facing section present? (the beginner miss)
    if not any(re.search(p, low) for p in AC_SIGNALS):
        n_flags += 1
        print("[Structure] No area-chair / decision-summary section detected. "
              "The AC is the second audience -- add a decision-oriented close.\n")

    # 5. Opens with thanks? (Tip 1/17) -- skip a LaTeX preamble if present.
    body = text.split("\\begin{document}", 1)[-1]
    head = "\n".join(body.splitlines()[:40]).lower()
    if not any(re.search(p, head) for p in THANK_SIGNALS):
        print("[Tip 1/17] No 'thanks / positive summary' near the top -- start positive.\n")

    # 6. Any statistics at all? (Tip 12)
    if not any(re.search(p, text, re.I) for p in STAT_SIGNALS):
        print("[Tip 12] No statistics detected (p / CI / effect size / % / seeds). "
              "Disagreements land harder with numbers than adjectives.\n")

    print(f"-- {n_flags} mechanical flag(s). Advisory only; author's judgment decides. --")


if __name__ == "__main__":
    main()
