from django.urls import path
from staticApp import views

urlpatterns = [
path('zurag', views.zurag, name='zurag'),
path('menu', views.menu, name='menu'),
path('media', views.media, name='media'),
]