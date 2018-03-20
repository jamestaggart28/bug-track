from accounts.views import login_view, register_view, logout_view, authenticated_view
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm, UserRegisterForm
from django.conf import settings
from django.urls import reverse_lazy

app_name = "accounts"

urlpatterns = [
    # path('login/', login_view, name="login"),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html", authentication_form=UserLoginForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path('authenticated/', authenticated_view, name="authenticated"),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="accounts/password_change_form.html", success_url=reverse_lazy("accounts:authenticated")), name="password-change"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html", email_template_name="accounts/password_reset_email.html", success_url=reverse_lazy("accounts:authenticated")), name="password-reset"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html", success_url=reverse_lazy("accounts:authenticated")), name="password-reset-confirm"),
    path('register/', register_view, name="register"),
]
