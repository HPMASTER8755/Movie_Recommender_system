import requests
import streamlit as st
import pandas as pd
import pickle

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=d24bb430305e98dc1b28cfaddd434795&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    re = []
    repo = []
    for j in movies_list:
        movie_id = movies.iloc[j[0]].id
        re.append(movies.iloc[j[0]].title)
        repo.append(fetch_poster(movie_id))
    return re, repo

movie_list = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_list)
moviess = movies['title'].values

# similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

option = st.selectbox(
    'How would you like to be contacted?',
    moviess)

if st.button('Recommend'):
    nam, pos = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
            st.text(nam[0])
            st.image(pos[0])

    with col2:
            st.text(nam[1])
            st.image(pos[1])

    with col3:
            st.text(nam[2])
            st.image(pos[2])

    with col4:
        st.text(nam[3])
        st.image(pos[3])

    with col5:
        st.text(nam[4])
        st.image(pos[4])
