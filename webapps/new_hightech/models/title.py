from django.db import models


class TitleModel(models.Model):
    favicon = models.ImageField(upload_to='favicon', blank=True, null=True)
    testimonySubTitle = models.CharField(max_length=150, blank=True, null=True)
    contactSubTitle = models.CharField(max_length=150, blank=True, null=True)
    projectSubTitle = models.CharField(max_length=150, blank=True, null=True)
    serviceSubTitle = models.CharField(max_length=150, blank=True, null=True)
    testimonyTitle = models.CharField(max_length=170, blank=True, null=True)
    footerSubTitle = models.CharField(max_length=150, blank=True, null=True)
    aboutSubTitle = models.CharField(max_length=150, blank=True, null=True)
    staffSubTitle = models.CharField(max_length=150, blank=True, null=True)
    studentTitle = models.CharField(max_length=170, blank=True, null=True)
    blogSubTitle = models.CharField(max_length=150, blank=True, null=True)
    contactTitle = models.CharField(max_length=170, blank=True, null=True)
    projectTitle = models.CharField(max_length=170, blank=True, null=True)
    serviceTitle = models.CharField(max_length=170, blank=True, null=True)
    privacyTitle = models.CharField(max_length=170, blank=True, null=True)
    searchTitle = models.CharField(max_length=150, blank=True, null=True)
    footerTitle = models.CharField(max_length=170, blank=True, null=True)
    staffTitle = models.CharField(max_length=170, blank=True, null=True)
    aboutTitle = models.CharField(max_length=170, blank=True, null=True)
    termsTitle = models.CharField(max_length=170, blank=True, null=True)
    pageTitle = models.CharField(max_length=150, blank=True, null=True)
    blogTitle = models.CharField(max_length=170, blank=True, null=True)
    faqTitle = models.CharField(max_length=170, blank=True, null=True)

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'Title'
