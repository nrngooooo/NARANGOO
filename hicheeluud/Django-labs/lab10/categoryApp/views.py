from django.shortcuts import render, redirect
from .models import *
from lab10.forms import *

def index(request):
    return render(request, "index.html")

def category_list(request):
    if request.method == 'GET':
        itm = Category.objects.all()
        form = CategoryForm()
        return render(request, "turul/turul.html",{'turuls': itm,'tform':form})
    elif request.method == 'POST':
        submitted_form = CategoryForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/turul')
def category_edit(request, id):
    if request.method == 'GET':
        i = Category.objects.get(id=id)
        edit_form = CategoryForm(instance=i)
        return render(request, "turul/turul_edit.html", {'edit': edit_form})
    elif request.method == 'POST':
        t = Category.objects.get(id=id)
        edited_form = CategoryForm(request.POST,instance=t)
        if edited_form.is_valid():
            edited_form.save()
        return redirect('/turul')
def category_delete(request, id):
    t = Category.objects.get(id=id)
    t.delete()
    return redirect('/turul')