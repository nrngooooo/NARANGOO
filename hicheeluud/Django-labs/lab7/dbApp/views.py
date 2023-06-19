from django.shortcuts import render
from dbApp.models import Branch
# Create your views here.
def index(request):
    return render(request, "index.html")
    
def branch(request):
    branch_list = Branch.objects.all()
    branch_dictionary = {'branches': branch_list}
    return render(request, 'branch/branch.html', context=branch_dictionary)