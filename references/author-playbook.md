# Author Playbook: Reviewer-Centered Rebuttals

## Contents

1. Choose the editing mode
2. Map reviewer concerns
3. Build answer units
4. Shape reviewer-level openings
5. Shape answer openings and closings
6. State revisions concretely
7. Compress without flattening
8. Harmonize across reviewers
9. Write AC/meta-review summaries
10. Make bounded micro-edits

## 1. Choose the editing mode

Name the task before editing:

- **Draft:** turn reviewer concerns and supplied material into responses.
- **Restructure:** preserve substance while changing order and hierarchy.
- **Compress:** retain coverage and decisive content within a tighter budget.
- **Micro-edit:** change only specified sentences or boundaries.
- **Consistency pass:** compare reviewer sections without reopening their scientific content.

Treat the user's designated draft as authoritative. During a writing or consistency pass, do not independently reopen paper claims, experiment protocols, seeds, confidence intervals, null results, or limitations. Do that only when the user explicitly requests scientific verification.

Before editing, record:

- files and sections that may change;
- language and formatting convention;
- whether reviewer quotations are fixed;
- whether the work is prose-only or includes scientific verification.

## 2. Map reviewer concerns

Split each review into atomic concerns. A useful private map has four columns:

| Reviewer concern | Direct answer | Supplied support | Revision, if any |
|---|---|---|---|
| What blocks the reviewer? | What should they know first? | Which result or clarification answers it? | What exactly changes in the manuscript? |

Keep weakness-before-question order when the draft already uses `W/Q/A`. Merge two items only when one answer truly resolves both and both concern labels remain easy to locate.

Prioritize by likely decision impact:

1. central novelty or validity concern;
2. missing comparison or requested analysis;
3. ambiguity that changes interpretation;
4. presentation or wording issue.

This ranking controls space, not truth. The most important concern gets the clearest direct answer and the most visible result.

## 3. Build answer units

A full answer unit can contain:

1. a plain-language heading;
2. the reviewer excerpt;
3. a direct answer;
4. one sentence of purpose or context;
5. the decisive supplied result;
6. the implication for this concern;
7. a specific manuscript revision.

Use only the pieces that help. A compact response may need just answer → result → implication.

Prefer this information order:

> **Answer first.** What changed or what the authors conclude.
>
> **Result next.** The number, comparison, or clarification that carries the answer.
>
> **Meaning last.** Why that result addresses this reviewer concern.

Avoid beginning with experimental plumbing when the conclusion can orient the reader first. Explain task, baseline, metric, or perturbation in ordinary language before internal names.

Preserve the user's chosen strength of claim. Editing should clarify a conclusion, not automatically replace `demonstrates` with `suggests`, insert unsolicited qualifications, or add a limitation paragraph.

## 4. Shape reviewer-level openings

The reviewer-level opening should do two jobs:

- thank the reviewer in a way connected to their actual focus;
- preview the one or two themes that organize the response.

Keep openings proportionate across reviewers. One reviewer should not receive four stacked gratitude phrases while another gets a bare `Thank you` unless the user intentionally wants that contrast.

A useful pattern is:

> We thank the reviewer for highlighting **[specific theme]**. Below we clarify **[issue 1]** and report **[issue 2/result]**.

Do not copy the same concern inventory into the first answer. The reviewer-level opening frames the section; the answer opening resolves its local concern.

## 5. Shape answer openings and closings

### Openings

Give adjacent answers different rhetorical jobs:

- direct conclusion;
- clarification of a misunderstanding;
- newly added comparison;
- explanation of design intent;
- acknowledgment of a requested revision.

Variation should come from function, not decorative synonym swaps. Read all first sentences side by side.

### Closings

Choose one closing job:

- interpret the decisive result;
- connect the answer to the reviewer's concern;
- state the exact manuscript revision;
- bridge to a separate answer when necessary.

Not every answer needs a revision promise. If five answers all end with `We will...`, retain that form only where a real manuscript change is the main takeaway. Let the others end on meaning.

Read closing sentences side by side. Check both repeated wording and repeated function.

## 6. State revisions concretely

A useful revision sentence names an object and an action:

- `We will add this comparison to Table 3.`
- `We will define the evaluation perturbations at the start of Sec. 4.2.`
- `We will replace “X” with “Y” throughout the method section.`

Avoid empty closures such as `We will revise accordingly.` If the location is not supplied, name the manuscript object without inventing a section number.

Revision commitments belong where they answer the concern. Do not append one mechanically to every response.

## 7. Compress without flattening

Compress in this order:

1. duplicate thanks;
2. repeated restatements of the concern;
3. setup already explained in the same answer;
4. transitions with no new job;
5. secondary detail that does not carry the conclusion.

Protect:

- one locatable response per concern;
- the direct answer;
- the decisive supplied result;
- the concern-specific implication;
- concrete revision language when promised.

Do not make every reviewer section sound identical. Consistency means shared conventions, not erased reviewer specificity.

## 8. Harmonize across reviewers

Make a short canonicalization sheet before the final pass:

| Category | Canonical form | Variants to replace or distinguish |
|---|---|---|
| Method/baseline | `Official GR00T-N1.6` | `Official`, `official checkpoint` |
| Supervision target | chosen project term | `pseudo-label`, `mined target`, `RVM target` |
| Difference unit | `percentage points` or `pp` | `%`, `points`, `pp` used for the same difference |
| Figure reference | `Fig.` or `Figure` | mixed forms |
| Answer label | one bolding convention | label-only versus whole-sentence bolding |

Use the actual project terms; the table above illustrates the method, not mandatory wording.

Compare reviewer sections along six axes:

1. **Terminology:** same object, same name.
2. **Numbers:** same value, same unit and precision.
3. **Structure:** compatible W/Q/A order, heading depth, separators, tables, and quote style.
4. **Openings:** comparable length, specificity, and warmth.
5. **Closings:** balanced use of implication versus revision promises.
6. **References:** consistent reviewer IDs, answer IDs, figure/table style, and manuscript object names.

If variants represent genuinely different objects, add a one-time distinction rather than forcing one label.

## 9. Write AC/meta-review summaries

Use a neutral title such as `Response to the Meta-Review`. Organize the response by the meta-review's stated concerns, not by a chronological recap of the author process.

For each concern, give:

1. the conclusion;
2. one headline supplied result or clarification;
3. the detailed reviewer-answer location when available.

The AC response should be a compact map to the substantive replies. Keep its terminology, numbers, and answer references aligned with the reviewer sections.

## 10. Make bounded micro-edits

For opening- or closing-only requests:

1. mark the exact editable sentences;
2. keep the body fixed;
3. assign each new sentence one rhetorical job;
4. compare it with the fixed sentence immediately before and after it;
5. read the same boundary across all reviewer sections;
6. inspect the diff to ensure nothing else changed.

Common boundary problems:

- the new opening repeats the next sentence's setup;
- the new closing repeats the previous result;
- reviewer-level thanks and the first answer use the same gratitude phrase;
- every final sentence promises a revision;
- one reviewer's opening is much warmer or longer than the others;
- a local edit introduces a new alias for an existing method or metric.

Fix the smallest span that removes the echo. Do not rewrite the entire answer when a one-sentence adjustment is enough.
