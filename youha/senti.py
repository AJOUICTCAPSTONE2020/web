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


class sentiment_analysis():
    

    def extract(video_id):

        engine = create_engine("mysql+pymysql://admin:soobiz2020@soobiz-1.caac1nulptmh.ap-northeast-2.rds.amazonaws.com:3306/ict-master",encoding='utf-8-sig')
        conn = engine.connect()
        db=pymysql.connect(host="soobiz-1.caac1nulptmh.ap-northeast-2.rds.amazonaws.com",port=3306,user="admin",passwd="soobiz2020",db="ict-master",charset='utf8')
        db_name = str(video_id) + ".txt"
        query_result = pd.read_sql(db_name,conn)

        db_list=[]
        for index, row in query_result.iterrows():
            try:
                db_list.append([int(float(row.timeline)),str(row.chat)])
            except ValueError:
                continue

        chat_list=[]
        for i in range(len(db_list)):
            chat_list.append(db_list[i][1])
        
        text = []
        y = []
        twitter_tag = Okt()
        with open('./sentiment_models/chat_746785184_labeling.csv', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader: 
                if row: 
                    text.append(row[0]) 
                    y.append(row[1]) 

        X_train, X_test, y_train, y_test = train_test_split(text, y,test_size=0.01,random_state=0)
        tfidf = TfidfVectorizer(tokenizer=twitter_tag.morphs, min_df=2)
        X_train_tfidf = tfidf.fit_transform(X_train)
        X_test_tfidf = tfidf.transform(chat_list)
        clf = LogisticRegression()
        clf.fit(X_train_tfidf, y_train)

        print(clf.predict(X_test_tfidf))
    




       