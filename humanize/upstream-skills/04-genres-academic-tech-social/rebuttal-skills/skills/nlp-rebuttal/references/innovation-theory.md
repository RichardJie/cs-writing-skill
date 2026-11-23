# Novelty, Motivation, Theory, and Scope (Tips 1-7)

Concerns about what the work is worth, how it truly differs from prior work, and where the method boundaries are.

Each tip: the typical reviewer concern, a reply style that backfires, a reply template that works, and the takeaway. Adapt templates to the actual paper. Replace every placeholder (XXX, A/B/C, Table X) with real content and real numbers before use.

## Tip 1: Method Too Complex / A Pile of Tricks

**Reviewer concern:** The method has many components and is complex overall. It is unclear which component actually matters and whether all of them are necessary.

**Bad answer (backfires):**

> "Thank you for your suggestion. The novelty of our method is XXX. We designed three components, A, B, and C. Every component is necessary, and none of them can be removed."

**Recommended answer (template):**

> Thank you for your suggestion. We understand your concern about the complexity of the method. However, the components in this paper are not a pile of tricks. Each one targets a different bottleneck:
> 1. Component A solves XXX;
> 2. Component B alleviates XXX;
> 3. Component C improves XXX.
> We have added a component-wise ablation. Removing A/B/C each causes a performance drop, and the full model achieves the best results. This shows the components are complementary and that the complexity comes from the challenges of the task.

**Takeaway:** Use design motivation plus component-wise ablation experiments to prove that each module is necessary, instead of just asserting that it works.

## Tip 2: Insufficient Novelty / Similar to Prior Work

**Reviewer concern:** The proposed method is similar to prior method A, and therefore lacks novelty.

**Bad answer (backfires):**

> "Thank you for your constructive comments. Our method is different from existing work, so it has some novelty."

**Recommended answer (template):**

> Thank you for your constructive comments. We clarify that our work differs from A in three aspects:
> 1. Different motivation: A focuses on XXX, while our work focuses on XXX.
> 2. Different implementation: A adopts XXX, while we design XXX.
> 3. Different role: A is used for XXX, while our method serves XXX.
> We will add a clearer comparison in the revised version.

**Takeaway:** Do not just say "we are novel." Spell it out: what the prior work does, what this paper does, and exactly where the two differ.

## Tip 3: Criticized as a Simple Combination of Existing Techniques

**Reviewer concern:** The method appears to simply stitch together existing techniques such as external memory, retrieval augmentation, and trajectory summarization.

**Bad answer (backfires):**

> "Although we use existing techniques, we are the first to apply them to the XXX domain and achieve SOTA performance. Therefore our work is valuable."

**Recommended answer (template):**

> Thank you for your feedback. We would like to clarify that the core conceptual novelty of this paper lies in XXX, which fills a gap left by prior frameworks.
>
> While our method includes basic modules such as retrieval and summarization, it is not an engineering patchwork. These modules serve a synergistic mechanism built around the core innovation.
>
> For example, the combination of modules A and B solves XXX, which traditional methods struggle to handle. It is exactly this deeply coupled system design that brings the significant performance gains.

**Takeaway:** Respond head-on. Emphasize the core innovation of the proposed work, the synergistic mechanism and deep coupling of its components, and its contribution to the field.

## Tip 4: Unclear Statement of Contributions

**Reviewer concern:** The paper's contributions are not clear enough. Readers have difficulty understanding what this paper actually contributes.

**Bad answer (backfires):**

> "Our contributions are already listed in the introduction. Perhaps the reviewer did not notice them."

**Recommended answer (template):**

> Thank you for pointing this out. We agree that the statement of contributions in the original paper is not focused enough.
> In the revised version, we will rewrite the contributions so that they map to the core innovations of this work:
> 1. We propose the XXX problem setting.
> 2. We design the XXX method.
> 3. We build the XXX experiments or analysis.
> We will also avoid presenting background material as contributions, and instead highlight what is genuinely new.

**Takeaway:** Do not blame the reviewer for not understanding. Contributions should be concrete, verifiable, and directly tied to the method and the experiments.

## Tip 5: Unclear Motivation / Insufficient Importance of the Problem

**Reviewer concern:** The authors' presentation does not convince me. I am not persuaded that this problem is real and important.

**Bad answer (backfires):**

> "Thank you for the reminder." Then repeat the content of the abstract or introduction and stress the importance of the problem one more time.

**Recommended answer (template):**

> Thank you for the reminder. We realize that the current version does not explain the motivation of the problem concretely enough.
>
> We will add a concrete application scenario to the introduction: in the XXX scenario, if XXX remains unsolved, the system suffers XXX consequences and incurs XXX costs.
>
> We will also explain how this paper mitigates that bottleneck through the XXX mechanism, so that the motivation, method, and experiments form a closed logical loop.

**Takeaway:** Show the problem's importance with a concrete use case plus the cost of leaving it unsolved, rather than rephrasing the abstract. This is more convincing.

## Tip 6: Insufficient Theoretical Analysis

**Reviewer concern:** The method lacks a theoretical explanation. It is unclear why it works.

**Bad answer (backfires):**

> "Thank you for your suggestion. Our method performs well in the experiments, which shows that it is effective."

**Recommended answer (template):**

> Thank you for your suggestion. We agree that a theoretical explanation helps clarify why the method is effective.
>
> The core intuition of this paper is XXX. Under the XXX assumption, M1 leads to XXX, which in turn enables M2 to XXX.
>
> In the revised version, we will add an analytical discussion, covering the core assumptions, the relation between the key steps and the objective function / representation space, and the boundary conditions under which the method may fail.

**Takeaway:** You do not have to provide a full theorem. But explain the mechanism, the assumptions, and the boundaries, and give the reviewer new insight.

## Tip 7: Superficial Discussion of Limitations

**Reviewer concern:** The discussion of limitations is insufficient and lacks depth. It does not face the real bottlenecks in practical applications.

**Bad answer (backfires):**

> "Our method does have limitations, such as requiring considerable computational resources and runtime. We will further optimize the structure and reduce the overhead in future work."

**Recommended answer (template):**

> Thank you for this insightful comment. We fully agree. The revised version will add a "Limitations and Future Work" subsection:
>
> 1. Our method depends on the initial capability of the base model. For weaker models, adding overly complex extra modules may interfere with their original performance and cause negative transfer.
> 2. Non-parametric extraction is bounded by the model's cognitive ceiling. Future work will explore paradigms such as reinforcement learning (see recent works X, Y).

**Takeaway:** Do not discuss limitations in vague terms like "not enough compute". Point out specific issues, such as capability thresholds, negative transfer, and ceiling effects.
