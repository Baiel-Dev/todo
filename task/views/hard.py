from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from task.forms import HardForm
from task.models import Hard





def hard_list(request):
    hard = Hard.objects.all()
    return render(request, 'task/hard_task.html', {'hard': hard, 'name': 'Hard'})


def hard_search(request):
    hard = Hard.objects.filter(first_name__icontains=request.GET['q'])
    return render(request, 'task/hard_task.html', {'hard': hard, 'name': 'Hard'})


# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'task/task_list.html', {'task': tasks, 'name': 'tasks tables'})


def hard_create_task(request):
    if request.method == 'POST':
        form = HardForm(request.POST)  # Исправил название формы
        if form.is_valid():
            form.save()
            return redirect('hard_list-task')
    else:
        form = HardForm()  # Исправил название формы
    return render(request, 'task/create_hard.html', {'form': form, 'name': 'hard Create task'})


def hard_edit_task(request, pk):
    hard = Hard.objects.get(pk=pk)
    if request.method == 'POST':
        form = HardForm(request.POST, instance=hard)  # Исправил название формы
        if form.is_valid():
            form.save()
            return redirect('hard_task')
    else:
        form = HardForm(instance=hard)  # Исправил название формы
    return render(request, 'task/create_hard.html', {'form': form, 'name': 'Edit hard task'})


def hard_delete_task(request, pk):
    try:
        task = Hard.objects.get(pk=pk)
    except Hard.DoesNotExist:  # Исправил название модели
        return redirect('hard_list-task')
    task.delete()
    return redirect('hard_list-task')


from django.shortcuts import get_object_or_404, redirect
from task.models import Hard

def toggle_task_completion(request, pk):
    task = get_object_or_404(Hard, pk=pk)
    task.is_completed = not task.is_completed  # Меняем статус выполнения
    task.save()
    return redirect('hard_list-task')  # Перенаправляем на список задач


