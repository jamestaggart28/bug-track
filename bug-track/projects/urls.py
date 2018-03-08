from django.urls import path
from .views import ProjectCreate, ProjectUpdate, ProjectDelete, ProjectList, ProjectDetail

app_name = "projects"

urlpatterns = [
    path('', ProjectCreate.as_view(), name="project-create"),
    path('<int:pk>/', ProjectDetail.as_view(), name="project-detail"),
    path('<int:pk>/update/', ProjectUpdate.as_view(), name="project-update"),
    path('<int:pk>/delete/', ProjectDelete.as_view(), name="project-delete"),
    path('list/', ProjectList.as_view(), name="project-list"),
]
