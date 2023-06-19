from django.urls import path
from clubApp import views

app_name = 'clubApp'

urlpatterns = [
    path('', views.ClubListView.as_view(), name='list'),
    path('<pk>/', views.ClubDetailView.as_view(),name='detail'),
    path('create/<pk>', views.ClubCreateView.as_view(), name='create'),
    path('update/<pk>/', views.ClubUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.ClubDeleteView.as_view(), name='delete'),
]