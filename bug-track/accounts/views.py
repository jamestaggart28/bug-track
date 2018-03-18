from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView


# Create your views here.
def login_view(request):
    next.request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("core:home")

    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("core:home")

    context = {
        "form": form,
    }
    return render(request, "accounts/register.html", context)


def logout_view(request):
    logout(request)
    return redirect('core:home')


def authenticated_view(request):
    return render(request, "accounts/authenticated.html", {})


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
