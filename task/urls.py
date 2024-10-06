
from django.urls import path
from task import views
from task.views import HomeView

urlpatterns = [
    path('', views.list_tasks, name='list-task'),
    path('<int:pk>/', views.toggle_task_status, name='toggle-task-status'),
    path('create/', views.create_task, name='create-task'),
    path('<int:pk>/edit/', views.edit_task, name='edit-task'),
    path('<int:pk>/delete/', views.delete_task, name='delete-task'),
    path('categories/', views.list_categories, name='list-categories'),
    path('priorities', views.list_priorities, name='list-priorities'),
    path('categories/<int:category_id>/', views.tasks_by_category, name='tasks-by-category'),
    path('priorities/<int:priority_id>/', views.tasks_by_priority, name='tasks-by-priority'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),

]
