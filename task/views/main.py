from django.shortcuts import render
from task.models import Task, Easy, Hard

def main_page(request):
    # Получаем количество задач в каждой категории
    task_count = Task.objects.count()
    easy_task_count = Easy.objects.count()
    hard_task_count = Hard.objects.count()

    # Получаем количество завершенных и незавершенных задач для каждой категории
    completed_tasks = Task.objects.filter(is_completed=True).count()
    not_completed_tasks = task_count - completed_tasks

    completed_easy_tasks = Easy.objects.filter(is_completed=True).count()
    not_completed_easy_tasks = easy_task_count - completed_easy_tasks

    completed_hard_tasks = Hard.objects.filter(is_completed=True).count()
    not_completed_hard_tasks = hard_task_count - completed_hard_tasks

    # Передаем все данные в шаблон
    context = {
        'task_count': task_count,
        'easy_task_count': easy_task_count,
        'hard_task_count': hard_task_count,
        'completed_tasks': completed_tasks,
        'not_completed_tasks': not_completed_tasks,
        'completed_easy_tasks': completed_easy_tasks,
        'not_completed_easy_tasks': not_completed_easy_tasks,
        'completed_hard_tasks': completed_hard_tasks,
        'not_completed_hard_tasks': not_completed_hard_tasks,
    }
    return render(request, 'task/Main.html', context)
