# Cross-Reviewer Consistency Check

This is a narrow comparison pass across reviewer sections. It is not a scientific, evidentiary, venue, quote-fidelity, or submission-readiness audit.

## Scope

- Use the current rebuttal draft as the authoritative text.
- Compare reviewer sections with one another.
- Do not open the paper, raw reviews, experiment logs, code, or venue rules unless the user explicitly asks.
- Do not reassess claim strength, protocols, seeds, uncertainty, negative results, limitations, or whether evidence is sufficient.
- Do not add caveats or soften strong conclusions merely because they sound assertive.

## 1. Terminology

Read the reviewer sections side by side and flag only cross-section mismatches:

- one method, baseline, dataset, target, metric, perturbation, or aggregation has multiple names;
- capitalization or hyphenation changes for the same term;
- an acronym is expanded differently;
- a local edit introduces a new alias.

If two labels intentionally denote different objects, preserve both and add a one-time distinction if needed.

## 2. Numbers and units

Check repeated values only for presentation consistency:

- same value uses the same unit and precision;
- success rates consistently include or omit `%` in equivalent tables;
- changes are consistently labeled `%`, `percentage points`, `points`, or `pp`;
- plus/minus signs, decimals, and ranges follow one convention.

Do not recompute results or judge the underlying statistics.

## 3. Structure and formatting

Compare:

- reviewer-level heading depth;
- W/Q/A order and numbering;
- blockquote, bolding, separator, table, and math style;
- figure, table, section, reviewer, and answer references;
- answer-first formatting, including whether only `A1` or the whole first sentence is bold.

The goal is a shared visual grammar, not identical response lengths.

## 4. Openings

Place all reviewer-level openings together, then all answer openings together.

Check:

- comparable warmth and gratitude density across reviewers;
- reviewer-specific focus rather than copied generic praise;
- no opening repeats the fixed sentence immediately after it;
- adjacent answers vary by rhetorical job, not just synonyms.

Do not standardize away useful reviewer specificity.

## 5. Closings

Place all answer-final sentences together.

Check:

- one reviewer does not end every answer with `We will...` while others end on implications;
- repeated revision closings name specific actions when retained;
- a closing does not restate the result immediately before it;
- comparable answers use compatible reference and revision conventions.

There is no required limitation sentence and no required caveat.

## 6. Output

Report only observable cross-review inconsistencies. For each item, state:

1. the two or more variants;
2. their reviewer sections or line locations;
3. one proposed canonical form or a note that the distinction should be defined.

Avoid general quality scores, risk labels, readiness verdicts, or evidence judgments. If no inconsistency is found, say that the checked dimensions are internally aligned; do not infer broader correctness.

Optional helper:

```bash
python3 scripts/audit_rebuttal.py DRAFT.md
python3 scripts/audit_rebuttal.py DRAFT.md --json
```

Treat its output as leads for a side-by-side read, not as a gate.
