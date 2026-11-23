# Experiments and Evaluation Evidence (Tips 13-28)

Empirical concerns: baselines, ablations, cost, generalization, significance, human evaluation, reproducibility.

Each tip: the typical reviewer concern, a reply style that backfires, a reply template that works, and the takeaway. Adapt templates to the actual paper. Replace every placeholder (XXX, A/B/C, Table X) with real content and real numbers before use.

## Tip 13: Insufficient Comparison with Strong Baselines

**Reviewer concern:** The paper does not compare against the latest or strongest baselines, so the experiments are not convincing enough.

**Bad answer (backfires):**

> "Due to time and computational resource constraints, we did not include this baseline. The existing results are already sufficient to show that our method is effective."

**Recommended answer (template):**

> "Thank you for this important suggestion. We agree that comparing with stronger baselines can make the experiments more convincing. The current version already compares against methods B, C, and D, which are representative methods of the XXX, XXX, and XXX categories, respectively. For method A that you mentioned, we have added a comparison experiment. The main results are shown in Table X. The results show that our method still outperforms A on the XXX metric, indicating that our conclusions still hold under stronger comparisons."

**Takeaway:** Do not use "insufficient resources" as the main reason. Explain the coverage of the existing baselines and add feasible experiments where possible. If a full comparison cannot be added, also explain why the current baselines are representative and provide some analysis of the algorithmic logic.

## Tip 14: Small Experimental Improvement Margins

**Reviewer concern:** The proposed method offers only limited improvement over the baseline, and its practical significance is unclear.

**Bad answer (backfires):**

> "Although the improvement is not large, our method still outperforms the baseline."

**Recommended answer (template):**

> "Thank you for this observation. We agree that the size of the improvement should be interpreted in light of task difficulty and real-world settings. The improvements in this paper are mainly reflected in three aspects. First, on the main metric our method improves over the strongest baseline by XXX. Second, in harder settings, such as XXX, the improvement is more pronounced. Third, our method also maintains lower computational cost, better stability, or stronger generalization, so the contribution does not come from a single metric gain alone. In the revision we will add statistical significance tests, variance results, and an explanation of the performance differences across settings."

**Takeaway:** Explain small improvements in terms of task difficulty, stability, cost, robustness, and statistical significance, rather than only insisting "ours is higher."

## Tip 15: Unfair Experimental Setup

**Reviewer concern:** The training setup, hyperparameters, or compute budget of the proposed method may differ from those of the baselines, making the comparison unfair.

**Bad answer (backfires):**

> "We have done our best to ensure a fair comparison. All experimental settings are reasonable."

**Recommended answer (template):**

> "Thank you for pointing this out. Fair comparison is indeed a key issue in our experimental design. In the current experiments, we keep the same data splits, number of training epochs, model backbone, evaluation metrics, and random seeds for all methods. For hyperparameters specific to each method, we use the settings recommended in the original papers or tune them on the validation set. In the revision, we will add an experimental configuration table that makes clear which settings are fully identical, which follow the default configurations of the original methods, and whether any extra compute budget exists and how it is controlled."

**Takeaway:** A response about fairness must be specific about data splits, training epochs, models, random seeds, hyperparameter search, and compute budget.

## Tip 16: Insufficient Ablation Study

**Reviewer concern:** The paper lacks an ablation study of its key components. It is impossible to judge whether each module is truly effective.

**Bad answer (backfires):**

> "Due to space limitations, we did not present ablation experiments, but every module is necessary."

**Recommended answer (template):**

> "Thank you for the suggestion. We agree that ablation studies are essential for verifying module effectiveness. Our method contains three key components: M1, M2, and M3. We have added the following experiments. We remove M1 to verify its effect on XXX. We replace M2 with a simple strategy to verify the necessity of our design choice. We remove M3 to analyze its contribution to stability, efficiency, and generalization. Preliminary results show that removing XXX drops performance from XXX to XXX. This shows the component makes a substantial contribution to the final results."

**Takeaway:** Do not just say "the module is necessary." State what you remove, what you replace, and which metric it affects, and provide real results or a clear plan for supplementary experiments.

