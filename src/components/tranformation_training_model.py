import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import get_stem, save_object
# from src.components.data_ingestion import DataIngestion
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from dataclasses import dataclass
from sklearn.metrics.pairwise import cosine_similarity
# to see the angle b/w vectors the smaller value the more similar
"""
    MOST DATA PRE-PROCESSING IS ALREADY WHILE EXTRACTING THE DATA THE DATA FILE IS THE TRANSFORMED FILE
"""
data = pd.read_csv('G:\Projects\03 Movie Recommendation\main data.csv')


@dataclass  # This will give whatever input required here
class ModelTrainingConfig:
    trained_model_filepath = os.path.join('Artifacts', "model.pkl")


class DataTransformation:

    def get_data_transformation(self):
        try:
            features = 'tags'
            data[features] = data[features].apply(get_stem)
            logging.info(f'stemming Features : {features}')
        except Exception as e:
            raise CustomException(e, sys)


class ModelTraining:
    def __init__(self):
        self.model_training_config = ModelTrainingConfig()

    def initiate_model_training(self):
        try:
            logging.info('Initiating model training and building')
            cv = CountVectorizer(max_features=5000, stop_words='english')  # will convert the text into vectors
            vectors = cv.fit_transform(data['tags']).toarray()
            similar = cosine_similarity(vectors)
            save_object(file_path=self.model_training_config.trained_model_filepath,
                        obj=similar)
        except Exception as e:
            raise CustomException(e, sys)
