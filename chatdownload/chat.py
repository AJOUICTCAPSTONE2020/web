import requests
import os

os.chdir('./.')

def get_comments(video_id, initial_offset):
    filename=video_id+".txt"
    filepath = os.path.join('output', filename)
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

if __name__ == '__main__':  
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soobiz.settings')
    #django.setup()
    #download_video_and_subtitle(output_dir, youtube_video_list)
    video_id_list=('794842555')
    initial_offset=0
    get_comments(video_id_list, initial_offset)