## Tip 17: Method Complexity / Excessive Computational Overhead

**Reviewer concern:** The proposed method introduces extra computational overhead, so its practical value may be limited.

**Bad answer (backfires):**

> "Although the overhead is large, this performance gain is worth it on highly challenging tasks."

**Recommended answer (template):**

> "Thank you for pointing this out. We agree that practical use must weigh both performance and cost. The extra overhead of our method comes mainly from XXX, with complexity XXX. Compared with the baseline, training/inference time increases by about XXX%, but this brings an XXX performance gain. Moreover, the overhead is controllable. It is introduced only in the training/preprocessing/offline-construction stage and does not affect online inference. The relevant steps can be parallelized. In large-scale settings, it is small relative to the cost of training the model itself. For multi-stage workflows, we will also explain its 'one-time investment, long-term reuse' nature: the upfront construction cost is amortized over later inference."

**Takeaway:** Do not answer in generalities. Give a concrete, detailed analysis, for example of complexity, time, GPU memory, and amortizability.

## Tip 18: Large-Scale Experiments That Cannot Be Finished Within the Rebuttal Period

**Reviewer concern:** The reviewer suggests validating on larger datasets, larger models, or more settings (but the full experiment is hard to complete within the rebuttal period).

**Bad answer (backfires):**

> "This experiment cannot be completed during the rebuttal period."

**Recommended answer (template):**

> "Thank you for the suggestion. We agree that larger-scale validation would further strengthen our conclusions. However, the full experiment requires substantial compute, for example about XXX GPU hours / XX GPUs running for XX days, so it is hard to finish the complete version within the rebuttal period. To address your concern as much as possible, we have added a representative small-scale experiment. The results are in Table X. Although this experiment is smaller in scale, it directly targets the core issue you raised, XXX. The results show that our method still yields stable gains in this setting, which suggests it has the potential to scale to larger settings. We will include this preliminary result in the final version and further complete the larger-scale experiments."

**Takeaway:** Do not simply say there is no time for the experiment. Instead, state the concrete cost of the full experiment, and try to add a representative experiment that answers the reviewer's core concern. Even if you can only provide small-scale results, explain why they are informative and state clearly how you will complete the full experiments later.

## Tip 19: The Dataset Is Too Small

**Reviewer concern:** The dataset used in this paper is small and insufficient to support the conclusions.

**Bad answer (backfires):**

> "Although the dataset is not large, the experimental results have already proven that the method is effective."

**Recommended answer (template):**

> "Thank you for the suggestion. We agree that dataset size affects how well the conclusions generalize. Following prior work, we chose this classic dataset because it covers XXX scenarios and allows a fair comparison with existing methods. To strengthen the reliability of our conclusions, we have added dataset statistics and new experiments on dataset B. We will also state clearly in the Limitations section that the current conclusions still need further validation on larger-scale data."

**Takeaway:** Do not dodge the dataset-size issue. Explain why this dataset was chosen, and state whether you will add experiments or narrow the claims.

## Tip 20: Insufficient Generalizability

**Reviewer concern:** The paper is validated on only a small number of datasets, models, or tasks, which cannot demonstrate generalizability.

**Bad answer (backfires):**

> "We believe the current datasets/models are representative enough, so they can demonstrate the generalizability of our method."

**Recommended answer (template):**

> "Thank you for the suggestion. We agree that validation in more settings would strengthen the conclusions. Our current datasets cover typical scenarios such as XXX, XXX, and XXX, and our models cover representative architectures such as XX and XX. This gives an initial validation of the method under different conditions. To further address your concern, we have added results on the additional dataset/model XXX, and included analyses under cross-dataset, cross-model, or cross-task settings. The revised version will also discuss where the method applies and where it may fail."

**Takeaway:** A generalizability concern cannot be answered with a single line like "our datasets are representative." It is best to add cross-dataset, cross-model, cross-task, or failure-case analyses.

## Tip 21: Results Lack Statistical Significance

**Reviewer concern:** The experiments do not report variance, confidence intervals, or results over multiple random seeds.

**Bad answer (backfires):**

> "Due to the high computational cost, we only ran the experiment once, but the trend in the results is clear."

