from rest_framework import generics
from django.shortcuts import render
from .models import Announcement
from .serializers import AnnSerialzers
from django.shortcuts import get_object_or_404
from users.models import User



# Announcement
class AnnListView(generics.ListCreateAPIView): # Provides GET and POST method handlers.
    queryset = Announcement.objects.all()
    serializer_class = AnnSerialzers
    
class AnnRUD(generics.RetrieveUpdateDestroyAPIView): # Provides PUT, PATCH and DELETE method handlers.
    queryset = Announcement.objects.all()
    serializer_class = AnnSerialzers
    lookup_field = 'id'

    
class FilterByOwner(generics.ListAPIView):
    serializer_class = AnnSerialzers
    
    def get_queryset(self):
        owner_id = self.kwargs["id"]
        owner = get_object_or_404(User, id=owner_id)
        return Announcement.objects.filter(owner=owner)