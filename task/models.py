from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey('TaskCustomUser', on_delete=models.CASCADE, related_name='tasks')

    def is_overdue(self):
        return self.due_date < timezone.now().date() and not self.status

    def __str__(self):
        return self.title

class TaskCustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

@receiver(post_save, sender=TaskCustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=TaskCustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