**Recommended answer (template):**

> "Thank you for pointing this out. We agree that results over multiple random seeds better reflect the stability of the method. The current version reports results with a fixed random seed. To address your concern, we have added the mean and standard deviation over at least XXX random seeds. Preliminary repeated experiments show that our method achieves XXX ± XXX on the main metric, which maintains a stable advantage over the baseline's XXX ± XXX. We will report standard deviations in the tables and discuss result variability in the main text."

**Takeaway:** Stability concerns are best answered with multiple random seeds, standard deviations, confidence intervals, or significance tests

## Tip 22: Training Data Leakage Risk

**Reviewer concern:** The paper's training data and test data may overlap, making the results unreliable.

**Bad answer (backfires):**

> "We believe there is no data leakage."

**Recommended answer (template):**

> "Thank you for pointing this out. We understand the reviewer's concern about the risk of data leakage. We adopted this dataset following the experimental settings of prior work. In addition, we further checked the overlap among the training, validation, and test sets and found no data leakage. In the next version, we will add a discussion of this issue."

**Takeaway:** Take data-leakage concerns seriously. Do not just say "there is none". Explain how you checked and ruled it out, so the reviewer is convinced.

## Tip 23: Hyperparameter Sensitivity

**Reviewer concern:** Are the experimental results sensitive to hyperparameters? Why is k fixed at 40? Are there any experiments on this hyperparameter?

**Bad answer (backfires):**

> "We report the best results the method can achieve, so we chose k=40."

**Recommended answer (template):**

> "Thank you for pointing this out. In fact, we already report a sensitivity analysis of k in Table X / Appendix X of the original paper. To make sure readers do not miss it, we will highlight this result further in the final version. We will also add a note in the main text: our method performs stably across different values of k, and k=40 offers a good balance between performance and efficiency, so it was chosen as the default setting."

**Takeaway:** A hyperparameter sweep shows whether the method is stable and explains the basis for the default value, rather than only reporting the best result.
The focus is on stating the tested range, the trend in the results, and the rationale for the final choice.

## Tip 24: Poor Choice of Evaluation Metrics

**Reviewer concern:** The chosen metrics do not truly measure the task; the xxx metric is missing.

**Bad answer (backfires):**

> "The metrics we use are common in this field, so there is no problem."
> or
> "Prior work all uses this metric, so we use it too."

**Recommended answer (template):**

> "Thank you for the suggestion. In the original paper we adopted the XXX metric mainly because it is consistent with existing baseline work, such as A, B, and C. This ensures a fair comparison with existing methods.
> At the same time, we agree that the XXX metric you point out can more directly measure the XXX property of the task. We have therefore added experimental results with this metric, shown in Table X. The results show that under the new metric, our method still outperforms the main baselines, and the overall conclusion stays consistent with the original experiments.
> In addition, we will further explain in the revision what each metric emphasizes: the XXX metric mainly measures XXX, while the newly added XXX metric focuses more on XXX. Combining the two therefore gives a more complete evaluation of the effectiveness of our method."

**Takeaway:** First explain that the original metric ensures a fair comparison with prior work. Then add the metric the reviewer suggests to address the evaluation needs of the task itself, and run new experiments to check whether the conclusions stay consistent. Also explain what each metric emphasizes, and avoid supporting your conclusions only with metrics that favor you.

## Tip 25: Missing Human Evaluation

**Reviewer concern:** Relying only on automatic metrics is not convincing. A human evaluation is needed to verify the effectiveness of the method.

**Bad answer (backfires):**

> "Automatic metrics correlate highly with human judgment, so no human evaluation is needed."

**Recommended answer (template):**

> "Thank you for the suggestion. We agree that automatic metrics alone may not fully reflect the quality of model outputs. To further verify the effectiveness of our method, we added a small-scale human evaluation. The results are in Table X. Specifically, we recruited N annotators to evaluate XXX randomly sampled examples. They scored or compared preferences along dimensions such as XXX, XXX, and XXX. We provided a clear annotation protocol and computed inter-annotator agreement, κ = XXX / Krippendorff's α = XXX. The human evaluation shows that our method outperforms the baseline on the XXX dimension, and the overall trend is consistent with the automatic metrics. This further shows that the improvement of our method is not only visible in automatic metrics but can also be perceived by human evaluators. We will add the human evaluation setup, the annotation protocol, and the result analysis to the final version."

