from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializers
from .models import Todo
class TodoViewset(viewsets.ModelViewSet):
    queryset =Todo.objects.all().orderby('date-created')
    serializer_class = TodoSerializers

