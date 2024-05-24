from rest_framework import generics
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Announcement, Header, Section, Card, Section2
from .serializers import AnnSerialzers, HeaderSerializers, SectionSerialzers, CardSerialzers, Section2Serialzers
from django.shortcuts import get_object_or_404
from users.models import User



# Announcement
class AnnListView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnSerialzers
    
class AnnRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnSerialzers
    lookup_field = 'id'
    parser_classes = (MultiPartParser, FormParser)
    
class FilterByOwner(generics.ListAPIView):
    serializer_class = AnnSerialzers
    
    def get_queryset(self):
        owner_id = self.kwargs["id"]
        owner = get_object_or_404(User, id=owner_id)
        return Announcement.objects.filter(owner=owner)
    




# То что комил попросил
# Header
class HeaderListView(generics.ListCreateAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializers
    
class HeaderRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializers
    parser_classes = (MultiPartParser, FormParser)




# Card
class CardListView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerialzers
    
class CardRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerialzers
    parser_classes = (MultiPartParser, FormParser)




# Section
class SectionListView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerialzers
    
class SectionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerialzers
    parser_classes = (MultiPartParser, FormParser)




# Section2
class Section2ListView(generics.ListCreateAPIView):
    queryset = Section2.objects.all()
    serializer_class = Section2Serialzers
    
class Section2RUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section2.objects.all()
    serializer_class = Section2Serialzers
    parser_classes = (MultiPartParser, FormParser)





