
import pandas as pd
import streamlit as st

# from src.exception import CustomException
# import sys
from src.pipeline.predict_pipeline import RecommendPipeline
# from tmdbv3api import TMDb
# tmdb = TMDb()
api_key = 'bd9a5e8dd6e5ee4eab2ad20d409c4a62'
# from flask import Flask, requests,
st.title('Movie Recommendation System')

movie_df = pd.read_csv('main data.csv')

movies_list = movie_df['movie_title'].values


selected_movie = st.selectbox(
    'Choose a Movie Name', movies_list)

# st.button("Reset", type="primary")
if st.button('Recommend Movies'):
    recom = RecommendPipeline()
    names, posters = recom.recommendation(movie=selected_movie, api_key=api_key)
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
