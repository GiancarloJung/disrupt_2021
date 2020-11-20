import streamlit as st
import streamlit.components.v1 as components

from app.db import Database

import numpy as np
import pandas as pd

from app.models.sentiment import sentiment_prediction

from app.utils.filter_component import filter_component
from app.utils.movie_component import movie_component


movies = [
    {
        "title": "Why Him?",
        "description": "A holiday gathering threatens to go off the rails when Ned Fleming realizes that his daughter's Silicon Valley millionaire boyfriend is about to pop the question.",
        "people": ["John Hamburg", "Zoey Deutch", "James Franco", "Tangie Ambrose"],
        "review": 'A wonderful little production. The filming technique is very unassuming- very old-time-BBC fashion and gives a comforting, and sometimes discomforting, sense of realism to the entire piece. The actors are extremely well chosen- Michael Sheen not only "has got all the polari" but he has all the voices down pat too! You can truly see the seamless editing guided by the references to Williams\' diary entries, not only is it well worth the watching but it is a terrificly written and performed piece. A masterful production about one of the great master\'s of comedy and his life. The realism really comes home with the little things: the fantasy of the guard which, rather than use the traditional \'dream\' techniques remains solid then disappears. It plays on our knowledge and our senses, particularly with the scenes concerning Orton and Halliwell and the sets (particularly of their flat with Halliwell\'s murals decorating every surface) are terribly well done.',
        "movie_score": "96%"
    },
    {
        "title": "Interstellar",
        "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "people": ["Christopher Nolan",	"Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
        "review": "The movie's storytelling masterstroke comes from adherence to principles of relativity: the astronauts perceive time differently depending on where Endurance is, which means that when they go down onto a prospective habitable world, a few minutes there equal weeks or months back on the ship. Meanwhile, on Earth, everyone is aging and losing hope. Under such circumstances, even tedious housekeeping-type exchanges become momentous: one has to think twice before arguing about what to do next, becau",
        "movie_score": "93%"
    }
]
df_movies = pd.DataFrame.from_dict(movies)

def predict_movie_results():
    return sentiment_prediction(df_movies)


def write():
    st.title("Dashboard")

    filter_component()

    df_movie_results = predict_movie_results()
    for index, movie in df_movie_results.iterrows():
        movie_component(movie, index)
