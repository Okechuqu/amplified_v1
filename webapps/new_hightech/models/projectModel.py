from django.db import models
from PIL import Image
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=35, default='New', blank=True, null=True)
    img = models.ImageField(upload_to='media/img', blank=True, null=True)
    projectName = models.CharField(max_length=20, blank=True, null=True)
    context = models.CharField(max_length=50, blank=True, null=True)
    fullContent = models.TextField(blank=True, null=True)
    slug = models.SlugField(default='', max_length=120, blank=True, null=True)
    
    def __str__(self):
        return self.name

 

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'project'
        verbose_name_plural = 'projects'
