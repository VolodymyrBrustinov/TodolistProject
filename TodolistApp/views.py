from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Task

@login_required
def project_list(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'project_list.html', {'projects': projects})

@login_required
def task_list(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'task_list.html', {'project': project, 'tasks': tasks})

@login_required
def add_project(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        Project.objects.create(name=project_name, user=request.user)
        return redirect('project_list')
    return render(request, 'add_project.html')

@login_required
def delete_project(request, project_id):
    Project.objects.get(id=project_id).delete()
    return redirect('project_list')

@login_required
def add_task(request, project_id):
    if request.method == 'POST':
        project = Project.objects.get(id=project_id)
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        Task.objects.create(project=project, title=title, description=description, priority=priority)
        return redirect('task_list', project_id=project_id)
    return render(request, 'add_task.html')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    project_id = task.project.id
    task.delete()
    return redirect('task_list', project_id=project_id)

def login_view(request):
    return render(request, 'login.html')
