import sys
import os
from src.exception import CustomException
from src.logger import logging
import dill
from nltk.stem.porter import PorterStemmer


def get_stem(text):
    try:
        output = []
        ps = PorterStemmer()
        for i in text.split():
            output.append(ps.stem(i))
        logging.info("Applying and Stemming The Feature Column for Model Training")
        return " ".join(output)
    except Exception as e:
        raise CustomException(e, sys)


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        # saving the pickle model to desired place
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info('Pickle file made and dumped with data')
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    except CustomException as e:
        raise CustomException(e, sys)
