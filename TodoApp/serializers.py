# import serializers here from restframework
from rest_framework import serializers  #converts objects into a py datatypes
from .models import *

#create serializer
class TodoSerializer(serializers.ModelSerializer): #modelserializer is a component of Django REST framework provides shortcuts
    class Meta:
        model = Todo #ModelName
        fields = ('id','task','priority', 'date','completed' )  # List of Fields