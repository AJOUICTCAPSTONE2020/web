import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soobiz.settings")
import django
django.setup()
import os
import youtube_dl
import ffmpeg
import requests

class download():
    # #import os
    # #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soobiz.settings")
    # import django
    # django.setup()
    # #import os
    # import youtube_dl
    # import ffmpeg
    # import requests
    # #import django
    # #django.setup()



    def downloader(video_id):
        #audio 다운로드 부분
        print("@")
        youtube_video_list=[]
        youtube_video_list.append('https://www.twitch.tv/videos/'+video_id)
        
        #download_path = os.path.join('.\youha\output', video_id+'.%(ext)s')
        print("시작")
        for video_url in youtube_video_list:

            # youtube_dl options
            ydl_opts = {
                
              #'format': 'bestaudio/worst',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
                'format': 'worstvideo/worst',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
                #'outtmpl': download_path, # 다운로드 경로 설정
                #'outtmpl': '.\output',
                'outtmpl': '.\youha\output\.'+video_id+'.%(ext)s',

            }

            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
                
            except Exception as e:
                print('error', e)  
        print("?")
        #chat 다운로드 부분
        initial_offset=0
        filename=video_id+".txt"
        filepath = os.path.join('.\youha\output', filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            request_headers = {'Accept': 'application/vnd.twitchtv.v5+json', 'Client-ID': 'qs5msq3whryszinfw7pt110aep84wr'}
            request_url = f'https://api.twitch.tv/v5/videos/{video_id}/comments?content_offset_seconds={initial_offset}'

            while True :
                print('request ' + request_url)
                response = requests.get(request_url, headers=request_headers).json()
                received_count = 0
            
            
                for comment in response['comments']:
                    if comment['source'] == 'chat':
                        offset = comment['content_offset_seconds']
                    
                        rem, secs = divmod(offset, 60)
                        hours, mins = divmod(rem, 60)
                        time = f'{int(hours):d}:{int(mins):02d}:{secs:06.3f}'

                        user = comment['commenter']['display_name']
                        message = comment['message']['body']

                        output = f'{offset:.3f} {time} [{user}] {message}'
                        # print(output)
                        f.write(output + '\n')

                        received_count += 1

                print(f'{received_count} comments received')
                if received_count > 0:
                    print(output)
                print()

                if '_next' not in response:
                    break

                next_cursor = response['_next']
                request_url = f'https://api.twitch.tv/v5/videos/{video_id}/comments?cursor={next_cursor}'