from django.db import models
# Create your models here.


class Service(models.Model):

    icon = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField(max_length=120, blank=True, null=True)
    fullContent = models.TextField(blank=True, null=True)
    slug = models.SlugField(default='', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
 
    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'service'
        verbose_name_plural = 'services'
