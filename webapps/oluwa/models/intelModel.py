from django.db import models

from webapps.oluwa.models.profileModel import UserProfile




# Intelligence and Analysis
class IntelligenceReport(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    source = models.CharField(max_length=200, null=True, blank=True)
    classification = models.CharField(max_length=50, null=True, blank=True)
    # author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        app_label = "oluwa"