**Takeaway:** Add a small-scale human evaluation with a clear annotation protocol and agreement metrics. Report the number of annotators, the sample size, the evaluation dimensions, and the result trend. Do not just claim that automatic metrics are already reliable enough.

## Tip 26: Lack of Direct Evaluation of Intermediate Results / Generation Quality

**Reviewer concern:** The method contains an intermediate module that generates, summarizes, or extracts knowledge, but there is no direct verification of whether this extracted intermediate content is actually accurate, effective, or free of redundancy.

**Bad answer (backfires):**

> "We manually inspected the generated intermediate content and its quality is high. In addition, the metric gains on the final end-to-end task also indirectly prove that the intermediate results are reliable."

**Recommended answer (template):**

> "Thank you for this constructive comment. We agree that directly validating the quality of the intermediate results is critical. To this end, we added a double-blind evaluation during the rebuttal period. We use a strong model (e.g., GPT-4 or Gemini-Pro) as an objective judge to score the intermediate content extracted by our method and by the baseline, along dimensions such as accuracy, trigger specificity, executability, and generalizability. The results show that our method significantly outperforms the baseline on 'executability' and 'specificity', and effectively reduces vague heuristic expressions (detailed numbers in the table below). We will add this detailed quality analysis to the revised version."

**Takeaway:** Do not argue backwards from "the final metrics are good" to "the intermediate generation quality is good". Introducing an objective, multi-dimensional evaluation with clear scoring criteria (e.g., a strong-model judge or a human double-blind evaluation) is an extremely rigorous and convincing solution.

## Tip 27: Dynamic/Continual Process Claims Lack Experimental Support Along the Time Dimension

**Reviewer concern:** The paper claims the method is "continually evolving", "online updating", or "dynamically accumulating", but the main experiments look like one-shot offline training and evaluation, with no evidence of the evolution process.

**Bad answer (backfires):**

> "Due to the setup of the evaluation framework, we fixed the parameters at test time to ensure fairness. In terms of its theoretical architecture, however, the method is fully capable of dynamic updating."

**Recommended answer (template):**

> "Thank you for this sharp observation. Although we used offline evaluation in the main experiments to ensure a fair zero-shot comparison, the method is designed to fully support online dynamic evolution. To demonstrate this, we added a longitudinal experiment: the system processes 100 tasks in sequence, and we evaluate its performance every 20 tasks. As the new table shows, the system's average success rate rises clearly as more tasks are processed (steadily improving from XX% to XX%). This strongly shows that the system can self-iterate over a continual stream. We will add this learning curve to the appendix."

**Takeaway:** When the "dynamic/continual" property is questioned, the strongest response is to add a longitudinal time-series experiment (e.g., a performance curve measured every fixed number of steps) and use real trend data to show that the system improves over time.

## Tip 28: Reproducibility / No Code Provided

**Reviewer concern:** No code is provided, random seeds are not given, and the hyperparameter description is incomplete, so the results are hard to reproduce.

**Bad answer (backfires):**

> "Code can be provided upon request."

**Recommended answer (template):**

> "Thank you for the suggestion. We agree that the current version does not describe the reproduction details sufficiently. To improve reproducibility, we have added a more complete experimental setup, including the main hyperparameters, random seeds, number of training epochs, batch size, learning rate, hardware environment, data preprocessing, and model selection details; see Table X. In addition, we have prepared an anonymous code repository and provide the link (in the rebuttal / supplementary material, where conference rules permit). If the paper is accepted, we commit to releasing the full code, configuration files, and run scripts so that future researchers can reproduce our results. We will also add more detailed implementation notes in the camera-ready version to make the experimental setup more transparent."

**Takeaway:** For reproducibility concerns, do not just promise to "provide code later." Fill in as much information as you can right now, including an anonymous repository, random seeds, hyperparameters, training details, the data processing pipeline, and environment configuration. Also state clearly whether the code will be open-sourced after acceptance.
