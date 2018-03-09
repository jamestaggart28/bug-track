from django.urls import path
from .views import AppCreate, AppUpdate, AppDelete, AppList, AppDetail

app_name = "apps"


urlpatterns = [
    path('', AppCreate.as_view(), name="app-create"),
    path('<int:pk>/', AppDetail.as_view(), name="app-detail"),
    path('<int:pk>/update/', AppUpdate.as_view(), name="app-update"),
    path('<int:pk>/delete/', AppDelete.as_view(), name="app-delete"),
    path('list/', AppList.as_view(), name="app-list"),
]
