from rest_framework import generics
from django.shortcuts import render
from .models import Section
from .serializers import SectionSerializers
from django.shortcuts import get_object_or_404


# Section
class SectionListView(generics.ListCreateAPIView): # Provides GET and POST method handlers.
    queryset = Section.objects.all()
    serializer_class = SectionSerializers
    
class SectionRUD(generics.RetrieveUpdateDestroyAPIView): # Provides PUT, PATCH and DELETE method handlers.
    queryset = Section.objects.all()
    serializer_class = SectionSerializers

