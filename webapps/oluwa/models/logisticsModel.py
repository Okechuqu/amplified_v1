from django.db import models

from webapps.oluwa.models.profileModel import Unit


# Equipment Management
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/oluwa')
    serial_number = models.CharField(max_length=50, unique=True)
    # maintenance_logs = models.TextField()
    service_history = models.TextField()
    responsible_unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        app_label = "oluwa"