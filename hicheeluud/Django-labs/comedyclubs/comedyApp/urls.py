from django.urls import path
from comedyApp import views

app_name = 'comedyApp'

urlpatterns = [
    path('', views.ClubListView.as_view(), name='list'),
    path('<pk>/', views.ClubDetailView.as_view(),name='detail'),

]