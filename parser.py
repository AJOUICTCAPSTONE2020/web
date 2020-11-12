from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soobiz.settings")
import django
django.setup()
from youha.models import originalVid, TwitchChapter
from datetime import datetime, timedelta
import mysql.connector

mydb = mysql.connector.connect(
    host = 'soobiz-1.caac1nulptmh.ap-northeast-2.rds.amazonaws.com', 
    user = 'admin', 
    password = 'soobiz2020',
    database = 'youha'
)

url = '787627853'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

def parse_twitch():
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.maximize_window()
    driver.get('https://www.twitch.tv/videos/'+url)
    driver.implicitly_wait(5)

    tt=driver.find_element_by_css_selector('#root > div > div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-full-height > div > main > div.root-scrollable.scrollable-area.scrollable-area--suppress-scroll-x > div.simplebar-scroll-content > div > div > div.channel-root.channel-root--watch-chat.channel-root--watch.channel-root--unanimated > div.channel-root__main--with-chat.tw-flex.tw-flex-column > div.channel-root__info.channel-root__info--offline.channel-root__info--with-chat > div > div.tw-flex-grow-0.tw-flex-shrink-1 > div > div.metadata-layout__split-top.tw-border-b.tw-flex.tw-justify-content-between.tw-mg-x-1.tw-pd-y-1 > div:nth-child(1) > h2')
    nm=driver.find_element_by_css_selector('#root > div > div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-full-height > div > main > div.root-scrollable.scrollable-area.scrollable-area--suppress-scroll-x > div.simplebar-scroll-content > div > div > div.channel-root.channel-root--watch-chat.channel-root--watch.channel-root--unanimated > div.channel-root__main--with-chat.tw-flex.tw-flex-column > div.channel-root__info.channel-root__info--offline.channel-root__info--with-chat > div > div.tw-flex-grow-0.tw-flex-shrink-1 > div > div.tw-flex.tw-justify-content-between.tw-relative > div > div.tw-flex.tw-flex-column.tw-full-width.tw-pd-x-1 > div.metadata-layout__support.tw-align-items-baseline.tw-flex.tw-flex-wrap-reverse.tw-justify-content-between > div.tw-align-items-center.tw-flex > a > h1')

    chapter_no=1
    chapter_name = []
    chapter_time = []
    reshaped_chapter_time = []
    chapter_list = []


    selected_tag_a=driver.find_element_by_css_selector('#root > div > div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-full-height > div > main > div.root-scrollable.scrollable-area.scrollable-area--suppress-scroll-x > div.simplebar-scroll-content > div > div > div.persistent-player > div > div.video-player > div > div > div > div:nth-child(5) > div > div.tw-flex.tw-mg-b-1.tw-mg-l-1.tw-mg-r-1 > div.player-controls__left-control-group.tw-align-items-center.tw-flex.tw-flex-grow-1.tw-justify-content-start > div:nth-child(2) > div.tw-inline-flex.tw-relative.tw-tooltip-wrapper > button > span > div > div > div > svg > g > path')
    selected_tag_a.click()
    while(True):
        try:
            chapter_name.append(driver.find_element_by_css_selector('#chapter-select-popover-body > div:nth-child('+str(chapter_no)+') > button > div > div.tw-flex.tw-flex-column.tw-flex-grow-1.tw-flex-shrink-1.tw-pd-l-1.tw-pd-t-1 > div.media-row__info-text > p').text)
            chapter_time.append(driver.find_element_by_css_selector('#chapter-select-popover-body > div:nth-child('+str(chapter_no)+') > button > div > div.tw-flex.tw-flex-column.tw-flex-grow-1.tw-flex-shrink-1.tw-pd-l-1.tw-pd-t-1 > div.media-row__info-description > p').text)
            chapter_no+=1
        except NoSuchElementException:
            break

    reshaped_chapter_time.append(0)

    for i in range(len(chapter_time)):

        chapter_time[0]=chapter_time[0].replace(" 남음","")
        if chapter_time[i].find("시간") == -1: 
            chapter_time[i] = "00:"+chapter_time[i]
            chapter_time[i] = chapter_time[i].replace("초","").replace("분",":").replace(" ","")
    
            
        else:
            if chapter_time[i].find("분") == -1:
                chapter_time[i] = chapter_time[i].replace("시간",":")
                chapter_time[i] = chapter_time[i]+"00:00"
            else:
                chapter_time[i] = chapter_time[i].replace("시간",":").replace("분",":").replace(" ","")

                chapter_time[i] = chapter_time[i]+"00"

        tmp = chapter_time[i].split(":")
        hour = int(tmp[0])
        minute = int(tmp[1])
        second= int(tmp[2])
        time = hour*3600 + minute*60 + second
        reshaped_chapter_time.append(reshaped_chapter_time[i]+time)


    for i in range(len(tt.text)):
        if tt.text[i]=='•':
            end = i

    time2=datetime.now()
    tm=tt.text[end+2:][0]
    try:
        rs_tm=time2 + timedelta(days=-int(tm))
    except ValueError:
        rs_tm=time2 + timedelta(days=-1)
    rs_time=rs_tm.strftime('%Y-%m-%d')

    for i in range(len(chapter_name)):
        chapter_list.append([chapter_name[i],reshaped_chapter_time[i]])

    data = [
        tt.text[:end],
        nm.text,
        rs_time,
        chapter_list,
    ]

    print(data)
    return data


data = parse_twitch()

originalVid(video_url=url, title=data[0], name=data[1], date=data[2]).save()
#for i in range(len(data[3])):
#    TwitchChapter(chaptername=data[3][i][0], chaptertime=data[3][i][1]).save()

val=[]
for i in range(len(data[3])):
    val.append((data[3][i][0],data[3][i][1],url))

print(val)
mycursor = mydb.cursor()

sql = "INSERT INTO youha_twitchchapter (chaptername, chaptertime, video_id) VALUES (%s, %s, %s)"

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record was inserted")