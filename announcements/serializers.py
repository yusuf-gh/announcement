from .models import Announcement, Header, Section, Card, Section2
from rest_framework import serializers

class AnnSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"
        
class HeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = "__all__"

class SectionSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"

class CardSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"

class Section2Serialzers(serializers.ModelSerializer):
    class Meta:
        model = Section2
        fields = "__all__"




