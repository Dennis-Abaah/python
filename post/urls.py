from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post', views.create_post, name='create_post'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user_posts', views.user_posts, name='user_posts'),
]
