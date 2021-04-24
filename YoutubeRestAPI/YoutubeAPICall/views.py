from django.shortcuts import render

from rest_framework import viewsets
from .serializers import VideoSerializer
from .models import Video

from .pagination import VideoLimitOffsetPagination

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('PublishedOn')
    search_fields = ['title','description','PublishedOn']

    pagination_class = VideoLimitOffsetPagination

    serializer_class = VideoSerializer
