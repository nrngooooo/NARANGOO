from django.shortcuts import render
from product_app.models import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def baraa(request, id):
    br = Product.objects.filter(category_id=id)
    tr = Category.objects.get(id=id)
    return render(request, "product/baraa.html",{'baraas': br,'turul': tr})