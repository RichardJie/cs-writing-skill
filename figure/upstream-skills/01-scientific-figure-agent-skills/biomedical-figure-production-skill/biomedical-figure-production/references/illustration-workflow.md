# Biomedical illustration workflow

## 1. Build an evidence map

For every proposed visual element, record:

- entity and biological compartment;
- relation or direction;
- source citation or dataset;
- model context: patient, animal, organoid, cell line, in silico, or cross-cancer;
- evidence class: direct perturbation, temporal observation, spatial association, cohort association, computational inference, or hypothesis;
- permitted wording and line style.

Reject decorative biology that has no source or explanatory purpose.

## 2. Draft the composition

Create a wireframe with boxes and arrows before generating artwork. Reserve fixed areas for panel letters, title, legend, boundary statement, and citations. Keep the visual reading direction consistent. Use whitespace to separate compartments rather than ornamental borders.

## 3. Create visual components

Use vector primitives for cells, organ outlines, membranes, arrows, receptors, axes, and labels whenever practical. If generative image creation is used:

- request a clean scientific illustration without labels or quantitative marks;
- avoid exact claims about histology, molecular binding geometry, or anatomical microstructure;
- save the generated bitmap separately from the annotated master;
- do not clone or extend observed experimental regions;
- document the tool and purpose in the manifest.

## 4. Encode evidence strength

Use a stable legend such as:

- solid line: direct experiment or perturbation in the stated disease model;
- dashed line: patient cohort or spatial association;
- dotted line: computationally inferred interaction;
- pale/dotted line: cross-cancer extrapolation or preclinical hypothesis.

Line style alone is insufficient when grayscale printing is possible. Pair it with labels or symbols.

## 5. Add text last

Add gene/protein names, doses, endpoints, and citations in an editable vector layer. Check nomenclature, italics policy, Greek characters, capitalization, abbreviations, and directional language. Use “associated with” when causality is not established.

## 6. Disclose boundaries

Include a short boundary statement when needed, for example: “Schematic relationships represent evidence from the models indicated; dotted links are computationally inferred or hypothesis-generating and do not establish patient-level causality.”

If the journal requires disclosure of generative AI use, state which non-data visual components were generated and that all scientific labels, quantitative content, and evidence coding were author-verified.

