from django.shortcuts import render, redirect
from basic_app.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.

def index(request):
    return render(request, "index.html")
def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'user_pic' in request.FILES:
                profile.user_pic = request.FILES['user_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',{
'user_form': user_form,
'profile_form': profile_form,
'registered': registered
}
)
def login(request):

    if request.method == 'POST':
        is_login = False
        has_message = False
        message = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                is_login = True
                has_message = True 
                message = f'Сайн байна уу {username} та амжилттай нэвтэрлээ.'
            else:
                has_message = True 
                message = 'Бүртгэлгүй хэрэглэгч байна.'
        else:
            has_message = True 
            message = 'Бүртгэлгүй хэрэглэгч байна.'
            print("Username: {} and password {}". format(username, password))
        return render(request, 'login.html',{
            'is_login': is_login,
            'message': message,
            'has_message': has_message           
            })
    else:
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))