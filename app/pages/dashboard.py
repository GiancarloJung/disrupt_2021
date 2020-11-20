import streamlit as st
from app.db import Database
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np


database = Database()
movies = [
    {
        "title": "Movie Project #1",
        "image": "https://media.comicbook.com/files/img/default-movie.png",
        "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "people": ["Person 1", "Person 2"]
    },
    {
        "title": "Movie Project #2",
        "image": "https://media.comicbook.com/files/img/default-movie.png",
        "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "people": ["Person 1", "Person 3"]
    }
]

def filter_component():
    st.write("Search and Filter")
    cols = st.beta_columns(3)
    cols[0].text_input("Filter by Title")
    cols[1].multiselect("Filter by People", ["Person 1", "Person 2", "Person 3"])
    cols[2].slider('Filter by Score', 70, 100)

    st.button("Filter")


def movie_component(movie, index):
    col1, col2 = st.beta_columns((2, 1))

    with col1:
        st.header(movie['title'])
        st.write(movie['description'])
        st.write(', '.join(movie["people"]))

    with col2:
        st.subheader("Success Score")
        st.header("99%")
        view_analysis = st.checkbox("View Analysis", key=index)

    if view_analysis:
        team_expander = st.beta_expander("99% Team Score")
        with team_expander:
            cols = st.beta_columns((1, 3, 3, 1))
            with cols[1]:
                arr = np.random.normal(1, 1, size=100)
                fig, ax = plt.subplots()
                ax.hist(arr, bins=20)
                st.pyplot(fig)

            with cols[2]:
                st.write("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

        team_expander = st.beta_expander("99% Story Score")
        with team_expander:
            cols = st.beta_columns((1, 3, 3, 1))
            with cols[1]:
                arr = np.random.normal(1, 1, size=100)
                fig, ax = plt.subplots()
                ax.hist(arr, bins=20)
                st.pyplot(fig)

            with cols[2]:
                st.write("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

        team_expander = st.beta_expander("99% Finance Score")
        with team_expander:
            cols = st.beta_columns((1, 3, 3, 1))
            with cols[1]:
                arr = np.random.normal(1, 1, size=100)
                fig, ax = plt.subplots()
                ax.hist(arr, bins=20)
                st.pyplot(fig)

            with cols[2]:
                st.write("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")


def write():
    st.title("Dashboard")

    filter_component()

    for index, movie in enumerate(movies, start=0):
        movie_component(movie, index)
