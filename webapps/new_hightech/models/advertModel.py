from django.db import models

class Advertisement(models.Model):
    name = models.CharField(max_length=20)
    adLink = models.URLField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'Advert'
        verbose_name_plural = 'Adverts'
