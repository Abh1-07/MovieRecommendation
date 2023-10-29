import pandas as pd
import numpy as np
import requests
from src.exception import CustomException
import sys
from src.utils import load_object
from src.logger import logging
movie_df = pd.read_csv('main data.csv')


class RecommendPipeline:
    def __init__(self):
        pass

    def fetch_poster(self, movie_id, api_key):
        try:
            req = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}")
            data_json = req.json()
            if data_json['poster_path']:
                path = data_json.get("poster_path")
                poster = f"https://image.tmdb.org/t/p/original/{path}"
                logging.info('Poster fetched of Recommended Movies')
                return poster
            else:
                return np.Nan
        except Exception as e:
            raise CustomException(e, sys)

    def recommendation(self, movie, api_key):
        try:
            recommended_movies = []
            movie = movie.lower()
            movie_index = movie_df[movie_df['movie_title'] == movie].index[0]
            file_path = 'Artifacts/similarity.pkl'
            similarity = load_object(file_path=file_path)
            logging.info("Loading the saved similarity Model")
            distance = similarity[movie_index]
            movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
            movie_posters = []
            for i in movie_list:
                movie_id = movie_df['id'].iloc[i[0]]
                movie_posters.append(self.fetch_poster(movie_id, api_key))
                recommended_movies.append(movie_df['movie_title'].iloc[i[0]])
            logging.info(f"Recommended the Movie with poster of: {movie.capitalize()} ")
            return recommended_movies, movie_posters
        except Exception as e:
            raise CustomException(e, sys)
