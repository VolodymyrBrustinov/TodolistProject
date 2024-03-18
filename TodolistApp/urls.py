from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:project_id>/', views.task_list, name='task_list'),
    path('add_project/', views.add_project, name='add_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('add_task/<int:project_id>/', views.add_task, name='add_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]





