from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import *
import requests
import smtplib, ssl


# Create your views here.

def index(request):
    tasks = Task.objects.filter(complete = False).order_by('-importance')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks/list.html', {'tasks':tasks, 'form':form})


def complete(request):
    tasks = Task.objects.filter(complete = True)

    return render(request, 'tasks/complete.html', {'tasks':tasks})



def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'tasks/delete.html', {'item': item})




