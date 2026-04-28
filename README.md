# Decoding the Debate: NLP Analysis of the Workplace Gender Equality Amendment Bill 2024

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Libraries](https://img.shields.io/badge/Libraries-Gensim%20%7C%20Scikit--Learn%20%7C%20NLTK-green)
![Status](https://img.shields.io/badge/Status-Complete-success)
![License](https://img.shields.io/badge/License-MIT-blue)

![Parliamentary Inquiry Process](https://live-production.wcms.abc-cdn.net.au/f975a010ae7dafb11057b1d957733dd5?impolicy=wcms_crop_resize&cropH=2813&cropW=5000&xPos=0&yPos=260&width=862&height=485)

## 📖 Project Overview

This project applies **Natural Language Processing (NLP)** techniques to deconstruct the parliamentary discourse surrounding the *Workplace Gender Equality Amendment (Setting Gender Equality Targets) Bill 2024*.

The analysis processes an unstructured corpus of **31 written submissions** to the Senate Finance and Public Administration Legislation Committee, transforming raw text into structured insights. By combining classical NLP techniques with modern machine learning, this project reveals how different stakeholder groups (unions, industry bodies, government, advocacy groups, and academics) frame the gender equality debate through distinct vocabularies and conceptual frameworks.

### Key Insight
The analysis reveals a **bifurcated discourse** where the success of the Bill depends on bridging the gap between *technical compliance* demands of employers and *safety/outcome* demands of workers.

## 🔍 Research Questions

1. **Thematic Divergence:** What are the dominant latent topics in the corpus, and how do they vary by stakeholder group?
2. **Stance & Vocabulary:** How do supportive vs. cautious submissions differ in their lexical choices?
3. **Policy Granularity:** Does the debate focus on high-level ideology or specific implementation details?

## 🛠️ Technical Approach & Pipeline

The project implements an end-to-end NLP pipeline:

### 1. Data Ingestion & OCR
- **Hybrid Extraction:** Utilized `pdfplumber` for digital PDFs and `pytesseract` (OCR) for scanned image-based submissions
- **Metadata Parsing:** Automated extraction of submitter names and classification into stakeholder groups (Union, Industry Body, Government, etc.)

### 2. Preprocessing
- **Cleaning:** Custom Regex functions to repair PDF artifacts and normalize whitespace
- **Filtering:** Domain-specific stopword removal to isolate content words
- **Tokenization:** N-gram generation (Bigrams) to capture semantic units like *"pay gap"* and *"parental leave"*

### 3. Advanced Modeling
- **Topic Modeling (LDA):** Latent Dirichlet Allocation model uncovering 5 latent themes
- **Clustering (K-Means):** K-Means clustering on TF-IDF vectors to group documents by semantic similarity
- **Dimensionality Reduction:** PCA for 2D visualization of document clusters

## 📊 Key Findings

The analysis revealed distinct discourse patterns:

- **The "Two Worlds" Narrative:**
  - **Industry Bodies (Cautious):** Focus on compliance, review mechanisms, and implementation policy
  - **Unions (Supportive):** Focus on safety, violence prevention, and leave entitlements
  - **Advocacy Groups & Academics:** Emphasize evidence-based approaches and robust data collection

- **Conclusion:** Policy success depends on bridging the gap between employers' compliance concerns and workers' safety/outcome demands

## 📂 Repository Structure

```
gender-equality-nlp-analysis/
├── notebooks/
│   └── ANLP_AT1_ManhTuanNguyen_25739083.ipynb    # Main analysis notebook
├── data/                                          # Data files (in .gitignore)
│   ├── raw/                                       # Original PDF submissions
│   ├── processed/                                 # Cleaned text data
│   └── external/                                  # Reference documents
├── reports/                                       # Generated visualizations
├── src/                                           # Source code
├── tests/                                         # Unit tests
├── pyproject.toml                                 # Project configuration
├── requirements.txt                               # Python dependencies
├── Makefile                                       # Development commands
├── .gitignore                                     # Git ignore rules
└── README.md                                      # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip or conda

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tuannm3812/gender-equality-nlp-analysis.git
   cd gender-equality-nlp-analysis
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   make requirements
   ```

### Running the Analysis

1. **Open Jupyter Notebook**
   ```bash
   jupyter notebook notebooks/ANLP_AT1_ManhTuanNguyen_25739083.ipynb
   ```

2. **Run the pipeline**
   ```bash
   make data
   ```

## 🔧 Development Commands

```bash
make help           # Show available commands
make requirements   # Install dependencies
make clean         # Remove cache and compiled files
make lint          # Check code style with ruff
make format        # Format code with ruff
make test          # Run tests with pytest
```

## 📦 Dependencies

### Core Libraries
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning (K-Means, TF-IDF, PCA)
- **gensim** - Topic modeling (LDA)
- **nltk** - NLP toolkit

### Visualization
- **matplotlib** - Static plots
- **seaborn** - Statistical visualizations
- **wordcloud** - Word frequency visualization
- **networkx** - Network analysis

### Data Processing
- **pdfplumber** - Digital PDF extraction
- **pytesseract** - OCR for scanned documents
- **pdf2image** - PDF to image conversion
- **Pillow** - Image processing

### Utilities
- **tqdm** - Progress bars
- **loguru** - Logging
- **python-dotenv** - Environment management
- **typer** - CLI framework
- **ruff** - Code linter and formatter

## 📊 Analysis Overview

### Dataset
- **31 written submissions** to the Senate Finance and Public Administration Legislation Committee
- **Multiple stakeholder groups:** Unions, Industry Bodies, Government agencies, Advocacy groups, Academics
- **Text preprocessing:** Custom regex, domain-specific stopword removal, bigram tokenization

### Methods
- **LDA Topic Modeling:** 5 latent topics identified
- **K-Means Clustering:** Document semantic grouping
- **TF-IDF Vectorization:** Feature extraction
- **PCA:** Dimensionality reduction for visualization

### Outputs
- Topic distributions by stakeholder
- Document similarity visualizations
- Vocabulary comparison by submission stance
- Policy focus analysis (high-level vs. specific details)

## 📝 Citation

If you use this project in your research, please cite:

```bibtex
@project{nguyen2024gender,
  title={Decoding the Debate: NLP Analysis of the Workplace Gender Equality Amendment Bill 2024},
  author={Nguyen, Manh Tuan},
  year={2024},
  url={https://github.com/tuannm3812/gender-equality-nlp-analysis}
}
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Manh Tuan Nguyen**
- GitHub: [@tuannm3812](https://github.com/tuannm3812)
- Student ID: 25739083

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues, questions, or suggestions, please open an [issue](https://github.com/tuannm3812/gender-equality-nlp-analysis/issues) on GitHub.

---

**Project Status:** ✅ Complete  
**Last Updated:** April 2026
