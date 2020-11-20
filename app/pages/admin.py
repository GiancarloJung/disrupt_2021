import streamlit as st
from app.db import Database
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np



def write():
    st.title("Admin")

    st.markdown(
        """
        This page will be used to add new movies to the list of movies to analise
        """
    )
