from django.contrib import admin
from django.urls import path,include
from playlist_app import views

urlpatterns = [
    path('', views.playlist_view, name='playlist'),
    path('admin/', admin.site.urls),
    path('playlist/', include('playlist_app.urls')),

]
