from django.db import models
from django.urls import reverse
from projects.models import Project


# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'apps:app-detail', args=[str(self.id)])


class Bug(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    reproduce = models.TextField()
    expected = models.TextField()
    observed = models.TextField()
    assigned = models.CharField(max_length=30)
    fixed = models.BooleanField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'apps:bug-detail', args=[str(self.id)])
