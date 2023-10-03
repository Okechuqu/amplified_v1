from django.db import models
from django.contrib.auth.models import User


# User Profile for Military Personnel
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=50)
    service_branch = models.CharField(max_length=100)
    security_clearance = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    service_history = models.TextField()
    awards_and_decorations = models.TextField()

    class Meta:
        app_label = "oluwa"

# Units and Subunits
class Unit(models.Model):
    name = models.CharField(max_length=100)
    parent_unit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    deployment_history = models.TextField()
    personnel = models.ManyToManyField(UserProfile, related_name='assigned_units')
    
    class Meta:
        app_label = "oluwa"

# Soldier Details
class Soldier(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    medical_records = models.TextField()
    training_history = models.TextField()
    current_assignment = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        app_label = "oluwa"