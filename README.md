CSV pipeline to postgreSQL DB
## ETL

## Project Overview
This project is a data pipeline designed to extract data from CSV and Excel files, transform the data, and load it into a target database table. It consists of modules for data extraction, transformation, and loading.
## Modules
## Extract: Contains classes for extracting data from CSV and Excel files.
## Transform: Placeholder for data transformation logic.
## ## Load: Handles loading data into the target database table.
Main: Entry point for running the ETL process.
## Dependencies
pandas: Data manipulation library.
requests: HTTP library for making API requests.
sqlalchemy: SQL toolkit and Object-Relational Mapping (ORM) library.
openpyxl: Required for reading Excel files.
python-dotenv: For loading environment variables from a .env file.

## Setup
Install dependencies listed in requirements.txt.
Ensure the necessary optional dependencies like openpyxl are installed.
Configure the database connection details in config/config.py.
Run the ETL process by executing python main.py.
Usage
Place CSV and Excel files in the designated data directories.
2. Run the ETL process to extract, transform, and load the data into the database.
Monitor logs for any errors or information during the process.


## Contributors
Aleksandr-kelvin# ETL-pipeline
