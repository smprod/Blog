from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('posts/', views.post, name="posts"),
    path('about/', views.about, name="about"),
    path('posts/<slug:post_slug>/', views.show_post, name="post")
]
