from django.urls import path, include
from task.views import task, easy





task_urls = [
    path('', task.task_list, name='list-task'),  # Главная страница, список задач
    path('create/', task.create_task, name='create_task'),  # Создание задачи
    path('<int:pk>/edit/', task.edit_task, name='edit-task'),  # Редактирование задачи
    path('<int:pk>/delete/', task.delete_task, name='delete-task'),  # Удаление задачи
    path('search_task/', task.search, name='search-task'),  # Поиск задачи
]
easy_urls = [
    path('', easy.easy_list, name='easy_list-task'),  # Главная страница, список задач
    path('create/',easy.easy_create_task, name='easy_create_task'),  # Создание задачи
    path('<int:pk>/edit/', easy.easy_edit_task, name='easy_edit-task'),  # Редактирование задачи
    path('<int:pk>/delete/', easy.easy_delete_task, name='easy_delete-task'),  # Удаление задачи
    path('search_task/', easy.easy_search, name='easy_search-task'),  # Поиск задачи
]

urlpatterns = [
    path('tasks/', include(task_urls)),
    path('easy/', include(easy_urls)),
]