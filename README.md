# 🏙️ NYC Airbnb ETL Pipeline & Dashboard

This project demonstrates an **ETL pipeline** for the NYC Airbnb dataset using **DuckDB**, along with an interactive **Streamlit dashboard** to explore listings data.

---

## 🔹 Features

- **ETL Pipeline** with DuckDB:
  - Reads raw CSV data (`AB_NYC_2019.csv`)
  - Creates a DuckDB database (`airbnb.duckdb`)
  - Cleans data (e.g., replaces missing `reviews_per_month` with 0)
  - Ensures fast, SQL-based processing

- **Streamlit Dashboard**:
  - Displays total listings, average price, and average reviews
  - Filter by borough (`neighbourhood_group`)
  - Interactive map of listings
  - Preview raw data table (top 100 rows)

---

## 🗂️ Project Structure
ETL-Pipeline-with-DuckDB/
├── data/
│   ├── AB_NYC_2019.csv        # Raw Airbnb CSV dataset
│   └── airbnb.duckdb          # DuckDB database created by ETL
├── etl_pipeline.py            # ETL script to process CSV into DuckDB
├── dashboard.py               # Streamlit dashboard to visualize data
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
---

##Installation and run
- pip install -r requirements.txt
- python etl_pipeline.py
- streamlit run dashboard.py
