from django.db import models
from django.utils import timezone  # Импортируйте timezone для получения текущей даты

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    due_date = models.DateField(default=timezone.now)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    def __str__(self):
        return self.title
