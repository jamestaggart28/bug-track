from django.db import models
from projects.models import Project


# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name


class Bug(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    reproduce = models.TextField()
    expected = models.TextField()
    observed = models.TextField()
    assigned = models.CharField(max_length=30)
    fixed = models.BooleanField()

    def __str__(self):
        return self.name
