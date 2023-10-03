from django.db import models

from webapps.oluwa.models.profileModel import UserProfile


class SiteInfoModel(models.Model):
    backgroundVideo = models.FileField(max_length=500)
    videoCaption = models.CharField(max_length=100)
    siteTitle = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    seo = models.CharField(max_length=255)
    footerContent = models.TextField()
    topNote = models.TextField()
    
    def __str__(self):
        return self.name

    class Meta:
        app_label = "oluwa"
