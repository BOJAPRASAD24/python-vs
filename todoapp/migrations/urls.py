from django.urls import path
from views import TodoList, TodoDetail, UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns =[
    path('register/',UserCreate.as_view(), name='create-user'),
    path('token/', TokenObtainPairView.as_view(), name='get-token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('todo/', TodoList.as_view(), name='todo-list'),
    path('todo/<int:pk>', TodoDetail.as_view(), name = 'todo-details'),
]

