from django.db import models


class ContactInfo(models.Model):
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField()
    streetAddress = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    
    class Meta:
        app_label = 'oluwa'
        verbose_name = 'contact'
        verbose_name_plural = 'contact_info'
        