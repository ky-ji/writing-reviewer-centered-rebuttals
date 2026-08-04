# Micro-Style Patterns for Rebuttal Openings, Closings, and Local Edits

Use this reference when the requested change is small but repeated across reviewer sections. The central trick is to give each boundary sentence one job, then compare equivalent boundaries side by side.

## 1. Sentence jobs

Label each sentence before revising it:

| Job | What it should do |
|---|---|
| Reviewer-level thanks | Name the reviewer's actual focus |
| Section preview | Group the main response themes |
| Direct answer | State the conclusion immediately |
| Context | Explain why the result or clarification is relevant |
| Result | Present the decisive supplied fact |
| Implication | Connect that fact to this concern |
| Revision | Name the manuscript object and action |
| Bridge | Point to a distinct answer without duplicating it |

If two adjacent sentences have the same job and content, delete or merge one.

## 2. Reviewer-level openings

Useful patterns:

```text
We thank the reviewer for focusing on [specific theme]. Below we clarify [issue] and report [result or addition].
```

```text
The review highlights two central questions: [theme 1] and [theme 2]. We address them in turn below.
```

```text
We appreciate the reviewer's close reading of [specific component]. The responses below separate [distinction] and add [requested comparison].
```

Normalize **structure and warmth**, not exact wording. One reviewer may warrant a more detailed opening, but avoid accidental imbalances such as:

- `Thank you.` for R1 versus four stacked praise phrases for R3;
- a one-sentence preview for R1/R2 versus a full response summary for R3;
- generic `valuable feedback` repeated for every reviewer.

After drafting an opening, compare it with the first fixed sentence of the first answer. Remove any repeated concern list, setup, or result.

## 3. Answer openings

Choose the opening by rhetorical job.

### Direct conclusion

```text
Yes—the added comparison shows [conclusion].
```

```text
The two components serve different roles: [X] handles ..., whereas [Y] handles ....
```

### Clarification

```text
The current wording conflates [A] with [B]; the intended distinction is ....
```

```text
Here, [term] refers specifically to ..., not ....
```

### New analysis or comparison

```text
We added the requested comparison under [plain-language setting].
```

```text
To answer this question directly, we evaluated ....
```

### Design rationale

```text
This design is intended to [purpose], while [other component] provides ....
```

Do not force gratitude into every answer opening. Reviewer-level thanks can carry the social function; local openings should usually carry the answer.

## 4. Result and implication pairs

Keep results and interpretation adjacent:

```text
The method improves success from 41.2% to 57.8% under the same camera shift. This directly supports the robustness benefit asked about in W2.
```

```text
Across the seven perturbations, the average gain is 12.4 percentage points. Thus, the improvement is not confined to a single view.
```

Use the units and claim strength already chosen by the authors. A prose pass should not automatically convert `demonstrates` to `suggests`, or add `may`, `preliminary`, `within this setup`, or a limitation sentence.

## 5. Answer closings

Select one useful ending.

### End on meaning

```text
Together, these results demonstrate that robot-centered supervision improves robustness.
```

```text
This distinction explains why the two modules are complementary rather than redundant.
```

### End on the exact revision

```text
We will add this comparison to Table 3 and define the perturbation protocol in its caption.
```

```text
We will replace the ambiguous term throughout Sec. 3 with [canonical term].
```

### End with a bridge

```text
The complementary control requested here is reported separately in R2-A3.
```

Avoid empty or mechanical endings:

```text
We will revise accordingly.
We hope this addresses the concern.
We thank the reviewer again.
```

These phrases are not forbidden; they simply add little when repeated. If several answers end with `We will...`, retain it only where the revision is the main takeaway.

## 6. The fixed-neighbor trick

For a boundary-only edit, never judge the new sentence alone.

### Editing an opening

Read:

1. reviewer-level opening;
2. new answer opening;
3. first unchanged body sentence.

Typical echo:

```text
New opening: We added an evaluation under camera perturbations.
Fixed next sentence: We evaluate the model under seven camera perturbations.
```

Better:

```text
New opening: The added evaluation directly tests robustness to viewpoint changes.
Fixed next sentence: We evaluate the model under seven camera perturbations.
```

### Editing a closing

Read:

1. last unchanged result sentence;
2. new closing;
3. next heading or answer, if any.

Typical echo:

```text
Fixed previous sentence: The gain is 12.4 percentage points on average.
New closing: These results show a 12.4-point average gain.
```

Better:

```text
New closing: This demonstrates that the benefit persists across viewpoint changes.
```

## 7. The parallel-boundary trick

Extract these lines into separate lists:

- all reviewer-level openings;
- all answer first sentences;
- all answer final sentences;
- all revision commitments.

Reading only the parallel boundaries makes patterns visible that disappear in full prose:

- R3 is much warmer than R1/R2;
- every answer begins with `We thank`;
- one reviewer uses only bold `A1`, while another bolds the full answer sentence;
- all R3 answers end with `We will`;
- the same baseline receives four different names.

Correct the pattern with the smallest local edits.

## 8. Canonical-term trick

Before the last pass, create a tiny substitution ledger:

```text
baseline: Official GR00T-N1.6
supervision target: RVM pseudo-label
camera condition: camera perturbation
difference unit: percentage points
figure reference: Fig.
```

Then scan all reviewer sections for aliases. Replace accidental variants. When two terms denote different concepts, keep them and add one explicit distinction.

This ledger also applies to capitalization, hyphenation, pluralization, and abbreviations.

## 9. Number-presentation trick

Repeated values should retain the same visual form:

- `29.5 percentage points` should not become `29.5%` elsewhere if it is a difference;
- a success-rate column should not include `%` in R1 and omit it in the equivalent R3 table;
- `26.4/24.7` should use the same precision and unit wherever repeated;
- choose either `mean ± s.d.` or another supplied label and use it consistently.

This is formatting normalization only. Do not recompute or reinterpret the numbers during a prose consistency pass.

## 10. Heading and bolding trick

Choose one local grammar and apply it across reviewer sections:

```text
**W1. [Weakness title]**
> [quote]
**A1. [Direct answer sentence]**
```

or:

```text
**A1.** [Direct answer sentence]
```

Either can work. The inconsistency arises when one answer bolds only the label, another bolds a full paragraph, and a third switches to `### Limitation` without a structural reason.

Also align heading depth, separators, table alignment, math delimiters, and reference forms such as `Fig.` versus `Figure`.

## 11. Concrete revision language

Replace vague promises with object + action:

| Vague | Concrete |
|---|---|
| We will clarify this. | We will define [term] at the start of the method section. |
| We will revise accordingly. | We will add the comparison to Table 3. |
| We will improve the discussion. | We will add a paragraph comparing [A] and [B]. |

Do not invent a location. If no section number is supplied, name only the manuscript object.

## 12. Final micro-edit pass

For each changed sentence, ask:

1. Does it have exactly one main job?
2. Does it repeat a fixed neighbor?
3. Is its warmth and length proportionate to parallel reviewer sections?
4. Does it introduce a new term, unit, heading style, or reference form?
5. Does it preserve the author's intended claim strength?
6. Is the smallest necessary span changed?

The goal is not to make every answer identical. It is to make differences intentional and conventions stable.
