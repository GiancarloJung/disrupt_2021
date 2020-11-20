import streamlit as st

import numpy as np
import pandas as pd
import seaborn as sns
from gensim.parsing.preprocessing import remove_stopwords

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize.toktok import ToktokTokenizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import  accuracy_score

import re, string, unicodedata

nltk.download('stopwords')

class SentimentRegressor():
    tk = ToktokTokenizer()
    tf = TfidfVectorizer(min_df=0, max_df=1, use_idf=True, ngram_range=(1,3))
    regressor = LogisticRegression(penalty='l2', max_iter=400, C=1, random_state=42)

    def __init__(self, reviews, sentiments):
        self.x = reviews
        self.y = sentiments
        self.stopwords = set(stopwords.words('english'))


    def pre_process(self):
        X_train, X_test, y_train, y_test = train_test_split(self.x, self.y, test_size = 0.333, random_state = 0)

        X_train = X_train.apply(clean_content)
        X_test = X_test.apply(clean_content)

        X_train = X_train.apply(stemmer)
        X_test = X_test.apply(stemmer)

        X_train = X_train.apply(remove_with_gensim)
        X_test = X_test.apply(remove_with_gensim)

        return X_train, X_test, y_train, y_test


    def train(self, X_train, X_test, y_train, y_test):
        train_reviews = self.tf.fit_transform(X_train)
        test_reviews = self.tf.transform(X_test)

        self.regressor.fit(train_reviews, y_train)
        prediction = self.regressor.predict(test_reviews)
        score = accuracy_score(y_test, prediction)

        return prediction, score


    def predict(self, reviews):
        reviews = self.tf.transform(reviews)
        prediction = self.regressor.predict(reviews)

        return prediction


def strip_html(text):
    clean = re.compile('<.*?>')

    return re.sub(clean, '', text)


def remove_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)


def clean_character(text):
    pattern = r'[^a-zA-z0-9\s]'

    return re.sub(pattern,'',text)


def clean_content(text):
    text = strip_html(text)
    text = remove_square_brackets(text)
    text = clean_character(text)

    return text


def stemmer(text):
    port = PorterStemmer()
    text = ' '.join([port.stem(word) for word in text.split()])

    return text


def remove_with_gensim(text):
    return remove_stopwords(text)

@st.cache
def sentiment_prediction(df_movies):
    df = pd.read_csv('./data/IMDB-Review.csv')
    reviews = df['review'][:2000]
    sentiments = df['sentiment'][:2000]

    regressor = SentimentRegressor(reviews, sentiments)
    X_train, X_test, y_train, y_test = regressor.pre_process()
    trained_prediction, score = regressor.train(X_train, X_test, y_train, y_test)

    df_movies['sentiment'] = regressor.predict(df_movies.review)

    return df_movies
