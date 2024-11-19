# src/load.py
import pandas as pd
from sqlalchemy import create_engine
from config.config import Config
import logging

class DataLoader:
    def __init__(self):
        self.config = Config()
        self.engine = create_engine(self.config.get_database_url())

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def load_data(self, df: pd.DataFrame, table_name: str, if_exists: str = 'replace'):
        """
        Load the given DataFrame into the target database table.
        
        Args:
            df: DataFrame to be loaded.
            table_name: Name of the target database table.
            if_exists: Behavior when the table already exists ('replace', 'append', 'fail').
        """
        self.logger.info(f"Loading data into table: {table_name}")

        try:
            df.to_sql(
                table_name,
                self.engine,
                if_exists=if_exists,
                index=False,
                chunksize=1000
            )
            self.logger.info(f"Data load complete for table: {table_name}")
        except Exception as e:
            self.logger.error(f"Error loading data into table {table_name}: {str(e)}")
            raise