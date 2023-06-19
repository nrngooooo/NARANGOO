from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models
from django.http import HttpResponse
class IndexView(View):
    print = 'Hello Django'
    def get(self, request):
        return HttpResponse('<h1>' + self.print + ' World</h1>')
class IndexView(TemplateView):
    template_name = 'index.html'
class ClubListView(ListView):
    context_object_name='clubList'
    model = models.Club
    template_name = 'club/club_list.html'

class ClubDetailView(DetailView):
    context_object_name='clubDetails'
    model = models.Club
    template_name ='club/club_detail.html'