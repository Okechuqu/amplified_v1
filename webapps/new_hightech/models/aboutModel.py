from django.db import models
from PIL import Image
# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=35,default='New')
    img = models.ImageField(upload_to='media/img')
    fullContent = models.TextField(blank=True,null=True)
    content = models.TextField()
    
    def __str__(self):
        return self.name


    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'about'