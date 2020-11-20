import streamlit as st


def filter_component():
    st.write("Search and Filter")
    cols = st.beta_columns(3)
    cols[0].text_input("Filter by Title")
    cols[1].multiselect("Filter by People", ["Person 1", "Person 2", "Person 3"])
    cols[2].slider('Filter by Score', 70, 100)

    st.button("Filter")
