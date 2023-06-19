from django.shortcuts import render

# Create your views here.
def index(request):
    a = {"text": "уш02200190"}
    return render(request, 'index.html', context=a)
def job(request):
    a = {"author": "narangoo dash"}
    return render(request, 'jobApp/job.html', context=a)
def jobHelp(request):

    jobHelp_dictionary = {'print': 'Энэ бол help page-н контент views.py-с дуудаж байна.'}
    return render(request, 'jobApp/jobHelp.html', context=jobHelp_dictionary)