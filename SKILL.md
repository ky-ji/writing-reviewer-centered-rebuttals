---
name: writing-reviewer-centered-rebuttals
description: Use when triaging, drafting, restructuring, compressing, micro-editing, or harmonizing academic rebuttals, author responses, reviewer replies, or AC/meta-review comments—especially when responses are generic, repetitive, poorly mapped to reviewer concerns, or inconsistent across reviewers in terminology, numbers, headings, openings, or closings.
---

# Writing Reviewer-Centered Rebuttals

Write for a reviewer who needs to recover the concern, see the answer, and understand why it matters without rereading the paper.

## Core contract

- Follow the user's authoritative draft, source set, version, template, language, and edit boundary literally. Never invent results, settings, citations, reviewer intent, locations, or completed work.
- Treat supplied claims and results as authoritative for writing work. Do not initiate paper/log/protocol verification, add caveats, or weaken conclusions unless the user explicitly asks for scientific validation or claim calibration.
- When reviewer text is quoted, keep it verbatim unless the user asks for paraphrase.
- Preserve the user's intended persuasive strength while making the reasoning easier to follow.

## Workflow

1. Read [references/author-playbook.md](references/author-playbook.md). For openings, closings, transitions, or sentence-level edits, also read [references/micro-style-patterns.md](references/micro-style-patterns.md). Lock the requested mode and mutation scope.
2. Split each review into atomic concerns. For each concern, identify the direct answer, best supplied result or clarification, implication, and any promised manuscript change.
3. Draft each unit as needed: plain heading → reviewer quote → direct answer → brief context → decisive result → concern-specific implication → concrete revision. Do not force every component when a shorter answer is clearer.
4. Make openings reviewer-specific but proportionate. Vary answer openings by rhetorical job rather than swapping synonyms. End on the result's meaning or a specific revision; avoid mechanical chains of identical `We will...` closings.
5. Read all reviewer sections side by side. Normalize canonical names, metric labels, units, percentage-versus-point notation, headings, answer-label styling, quote format, opening warmth, and closing rhythm. If two terms denote different objects, distinguish them once instead of flattening them.
6. Compress after coverage is stable. Remove repeated setup, duplicated concern summaries, and empty transitions before removing reviewer-specific evidence.
7. For a limited micro-edit, compare every new opening or closing with its fixed neighboring sentence so the edit does not echo information already present.

## Consistency check

When the draft contains multiple reviewer sections, read [references/final-audit.md](references/final-audit.md) and optionally run:

```bash
python3 scripts/audit_rebuttal.py DRAFT.md
```

The check is advisory and limited to cross-review consistency. It does not determine scientific correctness, evidence strength, protocol validity, quote fidelity, venue compliance, or submission readiness. Perform any broader audit only when the user requests it.
