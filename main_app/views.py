from django.shortcuts import render
from django.shortcuts import HttpResponse


class Character:
    def __init__(self, name, description, age):
        self.name = name,
        self.description = description,
        self.age = age
        
characters = [
    Character('Mario', 'Red and blue', 47),
    Character('Luigi', 'Green', 43),
    Character('Princess Peach', 'Pink', 23),
    Character('Toad', 'Blue and Brown', 34),
    Character('Bowser', 'Brown', 47),
    Character('Donkey', 'Brown', 17)
    ]


# Import HttpResponse to send text-based responses

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def character_index(request):
    return render(request,'characters/index.html', {'characters':characters})