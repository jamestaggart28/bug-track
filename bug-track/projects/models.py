from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'projects:project-detail', args=[str(self.id)])


class Bug(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    reproduce = models.TextField()
    expected = models.TextField()
    observed = models.TextField()
    assigned = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="project_bug_assigned"
    )
    fixed = models.BooleanField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="project_bug_created_by"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'projects:bug-detail', args=[str(self.id)])
