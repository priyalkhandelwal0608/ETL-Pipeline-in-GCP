import apache_beam as beam
import pandas as pd
import duckdb
import os


# -------------------------------
# Clean Data
# -------------------------------
class CleanData(beam.DoFn):
    def process(self, row):
        row.pop('last_review', None)
        row.pop('reviews_per_month', None)

        if 'name' in row:
            row['name'] = str(row['name']).strip()

        yield row


# -------------------------------
# Transform Data
# -------------------------------
class TransformData(beam.DoFn):
    def process(self, row):
        try:
            price = float(row.get('price', 0))

            if price < 100:
                row['price_category'] = 'Low'
            elif price < 300:
                row['price_category'] = 'Medium'
            else:
                row['price_category'] = 'High'

            yield row

        except Exception as e:
            print("❌ Transform Error:", e)
            yield row


# -------------------------------
# Run ETL Pipeline
# -------------------------------
def run_etl_pipeline(file_path: str,
                     output_path: str = "data/output.csv",
                     db_path: str = "data/airbnb.duckdb"):

    print("🚀 Starting ETL Pipeline...")

    os.makedirs("data", exist_ok=True)

    # -------------------------------
    # STEP 1: Read CSV
    # -------------------------------
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    if df.empty:
        raise ValueError("❌ CSV is empty")

    data = df.to_dict(orient='records')

    # -------------------------------
    # STEP 2: Beam Pipeline
    # -------------------------------
    with beam.Pipeline() as p:
        (
            p
            | "Create Data" >> beam.Create(data)
            | "Clean Data" >> beam.ParDo(CleanData())
            | "Transform Data" >> beam.ParDo(TransformData())
            | "To DataFrame" >> beam.Map(lambda x: pd.DataFrame([x]))
            | "Flatten DF" >> beam.CombineGlobally(
                lambda dfs: pd.concat(list(dfs), ignore_index=True)
            )
            | "Write CSV" >> beam.Map(lambda df: df.to_csv(output_path, index=False))
        )

    # -------------------------------
    # STEP 3: Read Output
    # -------------------------------
    if not os.path.exists(output_path):
        raise ValueError("❌ Beam did not produce output")

    final_df = pd.read_csv(output_path)

    print("✅ Final Data:", final_df.shape)

    if final_df.empty:
        raise ValueError("❌ Output CSV is empty")

    # -------------------------------
    # STEP 4: Store in DuckDB
    # -------------------------------
    con = duckdb.connect(db_path)

    con.execute("DROP TABLE IF EXISTS listings")
    con.register("temp_df", final_df)

    con.execute("""
        CREATE TABLE listings AS 
        SELECT * FROM temp_df
    """)

    con.close()

    print("✅ Data stored in DuckDB")

    return final_df
