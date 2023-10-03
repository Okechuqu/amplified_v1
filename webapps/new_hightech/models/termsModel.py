from django.db import models

 
class TermsAndCondition(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    introduction = models.TextField(max_length=550, blank=True, null=True)
    use_of_site = models.TextField(max_length=550, blank=True, null=True)
    intel_property = models.TextField(max_length=550, blank=True, null=True)
    user_content = models.TextField(max_length=550, blank=True, null=True)
    liability = models.TextField(max_length=550, blank=True, null=True)
    indemnification = models.TextField(max_length=550, blank=True, null=True)
    modification = models.TextField(max_length=550, blank=True, null=True)
    law = models.TextField(max_length=550, blank=True, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'Term'
        verbose_name_plural = 'Our Terms'