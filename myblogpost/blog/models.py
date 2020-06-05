from django.db import models
from django.views import generic
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.CharField(max_length=90, default='')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)


