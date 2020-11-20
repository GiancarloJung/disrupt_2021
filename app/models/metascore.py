import streamlit as st

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

class MetascoreRegressor():
    regressor = LinearRegression()

    def __init__(self, metascore, rating):
        self.x = metascore
        self.y = rating

    def pre_process(self):
        X_train, X_test, y_train, y_test = train_test_split(self.x, self.y, test_size = 0.333, random_state = 0)

        X_train = X_train.reshape(-1,1)
        X_test = X_test.reshape(-1,1)
        y_train = y_train.reshape(-1,1)
        y_test = y_test.reshape(-1,1)

        X_train = StandardScaler().fit_transform(X_train)
        X_test = StandardScaler().fit_transform(X_test)
        y_train = StandardScaler().fit_transform(y_train)

        return X_train, X_test, y_train, y_test


    def predict(self, X_train, y_train):
        self.regressor.fit(X_train, y_train)
        prediction = self.regressor.predict(X_train)

        return prediction


@st.cache
def metascore_predicition():
    df = pd.read_csv("./data/IMDB-Movie-Data.csv")
    df = df.dropna()

    metascore = df["Metascore"][:500].values
    rating = df["Rating"][:500].values

    regressor = MetascoreRegressor(metascore, rating)
    X_train, X_test, y_train, y_test = regressor.pre_process()
    result = regressor.predict(X_train, y_train)

    return X_train, y_train, result
