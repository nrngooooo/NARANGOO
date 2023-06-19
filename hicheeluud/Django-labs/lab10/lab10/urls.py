from django.contrib import admin
from django.urls import path, include
from itemApp import views
from categoryApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', include('itemApp.urls')),
    path('turul/', include('categoryApp.urls')),

    path('admin/', admin.site.urls),
]