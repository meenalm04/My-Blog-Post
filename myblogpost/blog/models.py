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

# class Post(models.Model):
#     title = models.CharField(max_length=200, unique=True)
   
#     author = models.ForeignKey(User, on_delete= models.CASCADE)
#     updated_on = models.DateTimeField(auto_now= True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)

    # def __str__(self):
    #     return self.title
# class Blog(models.Model):
#    title = models.CharField(max_length=100, unique=True)
#    slug = models.SlugField(max_length=100, unique=True)
#    body = models.TextField()
#    posted = models.DateField(db_index=True, auto_now_add=True)
#    category = models.ForeignKey('blog.Category')

# class Category(models.Model):
#    title = models.CharField(max_length=100, db_index=True)
# slug = models.SlugField(max_length=100, db_index=True) 
