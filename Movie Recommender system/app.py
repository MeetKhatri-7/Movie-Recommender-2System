import streamlit as st
import pickle
import pandas as pd

movie_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies=pd.DataFrame(movie_list)

st.title("Movie Recommender System")

option = st.selectbox(
    "How would you like to be contacted?",
    movies["title"].values)


st.write("You selected:", option)

