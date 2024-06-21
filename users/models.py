from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date

class User(models.Model):
    id = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999999)],
        help_text="Введите свой ID в ручную",
        primary_key=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    contact = models.CharField(max_length=13, null=True, blank=True, help_text="+998...")
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    
    def __str__(self):
        return self.username
    
    def age(self):
        if self.date_of_birth is None:
            return None
        today = date.today()
        age = today.year - self.date_of_birth.year
        
        if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
            
        return age
