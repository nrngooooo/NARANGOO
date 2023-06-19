from django.urls import path
from itemApp import views

urlpatterns = [
    path('', views.item_list, name='items'),
    path('edit/<int:id>', views.item_edit, name='update'),
    path('delete/<int:id>', views.item_delete, name='remove'),

]