import uuid
from django.db import models
from users.models import User


class Announcement(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False
         )
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.FileField(upload_to="img/announcement", null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    