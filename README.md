<!-- PROJECT BANNER -->
<p align="center">
 <img src="https://media1.tenor.com/m/jDvF_mSFBKAAAAAC/dna-helix.gif" width=100%">
</p>

<h1 align="center">🧬 Cancer Drug Response Predictor (Genomics-ML)</h1>

<p align="center">
  Precision Oncology · Genomics · Machine Learning · IC50 Prediction
</p>

---

## Project Motivation

In modern oncology, **Precision Medicine** aims to match the *right drug* to the *right patient* using their **genetic signature**.

This project predicts **IC50 values** from **gene expression data**, enabling insights into cancer drug sensitivity and resistance.

---

## Theoretical Background

### 🔬 What is IC50?

**IC50 (Half Maximal Inhibitory Concentration)** is the drug concentration required to inhibit **50% of cancer cell growth**.

| IC50 Level | Interpretation |
|-----------|----------------|
| **Low IC50** | High drug sensitivity (effective at low doses) |
| **High IC50** | Drug resistance (higher doses → toxicity risk) |

Predicting IC50 is critical for **treatment personalization** and **toxicity reduction**.

---

## Biological Input: Gene Expression

The model analyzes **mRNA expression levels**, represented as **Z-scores (-3 to +3)**:

- **Positive (+)** → Over-expressed (up-regulated)
- **Negative (-)** → Under-expressed (down-regulated)

The ML system learns which gene expression patterns **reduce IC50**, improving drug efficacy.

---

## Machine Learning Architecture

### 1️⃣ Data Synthesis

- High-dimensional synthetic genomics dataset
- **100 gene features**
- **200 cancer cell samples**
- Generated using **NumPy & Pandas**
- Embedded controlled mathematical relationships where **driver genes influence IC50**

This mimics real-world biological signaling pathways.

---

### 2️⃣ Orthogonal Matching Pursuit (OMP)

A **greedy sparse regression algorithm** used for feature selection and prediction.

#### 🧠 Why OMP?

- Genomic datasets are **sparse**
- Only a few genes truly drive drug response
- OMP efficiently identifies **biologically relevant signals** from noisy data

---

## 💻 Technical Stack & Optimization

| Layer | Technology |
|------|-----------|
| AutoML | PyCaret |
| ML Model | Orthogonal Matching Pursuit (OMP) |
| Web App | Streamlit |
| Serialization | Pickle (`.pkl`) |
| Data | NumPy, Pandas |
| Hardware | Apple Silicon (M4) optimized |

---

## 🌐 Web Interface

- Real-time IC50 prediction via **Streamlit**
- Instant inference using a preloaded `.pkl` model
- Lightweight and research-demo friendly

