import uuid
from django.db import models
from django.utils.timezone import now
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=1023)
    description = models.TextField()
    thumbnailURL = models.URLField(max_length = 200)
    
    #when this record was published on Youtube
    PublishedOn = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    
    #When this record was added to our db
    timeStamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    
    #Show Title 
    def __str__(self):
        return self.title
    
    #Indexing unique_id and publishedOn in desc 
    # class Meta:
    #     indexes = [
    #         models.Index(fields=['-PublishedOn']),
    #     ]