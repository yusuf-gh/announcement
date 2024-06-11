from rest_framework import generics
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer

class UsersListView(generics.ListCreateAPIView): # Provides GET and POST method handlers.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UsersRUD(generics.RetrieveUpdateDestroyAPIView): # Provides PUT, PATCH and DELETE method handlers.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
