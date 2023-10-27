import pickle
import pandas as pd
import numpy as np
import streamlit as st
import requests
from src.exception import CustomException
import sys
# from tmdbv3api import TMDb
# tmdb = TMDb()
api_key = 'bd9a5e8dd6e5ee4eab2ad20d409c4a62'
# from flask import Flask, requests,
st.title('Movie Recommendation System')

movie_df = pd.read_csv('main data.csv')

movies_list = movie_df['movie_title'].values
file_path = 'Artifacts/similarity.pkl'
similarity = pickle.load(open(file_path, 'rb'))


def fetch_poster(movie_id):
    try:
        req = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}")
        data_json = req.json()
        if data_json['poster_path']:
            path = data_json.get("poster_path")
            poster = f"https://image.tmdb.org/t/p/original/{path}"
            return poster
        else:
            return np.Nan
    except Exception as e:
        raise CustomException(e, sys)


def recommendation(movie):
    recommended_movies = []
    movie = movie.lower()
    movie_index = movie_df[movie_df['movie_title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    movie_posters = []
    for i in movie_list:
        movie_id = movie_df['id'].iloc[i[0]]
        movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movie_df['movie_title'].iloc[i[0]])
    return recommended_movies, movie_posters


selected_movie = st.selectbox(
    'Choose a Movie Name', movies_list)

# st.button("Reset", type="primary")
if st.button('Recommend Movies'):
    names, posters = recommendation(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(str(names[0]).capitalize())
        st.image(posters[0])

    with col2:
        st.text(str(names[1]).capitalize())
        st.image(posters[1])

    with col3:
        st.text(str(names[2]).capitalize())
        st.image(posters[2])
    with col4:
        st.text(str(names[3]).capitalize())
        st.image(posters[3])
    with col5:
        st.text(str(names[4]).capitalize())
        st.image(posters[4])

else:
    st.write('Sorry! The movie you requested is not in our database. '
             'Please check the spelling or try with some other movies')


# st.write('You selected:', )
