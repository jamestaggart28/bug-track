from django.urls import include, path
from .views import ProjectCreate, ProjectUpdate, ProjectDelete, ProjectList, ProjectDetail
from .views import BugCreate, BugUpdate, BugDelete, BugList, BugDetail

app_name = "projects"


bug_patterns = [
    path('', BugCreate.as_view(), name="bug-create"),
    path('<int:pk>/', BugDetail.as_view(), name="bug-detail"),
    path('<int:pk>/update/', BugUpdate.as_view(), name="bug-update"),
    path('<int:pk>/delete/', BugDelete.as_view(), name="bug-delete"),
    path('list/', BugList.as_view(), name="bug-list"),
]


urlpatterns = [
    path('', ProjectCreate.as_view(), name="project-create"),
    path('<int:pk>/', ProjectDetail.as_view(), name="project-detail"),
    path('<int:pk>/update/', ProjectUpdate.as_view(), name="project-update"),
    path('<int:pk>/delete/', ProjectDelete.as_view(), name="project-delete"),
    path('list/', ProjectList.as_view(), name="project-list"),
    path('bugs/', include(bug_patterns)),
]
