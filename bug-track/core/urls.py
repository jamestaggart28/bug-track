from django.urls import path
from core.views import Home, Register
from django.conf.urls import include

app_name = "core"

account_patterns = [
    path('registration/', Register.as_view(), name="register")
]

urlpatterns = [
    path('accounts/', include(account_patterns)),
    path('', Home.as_view(), name="home"),
]
