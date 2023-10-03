from django.db import models

class PressRelease(models.Model):
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        app_label = 'oluwa'