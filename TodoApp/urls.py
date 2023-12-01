# Todo APP URLS

# from django.contrib import admin
from django.urls import path
from .views import *
  
  # The first set of URL patterns utilizes Django's generic class-based views (CBVs) for handling CRUD operations.
  # The second set of URL patterns employs Django's traditional function-based views (FBVs) for managing CRUD operations.
urlpatterns = [
    path('update/<int:pk>/', DetailTodo.as_view()),  #link to update
    path('', ListTodo.as_view()),     #LINK TO READ 
    path('create', CreateTodo.as_view()),  #Link to create
    path('delete/<int:pk>', DeleteTodo.as_view()),  #link to delete
   
    # now crud with the help of frontend(html)
    path('home/', index, name='home'),  #Read
    path('create-task/', create_task, name='create_task'), #Create
    path('update-task/<int:pk>',update_task, name='update_task'), #update
    path('delete-task/<int:pk>',delete_task, name='delete_task'), #delete
     
]
