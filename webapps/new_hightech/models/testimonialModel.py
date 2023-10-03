from PIL import Image
from django.db import models
# Create your models here.


class Testimonial(models.Model):
    name = models.CharField(max_length=35, default='New', blank=True, null=True)
    clientProfession = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(upload_to='media/img', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5, blank=True, null=True)
    clientName = models.CharField(max_length=20, blank=True, null=True)
    feedBack = models.TextField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name


    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'testimony'
        verbose_name_plural = 'testimonial'
