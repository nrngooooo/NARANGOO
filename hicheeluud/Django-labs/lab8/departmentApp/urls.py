from django.urls import path
from departmentApp import views

urlpatterns = [
    path('', views.department, name='tenhim' ),
    path('edit/<int:id>', views.department_edit, name='edit'),
    path('delete/<int:id>', views.department_delete, name='delete'),
]