from django.contrib import admin
from django.urls import path, include

# main urlpatterns without importing itself
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('task.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
