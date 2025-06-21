from rest_framework import generics
from .models import TodoItem
from .serializes import TodoSerializer

class TodoList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoSerializer
