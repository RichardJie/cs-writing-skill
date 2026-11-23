# Writing Clarity, Related Work, and Communication (Tips 8-12)

Concerns about unclear writing, insufficient related work, reviewer misunderstandings, and low-quality negative reviews.

Each tip: the typical reviewer concern, a reply style that backfires, a reply template that works, and the takeaway. Adapt templates to the actual paper. Replace every placeholder (XXX, A/B/C, Table X) with real content and real numbers before use.

## Tip 8: Insufficient Discussion of Related Work

**Reviewer concern:** The paper does not adequately discuss its relationship to related work such as A, B, and C.

**Bad answer (backfires):**

> "We will cite these works in the revised version."

**Recommended answer (template):**

> Thank you for pointing this out. In the revised version, we will add the three lines of related work A, B, and C, and further clarify how they relate to our paper. Specifically, A mainly focuses on XXX. B mainly addresses XXX. C is the closest to our work, but its core assumption is XXX, while our paper focuses on XXX. Accordingly, we will add these comparisons in both the related work and method sections, so that readers do not misunderstand how our work differs from existing work.

**Takeaway:** Do not just add citations. It is better to explain how each work relates to your paper and what gap your paper fills.

## Tip 9: Unclear Writing in the Paper

**Reviewer concern:** Some concepts, notation, or the method pipeline in the paper are not clear enough, which hurts understanding.

**Bad answer (backfires):**

> "We will improve the writing in the final version."

**Recommended answer (template):**

> Thank you for pointing this out. We agree that the current version is not clear enough in the XXX part and may cause misunderstanding. In the revision we will make the following changes: add a formal definition of XXX in Section X; unify the use of symbol Y to avoid confusion with Z; add a method flowchart or pseudocode that explains the inputs, outputs, and each step; and clearly describe the implementation details of XXX in the experiment section.

**Takeaway:** Do not just say "we will rewrite it." Point out exactly where you will change, how you will change it, and which comprehension barrier it resolves.

## Tip 10: The Reviewer Misunderstood the Method

**Reviewer concern:** The reviewer raises a criticism based on a misunderstanding, for example believing the method depends on XXX when in fact it does not.

**Bad answer (backfires):**

> "You may have misunderstood our method. Our method does not work that way."

**Recommended answer (template):**

> Thank you for your comment. We believe the misunderstanding here may stem from unclear wording in the paper. Our method does not depend on XXX. The actual pipeline is: first XXX, then XXX, and finally XXX. Specifically, XXX is used only for XXX, not for XXX. Therefore, the risk raised in the review will not occur under the current setup. In the revision, we will revise the description in Section X and add a clarification to avoid similar misunderstandings.

**Takeaway:** When correcting a misunderstanding, do not directly say "the reviewer is wrong." First acknowledge that the wording was unclear, then focus on calmly clarifying how the method actually works.

## Tip 11: Vague, Low-Quality Negative Reviews

**Reviewer concern:** The review is vague overall. It only gives fuzzy negative judgments, such as "limited contribution", "insufficient experiments", or "unclear method", without concrete, actionable questions or suggestions for revision.

**Bad answer (backfires):**

> This review is too vague, so we cannot respond to it.
> Or: The reviewer did not understand our work.
> Or: Directly questioning the reviewer's expertise and judgment.

**Recommended answer (template):**

> Thank you for your feedback. We read the review carefully and extracted the concerns that we could respond to concretely. We address each of them below: ...
> For the more general comments, we may not fully grasp your specific concern without further detail. We are happy to improve the relevant parts in the final version, and we kindly ask you to point out your specific concerns so that we can make targeted revisions.
> If a note to the AC is needed, state briefly: some comments in this review are general and lack concrete, actionable detail. We have done our best to respond to every identifiable issue and have added supporting evidence. We hope the AC will weigh these responses and the added results.

**Takeaway:** For a vague negative review, respond point by point to every issue you can identify. For empty, generic comments, politely ask for clarification. When raising the matter with the AC, list only facts and evidence; never comment on the reviewer as a person.

## Tip 12: General Strategy: Try Not to Just Promise, Act Directly

**Reviewer concern:** The paper is missing a key experiment or analysis, so the current conclusions are not convincing enough. For example, the reviewer thinks the paper only reports overall performance, without further analysis of whether the method remains effective across different task scenarios or different model scales.

**Bad answer (backfires):**

> We will add this in the revised version.

**Recommended answer (template):**

> Thank you for this valuable suggestion. We agree that this analysis is very important for validating the effectiveness of our method. Following the reviewer's comment, we have added an experimental analysis broken down by sample difficulty. Specifically, we split the test set into easy, medium, and hard samples, and compared our method against the main baselines on each subset.
> The results show that... These results indicate that the main advantage of our method does not come only from an overall gain on easy samples. The effect is more pronounced on the more challenging samples. We will include these experimental results in the revised version and further discuss the reasons in the experimental analysis section.

**Takeaway:** Do not just say "we will add it". If time allows, present the key results of the new experiment or analysis directly in the rebuttal, including the experimental setup, core numbers, and conclusions.
