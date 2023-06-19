from django.urls import path, include
from playlist_app import views
urlpatterns = [
    path('', views.playlist_view, name='playlist'),
    # path('play/', views.play, name='play'),
    # path('prev/', views.prev, name='prev'),
    # path('next/', views.next, name='next'),
    # path('add_song/', views.add_song, name='add_song'),

]
