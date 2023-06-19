from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import BurtguulehForm
# Create your views here.

def first(request):
    return render(request, 'chatapp/first.html')
def signup(request):
    if request.method == 'POST':
        form = BurtguulehForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('first')
    else:
        form = BurtguulehForm()
    
    return render(request, 'chatapp/signup.html', {'form': form})
    