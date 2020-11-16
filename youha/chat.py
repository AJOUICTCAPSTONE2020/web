import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soobiz.settings")
import django
django.setup()
from .models import chatFlow
import mysql.connector

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import pymysql

class findChat():

    def extract(video_id, n):
        engine = create_engine("mysql+pymysql://admin:soobiz2020@soobiz-1.caac1nulptmh.ap-northeast-2.rds.amazonaws.com:3306/ict-master",encoding='utf-8-sig')
        conn = engine.connect()

        db_name = str(video_id) + ".txt"

        query_result = pd.read_sql(db_name,conn)

        print(query_result)
        
        # 채팅 리스트 저장
        chat_sec=[]
        chat_per_sec=[]
        for index, row in query_result.iterrows():
            chat_sec.append(int(float(row.timeline)))

        last=int(chat_sec[-1])//n +1
        for j in range(last):
            chat_per_sec.append(0)

        # n 초당 채팅 개수 저장
        for chats in chat_sec:
            index=chats//n
            chat_per_sec[index]+=1

        # print(index)
        # print(chat_per_sec)

        for i in range(index):
            chatFlow(chatFlowID=str(video_id)+"_"+str(i), time=i, num_of_chat=chat_per_sec[i], video_id=str(video_id)).save()