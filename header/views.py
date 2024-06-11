
from rest_framework import generics
from django.shortcuts import render
from .models import Header
from .serializers import HeaderSerializers
from django.shortcuts import get_object_or_404


# Header
class HeaderListView(generics.ListCreateAPIView): # Provides GET and POST method handlers.
    queryset = Header.objects.all()
    serializer_class = HeaderSerializers
    
class HeaderRUD(generics.RetrieveUpdateDestroyAPIView): # Provides PUT, PATCH and DELETE method handlers.
    queryset = Header.objects.all()
    serializer_class = HeaderSerializers
