from django.urls import path
from dbApp import views

urlpatterns = [
    path('', views.branch, name='branch' ),
]