# src/transform.py
import pandas as pd
from config.config import Config
import logging

class DataTransformer:
    def __init__(self):
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        self.config = Config()

    def transform_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Transform the input DataFrame.
        
        Args:
            df: Input DataFrame to be transformed.
        
        Returns:
            Transformed DataFrame.
        """
        self.logger.info("Transforming data...")
        
        # Example transformations:
        df = self.clean_column_names(df)
        df = self.handle_missing_values(df)
        df = self.convert_data_types(df)
        
        return df

    def clean_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean up column names (e.g., remove spaces, convert to lowercase, etc.)
        """
        self.logger.info("Cleaning column names...")
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        return df

    def handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Handle missing values in the DataFrame (e.g., fill, drop rows, etc.)
        """
        self.logger.info("Handling missing values...")
        df = df.fillna(0)
        return df

    def convert_data_types(self, df: pd.DataFrame) -> pd.DataFrame:
            # Convert 'created_at' only if it exists in the DataFrame
        if 'created_at' in df.columns:
            df['created_at'] = pd.to_datetime(df['created_at'])
        else:
            print("Note: 'created_at' column not found; skipping date conversion.")

        # Convert other columns as needed
        # ...

        return df