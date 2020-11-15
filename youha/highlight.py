import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import pymysql

from .models import highlightVid

class findhighlight():
    def extract(video_id,n):
        engine = create_engine("mysql+pymysql://admin:soobiz2020@soobiz-1.caac1nulptmh.ap-northeast-2.rds.amazonaws.com:3306/ict-capstone",encoding='utf-8-sig')
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
        for chat in chat_sec:
            index=chat//n
            chat_per_sec[index]+=1

        #채팅 많은 구간 
        chat_list=[]
        for i in range(len(chat_per_sec)):
            tmp=[chat_per_sec[i],i]
            chat_list.append(tmp)

        #chat_list=chat_list.sort(reverse=True)
        
        chat_list=sorted(chat_list,key=lambda x: -x[0])

        max_list=[]
        i=0
        while(True):
            if(i==len(chat_list)):
                break
            if(abs(chat_list[i][1] - chat_list[i+1][1]) ==1 ):
                
                tmp = [chat_list[i][0]+chat_list[i][1], chat_list[i][1],chat_list[i+1][1]]
                max_list.append(tmp)
                i =i +2
            else:
                tmp = [chat_list[i][0], chat_list[i][1],chat_list[i][1]]
                max_list.append(tmp)
                i=i+1


        for i in range(len(max_list)):
            if(max_list[i][1]>max_list[i][2]):
                max_list[i][1], max_list[i][2] = max_list[i][2], max_list[i][1]

        print(max_list)

        for i in range(10):
            highlightVid( start_time=max_list[i][1]*n, end_time=max_list[i][2]*n,video_id=str(video_id)).save()

