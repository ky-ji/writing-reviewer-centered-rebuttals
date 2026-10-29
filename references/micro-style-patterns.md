# Micro-Style Patterns for Rebuttal Prose

Examples below are schematic. Use the actual supplied facts and the user's current template.

## 1. Punctuation and readable sentences

As this author's default, write new rebuttal prose without colons or semicolons, including trailing colons in headings. Preserve reviewer quotations verbatim and keep punctuation required by technical syntax. Use periods for separate claims and ordinary conjunctions for closely related ideas. Treat this as a writing convention, with the current user's explicit instructions taking precedence.

| Dense wording | Readable revision |
|---|---|
| The components have different roles: A predicts; B acts. | The components have different roles. A predicts the future observation, and B uses it to choose actions. |
| W1. Added control: | W1. Added control |
| Success rises: [before] to [after]; all else is fixed. | With the remaining conditions fixed, success rises from [before] to [after]. |

Prefer `and` or the established `&` convention to slash-packed prose. Make each number's referent visible.

```text
Across [number] trials per method, Method A achieves [a]% success and Method B achieves [b]%.
```

Separate rates, trial counts, and durations into readable clauses or a table when space allows. Preserve the meaning of percentages and percentage-point differences when changing presentation. Keep meaningful distinctions between task-weighted and group-weighted averages.

## 2. Give each sentence a main job

| Job | Purpose |
|---|---|
| Opening | Orient the reviewer and acknowledge their actual focus |
| Answer | State the conclusion immediately |
| Mechanism | Explain how the design addresses the question |
| Result | Give the decisive supplied fact |
| Implication | Explain why that fact matters here |
| Revision | Name the manuscript object and action |
| Bridge | Locate a distinct complementary answer |

When neighboring sentences repeat the same content, combine them or give one a different job. Keep a short explanation between a compact claim and unfamiliar technical detail.

## 3. Lead with the answer

### Direct conclusion

```text
The added control isolates the contribution of the visual input. The policy and execution schedule remain fixed while [input] changes.
```

### Mechanism

```text
The model uses [available information] to predict [relevant change]. This supplies [the information needed by the downstream component].
```

### Design rationale

```text
The design preserves the existing input interface. This lets [the intended user or component] use [the capability] with [the supplied compatibility condition].
```

### Correction

```text
We agree that the definition should be explicit. We will define [term] where it first appears in the method section.
```

Choose openings by rhetorical function. A list of every experiment performed usually delays the answer. Reviewer-level gratitude can carry the social function, leaving local openings free to carry substance.

## 4. Keep results and meaning adjacent

```text
Under the same evaluation setting, success increases from [before]% to [after]%. Changing [the controlled component] therefore accounts for [the supported interpretation].
```

Use the actual comparison and units. When two results concern different settings, name those settings before relating them. This keeps a strong conclusion precise and easy to assess.

## 5. Write useful titles and gratitude

A reviewer-level title can summarize the main completed additions and clarifications.

```text
Added Control Experiments and Expanded Comparisons
```

Build gratitude from the reviewer's concrete contribution, the professional ability it reflects, and the resulting improvement to the paper. This gives them a clear role in making the work stronger. The examples below describe completed improvements. Adapt the object and tense to the actual revision.

### When the reviewer suggests literature

```text
Thank you for highlighting these important studies. Your insightful guidance on the literature has helped us clarify how our work relates to prior research.
```

Recognize the reviewer's scholarly judgement and explain how the suggested literature sharpens the research positioning.

### When the reviewer suggests an experiment

```text
Thank you for this insightful experimental suggestion. Your methodological guidance has helped us strengthen the experimental design and make the paper more rigorous.
```

Name the recommended comparison or analysis when space permits. Connect the reviewer's expertise to what the addition improves in the evaluation. For a planned addition, use wording such as `Your methodological guidance will help us strengthen the evaluation through the proposed comparison.`

### When the reviewer identifies an error

```text
Thank you for your sharp observation and careful review. Your comment helped us correct the definition and make the presentation more precise.
```

Name the actual correction so the recognition has substance. Acknowledge the reviewer's perceptiveness and attention to detail, then move directly to the correction or answer.

Use the established salutation and level of formality. Keep recognition sincere and proportional to the actual comment. Match parallel openings in warmth and length while preserving the specific contribution. One well-placed acknowledgment can carry this function for a response. Remove a preview when the title and first answer already provide the same information.

## 6. End on the result's meaning or the revision

```text
This comparison demonstrates [the supported answer to this concern].
```

```text
We will add the comparison to Table 3 and define the setting in its caption.
```

```text
The complementary control is reported in R2-A3.
```

Choose one useful ending. Repeated assurances such as `We hope this addresses the concern` can usually be removed. Keep a future revision promise when it names a real action that helps the reader.

## 7. Use the fixed-neighbor check

For an opening-only edit, read the reviewer-level opening, changed opening, and first unchanged sentence together.

```text
Echoing opening
We added an evaluation under camera shifts.

Fixed next sentence
We evaluate the model under [number] camera shifts.

Better opening
The added evaluation directly tests robustness to viewpoint changes.
```

For a closing-only edit, read the last unchanged result, changed closing, and next heading together. If the result already states the gain, let the closing explain what that gain establishes.

Inspect the diff after a bounded edit. Keep the requested body and neighboring answers fixed.

## 8. Compare parallel boundaries

Read all reviewer openings together, followed by all answer first sentences, all final sentences, and all revision commitments. Look for repeated setup, an unusually elaborate greeting, the same first-sentence function everywhere, or mechanical revision endings.

Vary the rhetorical job where the content calls for it. Preserve conventions for headings, labels, bolding, quotation style, tables, and math.

## 9. Keep names, numbers, and references stable

Maintain a small private terminology ledger with the canonical method, baseline, setting, metric, difference unit, averaging label, and reference style. Use project terms from the supplied material.

Repeated values retain their comparison, unit, precision, and aggregation. A rate difference in percentage points keeps that meaning even when the prose is shortened. Explain a real distinction once rather than giving different objects one name.

Integrate references into the sentence.

```text
The added comparison is shown in Table~\ref{tab:comparison}.
The evaluation setting is described in Section~\ref{sec:evaluation}.
```

Use supplied labels. Prefer these grammatical references to parenthesized Table or Section references, and keep the chosen `Section` or `Sec.` form consistent.

## 10. Read the final paragraph aloud

Check whether the conclusion is clear on the first read, the sentences connect, and each technical detail helps answer the question. Trim repeated thanks, generic assurances, and self-weakening language. Retain facts and qualifications that materially affect the answer.
