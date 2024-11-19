# config/config.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    SOURCE_PATH = os.getenv('SOURCE_PATH', './data/source')
    OUTPUT_PATH = os.getenv('OUTPUT_PATH', './data/output')
    
    # Database configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'ETLDemo')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'newpassword123')

    @staticmethod
    def create_directories():
        os.makedirs(Config.SOURCE_PATH, exist_ok=True)
        os.makedirs(Config.OUTPUT_PATH, exist_ok=True)

    @staticmethod
    def get_database_url():
        return f'postgresql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}'