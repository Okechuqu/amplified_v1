from django.db import models
import uuid


class CoreBaseModel(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    created = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'Core'
        verbose_name_plural = 'Cores'
