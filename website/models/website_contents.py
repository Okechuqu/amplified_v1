from typing import Iterable, Optional
from django.db import models


class WebsiteContentForm(models.Model):
    SECTIONS = [
        ('slider', 'Slider'),
    ]
    FORM_TYPE = [
        ('text', 'Text'),
        ('date', 'Date'),
    ]

    FORM_ELEMENT = [
        ('input', 'Input'),
        ('textarea', 'Textarea'),
    ]
    app = models.CharField(max_length=150, null=True)
    pageid = models.CharField(max_length=150, null=True, choices=SECTIONS, default=SECTIONS)
    name = models.CharField(max_length=150, null=True)
    form_name = models.CharField(max_length=150, null=True, editable=False)
    form_type = models.CharField(max_length=150, null=True, choices=FORM_TYPE)
    form_element = models.CharField(max_length=150, null=True, choices=FORM_ELEMENT)
    index = models.IntegerField(default=0)


    def save(self, *args, **kwargs) -> None:
        self.form_name = str(self.name).replace(' ', '_')
        return super().save(args, kwargs)
    
    def __str__(self) -> str:
        return f"{self.name}"




class WebsiteContent(models.Model):
    app = models.CharField(max_length=150, null=True)
    pageid = models.CharField(max_length=150, null=True, default='slider')
    content = models.TextField(default={})

    class Meta:
        verbose_name = 'Web Content'
        verbose_name_plural = 'Web Contents'

    def __str__(self) -> str:
        return f"{self.app} - {self.pageid}"



NAVIGATION_LIST_DISPLAY = ['title','links','has_dropdown','is_active','order']
class Navigations(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    links = models.CharField(max_length=150, blank=True, null=True)
    has_dropdown = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField(default=1)
    is_shown = models.BooleanField(default=True, choices=[(True,'On'), (False,'Off')])

    class Meta:
        verbose_name = 'Navigation'
        verbose_name_plural = 'Navigations'

    def __str__(self) -> str:
        return f"{self.title}"


class NavigationDropdown(models.Model):
    parent =  models.ForeignKey("website.Navigations", on_delete=models.CASCADE, related_name='navigation_related')
    title = models.CharField(max_length=150)
    links = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Navigation Dropdown'
        verbose_name_plural = 'Navigation Dropdown'


