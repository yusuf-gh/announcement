from .models import Announcement
from rest_framework import serializers

class AnnSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"
        





