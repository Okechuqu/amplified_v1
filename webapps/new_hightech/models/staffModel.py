from PIL import Image
from django.core.exceptions import ValidationError
from django.db import models
# Create your models here.


class Position(models.Model):
    name = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=50, default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        app_label = 'new_hightech'


class Staff(models.Model):
    position = models.ForeignKey('new_hightech.Position', on_delete=models.CASCADE)
    instagram_handle = models.URLField(blank=True, null=True)
    linkedin_handle = models.URLField(blank=True, null=True)
    facebook_handle = models.URLField(blank=True, null=True)
    twitter_handle = models.URLField(blank=True, null=True)
    github_handle = models.URLField(blank=True, null=True)
    img = models.ImageField(upload_to='media/img')
    is_active = models.BooleanField(default=True)
    fullName = models.CharField(max_length=100)

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'staff'
        verbose_name_plural = 'personel'

    def __str__(self):
        return self.fullName

