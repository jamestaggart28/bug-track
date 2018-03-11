from django.urls import include, path
from .views import AppCreate, AppUpdate, AppDelete, AppList, AppDetail
from .views import BugCreate, BugUpdate, BugDelete, BugList, BugDetail

app_name = "apps"


bug_patterns = [
    path('', BugCreate.as_view(), name="bug-create"),
    path('<int:pk>/', BugDetail.as_view(), name="bug-detail"),
    path('<int:pk>/update/', BugUpdate.as_view(), name="bug-update"),
    path('<int:pk>/delete/', BugDelete.as_view(), name="bug-delete"),
    path('list/', BugList.as_view(), name="bug-list"),
]


urlpatterns = [
    path('', AppCreate.as_view(), name="app-create"),
    path('<int:pk>/', AppDetail.as_view(), name="app-detail"),
    path('<int:pk>/update/', AppUpdate.as_view(), name="app-update"),
    path('<int:pk>/delete/', AppDelete.as_view(), name="app-delete"),
    path('list/', AppList.as_view(), name="app-list"),
    path('bugs/', include(bug_patterns)),
]
