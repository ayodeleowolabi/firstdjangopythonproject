from django.db import models
from django.urls import reverse

class Character(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(max_length=250)


    def __str__(self):
        return f' {self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse("character-detail", kwargs={"character_id": self.id})
    

    
    
