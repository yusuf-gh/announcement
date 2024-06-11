from django.db import models

class Section2(models.Model):
    title = models.TextField(blank=True)
    img = models.FileField(upload_to="img/announcement", null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
