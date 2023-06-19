from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy
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

class ClubCreateView(CreateView):
    fields = ('cname', 'location')
    model = models.Club
    template_name = "club/club_form.html"
    success_url = reverse_lazy('clubApp:list')

class ClubUpdateView(UpdateView):
    fields = ('cname', 'location')
    model = models.Club
    template_name = "club/club_form.html"
    success_url = reverse_lazy('clubApp:list')

class ClubDeleteView(DeleteView):
    model = models.Club
    template_name = "club/club_confirm_delete.html"
    success_url= reverse_lazy("clubApp:list")
# class ComedianUpdateView(UpdateView):
#     fields = ('coname', 'age','image','club')
#     model = models.Comedian
#     template_name = "club/club_form.html"
#     success_url = reverse_lazy('clubApp:list')

# class ComedianDeleteView(DeleteView):
#     model = models.Comedian
#     template_name = "club/comedian_confirm_delete.html"
#     success_url= reverse_lazy("clubApp:list")
