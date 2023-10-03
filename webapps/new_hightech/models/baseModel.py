from django.db import models
from PIL import Image
# Create your models here.


class Slider(models.Model):
    img = models.ImageField(upload_to='media/img', blank=True, null=True)
    title = models.CharField(max_length=70, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    description = models.TextField( blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'

class PageImage(models.Model):
    title = models.CharField(max_length=10)
    img = models.ImageField(upload_to='media/img')

    def __str__(self):
        return self.title
    
    class Meta:
        app_label = 'new_hightech'

class Fact(models.Model):
    numb = models.IntegerField()
    content = models.CharField(max_length=100)

    class Meta:
        app_label = 'new_hightech'
