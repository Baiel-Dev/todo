from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from task.forms import TaskForm
from task.models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks, 'name': 'Tasks List'})


def search(request):
    tasks = Task.objects.filter(first_name__icontains=request.GET['q'])
    return render(request, 'task/task_list.html', {'task': tasks, 'name': 'tasks tables'})


# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'task/task_list.html', {'task': tasks, 'name': 'tasks tables'})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Исправил название формы
        if form.is_valid():
            form.save()
            return redirect('list-task')
    else:
        form = TaskForm()  # Исправил название формы
    return render(request, 'task/create_task.html', {'form': form, 'name': 'Create task'})


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Исправил название формы
        if form.is_valid():
            form.save()
            return redirect('list-task')
    else:
        form = TaskForm(instance=task)  # Исправил название формы
    return render(request, 'task/create_task.html', {'form': form, 'name': 'Edit task'})


def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:  # Исправил название модели
        return redirect('list-task')
    task.delete()
    return redirect('list-task')
