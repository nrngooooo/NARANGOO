from django.urls import path
from jobApp import views
urlpatterns = [
    path('job', views.job, name='job'),
    path('jobHelp', views.jobHelp, name='jobHelp'),
]