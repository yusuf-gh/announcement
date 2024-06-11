from rest_framework import serializers
from .models import Header

class HeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = "__all__"
        