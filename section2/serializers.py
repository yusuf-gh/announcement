from rest_framework import serializers
from .models import Section2

class Section2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Section2
        fields = "__all__"
        