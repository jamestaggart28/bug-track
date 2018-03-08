from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project, Bug


# Create your views here.
class ProjectCreate(CreateView):
    model = Project
    fields = ['name', 'description']


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name', 'description']


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project:project-list')


class ProjectDetail(DetailView):
    model = Project


class ProjectList(ListView):
    model = Project
