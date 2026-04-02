# pipeline.py
import apache_beam as beam
import pandas as pd
from apache_beam.options.pipeline_options import PipelineOptions


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
        except:
            return


# -------------------------------
# Run ETL Pipeline
# -------------------------------
def run_etl_pipeline(file_path: str) -> pd.DataFrame:

    # STEP 1: Read CSV
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    # STEP 2: CLEAN
    df = df.drop(columns=['last_review', 'reviews_per_month'], errors='ignore')

    if 'name' in df.columns:
        df['name'] = df['name'].astype(str).str.strip()

    # STEP 3: TRANSFORM
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    def categorize(price):
        if price < 100:
            return 'Low'
        elif price < 300:
            return 'Medium'
        else:
            return 'High'

    df['price_category'] = df['price'].apply(categorize)

    # Fix numeric columns
    for col in ['minimum_nights', 'latitude', 'longitude']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df
