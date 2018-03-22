from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import App, Bug
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.
class AppCreate(LoginRequiredMixin, CreateView):
    model = App
    fields = ['name', 'description', 'projects']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AppUpdate(UserPassesTestMixin, UpdateView):
    model = App
    fields = ['name', 'description', 'projects']

    def test_func(self):
        app = self.get_object()
        return app.created_by == self.request.user


class AppDelete(UserPassesTestMixin, DeleteView):
    model = App
    success_url = reverse_lazy('apps:app-list')

    def test_func(self):
        app = self.get_object()
        return app.created_by == self.request.user


class AppList(ListView):
    model = App


class AppDetail(DetailView):
    model = App


class BugCreate(LoginRequiredMixin, CreateView):
    model = Bug
    fields = [
        'app', 'name', 'reproduce', 'expected',
        'observed', 'assigned', 'fixed']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class BugUpdate(UserPassesTestMixin, UpdateView):
    model = Bug
    fields = [
        'app', 'name', 'reproduce', 'expected',
        'observed', 'assigned', 'fixed']

    def test_func(self):
        app = self.get_object()
        return app.created_by == self.request.user or app.assigned == self.request.user


class BugDelete(UserPassesTestMixin, DeleteView):
    model = Bug
    success_url = reverse_lazy('apps:bug-list')

    def test_func(self):
        app = self.get_object()
        return app.created_by == self.request.user


class BugDetail(DetailView):
    model = Bug


class BugList(ListView):
    model = Bug
