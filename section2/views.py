
from rest_framework import generics
from django.shortcuts import render
from .models import Section2
from .serializers import Section2Serializers
from django.shortcuts import get_object_or_404


# Section2
class Section2ListView(generics.ListCreateAPIView): # Provides GET and POST method handlers.
    queryset = Section2.objects.all()
    serializer_class = Section2Serializers
    
class Section2RUD(generics.RetrieveUpdateDestroyAPIView): # Provides PUT, PATCH and DELETE method handlers.
    queryset = Section2.objects.all()
    serializer_class = Section2Serializers



