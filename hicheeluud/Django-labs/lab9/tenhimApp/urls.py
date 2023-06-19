from django.urls import path
from tenhimApp import views

urlpatterns = [
    path('', views.tenhim, name='tenhim'),
    path('create/', views.tenhim_add, name='create'),
    path('edit/<int:id>', views.tenhim_edit, name='edit'),
    path('delete/<int:pk>', views.tenhim_delete,name='delete'),
]
