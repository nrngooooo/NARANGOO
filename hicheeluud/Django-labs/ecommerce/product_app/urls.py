from django.urls import path
from product_app import views

app_name = 'pro'

urlpatterns = [
    path('<int:id>', views.baraa, name='baraa'),

]