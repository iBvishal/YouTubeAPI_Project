from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title','description','thumbnailURL','PublishedOn','timeStamp']
    list_filter = ['title','description','PublishedOn','timeStamp']
    search_fields = ['title','description']

# Register your models here.
admin.site.register(Video, VideoAdmin)