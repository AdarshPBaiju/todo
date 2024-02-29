from django.shortcuts import render,redirect
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