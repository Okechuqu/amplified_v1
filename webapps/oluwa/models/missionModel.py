from django.db import models
from webapps.oluwa.models.profileModel import Unit


# Mission Planning and Execution
class Mission(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="media/img")
    description = models.TextField()
    objectives = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    assigned_units = models.ManyToManyField(Unit)
    slug = models.SlugField(max_length=200)
    # mission_reports = models.TextField()
    # task_assignments = models.TextField()
    # after_action_reviews = models.TextField()

    class Meta:
        app_label = "oluwa"
