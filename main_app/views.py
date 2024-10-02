from django.shortcuts import render
from .models import Character
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Import HttpResponse to send text-based responses

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def character_index(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', {'characters': characters})

def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    return render(request, 'characters/detail.html', {'character': character})

    

class CharacterCreate(CreateView):
    model = Character
    fields = '__all__'

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['age', 'description']
    

class CharacterDelete(DeleteView):
    model = Character
    success_url='/characters/'