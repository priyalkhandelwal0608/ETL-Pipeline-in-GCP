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


##  Key Features
* **Batch Processing with Apache Beam:** Uses the `DirectRunner` to handle complex data transformations, including text cleaning and structural parsing.
* **Local AI Enrichment:** Integrates **Ollama** to generate 5-word "catchy" summaries for each listing, eliminating the need for expensive API keys.
* **Production-Ready ETL:** Implements a modular `src/` architecture with reusable utilities for API communication and data sanitization.
* **Real-time Analytics:** A Streamlit frontend that triggers the pipeline, monitors progress, and visualizes borough-wise price distributions.
* **Fault Tolerance:** Implements robust error handling in the `DoFn` logic to ensure the pipeline continues even if specific LLM calls fail.

---

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
#  NYC Airbnb AI: End-to-End MLOps Pipeline
This project is a high-performance **ETL & MLOps Pipeline** designed to process massive datasets (NYC Airbnb Open Data) using **Apache Beam**. It integrates a **Local LLM (Llama 3 via Ollama)** to perform real-time data enrichment and text summarization, all visualized through a dynamic **Streamlit** dashboard.
