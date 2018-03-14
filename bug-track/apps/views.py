from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import App, Bug


# Create your views here.
class AppCreate(CreateView):
    model = App
    fields = ['name', 'description', 'projects']


class AppUpdate(UpdateView):
    model = App
    fields = ['name', 'description', 'projects']


class AppDelete(DeleteView):
    model = App
    success_url = reverse_lazy('apps:app-list')


class AppList(ListView):
    model = App


class AppDetail(DetailView):
    model = App


class BugCreate(CreateView):
    model = Bug
    fields = [
        'app', 'name', 'reproduce', 'expected',
        'observed', 'assigned', 'fixed']


class BugUpdate(UpdateView):
    model = Bug
    fields = [
        'app', 'name', 'reproduce', 'expected',
        'observed', 'assigned', 'fixed']


class BugDelete(DeleteView):
    model = Bug
    success_url = reverse_lazy('apps:bug-list')


class BugDetail(DetailView):
    model = Bug


class BugList(ListView):
    model = Bug
