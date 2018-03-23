from accounts.views import (
    Register, Profile, ResetDone, ResetComplete
)
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm
from django.urls import reverse_lazy

app_name = "accounts"

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name="accounts/login.html",
            authentication_form=UserLoginForm
        ),
        name="login"
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(
            template_name="accounts/logout.html"
        ),
        name="logout"
    ),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change_form.html",
            success_url=reverse_lazy("accounts:profile")
        ),
        name="password-change"
    ),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset_form.html",
            email_template_name="accounts/password_reset_email.html",
            success_url=reverse_lazy("accounts:reset-done")
        ),
        name="password-reset"
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url=reverse_lazy("accounts:reset-complete")
        ),
        name="password-reset-confirm"
    ),
    path('register/', Register.as_view(), name="register"),
    path('profile/', Profile.as_view(), name="profile"),
    path('reset_done/', ResetDone.as_view(), name="reset-done"),
    path('reset_complete/', ResetComplete.as_view(), name="reset-complete")
]
