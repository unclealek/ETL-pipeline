# src/main.py
from extract import DataExtractor
from transform import DataTransformer
from load import DataLoader

def run_etl():
    # Extract from PostgreSQL
    extractor = DataExtractor()

    # Extract from CSV
    csv_data = extractor.extract_from_csv("/Users/kelvinaliche/Desktop/DownProject/CSV_pipelin/data/centerwatch.csv")
    # Extract from Excel
    excel_data = extractor.extract_from_excel("/Users/kelvinaliche/Desktop/DownProject/CSV_pipelin/data/Clinical trials.xlsx")

    # Combine the data from various sources
    all_data = [csv_data, excel_data]
    print("Successfully added all data.")
    # Transform the data
    transformer = DataTransformer()
    transformed_data = [transformer.transform_data(df) for df in all_data]

    # Load the data
    loader = DataLoader()
    for i, df in enumerate(transformed_data):
        loader.load_data(df, f"target_table_{i}", if_exists='replace')

    print("ETL process completed.")

if __name__ == "__main__":
    run_etl()
