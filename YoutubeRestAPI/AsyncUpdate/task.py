import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# from YoutubeAPICall.models import Video

def youtube_search():
    pass
    # DEVELOPER_KEY = 'AIzaSyDMGaY_kIHI7wG3SozMFY3LtJwU3EYzd4k'
    
    # search_url = 'https://www.googleapis.com/youtube/v3/search'
    # video_url = 'https://www.googleapis.com/youtube/v3/videos'
    
    # search_params = {
    #     'part' : 'snippet',
    #     'q' : 'search',
    #     'key' : DEVELOPER_KEY,
    #     'maxResults' : 10,
    #     'type' : 'video'
    # }

    # r = get(search_url, params=search_params)

    # results = r.json()['items']

    # videos = []
    # for result in results:
    #     video_data = {
    #         'title' : result['snippet']['title'],
    #         'id' : result['id'],
    #         'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
    #         'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
    #         'thumbnail' : result['snippet']['thumbnails']['high']['url']
    #     }
    #     videos.append(video_data)
    
    # print(videos)
    # for search_result in results:
    #     # Video.ChannelTitle = search_result['channelId']
    #     # Video.description = search_result['channelId']
    #     # Video.PublishedOn = search_result['PublishedOn']
    #     # Video.thumbnailURL = search_result['thumbnailURL']
    #     # Video.videoID = search_result['videoID']
    #     # Video.title = search_result['Title']
        
    #     print(search_result['channelId'])
    #     print(search_result['channelId'])
    #     print(search_result['PublishedOn'])
    #     print(search_result['thumbnailURL'])
    #     print(search_result['videoID'])
    #     print(search_result['Title'])

youtube_search()