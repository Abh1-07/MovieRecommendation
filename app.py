import pickle
import pandas as pd
import streamlit as st

st.title('Movie Recommendation System')

# movies_dict = pickle.load(open('Artifacts\\movie_dict.pkl', 'rb'))
movie_df = pd.read_csv('main data.csv')

movies_list = movie_df['movie_title'].values
file_path = 'Artifacts/similarity.pkl'
similarity = pickle.load(open(file_path,'rb'))


def Recommendation(movie):
    recommended_movies = []
    movie = movie.lower()
    movie_index = movie_df[movie_df['movie_title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movie_list:
        recommended_movies.append(movie_df['movie_title'].iloc[i[0]])
    return recommended_movies



selected_movie = st.selectbox(
    'Choose a Movie Name', movies_list)

# st.button("Reset", type="primary")
if st.button('Recommend Movies'):
    recommendations = Recommendation(selected_movie)
    for i in recommendations:
        st.write(i)
else:
    st.write('No movie there')


# st.write('You selected:', )
