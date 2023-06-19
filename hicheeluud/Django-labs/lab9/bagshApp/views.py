from django.shortcuts import render, redirect
from .models import Bagsh,Tenhim
from bagshApp.forms import BagshForm

# Create your views here.
def index(request):
    context = {'print': 'Энэ бол нүүр хуудас'}
    return render(request, 'index.html', context)

def bagsh(request):
    b = Bagsh.objects.all()
    context = {'bagshnar': b}
    return render(request, "bagsh/bagsh.html",context)

def bagsh_add(request):
    if request.method == 'GET':
        bagsh_form = BagshForm()
        return render(request, "bagsh/bagsh_add.html", {'bform':bagsh_form})
    else:
        submitted_form = BagshForm(request.POST)
        if submitted_form.is_valid():
            b = Bagsh()
            b.bovog = submitted_form.cleaned_data['bovog']
            b.bname = submitted_form.cleaned_data['bname']
            b.email = submitted_form.cleaned_data['email']
            b.tenhim = submitted_form.cleaned_data['tenhim']
            b.password = submitted_form.cleaned_data['password']
            b.password_confirm = submitted_form.cleaned_data['password_confirm']
            b.save()
            return redirect('/bagsh')
        
def bagsh_edit(request, id):
    if request.method == 'GET':
        w = Bagsh.objects.get(id=id)
        b = Tenhim.objects.all()
        return render(request,"bagsh/bagsh_edit.html",{'bagsh': w, 'tenhim': b})
    elif request.method == 'POST':
        w = Bagsh.objects.get(id=id)
        w.bovog = request.POST.get('bovog')
        w.bname = request.POST.get('bname')
        w.tenhim_id = request.POST.get('tenhim_id')
        w.email = request.POST.get('email')
        w.password = request.POST.get('password')
        w.password_confirm = request.POST.get('password_confirm')
        w.save()
        return redirect('/bagsh')
        
def bagsh_delete(request, pk):
    w = Bagsh.objects.get(id=pk)
    w.delete()
    return redirect('/bagsh')