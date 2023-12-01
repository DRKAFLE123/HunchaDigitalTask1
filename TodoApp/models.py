from django.db import models
#In SQLIte we have types: text, numeric, integer, real, bolb

# Create your models here.

class Todo(models.Model):  #created a model according to requirements in task
       
    # user = models.ForeignKey(User, on_delete = models.CASCADE)  # created users as a foregin key 
    task = models.CharField(max_length=255, blank=False)  #descriptions of task (title)
    priority = models.IntegerField(max_length=2, blank = False , default = '0')  # it will show the priority 
    completed = models.BooleanField(default=False)  # to check status of task
    date = models.DateField(auto_now_add = True )  #it will automatically add the date
    
    def is_completed(self):
        return self.completed
    
    def __str__(self):
        return self.task
    
    
    