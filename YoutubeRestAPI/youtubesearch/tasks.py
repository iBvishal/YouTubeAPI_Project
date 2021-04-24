from celery import task 
from celery import shared_task 

import argparse
import requests

DEVELOPER_KEY = 'AIzaSyCGhwD9FguAyV-qguQP8P6ikfFoJZ22pbk'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


@shared_task
def testing():
    print('hola')

# @shared_task
# def fetch_youtube_videos():
#     search_url = 'https://www.googleapis.com/youtube/v3/search'
#     video_url = 'https://www.googleapis.com/youtube/v3/videos'
#     videos = []
#     search_params = {
#         'part' : 'snippet',
#         'q' : 'football',
#         'key' : DEVELOPER_KEY,
#         'maxResults' : 30,
#         'type' : 'video'
#     }
#     result = requests.get(search_url, params=search_params)
#     result1 = result.json()['items']

#     for search_result in result1:
#         Video = {
#             'videoID' : search_result['id']['videoId'],
#             'ChannelTitle' : search_result['snippet']['channelId'],
#             'title' : search_result['snippet']['title'],
#             'description' : search_result['snippet']['description'],
#             'thumbnailURL' : search_result['snippet']['thumbnails']['high']['url'],
#             'PublishedOn' : search_result['snippet']['publishedAt']
#         }
#         print(Video)
#         videos.append(Video)