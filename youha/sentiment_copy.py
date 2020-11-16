#pip install scikit-learn
#pip install konlpy
import csv
from konlpy.tag import Okt 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import joblib
from sqlalchemy import create_engine
import pymysql
import os
import pandas as pd
import numpy as np


class sent():
    if __name__ == "__main__":
        text = []
        y = []
        with open('./sentiment_models/chat_746785184_labeling.csv', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                #print(row)
                if row: #그 줄에 내용이 있는 경우에만
                    text.append(row[0]) #영화 리뷰를 text 리스트에 추가
                    y.append(row[1]) #영화이름을 text 리스트에 추가

        X_train, X_test, y_train, y_test = train_test_split(text, y,test_size=0.01,random_state=0)
        # 비율을 지정하지 않으면 75:25로 분할됨


        filepath= "./sentiment_models/sentiment_03.pkl"
        twitter_tag = Okt()
        def twit_tokenizer3(text):
            #target_tags = ['Noun', 'Verb', 'Adjective']
            twitter_tag = Okt()
            result = []
            for word, tag in twitter_tag.pos(text, norm=True, stem=True):
                result.append('/'.join([word, tag])) #단어의 품사를 구분할 수 있도록 함
            return result

        sentiment = joblib.load(filepath)


        tfidf = TfidfVectorizer(tokenizer=twit_tokenizer3, min_df=2)
        X_train_tfidf = tfidf.fit_transform(X_train)
        X_test_tfidf = tfidf.transform(X_test)


        new_test =['개웃겨 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ', '떡볶이먹고싶다','ㅠㅠㅠㅠㅠ','개못해','안녕','???']
        input_tfidf= tfidf.transform(new_test)
        test_X_clf = sentiment.predict(input_tfidf)

        print(test_X_clf)

