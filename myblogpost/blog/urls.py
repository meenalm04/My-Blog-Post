from django.urls import path, include
from . import views


urlpatterns = [
    path('about/', views.about, name='blog-about'),
    path('', views.home, name='blog-home'),
    path('post_detail/<int:id>', views.DetailView, name='blog-Detail-View' )
]
