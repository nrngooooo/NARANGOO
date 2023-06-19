from django.urls import path
from bagshApp import views

urlpatterns = [
    path('', views.bagsh, name='bagsh'),
    path('create/', views.bagsh_add, name='create'),
    path('edit/<int:id>', views.bagsh_edit, name='update'),
    path('delete/<int:pk>', views.bagsh_delete,name='remove'),
]
