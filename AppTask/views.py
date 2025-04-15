from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Tasks lists
def taskList(request):
    tasks = Task.objects.all()
    return render(request, 'Tasks/taskList.html', {'tasks' : tasks})

# Add task
def taskCreate(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('taskList')
        
    else:
        form = TaskForm()

    return render(request, 'Tasks/taskForm.html', {'form': form})

# Update task
def taskUpdate(request, pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)

        if form.is_valid():
            form.save()
            return redirect('taskList')
        
    else:
        form = TaskForm(instance = task)

    return render(request, 'Tasks/taskForm.html', {'form': form})

# Delete Task
def taskDelete(request, pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('taskList')
    
    return render(request, 'Tasks/taskConfirmDelete.html', {'task': task})