from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(max_length=250)


    def __str__(self):
        return f' {self.name} ({self.id})'

    
    
