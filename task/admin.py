from django.contrib import admin

# Register your models here.

from django.contrib import admin
from task.models import Task
from task.views.task import task_list


@admin.register(Task)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','task_name','task','time')
