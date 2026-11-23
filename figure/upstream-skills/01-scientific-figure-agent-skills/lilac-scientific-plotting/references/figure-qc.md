# Figure QC

Derived synthesis from pp.8-20,106-130,170-205, with added statistical/export checks. Apply relevant checks; record failures, repairs, and anything not verified.

## Data And Statistical Meaning

- [ ] Research question, observational unit and chart agree.
- [ ] Row counts, groups, units, transformations, exclusions and missingness are accounted for.
- [ ] Count versus identity, density versus count, total versus proportion are correct.
- [ ] Pair IDs, factor order, aggregation and map joins preserve intended relationships.
- [ ] Estimates, CI/SE/SD/prediction bounds, confidence level and effective n are defined.
- [ ] Model/test annotations come from the actual analysis; multiplicity/assumptions are not invented.
- [ ] Baselines, log transformations, facet scales, size mappings and secondary axes do not mislead.

## Visual Review At Final Size

- [ ] Each encoding has a purpose; palette is appropriate and distinguishable.
- [ ] Labels/units/legend are sufficient; no unnecessary duplicated guides.
- [ ] Legends and annotations do not obscure measurements, uncertainty or outliers.
- [ ] Labels/ticks/tags are legible, uncut and associated with the correct marks.
- [ ] Panel interiors align; whitespace and relative dimensions suit the content.
- [ ] Point size, line width, alpha and text hierarchy remain balanced after reduction.
- [ ] Useful guides remain; decorative clutter does not compete with evidence.

## Export And Reproduction

- [ ] Correct dimensions, format, DPI (raster), background and fonts.
- [ ] Reopened exported file is nonblank and matches expected content.
- [ ] Vector/raster choice matches the venue and graphic; font rendering checked.
- [ ] Code, seed, input provenance, statistical decisions and package versions are available.
- [ ] Tested/unverified boundaries are explicit; no claim of accessibility or journal compliance without checking it.
