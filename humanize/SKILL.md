---
name: humanize
description: "Remove AI voice from prose. Invoke with :chinese for 去AI味/中文重构 (7-step surgery, Chinese patterns) or :english for humanize/English rewrite (pattern catalog, direct-statement rules, em-dash ban). Triggers: 去AI味, humanize, remove AI tells, make it sound natural, 让文字更像人写的."
---

# Humanize — Remove AI Voice

One installable skill, two language tracks. **Read the matching file in full before rewriting.**

| Invocation | Read | Use when |
|------------|------|----------|
| `:chinese` or Chinese input / 去AI味 | [chinese.md](chinese.md) | Chinese prose, WeChat posts, CN blogs, 中文论文润色（非 cs-writing 边界） |
| `:english` or English input / humanize | [english.md](english.md) | English prose, READMEs, essays, LinkedIn, technical docs |

## Router

1. **Explicit tag wins.** `:chinese` → `chinese.md`; `:english` → `english.md`.
2. **No tag:** infer from the text language. Mixed or unclear → ask once, default `:english`.
3. **Embedded mode** (another task calls humanize as a step): run the loop internally; output only the final rewrite unless the user asked for diagnosis.

## Shared guardrails (both tracks)

- **Preserve facts.** No new names, numbers, dates, quotes, or citations. Opinions and stance are voice, not facts.
- **Preserve information, not shape.** Compress dull parts; vary paragraph length; merge or split freely. Information beats mirroring structure.
- **Flag clusters, not isolated tells.** One em dash or one "crucial" is human; stacks of tells are not.
- **Do not rewrite** quoted speech, titles, code, frontmatter, or examples *about* AI patterns.
- **Voice calibration:** if the user supplies a writing sample, match its habits (including punctuation) over these rules.
- **Register match:** encyclopedic, legal, and reference text stay neutral; blog/opinion pieces get personality when appropriate.
- **Do not over-edit.** Specific, messy, dated human detail → leave it alone.

## Output modes

| Mode | Deliver |
|------|---------|
| **Pasted text (default)** | Brief diagnosis bullets → final rewrite → short change summary |
| **File** | Rewrite in place; leave code blocks and frontmatter untouched; summarize changes in chat |
| **Embedded** | Final text only |

## Examples

**`:chinese`** — Input: "综上所述，人工智能为各行各业带来前所未有的机遇和挑战。"  
→ Apply [chinese.md](chinese.md) 7-step surgery; cut 综上所述/机遇挑战; add concrete scene.

**`:english`** — Input: "Additionally, this pivotal initiative underscores our commitment to fostering innovation in today's evolving landscape."  
→ Apply [english.md](english.md); kill AI vocabulary; ban em dashes; state what the initiative *is*.

## Related skills

- **`cs-writing`** — CS paper *narrative boundaries* (press-conference principle, no self-undermining). Does not strip AI voice; pair with `:english` or `:chinese` on finished prose.
- **`plain`** — Explain hard ideas clearly; orthogonal to de-slopping.
