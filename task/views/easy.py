from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from task.forms import  EasyForm
from task.models import  Easy





def easy_list(request):
    easy = Easy.objects.all()
    return render(request, 'task/Easy.html', {'easy': easy, 'name': 'Easy'})


def easy_search(request):
    easy = Easy.objects.filter(first_name__icontains=request.GET['q'])
    return render(request, 'task/Easy.html', {'easy': easy, 'name': 'Easy'})


# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'task/task_list.html', {'task': tasks, 'name': 'tasks tables'})


def easy_create_task(request):
    if request.method == 'POST':
        form = EasyForm(request.POST)  # Исправил название формы
        if form.is_valid():
            form.save()
            return redirect('easy_list-task')
    else:
        form = EasyForm()  # Исправил название формы
    return render(request, 'task/create_easy.html', {'form': form, 'name': 'easy Create task'})


def easy_edit_task(request, pk):
    easy = Easy.objects.get(pk=pk)
    if request.method == 'POST':
        form = EasyForm(request.POST, instance=easy)  # Исправил название формы
        if form.is_valid():
            form.save()
            return redirect('easy_list-task')
    else:
        form = EasyForm(instance=easy)  # Исправил название формы
    return render(request, 'task/create_easy.html', {'form': form, 'name': 'Edit easy task'})


def easy_delete_task(request, pk):
    try:
        task = Easy.objects.get(pk=pk)
    except Easy.DoesNotExist:  # Исправил название модели
        return redirect('easy_list-task')
    task.delete()
    return redirect('easy_list-task')

