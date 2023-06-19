from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def zurag(request):
    dic = {'print':'Handsome oppaaaaayaa:'}
    return render(request, "staticApp/zurag.html", context = dic)

def menu(request):
    dic = {'print':'Hover menu'}
    return render(request, "staticApp/menu.html", context = dic)
def media(request):
    dic = {'print':'Wonderful Video'}
    return render(request, "staticApp/media.html", context = dic)