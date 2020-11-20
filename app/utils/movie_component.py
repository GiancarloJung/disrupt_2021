import streamlit as st
import matplotlib.pyplot as plt

from app.models.metascore import metascore_predicition

def movie_component(movie, index):
    X_train, y_train, result = metascore_predicition()
    col1, col2 = st.beta_columns((2, 1))

    with col1:
        st.header(movie['title'])
        st.write(movie['description'])
        st.write(', '.join(movie["people"]))

    with col2:
        st.subheader("Success Score")
        st.header(movie['movie_score'])
        view_analysis = st.checkbox("View Analysis", key=index)

    if view_analysis:
        sentiment_expander = st.beta_expander("Review Sentiment Analysis")
        with sentiment_expander:
            cols = st.beta_columns((1, 3, 3, 1))
            with cols[1]:
                st.title(movie['sentiment'])

            with cols[2]:
                st.write(movie['review'])

        metascore_expander = st.beta_expander("Metascore Analysis")
        with metascore_expander:
            cols = st.beta_columns((1, 3, 3, 1))
            with cols[1]:
                st.title('Metascore')
                st.write("Metascore is considered the rating of a film. Scores are assigned to movie's reviews of large group of the world's most respected critics, and weighted average are applied to summarize their opinions range. The result is shown in single number that captures the essence of critical opinion in one Metascore.")

            with cols[2]:
                plot_graph(X_train, y_train, result)


def plot_graph(X_train, y_train, result):
    plt.scatter(X_train, y_train, c='green')
    plt.plot(X_train, result, c='black')
    plt.title('MetaScore x Rating (Training Set)')
    fig = plt.show()

    st.pyplot(fig)
