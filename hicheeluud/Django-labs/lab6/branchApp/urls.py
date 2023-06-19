from django.urls import path
from branchApp import views

urlpatterns = [
    path('', views.branch, name='salbar' ),
    path('edit/<int:id>', views.edit_branch, name='branch_edit'),
    path('delete/<int:id>', views.delete_branch, name='branch_delete'),
]