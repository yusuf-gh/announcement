
from rest_framework import generics
from django.shortcuts import render
from .models import Card
from .serializers import CardSerialzers
from django.shortcuts import get_object_or_404


# Card 
class CardListView(generics.ListCreateAPIView): # Provides GET and POST method handlers.
    queryset = Card.objects.all()
    serializer_class = CardSerialzers
    
class CardRUD(generics.RetrieveUpdateDestroyAPIView): # Provides PUT, PATCH and DELETE method handlers.
    queryset = Card.objects.all()
    serializer_class = CardSerialzers
    



