from django.urls import path
from task import views
from task.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('tasks/', views.list_tasks, name='list-task'),  # Список задач
    path('<int:pk>/', views.toggle_task_status, name='toggle-task-status'),  # Изменение статуса задачи
    path('create/', views.create_task, name='create-task'),  # Создание задачи
    path('<int:pk>/edit/', views.edit_task, name='edit-task'),  # Редактирование задачи
    path('<int:pk>/delete/', views.delete_task, name='delete-task'),  # Удаление задачи
    path('categories/', views.list_categories, name='list-categories'),  # Список категорий
    path('priorities/', views.list_priorities, name='list-priorities'),  # Список приоритетов
    path('categories/<int:category_id>/', views.tasks_by_category, name='tasks-by-category'),  # Задачи по категории
    path('priorities/<int:priority_id>/', views.tasks_by_priority, name='tasks-by-priority'),  # Задачи по приоритету
    path('register/', views.register, name='register'),  # Регистрация пользователя
    path('login/', views.login_view, name='login'),  # Вход пользователя
    path('profile/<int:pk>/', views.profile, name='profile'),  # Профиль пользователя
    path('profile/<int:pk>/edit/', views.edit_profile, name='edit-profile'),  # Редактирование профиля
]
