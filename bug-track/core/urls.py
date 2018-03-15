from django.urls import path
from core.views import Home, Register, Profile
from django.conf.urls import include

app_name = "core"

account_patterns = [
    path('registration/', Register.as_view(), name="register"),
    path('profile/', Profile.as_view(), name="profile")
]

urlpatterns = [
    path('accounts/', include(account_patterns)),
    path('', Home.as_view(), name="home"),
]
