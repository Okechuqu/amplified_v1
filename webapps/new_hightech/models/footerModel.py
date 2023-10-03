from django.db import models
# Create your models here.


class Footer(models.Model):
    instagram_handle = models.URLField(blank=True, null=True)
    facebook_handle = models.URLField(blank=True, null=True)
    linkedin_handle = models.URLField(blank=True, null=True)
    twitter_handle = models.URLField(blank=True, null=True)
    github_handle = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=35, default='New')
    img = models.ImageField(upload_to='media/img', default=0)
    siteName = models.CharField(max_length=35)
    note = models.CharField(max_length=35)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta: 
        app_label = 'new_hightech'
        verbose_name = 'foot'
        verbose_name_plural = 'footer'
