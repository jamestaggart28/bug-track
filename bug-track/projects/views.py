from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project, Bug
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.
class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProjectUpdate(UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'description']

    def test_func(self):
        project = self.get_object()
        return project.created_by == self.request.user


class ProjectDelete(UserPassesTestMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('projects:project-list')

    def test_func(self):
        project = self.get_object()
        return project.created_by == self.request.user


class ProjectDetail(DetailView):
    model = Project


class ProjectList(ListView):
    model = Project


class BugCreate(LoginRequiredMixin, CreateView):
    model = Bug
    fields = [
        'project', 'name', 'reproduce', 'expected',
        'observed', 'assigned', 'fixed']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class BugUpdate(UserPassesTestMixin, UpdateView):
    model = Bug
    fields = [
        'project', 'name', 'reproduce', 'expected',
        'observed', 'assigned', 'fixed']

    def test_func(self):
        project = self.get_object()
        return project.created_by == self.request.user or project.assigned == self.request.user


class BugDelete(UserPassesTestMixin, DeleteView):
    model = Bug
    success_url = reverse_lazy('projects:bug-list')

    def test_func(self):
        project = self.get_object()
        return project.created_by == self.request.user


class BugDetail(DetailView):
    model = Bug


class BugList(ListView):
    model = Bug
