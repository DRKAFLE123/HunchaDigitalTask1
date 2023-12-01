from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from rest_framework import generics  #importing for generic view
from .serializers import TodoSerializer # imports all serializers
from .models import * # imports all models

# Create your views here.

# CRUD operations with REST API

class ListTodo(generics.ListAPIView): #Reads and provides generic view
    queryset = Todo.objects.all().order_by('priority') # retrieves all Todo objects from db and show according to priority
    serializer_class = TodoSerializer  # converts Todo obj into Json
    
    
class DetailTodo(generics.RetrieveUpdateAPIView): #Update
    queryset = Todo.objects.all()  
    serializer_class = TodoSerializer  
    
class CreateTodo(generics.CreateAPIView):   #Create
    queryset = Todo.objects.all()  
    serializer_class = TodoSerializer  
    
class DeleteTodo(generics.RetrieveDestroyAPIView):  #Delete
    queryset = Todo.objects.all()  
    serializer_class = TodoSerializer 
    
    

# CRUD operation with help of HTML



def index(request):  # Read
    tasks = Todo.objects.all().order_by('priority')
    return render(request, 'index.html', {'tasks':tasks})
    
    
   
def create_task(request):  #Create
    if request.method == 'POST':
        task_name = request.POST['task_name']
        priority = int(request.POST['priority'])
        status = request.POST['status']
        task = Todo(task=task_name, priority=priority, completed=status)
        task.save()
        return redirect('/api/home')  # Redirect to homepage after creation

    return render(request, 'index.html')

    

def update_task(request, pk):  #update
    #to see the task table while updating also
    # tasks = Todo.objects.all().order_by('priority')
    # return render(request, 'index.html', {'tasks':tasks})
    
    task = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        task.task_name = request.POST['task_name']
        task.priority = int(request.POST['priority'])
        task.status = request.POST['status']
        task.save()
        return redirect('/api/home')
        
    return render(request, 'update_task.html', {'task': task})
        # return redirect('/api/update-task')

    

def delete_task(request, pk):  #delete
    #handling error if id doesnot exist
    try:
        task = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return redirect('/api/')  #it will redirect to the api view with ids
    return redirect('/api/home')

   
    
        

    

