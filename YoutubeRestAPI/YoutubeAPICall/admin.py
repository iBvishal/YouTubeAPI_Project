from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ['videoID', 'ChannelTitle', 'title','description','thumbnailURL','PublishedOn','timeStamp']
    list_filter = ['title', 'ChannelTitle', 'description','PublishedOn','timeStamp']
    search_fields = ['title', 'ChannelTitle', 'description']

# Register your models here.
admin.site.register(Video, VideoAdmin)