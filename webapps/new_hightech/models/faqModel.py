from django.db import models


class FAQs(models.Model):
    question = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    answer = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'faq'
        verbose_name_plural = 'faqs'