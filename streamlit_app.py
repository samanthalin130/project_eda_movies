import streamlit as st
import pandas as pd

df = pd.read_csv('movies_clean.csv')

st.title("🎬 Movie Genre Explorer")

all_genres = sorted(df['genres'].str.split('|').explode().unique())
all_genres = [g for g in all_genres if g != '(no genres listed)']

selected_genre = st.selectbox("Choose a genre:", all_genres)

filtered = df[df['genres'].str.contains(selected_genre, na=False)]

st.write(f"Showing {len(filtered)} movies in **{selected_genre}**")
st.dataframe(filtered[['Title', 'Year', 'genres']])

streamlit run streamlit_app.py
