from django.contrib import admin
from django.urls import path, include
from bagshApp import views
from tenhimApp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('bagsh/', include('bagshApp.urls')),
    path('tenhim/', include('tenhimApp.urls')),
    path('admin/', admin.site.urls),
]