from django.urls import path, include
from task.views import task, easy, hard
from task.views.main import main_page

task_urls = [
    path('', task.task_list, name='list-task'),  # Главная страница, список задач
    path('create/', task.create_task, name='create_task'),  # Создание задачи
    path('<int:pk>/edit/', task.edit_task, name='edit-task'),  # Редактирование задачи
    path('<int:pk>/delete/', task.delete_task, name='delete-task'),  # Удаление задачи
    path('search_task/', task.search, name='search-task'),  # Поиск задачи
    path('<int:pk>/toggle/', task.toggle_task_completion, name='toggle-task_task'),



]

easy_urls = [
    path('', easy.easy_list, name='easy_list-task'),  # Главная страница, список задач
    path('create/', easy.easy_create_task, name='easy_create_task'),  # Создание задачи
    path('<int:pk>/edit/', easy.easy_edit_task, name='easy_edit-task'),  # Редактирование задачи
    path('<int:pk>/delete/', easy.easy_delete_task, name='easy_delete-task'),  # Удаление задачи
    path('search_task/', easy.easy_search, name='easy_search-task'),  # Поиск задачи
    path('<int:pk>/toggle/', easy.toggle_task_completion, name='toggle-task_easy'),

]

hard_urls = [
    path('', hard.hard_list, name='hard_list-task'),  # Главная страница, список задач
    path('create/', hard.hard_create_task, name='hard_create_task'),  # Создание задачи
    path('<int:pk>/edit/', hard.hard_edit_task, name='hard_edit-task'),  # Редактирование задачи
    path('<int:pk>/delete/', hard.hard_delete_task, name='hard_delete-task'),  # Удаление задачи
    path('search_task/', hard.hard_search, name='hard_search-task'),  # Поиск задачи
    path('<int:pk>/toggle/', hard.toggle_task_completion, name='toggle-task'),  # Маркировка задачи
]

urlpatterns = [
    path('', main_page, name='main_page'),  # Главная страница
    path('tasks/', include(task_urls)),
    path('easy/', include(easy_urls)),
    path('hard/', include(hard_urls)),
]
