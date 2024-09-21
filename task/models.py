from django.db import models

# Create your models here.
from django.db import models


class Task(models.Model):
    is_completed = models.BooleanField(default=False)  # Добавляем поле для статуса
    task_name = models.CharField(max_length=100)
    task = models.CharField(max_length=200)
    time = models.DateTimeField()
    def __str__(self):
        return self.task_name



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Priority(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Easy(models.Model):
    is_completed = models.BooleanField(default=False)  # Добавляем поле для статуса
    easy_task_name = models.CharField(max_length=100)
    easy_task = models.CharField(max_length=200)
    easy_time = models.DateTimeField()
    def __str__(self):
        return self.easy_task_name




class Hard(models.Model):
    is_completed = models.BooleanField(default=False)  # Добавляем поле для статуса
    hard_task_name = models.CharField(max_length=100)
    hard_task = models.CharField(max_length=200)
    hard_time = models.DateTimeField()
    def __str__(self):
        return self.hard_task_name






