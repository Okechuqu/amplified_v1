from django.db import models

from webapps.oluwa.models.profileModel import UserProfile
from webapps.oluwa.models.mediaModel import *



# Event Management
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=15)
    attendees = models.ManyToManyField(UserProfile, related_name='attended_events')
    gallery = models.ManyToManyField('Gallery', related_name='events')

    class Meta:
        app_label = "oluwa"

