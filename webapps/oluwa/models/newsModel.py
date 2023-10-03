from django.db import models
from django.contrib.auth.models import User
from webapps.oluwa.models.profileModel import UserProfile



# News and Updates
class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # comments = models.ManyToManyField('Comment', related_name='article_comments')
    images = models.ManyToManyField('Image', related_name='article_images')
    date = models.DateField()

    class Meta:
        app_label = "oluwa"

# Comment System
class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        app_label = "oluwa"