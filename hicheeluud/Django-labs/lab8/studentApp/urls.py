from django.urls import path
from studentApp import views

urlpatterns = [
    path('', views.student, name='oyutan' ),
    path('create/', views.student_add, name='create'),
    path('edit/<int:id>', views.student_edit, name='edit'),
    path('delete/<int:id>', views.student_delete, name='delete'),
]