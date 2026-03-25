import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import csv
import io
import os
from src.utils import call_ollama, clean_csv_value

COLUMNS = [
    'id', 'name', 'host_id', 'host_name', 'neighbourhood_group', 
    'neighbourhood', 'latitude', 'longitude', 'room_type', 'price', 
    'minimum_nights', 'number_of_reviews', 'last_review', 
    'reviews_per_month', 'calculated_host_listings_count', 'availability_365'
]

class CleanAndEnrich(beam.DoFn):
    def process(self, element):
        try:
            name = clean_csv_value(element.get('name', 'Unknown Listing'))
            price = float(element.get('price', 0))
            group = element.get('neighbourhood_group', 'NYC')

            # AI Summary call
            summary = call_ollama(f"Summarize this NYC Airbnb in 5 words: {name}")
            summary = clean_csv_value(summary)

            yield f"{element['id']},{name},{group},{price},{summary}"
        except:
            pass

def run_pipeline():
    input_file = 'data/AB_NYC_2019.csv'
    output_path = 'data/processed_results'
    
    if not os.path.exists('data'): os.makedirs('data')
    
    options = PipelineOptions(runner='DirectRunner')
    
    with beam.Pipeline(options=options) as p:
        (
            p 
            | "Read CSV" >> beam.io.ReadFromText(input_file, skip_header_lines=1)
            | "Sample 20 Rows" >> beam.combiners.Sample.FixedSizeGlobally(20)
            | "Flatten List" >> beam.FlatMap(lambda x: x)
            | "Parse NYC" >> beam.Map(lambda line: next(csv.DictReader(
                                    io.StringIO(line), fieldnames=COLUMNS)))
            | "AI Enrich" >> beam.ParDo(CleanAndEnrich())
            | "Write" >> beam.io.WriteToText(
                                    output_path, 
                                    file_name_suffix='.csv', 
                                    header="id,name,neighbourhood_group,price,ai_summary",
                                    shard_name_template='') 
        )

if __name__ == '__main__':
    run_pipeline()