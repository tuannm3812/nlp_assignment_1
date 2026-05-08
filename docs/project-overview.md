# Project Overview

## Purpose

This repository analyses public submissions about the Workplace Gender Equality Amendment (Setting Gender Equality Targets) Bill 2024. The project is designed as a reproducible NLP case study rather than a one-off notebook submission.

## Research Questions

1. What themes dominate the submission corpus?
2. How do stakeholder groups differ in vocabulary and policy framing?
3. Does the debate focus more on implementation detail, compliance, worker outcomes, or broad policy principle?

## Data Notes

The original submission PDFs and generated data tables are not committed to the repository. This keeps the repository lightweight and avoids redistributing source material that should be retrieved from the original public record.

Expected local structure:

```text
data/
├── raw/
│   └── submissions/
├── processed/
└── external/
```

## Reproducibility

The notebook contains the exploratory analysis and narrative interpretation. The Python package contains reusable pieces of the workflow so future analyses can run from the command line.
