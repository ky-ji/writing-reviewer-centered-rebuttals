# Author Playbook for Reviewer-Centered Rebuttals

## 1. Choose the work that serves the request

Use the current draft and evidence designated by the user. Match the edit to its purpose.

- **Draft** turns concerns and supplied material into an argument.
- **Restructure** changes the order while preserving substance.
- **Compress** keeps coverage and decisive evidence within a budget.
- **Micro-edit** changes only the specified sentences or boundaries.
- **Consistency pass** aligns reviewer sections and repeated facts.

Carry forward the requested language, quotation convention, template, and editable span. For prose work, focus on explaining the supplied results. If a visible conflict changes the answer, identify the specific comparison or value that needs resolution and continue the independent edits.

## 2. Find the question that matters

Separate each review into atomic concerns, then ask what would resolve the underlying doubt. A request for more comparisons may concern novelty, compatibility, or fairness. A request for a control may concern which component causes the reported improvement. Use the reviewer's words to choose the relevant interpretation.

A private map can keep the argument focused.

| Concern and original label | Direct answer | Decisive supplied support | Meaning or revision |
|---|---|---|---|
| What needs to be resolved? | What should the reader know first? | Which result or explanation answers it? | Why does it resolve this concern, and what changes? |

Give the clearest answer and most space to concerns that affect the assessment of the contribution. Preserve the existing W/Q order when requested. Merge related items when one argument answers them together, and retain every original label so coverage stays visible.

## 3. Build a complete argument

A useful answer often follows this progression.

1. State the answer or conclusion in ordinary language.
2. Explain the mechanism or distinction needed to understand it.
3. Give the strongest relevant result or clarification.
4. Say what that evidence establishes for this concern.
5. State a concrete manuscript change when it adds value.

Adapt the progression to the question. A yes/no question can start with `Yes.` and the substantive answer. A design question may need one sentence of purpose before its evidence. A short correction may need only an acknowledgment and the exact change.

For a mechanism concern, connect what information is available, how the method uses it, and what changes in the outcome. Put model names, setup details, and formulas after the reader understands their role.

For novelty or design rationale, state the positive contribution and the useful distinction from prior work. Support that distinction with the relevant comparison. Explain why an interface, assumption, or system choice matters to the intended use.

For a fairness concern, name the conditions that are shared and the cost that is included. Explain which question the comparison answers. A controlled component comparison and an end-to-end deployment comparison can support complementary points. Keep each result attached to its actual setting.

For a request about completed additions, summarize what has been added and give the key finding. Keep technical detail proportional to what the reviewer asked.

## 4. Write for both the reviewer and the AC

Each reviewer reply should make sense on its own. Include enough context to identify the issue and interpret its decisive result. A section number can help locate detail after the explanation.

Across replies, repeat a headline result when it answers another reviewer's concern. Keep the value, comparison, unit, and interpretation aligned. Within one answer, remove repeated setup and conclusions.

For an AC or meta-review response, organize around the concerns that matter to the assessment. Give the contribution, the most consequential resolved questions, their headline evidence, and the detailed reply locations when useful. Present a readable argument rather than a chronological account of the authors' work.

## 5. Use titles and openings to orient the reader

A response title should summarize what the reply contributes, such as an added control, expanded comparison, or clarified design. Prefer a concrete title over a generic promise to clarify everything. Keep its length proportionate to the document.

Keep the reviewer-level opening brief. Connect gratitude to a contribution or issue the reviewer actually recognized. A short preview is useful when it adds orientation beyond the title and first answer.

```text
Dear reviewer, thank you for recognizing the practical motivation and systems design.
```

Use `Dear reviewer` when it fits the established template. Match the warmth and length across reviewers while preserving their individual focus.

An answer heading should name its topic in plain language. Keep original concern labels and omit a trailing colon. Use the chosen connector consistently when grouping labels, for example `W1 & Q2`.

## 6. Keep the voice confident and constructive

Let the reasoning and evidence carry the response. Explain the method's purpose, the relevant distinction, and the observed result directly. Replace remarks about what a reviewer misunderstood with the explanation they need.

When a correction is warranted, acknowledge it briefly and state the specific action. When a limitation or uncertainty is central to the question, explain it accurately alongside the result and its implication. Keep these statements tied to the concern. Remove automatic apologies, generic limitation appendices, and self-protective commentary that add no information.

Maintain supported claim strength. Polishing should make the conclusion clearer. Preserve the distinction between demonstrated effects, associations, unresolved values, and future work.

## 7. End with meaning or a concrete change

Choose the ending that advances the local argument.

- Explain why the decisive result answers this concern.
- State the manuscript object and the action that will change it.
- Point to a distinct complementary answer when useful.

```text
We will add the comparison to Table 3 and explain the evaluation setting in its caption.
```

Use an exact section number only when supplied. Keep completed work in the appropriate completed tense and future revisions as commitments. End on the finding when there is no useful revision to promise. Compare closings side by side to catch mechanical repetitions of `We will...`.

## 8. Compress for the actual submission format

Draft enough to establish the answer, then compress in this order.

1. Repeated thanks and generic transitions.
2. Restatements of a concern already visible in its heading.
3. Setup repeated within the same reply.
4. Secondary detail that does not carry the conclusion.
5. Unnecessary words within otherwise complete sentences.

Protect the direct answer, decisive evidence, its meaning, and any useful revision. Keep at least one locatable answer for every concern. Match abbreviations and detail to the reader's ability to follow the argument.

Use the actual supplied limit and counting convention. Check the text that will be submitted, including any headings, greetings, spaces, and line breaks counted by that format. Preserve verbatim reviewer excerpts where the document calls for them. A separate reference layer can retain the reviews when the submission contains replies alone.

## 9. Harmonize without flattening

Create a small private ledger of canonical method names, metrics, units, averaging labels, and reference forms. Distinguish terms that refer to different objects. Compare the same boundary sentences across reviewers to align warmth and formatting while keeping each answer specific.

Use [micro-style-patterns.md](micro-style-patterns.md) for punctuation, sentence flow, and local edits. Use [final-audit.md](final-audit.md) for the final cross-review read.
