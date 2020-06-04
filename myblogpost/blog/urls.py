from django.urls import path, include
from . import views


urlpatterns = [
    path('about/', views.about, name='blog-about'),
    path('', views.home, name='blog-home'),
    # path('', views.PostDetail.as_view(), name='post_detail'),
    # for looping through posts
    # path('', views.PostList.as_view(), name='home'), 
    
    # path('object.title/', views.PostDetail.as_view(), name='post_detail'),
   
    
]
