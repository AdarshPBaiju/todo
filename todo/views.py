from django.shortcuts import render,redirect,get_object_or_404
from django.http import  HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    if request.method == 'POST':
        # Ensure 'task' key exists in POST data
        if 'task' in request.POST:
            task = request.POST['task']
            # Ensure 'task' value is not empty
            if task.strip():
                Task.objects.create(task=task)
                return redirect('home')
            else:
                return HttpResponse("Task cannot be empty")
        else:
            return HttpResponse("Task key not found in form data")
    else:
        return HttpResponse("This view only accepts POST requests")
    
def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task=get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect ('home')
    else:
        context = {
            'get_task':get_task,
        }
        return render(request, 'edit_task.html',context)

def delete_task(request, pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')