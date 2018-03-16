from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views.generic import TemplateView


# Create your views here.
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    return render(request, "form.html", {})


def logout_view(request):
    return render(request, "form.html", {})


class Register(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('core:home')


class Profile(TemplateView):
    template_name = "accounts/profile.html"
