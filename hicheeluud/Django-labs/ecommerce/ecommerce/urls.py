from django.contrib import admin
from django.urls import path, include
from product_app import views

urlpatterns = [

    path('', views.index, name='index'),

    path('pro/', include('product_app.urls')),
    path('admin/', admin.site.urls),

]