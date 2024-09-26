from django.contrib import admin
from task.models import Task, Category, Priority


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'priority')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'priority')