import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import pymysql

from .models import highlightVid

class findhighlight():
    def extract(video_id,n):
        engine = create_engine("mysql+pymysql://admin:soobiz2020@soobiz-1.caac1nulptmh.ap-northeast-2.rds.amazonaws.com:3306/ict-master",encoding='utf-8-sig')
        conn = engine.connect()
        db=pymysql.connect(host="soobiz-1.caac1nulptmh.ap-northeast-2.rds.amazonaws.com",port=3306,user="admin",passwd="soobiz2020",db="ict-master",charset='utf8')
        db_name = str(video_id) + ".txt"

        query_result = pd.read_sql(db_name,conn)



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

        start= 2520
        end = 7920

        si=start/n
        ei =end/n

        print(len(chat_per_sec))
        print(si)
        print(ei)
        #채팅 많은 구간 
        chat_list=[]
        for i in range(int(si),int(ei)+n):
            tmp=[chat_per_sec[i],i]
            chat_list.append(tmp)

        print(chat_list)


        #chat_list=chat_list.sort(reverse=True)
        
        chat_list=sorted(chat_list,key=lambda x: -x[0])

        chat_list2 = chat_list[0:len(chat_list)//5]
        chat2=[]
        for i in range(len(chat_list2)):
            chat2.append([chat_list2[i][1]])

        highlight=[]
        while(len(chat2) != 0):
            while True:

                flag=0
                i=0
                del_list=[]
                for j in range(len(chat2)-1):

                    if(abs(chat2[i][0]-chat2[j+1][0])==1 or abs(chat2[i][-1]-chat2[j+1][0])==1):
                        flag=1
                        chat2[i].append(chat2[j+1][0])
                        del_list.append([chat2[j+1][0]])

                for j in range(len(del_list)):
                    chat2.remove(del_list[j])

                for j in range(len(chat2)):
                    chat2[j].sort()
                i+=1
                if(flag==0):
                    break
            highlight.append(chat2[0])
            del chat2[0]

        max_list=[]
        for i in range(len(highlight)):
            if(len(highlight[i])>1):
                max_list.append([highlight[i][0],highlight[i][-1]])

        if(len(max_list)<20):
            for i in range(len(max_list)):
                highlightVid( start_time=max_list[i][0]*n, end_time=max_list[i][1]*n+n,video_id=str(video_id),highlightID=str(video_id)+"_"+str(i)).save()
        else:
            for i in range(20):
                highlightVid( start_time=max_list[i][0]*n, end_time=max_list[i][1]*n+n,video_id=str(video_id),highlightID=str(video_id)+"_"+str(i)).save()
