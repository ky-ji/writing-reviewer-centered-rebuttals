---
name: writing-reviewer-centered-rebuttals
description: Draft, restructure, compress, and polish academic rebuttals, reviewer replies, and AC responses. Use for concern-specific arguments, direct answers, readable prose, and consistency across reviewers, including bounded opening or closing edits.
---

# Writing Reviewer-Centered Rebuttals

Help the reviewer and a neutral AC understand the concern, the answer, and why the supplied evidence resolves it without rereading the paper. Make the contribution easy to assess through clear reasoning and concrete results.

## Writing approach

- Start from the user's current draft, supplied evidence, requested language, template, and edit boundary. Keep results, comparison identities, units, quotations, and completed versus planned work accurate. Resolve a material source conflict locally or ask a focused question while continuing unaffected writing.
- Lead with the substantive answer. Follow with the mechanism or distinction needed to understand it, the decisive result, and its meaning for this concern. Choose the pieces and order that make the argument clearest.
- Write with calm confidence. Explain what the method achieves and how the evidence answers the question. Acknowledge a concrete correction directly. Include qualifications when they change the answer, and keep the author's supported persuasive strength.
- Use complete, connected sentences. As this author's default, avoid colons and semicolons in newly written rebuttal prose and trailing colons in headings. Split the thought or connect it with an ordinary conjunction. Preserve verbatim reviewer quotations and technical syntax.
- Keep each reviewer reply independently understandable. Repeat a decisive fact when another reviewer needs it, using the same name, value, unit, and interpretation.

## Workflow

1. Read [references/author-playbook.md](references/author-playbook.md) for argument design, concern mapping, compression, and AC responses. For local prose, punctuation, headings, or boundary edits, read [references/micro-style-patterns.md](references/micro-style-patterns.md).
2. Identify the underlying question behind each review item. Map it to a direct answer, the strongest relevant supplied support, and any concrete manuscript change. Allocate space by decision impact and preserve locatable concern labels.
3. Draft answer-first paragraphs. State the main distinction before method names or implementation details. Keep result and interpretation adjacent. Distinguish completed additions from future revisions.
4. Make gratitude specific and brief. Recognize the reviewer's relevant expertise, judgement, or careful reading and connect their guidance to a concrete improvement in the paper. Treat them as an expert contributor to the revision. Make a response title summarize substantive additions or clarifications. Let individual answers end on their meaning or a useful revision, with varied sentence functions.
5. Compress repeated setup, courtesy, and empty transitions before cutting evidence. Prefer readable sentences over slash-packed names, number strings, or undefined abbreviations. For a bounded edit, compare the changed sentence with both fixed neighbors and inspect the diff.
6. Read reviewer sections side by side using [references/final-audit.md](references/final-audit.md). Align terminology, numbers, concern labels, formatting, openings, and closing rhythm. Check the actual submitted text against any supplied character or format limit.

The optional helper finds presentation patterns in Markdown reviewer sections.

```bash
python3 scripts/audit_rebuttal.py DRAFT.md
```

Use its observations to guide a manual read. Match any broader scientific review or experiment work to the user's requested task.
