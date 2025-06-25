from rest_framework import generics
from .models import TodoItem
from .serializes import TodoSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class TodoList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoSerializer
    permission_classes=[IsAuthenticated]

class TodoDetail(generics.RetrieveUpadeDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoSerializer
    permission_classes=[IsAuthenticated]

class UserCreate(generics.CreateAPIView):
    queryset= User.object.all()
    serializer_class=UserSerializer
    permission_classes = []

