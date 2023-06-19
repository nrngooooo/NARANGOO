from django.urls import path
from workerApp import views

urlpatterns = [
    path('worker/', views.worker, name='ajiltan' ),
    path('create/', views.worker_add, name='ajiltan_nemeh'),
    path('edit/<int:id>', views.edit_worker, name='worker_edit'),
    path('delete/<int:id>', views.delete_worker, name='worker_delete'),
]