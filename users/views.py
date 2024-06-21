from rest_framework import generics
from .models import User
from .filters import UserFilterByAge
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UsersListView(generics.ListCreateAPIView): # Provides GET and POST method handlers, and filters by age (lte)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilterByAge
    
    
    
class UsersRUD(generics.RetrieveUpdateDestroyAPIView): # Provides PUT, PATCH and DELETE method handlers.
    queryset = User.objects.all()
    serializer_class = UserSerializer

        
    
