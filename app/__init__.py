import streamlit as st
from app.db import Database
import awesome_streamlit as ast
from app.pages import admin, dashboard, data_analysis


PAGES = {
    "Dashboard": dashboard,
    "Data Analysis": data_analysis,
    "Admin": admin
}

def run():
    st.set_page_config(layout="wide")

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    st.sidebar.button("Logout")

    page = PAGES[selection]

    with st.spinner(f"Loading..."):
        ast.shared.components.write_page(page)
