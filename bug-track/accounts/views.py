from django.shortcuts import redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Register(FormView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.save()
        login(self.request, user)
        return redirect('accounts:profile')


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


class ResetDone(TemplateView):
    template_name = "accounts/password_reset_done.html"


class ResetComplete(TemplateView):
    template_name = "accounts/password_reset_complete.html"
