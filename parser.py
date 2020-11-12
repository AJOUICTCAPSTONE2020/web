from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soobiz.settings")
import django
django.setup()
from react.models import TwitchData, TwitchChapter

def parse_twitch():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.twitch.tv/videos/790509580')
    driver.implicitly_wait(3)

    tt=driver.find_element_by_css_selector('#root > div > div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-full-height > div > main > div.root-scrollable.scrollable-area.scrollable-area--suppress-scroll-x > div.simplebar-scroll-content > div > div > div.channel-root.channel-root--watch.channel-root--unanimated > div.tw-flex.tw-flex-column > div.channel-root__info.channel-root__info--offline > div > div.tw-flex-grow-0.tw-flex-shrink-1 > div > div.metadata-layout__split-top.tw-border-b.tw-flex.tw-justify-content-between.tw-mg-x-1.tw-pd-y-1 > div:nth-child(1) > h2')
    nm=driver.find_element_by_css_selector('#root > div > div.tw-flex.tw-flex-column.tw-flex-nowrap.tw-full-height > div > main > div.root-scrollable.scrollable-area.scrollable-area--suppress-scroll-x > div.simplebar-scroll-content > div > div > div.channel-root.channel-root--watch.channel-root--unanimated > div.tw-flex.tw-flex-column > div.channel-root__info.channel-root__info--offline > div > div.tw-flex-grow-0.tw-flex-shrink-1 > div > div.tw-flex.tw-justify-content-between.tw-relative > div > div.tw-flex.tw-flex-column.tw-full-width.tw-pd-x-1 > div.metadata-layout__support.tw-align-items-baseline.tw-flex.tw-flex-wrap-reverse.tw-justify-content-between > div.tw-align-items-center.tw-flex > a > h1')

    chapter_no=1
    chapter_name = []
    chapter_time = []
    while(True):
        try:
            selected_tag_a=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[6]/div/div[2]/div[1]/div[2]/div[2]')
            selected_tag_a.click()
            while(True):
                try:
                    chapter_name.append(driver.find_element_by_css_selector('#chapter-select-popover-body > div:nth-child('+str(chapter_no)+') > button > div > div.tw-flex.tw-flex-column.tw-flex-grow-1.tw-flex-shrink-1.tw-pd-l-1.tw-pd-t-1 > div.media-row__info-text > p').text)
                    chapter_time.append(driver.find_element_by_css_selector('#chapter-select-popover-body > div:nth-child('+str(chapter_no)+') > button > div > div.tw-flex.tw-flex-column.tw-flex-grow-1.tw-flex-shrink-1.tw-pd-l-1.tw-pd-t-1 > div.media-row__info-description > p').text)
                    chapter_no+=1
                except NoSuchElementException:
                    break

                reshaped_chapter_time = []
                reshaped_chapter_time.append(0)
                for i in range(len(chapter_time)):
                    chapter_time[0]=chapter_time[0].replace(" 남음","")
                    if chapter_time[i].find("시간") != -1: 
                        chapter_time[i] = chapter_time[i].replace("시간",":").replace("분",":").replace(" ","")
                        chapter_time[i] = chapter_time[i]+"00"
                        
                    else:
                        chapter_time[i] = "00:"+chapter_time[i]
                        chapter_time[i] = chapter_time[i].replace("초","").replace("분",":").replace(" ","")
                    #print(chapter_time[i])
                    tmp = chapter_time[i].split(":")
                    #print(tmp)
                    hour = int(tmp[0])
                    minute = int(tmp[1])
                    second= int(tmp[2])
                    time = hour*3600 + minute*60 + second
                    reshaped_chapter_time.append(reshaped_chapter_time[i]+time)
        except NoSuchElementException:
            break

    for i in range(len(tt.text)):
        if tt.text[i]=='•':
            end = i
    data = [
        tt.text[:end],
        nm.text,
        chapter_name,
        reshaped_chapter_time,
    ]
    return data

 
TwitchData(title=parse_twitch()[0], name=parse_twitch()[1]).save()
TwitchChapter(chaptername=parse_twitch()[2], chaptertime=parse_twitch()[3]).save()