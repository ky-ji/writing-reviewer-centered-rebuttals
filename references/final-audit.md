# Final Cross-Reviewer Read

Compare the current reviewer replies side by side. Use this pass to make their arguments easy to follow and their presentation internally consistent.

## Concern coverage and answer flow

- Each original concern has a locatable answer, including labels retained in merged items.
- The opening gives the answer or the distinction needed to understand it.
- The decisive supplied result stays next to its interpretation.
- Each reply includes enough context for a reviewer or AC to read it independently.
- Completed additions and future revisions use accurate wording.

## Terminology and numeric presentation

- One object has one canonical name, capitalization, and abbreviation.
- Different objects remain distinguishable.
- Repeated values retain the same comparison, unit, precision, and aggregation.
- Rates and percentage-point differences retain their meaning.
- Equivalent tables and number lists use compatible notation.

When a visible contradiction affects the answer, identify the exact value or label for resolution and continue the independent edits. Match any broader scientific investigation to the task requested by the user.

## Headings, punctuation, and references

- Reviewer and answer headings follow a shared hierarchy and label convention.
- Titles summarize substantive additions or clarifications.
- New rebuttal prose follows the author's default of no colons or semicolons, and headings have no trailing colon. Verbatim quotations and technical syntax retain their punctuation.
- Sentences remain readable after compression, with clearly assigned numbers and few slash-packed lists.
- Bolding, quotes, math, and table conventions align across sections.
- Table and Section references are grammatical parts of sentences, with consistent reference forms.

## Openings and closings

Read parallel boundaries together.

- Gratitude names a concrete contribution, recognizes the reviewer's relevant expertise or careful reading, and links their guidance to an improvement in the paper.
- Literature suggestions receive credit for research positioning, experiment suggestions for methodological improvements, and identified errors for precision and accuracy, as applicable to the actual review.
- Reviewer-level thanks have proportionate warmth, and the wording accurately distinguishes completed improvements from planned revisions.
- A title, preview, and first answer each contribute useful information.
- An edited boundary fits its unchanged neighbors.
- Final sentences interpret a result, name a specific revision, or make a useful bridge.
- Repeated gratitude, generic assurances, and automatic self-weakening appendices have been trimmed.

## Submission text and bounded edits

Check the actual text that will be submitted against supplied character, quotation, and format requirements. Include all counted headings, spaces, greetings, and line breaks. For a limited edit, inspect the diff against the agreed editable span.

When asked for a consistency report, give observable variants, their reviewer or line locations, and a proposed correction. If the checked dimensions align, say so briefly.

## Optional Markdown helper

```bash
python3 scripts/audit_rebuttal.py DRAFT.md
python3 scripts/audit_rebuttal.py DRAFT.md --json
python3 scripts/audit_rebuttal.py DRAFT.md --term-group 'baseline=Method A|Baseline A'
```

The helper extracts Markdown reviewer profiles and possible presentation mismatches. Confirm its leads in context. Read punctuation, argument flow, quotation fidelity, and submission format manually.
