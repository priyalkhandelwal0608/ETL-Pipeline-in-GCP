# ** NYC Airbnb AI: End-to-End MLOps Pipeline**

This project is a high-performance **ETL & MLOps Pipeline** designed to process massive datasets (NYC Airbnb Open Data) using **Apache Beam**. It integrates a **Local LLM (Llama 3 via Ollama)** to perform real-time data enrichment and text summarization, all visualized through a dynamic **Streamlit** dashboard.

---

## ** Key Features**
* **Batch Processing with Apache Beam:** Uses the `DirectRunner` to handle complex data transformations, including text cleaning and structural parsing.
* **Local AI Enrichment:** Integrates **Ollama** to generate 5-word "catchy" summaries for each listing, eliminating the need for expensive API keys.
* **Production-Ready ETL:** Implements a modular `src/` architecture with reusable utilities for API communication and data sanitization.
* **Real-time Analytics:** A Streamlit frontend that triggers the pipeline, monitors progress, and visualizes borough-wise price distributions.
* **Fault Tolerance:** Implements robust error handling in the `DoFn` logic to ensure the pipeline continues even if specific LLM calls fail.

---

## ** Project Architecture**
```text
ETL-Pipeline-in-GCP/
├── data/                  # Input CSV & Processed Results
├── src/
│   ├── pipeline.py        # Apache Beam ETL Logic
│   └── utils.py           # Ollama API & Cleaning Utilities
├── app.py                 # Streamlit UI Dashboard
├── requirements.txt       # Project Dependencies
└── .gitignore             # Optimized for Data Engineering
#  NYC Airbnb AI: End-to-End MLOps Pipeline
This project is a high-performance **ETL & MLOps Pipeline** designed to process massive datasets (NYC Airbnb Open Data) using **Apache Beam**. It integrates a **Local LLM (Llama 3 via Ollama)** to perform real-time data enrichment and text summarization, all visualized through a dynamic **Streamlit** dashboard.

---

##  Key Features
* **Batch Processing with Apache Beam:** Uses the `DirectRunner` to handle complex data transformations, including text cleaning and structural parsing.
* **Local AI Enrichment:** Integrates **Ollama** to generate 5-word "catchy" summaries for each listing, eliminating the need for expensive API keys.
* **Production-Ready ETL:** Implements a modular `src/` architecture with reusable utilities for API communication and data sanitization.
* **Real-time Analytics:** A Streamlit frontend that triggers the pipeline, monitors progress, and visualizes borough-wise price distributions.
* **Fault Tolerance:** Implements robust error handling in the `DoFn` logic to ensure the pipeline continues even if specific LLM calls fail.

---
# Project Overview

| Category | Tools |
| :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) |
| **Data Engineering** | ![Apache Beam](https://img.shields.io/badge/apache_beam-%23FF5733.svg?style=for-the-badge&logo=apache-beam&logoColor=white) |
| **Artificial Intelligence** | ![Ollama](https://img.shields.io/badge/Ollama-Llama3-black?style=for-the-badge) ![Requests](https://img.shields.io/badge/Requests-Rest_API-orange?style=for-the-badge) |
| **Frontend/Data Viz** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) |
| **DevOps & IDE** | ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) |

---

## **Getting Started**

### **1. Prerequisites**
Ensure you have **Ollama** installed and the **Llama 3** model downloaded locally. Run the following command in your terminal:

```bash
ollama run llama3
```bash
streamlit run app.py

##  Project Architecture
```text
ETL-Pipeline-in-GCP/
├── data/                  # Input CSV & Processed Results
├── src/
│   ├── pipeline.py        # Apache Beam ETL Logic
│   └── utils.py           # Ollama API & Cleaning Utilities
├── app.py                 # Streamlit UI Dashboard
├── requirements.txt       # Project Dependencies
└── .gitignore             # Optimized for Data Engineering
##  Tech Stack

| Category | Tools |
| :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) |
| **Data Engineering** | ![Apache Beam](https://img.shields.io/badge/apache_beam-%23FF5733.svg?style=for-the-badge&logo=apache-beam&logoColor=white) |
| **Artificial Intelligence** | ![Ollama](https://img.shields.io/badge/Ollama-Llama3-black?style=for-the-badge) ![Requests](https://img.shields.io/badge/Requests-Rest_API-orange?style=for-the-badge) |
| **Frontend/Data Viz** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) |
| **DevOps & IDE** | ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) |

---

##  Getting Started

### 1. Prerequisites
Ensure you have [Ollama](https://ollama.com/) installed and the **Llama 3** model downloaded locally:
```bash
ollama run llama3
```bash
streamlit run app.py
