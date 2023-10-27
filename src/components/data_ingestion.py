import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass


@dataclass  # This decorator, to define class we use __int__, through this can directly define the class variable
# Use dataclass when just defining variables, not if there are no other funcs
class DataIngestionConfig:
    raw_data_path: str = os.path.join('Artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Initiate Data Ingestion method')
        try:
            df = pd.read_csv('G:\Projects\03 Movie Recommendation\main data.csv')
            logging.info("Data Extracted and read as DataFrame")
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            return self.ingestion_config.raw_data_path
        except Exception as e:
            raise CustomException(e, sys)
