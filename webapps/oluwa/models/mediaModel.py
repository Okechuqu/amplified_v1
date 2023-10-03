from django.db import models




# Media and Galleries
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    class Meta:
        app_label = "oluwa"

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    images = models.ManyToManyField(Image, related_name='gallery_images')

    class Meta:
        app_label = "oluwa"