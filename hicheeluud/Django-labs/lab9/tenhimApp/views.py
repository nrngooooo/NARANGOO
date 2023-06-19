from django.shortcuts import render, redirect
from django.contrib import messages
from tenhimApp.models import Tenhim
from tenhimApp.forms import TenhimForm
# Create your views here.


def index(request):
    context = {'print': 'Энэ бол нүүр хуудас'}
    return render(request, 'index.html', context)

def tenhim(request):
    t = Tenhim.objects.all()
    context = {'tenhims': t}
    return render(request, "tenhim/tenhim.html", context)

def tenhim_add(request):
    if request.method == 'GET':
        tenhim_form = TenhimForm()
        return render(request, "tenhim/tenhim_add.html", {'tform':tenhim_form})
    else:
        submitted_form = TenhimForm(request.POST)
        if submitted_form.is_valid():
            b = Tenhim()
            b.tname = submitted_form.cleaned_data['tname']
            b.save()
            return redirect('/tenhim')
        
def tenhim_edit(request, id):
    if request.method == 'GET':
        w = Tenhim.objects.get(id=id)
        return render(request,"tenhim/tenhim_edit.html",{'tenhims': w})
    elif request.method == 'POST':
        w = Tenhim.objects.get(id=id)
        w.tname = request.POST.get('tname')
        w.save()
        return redirect('/tenhim')
    
def tenhim_delete(request, pk):
    w = Tenhim.objects.get(id=pk)
    w.delete()
    return redirect('/tenhim')