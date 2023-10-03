from django.db import models
from webapps.oluwa.models.profileModel import UserProfile


# Training Programs and Records
class TrainingProgram(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    # trainers = models.ManyToManyField(UserProfile, related_name='trained_programs')
    # trainees = models.ManyToManyField(UserProfile, related_name='attended_programs')

    class Meta:
        app_label = "oluwa"
        