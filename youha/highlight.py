import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import pymysql
import os
from .models import highlightVid, chatFlow,TwitchChapter
from pyodbc import ProgrammingError
class findhighlight():
    def extract(video_id,chapter_name,n):
        filename=str(video_id)+".txt"
        filepath = os.path.join('.\youha\output', filename)
        #print(filepath)
        while(True):
            try:
                a=open(filepath,'r') 
       
                engine = create_engine("mysql+pymysql://admin:soobiz2020@soobiz-1.caac1nulptmh.ap-northeast-2.rds.amazonaws.com:3306/ict-master",encoding='utf-8-sig')
                conn = engine.connect()
                db=pymysql.connect(host="soobiz-1.caac1nulptmh.ap-northeast-2.rds.amazonaws.com",port=3306,user="admin",passwd="soobiz2020",db="ict-master",charset='utf8')
                db_name = str(video_id) + ".txt"

                query_result = pd.read_sql(db_name,conn)


                # 채팅 리스트 저장
                chat_sec=[]
                chat_per_sec=[]
                for index, row in query_result.iterrows():
                    try:
                        chat_sec.append(int(float(row.timeline)))
                    except ValueError:
            
                        continue

            
                last=int(chat_sec[-1])//n +1
                #print(last)
                for j in range(last):
                    chat_per_sec.append(0)
                #print(len(chat_per_sec))
                # n 초당 채팅 개수 저장
                for chat in chat_sec:
                    index=chat//n
                    if(index>=last):
                        continue
                    chat_per_sec[index]+=1

                if(chatFlow.objects.filter(video=video_id).first() ==None):
                    #print("not saved")
                    for i in range(index):
                        chatFlow(chatFlowID=str(video_id)+"_"+str(i), time=i*n, num_of_chat=chat_per_sec[i], video_id=str(video_id)).save()

            
                chapter_time=TwitchChapter.objects.filter(video=video_id , chaptername= chapter_name)

                chat_list=[]

                # if(chapter_time.count()>1):
                for cha in chapter_time:
                    start = cha.startTime
                    end = cha.endTime
                    si=start/n
                    ei =end/n
                    if(ei>0):
                        for i in range(int(si),int(ei)):
                            tmp=[chat_per_sec[i],i]
                            chat_list.append(tmp)
                    else:
                        for i in range(int(si),len(chat_per_sec)):
                            tmp=[chat_per_sec[i],i]
                            chat_list.append(tmp)
            
                # print(chat_list)


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

                if(len(max_list)<5):
                    max_list=[]
                    for i in range(len(highlight)):
                        max_list.append([highlight[i][0],highlight[i][-1]])

                if(len(max_list)<20):
                    for i in range(len(max_list)):
                        highlightVid( start_time=max_list[i][0]*n, end_time=max_list[i][1]*n+n,video_id=str(video_id),highlightID=str(video_id)+"_"+chapter_name+"_"+str(i),chapter=chapter_name).save()
                else:
                    for i in range(20):
                        highlightVid( start_time=max_list[i][0]*n, end_time=max_list[i][1]*n+n,video_id=str(video_id),highlightID=str(video_id)+"_"+chapter_name+"_"+str(i),chapter=chapter_name).save()

            except:
                continue
                
            else:
                return