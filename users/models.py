from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        help_text="Введите свой ID в ручную",
        primary_key=True
    )
    username = models.CharField(max_length=50, null=True, blank=True)
    contact = models.CharField(max_length=13, null=True, blank=True, help_text="+998...")
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
