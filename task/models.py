from django.db import models
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Priority(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task = models.CharField(max_length=200)
    time = models.DateTimeField()

    def __str__(self):
        return self.task_name
