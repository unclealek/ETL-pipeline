# src/extract.py
import pandas as pd
import requests
from sqlalchemy import create_engine
from config.config import Config
import logging
from typing import Optional, Dict, Any

class DataExtractor:
    def __init__(self):
        self.config = Config()
        self.engine = create_engine(
            f'postgresql://{self.config.DB_USER}:{self.config.DB_PASSWORD}'
            f'@{self.config.DB_HOST}:{self.config.DB_PORT}/{self.config.DB_NAME}'
        )
        
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def extract_from_csv(self, file_path: str) -> pd.DataFrame:
        '''Extract data from CSV file'''
        try:
            self.logger.info(f"Extracting data from CSV file: {file_path}")
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            self.logger.error(f"Error extracting data from CSV: {str(e)}")
            raise
    def extract_from_excel(self, file_path: str, sheet_name: str = 'Sheet1') -> pd.DataFrame:
        """Extract data from Excel file"""
        try:
            self.logger.info(f"Extracting data from Excel file: {file_path}")
            df = pd.read_excel(file_path, sheet_name=sheet_name)     # <-- file_path and sheet_name are used here
            return df
        except Exception as e:
            self.logger.error(f"Error extracting data from Excel: {str(e)}")
            raise
