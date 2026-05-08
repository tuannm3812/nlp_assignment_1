# Gender Equality Policy NLP

![Python](https://img.shields.io/badge/Python-3.11-blue)
![NLP](https://img.shields.io/badge/NLP-TF--IDF%20%7C%20LDA%20%7C%20Clustering-green)
![License](https://img.shields.io/badge/License-MIT-blue)

![Parliamentary Inquiry Process](https://live-production.wcms.abc-cdn.net.au/f975a010ae7dafb11057b1d957733dd5?impolicy=wcms_crop_resize&cropH=2813&cropW=5000&xPos=0&yPos=260&width=862&height=485)

Natural language processing project for analysing Australian parliamentary submissions on the Workplace Gender Equality Amendment (Setting Gender Equality Targets) Bill 2024.

The project turns unstructured policy submissions into structured evidence about stakeholder priorities, vocabulary, and thematic differences. It combines document cleaning, TF-IDF feature extraction, topic modelling, clustering, and exploratory visual analysis to compare how unions, industry groups, government bodies, advocacy organisations, and academics frame workplace gender equality reform.

## Key Findings

- Industry submissions tend to emphasise compliance, review mechanisms, reporting burden, and implementation detail.
- Union submissions tend to emphasise worker safety, violence prevention, leave entitlements, and measurable outcomes.
- Advocacy and academic submissions frequently focus on evidence quality, data collection, and policy accountability.
- The central policy tension is between employer-side implementation risk and worker-side outcome expectations.

## Repository Layout

```text
gender-equality-nlp-analysis/
├── gender_equality_nlp/                         # Reusable Python package
│   ├── dataset.py                               # Corpus loading and text cleaning
│   ├── features.py                              # TF-IDF feature generation
│   ├── plots.py                                 # Plotting helpers and CLI
│   └── modeling/
│       ├── train.py                             # K-Means training workflow
│       └── predict.py                           # Cluster assignment workflow
├── notebooks/
│   └── workplace_gender_equality_discourse_analysis.ipynb
├── reports/
│   └── workplace_gender_equality_nlp_report.pdf
├── docs/
│   └── project-overview.md
├── tests/
├── pyproject.toml
├── requirements.txt
├── Makefile
└── README.md
```

Raw and processed data are intentionally excluded from version control. Place source documents under `data/raw/` and generated tables under `data/processed/`.

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e ".[dev]"
```

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
```

## Pipeline

Prepare a plain-text corpus:

```bash
python -m gender_equality_nlp.dataset --input-path data/raw/submissions --output-path data/processed/submissions.csv
```

Generate TF-IDF features:

```bash
python -m gender_equality_nlp.features --input-path data/processed/submissions.csv --output-path data/processed/features.csv
```

Train document clusters:

```bash
python -m gender_equality_nlp.modeling.train --features-path data/processed/features.csv
```

Create a top-term chart:

```bash
python -m gender_equality_nlp.plots --input-path data/processed/features.csv --output-path reports/figures/top_terms.png
```

## Development

```bash
make requirements   # Install package and development tools
make lint           # Run Ruff checks
make format         # Format and autofix Python files
make test           # Run tests with coverage
make typecheck      # Run mypy
make clean          # Remove local build and cache files
```

## Methods

The analysis uses a classical, inspectable NLP workflow:

- PDF/OCR extraction and manual text quality checks for source submissions
- Regex-based text cleanup for PDF artifacts and OCR spacing issues
- Domain-aware stopword handling and n-gram generation
- TF-IDF feature extraction for lexical comparison
- LDA topic modelling to identify recurring themes
- K-Means clustering and PCA visualisation for document-level structure

## Outputs

- Cleaned corpus tables
- Document-term feature matrices
- Cluster assignments
- Topic and vocabulary charts
- A PDF report summarising the policy interpretation

## Citation

```bibtex
@software{nguyen2024gender_equality_nlp,
  title = {Gender Equality Policy NLP},
  author = {Nguyen, Manh Tuan},
  year = {2024},
  url = {https://github.com/tuannm3812/gender-equality-nlp-analysis}
}
```

## License

This project is released under the MIT License. See [LICENSE](LICENSE).
