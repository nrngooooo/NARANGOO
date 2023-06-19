from django.urls import path
from workerApp import views

urlpatterns = [
    path('', views.worker, name='worker' ),
]