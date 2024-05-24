from rest_framework import generics
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer

class UsersListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UsersRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
