import os
import youtube_dl
import ffmpeg
#import django
#django.setup()

VIDEO_DOWNLOAD_PATH = '.\.'  # 다운로드 경로

def download_video_and_subtitle(output_dir, youtube_video_list):

    download_path = os.path.join(output_dir, '%(id)s-%(title)s.%(ext)s')

    for video_url in youtube_video_list:

        # youtube_dl options
        ydl_opts = {
            'format': 'bestaudio/worst',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
            'outtmpl': download_path, # 다운로드 경로 설정
            'start_time':'0', #이건 안되네요 ㅜ
            'end_time':'300', #이건 안되네요 ㅜ
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        except Exception as e:
            print('error', e)

if __name__ == '__main__':  
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soobiz.settings')
    #django.setup()
    #download_video_and_subtitle(output_dir, youtube_video_list)
    youtube_url_list = ['https://www.twitch.tv/videos/794842555']
    download_video_and_subtitle(VIDEO_DOWNLOAD_PATH, youtube_url_list)