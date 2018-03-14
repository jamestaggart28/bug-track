from django.db import models
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

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
    assigned = models.CharField(max_length=30)
    fixed = models.BooleanField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'projects:bug-detail', args=[str(self.id)])
