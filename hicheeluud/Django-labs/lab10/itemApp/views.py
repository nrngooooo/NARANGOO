from django.shortcuts import render, redirect
from .models import *
from lab10.forms import *

def index(request):
    return render(request, "index.html")

def item_list(request):
    if request.method == 'GET':
        itm = Item.objects.all()
        form = ItemForm()
        return render(request, "baraa/item.html",{'items': itm,'iform':form})
    elif request.method == 'POST':
        submitted_form = ItemForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect('/items')
def item_edit(request, id):
    if request.method == 'GET':
        i = Item.objects.get(id=id)
        edit_form = ItemForm(instance=i)
        return render(request, "baraa/item_edit.html", {'edit': edit_form})
    elif request.method == 'POST':
        itm = Item.objects.get(id=id)
        edited_form = ItemForm(request.POST,instance=itm)
        if edited_form.is_valid():
            edited_form.save()
        return redirect('/items')
def item_delete(request, id):
    itm = Item.objects.get(id=id)
    itm.delete()
    return redirect('/items')