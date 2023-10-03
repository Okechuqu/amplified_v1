from django.db import models
from PIL import Image
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=35, default='New', blank=True, null=True)
    img = models.ImageField(upload_to='media/img', blank=True, null=True)
    addressUrl = models.URLField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    
 

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

