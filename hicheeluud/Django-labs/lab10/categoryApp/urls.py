from django.urls import path
from categoryApp import views

urlpatterns = [
    path('', views.category_list, name='turul'),
    path('edit/<int:id>', views.category_edit, name='edit'),
    path('delete/<int:id>', views.category_delete, name='delete'),

]