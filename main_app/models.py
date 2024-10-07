from django.db import models
from django.urls import reverse

POWERUPS = (
    ('M', 'Mushrooms'),
    ('S', 'Shell'),
    ('F', 'Flower'),
    ('C', 'Carrot')
)

class Character(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(max_length=250)


    def __str__(self):
        return f' {self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse("character-detail", kwargs={"character_id": self.id})
    
    
class GameSession(models.Model):
    date = models.DateField('Game Date')
    power_up = models.CharField(
        max_length=2,
        choices=POWERUPS,
        default=POWERUPS[0][0]
        )
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_power_up_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    
    

    
    
