from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
import requests
import json
from .models import Post
from django.contrib.auth.models import User

# posts = json.loads(requests.get('https://jsonplaceholder.typicode.com/posts%27).text)
# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'post' : posts
    }
    return render(request, 'blog/index.html', context)
def index(request):
    return render(request, 'blog/index.html', {'title' : 'Index'})
def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

# class PostList(generic.ListView):
#     queryset = Post.objects.order_by('date_posted')
#     template_name = 'index.html'
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

 


