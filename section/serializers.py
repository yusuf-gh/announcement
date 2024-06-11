from .models import Section
from rest_framework import serializers

class SectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"