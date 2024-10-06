from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from .forms import SignUpForm, TaskForm
from .models import Task, Category, Priority

# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохранение нового пользователя
            login(request, user)  # Логин пользователя сразу после регистрации
            return redirect('home')  # Перенаправление на главную страницу
        else:
            print(form.errors)  # Вывод ошибок формы в консоль
    else:
        form = SignUpForm()  # Создание новой формы
    return render(request, 'task/register.html', {'form': form})

# Вход в систему
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = AuthenticationForm()
    return render(request, 'task/login.html', {'form': form})

# Главная страница
class HomeView(TemplateView):
    template_name = 'task/home.html'

# Список задач
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
            'selected_category': category_id,
            'selected_priority': priority_id,
            'search_task': search_task,
        }
    )

# Задачи по категории
def tasks_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    tasks = Task.objects.filter(category=category)
    return render(
        request,
        'task/task_list.html',
        {'tasks': tasks}
    )

# Задачи по приоритету
def tasks_by_priority(request, priority_id):
    priority = Priority.objects.get(id=priority_id)
    tasks = Task.objects.filter(priority=priority)
    return render(
        request,
        'task/task_list.html',
        {'tasks': tasks}
    )

# Создание задачи
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-task')  # Перенаправление на список задач
    else:
        form = TaskForm()
    return render(request, 'task/create_task.html', {'form': form})

# Редактирование задачи
def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list-task')  # Перенаправление на список задач
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/edit_task.html', {'form': form})

# Удаление задачи
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('list-task')  # Перенаправление на список задач

# Переключение статуса задачи
def toggle_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = True  # Предполагается, что статус завершённой задачи - True
    task.save()
    return redirect('list-task')  # Перенаправление на список задач

# Список категорий
def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'task/list_categories.html', {'categories': categories})

# Список приоритетов
def list_priorities(request):
    priorities = Priority.objects.all()
    return render(request, 'task/list_priorities.html', {'priorities': priorities})
from django.contrib.auth.decorators import login_required

@login_required
def some_view(request):
    current_user = request.user
    return render(request, 'some_template.html', {'user': current_user})
def some_view(request):
    print(request.user)  # Печатает текущего пользователя в консоль
    return render(request, 'some_template.html')
