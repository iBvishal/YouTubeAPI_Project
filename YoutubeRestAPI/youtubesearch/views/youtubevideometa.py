from rest_framework import status, viewsets, mixins

from youtubesearch.serializers import YoutubeVideoMetaSerializer
from youtubesearch.models import YoutubeVideoMeta

class YoutubeVideoMetaViewset(viewsets.ModelViewSet):
    queryset = YoutubeVideoMeta.objects.all()
    serializer_class = YoutubeVideoMetaSerializer