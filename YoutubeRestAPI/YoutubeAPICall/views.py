from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import VideoSerializer
from .models import Video
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import VideoLimitOffsetPagination

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by("PublishedOn")
    serializer_class = VideoSerializer
    pagination_class = VideoLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title','description']
