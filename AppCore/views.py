from django.shortcuts import render
from AppTask.models import Task

def welcome(request):
    return render(request, 'Core/welcome.html')

def home(request):
    tasks = Task.objects.all()
    total_tasks = tasks.count()
    in_progress = tasks.filter(status='in_progress').count()
    finished = tasks.filter(status='finished').count()

    context = {
        'total_tasks': total_tasks,
        'in_progress': in_progress,
        'finished': finished
    }

    return render(request, 'Core/home.html',context)