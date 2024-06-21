from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    get_age = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ("id", "date_of_birth", "username", "contact", "age")
        
    def get_age(self, age):
        return dict(age)


    

