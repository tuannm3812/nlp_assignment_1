# Decoding the Debate: NLP Analysis of the Workplace Gender Equality Amendment Bill 2024

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Libraries](https://img.shields.io/badge/Libraries-Gensim%20%7C%20Scikit--Learn%20%7C%20NLTK-green)
![Status](https://img.shields.io/badge/Status-Complete-success)

![Parliamentary Inquiry Process](https://live-production.wcms.abc-cdn.net.au/f975a010ae7dafb11057b1d957733dd5?impolicy=wcms_crop_resize&cropH=2813&cropW=5000&xPos=0&yPos=260&width=862&height=485)

## 📖 Project Overview

This project applies **Natural Language Processing (NLP)** techniques to deconstruct the parliamentary discourse surrounding the *Workplace Gender Equality Amendment (Setting Gender Equality Targets) Bill 2024*. 

The analysis processes an unstructured corpus of **31 written submissions** to the Senate Finance and Public Administration Legislation Committee. By transforming raw text into structured data, this project reveals how different stakeholders (Unions, Industry Bodies, Advocacy Groups) frame the shift from voluntary reporting to mandatory gender equality targets.

## 🔍 Key Research Questions
1.  **Thematic Divergence:** What are the dominant latent topics in the corpus, and how do they vary by stakeholder group?
2.  **Stance & Vocabulary:** How do supportive vs. cautious submissions differ in their lexical choices?
3.  **Policy Granularity:** Does the debate focus on high-level ideology or specific implementation details?

## 🛠️ Technical Approach & Pipeline

The project implements an end-to-end NLP pipeline:

### 1. Data Ingestion & OCR
* **Hybrid Extraction:** Utilized `pdfplumber` for digital PDFs and `pytesseract` (OCR) for scanned image-based submissions.
* **Metadata Parsing:** Automated extraction of submitter names and classification into stakeholder groups (e.g., *Union*, *Industry Body*, *Government*).

### 2. Preprocessing
* **Cleaning:** Custom Regex functions to repair PDF artifacts (e.g., broken headers in ACTU submissions) and normalize whitespace.
* **Filtering:** Domain-specific stopword removal (excluding procedural terms like "inquiry" or "submission") to isolate content words.
* **Tokenization:** N-gram generation (Bigrams) to capture semantic units like *"pay gap"* and *"parental leave"*.

### 3. Advanced Modeling
* **Topic Modeling (LDA):** Trained a Latent Dirichlet Allocation model to uncover 5 latent themes, identifying a split between "Compliance" (Topic 2) and "Workplace Safety" (Topic 4).
* **Clustering (K-Means):** Applied K-Means clustering on TF-IDF vectors to group documents by semantic similarity.
* **Dimensionality Reduction:** Used PCA to visualize document clusters in 2D space.

## 📊 Key Findings

The analysis revealed a **bifurcated discourse** defined by role rather than consensus:

* **The "Two Worlds" Narrative:**
    * **Industry Bodies** (Cautious) clustered heavily around **Legislative Schemes**, using language focused on compliance, review mechanisms, and implementation policy.
    * **Unions** (Supportive) clustered around **Lived Experience**, using language focused on safety, violence prevention, and leave entitlements.
* **The Data Gap:** Advocacy groups and Academics formed a distinct cluster focused on **Evidence**, emphasizing the need for robust data collection and leadership metrics.
* **Conclusion:** The success of the Bill depends on bridging the gap between the *technical compliance* demands of employers and the *safety/outcome* demands of workers.

## 📂 Repository Structure

```text
├── data
│   ├── raw            # Original PDF submissions
│   ├── processed      # Cleaned text data (if saved)
│   └── external       # Reference documents
├── notebooks
│   └── ANLP_AT1_ManhTuanNguyen_25739083.ipynb  # Main Analysis Notebook
├── reports            # Generated figures and final report
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation