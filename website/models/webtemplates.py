from django.db import models
from core.core import CoreBaseModel

class WebTemplate(CoreBaseModel):
    path = models.CharField(max_length=300)
    name = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=300, null=True, blank=True)
    version = models.CharField(max_length=150, null=True, blank=True)
    message = models.CharField(max_length=150, null=True, blank=True)
    is_activated = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Web Manager'
        verbose_name_plural = 'Web Managers'

    def __str__(self) -> str:
        return f"{self.name}"
