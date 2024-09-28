from django.shortcuts import render, redirect
from django.utils import timezone

from task.models import Task, Category, Priority
from task.forms import TaskForm


def list_tasks(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    priorities = Priority.objects.all()
    today = timezone.now().date()
    search_task = request.GET.get('search_task')
    category_id = request.GET.get('category')
    priority_id = request.GET.get('priority')

    if search_task:
        tasks = tasks.filter(title__icontains=search_task)

    if category_id:
        tasks = tasks.filter(category_id=category_id)

    if priority_id:
        tasks = tasks.filter(priority_id=priority_id)

    return render(
        request,
        'task/task_list.html',
        {
            'tasks': tasks,
            'categories': categories,
            'priorities': priorities,
            'today': today,
        }
    )


def tasks_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    tasks = Task.objects.filter(category=category)
    return render(
        request,
        'task/task_list.html',
        {'tasks': tasks}
    )


def tasks_by_priority(request, priority_id):
    priority = Priority.objects.get(id=priority_id)
    tasks = Task.objects.filter(priority=priority)
    return render(
        request,
        'task/task_list.html',
        {'tasks': tasks}
    )


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-task')
        # else:
        #     return render(request, 'task/create_task.html', {'form': form})
    else:
        form = TaskForm()
        return render(request, 'task/create_task.html', {'form': form})


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list-task')
    else:
        form = TaskForm(instance=task)
        return render(request, 'task/edit_task.html', {'form': form})


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('list-task')


def toggle_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = True
    task.save()
    return redirect('list-task')


def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'task/list_categories.html', {'categories': categories})


def list_priorities(request):
    priorities = Priority.objects.all()
    return render(request, 'task/list_priorities.html', {'priorities': priorities})